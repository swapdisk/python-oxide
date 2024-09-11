# oxide.InstancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_create**](InstancesApi.md#instance_create) | **POST** /v1/instances | Create instance
[**instance_delete**](InstancesApi.md#instance_delete) | **DELETE** /v1/instances/{instance} | Delete instance
[**instance_disk_attach**](InstancesApi.md#instance_disk_attach) | **POST** /v1/instances/{instance}/disks/attach | Attach disk to instance
[**instance_disk_detach**](InstancesApi.md#instance_disk_detach) | **POST** /v1/instances/{instance}/disks/detach | Detach disk from instance
[**instance_disk_list**](InstancesApi.md#instance_disk_list) | **GET** /v1/instances/{instance}/disks | List disks for instance
[**instance_ephemeral_ip_attach**](InstancesApi.md#instance_ephemeral_ip_attach) | **POST** /v1/instances/{instance}/external-ips/ephemeral | Allocate and attach ephemeral IP to instance
[**instance_ephemeral_ip_detach**](InstancesApi.md#instance_ephemeral_ip_detach) | **DELETE** /v1/instances/{instance}/external-ips/ephemeral | Detach and deallocate ephemeral IP from instance
[**instance_external_ip_list**](InstancesApi.md#instance_external_ip_list) | **GET** /v1/instances/{instance}/external-ips | List external IP addresses
[**instance_list**](InstancesApi.md#instance_list) | **GET** /v1/instances | List instances
[**instance_network_interface_create**](InstancesApi.md#instance_network_interface_create) | **POST** /v1/network-interfaces | Create network interface
[**instance_network_interface_delete**](InstancesApi.md#instance_network_interface_delete) | **DELETE** /v1/network-interfaces/{interface} | Delete network interface
[**instance_network_interface_list**](InstancesApi.md#instance_network_interface_list) | **GET** /v1/network-interfaces | List network interfaces
[**instance_network_interface_update**](InstancesApi.md#instance_network_interface_update) | **PUT** /v1/network-interfaces/{interface} | Update network interface
[**instance_network_interface_view**](InstancesApi.md#instance_network_interface_view) | **GET** /v1/network-interfaces/{interface} | Fetch network interface
[**instance_reboot**](InstancesApi.md#instance_reboot) | **POST** /v1/instances/{instance}/reboot | Reboot an instance
[**instance_serial_console**](InstancesApi.md#instance_serial_console) | **GET** /v1/instances/{instance}/serial-console | Fetch instance serial console
[**instance_serial_console_stream**](InstancesApi.md#instance_serial_console_stream) | **GET** /v1/instances/{instance}/serial-console/stream | Stream instance serial console
[**instance_ssh_public_key_list**](InstancesApi.md#instance_ssh_public_key_list) | **GET** /v1/instances/{instance}/ssh-public-keys | List SSH public keys for instance
[**instance_start**](InstancesApi.md#instance_start) | **POST** /v1/instances/{instance}/start | Boot instance
[**instance_stop**](InstancesApi.md#instance_stop) | **POST** /v1/instances/{instance}/stop | Stop instance
[**instance_view**](InstancesApi.md#instance_view) | **GET** /v1/instances/{instance} | Fetch instance


# **instance_create**
> Instance instance_create(project, instance_create)

Create instance

### Example


```python
import oxide
from oxide.models.instance import Instance
from oxide.models.instance_create import InstanceCreate
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
    api_instance = oxide.InstancesApi(api_client)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project
    instance_create = oxide.InstanceCreate() # InstanceCreate | 

    try:
        # Create instance
        api_response = api_instance.instance_create(project, instance_create)
        print("The response of InstancesApi->instance_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NameOrId**](.md)| Name or ID of the project | 
 **instance_create** | [**InstanceCreate**](InstanceCreate.md)|  | 

### Return type

[**Instance**](Instance.md)

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

# **instance_delete**
> instance_delete(instance, project=project)

Delete instance

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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Delete instance
        api_instance.instance_delete(instance, project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
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

# **instance_disk_attach**
> Disk instance_disk_attach(instance, disk_path, project=project)

Attach disk to instance

### Example


```python
import oxide
from oxide.models.disk import Disk
from oxide.models.disk_path import DiskPath
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    disk_path = oxide.DiskPath() # DiskPath | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Attach disk to instance
        api_response = api_instance.instance_disk_attach(instance, disk_path, project=project)
        print("The response of InstancesApi->instance_disk_attach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_disk_attach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **disk_path** | [**DiskPath**](DiskPath.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Disk**](Disk.md)

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

# **instance_disk_detach**
> Disk instance_disk_detach(instance, disk_path, project=project)

Detach disk from instance

### Example


```python
import oxide
from oxide.models.disk import Disk
from oxide.models.disk_path import DiskPath
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    disk_path = oxide.DiskPath() # DiskPath | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Detach disk from instance
        api_response = api_instance.instance_disk_detach(instance, disk_path, project=project)
        print("The response of InstancesApi->instance_disk_detach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_disk_detach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **disk_path** | [**DiskPath**](DiskPath.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Disk**](Disk.md)

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

# **instance_disk_list**
> DiskResultsPage instance_disk_list(instance, limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List disks for instance

### Example


```python
import oxide
from oxide.models.disk_results_page import DiskResultsPage
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List disks for instance
        api_response = api_instance.instance_disk_list(instance, limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of InstancesApi->instance_disk_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_disk_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**DiskResultsPage**](DiskResultsPage.md)

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

# **instance_ephemeral_ip_attach**
> ExternalIp instance_ephemeral_ip_attach(instance, ephemeral_ip_create, project=project)

Allocate and attach ephemeral IP to instance

### Example


```python
import oxide
from oxide.models.ephemeral_ip_create import EphemeralIpCreate
from oxide.models.external_ip import ExternalIp
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    ephemeral_ip_create = oxide.EphemeralIpCreate() # EphemeralIpCreate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Allocate and attach ephemeral IP to instance
        api_response = api_instance.instance_ephemeral_ip_attach(instance, ephemeral_ip_create, project=project)
        print("The response of InstancesApi->instance_ephemeral_ip_attach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_ephemeral_ip_attach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **ephemeral_ip_create** | [**EphemeralIpCreate**](EphemeralIpCreate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**ExternalIp**](ExternalIp.md)

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

# **instance_ephemeral_ip_detach**
> instance_ephemeral_ip_detach(instance, project=project)

Detach and deallocate ephemeral IP from instance

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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Detach and deallocate ephemeral IP from instance
        api_instance.instance_ephemeral_ip_detach(instance, project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_ephemeral_ip_detach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
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

# **instance_external_ip_list**
> ExternalIpResultsPage instance_external_ip_list(instance, project=project)

List external IP addresses

### Example


```python
import oxide
from oxide.models.external_ip_results_page import ExternalIpResultsPage
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # List external IP addresses
        api_response = api_instance.instance_external_ip_list(instance, project=project)
        print("The response of InstancesApi->instance_external_ip_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_external_ip_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**ExternalIpResultsPage**](ExternalIpResultsPage.md)

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

# **instance_list**
> InstanceResultsPage instance_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List instances

### Example


```python
import oxide
from oxide.models.instance_results_page import InstanceResultsPage
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
    api_instance = oxide.InstancesApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List instances
        api_response = api_instance.instance_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of InstancesApi->instance_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**InstanceResultsPage**](InstanceResultsPage.md)

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

# **instance_network_interface_create**
> InstanceNetworkInterface instance_network_interface_create(instance, instance_network_interface_create, project=project)

Create network interface

### Example


```python
import oxide
from oxide.models.instance_network_interface import InstanceNetworkInterface
from oxide.models.instance_network_interface_create import InstanceNetworkInterfaceCreate
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    instance_network_interface_create = oxide.InstanceNetworkInterfaceCreate() # InstanceNetworkInterfaceCreate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `instance` is provided as a `Name` (optional)

    try:
        # Create network interface
        api_response = api_instance.instance_network_interface_create(instance, instance_network_interface_create, project=project)
        print("The response of InstancesApi->instance_network_interface_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_network_interface_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **instance_network_interface_create** | [**InstanceNetworkInterfaceCreate**](InstanceNetworkInterfaceCreate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;instance&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**InstanceNetworkInterface**](InstanceNetworkInterface.md)

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

# **instance_network_interface_delete**
> instance_network_interface_delete(interface, instance=instance, project=project)

Delete network interface

Note that the primary interface for an instance cannot be deleted if there are any secondary interfaces. A new primary interface must be designated first. The primary interface can be deleted if there are no secondary interfaces.

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
    api_instance = oxide.InstancesApi(api_client)
    interface = oxide.NameOrId() # NameOrId | Name or ID of the network interface
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `instance` is provided as a `Name` (optional)

    try:
        # Delete network interface
        api_instance.instance_network_interface_delete(interface, instance=instance, project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_network_interface_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | [**NameOrId**](.md)| Name or ID of the network interface | 
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;instance&#x60; is provided as a &#x60;Name&#x60; | [optional] 

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

# **instance_network_interface_list**
> InstanceNetworkInterfaceResultsPage instance_network_interface_list(instance=instance, limit=limit, page_token=page_token, project=project, sort_by=sort_by)

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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance (optional)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `instance` is provided as a `Name` (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List network interfaces
        api_response = api_instance.instance_network_interface_list(instance=instance, limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of InstancesApi->instance_network_interface_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_network_interface_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | [optional] 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;instance&#x60; is provided as a &#x60;Name&#x60; | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

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

# **instance_network_interface_update**
> InstanceNetworkInterface instance_network_interface_update(interface, instance_network_interface_update, instance=instance, project=project)

Update network interface

### Example


```python
import oxide
from oxide.models.instance_network_interface import InstanceNetworkInterface
from oxide.models.instance_network_interface_update import InstanceNetworkInterfaceUpdate
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
    api_instance = oxide.InstancesApi(api_client)
    interface = oxide.NameOrId() # NameOrId | Name or ID of the network interface
    instance_network_interface_update = oxide.InstanceNetworkInterfaceUpdate() # InstanceNetworkInterfaceUpdate | 
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `instance` is provided as a `Name` (optional)

    try:
        # Update network interface
        api_response = api_instance.instance_network_interface_update(interface, instance_network_interface_update, instance=instance, project=project)
        print("The response of InstancesApi->instance_network_interface_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_network_interface_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | [**NameOrId**](.md)| Name or ID of the network interface | 
 **instance_network_interface_update** | [**InstanceNetworkInterfaceUpdate**](InstanceNetworkInterfaceUpdate.md)|  | 
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;instance&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**InstanceNetworkInterface**](InstanceNetworkInterface.md)

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

# **instance_network_interface_view**
> InstanceNetworkInterface instance_network_interface_view(interface, instance=instance, project=project)

Fetch network interface

### Example


```python
import oxide
from oxide.models.instance_network_interface import InstanceNetworkInterface
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
    api_instance = oxide.InstancesApi(api_client)
    interface = oxide.NameOrId() # NameOrId | Name or ID of the network interface
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `instance` is provided as a `Name` (optional)

    try:
        # Fetch network interface
        api_response = api_instance.instance_network_interface_view(interface, instance=instance, project=project)
        print("The response of InstancesApi->instance_network_interface_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_network_interface_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | [**NameOrId**](.md)| Name or ID of the network interface | 
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;instance&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**InstanceNetworkInterface**](InstanceNetworkInterface.md)

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

# **instance_reboot**
> Instance instance_reboot(instance, project=project)

Reboot an instance

### Example


```python
import oxide
from oxide.models.instance import Instance
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Reboot an instance
        api_response = api_instance.instance_reboot(instance, project=project)
        print("The response of InstancesApi->instance_reboot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_reboot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Instance**](Instance.md)

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

# **instance_serial_console**
> InstanceSerialConsoleData instance_serial_console(instance, from_start=from_start, max_bytes=max_bytes, most_recent=most_recent, project=project)

Fetch instance serial console

### Example


```python
import oxide
from oxide.models.instance_serial_console_data import InstanceSerialConsoleData
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    from_start = 56 # int | Character index in the serial buffer from which to read, counting the bytes output since instance start. If this is not provided, `most_recent` must be provided, and if this *is* provided, `most_recent` must *not* be provided. (optional)
    max_bytes = 56 # int | Maximum number of bytes of buffered serial console contents to return. If the requested range runs to the end of the available buffer, the data returned will be shorter than `max_bytes`. (optional)
    most_recent = 56 # int | Character index in the serial buffer from which to read, counting *backward* from the most recently buffered data retrieved from the instance. (See note on `from_start` about mutual exclusivity) (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `instance` is provided as a `Name` (optional)

    try:
        # Fetch instance serial console
        api_response = api_instance.instance_serial_console(instance, from_start=from_start, max_bytes=max_bytes, most_recent=most_recent, project=project)
        print("The response of InstancesApi->instance_serial_console:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_serial_console: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **from_start** | **int**| Character index in the serial buffer from which to read, counting the bytes output since instance start. If this is not provided, &#x60;most_recent&#x60; must be provided, and if this *is* provided, &#x60;most_recent&#x60; must *not* be provided. | [optional] 
 **max_bytes** | **int**| Maximum number of bytes of buffered serial console contents to return. If the requested range runs to the end of the available buffer, the data returned will be shorter than &#x60;max_bytes&#x60;. | [optional] 
 **most_recent** | **int**| Character index in the serial buffer from which to read, counting *backward* from the most recently buffered data retrieved from the instance. (See note on &#x60;from_start&#x60; about mutual exclusivity) | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;instance&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

[**InstanceSerialConsoleData**](InstanceSerialConsoleData.md)

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

# **instance_serial_console_stream**
> object instance_serial_console_stream(instance, most_recent=most_recent, project=project)

Stream instance serial console

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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    most_recent = 56 # int | Character index in the serial buffer from which to read, counting *backward* from the most recently buffered data retrieved from the instance. (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project, only required if `instance` is provided as a `Name` (optional)

    try:
        # Stream instance serial console
        api_response = api_instance.instance_serial_console_stream(instance, most_recent=most_recent, project=project)
        print("The response of InstancesApi->instance_serial_console_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_serial_console_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **most_recent** | **int**| Character index in the serial buffer from which to read, counting *backward* from the most recently buffered data retrieved from the instance. | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project, only required if &#x60;instance&#x60; is provided as a &#x60;Name&#x60; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_ssh_public_key_list**
> SshKeyResultsPage instance_ssh_public_key_list(instance, limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List SSH public keys for instance

List SSH public keys injected via cloud-init during instance creation. Note that this list is a snapshot in time and will not reflect updates made after the instance is created.

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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List SSH public keys for instance
        api_response = api_instance.instance_ssh_public_key_list(instance, limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of InstancesApi->instance_ssh_public_key_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_ssh_public_key_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
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

# **instance_start**
> Instance instance_start(instance, project=project)

Boot instance

### Example


```python
import oxide
from oxide.models.instance import Instance
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Boot instance
        api_response = api_instance.instance_start(instance, project=project)
        print("The response of InstancesApi->instance_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Instance**](Instance.md)

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

# **instance_stop**
> Instance instance_stop(instance, project=project)

Stop instance

### Example


```python
import oxide
from oxide.models.instance import Instance
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Stop instance
        api_response = api_instance.instance_stop(instance, project=project)
        print("The response of InstancesApi->instance_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Instance**](Instance.md)

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

# **instance_view**
> Instance instance_view(instance, project=project)

Fetch instance

### Example


```python
import oxide
from oxide.models.instance import Instance
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
    api_instance = oxide.InstancesApi(api_client)
    instance = oxide.NameOrId() # NameOrId | Name or ID of the instance
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Fetch instance
        api_response = api_instance.instance_view(instance, project=project)
        print("The response of InstancesApi->instance_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**NameOrId**](.md)| Name or ID of the instance | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Instance**](Instance.md)

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

