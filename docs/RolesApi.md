# oxide.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_list**](RolesApi.md#role_list) | **GET** /v1/system/roles | List built-in roles
[**role_view**](RolesApi.md#role_view) | **GET** /v1/system/roles/{role_name} | Fetch built-in role


# **role_list**
> RoleResultsPage role_list(limit=limit, page_token=page_token)

List built-in roles

### Example


```python
import oxide
from oxide.models.role_results_page import RoleResultsPage
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
    api_instance = oxide.RolesApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)

    try:
        # List built-in roles
        api_response = api_instance.role_list(limit=limit, page_token=page_token)
        print("The response of RolesApi->role_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->role_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 

### Return type

[**RoleResultsPage**](RoleResultsPage.md)

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

# **role_view**
> Role role_view(role_name)

Fetch built-in role

### Example


```python
import oxide
from oxide.models.role import Role
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
    api_instance = oxide.RolesApi(api_client)
    role_name = 'role_name_example' # str | The built-in role's unique name.

    try:
        # Fetch built-in role
        api_response = api_instance.role_view(role_name)
        print("The response of RolesApi->role_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->role_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| The built-in role&#39;s unique name. | 

### Return type

[**Role**](Role.md)

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

