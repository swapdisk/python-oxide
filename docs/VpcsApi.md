# oxide.VpcsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vpc_create**](VpcsApi.md#vpc_create) | **POST** /v1/vpcs | Create VPC
[**vpc_delete**](VpcsApi.md#vpc_delete) | **DELETE** /v1/vpcs/{vpc} | Delete VPC
[**vpc_firewall_rules_update**](VpcsApi.md#vpc_firewall_rules_update) | **PUT** /v1/vpc-firewall-rules | Replace firewall rules
[**vpc_firewall_rules_view**](VpcsApi.md#vpc_firewall_rules_view) | **GET** /v1/vpc-firewall-rules | List firewall rules
[**vpc_list**](VpcsApi.md#vpc_list) | **GET** /v1/vpcs | List VPCs
[**vpc_router_create**](VpcsApi.md#vpc_router_create) | **POST** /v1/vpc-routers | Create VPC router
[**vpc_router_delete**](VpcsApi.md#vpc_router_delete) | **DELETE** /v1/vpc-routers/{router} | Delete router
[**vpc_router_list**](VpcsApi.md#vpc_router_list) | **GET** /v1/vpc-routers | List routers
[**vpc_router_route_create**](VpcsApi.md#vpc_router_route_create) | **POST** /v1/vpc-router-routes | Create route
[**vpc_router_route_delete**](VpcsApi.md#vpc_router_route_delete) | **DELETE** /v1/vpc-router-routes/{route} | Delete route
[**vpc_router_route_list**](VpcsApi.md#vpc_router_route_list) | **GET** /v1/vpc-router-routes | List routes
[**vpc_router_route_update**](VpcsApi.md#vpc_router_route_update) | **PUT** /v1/vpc-router-routes/{route} | Update route
[**vpc_router_route_view**](VpcsApi.md#vpc_router_route_view) | **GET** /v1/vpc-router-routes/{route} | Fetch route
[**vpc_router_update**](VpcsApi.md#vpc_router_update) | **PUT** /v1/vpc-routers/{router} | Update router
[**vpc_router_view**](VpcsApi.md#vpc_router_view) | **GET** /v1/vpc-routers/{router} | Fetch router
[**vpc_subnet_create**](VpcsApi.md#vpc_subnet_create) | **POST** /v1/vpc-subnets | Create subnet
[**vpc_subnet_delete**](VpcsApi.md#vpc_subnet_delete) | **DELETE** /v1/vpc-subnets/{subnet} | Delete subnet
[**vpc_subnet_list**](VpcsApi.md#vpc_subnet_list) | **GET** /v1/vpc-subnets | List subnets
[**vpc_subnet_list_network_interfaces**](VpcsApi.md#vpc_subnet_list_network_interfaces) | **GET** /v1/vpc-subnets/{subnet}/network-interfaces | List network interfaces
[**vpc_subnet_update**](VpcsApi.md#vpc_subnet_update) | **PUT** /v1/vpc-subnets/{subnet} | Update subnet
[**vpc_subnet_view**](VpcsApi.md#vpc_subnet_view) | **GET** /v1/vpc-subnets/{subnet} | Fetch subnet
[**vpc_update**](VpcsApi.md#vpc_update) | **PUT** /v1/vpcs/{vpc} | Update a VPC
[**vpc_view**](VpcsApi.md#vpc_view) | **GET** /v1/vpcs/{vpc} | Fetch VPC


# **vpc_create**
> Vpc vpc_create(project, vpc_create)

Create VPC

### Example


```python
import oxide
from oxide.models.vpc import Vpc
from oxide.models.vpc_create import VpcCreate
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
    api_instance = oxide.VpcsApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    vpc_create = oxide.VpcCreate() # VpcCreate | 

    try:
        # Create VPC
        api_response = api_instance.vpc_create(project, vpc_create)
        print("The response of VpcsApi->vpc_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **vpc_create** | [**VpcCreate**](VpcCreate.md)|  | 

### Return type

[**Vpc**](Vpc.md)

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

# **vpc_delete**
> vpc_delete(vpc, project=project)

Delete VPC

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
    api_instance = oxide.VpcsApi(api_client)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Delete VPC
        api_instance.vpc_delete(vpc, project=project)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | 
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

# **vpc_firewall_rules_update**
> VpcFirewallRules vpc_firewall_rules_update(vpc, vpc_firewall_rule_update_params, project=project)

Replace firewall rules

The maximum number of rules per VPC is 1024.  Targets are used to specify the set of instances to which a firewall rule applies. You can target instances directly by name, or specify a VPC, VPC subnet, IP, or IP subnet, which will apply the rule to traffic going to all matching instances. Targets are additive: the rule applies to instances matching ANY target. The maximum number of targets is 256.  Filters reduce the scope of a firewall rule. Without filters, the rule applies to all packets to the targets (or from the targets, if it's an outbound rule). With multiple filters, the rule applies only to packets matching ALL filters. The maximum number of each type of filter is 256.

### Example


```python
import oxide
from oxide.models.vpc_firewall_rule_update_params import VpcFirewallRuleUpdateParams
from oxide.models.vpc_firewall_rules import VpcFirewallRules
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
    api_instance = oxide.VpcsApi(api_client)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC
    vpc_firewall_rule_update_params = oxide.VpcFirewallRuleUpdateParams() # VpcFirewallRuleUpdateParams | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)

    try:
        # Replace firewall rules
        api_response = api_instance.vpc_firewall_rules_update(vpc, vpc_firewall_rule_update_params, project=project)
        print("The response of VpcsApi->vpc_firewall_rules_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_firewall_rules_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | 
 **vpc_firewall_rule_update_params** | [**VpcFirewallRuleUpdateParams**](VpcFirewallRuleUpdateParams.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**VpcFirewallRules**](VpcFirewallRules.md)

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

# **vpc_firewall_rules_view**
> VpcFirewallRules vpc_firewall_rules_view(vpc, project=project)

List firewall rules

### Example


```python
import oxide
from oxide.models.vpc_firewall_rules import VpcFirewallRules
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
    api_instance = oxide.VpcsApi(api_client)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)

    try:
        # List firewall rules
        api_response = api_instance.vpc_firewall_rules_view(vpc, project=project)
        print("The response of VpcsApi->vpc_firewall_rules_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_firewall_rules_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**VpcFirewallRules**](VpcFirewallRules.md)

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

# **vpc_list**
> VpcResultsPage vpc_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List VPCs

### Example


```python
import oxide
from oxide.models.vpc_results_page import VpcResultsPage
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
    api_instance = oxide.VpcsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List VPCs
        api_response = api_instance.vpc_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of VpcsApi->vpc_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**VpcResultsPage**](VpcResultsPage.md)

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

# **vpc_router_create**
> VpcRouter vpc_router_create(vpc, vpc_router_create, project=project)

Create VPC router

### Example


```python
import oxide
from oxide.models.vpc_router import VpcRouter
from oxide.models.vpc_router_create import VpcRouterCreate
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
    api_instance = oxide.VpcsApi(api_client)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC
    vpc_router_create = oxide.VpcRouterCreate() # VpcRouterCreate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)

    try:
        # Create VPC router
        api_response = api_instance.vpc_router_create(vpc, vpc_router_create, project=project)
        print("The response of VpcsApi->vpc_router_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | 
 **vpc_router_create** | [**VpcRouterCreate**](VpcRouterCreate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**VpcRouter**](VpcRouter.md)

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

# **vpc_router_delete**
> vpc_router_delete(router, project=project, vpc=vpc)

Delete router

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
    api_instance = oxide.VpcsApi(api_client)
    router = oxide.NameOrId() # NameOrId | Name or ID of the router
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # Delete router
        api_instance.vpc_router_delete(router, project=project, vpc=vpc)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router** | [**NameOrId**](.md)| Name or ID of the router | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

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

# **vpc_router_list**
> VpcRouterResultsPage vpc_router_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by, vpc=vpc)

List routers

### Example


```python
import oxide
from oxide.models.vpc_router_results_page import VpcRouterResultsPage
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
    api_instance = oxide.VpcsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # List routers
        api_response = api_instance.vpc_router_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by, vpc=vpc)
        print("The response of VpcsApi->vpc_router_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

### Return type

[**VpcRouterResultsPage**](VpcRouterResultsPage.md)

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

# **vpc_router_route_create**
> RouterRoute vpc_router_route_create(router, router_route_create, project=project, vpc=vpc)

Create route

### Example


```python
import oxide
from oxide.models.router_route import RouterRoute
from oxide.models.router_route_create import RouterRouteCreate
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
    api_instance = oxide.VpcsApi(api_client)
    router = oxide.NameOrId() # NameOrId | Name or ID of the router
    router_route_create = oxide.RouterRouteCreate() # RouterRouteCreate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC, only required if `router` is provided as a `Name` (optional)

    try:
        # Create route
        api_response = api_instance.vpc_router_route_create(router, router_route_create, project=project, vpc=vpc)
        print("The response of VpcsApi->vpc_router_route_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_route_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router** | [**NameOrId**](.md)| Name or ID of the router | 
 **router_route_create** | [**RouterRouteCreate**](RouterRouteCreate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC, only required if &#x60;router&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**RouterRoute**](RouterRoute.md)

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

# **vpc_router_route_delete**
> vpc_router_route_delete(route, project=project, router=router, vpc=vpc)

Delete route

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
    api_instance = oxide.VpcsApi(api_client)
    route = oxide.NameOrId() # NameOrId | Name or ID of the route
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    router = oxide.NameOrId() # NameOrId | Name or ID of the router (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC, only required if `router` is provided as a `Name` (optional)

    try:
        # Delete route
        api_instance.vpc_router_route_delete(route, project=project, router=router, vpc=vpc)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_route_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**NameOrId**](.md)| Name or ID of the route | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **router** | [**NameOrId**](.md)| Name or ID of the router | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC, only required if &#x60;router&#x60; is provided as a &#x60;Name&#x60; | [optional] 

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

# **vpc_router_route_list**
> RouterRouteResultsPage vpc_router_route_list(limit=limit, page_token=page_token, project=project, router=router, sort_by=sort_by, vpc=vpc)

List routes

List the routes associated with a router in a particular VPC.

### Example


```python
import oxide
from oxide.models.router_route_results_page import RouterRouteResultsPage
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
    api_instance = oxide.VpcsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    router = oxide.NameOrId() # NameOrId | Name or ID of the router (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC, only required if `router` is provided as a `Name` (optional)

    try:
        # List routes
        api_response = api_instance.vpc_router_route_list(limit=limit, page_token=page_token, project=project, router=router, sort_by=sort_by, vpc=vpc)
        print("The response of VpcsApi->vpc_router_route_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_route_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **router** | [**NameOrId**](.md)| Name or ID of the router | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC, only required if &#x60;router&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**RouterRouteResultsPage**](RouterRouteResultsPage.md)

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

# **vpc_router_route_update**
> RouterRoute vpc_router_route_update(route, router_route_update, project=project, router=router, vpc=vpc)

Update route

### Example


```python
import oxide
from oxide.models.router_route import RouterRoute
from oxide.models.router_route_update import RouterRouteUpdate
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
    api_instance = oxide.VpcsApi(api_client)
    route = oxide.NameOrId() # NameOrId | Name or ID of the route
    router_route_update = oxide.RouterRouteUpdate() # RouterRouteUpdate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    router = oxide.NameOrId() # NameOrId | Name or ID of the router (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC, only required if `router` is provided as a `Name` (optional)

    try:
        # Update route
        api_response = api_instance.vpc_router_route_update(route, router_route_update, project=project, router=router, vpc=vpc)
        print("The response of VpcsApi->vpc_router_route_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_route_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**NameOrId**](.md)| Name or ID of the route | 
 **router_route_update** | [**RouterRouteUpdate**](RouterRouteUpdate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **router** | [**NameOrId**](.md)| Name or ID of the router | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC, only required if &#x60;router&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**RouterRoute**](RouterRoute.md)

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

# **vpc_router_route_view**
> RouterRoute vpc_router_route_view(route, router, project=project, vpc=vpc)

Fetch route

### Example


```python
import oxide
from oxide.models.router_route import RouterRoute
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
    api_instance = oxide.VpcsApi(api_client)
    route = oxide.NameOrId() # NameOrId | Name or ID of the route
    router = oxide.NameOrId() # NameOrId | Name or ID of the router
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC, only required if `router` is provided as a `Name` (optional)

    try:
        # Fetch route
        api_response = api_instance.vpc_router_route_view(route, router, project=project, vpc=vpc)
        print("The response of VpcsApi->vpc_router_route_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_route_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**NameOrId**](.md)| Name or ID of the route | 
 **router** | [**NameOrId**](.md)| Name or ID of the router | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC, only required if &#x60;router&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**RouterRoute**](RouterRoute.md)

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

# **vpc_router_update**
> VpcRouter vpc_router_update(router, vpc_router_update, project=project, vpc=vpc)

Update router

### Example


```python
import oxide
from oxide.models.vpc_router import VpcRouter
from oxide.models.vpc_router_update import VpcRouterUpdate
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
    api_instance = oxide.VpcsApi(api_client)
    router = oxide.NameOrId() # NameOrId | Name or ID of the router
    vpc_router_update = oxide.VpcRouterUpdate() # VpcRouterUpdate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # Update router
        api_response = api_instance.vpc_router_update(router, vpc_router_update, project=project, vpc=vpc)
        print("The response of VpcsApi->vpc_router_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router** | [**NameOrId**](.md)| Name or ID of the router | 
 **vpc_router_update** | [**VpcRouterUpdate**](VpcRouterUpdate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

### Return type

[**VpcRouter**](VpcRouter.md)

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

# **vpc_router_view**
> VpcRouter vpc_router_view(router, project=project, vpc=vpc)

Fetch router

### Example


```python
import oxide
from oxide.models.vpc_router import VpcRouter
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
    api_instance = oxide.VpcsApi(api_client)
    router = oxide.NameOrId() # NameOrId | Name or ID of the router
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # Fetch router
        api_response = api_instance.vpc_router_view(router, project=project, vpc=vpc)
        print("The response of VpcsApi->vpc_router_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_router_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router** | [**NameOrId**](.md)| Name or ID of the router | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

### Return type

[**VpcRouter**](VpcRouter.md)

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

# **vpc_subnet_create**
> VpcSubnet vpc_subnet_create(vpc, vpc_subnet_create, project=project)

Create subnet

### Example


```python
import oxide
from oxide.models.vpc_subnet import VpcSubnet
from oxide.models.vpc_subnet_create import VpcSubnetCreate
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
    api_instance = oxide.VpcsApi(api_client)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC
    vpc_subnet_create = oxide.VpcSubnetCreate() # VpcSubnetCreate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)

    try:
        # Create subnet
        api_response = api_instance.vpc_subnet_create(vpc, vpc_subnet_create, project=project)
        print("The response of VpcsApi->vpc_subnet_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_subnet_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | 
 **vpc_subnet_create** | [**VpcSubnetCreate**](VpcSubnetCreate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**VpcSubnet**](VpcSubnet.md)

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

# **vpc_subnet_delete**
> vpc_subnet_delete(subnet, project=project, vpc=vpc)

Delete subnet

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
    api_instance = oxide.VpcsApi(api_client)
    subnet = oxide.NameOrId() # NameOrId | Name or ID of the subnet
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # Delete subnet
        api_instance.vpc_subnet_delete(subnet, project=project, vpc=vpc)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_subnet_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet** | [**NameOrId**](.md)| Name or ID of the subnet | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

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

# **vpc_subnet_list**
> VpcSubnetResultsPage vpc_subnet_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by, vpc=vpc)

List subnets

### Example


```python
import oxide
from oxide.models.vpc_subnet_results_page import VpcSubnetResultsPage
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
    api_instance = oxide.VpcsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # List subnets
        api_response = api_instance.vpc_subnet_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by, vpc=vpc)
        print("The response of VpcsApi->vpc_subnet_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_subnet_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

### Return type

[**VpcSubnetResultsPage**](VpcSubnetResultsPage.md)

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

# **vpc_subnet_list_network_interfaces**
> InstanceNetworkInterfaceResultsPage vpc_subnet_list_network_interfaces(subnet, limit=limit, page_token=page_token, project=project, sort_by=sort_by, vpc=vpc)

List network interfaces

### Example


```python
import oxide
from oxide.models.instance_network_interface_results_page import InstanceNetworkInterfaceResultsPage
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
    api_instance = oxide.VpcsApi(api_client)
    subnet = oxide.NameOrId() # NameOrId | Name or ID of the subnet
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # List network interfaces
        api_response = api_instance.vpc_subnet_list_network_interfaces(subnet, limit=limit, page_token=page_token, project=project, sort_by=sort_by, vpc=vpc)
        print("The response of VpcsApi->vpc_subnet_list_network_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_subnet_list_network_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet** | [**NameOrId**](.md)| Name or ID of the subnet | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

### Return type

[**InstanceNetworkInterfaceResultsPage**](InstanceNetworkInterfaceResultsPage.md)

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

# **vpc_subnet_update**
> VpcSubnet vpc_subnet_update(subnet, vpc_subnet_update, project=project, vpc=vpc)

Update subnet

### Example


```python
import oxide
from oxide.models.vpc_subnet import VpcSubnet
from oxide.models.vpc_subnet_update import VpcSubnetUpdate
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
    api_instance = oxide.VpcsApi(api_client)
    subnet = oxide.NameOrId() # NameOrId | Name or ID of the subnet
    vpc_subnet_update = oxide.VpcSubnetUpdate() # VpcSubnetUpdate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # Update subnet
        api_response = api_instance.vpc_subnet_update(subnet, vpc_subnet_update, project=project, vpc=vpc)
        print("The response of VpcsApi->vpc_subnet_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_subnet_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet** | [**NameOrId**](.md)| Name or ID of the subnet | 
 **vpc_subnet_update** | [**VpcSubnetUpdate**](VpcSubnetUpdate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

### Return type

[**VpcSubnet**](VpcSubnet.md)

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

# **vpc_subnet_view**
> VpcSubnet vpc_subnet_view(subnet, project=project, vpc=vpc)

Fetch subnet

### Example


```python
import oxide
from oxide.models.vpc_subnet import VpcSubnet
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
    api_instance = oxide.VpcsApi(api_client)
    subnet = oxide.NameOrId() # NameOrId | Name or ID of the subnet
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `vpc` is provided as a `Name` (optional)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC (optional)

    try:
        # Fetch subnet
        api_response = api_instance.vpc_subnet_view(subnet, project=project, vpc=vpc)
        print("The response of VpcsApi->vpc_subnet_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_subnet_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet** | [**NameOrId**](.md)| Name or ID of the subnet | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;vpc&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | [optional] 

### Return type

[**VpcSubnet**](VpcSubnet.md)

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

# **vpc_update**
> Vpc vpc_update(vpc, vpc_update, project=project)

Update a VPC

### Example


```python
import oxide
from oxide.models.vpc import Vpc
from oxide.models.vpc_update import VpcUpdate
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
    api_instance = oxide.VpcsApi(api_client)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC
    vpc_update = oxide.VpcUpdate() # VpcUpdate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Update a VPC
        api_response = api_instance.vpc_update(vpc, vpc_update, project=project)
        print("The response of VpcsApi->vpc_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | 
 **vpc_update** | [**VpcUpdate**](VpcUpdate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Vpc**](Vpc.md)

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

# **vpc_view**
> Vpc vpc_view(vpc, project=project)

Fetch VPC

### Example


```python
import oxide
from oxide.models.vpc import Vpc
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
    api_instance = oxide.VpcsApi(api_client)
    vpc = oxide.NameOrId() # NameOrId | Name or ID of the VPC
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Fetch VPC
        api_response = api_instance.vpc_view(vpc, project=project)
        print("The response of VpcsApi->vpc_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VpcsApi->vpc_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc** | [**NameOrId**](.md)| Name or ID of the VPC | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Vpc**](Vpc.md)

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

