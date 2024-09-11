# ImageSource

The source of the underlying image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.image_source import ImageSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSource from a JSON string
image_source_instance = ImageSource.from_json(json)
# print the JSON string representation of the object
print(ImageSource.to_json())

# convert the object into a dict
image_source_dict = image_source_instance.to_dict()
# create an instance of ImageSource from a dict
image_source_from_dict = ImageSource.from_dict(image_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


