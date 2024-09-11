# oxide.SystemMetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_metric**](SystemMetricsApi.md#system_metric) | **GET** /v1/system/metrics/{metric_name} | View metrics


# **system_metric**
> MeasurementResultsPage system_metric(metric_name, end_time=end_time, limit=limit, order=order, page_token=page_token, start_time=start_time, silo=silo)

View metrics

View CPU, memory, or storage utilization metrics at the fleet or silo level.

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
    api_instance = oxide.SystemMetricsApi(api_client)
    metric_name = oxide.SystemMetricName() # SystemMetricName | 
    end_time = '2013-10-20T19:20:30+01:00' # datetime | An exclusive end time of metrics. (optional)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    order = oxide.PaginationOrder() # PaginationOrder | Query result order (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | An inclusive start time of metrics. (optional)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo (optional)

    try:
        # View metrics
        api_response = api_instance.system_metric(metric_name, end_time=end_time, limit=limit, order=order, page_token=page_token, start_time=start_time, silo=silo)
        print("The response of SystemMetricsApi->system_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemMetricsApi->system_metric: %s\n" % e)
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
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | [optional] 

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

