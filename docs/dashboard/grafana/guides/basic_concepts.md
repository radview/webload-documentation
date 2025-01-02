# Basic Concepts

This document is a “bottom up” introduction to basic concepts in Grafana, and can be used as a starting point to get familiar with core features.

### Data Source

Grafana supports many different storage backends for your time series data (Data Source). Each Data Source has a specific Query Editor that is customized for the features and capabilities that the particular Data Source exposes.

The following datasources are officially supported: [Graphite](../features/datasources/graphite.md), [InfluxDB](../features/datasources/influxdb.md), [OpenTSDB](../features/datasources/opentsdb.md), [Prometheus](../features/datasources/prometheus.md), [Elasticsearch](../features/datasources/elasticsearch.md), [CloudWatch](../features/datasources/cloudwatch.md).

The query language and capabilities of each Data Source are obviously very different. You can combine data from multiple Data Sources onto a single Dashboard, but each Panel is tied to a specific Data Source that belongs to a particular Organization.

### Organization

Grafana supports multiple organizations in order to support a wide variety of deployment models, including using a single Grafana instance to provide service to multiple potentially untrusted Organizations.

In many cases, Grafana will be deployed with a single Organization.

Each Organization can have one or more Data Sources.

All Dashboards are owned by a particular Organization.

 > Note: It is important to remember that most metric databases do not provide any sort of per-user series authentication. Therefore, in Grafana, Data Sources and Dashboards are available to all Users in a particular Organization.

For more details on the user model for Grafana, please refer to [Admin](../reference/admin.md)

### User

A User is a named account in Grafana. A user can belong to one or more Organizations, and can be assigned different levels of privileges through roles.

Grafana supports a wide variety of internal and external ways for Users to authenticate themselves. These include from its own integrated database, from an external SQL server, or from an external LDAP server.

For more details please refer to [User Auth](../http_api/auth.md)

### Row

A Row is a logical divider within a Dashboard, and is used to group Panels together.

Rows are always 12 “units” wide. These units are automatically scaled dependent on the horizontal resolution of your browser. You can control the relative width of Panels within a row by setting their own width.

We utilize a unit abstraction so that Grafana looks great on all screens both small and huge.

 > Note: With MaxDataPoint functionality, Grafana can show you the perfect amount of datapoints no matter your resolution or time-range.

Utilize the [Repeating Row functionality](../reference/templating.md#templating) to dynamically create or remove entire Rows (that can be filled with Panels), based on the Template variables selected.

Rows can be collapsed by clicking on the Row Title. If you save a Dashboard with a Row collapsed, it will save in that state and will not preload those graphs until the row is expanded.

### Panel

The Panel is the basic visualization building block in Grafana. Each Panel provides a Query Editor (dependent on the Data Source selected in the panel) that allows you to extract the perfect visualization to display on the Panel by utilizing the Query Editor

There are a wide variety of styling and formatting options that each Panel exposes to allow you to create the perfect picture.

Panels can be dragged and dropped and rearranged on the Dashboard. They can also be resized.

There are currently four Panel types: [Graph](../features/panels/graph.md), [Singlestat](../features/panels/singlestat.md), [Dashlist](../features/panels//dashlist.md), [Table](../features/panels/table_panel.md),and [Text]().

Panels like the [Graph](../features/panels/graph.md) panel allow you to graph as many metrics and series as you want. Other panels like [Singlestat](../features/panels/singlestat.md) require a reduction of a single query into a single number. [Dashlist](../features/panels/dashlist.md) and Text are special panels that do not connect to any Data Source.

Panels can be made more dynamic by utilizing [Dashboard Templating](../reference/templating.md) variable strings within the panel configuration (including queries to your Data Source configured via the Query Editor).

Utilize the [Repeating Panel](../reference/templating.md#repeating-panels-and-repeating-rows) functionality to dynamically create or remove Panels based on the [Templating Variables](../reference/templating.md#templating) selected.

The time range on Panels is normally what is set in the [Dashboard time picker](../reference/timerange.md) but this can be overridden by utilizes [Panel specific time overrides](../reference/timerange.md#panel-time-overrides-timeshift).

Panels (or an entire Dashboard) can be [Shared](../reference/sharing.md) easily in a variety of ways. You can send a link to someone who has a login to your Grafana. You can use the [Snapshot](../reference/sharing.md#share-dashboard) feature to encode all the data currently being viewed into a static and interactive JSON document; it's so much better than emailing a screenshot!


### Query Editor

The Query Editor exposes capabilities of your Data Source and allows you to query the metrics that it contains.

Use the Query Editor to build one or more queries (for one or more series) in your time series database. The panel will instantly update allowing you to effectively explore your data in real time and build a perfect query for that particular Panel.

You can utilize [Template variables](../reference/templating.md) in the Query Editor within the queries themselves. This provides a powerful way to explore data dynamically based on the Templating variables selected on the Dashboard.

Grafana allows you to reference queries in the Query Editor by the row that they’re on. If you add a second query to graph, you can reference the first query simply by typing in #A. This provides an easy and convenient way to build compounded queries.

### Dashboard

The Dashboard is where it all comes together. Dashboards can be thought of as of a set of one or more Panels organized and arranged into one or more Rows.

The time period for the Dashboard can be controlled by the [Dashboard time picker](../reference/timerange.md) in the upper right of the Dashboard.

Dashboards can utilize [Templating](../reference/templating.md) to make them more dynamic and interactive.

Dashboards can utilize [Annotations](../reference/annotations.md) to display event data across Panels. This can help correlate the time series data in the Panel with other events.

Dashboards (or a specific Panel) can be [Shared](../reference/sharing.md) easily in a variety of ways. You can send a link to someone who has a login to your Grafana. You can use the [Snapshot](../reference/sharing.md#dashboard-snapshot) feature to encode all the data currently being viewed into a static and interactive JSON document; it's so much better than emailing a screenshot!

Dashboards can be tagged, and the Dashboard picker provides quick, searchable access to all Dashboards in a particular Organization.
