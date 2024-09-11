# oxide.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_create**](ProjectsApi.md#project_create) | **POST** /v1/projects | Create project
[**project_delete**](ProjectsApi.md#project_delete) | **DELETE** /v1/projects/{project} | Delete project
[**project_ip_pool_list**](ProjectsApi.md#project_ip_pool_list) | **GET** /v1/ip-pools | List IP pools
[**project_ip_pool_view**](ProjectsApi.md#project_ip_pool_view) | **GET** /v1/ip-pools/{pool} | Fetch IP pool
[**project_list**](ProjectsApi.md#project_list) | **GET** /v1/projects | List projects
[**project_policy_update**](ProjectsApi.md#project_policy_update) | **PUT** /v1/projects/{project}/policy | Update project&#39;s IAM policy
[**project_policy_view**](ProjectsApi.md#project_policy_view) | **GET** /v1/projects/{project}/policy | Fetch project&#39;s IAM policy
[**project_update**](ProjectsApi.md#project_update) | **PUT** /v1/projects/{project} | Update a project
[**project_view**](ProjectsApi.md#project_view) | **GET** /v1/projects/{project} | Fetch project


# **project_create**
> Project project_create(project_create)

Create project

### Example


```python
import oxide
from oxide.models.project import Project
from oxide.models.project_create import ProjectCreate
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
    api_instance = oxide.ProjectsApi(api_client)
    project_create = oxide.ProjectCreate() # ProjectCreate | 

    try:
        # Create project
        api_response = api_instance.project_create(project_create)
        print("The response of ProjectsApi->project_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  | 

### Return type

[**Project**](Project.md)

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

# **project_delete**
> project_delete(project)

Delete project

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
    api_instance = oxide.ProjectsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project

    try:
        # Delete project
        api_instance.project_delete(project)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 

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

# **project_ip_pool_list**
> SiloIpPoolResultsPage project_ip_pool_list(limit=limit, page_token=page_token, sort_by=sort_by)

List IP pools

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
    api_instance = oxide.ProjectsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List IP pools
        api_response = api_instance.project_ip_pool_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of ProjectsApi->project_ip_pool_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_ip_pool_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **project_ip_pool_view**
> SiloIpPool project_ip_pool_view(pool)

Fetch IP pool

### Example


```python
import oxide
from oxide.models.silo_ip_pool import SiloIpPool
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
    api_instance = oxide.ProjectsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool

    try:
        # Fetch IP pool
        api_response = api_instance.project_ip_pool_view(pool)
        print("The response of ProjectsApi->project_ip_pool_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_ip_pool_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 

### Return type

[**SiloIpPool**](SiloIpPool.md)

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

# **project_list**
> ProjectResultsPage project_list(limit=limit, page_token=page_token, sort_by=sort_by)

List projects

### Example


```python
import oxide
from oxide.models.project_results_page import ProjectResultsPage
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
    api_instance = oxide.ProjectsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List projects
        api_response = api_instance.project_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of ProjectsApi->project_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**ProjectResultsPage**](ProjectResultsPage.md)

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

# **project_policy_update**
> ProjectRolePolicy project_policy_update(project, project_role_policy)

Update project's IAM policy

### Example


```python
import oxide
from oxide.models.project_role_policy import ProjectRolePolicy
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
    api_instance = oxide.ProjectsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    project_role_policy = oxide.ProjectRolePolicy() # ProjectRolePolicy | 

    try:
        # Update project's IAM policy
        api_response = api_instance.project_policy_update(project, project_role_policy)
        print("The response of ProjectsApi->project_policy_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_policy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **project_role_policy** | [**ProjectRolePolicy**](ProjectRolePolicy.md)|  | 

### Return type

[**ProjectRolePolicy**](ProjectRolePolicy.md)

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

# **project_policy_view**
> ProjectRolePolicy project_policy_view(project)

Fetch project's IAM policy

### Example


```python
import oxide
from oxide.models.project_role_policy import ProjectRolePolicy
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
    api_instance = oxide.ProjectsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project

    try:
        # Fetch project's IAM policy
        api_response = api_instance.project_policy_view(project)
        print("The response of ProjectsApi->project_policy_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_policy_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 

### Return type

[**ProjectRolePolicy**](ProjectRolePolicy.md)

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

# **project_update**
> Project project_update(project, project_update)

Update a project

### Example


```python
import oxide
from oxide.models.project import Project
from oxide.models.project_update import ProjectUpdate
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
    api_instance = oxide.ProjectsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    project_update = oxide.ProjectUpdate() # ProjectUpdate | 

    try:
        # Update a project
        api_response = api_instance.project_update(project, project_update)
        print("The response of ProjectsApi->project_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **project_update** | [**ProjectUpdate**](ProjectUpdate.md)|  | 

### Return type

[**Project**](Project.md)

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

# **project_view**
> Project project_view(project)

Fetch project

### Example


```python
import oxide
from oxide.models.project import Project
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
    api_instance = oxide.ProjectsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project

    try:
        # Fetch project
        api_response = api_instance.project_view(project)
        print("The response of ProjectsApi->project_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 

### Return type

[**Project**](Project.md)

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

