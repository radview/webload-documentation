# Loadtest API

Below are all the API endpoints for managing loadtest. Unless otherwise noted, all requests must include appropriate authentication headers (for example, a Bearer token).

## Get all loadtests

Retrieve a paginated list of all loadtests.  
Supports an optional search query, along with `page` and `perpage` parameters.

GET /api/loadtest

***Query Parameters***

- **query** (optional): Filter results by matching loadtest name.  
- **page** (optional): Page number to return (default: `1`).  
- **perpage** (optional): Number of items per page (default: `1000`).

***Example Request***

``` javascript
GET /api/loadtest?query=staging&page=1&perpage=20 HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json
{
    "orgId": 0,
    "totalCount": 13,
    "loadtests": [
        {
            "Id": 23,
            "OrgId": 1,
            "Version": 0,
            "Name": "some url",
            "Path": "http://www.httpbin.org",
            "State": " ",
            "Schedule": "Not Scheduled",
            "ScheduleOverride": 2,
            "NextExec": "0000-12-31T19:00:00-05:00",
            "DatasourceId": 1,
            "Location": "America/New_York",
            "Data": {
                "LGRegions": [
                    {
                        "distribution": 100,
                        "name": "LocalHost"
                    }
                ],
                "TestType": 3,
                "datasourceName": "webload",
                "detailedSchedule": {
                    "Duration": 1,
                    "MaxVC": 1,
                    "RampDownTime": 0,
                    "RampUpTime": 0,
                    "Rounds": 0
                },
                "execoptions": [],
                "is_specific": true,
                "loadGenerators": [],
                "name": "some url",
                "path": "http://www.httpbin.org",
                "schedule": "Not Scheduled",
                "sleep": 1000,
                "url": "http://www.httpbin.org",
                "urls": [
                    {
                        "body": "formdata",
                        "display": 0,
                        "formdata": [],
                        "headers": [],
                        "method": "Get",
                        "requestbody": "",
                        "url": "http://www.httpbin.org"
                    }
                ]
            },
            "TestType": 3,
            "Created": "2024-10-03T13:52:52-04:00",
            "Updated": "2024-10-03T13:53:03-04:00"
    }  
    ]
}
```

## Add a standard loadtest (by data source ID)

Creates a new standard (script-based) loadtest by **datasourceId**.

POST /api/loadtest/byDatasourceId

***Request Body***

| Field             | Type   | Description                                               |
|-------------------|--------|-----------------------------------------------------------|
| `name`            | string | Loadtest name                                            |
| `datasourceId`    | number | Existing data source ID                                  |
| `path`            | string | Path to the loadtest script or file                      |
| `state`           | string | Initial state (leave blank)                |
| `schedule`        | string | Cron schedule or scheduling definition                   |
| `location`        | string | Timezone for schedule, e.g "America/New_York" (optional)                    |
| `testType`        | number | 1 = URL test, 2 = agenda test, 3 = template test              |
| `nextExec`        | string | Next execution time (ISO 8601) (optional)               |
| `scheduleOverride`| number | 0 = none, 1 = run now, etc.                              |
| `data`            | object | Additional loadtest data (JSON object)                   |

***Example Request***

```text
POST /api/loadtest/byDatasourceId HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>

{ "name": "staging_test", "datasourceId": 1, "path": "/tests/staging.js", "state": "idle", "schedule": "0 */2 * * *", "location": "us-east", "testType": 1, "scheduleOverride": 0, "data": { "spawncount": 50 } }
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "message": "loadtest added", "id": 5, "name": "staging_test" }
```


## Add a standard loadtest (by data source **name**)

Creates a new standard loadtest, but references the data source by its **name** instead of **id**.

POST /api/loadtest

***Request Body***

| Field      | Type   | Description                                                             |
|------------|--------|-------------------------------------------------------------------------|
| `name`     | string | Loadtest name                                                            |
| `path`     | string | Path to the loadtest script                                              |
| `state`    | string | Initial state (e.g., "idle", "scheduled")                                |
| `schedule` | string | Cron schedule or scheduling definition                                   |
| `location` | string | Geographic/runner location (optional)                                    |
| `data`     | object | Additional loadtest data (JSON object)                                   |

> **Note:** This endpoint also requires the data source name in the URL route.

***Example Request***

