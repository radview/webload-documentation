# Sample API Usage using Groovy

The below is a sample Groovy script that starts a load-test in the Dashboard and generate an Analytics report.

Can be used in local installation and in SaaS installations.
You will need:

- Authorization Key - for local installtion, using an Admin user, go to user menu, API Keys and create an 'Editor' key. For SaaS, ask RadView Support.
- orgId - the Organization ID - default is 1, if using more than one organization see the ID in the Admin - Global Orgs menu. For SaaS, ask RadView Support.
- docRoot - entry point. For SaaS this is `http://saas.radview.com`, for local it's `http://localhost:3000` or where your Dashboard is installed.
- datasourceEndPoint - location for datasource. For direct, local, API calls, this can be `http://localhost:8080/api`. For proxied local calls it will be `http://localhost:3000/api/datasources/proxy/1/` with the appropriate datasource id. For SaaS, ask RadView support.

```groovy
import groovy.json.JsonSlurper

/*
 * //Example of using it:
 * auth_key = "eyJrI....."
 * orgId = "186"
 * docRoot ="http://saas.radview.com"
 * datasourceEndpoint = "https://saas.radview.com/api/datasources/proxy/190"
 *
 * //Run test by it's name, get the create session id:
 * def sessionId =  runTestByName ( "My Test");
 *
 * //Wait for a session to finish running:
 * waitSessionEnd(sessionId);
 *
 * //Run Analytics report for the session:
 * saveAnalyticsReport([sessionId], "c:\\temp\\summary.pdf", "Performance Summary");
 *
 * //Run Analytics report to compare to a base line session
 * def baselineSessionId=3;
 * saveAnalyticsReport([sessionId, baselineSessionId], "c:\\temp\\comparison.pdf", null, "Session Comparison Portfolio");
 */

def getTestId(testName) {
    def encTestName = URLEncoder.encode(testName, "UTF-8")
    def findTestUrl = "$docRoot/api/loadtest/search?query=$encTestName"
    def testData = getData(findTestUrl);
    def jsonSlurper = new JsonSlurper()
    def tests = jsonSlurper.parseText(testData)
    //println tests
    def loadtest = tests.loadtests.find { it.Name == testName}
    //println loadtest
    if (loadtest) {
        return loadtest.Id
    } else {
        throw new RuntimeException("test '$testName' not found")
    }
}


def waitSessionEnd(sessionId) {
    while(true) {
        def sessionObj = getSession(sessionId);
        if (sessionObj.returnCode!="Running") {
            println("Session over - $sessionObj.returnCode");
            return true;
        }
        sleep(30000);
        println("waiting for session to end...");
    }
}

def saveAnalyticsReport(List sessionList, String outfileName, template=null, portfolio=null, reportFormat=null, reportName=null) {
    //http://localhost:8080/api/analytics?sessionid=3&portfolio=Summary%20Portfolio&format=PDF&param=TIME_FILTER_FROM_BEGINNING%3D180&name=Report

    def url  = datasourceEndpoint + "/analytics?";
    sessionList.each {sessionId ->
        url += "&sessionid=" + URLEncoder.encode(String.valueOf(sessionId), "UTF-8");
    }
    if (template != null) url += "&template=" + URLEncoder.encode(template, "UTF-8");
    if (portfolio != null) url += "&portfolio=" + URLEncoder.encode(portfolio, "UTF-8");
    if (reportFormat != null) url += "&format=" + URLEncoder.encode(reportFormat, "UTF-8");
    if (reportName != null) url += "&name=" + URLEncoder.encode(reportName, "UTF-8");

    def get = new URL(url).openConnection()
    def getRC
    get.addRequestProperty("Authorization", "Bearer $auth_key")
    get.addRequestProperty("X-Grafana-Org-Id", orgId)
    getRC = get.getResponseCode()
    if (getRC != 200) {
        throw new Exception("HTTP Error $getRC, while getting $url")
    }
    def response =get.getInputStream().getBytes();
    def outFile = new File(outfileName).withOutputStream { stream -> stream.write(response)};
    println ("saved report to $outfileName");
}

/**
 * @param testName to start running
 * @return sessionId of created session
 * @throws Error if could not start, or if waiting for sessionId timedout
 */
def runTestByName(testName) {
    def previousSessionId = getLatestSessionId(testName)
    def testId = getTestId(testName)
    def timeoutMillis = 5*60*1000 //5 minutes
    runTestById(testId)
    def startTime = System.currentTimeMillis()
    while(true) {
        def sessionId = getLatestSessionId(testName)
        if (sessionId != previousSessionId) {
            println "test started. session id: $sessionId";
            return sessionId
        }
        println "waiting for test session id..."
        def runningTime = System.currentTimeMillis() - startTime
        if (runningTime > timeoutMillis  ) {
            throw new RuntimeException("Timeout waiting for session id, test may have started")
        }
        sleep(5000)
    }
}

def getSession(sessionId) {
    return getJsonData("$datasourceEndpoint/session/$sessionId")
}

def runTestById(testId) {
    def startResult = getData("$docRoot/api/loadtest/$testId/start")
    def jsonSlurper = new JsonSlurper()
    def resultObj = jsonSlurper.parseText(startResult)
    def resultMessage = resultObj.message
    //println resultMessage
    println "Start test result: $resultMessage"
    return resultMessage
}

def getLatestSessionId(testName) {
    def sessionData = getData(datasourceEndpoint + "/session/findSessions?timeRange=Last%20Day")
    def jsonSlurper = new JsonSlurper()
    def sessions = jsonSlurper.parseText(sessionData)
    def lastSession = sessions.find { it.testDescription == testName}
    if (lastSession) {
        return lastSession.sessionId
    } else {
        return -1
    }
}

def getData(url) {
    def get = new URL(url).openConnection()
    def getRC
    get.addRequestProperty("Authorization", "Bearer $auth_key")
    get.addRequestProperty("X-Grafana-Org-Id", orgId)
    getRC = get.getResponseCode()
    if (getRC != 200) {
        throw new Exception("HTTP Error $getRC, while getting $url")
    }
    def response =get.getInputStream().getText()
    return response
}

def getJsonData(url) {
    def jsonSlurper = new JsonSlurper()
    return jsonSlurper.parseText(getData(url))
}
```