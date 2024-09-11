# oxide.MetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**silo_metric**](MetricsApi.md#silo_metric) | **GET** /v1/metrics/{metric_name} | View metrics
[**timeseries_query**](MetricsApi.md#timeseries_query) | **POST** /v1/timeseries/query | Run timeseries query
[**timeseries_schema_list**](MetricsApi.md#timeseries_schema_list) | **GET** /v1/timeseries/schema | List timeseries schemas


# **silo_metric**
> MeasurementResultsPage silo_metric(metric_name, end_time=end_time, limit=limit, order=order, page_token=page_token, start_time=start_time, project=project)

View metrics

View CPU, memory, or storage utilization metrics at the silo or project level.

### Example


```python
import oxide
from oxide.models.measurement_results_page import MeasurementResultsPage
from oxide.models.pagination_order import PaginationOrder
from oxide.models.system_metric_name import SystemMetricName
from oxide.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = oxide.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with oxide.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oxide.MetricsApi(api_client)
    metric_name = oxide.SystemMetricName() # SystemMetricName | 
    end_time = '2013-10-20T19:20:30+01:00' # datetime | An exclusive end time of metrics. (optional)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    order = oxide.PaginationOrder() # PaginationOrder | Query result order (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | An inclusive start time of metrics. (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # View metrics
        api_response = api_instance.silo_metric(metric_name, end_time=end_time, limit=limit, order=order, page_token=page_token, start_time=start_time, project=project)
        print("The response of MetricsApi->silo_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->silo_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | [**SystemMetricName**](.md)|  | 
 **end_time** | **datetime**| An exclusive end time of metrics. | [optional] 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **order** | [**PaginationOrder**](.md)| Query result order | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **start_time** | **datetime**| An inclusive start time of metrics. | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**MeasurementResultsPage**](MeasurementResultsPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries_query**
> OxqlQueryResult timeseries_query(timeseries_query)

Run timeseries query

Queries are written in OxQL.

### Example


```python
import oxide
from oxide.models.oxql_query_result import OxqlQueryResult
from oxide.models.timeseries_query import TimeseriesQuery
from oxide.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = oxide.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with oxide.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oxide.MetricsApi(api_client)
    timeseries_query = oxide.TimeseriesQuery() # TimeseriesQuery | 

    try:
        # Run timeseries query
        api_response = api_instance.timeseries_query(timeseries_query)
        print("The response of MetricsApi->timeseries_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->timeseries_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeseries_query** | [**TimeseriesQuery**](TimeseriesQuery.md)|  | 

### Return type

[**OxqlQueryResult**](OxqlQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries_schema_list**
> TimeseriesSchemaResultsPage timeseries_schema_list(limit=limit, page_token=page_token)

List timeseries schemas

### Example


```python
import oxide
from oxide.models.timeseries_schema_results_page import TimeseriesSchemaResultsPage
from oxide.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = oxide.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with oxide.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oxide.MetricsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)

    try:
        # List timeseries schemas
        api_response = api_instance.timeseries_schema_list(limit=limit, page_token=page_token)
        print("The response of MetricsApi->timeseries_schema_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->timeseries_schema_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 

### Return type

[**TimeseriesSchemaResultsPage**](TimeseriesSchemaResultsPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

