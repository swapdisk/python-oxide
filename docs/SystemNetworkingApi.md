# oxide.SystemNetworkingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networking_address_lot_block_list**](SystemNetworkingApi.md#networking_address_lot_block_list) | **GET** /v1/system/networking/address-lot/{address_lot}/blocks | List blocks in address lot
[**networking_address_lot_create**](SystemNetworkingApi.md#networking_address_lot_create) | **POST** /v1/system/networking/address-lot | Create address lot
[**networking_address_lot_delete**](SystemNetworkingApi.md#networking_address_lot_delete) | **DELETE** /v1/system/networking/address-lot/{address_lot} | Delete address lot
[**networking_address_lot_list**](SystemNetworkingApi.md#networking_address_lot_list) | **GET** /v1/system/networking/address-lot | List address lots
[**networking_allow_list_update**](SystemNetworkingApi.md#networking_allow_list_update) | **PUT** /v1/system/networking/allow-list | Update user-facing services IP allowlist
[**networking_allow_list_view**](SystemNetworkingApi.md#networking_allow_list_view) | **GET** /v1/system/networking/allow-list | Get user-facing services IP allowlist
[**networking_bfd_disable**](SystemNetworkingApi.md#networking_bfd_disable) | **POST** /v1/system/networking/bfd-disable | Disable a BFD session
[**networking_bfd_enable**](SystemNetworkingApi.md#networking_bfd_enable) | **POST** /v1/system/networking/bfd-enable | Enable a BFD session
[**networking_bfd_status**](SystemNetworkingApi.md#networking_bfd_status) | **GET** /v1/system/networking/bfd-status | Get BFD status
[**networking_bgp_announce_set_delete**](SystemNetworkingApi.md#networking_bgp_announce_set_delete) | **DELETE** /v1/system/networking/bgp-announce-set/{name_or_id} | Delete BGP announce set
[**networking_bgp_announce_set_list**](SystemNetworkingApi.md#networking_bgp_announce_set_list) | **GET** /v1/system/networking/bgp-announce-set | List BGP announce sets
[**networking_bgp_announce_set_update**](SystemNetworkingApi.md#networking_bgp_announce_set_update) | **PUT** /v1/system/networking/bgp-announce-set | Update BGP announce set
[**networking_bgp_announcement_list**](SystemNetworkingApi.md#networking_bgp_announcement_list) | **GET** /v1/system/networking/bgp-announce-set/{name_or_id}/announcement | Get originated routes for a specified BGP announce set
[**networking_bgp_config_create**](SystemNetworkingApi.md#networking_bgp_config_create) | **POST** /v1/system/networking/bgp | Create new BGP configuration
[**networking_bgp_config_delete**](SystemNetworkingApi.md#networking_bgp_config_delete) | **DELETE** /v1/system/networking/bgp | Delete BGP configuration
[**networking_bgp_config_list**](SystemNetworkingApi.md#networking_bgp_config_list) | **GET** /v1/system/networking/bgp | List BGP configurations
[**networking_bgp_exported**](SystemNetworkingApi.md#networking_bgp_exported) | **GET** /v1/system/networking/bgp-exported | Get BGP exported routes
[**networking_bgp_imported_routes_ipv4**](SystemNetworkingApi.md#networking_bgp_imported_routes_ipv4) | **GET** /v1/system/networking/bgp-routes-ipv4 | Get imported IPv4 BGP routes
[**networking_bgp_message_history**](SystemNetworkingApi.md#networking_bgp_message_history) | **GET** /v1/system/networking/bgp-message-history | Get BGP router message history
[**networking_bgp_status**](SystemNetworkingApi.md#networking_bgp_status) | **GET** /v1/system/networking/bgp-status | Get BGP peer status
[**networking_loopback_address_create**](SystemNetworkingApi.md#networking_loopback_address_create) | **POST** /v1/system/networking/loopback-address | Create loopback address
[**networking_loopback_address_delete**](SystemNetworkingApi.md#networking_loopback_address_delete) | **DELETE** /v1/system/networking/loopback-address/{rack_id}/{switch_location}/{address}/{subnet_mask} | Delete loopback address
[**networking_loopback_address_list**](SystemNetworkingApi.md#networking_loopback_address_list) | **GET** /v1/system/networking/loopback-address | List loopback addresses
[**networking_switch_port_settings_create**](SystemNetworkingApi.md#networking_switch_port_settings_create) | **POST** /v1/system/networking/switch-port-settings | Create switch port settings
[**networking_switch_port_settings_delete**](SystemNetworkingApi.md#networking_switch_port_settings_delete) | **DELETE** /v1/system/networking/switch-port-settings | Delete switch port settings
[**networking_switch_port_settings_list**](SystemNetworkingApi.md#networking_switch_port_settings_list) | **GET** /v1/system/networking/switch-port-settings | List switch port settings
[**networking_switch_port_settings_view**](SystemNetworkingApi.md#networking_switch_port_settings_view) | **GET** /v1/system/networking/switch-port-settings/{port} | Get information about switch port


# **networking_address_lot_block_list**
> AddressLotBlockResultsPage networking_address_lot_block_list(address_lot, limit=limit, page_token=page_token, sort_by=sort_by)

List blocks in address lot

### Example


```python
import oxide
from oxide.models.address_lot_block_results_page import AddressLotBlockResultsPage
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    address_lot = oxide.NameOrId() # NameOrId | Name or ID of the address lot
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List blocks in address lot
        api_response = api_instance.networking_address_lot_block_list(address_lot, limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemNetworkingApi->networking_address_lot_block_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_address_lot_block_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_lot** | [**NameOrId**](.md)| Name or ID of the address lot | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**AddressLotBlockResultsPage**](AddressLotBlockResultsPage.md)

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

# **networking_address_lot_create**
> AddressLotCreateResponse networking_address_lot_create(address_lot_create)

Create address lot

### Example


```python
import oxide
from oxide.models.address_lot_create import AddressLotCreate
from oxide.models.address_lot_create_response import AddressLotCreateResponse
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    address_lot_create = oxide.AddressLotCreate() # AddressLotCreate | 

    try:
        # Create address lot
        api_response = api_instance.networking_address_lot_create(address_lot_create)
        print("The response of SystemNetworkingApi->networking_address_lot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_address_lot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_lot_create** | [**AddressLotCreate**](AddressLotCreate.md)|  | 

### Return type

[**AddressLotCreateResponse**](AddressLotCreateResponse.md)

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

# **networking_address_lot_delete**
> networking_address_lot_delete(address_lot)

Delete address lot

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
    api_instance = oxide.SystemNetworkingApi(api_client)
    address_lot = oxide.NameOrId() # NameOrId | Name or ID of the address lot

    try:
        # Delete address lot
        api_instance.networking_address_lot_delete(address_lot)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_address_lot_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_lot** | [**NameOrId**](.md)| Name or ID of the address lot | 

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

# **networking_address_lot_list**
> AddressLotResultsPage networking_address_lot_list(limit=limit, page_token=page_token, sort_by=sort_by)

List address lots

### Example


```python
import oxide
from oxide.models.address_lot_results_page import AddressLotResultsPage
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List address lots
        api_response = api_instance.networking_address_lot_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemNetworkingApi->networking_address_lot_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_address_lot_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**AddressLotResultsPage**](AddressLotResultsPage.md)

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

# **networking_allow_list_update**
> AllowList networking_allow_list_update(allow_list_update)

Update user-facing services IP allowlist

### Example


```python
import oxide
from oxide.models.allow_list import AllowList
from oxide.models.allow_list_update import AllowListUpdate
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    allow_list_update = oxide.AllowListUpdate() # AllowListUpdate | 

    try:
        # Update user-facing services IP allowlist
        api_response = api_instance.networking_allow_list_update(allow_list_update)
        print("The response of SystemNetworkingApi->networking_allow_list_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_allow_list_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_list_update** | [**AllowListUpdate**](AllowListUpdate.md)|  | 

### Return type

[**AllowList**](AllowList.md)

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

# **networking_allow_list_view**
> AllowList networking_allow_list_view()

Get user-facing services IP allowlist

### Example


```python
import oxide
from oxide.models.allow_list import AllowList
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
    api_instance = oxide.SystemNetworkingApi(api_client)

    try:
        # Get user-facing services IP allowlist
        api_response = api_instance.networking_allow_list_view()
        print("The response of SystemNetworkingApi->networking_allow_list_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_allow_list_view: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AllowList**](AllowList.md)

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

# **networking_bfd_disable**
> networking_bfd_disable(bfd_session_disable)

Disable a BFD session

### Example


```python
import oxide
from oxide.models.bfd_session_disable import BfdSessionDisable
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    bfd_session_disable = oxide.BfdSessionDisable() # BfdSessionDisable | 

    try:
        # Disable a BFD session
        api_instance.networking_bfd_disable(bfd_session_disable)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bfd_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bfd_session_disable** | [**BfdSessionDisable**](BfdSessionDisable.md)|  | 

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

# **networking_bfd_enable**
> networking_bfd_enable(bfd_session_enable)

Enable a BFD session

### Example


```python
import oxide
from oxide.models.bfd_session_enable import BfdSessionEnable
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    bfd_session_enable = oxide.BfdSessionEnable() # BfdSessionEnable | 

    try:
        # Enable a BFD session
        api_instance.networking_bfd_enable(bfd_session_enable)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bfd_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bfd_session_enable** | [**BfdSessionEnable**](BfdSessionEnable.md)|  | 

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

# **networking_bfd_status**
> List[BfdStatus] networking_bfd_status()

Get BFD status

### Example


```python
import oxide
from oxide.models.bfd_status import BfdStatus
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
    api_instance = oxide.SystemNetworkingApi(api_client)

    try:
        # Get BFD status
        api_response = api_instance.networking_bfd_status()
        print("The response of SystemNetworkingApi->networking_bfd_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bfd_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BfdStatus]**](BfdStatus.md)

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

# **networking_bgp_announce_set_delete**
> networking_bgp_announce_set_delete(name_or_id)

Delete BGP announce set

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
    api_instance = oxide.SystemNetworkingApi(api_client)
    name_or_id = oxide.NameOrId() # NameOrId | A name or id to use when selecting BGP port settings

    try:
        # Delete BGP announce set
        api_instance.networking_bgp_announce_set_delete(name_or_id)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_announce_set_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_or_id** | [**NameOrId**](.md)| A name or id to use when selecting BGP port settings | 

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

# **networking_bgp_announce_set_list**
> List[BgpAnnounceSet] networking_bgp_announce_set_list(limit=limit, name_or_id=name_or_id, page_token=page_token, sort_by=sort_by)

List BGP announce sets

### Example


```python
import oxide
from oxide.models.bgp_announce_set import BgpAnnounceSet
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    name_or_id = oxide.NameOrId() # NameOrId | A name or id to use when s electing BGP port settings (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List BGP announce sets
        api_response = api_instance.networking_bgp_announce_set_list(limit=limit, name_or_id=name_or_id, page_token=page_token, sort_by=sort_by)
        print("The response of SystemNetworkingApi->networking_bgp_announce_set_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_announce_set_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **name_or_id** | [**NameOrId**](.md)| A name or id to use when s electing BGP port settings | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**List[BgpAnnounceSet]**](BgpAnnounceSet.md)

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

# **networking_bgp_announce_set_update**
> BgpAnnounceSet networking_bgp_announce_set_update(bgp_announce_set_create)

Update BGP announce set

If the announce set exists, this endpoint replaces the existing announce set with the one specified.

### Example


```python
import oxide
from oxide.models.bgp_announce_set import BgpAnnounceSet
from oxide.models.bgp_announce_set_create import BgpAnnounceSetCreate
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    bgp_announce_set_create = oxide.BgpAnnounceSetCreate() # BgpAnnounceSetCreate | 

    try:
        # Update BGP announce set
        api_response = api_instance.networking_bgp_announce_set_update(bgp_announce_set_create)
        print("The response of SystemNetworkingApi->networking_bgp_announce_set_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_announce_set_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_announce_set_create** | [**BgpAnnounceSetCreate**](BgpAnnounceSetCreate.md)|  | 

### Return type

[**BgpAnnounceSet**](BgpAnnounceSet.md)

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

# **networking_bgp_announcement_list**
> List[BgpAnnouncement] networking_bgp_announcement_list(name_or_id)

Get originated routes for a specified BGP announce set

### Example


```python
import oxide
from oxide.models.bgp_announcement import BgpAnnouncement
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    name_or_id = oxide.NameOrId() # NameOrId | A name or id to use when selecting BGP port settings

    try:
        # Get originated routes for a specified BGP announce set
        api_response = api_instance.networking_bgp_announcement_list(name_or_id)
        print("The response of SystemNetworkingApi->networking_bgp_announcement_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_announcement_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_or_id** | [**NameOrId**](.md)| A name or id to use when selecting BGP port settings | 

### Return type

[**List[BgpAnnouncement]**](BgpAnnouncement.md)

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

# **networking_bgp_config_create**
> BgpConfig networking_bgp_config_create(bgp_config_create)

Create new BGP configuration

### Example


```python
import oxide
from oxide.models.bgp_config import BgpConfig
from oxide.models.bgp_config_create import BgpConfigCreate
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    bgp_config_create = oxide.BgpConfigCreate() # BgpConfigCreate | 

    try:
        # Create new BGP configuration
        api_response = api_instance.networking_bgp_config_create(bgp_config_create)
        print("The response of SystemNetworkingApi->networking_bgp_config_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_config_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_config_create** | [**BgpConfigCreate**](BgpConfigCreate.md)|  | 

### Return type

[**BgpConfig**](BgpConfig.md)

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

# **networking_bgp_config_delete**
> networking_bgp_config_delete(name_or_id)

Delete BGP configuration

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
    api_instance = oxide.SystemNetworkingApi(api_client)
    name_or_id = oxide.NameOrId() # NameOrId | A name or id to use when selecting BGP config.

    try:
        # Delete BGP configuration
        api_instance.networking_bgp_config_delete(name_or_id)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_config_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_or_id** | [**NameOrId**](.md)| A name or id to use when selecting BGP config. | 

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

# **networking_bgp_config_list**
> BgpConfigResultsPage networking_bgp_config_list(limit=limit, name_or_id=name_or_id, page_token=page_token, sort_by=sort_by)

List BGP configurations

### Example


```python
import oxide
from oxide.models.bgp_config_results_page import BgpConfigResultsPage
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    name_or_id = oxide.NameOrId() # NameOrId | A name or id to use when selecting BGP config. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List BGP configurations
        api_response = api_instance.networking_bgp_config_list(limit=limit, name_or_id=name_or_id, page_token=page_token, sort_by=sort_by)
        print("The response of SystemNetworkingApi->networking_bgp_config_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_config_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **name_or_id** | [**NameOrId**](.md)| A name or id to use when selecting BGP config. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**BgpConfigResultsPage**](BgpConfigResultsPage.md)

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

# **networking_bgp_exported**
> BgpExported networking_bgp_exported()

Get BGP exported routes

### Example


```python
import oxide
from oxide.models.bgp_exported import BgpExported
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
    api_instance = oxide.SystemNetworkingApi(api_client)

    try:
        # Get BGP exported routes
        api_response = api_instance.networking_bgp_exported()
        print("The response of SystemNetworkingApi->networking_bgp_exported:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_exported: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BgpExported**](BgpExported.md)

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

# **networking_bgp_imported_routes_ipv4**
> List[BgpImportedRouteIpv4] networking_bgp_imported_routes_ipv4(asn)

Get imported IPv4 BGP routes

### Example


```python
import oxide
from oxide.models.bgp_imported_route_ipv4 import BgpImportedRouteIpv4
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    asn = 56 # int | The ASN to filter on. Required.

    try:
        # Get imported IPv4 BGP routes
        api_response = api_instance.networking_bgp_imported_routes_ipv4(asn)
        print("The response of SystemNetworkingApi->networking_bgp_imported_routes_ipv4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_imported_routes_ipv4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn** | **int**| The ASN to filter on. Required. | 

### Return type

[**List[BgpImportedRouteIpv4]**](BgpImportedRouteIpv4.md)

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

# **networking_bgp_message_history**
> AggregateBgpMessageHistory networking_bgp_message_history(asn)

Get BGP router message history

### Example


```python
import oxide
from oxide.models.aggregate_bgp_message_history import AggregateBgpMessageHistory
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    asn = 56 # int | The ASN to filter on. Required.

    try:
        # Get BGP router message history
        api_response = api_instance.networking_bgp_message_history(asn)
        print("The response of SystemNetworkingApi->networking_bgp_message_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_message_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn** | **int**| The ASN to filter on. Required. | 

### Return type

[**AggregateBgpMessageHistory**](AggregateBgpMessageHistory.md)

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

# **networking_bgp_status**
> List[BgpPeerStatus] networking_bgp_status()

Get BGP peer status

### Example


```python
import oxide
from oxide.models.bgp_peer_status import BgpPeerStatus
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
    api_instance = oxide.SystemNetworkingApi(api_client)

    try:
        # Get BGP peer status
        api_response = api_instance.networking_bgp_status()
        print("The response of SystemNetworkingApi->networking_bgp_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_bgp_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BgpPeerStatus]**](BgpPeerStatus.md)

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

# **networking_loopback_address_create**
> LoopbackAddress networking_loopback_address_create(loopback_address_create)

Create loopback address

### Example


```python
import oxide
from oxide.models.loopback_address import LoopbackAddress
from oxide.models.loopback_address_create import LoopbackAddressCreate
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    loopback_address_create = oxide.LoopbackAddressCreate() # LoopbackAddressCreate | 

    try:
        # Create loopback address
        api_response = api_instance.networking_loopback_address_create(loopback_address_create)
        print("The response of SystemNetworkingApi->networking_loopback_address_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_loopback_address_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loopback_address_create** | [**LoopbackAddressCreate**](LoopbackAddressCreate.md)|  | 

### Return type

[**LoopbackAddress**](LoopbackAddress.md)

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

# **networking_loopback_address_delete**
> networking_loopback_address_delete(address, rack_id, subnet_mask, switch_location)

Delete loopback address

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
    api_instance = oxide.SystemNetworkingApi(api_client)
    address = 'address_example' # str | The IP address and subnet mask to use when selecting the loopback address.
    rack_id = 'rack_id_example' # str | The rack to use when selecting the loopback address.
    subnet_mask = 56 # int | The IP address and subnet mask to use when selecting the loopback address.
    switch_location = 'switch_location_example' # str | The switch location to use when selecting the loopback address.

    try:
        # Delete loopback address
        api_instance.networking_loopback_address_delete(address, rack_id, subnet_mask, switch_location)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_loopback_address_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The IP address and subnet mask to use when selecting the loopback address. | 
 **rack_id** | **str**| The rack to use when selecting the loopback address. | 
 **subnet_mask** | **int**| The IP address and subnet mask to use when selecting the loopback address. | 
 **switch_location** | **str**| The switch location to use when selecting the loopback address. | 

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

# **networking_loopback_address_list**
> LoopbackAddressResultsPage networking_loopback_address_list(limit=limit, page_token=page_token, sort_by=sort_by)

List loopback addresses

### Example


```python
import oxide
from oxide.models.loopback_address_results_page import LoopbackAddressResultsPage
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List loopback addresses
        api_response = api_instance.networking_loopback_address_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemNetworkingApi->networking_loopback_address_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_loopback_address_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**LoopbackAddressResultsPage**](LoopbackAddressResultsPage.md)

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

# **networking_switch_port_settings_create**
> SwitchPortSettingsView networking_switch_port_settings_create(switch_port_settings_create)

Create switch port settings

### Example


```python
import oxide
from oxide.models.switch_port_settings_create import SwitchPortSettingsCreate
from oxide.models.switch_port_settings_view import SwitchPortSettingsView
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    switch_port_settings_create = oxide.SwitchPortSettingsCreate() # SwitchPortSettingsCreate | 

    try:
        # Create switch port settings
        api_response = api_instance.networking_switch_port_settings_create(switch_port_settings_create)
        print("The response of SystemNetworkingApi->networking_switch_port_settings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_switch_port_settings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_port_settings_create** | [**SwitchPortSettingsCreate**](SwitchPortSettingsCreate.md)|  | 

### Return type

[**SwitchPortSettingsView**](SwitchPortSettingsView.md)

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

# **networking_switch_port_settings_delete**
> networking_switch_port_settings_delete(port_settings=port_settings)

Delete switch port settings

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
    api_instance = oxide.SystemNetworkingApi(api_client)
    port_settings = oxide.NameOrId() # NameOrId | An optional name or id to use when selecting port settings. (optional)

    try:
        # Delete switch port settings
        api_instance.networking_switch_port_settings_delete(port_settings=port_settings)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_switch_port_settings_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_settings** | [**NameOrId**](.md)| An optional name or id to use when selecting port settings. | [optional] 

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

# **networking_switch_port_settings_list**
> SwitchPortSettingsResultsPage networking_switch_port_settings_list(limit=limit, page_token=page_token, port_settings=port_settings, sort_by=sort_by)

List switch port settings

### Example


```python
import oxide
from oxide.models.switch_port_settings_results_page import SwitchPortSettingsResultsPage
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    port_settings = oxide.NameOrId() # NameOrId | An optional name or id to use when selecting port settings. (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List switch port settings
        api_response = api_instance.networking_switch_port_settings_list(limit=limit, page_token=page_token, port_settings=port_settings, sort_by=sort_by)
        print("The response of SystemNetworkingApi->networking_switch_port_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_switch_port_settings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **port_settings** | [**NameOrId**](.md)| An optional name or id to use when selecting port settings. | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**SwitchPortSettingsResultsPage**](SwitchPortSettingsResultsPage.md)

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

# **networking_switch_port_settings_view**
> SwitchPortSettingsView networking_switch_port_settings_view(port)

Get information about switch port

### Example


```python
import oxide
from oxide.models.switch_port_settings_view import SwitchPortSettingsView
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
    api_instance = oxide.SystemNetworkingApi(api_client)
    port = oxide.NameOrId() # NameOrId | A name or id to use when selecting switch port settings info objects.

    try:
        # Get information about switch port
        api_response = api_instance.networking_switch_port_settings_view(port)
        print("The response of SystemNetworkingApi->networking_switch_port_settings_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemNetworkingApi->networking_switch_port_settings_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | [**NameOrId**](.md)| A name or id to use when selecting switch port settings info objects. | 

### Return type

[**SwitchPortSettingsView**](SwitchPortSettingsView.md)

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