```text
POST /api/loadtest?DatasourceName=mydatasource HTTP/1.1 
Accept: application/json 
Content-Type: application/json Authorization: 
Bearer <YOUR_API_TOKEN>

{ "name": "my_loadtest", "path": "/tests/my_loadtest.js", "state": "idle", "schedule": "0 1 * * *", "location": "us-east", "data": { "spawncount": 100 } }
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "message": "loadtest added", "id": 6, "name": "my_loadtest" }
```

## Add an agenda-based loadtest

Creates a new **agenda-based** loadtest (testType = 2) using a data source name.

POST /api/loadtest/agenda

***Request Body***

| Field      | Type   | Description                                                      |
|------------|--------|------------------------------------------------------------------|
| `name`     | string | Loadtest name                                                   |
| `path`     | string | Path or reference to the agenda driver                           |
| `state`    | string | Initial state (e.g., "idle", "scheduled")                       |
| `schedule` | string | Cron schedule or scheduling definition                          |
| `location` | string | Geographic/runner location (optional)                           |
| `data`     | object | Additional loadtest data (JSON object)                          |

> Must specify the data source **name** in the query (as `:DatasourceName`).  
> This sets `testType` to `2` internally.

***Example Request***

```text
POST /api/loadtest/agenda?DatasourceName=mydatasource HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>

{ "name": "agenda_demo", "path": "/tests/agenda_runner.js", "state": "idle", "schedule": "0 3 * * *", "location": "us-east", "data": { "spawncount": 20, "agendaPath": "/agendas/demo_agenda.json", "agendas": [ { "agendaname": "step1", "agendapath": "/agendas/step1.js", "percentage": 50, "execoptions": [ { "Name": "timeout", "Value": "30" } ], "sleepoptions": {} } ] } }
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "message": "loadtest added", "id": 10, "name": "agenda_demo" }
```

## Add a URL-based loadtest

Creates a new **URL-based** loadtest (testType = 3) using a data source name.

POST /api/loadtest/url


***Request Body***

| Field      | Type   | Description                                                             |
|------------|--------|-------------------------------------------------------------------------|
| `name`     | string | Loadtest name                                                            |
| `path`     | string | Some path or descriptor for the test (optional)                          |
| `state`    | string | Initial state (e.g., "idle", "scheduled")                                |
| `schedule` | string | Cron schedule or scheduling definition                                   |
| `location` | string | Geographic/runner location (optional)                                    |
| `data`     | object | Additional loadtest data (JSON object)                                   |

> This sets `testType = 3` internally. For example, can store multiple URLs, request methods, headers, etc.

***Example Request***

```text
POST /api/loadtest/url?DatasourceName=mydatasource HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>

{ "name": "url_test_example", "path": "/urls/url_test_example", "state": "idle", "schedule": "0 4 * * *", "data": { "spawncount": 30, "url": "https://example.com", "urls": [ { "url": "https://example.com/login", "method": "POST", "requestbody": "{}", "headers": [ {"Name": "Content-Type", "Value": "application/json"} ], "formdata": [] } ] } }
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "message": "loadtest added", "id": 11, "name": "url_test_example" }
```

## Get a single loadtest by ID

Retrieve a single loadtest, given its numeric ID.

GET /api/loadtest/:id

***Example Request***

