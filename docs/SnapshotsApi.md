# oxide.SnapshotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapshot_create**](SnapshotsApi.md#snapshot_create) | **POST** /v1/snapshots | Create snapshot
[**snapshot_delete**](SnapshotsApi.md#snapshot_delete) | **DELETE** /v1/snapshots/{snapshot} | Delete snapshot
[**snapshot_list**](SnapshotsApi.md#snapshot_list) | **GET** /v1/snapshots | List snapshots
[**snapshot_view**](SnapshotsApi.md#snapshot_view) | **GET** /v1/snapshots/{snapshot} | Fetch snapshot


# **snapshot_create**
> Snapshot snapshot_create(project, snapshot_create)

Create snapshot

Creates a point-in-time snapshot from a disk.

### Example


```python
import oxide
from oxide.models.snapshot import Snapshot
from oxide.models.snapshot_create import SnapshotCreate
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
    api_instance = oxide.SnapshotsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    snapshot_create = oxide.SnapshotCreate() # SnapshotCreate | 

    try:
        # Create snapshot
        api_response = api_instance.snapshot_create(project, snapshot_create)
        print("The response of SnapshotsApi->snapshot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->snapshot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **snapshot_create** | [**SnapshotCreate**](SnapshotCreate.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

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

# **snapshot_delete**
> snapshot_delete(snapshot, project=project)

Delete snapshot

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
    api_instance = oxide.SnapshotsApi(api_client)
    snapshot = oxide.NameOrId() # NameOrId | Name or ID of the snapshot
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Delete snapshot
        api_instance.snapshot_delete(snapshot, project=project)
    except Exception as e:
        print("Exception when calling SnapshotsApi->snapshot_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot** | [**NameOrId**](.md)| Name or ID of the snapshot | 
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

# **snapshot_list**
> SnapshotResultsPage snapshot_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List snapshots

### Example


```python
import oxide
from oxide.models.snapshot_results_page import SnapshotResultsPage
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
    api_instance = oxide.SnapshotsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List snapshots
        api_response = api_instance.snapshot_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of SnapshotsApi->snapshot_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->snapshot_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**SnapshotResultsPage**](SnapshotResultsPage.md)

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

# **snapshot_view**
> Snapshot snapshot_view(snapshot, project=project)

Fetch snapshot

### Example


```python
import oxide
from oxide.models.snapshot import Snapshot
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
    api_instance = oxide.SnapshotsApi(api_client)
    snapshot = oxide.NameOrId() # NameOrId | Name or ID of the snapshot
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Fetch snapshot
        api_response = api_instance.snapshot_view(snapshot, project=project)
        print("The response of SnapshotsApi->snapshot_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->snapshot_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot** | [**NameOrId**](.md)| Name or ID of the snapshot | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Snapshot**](Snapshot.md)

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

