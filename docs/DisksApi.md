# oxide.DisksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disk_bulk_write_import**](DisksApi.md#disk_bulk_write_import) | **POST** /v1/disks/{disk}/bulk-write | Import blocks into disk
[**disk_bulk_write_import_start**](DisksApi.md#disk_bulk_write_import_start) | **POST** /v1/disks/{disk}/bulk-write-start | Start importing blocks into disk
[**disk_bulk_write_import_stop**](DisksApi.md#disk_bulk_write_import_stop) | **POST** /v1/disks/{disk}/bulk-write-stop | Stop importing blocks into disk
[**disk_create**](DisksApi.md#disk_create) | **POST** /v1/disks | Create a disk
[**disk_delete**](DisksApi.md#disk_delete) | **DELETE** /v1/disks/{disk} | Delete disk
[**disk_finalize_import**](DisksApi.md#disk_finalize_import) | **POST** /v1/disks/{disk}/finalize | Confirm disk block import completion
[**disk_list**](DisksApi.md#disk_list) | **GET** /v1/disks | List disks
[**disk_metrics_list**](DisksApi.md#disk_metrics_list) | **GET** /v1/disks/{disk}/metrics/{metric} | Fetch disk metrics
[**disk_view**](DisksApi.md#disk_view) | **GET** /v1/disks/{disk} | Fetch disk


# **disk_bulk_write_import**
> disk_bulk_write_import(disk, import_blocks_bulk_write, project=project)

Import blocks into disk

### Example


```python
import oxide
from oxide.models.import_blocks_bulk_write import ImportBlocksBulkWrite
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
    api_instance = oxide.DisksApi(api_client)
    disk = oxide.NameOrId() # NameOrId | Name or ID of the disk
    import_blocks_bulk_write = oxide.ImportBlocksBulkWrite() # ImportBlocksBulkWrite | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Import blocks into disk
        api_instance.disk_bulk_write_import(disk, import_blocks_bulk_write, project=project)
    except Exception as e:
        print("Exception when calling DisksApi->disk_bulk_write_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk** | [**NameOrId**](.md)| Name or ID of the disk | 
 **import_blocks_bulk_write** | [**ImportBlocksBulkWrite**](ImportBlocksBulkWrite.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | resource updated |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_bulk_write_import_start**
> disk_bulk_write_import_start(disk, project=project)

Start importing blocks into disk

Start the process of importing blocks into a disk

### Example


```python
import oxide
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
    api_instance = oxide.DisksApi(api_client)
    disk = oxide.NameOrId() # NameOrId | Name or ID of the disk
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Start importing blocks into disk
        api_instance.disk_bulk_write_import_start(disk, project=project)
    except Exception as e:
        print("Exception when calling DisksApi->disk_bulk_write_import_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk** | [**NameOrId**](.md)| Name or ID of the disk | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | resource updated |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_bulk_write_import_stop**
> disk_bulk_write_import_stop(disk, project=project)

Stop importing blocks into disk

Stop the process of importing blocks into a disk

### Example


```python
import oxide
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
    api_instance = oxide.DisksApi(api_client)
    disk = oxide.NameOrId() # NameOrId | Name or ID of the disk
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Stop importing blocks into disk
        api_instance.disk_bulk_write_import_stop(disk, project=project)
    except Exception as e:
        print("Exception when calling DisksApi->disk_bulk_write_import_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk** | [**NameOrId**](.md)| Name or ID of the disk | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | resource updated |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_create**
> Disk disk_create(project, disk_create)

Create a disk

### Example


```python
import oxide
from oxide.models.disk import Disk
from oxide.models.disk_create import DiskCreate
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
    api_instance = oxide.DisksApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    disk_create = oxide.DiskCreate() # DiskCreate | 

    try:
        # Create a disk
        api_response = api_instance.disk_create(project, disk_create)
        print("The response of DisksApi->disk_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisksApi->disk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **disk_create** | [**DiskCreate**](DiskCreate.md)|  | 

### Return type

[**Disk**](Disk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful creation |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_delete**
> disk_delete(disk, project=project)

Delete disk

### Example


```python
import oxide
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
    api_instance = oxide.DisksApi(api_client)
    disk = oxide.NameOrId() # NameOrId | Name or ID of the disk
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Delete disk
        api_instance.disk_delete(disk, project=project)
    except Exception as e:
        print("Exception when calling DisksApi->disk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk** | [**NameOrId**](.md)| Name or ID of the disk | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful deletion |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_finalize_import**
> disk_finalize_import(disk, finalize_disk, project=project)

Confirm disk block import completion

### Example


```python
import oxide
from oxide.models.finalize_disk import FinalizeDisk
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
    api_instance = oxide.DisksApi(api_client)
    disk = oxide.NameOrId() # NameOrId | Name or ID of the disk
    finalize_disk = oxide.FinalizeDisk() # FinalizeDisk | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Confirm disk block import completion
        api_instance.disk_finalize_import(disk, finalize_disk, project=project)
    except Exception as e:
        print("Exception when calling DisksApi->disk_finalize_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk** | [**NameOrId**](.md)| Name or ID of the disk | 
 **finalize_disk** | [**FinalizeDisk**](FinalizeDisk.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | resource updated |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_list**
> DiskResultsPage disk_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List disks

### Example


```python
import oxide
from oxide.models.disk_results_page import DiskResultsPage
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
    api_instance = oxide.DisksApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List disks
        api_response = api_instance.disk_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of DisksApi->disk_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisksApi->disk_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**DiskResultsPage**](DiskResultsPage.md)

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

# **disk_metrics_list**
> MeasurementResultsPage disk_metrics_list(disk, metric, end_time=end_time, limit=limit, order=order, page_token=page_token, start_time=start_time, project=project)

Fetch disk metrics

### Example


```python
import oxide
from oxide.models.disk_metric_name import DiskMetricName
from oxide.models.measurement_results_page import MeasurementResultsPage
from oxide.models.pagination_order import PaginationOrder
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
    api_instance = oxide.DisksApi(api_client)
    disk = oxide.NameOrId() # NameOrId | 
    metric = oxide.DiskMetricName() # DiskMetricName | 
    end_time = '2013-10-20T19:20:30+01:00' # datetime | An exclusive end time of metrics. (optional)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    order = oxide.PaginationOrder() # PaginationOrder | Query result order (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | An inclusive start time of metrics. (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Fetch disk metrics
        api_response = api_instance.disk_metrics_list(disk, metric, end_time=end_time, limit=limit, order=order, page_token=page_token, start_time=start_time, project=project)
        print("The response of DisksApi->disk_metrics_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisksApi->disk_metrics_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk** | [**NameOrId**](.md)|  | 
 **metric** | [**DiskMetricName**](.md)|  | 
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

# **disk_view**
> Disk disk_view(disk, project=project)

Fetch disk

### Example


```python
import oxide
from oxide.models.disk import Disk
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
    api_instance = oxide.DisksApi(api_client)
    disk = oxide.NameOrId() # NameOrId | Name or ID of the disk
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Fetch disk
        api_response = api_instance.disk_view(disk, project=project)
        print("The response of DisksApi->disk_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisksApi->disk_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk** | [**NameOrId**](.md)| Name or ID of the disk | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Disk**](Disk.md)

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

