# oxide.SessionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**current_user_groups**](SessionApi.md#current_user_groups) | **GET** /v1/me/groups | Fetch current user&#39;s groups
[**current_user_ssh_key_create**](SessionApi.md#current_user_ssh_key_create) | **POST** /v1/me/ssh-keys | Create SSH public key
[**current_user_ssh_key_delete**](SessionApi.md#current_user_ssh_key_delete) | **DELETE** /v1/me/ssh-keys/{ssh_key} | Delete SSH public key
[**current_user_ssh_key_list**](SessionApi.md#current_user_ssh_key_list) | **GET** /v1/me/ssh-keys | List SSH public keys
[**current_user_ssh_key_view**](SessionApi.md#current_user_ssh_key_view) | **GET** /v1/me/ssh-keys/{ssh_key} | Fetch SSH public key
[**current_user_view**](SessionApi.md#current_user_view) | **GET** /v1/me | Fetch user for current session


# **current_user_groups**
> GroupResultsPage current_user_groups(limit=limit, page_token=page_token, sort_by=sort_by)

Fetch current user's groups

### Example


```python
import oxide
from oxide.models.group_results_page import GroupResultsPage
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
    api_instance = oxide.SessionApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # Fetch current user's groups
        api_response = api_instance.current_user_groups(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SessionApi->current_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->current_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**GroupResultsPage**](GroupResultsPage.md)

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

# **current_user_ssh_key_create**
> SshKey current_user_ssh_key_create(ssh_key_create)

Create SSH public key

Create an SSH public key for the currently authenticated user.

### Example


```python
import oxide
from oxide.models.ssh_key import SshKey
from oxide.models.ssh_key_create import SshKeyCreate
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
    api_instance = oxide.SessionApi(api_client)
    ssh_key_create = oxide.SshKeyCreate() # SshKeyCreate | 

    try:
        # Create SSH public key
        api_response = api_instance.current_user_ssh_key_create(ssh_key_create)
        print("The response of SessionApi->current_user_ssh_key_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->current_user_ssh_key_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_create** | [**SshKeyCreate**](SshKeyCreate.md)|  | 

### Return type

[**SshKey**](SshKey.md)

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

# **current_user_ssh_key_delete**
> current_user_ssh_key_delete(ssh_key)

Delete SSH public key

Delete an SSH public key associated with the currently authenticated user.

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
    api_instance = oxide.SessionApi(api_client)
    ssh_key = oxide.NameOrId() # NameOrId | Name or ID of the SSH key

    try:
        # Delete SSH public key
        api_instance.current_user_ssh_key_delete(ssh_key)
    except Exception as e:
        print("Exception when calling SessionApi->current_user_ssh_key_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key** | [**NameOrId**](.md)| Name or ID of the SSH key | 

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

# **current_user_ssh_key_list**
> SshKeyResultsPage current_user_ssh_key_list(limit=limit, page_token=page_token, sort_by=sort_by)

List SSH public keys

Lists SSH public keys for the currently authenticated user.

### Example


```python
import oxide
from oxide.models.ssh_key_results_page import SshKeyResultsPage
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
    api_instance = oxide.SessionApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List SSH public keys
        api_response = api_instance.current_user_ssh_key_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SessionApi->current_user_ssh_key_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->current_user_ssh_key_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**SshKeyResultsPage**](SshKeyResultsPage.md)

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

# **current_user_ssh_key_view**
> SshKey current_user_ssh_key_view(ssh_key)

Fetch SSH public key

Fetch SSH public key associated with the currently authenticated user.

### Example


```python
import oxide
from oxide.models.ssh_key import SshKey
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
    api_instance = oxide.SessionApi(api_client)
    ssh_key = oxide.NameOrId() # NameOrId | Name or ID of the SSH key

    try:
        # Fetch SSH public key
        api_response = api_instance.current_user_ssh_key_view(ssh_key)
        print("The response of SessionApi->current_user_ssh_key_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->current_user_ssh_key_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key** | [**NameOrId**](.md)| Name or ID of the SSH key | 

### Return type

[**SshKey**](SshKey.md)

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

# **current_user_view**
> CurrentUser current_user_view()

Fetch user for current session

### Example


```python
import oxide
from oxide.models.current_user import CurrentUser
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
    api_instance = oxide.SessionApi(api_client)

    try:
        # Fetch user for current session
        api_response = api_instance.current_user_view()
        print("The response of SessionApi->current_user_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->current_user_view: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrentUser**](CurrentUser.md)

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

