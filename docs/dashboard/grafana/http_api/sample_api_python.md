# Sample API Usage using Python

The below is a sample Groovy script that starts a load-test in the Dashboard and generate an Analytics report.

Can be used in local installation and in SaaS installations.
You will need:

- Authorization Key - for local installtion, using an Admin user, go to user menu, API Keys and create an 'Editor' key. For SaaS, ask RadView Support.
- orgId - the Organization ID - default is 1, if using more than one organization see the ID in the Admin - Global Orgs menu. For SaaS, ask RadView Support.
- docRoot - entry point. For SaaS this is `http://saas.radview.com`, for local it's `http://localhost:3000` or where your Dashboard is installed.
- datasourceEndPoint - location for datasource. For direct, local, API calls, this can be `http://localhost:8080/api`. For proxied local calls it will be `http://localhost:3000/api/datasources/proxy/1/` with the appropriate datasource id. For SaaS, ask RadView support.

```python
import requests
import time
import urllib.parse
import json

#Auth-key - create in Dashboard API Keys menu or ask from support for SaaS
auth_key = "eyJrIj...." 
orgId = "1"
docRoot = "http://localhost:3000/" 
datasourceEndpoint = "http://localhost:3000/api/datasources/proxy/1"


# Example of usage
if __name__ == "__main__":
    session_id = run_test_by_name("my test name")
    wait_session_end(session_id)
    save_analytics_report([session_id], "summary.pdf", "Performance Summary")

def get_test_id(test_name):
    enc_test_name = urllib.parse.quote(test_name)
    find_test_url = f"{docRoot}/api/loadtest/search?query={enc_test_name}"
    test_data = get_data(find_test_url)
    tests = json.loads(test_data)
    loadtest = next((lt for lt in tests["loadtests"] if lt["Name"] == test_name), None)

    if loadtest:
        return loadtest["Id"]
    else:
        raise RuntimeError(f"Test '{test_name}' not found")


def wait_session_end(session_id):
    while True:
        session_obj = get_session(session_id)
        if session_obj["returnCode"] != "Running":
            print(f"Session over - {session_obj['returnCode']}")
            return True
        print(f"Waiting for session {session_id} to end...")
        time.sleep(30)  # Sleep for 30 seconds


def save_analytics_report(session_list, outfile_name, template=None, portfolio=None, report_format=None,
                          report_name=None):
    url = f"{datasourceEndpoint}/analytics?"

    for session_id in session_list:
        url += f"&sessionid={urllib.parse.quote(str(session_id))}"

    if template:
        url += f"&template={urllib.parse.quote(template)}"
    if portfolio:
        url += f"&portfolio={urllib.parse.quote(portfolio)}"
    if report_format:
        url += f"&format={urllib.parse.quote(report_format)}"
    if report_name:
        url += f"&name={urllib.parse.quote(report_name)}"

    headers = {
        "Authorization": f"Bearer {auth_key}",
        "X-Grafana-Org-Id": orgId
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"HTTP Error {response.status_code} while getting {url}")

    with open(outfile_name, 'wb') as outfile:
        outfile.write(response.content)

    print(f"Saved report to {outfile_name}")


def run_test_by_name(test_name):
    previous_session_id = get_latest_session_id(test_name)
    test_id = get_test_id(test_name)
    timeout_millis = 5 * 60 * 1000  # 5 minutes
    run_test_by_id(test_id)

    start_time = time.time()
    while True:
        session_id = get_latest_session_id(test_name)
        if session_id != previous_session_id:
            print(f"Test started. Session id: {session_id}")
            return session_id

        print("Waiting for test session id...")
        running_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        if running_time > timeout_millis:
            raise RuntimeError("Timeout waiting for session id, test may have started")

        time.sleep(5)  # Sleep for 5 seconds


def get_session(session_id):
    session_url = f"{datasourceEndpoint}/session/{session_id}"
    session_data = get_data(session_url)
    return json.loads(session_data)


def run_test_by_id(test_id):
    start_url = f"{docRoot}/api/loadtest/{test_id}/start"
    start_result = get_data(start_url)
    result_obj = json.loads(start_result)
    print(f"Start test result: {result_obj['message']}")
    return result_obj["message"]


def get_latest_session_id(test_name):
    session_url = f"{datasourceEndpoint}/session/findSessions?timeRange=Last%20Day"
    session_data = get_data(session_url)
    sessions = json.loads(session_data)
    last_session = next((s for s in sessions if s["testDescription"] == test_name), None)
    if last_session:
        return last_session["sessionId"]
    else:
        return -1


def get_data(url):
    headers = {
        "Authorization": f"Bearer {auth_key}",
        "X-Grafana-Org-Id": orgId
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"HTTP Error {response.status_code} while getting {url}")

    return response.text
```