GET /api/loadtest/10 HTTP/1.1 Accept: application/json Content-Type: application/json Authorization: Bearer <YOUR_API_TOKEN>

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "id": 10, "orgId": 1, "name": "agenda_demo", "path": "/tests/agenda_runner.js", "schedule": "0 3 * * *", "scheduleOverride": 0, "nextExec": "2025-04-22T03:00:00Z", "state": "idle", "datasourceId": 1, "location": "us-east", "data": { "spawncount": 20, "agendaPath": "/agendas/demo_agenda.json", ... }, "testType": 2 }
```

## Get a single **agenda** loadtest by ID

Similar to above, but if you specifically know the test was created as `testType = 2` (agenda-based), you can use:

GET /api/loadtest/agenda/:id

This returns the same kind of object but often includes extra fields like `agendaPath`, `agendas`, `detailedSchedule`, etc.

***Example Request***

```text
GET /api/loadtest/agenda/10 HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "id": 10, "orgId": 1, "name": "agenda_demo", "path": "/tests/agenda_runner.js", "schedule": "0 3 * * *", "scheduleOverride": 0, "nextExec": "2025-04-22T03:00:00Z", "state": "idle", "datasourceId": 1, "location": "us-east", "agendaPath": "/agendas/demo_agenda.json", "spawnCount": 20, "detailedSchedule": { "rampUpTime": 60, "duration": 300, "rampDownTime": 60, "maxVC": 100, "limitRounds": false }, "agendas": [ { "agendaname": "step1", "agendapath": "/agendas/step1.js", "percentage": 50, "execoptions": [ { "Name": "timeout", "Value": "30" } ], "sleepoptions": {} } ], "testType": 2, "data": { ... } }
```

## Get a single **URL-based** loadtest by ID

GET /api/loadtest/url/:id

Returns extended URL-based test details if `testType = 3`.

***Example Request***

```text
GET /api/loadtest/url/11 HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "id": 11, "orgId": 1, "name": "url_test_example", "path": "/urls/url_test_example", "schedule": "0 4 * * *", "scheduleOverride": 0, "nextExec": "2025-04-22T04:00:00Z", "state": "idle", "datasourceId": 1, "location": "us-east", "url": "https://example.com", "urls": [ { "url": "https://example.com/login", "method": "POST", "requestbody": "{}", "headers": [ { "Name": "Content-Type", "Value": "application/json" } ], "formdata": [] } ], "spawnCount": 30, "testType": 3, "data": { ... } }
```

## Update a loadtest

Updates an existing loadtest by ID.

PUT /api/loadtest/:id

***Request Body***

Similar to the **Add** loadtest body, but includes any fields that require updating.

| Field             | Type   | Description                                                |
|-------------------|--------|------------------------------------------------------------|
| `name`            | string | Loadtest name                                             |
| `path`            | string | Script path or relevant file path                         |
| `state`           | string | Loadtest state                                            |
| `schedule`        | string | Cron schedule or scheduling definition                    |
| `location`        | string | Geographic/runner location (optional)                     |
| `scheduleOverride`| number | 0 = none, 1 = run now, etc.                               |
| `data`            | object | JSON object with details (e.g., spawncount, URL list, etc.)|

***Example Request***

```
PUT /api/loadtest/5 HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>

{ "name": "staging_test_updated", "path": "/tests/new_staging.js", "schedule": "0 */4 * * *", "scheduleOverride": 1, "data": { "spawncount": 80 } }
```

***Example Response***

```
HTTP/1.1 200 
Content-Type: application/json

{ "message": "loadtest updated", "id": 5, "name": "staging_test_updated" }
```

## Delete a loadtest by ID

Removes a loadtest by its ID.

DELETE /api/loadtest/:id

***Example Request***

```
DELETE /api/loadtest/10 HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>
```

***Example Response***

```
HTTP/1.1 200 
Content-Type: application/json

{ "message": "load test deleted" }
```

## Delete a loadtest by name

Removes a loadtest by its name.

DELETE /api/loadtest/name/:name

***Example Request***

```
DELETE /api/loadtest/name/prod_loadtest HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "message": "loadtest was deleted" }

```

## Start a loadtest by ID

Forces a loadtest to start immediately by updating its `state` and next execution.

GET /api/loadtest/:id/start


***Example Request***

GET /api/loadtest/10/start HTTP/1.1 Accept: application/json Content-Type: application/json Authorization: Bearer <YOUR_API_TOKEN>


***Example Response***

HTTP/1.1 200 Content-Type: application/json

{ "message": "loadtest started", "id": 10, "name": "agenda_demo" }


## Get a loadtest by name

Retrieves a single loadtest by its unique name.

GET /api/loadtest/name/:name

***Example Request***

```text
GET /api/loadtest/name/staging_test HTTP/1.1 
Accept: application/json 
Content-Type: application/json 
Authorization: Bearer <YOUR_API_TOKEN>
```

***Example Response***

```text
HTTP/1.1 200 
Content-Type: application/json

{ "id": 5, "orgId": 1, "name": "staging_test", "path": "/tests/staging.js", "schedule": "0 */2 * * *", "scheduleOverride": 0, "nextExec": "2025-04-22T02:00:00Z", "state": "scheduled", "datasourceId": 1, "location": "us-east", "data": { ... }, "testType": 1 }
```

**NOTE**: The request and response bodies above are representative examples; actual fields (especially within `data`) can vary depending on the testType and extended settings. Always ensure you include the required headers and valid JSON structures in your requests.
