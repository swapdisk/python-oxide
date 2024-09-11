# oxide.SystemSilosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**local_idp_user_create**](SystemSilosApi.md#local_idp_user_create) | **POST** /v1/system/identity-providers/local/users | Create user
[**local_idp_user_delete**](SystemSilosApi.md#local_idp_user_delete) | **DELETE** /v1/system/identity-providers/local/users/{user_id} | Delete user
[**local_idp_user_set_password**](SystemSilosApi.md#local_idp_user_set_password) | **POST** /v1/system/identity-providers/local/users/{user_id}/set-password | Set or invalidate user&#39;s password
[**saml_identity_provider_create**](SystemSilosApi.md#saml_identity_provider_create) | **POST** /v1/system/identity-providers/saml | Create SAML IdP
[**saml_identity_provider_view**](SystemSilosApi.md#saml_identity_provider_view) | **GET** /v1/system/identity-providers/saml/{provider} | Fetch SAML IdP
[**silo_create**](SystemSilosApi.md#silo_create) | **POST** /v1/system/silos | Create a silo
[**silo_delete**](SystemSilosApi.md#silo_delete) | **DELETE** /v1/system/silos/{silo} | Delete a silo
[**silo_identity_provider_list**](SystemSilosApi.md#silo_identity_provider_list) | **GET** /v1/system/identity-providers | List a silo&#39;s IdP&#39;s name
[**silo_ip_pool_list**](SystemSilosApi.md#silo_ip_pool_list) | **GET** /v1/system/silos/{silo}/ip-pools | List IP pools linked to silo
[**silo_list**](SystemSilosApi.md#silo_list) | **GET** /v1/system/silos | List silos
[**silo_policy_update**](SystemSilosApi.md#silo_policy_update) | **PUT** /v1/system/silos/{silo}/policy | Update silo IAM policy
[**silo_policy_view**](SystemSilosApi.md#silo_policy_view) | **GET** /v1/system/silos/{silo}/policy | Fetch silo IAM policy
[**silo_quotas_update**](SystemSilosApi.md#silo_quotas_update) | **PUT** /v1/system/silos/{silo}/quotas | Update resource quotas for silo
[**silo_quotas_view**](SystemSilosApi.md#silo_quotas_view) | **GET** /v1/system/silos/{silo}/quotas | Fetch resource quotas for silo
[**silo_user_list**](SystemSilosApi.md#silo_user_list) | **GET** /v1/system/users | List built-in (system) users in silo
[**silo_user_view**](SystemSilosApi.md#silo_user_view) | **GET** /v1/system/users/{user_id} | Fetch built-in (system) user
[**silo_utilization_list**](SystemSilosApi.md#silo_utilization_list) | **GET** /v1/system/utilization/silos | List current utilization state for all silos
[**silo_utilization_view**](SystemSilosApi.md#silo_utilization_view) | **GET** /v1/system/utilization/silos/{silo} | Fetch current utilization for given silo
[**silo_view**](SystemSilosApi.md#silo_view) | **GET** /v1/system/silos/{silo} | Fetch silo
[**system_quotas_list**](SystemSilosApi.md#system_quotas_list) | **GET** /v1/system/silo-quotas | Lists resource quotas for all silos
[**user_builtin_list**](SystemSilosApi.md#user_builtin_list) | **GET** /v1/system/users-builtin | List built-in users
[**user_builtin_view**](SystemSilosApi.md#user_builtin_view) | **GET** /v1/system/users-builtin/{user} | Fetch built-in user


# **local_idp_user_create**
> User local_idp_user_create(silo, user_create)

Create user

Users can only be created in Silos with `provision_type` == `Fixed`. Otherwise, Silo users are just-in-time (JIT) provisioned when a user first logs in using an external Identity Provider.

### Example


```python
import oxide
from oxide.models.user import User
from oxide.models.user_create import UserCreate
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo
    user_create = oxide.UserCreate() # UserCreate | 

    try:
        # Create user
        api_response = api_instance.local_idp_user_create(silo, user_create)
        print("The response of SystemSilosApi->local_idp_user_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->local_idp_user_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**User**](User.md)

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

# **local_idp_user_delete**
> local_idp_user_delete(user_id, silo)

Delete user

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
    api_instance = oxide.SystemSilosApi(api_client)
    user_id = 'user_id_example' # str | The user's internal ID
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Delete user
        api_instance.local_idp_user_delete(user_id, silo)
    except Exception as e:
        print("Exception when calling SystemSilosApi->local_idp_user_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s internal ID | 
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

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

# **local_idp_user_set_password**
> local_idp_user_set_password(user_id, silo, user_password)

Set or invalidate user's password

Passwords can only be updated for users in Silos with identity mode `LocalOnly`.

### Example


```python
import oxide
from oxide.models.user_password import UserPassword
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
    api_instance = oxide.SystemSilosApi(api_client)
    user_id = 'user_id_example' # str | The user's internal ID
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo
    user_password = oxide.UserPassword() # UserPassword | 

    try:
        # Set or invalidate user's password
        api_instance.local_idp_user_set_password(user_id, silo, user_password)
    except Exception as e:
        print("Exception when calling SystemSilosApi->local_idp_user_set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s internal ID | 
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 
 **user_password** | [**UserPassword**](UserPassword.md)|  | 

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

# **saml_identity_provider_create**
> SamlIdentityProvider saml_identity_provider_create(silo, saml_identity_provider_create)

Create SAML IdP

### Example


```python
import oxide
from oxide.models.saml_identity_provider import SamlIdentityProvider
from oxide.models.saml_identity_provider_create import SamlIdentityProviderCreate
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo
    saml_identity_provider_create = oxide.SamlIdentityProviderCreate() # SamlIdentityProviderCreate | 

    try:
        # Create SAML IdP
        api_response = api_instance.saml_identity_provider_create(silo, saml_identity_provider_create)
        print("The response of SystemSilosApi->saml_identity_provider_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->saml_identity_provider_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 
 **saml_identity_provider_create** | [**SamlIdentityProviderCreate**](SamlIdentityProviderCreate.md)|  | 

### Return type

[**SamlIdentityProvider**](SamlIdentityProvider.md)

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

# **saml_identity_provider_view**
> SamlIdentityProvider saml_identity_provider_view(provider, silo)

Fetch SAML IdP

### Example


```python
import oxide
from oxide.models.saml_identity_provider import SamlIdentityProvider
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
    api_instance = oxide.SystemSilosApi(api_client)
    provider = oxide.NameOrId() # NameOrId | Name or ID of the SAML identity provider
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Fetch SAML IdP
        api_response = api_instance.saml_identity_provider_view(provider, silo)
        print("The response of SystemSilosApi->saml_identity_provider_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->saml_identity_provider_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**NameOrId**](.md)| Name or ID of the SAML identity provider | 
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

### Return type

[**SamlIdentityProvider**](SamlIdentityProvider.md)

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

# **silo_create**
> Silo silo_create(silo_create)

Create a silo

### Example


```python
import oxide
from oxide.models.silo import Silo
from oxide.models.silo_create import SiloCreate
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo_create = oxide.SiloCreate() # SiloCreate | 

    try:
        # Create a silo
        api_response = api_instance.silo_create(silo_create)
        print("The response of SystemSilosApi->silo_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo_create** | [**SiloCreate**](SiloCreate.md)|  | 

### Return type

[**Silo**](Silo.md)

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

# **silo_delete**
> silo_delete(silo)

Delete a silo

Delete a silo by name or ID.

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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Delete a silo
        api_instance.silo_delete(silo)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

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

# **silo_identity_provider_list**
> IdentityProviderResultsPage silo_identity_provider_list(limit=limit, page_token=page_token, silo=silo, sort_by=sort_by)

List a silo's IdP's name

### Example


```python
import oxide
from oxide.models.identity_provider_results_page import IdentityProviderResultsPage
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
    api_instance = oxide.SystemSilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List a silo's IdP's name
        api_response = api_instance.silo_identity_provider_list(limit=limit, page_token=page_token, silo=silo, sort_by=sort_by)
        print("The response of SystemSilosApi->silo_identity_provider_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_identity_provider_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**IdentityProviderResultsPage**](IdentityProviderResultsPage.md)

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

# **silo_ip_pool_list**
> SiloIpPoolResultsPage silo_ip_pool_list(silo, limit=limit, page_token=page_token, sort_by=sort_by)

List IP pools linked to silo

Linked IP pools are available to users in the specified silo. A silo can have at most one default pool. IPs are allocated from the default pool when users ask for one without specifying a pool.

### Example


```python
import oxide
from oxide.models.silo_ip_pool_results_page import SiloIpPoolResultsPage
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List IP pools linked to silo
        api_response = api_instance.silo_ip_pool_list(silo, limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemSilosApi->silo_ip_pool_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_ip_pool_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**SiloIpPoolResultsPage**](SiloIpPoolResultsPage.md)

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

# **silo_list**
> SiloResultsPage silo_list(limit=limit, page_token=page_token, sort_by=sort_by)

List silos

Lists silos that are discoverable based on the current permissions.

### Example


```python
import oxide
from oxide.models.silo_results_page import SiloResultsPage
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
    api_instance = oxide.SystemSilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List silos
        api_response = api_instance.silo_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemSilosApi->silo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**SiloResultsPage**](SiloResultsPage.md)

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

# **silo_policy_update**
> SiloRolePolicy silo_policy_update(silo, silo_role_policy)

Update silo IAM policy

### Example


```python
import oxide
from oxide.models.silo_role_policy import SiloRolePolicy
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo
    silo_role_policy = oxide.SiloRolePolicy() # SiloRolePolicy | 

    try:
        # Update silo IAM policy
        api_response = api_instance.silo_policy_update(silo, silo_role_policy)
        print("The response of SystemSilosApi->silo_policy_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_policy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 
 **silo_role_policy** | [**SiloRolePolicy**](SiloRolePolicy.md)|  | 

### Return type

[**SiloRolePolicy**](SiloRolePolicy.md)

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

# **silo_policy_view**
> SiloRolePolicy silo_policy_view(silo)

Fetch silo IAM policy

### Example


```python
import oxide
from oxide.models.silo_role_policy import SiloRolePolicy
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Fetch silo IAM policy
        api_response = api_instance.silo_policy_view(silo)
        print("The response of SystemSilosApi->silo_policy_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_policy_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

### Return type

[**SiloRolePolicy**](SiloRolePolicy.md)

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

# **silo_quotas_update**
> SiloQuotas silo_quotas_update(silo, silo_quotas_update)

Update resource quotas for silo

If a quota value is not specified, it will remain unchanged.

### Example


```python
import oxide
from oxide.models.silo_quotas import SiloQuotas
from oxide.models.silo_quotas_update import SiloQuotasUpdate
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo
    silo_quotas_update = oxide.SiloQuotasUpdate() # SiloQuotasUpdate | 

    try:
        # Update resource quotas for silo
        api_response = api_instance.silo_quotas_update(silo, silo_quotas_update)
        print("The response of SystemSilosApi->silo_quotas_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_quotas_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 
 **silo_quotas_update** | [**SiloQuotasUpdate**](SiloQuotasUpdate.md)|  | 

### Return type

[**SiloQuotas**](SiloQuotas.md)

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

# **silo_quotas_view**
> SiloQuotas silo_quotas_view(silo)

Fetch resource quotas for silo

### Example


```python
import oxide
from oxide.models.silo_quotas import SiloQuotas
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Fetch resource quotas for silo
        api_response = api_instance.silo_quotas_view(silo)
        print("The response of SystemSilosApi->silo_quotas_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_quotas_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

### Return type

[**SiloQuotas**](SiloQuotas.md)

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

# **silo_user_list**
> UserResultsPage silo_user_list(limit=limit, page_token=page_token, silo=silo, sort_by=sort_by)

List built-in (system) users in silo

### Example


```python
import oxide
from oxide.models.user_results_page import UserResultsPage
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
    api_instance = oxide.SystemSilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List built-in (system) users in silo
        api_response = api_instance.silo_user_list(limit=limit, page_token=page_token, silo=silo, sort_by=sort_by)
        print("The response of SystemSilosApi->silo_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**UserResultsPage**](UserResultsPage.md)

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

# **silo_user_view**
> User silo_user_view(user_id, silo)

Fetch built-in (system) user

### Example


```python
import oxide
from oxide.models.user import User
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
    api_instance = oxide.SystemSilosApi(api_client)
    user_id = 'user_id_example' # str | The user's internal ID
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Fetch built-in (system) user
        api_response = api_instance.silo_user_view(user_id, silo)
        print("The response of SystemSilosApi->silo_user_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_user_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s internal ID | 
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

### Return type

[**User**](User.md)

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

# **silo_utilization_list**
> SiloUtilizationResultsPage silo_utilization_list(limit=limit, page_token=page_token, sort_by=sort_by)

List current utilization state for all silos

### Example


```python
import oxide
from oxide.models.silo_utilization_results_page import SiloUtilizationResultsPage
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
    api_instance = oxide.SystemSilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List current utilization state for all silos
        api_response = api_instance.silo_utilization_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemSilosApi->silo_utilization_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_utilization_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**SiloUtilizationResultsPage**](SiloUtilizationResultsPage.md)

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

# **silo_utilization_view**
> SiloUtilization silo_utilization_view(silo)

Fetch current utilization for given silo

### Example


```python
import oxide
from oxide.models.silo_utilization import SiloUtilization
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Fetch current utilization for given silo
        api_response = api_instance.silo_utilization_view(silo)
        print("The response of SystemSilosApi->silo_utilization_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_utilization_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

### Return type

[**SiloUtilization**](SiloUtilization.md)

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

# **silo_view**
> Silo silo_view(silo)

Fetch silo

Fetch silo by name or ID.

### Example


```python
import oxide
from oxide.models.silo import Silo
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
    api_instance = oxide.SystemSilosApi(api_client)
    silo = oxide.NameOrId() # NameOrId | Name or ID of the silo

    try:
        # Fetch silo
        api_response = api_instance.silo_view(silo)
        print("The response of SystemSilosApi->silo_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->silo_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo** | [**NameOrId**](.md)| Name or ID of the silo | 

### Return type

[**Silo**](Silo.md)

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

# **system_quotas_list**
> SiloQuotasResultsPage system_quotas_list(limit=limit, page_token=page_token, sort_by=sort_by)

Lists resource quotas for all silos

### Example


```python
import oxide
from oxide.models.silo_quotas_results_page import SiloQuotasResultsPage
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
    api_instance = oxide.SystemSilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # Lists resource quotas for all silos
        api_response = api_instance.system_quotas_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemSilosApi->system_quotas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->system_quotas_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**SiloQuotasResultsPage**](SiloQuotasResultsPage.md)

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

# **user_builtin_list**
> UserBuiltinResultsPage user_builtin_list(limit=limit, page_token=page_token, sort_by=sort_by)

List built-in users

### Example


```python
import oxide
from oxide.models.user_builtin_results_page import UserBuiltinResultsPage
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
    api_instance = oxide.SystemSilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameSortMode() # NameSortMode |  (optional)

    try:
        # List built-in users
        api_response = api_instance.user_builtin_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemSilosApi->user_builtin_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->user_builtin_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameSortMode**](.md)|  | [optional] 

### Return type

[**UserBuiltinResultsPage**](UserBuiltinResultsPage.md)

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

# **user_builtin_view**
> UserBuiltin user_builtin_view(user)

Fetch built-in user

### Example


```python
import oxide
from oxide.models.user_builtin import UserBuiltin
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
    api_instance = oxide.SystemSilosApi(api_client)
    user = oxide.NameOrId() # NameOrId | 

    try:
        # Fetch built-in user
        api_response = api_instance.user_builtin_view(user)
        print("The response of SystemSilosApi->user_builtin_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSilosApi->user_builtin_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**NameOrId**](.md)|  | 

### Return type

[**UserBuiltin**](UserBuiltin.md)

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

