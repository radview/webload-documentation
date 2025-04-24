# REST API Reference

The Dashboard can be controlled using API. The backend server controls session-data, resources and Analytics.
can be called on `http://localhost:8080/api`, see below the API documentation.

The Front-end API controls load-tests, users, organizations, and is accessible on `http://localhost:3000` or `https://saas.radview.com` for SaaS users. 
See [Front-end API documentation](./grafana/http_api/index.md). To access it, you will need [API Key](./managing_organizations.md#managing-api-keys)

See scripts that uses these APIs to start tests and generate reports:

- [Python script](./grafana/http_api/sample_api_python.md)
- [Groovy script](./grafana/http_api/sample_api_groovy.md)

<swagger-ui src="swagger.json"/>