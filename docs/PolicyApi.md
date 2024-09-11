# oxide.PolicyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_policy_update**](PolicyApi.md#system_policy_update) | **PUT** /v1/system/policy | Update top-level IAM policy
[**system_policy_view**](PolicyApi.md#system_policy_view) | **GET** /v1/system/policy | Fetch top-level IAM policy


# **system_policy_update**
> FleetRolePolicy system_policy_update(fleet_role_policy)

Update top-level IAM policy

### Example


```python
import oxide
from oxide.models.fleet_role_policy import FleetRolePolicy
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
    api_instance = oxide.PolicyApi(api_client)
    fleet_role_policy = oxide.FleetRolePolicy() # FleetRolePolicy | 

    try:
        # Update top-level IAM policy
        api_response = api_instance.system_policy_update(fleet_role_policy)
        print("The response of PolicyApi->system_policy_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->system_policy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_role_policy** | [**FleetRolePolicy**](FleetRolePolicy.md)|  | 

### Return type

[**FleetRolePolicy**](FleetRolePolicy.md)

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

# **system_policy_view**
> FleetRolePolicy system_policy_view()

Fetch top-level IAM policy

### Example


```python
import oxide
from oxide.models.fleet_role_policy import FleetRolePolicy
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
    api_instance = oxide.PolicyApi(api_client)

    try:
        # Fetch top-level IAM policy
        api_response = api_instance.system_policy_view()
        print("The response of PolicyApi->system_policy_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->system_policy_view: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FleetRolePolicy**](FleetRolePolicy.md)

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

