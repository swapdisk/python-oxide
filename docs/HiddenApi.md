# oxide.HiddenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_access_token**](HiddenApi.md#device_access_token) | **POST** /device/token | Request a device access token
[**device_auth_confirm**](HiddenApi.md#device_auth_confirm) | **POST** /device/confirm | Confirm an OAuth 2.0 Device Authorization Grant
[**device_auth_request**](HiddenApi.md#device_auth_request) | **POST** /device/auth | Start an OAuth 2.0 Device Authorization Grant
[**logout**](HiddenApi.md#logout) | **POST** /v1/logout | Log user out of web console by deleting session on client and server
[**probe_create**](HiddenApi.md#probe_create) | **POST** /experimental/v1/probes | Create instrumentation probe
[**probe_delete**](HiddenApi.md#probe_delete) | **DELETE** /experimental/v1/probes/{probe} | Delete instrumentation probe
[**probe_list**](HiddenApi.md#probe_list) | **GET** /experimental/v1/probes | List instrumentation probes
[**probe_view**](HiddenApi.md#probe_view) | **GET** /experimental/v1/probes/{probe} | View instrumentation probe


# **device_access_token**
> object device_access_token(client_id, device_code, grant_type)

Request a device access token

This endpoint should be polled by the client until the user code is verified and the grant is confirmed.

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
    api_instance = oxide.HiddenApi(api_client)
    client_id = 'client_id_example' # str | 
    device_code = 'device_code_example' # str | 
    grant_type = 'grant_type_example' # str | 

    try:
        # Request a device access token
        api_response = api_instance.device_access_token(client_id, device_code, grant_type)
        print("The response of HiddenApi->device_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HiddenApi->device_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **device_code** | **str**|  | 
 **grant_type** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_auth_confirm**
> device_auth_confirm(device_auth_verify)

Confirm an OAuth 2.0 Device Authorization Grant

This endpoint is designed to be accessed by the user agent (browser), not the client requesting the token. So we do not actually return the token here; it will be returned in response to the poll on `/device/token`.

### Example


```python
import oxide
from oxide.models.device_auth_verify import DeviceAuthVerify
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
    api_instance = oxide.HiddenApi(api_client)
    device_auth_verify = oxide.DeviceAuthVerify() # DeviceAuthVerify | 

    try:
        # Confirm an OAuth 2.0 Device Authorization Grant
        api_instance.device_auth_confirm(device_auth_verify)
    except Exception as e:
        print("Exception when calling HiddenApi->device_auth_confirm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_auth_verify** | [**DeviceAuthVerify**](DeviceAuthVerify.md)|  | 

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

# **device_auth_request**
> object device_auth_request(client_id)

Start an OAuth 2.0 Device Authorization Grant

This endpoint is designed to be accessed from an *unauthenticated* API client. It generates and records a `device_code` and `user_code` which must be verified and confirmed prior to a token being granted.

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
    api_instance = oxide.HiddenApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Start an OAuth 2.0 Device Authorization Grant
        api_response = api_instance.device_auth_request(client_id)
        print("The response of HiddenApi->device_auth_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HiddenApi->device_auth_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Log user out of web console by deleting session on client and server

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
    api_instance = oxide.HiddenApi(api_client)

    try:
        # Log user out of web console by deleting session on client and server
        api_instance.logout()
    except Exception as e:
        print("Exception when calling HiddenApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **probe_create**
> Probe probe_create(project, probe_create)

Create instrumentation probe

### Example


```python
import oxide
from oxide.models.probe import Probe
from oxide.models.probe_create import ProbeCreate
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
    api_instance = oxide.HiddenApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    probe_create = oxide.ProbeCreate() # ProbeCreate | 

    try:
        # Create instrumentation probe
        api_response = api_instance.probe_create(project, probe_create)
        print("The response of HiddenApi->probe_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HiddenApi->probe_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **probe_create** | [**ProbeCreate**](ProbeCreate.md)|  | 

### Return type

[**Probe**](Probe.md)

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

# **probe_delete**
> probe_delete(project, probe)

Delete instrumentation probe

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
    api_instance = oxide.HiddenApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    probe = oxide.NameOrId() # NameOrId | Name or ID of the probe

    try:
        # Delete instrumentation probe
        api_instance.probe_delete(project, probe)
    except Exception as e:
        print("Exception when calling HiddenApi->probe_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **probe** | [**NameOrId**](.md)| Name or ID of the probe | 

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

# **probe_list**
> ProbeInfoResultsPage probe_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List instrumentation probes

### Example


```python
import oxide
from oxide.models.probe_info_results_page import ProbeInfoResultsPage
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
    api_instance = oxide.HiddenApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List instrumentation probes
        api_response = api_instance.probe_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of HiddenApi->probe_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HiddenApi->probe_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**ProbeInfoResultsPage**](ProbeInfoResultsPage.md)

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

# **probe_view**
> ProbeInfo probe_view(probe, project)

View instrumentation probe

### Example


```python
import oxide
from oxide.models.probe_info import ProbeInfo
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
    api_instance = oxide.HiddenApi(api_client)
    probe = oxide.NameOrId() # NameOrId | Name or ID of the probe
    project = oxide.NameOrId() # NameOrId | Name or ID of the project

    try:
        # View instrumentation probe
        api_response = api_instance.probe_view(probe, project)
        print("The response of HiddenApi->probe_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HiddenApi->probe_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **probe** | [**NameOrId**](.md)| Name or ID of the probe | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | 

### Return type

[**ProbeInfo**](ProbeInfo.md)

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

