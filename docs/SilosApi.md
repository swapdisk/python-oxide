# oxide.SilosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_create**](SilosApi.md#certificate_create) | **POST** /v1/certificates | Create new system-wide x.509 certificate
[**certificate_delete**](SilosApi.md#certificate_delete) | **DELETE** /v1/certificates/{certificate} | Delete certificate
[**certificate_list**](SilosApi.md#certificate_list) | **GET** /v1/certificates | List certificates for external endpoints
[**certificate_view**](SilosApi.md#certificate_view) | **GET** /v1/certificates/{certificate} | Fetch certificate
[**group_list**](SilosApi.md#group_list) | **GET** /v1/groups | List groups
[**group_view**](SilosApi.md#group_view) | **GET** /v1/groups/{group_id} | Fetch group
[**policy_update**](SilosApi.md#policy_update) | **PUT** /v1/policy | Update current silo&#39;s IAM policy
[**policy_view**](SilosApi.md#policy_view) | **GET** /v1/policy | Fetch current silo&#39;s IAM policy
[**user_list**](SilosApi.md#user_list) | **GET** /v1/users | List users
[**utilization_view**](SilosApi.md#utilization_view) | **GET** /v1/utilization | Fetch resource utilization for user&#39;s current silo


# **certificate_create**
> Certificate certificate_create(certificate_create)

Create new system-wide x.509 certificate

This certificate is automatically used by the Oxide Control plane to serve external connections.

### Example


```python
import oxide
from oxide.models.certificate import Certificate
from oxide.models.certificate_create import CertificateCreate
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
    api_instance = oxide.SilosApi(api_client)
    certificate_create = oxide.CertificateCreate() # CertificateCreate | 

    try:
        # Create new system-wide x.509 certificate
        api_response = api_instance.certificate_create(certificate_create)
        print("The response of SilosApi->certificate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->certificate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_create** | [**CertificateCreate**](CertificateCreate.md)|  | 

### Return type

[**Certificate**](Certificate.md)

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

# **certificate_delete**
> certificate_delete(certificate)

Delete certificate

Permanently delete a certificate. This operation cannot be undone.

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
    api_instance = oxide.SilosApi(api_client)
    certificate = oxide.NameOrId() # NameOrId | Name or ID of the certificate

    try:
        # Delete certificate
        api_instance.certificate_delete(certificate)
    except Exception as e:
        print("Exception when calling SilosApi->certificate_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**NameOrId**](.md)| Name or ID of the certificate | 

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

# **certificate_list**
> CertificateResultsPage certificate_list(limit=limit, page_token=page_token, sort_by=sort_by)

List certificates for external endpoints

Returns a list of TLS certificates used for the external API (for the current Silo).  These are sorted by creation date, with the most recent certificates appearing first.

### Example


```python
import oxide
from oxide.models.certificate_results_page import CertificateResultsPage
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
    api_instance = oxide.SilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List certificates for external endpoints
        api_response = api_instance.certificate_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SilosApi->certificate_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->certificate_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**CertificateResultsPage**](CertificateResultsPage.md)

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

# **certificate_view**
> Certificate certificate_view(certificate)

Fetch certificate

Returns the details of a specific certificate

### Example


```python
import oxide
from oxide.models.certificate import Certificate
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
    api_instance = oxide.SilosApi(api_client)
    certificate = oxide.NameOrId() # NameOrId | Name or ID of the certificate

    try:
        # Fetch certificate
        api_response = api_instance.certificate_view(certificate)
        print("The response of SilosApi->certificate_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->certificate_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**NameOrId**](.md)| Name or ID of the certificate | 

### Return type

[**Certificate**](Certificate.md)

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

# **group_list**
> GroupResultsPage group_list(limit=limit, page_token=page_token, sort_by=sort_by)

List groups

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
    api_instance = oxide.SilosApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List groups
        api_response = api_instance.group_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SilosApi->group_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->group_list: %s\n" % e)
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

# **group_view**
> Group group_view(group_id)

Fetch group

### Example


```python
import oxide
from oxide.models.group import Group
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
    api_instance = oxide.SilosApi(api_client)
    group_id = 'group_id_example' # str | ID of the group

    try:
        # Fetch group
        api_response = api_instance.group_view(group_id)
        print("The response of SilosApi->group_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->group_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ID of the group | 

### Return type

[**Group**](Group.md)

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

# **policy_update**
> SiloRolePolicy policy_update(silo_role_policy)

Update current silo's IAM policy

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
    api_instance = oxide.SilosApi(api_client)
    silo_role_policy = oxide.SiloRolePolicy() # SiloRolePolicy | 

    try:
        # Update current silo's IAM policy
        api_response = api_instance.policy_update(silo_role_policy)
        print("The response of SilosApi->policy_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->policy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **policy_view**
> SiloRolePolicy policy_view()

Fetch current silo's IAM policy

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
    api_instance = oxide.SilosApi(api_client)

    try:
        # Fetch current silo's IAM policy
        api_response = api_instance.policy_view()
        print("The response of SilosApi->policy_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->policy_view: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **user_list**
> UserResultsPage user_list(group=group, limit=limit, page_token=page_token, sort_by=sort_by)

List users

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
    api_instance = oxide.SilosApi(api_client)
    group = 'group_example' # str |  (optional)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List users
        api_response = api_instance.user_list(group=group, limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SilosApi->user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**|  | [optional] 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
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

# **utilization_view**
> Utilization utilization_view()

Fetch resource utilization for user's current silo

### Example


```python
import oxide
from oxide.models.utilization import Utilization
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
    api_instance = oxide.SilosApi(api_client)

    try:
        # Fetch resource utilization for user's current silo
        api_response = api_instance.utilization_view()
        print("The response of SilosApi->utilization_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SilosApi->utilization_view: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Utilization**](Utilization.md)

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

