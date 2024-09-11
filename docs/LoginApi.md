# oxide.LoginApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_local**](LoginApi.md#login_local) | **POST** /v1/login/{silo_name}/local | Authenticate a user via username and password
[**login_saml**](LoginApi.md#login_saml) | **POST** /login/{silo_name}/saml/{provider_name} | Authenticate a user via SAML


# **login_local**
> login_local(silo_name, username_password_credentials)

Authenticate a user via username and password

### Example


```python
import oxide
from oxide.models.username_password_credentials import UsernamePasswordCredentials
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
    api_instance = oxide.LoginApi(api_client)
    silo_name = 'silo_name_example' # str | 
    username_password_credentials = oxide.UsernamePasswordCredentials() # UsernamePasswordCredentials | 

    try:
        # Authenticate a user via username and password
        api_instance.login_local(silo_name, username_password_credentials)
    except Exception as e:
        print("Exception when calling LoginApi->login_local: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silo_name** | **str**|  | 
 **username_password_credentials** | [**UsernamePasswordCredentials**](UsernamePasswordCredentials.md)|  | 

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

# **login_saml**
> login_saml(provider_name, silo_name, body)

Authenticate a user via SAML

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
    api_instance = oxide.LoginApi(api_client)
    provider_name = 'provider_name_example' # str | 
    silo_name = 'silo_name_example' # str | 
    body = None # bytearray | 

    try:
        # Authenticate a user via SAML
        api_instance.login_saml(provider_name, silo_name, body)
    except Exception as e:
        print("Exception when calling LoginApi->login_saml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **silo_name** | **str**|  | 
 **body** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | redirect (see other) |  * location - HTTP \&quot;Location\&quot; header <br>  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

