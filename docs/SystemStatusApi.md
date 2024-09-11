# oxide.SystemStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](SystemStatusApi.md#ping) | **GET** /v1/ping | Ping API


# **ping**
> Ping ping()

Ping API

Always responds with Ok if it responds at all.

### Example


```python
import oxide
from oxide.models.ping import Ping
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
    api_instance = oxide.SystemStatusApi(api_client)

    try:
        # Ping API
        api_response = api_instance.ping()
        print("The response of SystemStatusApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Ping**](Ping.md)

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

