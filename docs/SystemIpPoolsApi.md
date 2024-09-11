# oxide.SystemIpPoolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_pool_create**](SystemIpPoolsApi.md#ip_pool_create) | **POST** /v1/system/ip-pools | Create IP pool
[**ip_pool_delete**](SystemIpPoolsApi.md#ip_pool_delete) | **DELETE** /v1/system/ip-pools/{pool} | Delete IP pool
[**ip_pool_list**](SystemIpPoolsApi.md#ip_pool_list) | **GET** /v1/system/ip-pools | List IP pools
[**ip_pool_range_add**](SystemIpPoolsApi.md#ip_pool_range_add) | **POST** /v1/system/ip-pools/{pool}/ranges/add | Add range to IP pool
[**ip_pool_range_list**](SystemIpPoolsApi.md#ip_pool_range_list) | **GET** /v1/system/ip-pools/{pool}/ranges | List ranges for IP pool
[**ip_pool_range_remove**](SystemIpPoolsApi.md#ip_pool_range_remove) | **POST** /v1/system/ip-pools/{pool}/ranges/remove | Remove range from IP pool
[**ip_pool_service_range_add**](SystemIpPoolsApi.md#ip_pool_service_range_add) | **POST** /v1/system/ip-pools-service/ranges/add | Add IP range to Oxide service pool
[**ip_pool_service_range_list**](SystemIpPoolsApi.md#ip_pool_service_range_list) | **GET** /v1/system/ip-pools-service/ranges | List IP ranges for the Oxide service pool
[**ip_pool_service_range_remove**](SystemIpPoolsApi.md#ip_pool_service_range_remove) | **POST** /v1/system/ip-pools-service/ranges/remove | Remove IP range from Oxide service pool
[**ip_pool_service_view**](SystemIpPoolsApi.md#ip_pool_service_view) | **GET** /v1/system/ip-pools-service | Fetch Oxide service IP pool
[**ip_pool_silo_link**](SystemIpPoolsApi.md#ip_pool_silo_link) | **POST** /v1/system/ip-pools/{pool}/silos | Link IP pool to silo
[**ip_pool_silo_list**](SystemIpPoolsApi.md#ip_pool_silo_list) | **GET** /v1/system/ip-pools/{pool}/silos | List IP pool&#39;s linked silos
[**ip_pool_silo_unlink**](SystemIpPoolsApi.md#ip_pool_silo_unlink) | **DELETE** /v1/system/ip-pools/{pool}/silos/{silo} | Unlink IP pool from silo
[**ip_pool_silo_update**](SystemIpPoolsApi.md#ip_pool_silo_update) | **PUT** /v1/system/ip-pools/{pool}/silos/{silo} | Make IP pool default for silo
[**ip_pool_update**](SystemIpPoolsApi.md#ip_pool_update) | **PUT** /v1/system/ip-pools/{pool} | Update IP pool
[**ip_pool_utilization_view**](SystemIpPoolsApi.md#ip_pool_utilization_view) | **GET** /v1/system/ip-pools/{pool}/utilization | Fetch IP pool utilization
[**ip_pool_view**](SystemIpPoolsApi.md#ip_pool_view) | **GET** /v1/system/ip-pools/{pool} | Fetch IP pool


# **ip_pool_create**
> IpPool ip_pool_create(ip_pool_create)

Create IP pool

### Example


```python
import oxide
from oxide.models.ip_pool import IpPool
from oxide.models.ip_pool_create import IpPoolCreate
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    ip_pool_create = oxide.IpPoolCreate() # IpPoolCreate | 

    try:
        # Create IP pool
        api_response = api_instance.ip_pool_create(ip_pool_create)
        print("The response of SystemIpPoolsApi->ip_pool_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_pool_create** | [**IpPoolCreate**](IpPoolCreate.md)|  | 

### Return type

[**IpPool**](IpPool.md)

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

# **ip_pool_delete**
> ip_pool_delete(pool)

Delete IP pool

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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool

    try:
        # Delete IP pool
        api_instance.ip_pool_delete(pool)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 

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

# **ip_pool_list**
> IpPoolResultsPage ip_pool_list(limit=limit, page_token=page_token, sort_by=sort_by)

List IP pools

### Example


```python
import oxide
from oxide.models.ip_pool_results_page import IpPoolResultsPage
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List IP pools
        api_response = api_instance.ip_pool_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemIpPoolsApi->ip_pool_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**IpPoolResultsPage**](IpPoolResultsPage.md)

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

# **ip_pool_range_add**
> IpPoolRange ip_pool_range_add(pool, ip_range)

Add range to IP pool

IPv6 ranges are not allowed yet.

### Example


```python
import oxide
from oxide.models.ip_pool_range import IpPoolRange
from oxide.models.ip_range import IpRange
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool
    ip_range = oxide.IpRange() # IpRange | 

    try:
        # Add range to IP pool
        api_response = api_instance.ip_pool_range_add(pool, ip_range)
        print("The response of SystemIpPoolsApi->ip_pool_range_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_range_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 
 **ip_range** | [**IpRange**](IpRange.md)|  | 

### Return type

[**IpPoolRange**](IpPoolRange.md)

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

# **ip_pool_range_list**
> IpPoolRangeResultsPage ip_pool_range_list(pool, limit=limit, page_token=page_token)

List ranges for IP pool

Ranges are ordered by their first address.

### Example


```python
import oxide
from oxide.models.ip_pool_range_results_page import IpPoolRangeResultsPage
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)

    try:
        # List ranges for IP pool
        api_response = api_instance.ip_pool_range_list(pool, limit=limit, page_token=page_token)
        print("The response of SystemIpPoolsApi->ip_pool_range_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_range_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 

### Return type

[**IpPoolRangeResultsPage**](IpPoolRangeResultsPage.md)

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

# **ip_pool_range_remove**
> ip_pool_range_remove(pool, ip_range)

Remove range from IP pool

### Example


```python
import oxide
from oxide.models.ip_range import IpRange
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool
    ip_range = oxide.IpRange() # IpRange | 

    try:
        # Remove range from IP pool
        api_instance.ip_pool_range_remove(pool, ip_range)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_range_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 
 **ip_range** | [**IpRange**](IpRange.md)|  | 

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

# **ip_pool_service_range_add**
> IpPoolRange ip_pool_service_range_add(ip_range)

Add IP range to Oxide service pool

IPv6 ranges are not allowed yet.

### Example


```python
import oxide
from oxide.models.ip_pool_range import IpPoolRange
from oxide.models.ip_range import IpRange
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    ip_range = oxide.IpRange() # IpRange | 

    try:
        # Add IP range to Oxide service pool
        api_response = api_instance.ip_pool_service_range_add(ip_range)
        print("The response of SystemIpPoolsApi->ip_pool_service_range_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_service_range_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_range** | [**IpRange**](IpRange.md)|  | 

### Return type

[**IpPoolRange**](IpPoolRange.md)

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

# **ip_pool_service_range_list**
> IpPoolRangeResultsPage ip_pool_service_range_list(limit=limit, page_token=page_token)

List IP ranges for the Oxide service pool

Ranges are ordered by their first address.

### Example


```python
import oxide
from oxide.models.ip_pool_range_results_page import IpPoolRangeResultsPage
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)

    try:
        # List IP ranges for the Oxide service pool
        api_response = api_instance.ip_pool_service_range_list(limit=limit, page_token=page_token)
        print("The response of SystemIpPoolsApi->ip_pool_service_range_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_service_range_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 

### Return type

[**IpPoolRangeResultsPage**](IpPoolRangeResultsPage.md)

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

# **ip_pool_service_range_remove**
> ip_pool_service_range_remove(ip_range)

Remove IP range from Oxide service pool

### Example


```python
import oxide
from oxide.models.ip_range import IpRange
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    ip_range = oxide.IpRange() # IpRange | 

    try:
        # Remove IP range from Oxide service pool
        api_instance.ip_pool_service_range_remove(ip_range)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_service_range_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_range** | [**IpRange**](IpRange.md)|  | 

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

# **ip_pool_service_view**
> IpPool ip_pool_service_view()

Fetch Oxide service IP pool

### Example


```python
import oxide
from oxide.models.ip_pool import IpPool
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
    api_instance = oxide.SystemIpPoolsApi(api_client)

    try:
        # Fetch Oxide service IP pool
        api_response = api_instance.ip_pool_service_view()
        print("The response of SystemIpPoolsApi->ip_pool_service_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_service_view: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IpPool**](IpPool.md)

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

# **ip_pool_silo_link**
> IpPoolSiloLink ip_pool_silo_link(pool, ip_pool_link_silo)

Link IP pool to silo

Users in linked silos can allocate external IPs from this pool for their instances. A silo can have at most one default pool. IPs are allocated from the default pool when users ask for one without specifying a pool.

### Example


```python
import oxide
from oxide.models.ip_pool_link_silo import IpPoolLinkSilo
from oxide.models.ip_pool_silo_link import IpPoolSiloLink
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool
    ip_pool_link_silo = oxide.IpPoolLinkSilo() # IpPoolLinkSilo | 

    try:
        # Link IP pool to silo
        api_response = api_instance.ip_pool_silo_link(pool, ip_pool_link_silo)
        print("The response of SystemIpPoolsApi->ip_pool_silo_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_silo_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 
 **ip_pool_link_silo** | [**IpPoolLinkSilo**](IpPoolLinkSilo.md)|  | 

### Return type

[**IpPoolSiloLink**](IpPoolSiloLink.md)

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

# **ip_pool_silo_list**
> IpPoolSiloLinkResultsPage ip_pool_silo_list(pool, limit=limit, page_token=page_token, sort_by=sort_by)

List IP pool's linked silos

### Example


```python
import oxide
from oxide.models.ip_pool_silo_link_results_page import IpPoolSiloLinkResultsPage
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List IP pool's linked silos
        api_response = api_instance.ip_pool_silo_list(pool, limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemIpPoolsApi->ip_pool_silo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_silo_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**IpPoolSiloLinkResultsPage**](IpPoolSiloLinkResultsPage.md)

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

# **ip_pool_silo_unlink**
> ip_pool_silo_unlink(pool, silo)

Unlink IP pool from silo

Will fail if there are any outstanding IPs allocated in the silo.

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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | 
    silo = oxide.NameOrId() # NameOrId | 

    try:
        # Unlink IP pool from silo
        api_instance.ip_pool_silo_unlink(pool, silo)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_silo_unlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)|  | 
 **silo** | [**NameOrId**](.md)|  | 

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

# **ip_pool_silo_update**
> IpPoolSiloLink ip_pool_silo_update(pool, silo, ip_pool_silo_update)

Make IP pool default for silo

When a user asks for an IP (e.g., at instance create time) without specifying a pool, the IP comes from the default pool if a default is configured. When a pool is made the default for a silo, any existing default will remain linked to the silo, but will no longer be the default.

### Example


```python
import oxide
from oxide.models.ip_pool_silo_link import IpPoolSiloLink
from oxide.models.ip_pool_silo_update import IpPoolSiloUpdate
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | 
    silo = oxide.NameOrId() # NameOrId | 
    ip_pool_silo_update = oxide.IpPoolSiloUpdate() # IpPoolSiloUpdate | 

    try:
        # Make IP pool default for silo
        api_response = api_instance.ip_pool_silo_update(pool, silo, ip_pool_silo_update)
        print("The response of SystemIpPoolsApi->ip_pool_silo_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_silo_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)|  | 
 **silo** | [**NameOrId**](.md)|  | 
 **ip_pool_silo_update** | [**IpPoolSiloUpdate**](IpPoolSiloUpdate.md)|  | 

### Return type

[**IpPoolSiloLink**](IpPoolSiloLink.md)

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

# **ip_pool_update**
> IpPool ip_pool_update(pool, ip_pool_update)

Update IP pool

### Example


```python
import oxide
from oxide.models.ip_pool import IpPool
from oxide.models.ip_pool_update import IpPoolUpdate
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool
    ip_pool_update = oxide.IpPoolUpdate() # IpPoolUpdate | 

    try:
        # Update IP pool
        api_response = api_instance.ip_pool_update(pool, ip_pool_update)
        print("The response of SystemIpPoolsApi->ip_pool_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 
 **ip_pool_update** | [**IpPoolUpdate**](IpPoolUpdate.md)|  | 

### Return type

[**IpPool**](IpPool.md)

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

# **ip_pool_utilization_view**
> IpPoolUtilization ip_pool_utilization_view(pool)

Fetch IP pool utilization

### Example


```python
import oxide
from oxide.models.ip_pool_utilization import IpPoolUtilization
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool

    try:
        # Fetch IP pool utilization
        api_response = api_instance.ip_pool_utilization_view(pool)
        print("The response of SystemIpPoolsApi->ip_pool_utilization_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_utilization_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 

### Return type

[**IpPoolUtilization**](IpPoolUtilization.md)

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

# **ip_pool_view**
> IpPool ip_pool_view(pool)

Fetch IP pool

### Example


```python
import oxide
from oxide.models.ip_pool import IpPool
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
    api_instance = oxide.SystemIpPoolsApi(api_client)
    pool = oxide.NameOrId() # NameOrId | Name or ID of the IP pool

    try:
        # Fetch IP pool
        api_response = api_instance.ip_pool_view(pool)
        print("The response of SystemIpPoolsApi->ip_pool_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemIpPoolsApi->ip_pool_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**NameOrId**](.md)| Name or ID of the IP pool | 

### Return type

[**IpPool**](IpPool.md)

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

