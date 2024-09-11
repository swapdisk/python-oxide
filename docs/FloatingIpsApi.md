# oxide.FloatingIpsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**floating_ip_attach**](FloatingIpsApi.md#floating_ip_attach) | **POST** /v1/floating-ips/{floating_ip}/attach | Attach floating IP
[**floating_ip_create**](FloatingIpsApi.md#floating_ip_create) | **POST** /v1/floating-ips | Create floating IP
[**floating_ip_delete**](FloatingIpsApi.md#floating_ip_delete) | **DELETE** /v1/floating-ips/{floating_ip} | Delete floating IP
[**floating_ip_detach**](FloatingIpsApi.md#floating_ip_detach) | **POST** /v1/floating-ips/{floating_ip}/detach | Detach floating IP
[**floating_ip_list**](FloatingIpsApi.md#floating_ip_list) | **GET** /v1/floating-ips | List floating IPs
[**floating_ip_update**](FloatingIpsApi.md#floating_ip_update) | **PUT** /v1/floating-ips/{floating_ip} | Update floating IP
[**floating_ip_view**](FloatingIpsApi.md#floating_ip_view) | **GET** /v1/floating-ips/{floating_ip} | Fetch floating IP


# **floating_ip_attach**
> FloatingIp floating_ip_attach(floating_ip, floating_ip_attach, project=project)

Attach floating IP

Attach floating IP to an instance or other resource.

### Example


```python
import oxide
from oxide.models.floating_ip import FloatingIp
from oxide.models.floating_ip_attach import FloatingIpAttach
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
    api_instance = oxide.FloatingIpsApi(api_client)
    floating_ip = oxide.NameOrId() # NameOrId | Name or ID of the floating IP
    floating_ip_attach = oxide.FloatingIpAttach() # FloatingIpAttach | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Attach floating IP
        api_response = api_instance.floating_ip_attach(floating_ip, floating_ip_attach, project=project)
        print("The response of FloatingIpsApi->floating_ip_attach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpsApi->floating_ip_attach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | [**NameOrId**](.md)| Name or ID of the floating IP | 
 **floating_ip_attach** | [**FloatingIpAttach**](FloatingIpAttach.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**FloatingIp**](FloatingIp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully enqueued operation |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **floating_ip_create**
> FloatingIp floating_ip_create(project, floating_ip_create)

Create floating IP

### Example


```python
import oxide
from oxide.models.floating_ip import FloatingIp
from oxide.models.floating_ip_create import FloatingIpCreate
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
    api_instance = oxide.FloatingIpsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    floating_ip_create = oxide.FloatingIpCreate() # FloatingIpCreate | 

    try:
        # Create floating IP
        api_response = api_instance.floating_ip_create(project, floating_ip_create)
        print("The response of FloatingIpsApi->floating_ip_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpsApi->floating_ip_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **floating_ip_create** | [**FloatingIpCreate**](FloatingIpCreate.md)|  | 

### Return type

[**FloatingIp**](FloatingIp.md)

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

# **floating_ip_delete**
> floating_ip_delete(floating_ip, project=project)

Delete floating IP

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
    api_instance = oxide.FloatingIpsApi(api_client)
    floating_ip = oxide.NameOrId() # NameOrId | Name or ID of the floating IP
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Delete floating IP
        api_instance.floating_ip_delete(floating_ip, project=project)
    except Exception as e:
        print("Exception when calling FloatingIpsApi->floating_ip_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | [**NameOrId**](.md)| Name or ID of the floating IP | 
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

# **floating_ip_detach**
> FloatingIp floating_ip_detach(floating_ip, project=project)

Detach floating IP

### Example


```python
import oxide
from oxide.models.floating_ip import FloatingIp
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
    api_instance = oxide.FloatingIpsApi(api_client)
    floating_ip = oxide.NameOrId() # NameOrId | Name or ID of the floating IP
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Detach floating IP
        api_response = api_instance.floating_ip_detach(floating_ip, project=project)
        print("The response of FloatingIpsApi->floating_ip_detach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpsApi->floating_ip_detach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | [**NameOrId**](.md)| Name or ID of the floating IP | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**FloatingIp**](FloatingIp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully enqueued operation |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **floating_ip_list**
> FloatingIpResultsPage floating_ip_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List floating IPs

### Example


```python
import oxide
from oxide.models.floating_ip_results_page import FloatingIpResultsPage
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
    api_instance = oxide.FloatingIpsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List floating IPs
        api_response = api_instance.floating_ip_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of FloatingIpsApi->floating_ip_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpsApi->floating_ip_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**FloatingIpResultsPage**](FloatingIpResultsPage.md)

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

# **floating_ip_update**
> FloatingIp floating_ip_update(floating_ip, floating_ip_update, project=project)

Update floating IP

### Example


```python
import oxide
from oxide.models.floating_ip import FloatingIp
from oxide.models.floating_ip_update import FloatingIpUpdate
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
    api_instance = oxide.FloatingIpsApi(api_client)
    floating_ip = oxide.NameOrId() # NameOrId | Name or ID of the floating IP
    floating_ip_update = oxide.FloatingIpUpdate() # FloatingIpUpdate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Update floating IP
        api_response = api_instance.floating_ip_update(floating_ip, floating_ip_update, project=project)
        print("The response of FloatingIpsApi->floating_ip_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpsApi->floating_ip_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | [**NameOrId**](.md)| Name or ID of the floating IP | 
 **floating_ip_update** | [**FloatingIpUpdate**](FloatingIpUpdate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**FloatingIp**](FloatingIp.md)

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

# **floating_ip_view**
> FloatingIp floating_ip_view(floating_ip, project=project)

Fetch floating IP

### Example


```python
import oxide
from oxide.models.floating_ip import FloatingIp
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
    api_instance = oxide.FloatingIpsApi(api_client)
    floating_ip = oxide.NameOrId() # NameOrId | Name or ID of the floating IP
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Fetch floating IP
        api_response = api_instance.floating_ip_view(floating_ip, project=project)
        print("The response of FloatingIpsApi->floating_ip_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpsApi->floating_ip_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | [**NameOrId**](.md)| Name or ID of the floating IP | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**FloatingIp**](FloatingIp.md)

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

