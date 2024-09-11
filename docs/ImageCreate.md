# ImageCreate

Create-time parameters for an `Image`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**os** | **str** | The family of the operating system (e.g. Debian, Ubuntu, etc.) | 
**source** | [**ImageSource**](ImageSource.md) | The source of the image&#39;s contents. | 
**version** | **str** | The version of the operating system (e.g. 18.04, 20.04, etc.) | 

## Example

```python
from oxide.models.image_create import ImageCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCreate from a JSON string
image_create_instance = ImageCreate.from_json(json)
# print the JSON string representation of the object
print(ImageCreate.to_json())

# convert the object into a dict
image_create_dict = image_create_instance.to_dict()
# create an instance of ImageCreate from a dict
image_create_from_dict = ImageCreate.from_dict(image_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


