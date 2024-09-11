# oxide.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_create**](ImagesApi.md#image_create) | **POST** /v1/images | Create image
[**image_delete**](ImagesApi.md#image_delete) | **DELETE** /v1/images/{image} | Delete image
[**image_demote**](ImagesApi.md#image_demote) | **POST** /v1/images/{image}/demote | Demote silo image
[**image_list**](ImagesApi.md#image_list) | **GET** /v1/images | List images
[**image_promote**](ImagesApi.md#image_promote) | **POST** /v1/images/{image}/promote | Promote project image
[**image_view**](ImagesApi.md#image_view) | **GET** /v1/images/{image} | Fetch image


# **image_create**
> Image image_create(image_create, project=project)

Create image

Create a new image in a project.

### Example


```python
import oxide
from oxide.models.image import Image
from oxide.models.image_create import ImageCreate
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
    api_instance = oxide.ImagesApi(api_client)
    image_create = oxide.ImageCreate() # ImageCreate | 
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Create image
        api_response = api_instance.image_create(image_create, project=project)
        print("The response of ImagesApi->image_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_create** | [**ImageCreate**](ImageCreate.md)|  | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Image**](Image.md)

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

# **image_delete**
> image_delete(image, project=project)

Delete image

Permanently delete an image from a project. This operation cannot be undone. Any instances in the project using the image will continue to run, however new instances can not be created with this image.

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
    api_instance = oxide.ImagesApi(api_client)
    image = oxide.NameOrId() # NameOrId | Name or ID of the image
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Delete image
        api_instance.image_delete(image, project=project)
    except Exception as e:
        print("Exception when calling ImagesApi->image_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**NameOrId**](.md)| Name or ID of the image | 
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

# **image_demote**
> Image image_demote(image, project)

Demote silo image

Demote silo image to be visible only to a specified project

### Example


```python
import oxide
from oxide.models.image import Image
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
    api_instance = oxide.ImagesApi(api_client)
    image = oxide.NameOrId() # NameOrId | Name or ID of the image
    project = oxide.NameOrId() # NameOrId | Name or ID of the project

    try:
        # Demote silo image
        api_response = api_instance.image_demote(image, project)
        print("The response of ImagesApi->image_demote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_demote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**NameOrId**](.md)| Name or ID of the image | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | 

### Return type

[**Image**](Image.md)

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

# **image_list**
> ImageResultsPage image_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)

List images

List images which are global or scoped to the specified project. The images are returned sorted by creation date, with the most recent images appearing first.

### Example


```python
import oxide
from oxide.models.image_results_page import ImageResultsPage
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
    api_instance = oxide.ImagesApi(api_client)
    limit = 56 # int | Maximum number of items returned by a single call (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page (optional)
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)
    sort_by = oxide.NameOrIdSortMode() # NameOrIdSortMode |  (optional)

    try:
        # List images
        api_response = api_instance.image_list(limit=limit, page_token=page_token, project=project, sort_by=sort_by)
        print("The response of ImagesApi->image_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items returned by a single call | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page | [optional] 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 
 **sort_by** | [**NameOrIdSortMode**](.md)|  | [optional] 

### Return type

[**ImageResultsPage**](ImageResultsPage.md)

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

# **image_promote**
> Image image_promote(image, project=project)

Promote project image

Promote project image to be visible to all projects in the silo

### Example


```python
import oxide
from oxide.models.image import Image
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
    api_instance = oxide.ImagesApi(api_client)
    image = oxide.NameOrId() # NameOrId | Name or ID of the image
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Promote project image
        api_response = api_instance.image_promote(image, project=project)
        print("The response of ImagesApi->image_promote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_promote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**NameOrId**](.md)| Name or ID of the image | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Image**](Image.md)

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

# **image_view**
> Image image_view(image, project=project)

Fetch image

Fetch the details for a specific image in a project.

### Example


```python
import oxide
from oxide.models.image import Image
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
    api_instance = oxide.ImagesApi(api_client)
    image = oxide.NameOrId() # NameOrId | Name or ID of the image
    project = oxide.NameOrId() # NameOrId | Name or ID of the project (optional)

    try:
        # Fetch image
        api_response = api_instance.image_view(image, project=project)
        print("The response of ImagesApi->image_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**NameOrId**](.md)| Name or ID of the image | 
 **project** | [**NameOrId**](.md)| Name or ID of the project | [optional] 

### Return type

[**Image**](Image.md)

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

