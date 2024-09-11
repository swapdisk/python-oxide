# oxide.SystemHardwareApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networking_switch_port_apply_settings**](SystemHardwareApi.md#networking_switch_port_apply_settings) | **POST** /v1/system/hardware/switch-port/{port}/settings | Apply switch port settings
[**networking_switch_port_clear_settings**](SystemHardwareApi.md#networking_switch_port_clear_settings) | **DELETE** /v1/system/hardware/switch-port/{port}/settings | Clear switch port settings
[**networking_switch_port_list**](SystemHardwareApi.md#networking_switch_port_list) | **GET** /v1/system/hardware/switch-port | List switch ports
[**networking_switch_port_status**](SystemHardwareApi.md#networking_switch_port_status) | **GET** /v1/system/hardware/switch-port/{port}/status | Get switch port status
[**physical_disk_list**](SystemHardwareApi.md#physical_disk_list) | **GET** /v1/system/hardware/disks | List physical disks
[**physical_disk_view**](SystemHardwareApi.md#physical_disk_view) | **GET** /v1/system/hardware/disks/{disk_id} | Get a physical disk
[**rack_list**](SystemHardwareApi.md#rack_list) | **GET** /v1/system/hardware/racks | List racks
[**rack_view**](SystemHardwareApi.md#rack_view) | **GET** /v1/system/hardware/racks/{rack_id} | Fetch rack
[**sled_add**](SystemHardwareApi.md#sled_add) | **POST** /v1/system/hardware/sleds | Add sled to initialized rack
[**sled_instance_list**](SystemHardwareApi.md#sled_instance_list) | **GET** /v1/system/hardware/sleds/{sled_id}/instances | List instances running on given sled
[**sled_list**](SystemHardwareApi.md#sled_list) | **GET** /v1/system/hardware/sleds | List sleds
[**sled_list_uninitialized**](SystemHardwareApi.md#sled_list_uninitialized) | **GET** /v1/system/hardware/sleds-uninitialized | List uninitialized sleds
[**sled_physical_disk_list**](SystemHardwareApi.md#sled_physical_disk_list) | **GET** /v1/system/hardware/sleds/{sled_id}/disks | List physical disks attached to sleds
[**sled_set_provision_policy**](SystemHardwareApi.md#sled_set_provision_policy) | **PUT** /v1/system/hardware/sleds/{sled_id}/provision-policy | Set sled provision policy
[**sled_view**](SystemHardwareApi.md#sled_view) | **GET** /v1/system/hardware/sleds/{sled_id} | Fetch sled
[**switch_list**](SystemHardwareApi.md#switch_list) | **GET** /v1/system/hardware/switches | List switches
[**switch_view**](SystemHardwareApi.md#switch_view) | **GET** /v1/system/hardware/switches/{switch_id} | Fetch switch


# **networking_switch_port_apply_settings**
> networking_switch_port_apply_settings(port, rack_id, switch_location, switch_port_apply_settings)

Apply switch port settings

### Example


```python
import oxide
from oxide.models.switch_port_apply_settings import SwitchPortApplySettings
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
    api_instance = oxide.SystemHardwareApi(api_client)
    port = 'port_example' # str | A name to use when selecting switch ports.
    rack_id = 'rack_id_example' # str | A rack id to use when selecting switch ports.
    switch_location = 'switch_location_example' # str | A switch location to use when selecting switch ports.
    switch_port_apply_settings = oxide.SwitchPortApplySettings() # SwitchPortApplySettings | 

    try:
        # Apply switch port settings
        api_instance.networking_switch_port_apply_settings(port, rack_id, switch_location, switch_port_apply_settings)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->networking_switch_port_apply_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**| A name to use when selecting switch ports. | 
 **rack_id** | **str**| A rack id to use when selecting switch ports. | 
 **switch_location** | **str**| A switch location to use when selecting switch ports. | 
 **switch_port_apply_settings** | [**SwitchPortApplySettings**](SwitchPortApplySettings.md)|  | 

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

# **networking_switch_port_clear_settings**
> networking_switch_port_clear_settings(port, rack_id, switch_location)

Clear switch port settings

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
    api_instance = oxide.SystemHardwareApi(api_client)
    port = 'port_example' # str | A name to use when selecting switch ports.
    rack_id = 'rack_id_example' # str | A rack id to use when selecting switch ports.
    switch_location = 'switch_location_example' # str | A switch location to use when selecting switch ports.

    try:
        # Clear switch port settings
        api_instance.networking_switch_port_clear_settings(port, rack_id, switch_location)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->networking_switch_port_clear_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**| A name to use when selecting switch ports. | 
 **rack_id** | **str**| A rack id to use when selecting switch ports. | 
 **switch_location** | **str**| A switch location to use when selecting switch ports. | 

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

# **networking_switch_port_list**
> SwitchPortResultsPage networking_switch_port_list(limit=limit, page_token=page_token, sort_by=sort_by, switch_port_id=switch_port_id)

List switch ports

### Example


```python
import oxide
from oxide.models.switch_port_results_page import SwitchPortResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)
    switch_port_id = 'switch_port_id_example' # str | An optional switch port id to use when listing switch ports. (optional)

    try:
        # List switch ports
        api_response = api_instance.networking_switch_port_list(limit=limit, page_token=page_token, sort_by=sort_by, switch_port_id=switch_port_id)
        print("The response of SystemHardwareApi->networking_switch_port_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->networking_switch_port_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 
 **switch_port_id** | **str**| An optional switch port id to use when listing switch ports. | [optional] 

### Return type

[**SwitchPortResultsPage**](SwitchPortResultsPage.md)

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

# **networking_switch_port_status**
> object networking_switch_port_status(port, rack_id, switch_location)

Get switch port status

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
    api_instance = oxide.SystemHardwareApi(api_client)
    port = 'port_example' # str | A name to use when selecting switch ports.
    rack_id = 'rack_id_example' # str | A rack id to use when selecting switch ports.
    switch_location = 'switch_location_example' # str | A switch location to use when selecting switch ports.

    try:
        # Get switch port status
        api_response = api_instance.networking_switch_port_status(port, rack_id, switch_location)
        print("The response of SystemHardwareApi->networking_switch_port_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->networking_switch_port_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**| A name to use when selecting switch ports. | 
 **rack_id** | **str**| A rack id to use when selecting switch ports. | 
 **switch_location** | **str**| A switch location to use when selecting switch ports. | 

### Return type

**object**

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

# **physical_disk_list**
> PhysicalDiskResultsPage physical_disk_list(limit=limit, page_token=page_token, sort_by=sort_by)

List physical disks

### Example


```python
import oxide
from oxide.models.physical_disk_results_page import PhysicalDiskResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List physical disks
        api_response = api_instance.physical_disk_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemHardwareApi->physical_disk_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->physical_disk_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**PhysicalDiskResultsPage**](PhysicalDiskResultsPage.md)

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

# **physical_disk_view**
> PhysicalDisk physical_disk_view(disk_id)

Get a physical disk

### Example


```python
import oxide
from oxide.models.physical_disk import PhysicalDisk
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
    api_instance = oxide.SystemHardwareApi(api_client)
    disk_id = 'disk_id_example' # str | ID of the physical disk

    try:
        # Get a physical disk
        api_response = api_instance.physical_disk_view(disk_id)
        print("The response of SystemHardwareApi->physical_disk_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->physical_disk_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_id** | **str**| ID of the physical disk | 

### Return type

[**PhysicalDisk**](PhysicalDisk.md)

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

# **rack_list**
> RackResultsPage rack_list(limit=limit, page_token=page_token, sort_by=sort_by)

List racks

### Example


```python
import oxide
from oxide.models.rack_results_page import RackResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List racks
        api_response = api_instance.rack_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemHardwareApi->rack_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->rack_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**RackResultsPage**](RackResultsPage.md)

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

# **rack_view**
> Rack rack_view(rack_id)

Fetch rack

### Example


```python
import oxide
from oxide.models.rack import Rack
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
    api_instance = oxide.SystemHardwareApi(api_client)
    rack_id = 'rack_id_example' # str | ID of the rack

    try:
        # Fetch rack
        api_response = api_instance.rack_view(rack_id)
        print("The response of SystemHardwareApi->rack_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->rack_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rack_id** | **str**| ID of the rack | 

### Return type

[**Rack**](Rack.md)

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

# **sled_add**
> SledId sled_add(uninitialized_sled_id)

Add sled to initialized rack

### Example


```python
import oxide
from oxide.models.sled_id import SledId
from oxide.models.uninitialized_sled_id import UninitializedSledId
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
    api_instance = oxide.SystemHardwareApi(api_client)
    uninitialized_sled_id = oxide.UninitializedSledId() # UninitializedSledId | 

    try:
        # Add sled to initialized rack
        api_response = api_instance.sled_add(uninitialized_sled_id)
        print("The response of SystemHardwareApi->sled_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->sled_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uninitialized_sled_id** | [**UninitializedSledId**](UninitializedSledId.md)|  | 

### Return type

[**SledId**](SledId.md)

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

# **sled_instance_list**
> SledInstanceResultsPage sled_instance_list(sled_id, limit=limit, page_token=page_token, sort_by=sort_by)

List instances running on given sled

### Example


```python
import oxide
from oxide.models.sled_instance_results_page import SledInstanceResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    sled_id = 'sled_id_example' # str | ID of the sled
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List instances running on given sled
        api_response = api_instance.sled_instance_list(sled_id, limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemHardwareApi->sled_instance_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->sled_instance_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sled_id** | **str**| ID of the sled | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**SledInstanceResultsPage**](SledInstanceResultsPage.md)

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

# **sled_list**
> SledResultsPage sled_list(limit=limit, page_token=page_token, sort_by=sort_by)

List sleds

### Example


```python
import oxide
from oxide.models.sled_results_page import SledResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List sleds
        api_response = api_instance.sled_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemHardwareApi->sled_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->sled_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**SledResultsPage**](SledResultsPage.md)

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

# **sled_list_uninitialized**
> UninitializedSledResultsPage sled_list_uninitialized(limit=limit, page_token=page_token)

List uninitialized sleds

### Example


```python
import oxide
from oxide.models.uninitialized_sled_results_page import UninitializedSledResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)

    try:
        # List uninitialized sleds
        api_response = api_instance.sled_list_uninitialized(limit=limit, page_token=page_token)
        print("The response of SystemHardwareApi->sled_list_uninitialized:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->sled_list_uninitialized: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 

### Return type

[**UninitializedSledResultsPage**](UninitializedSledResultsPage.md)

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

# **sled_physical_disk_list**
> PhysicalDiskResultsPage sled_physical_disk_list(sled_id, limit=limit, page_token=page_token, sort_by=sort_by)

List physical disks attached to sleds

### Example


```python
import oxide
from oxide.models.physical_disk_results_page import PhysicalDiskResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    sled_id = 'sled_id_example' # str | ID of the sled
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List physical disks attached to sleds
        api_response = api_instance.sled_physical_disk_list(sled_id, limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemHardwareApi->sled_physical_disk_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->sled_physical_disk_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sled_id** | **str**| ID of the sled | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**PhysicalDiskResultsPage**](PhysicalDiskResultsPage.md)

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

# **sled_set_provision_policy**
> SledProvisionPolicyResponse sled_set_provision_policy(sled_id, sled_provision_policy_params)

Set sled provision policy

### Example


```python
import oxide
from oxide.models.sled_provision_policy_params import SledProvisionPolicyParams
from oxide.models.sled_provision_policy_response import SledProvisionPolicyResponse
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
    api_instance = oxide.SystemHardwareApi(api_client)
    sled_id = 'sled_id_example' # str | ID of the sled
    sled_provision_policy_params = oxide.SledProvisionPolicyParams() # SledProvisionPolicyParams | 

    try:
        # Set sled provision policy
        api_response = api_instance.sled_set_provision_policy(sled_id, sled_provision_policy_params)
        print("The response of SystemHardwareApi->sled_set_provision_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->sled_set_provision_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sled_id** | **str**| ID of the sled | 
 **sled_provision_policy_params** | [**SledProvisionPolicyParams**](SledProvisionPolicyParams.md)|  | 

### Return type

[**SledProvisionPolicyResponse**](SledProvisionPolicyResponse.md)

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

# **sled_view**
> Sled sled_view(sled_id)

Fetch sled

### Example


```python
import oxide
from oxide.models.sled import Sled
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
    api_instance = oxide.SystemHardwareApi(api_client)
    sled_id = 'sled_id_example' # str | ID of the sled

    try:
        # Fetch sled
        api_response = api_instance.sled_view(sled_id)
        print("The response of SystemHardwareApi->sled_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->sled_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sled_id** | **str**| ID of the sled | 

### Return type

[**Sled**](Sled.md)

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

# **switch_list**
> SwitchResultsPage switch_list(limit=limit, page_token=page_token, sort_by=sort_by)

List switches

### Example


```python
import oxide
from oxide.models.switch_results_page import SwitchResultsPage
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
    api_instance = oxide.SystemHardwareApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    sort_by = oxide.IdSortMode() # IdSortMode |  (optional)

    try:
        # List switches
        api_response = api_instance.switch_list(limit=limit, page_token=page_token, sort_by=sort_by)
        print("The response of SystemHardwareApi->switch_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->switch_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **sort_by** | [**IdSortMode**](.md)|  | [optional] 

### Return type

[**SwitchResultsPage**](SwitchResultsPage.md)

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

# **switch_view**
> Switch switch_view(switch_id)

Fetch switch

### Example


```python
import oxide
from oxide.models.switch import Switch
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
    api_instance = oxide.SystemHardwareApi(api_client)
    switch_id = 'switch_id_example' # str | ID of the switch

    try:
        # Fetch switch
        api_response = api_instance.switch_view(switch_id)
        print("The response of SystemHardwareApi->switch_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemHardwareApi->switch_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_id** | **str**| ID of the switch | 

### Return type

[**Switch**](Switch.md)

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

