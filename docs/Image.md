# Image

View of an image  If `project_id` is present then the image is only visible inside that project. If it's not present then the image is visible to all projects in the silo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **int** | size of blocks in bytes | 
**description** | **str** | human-readable free-form text about a resource | 
**digest** | [**Digest**](Digest.md) | Hash of the image contents, if applicable | [optional] 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**os** | **str** | The family of the operating system like Debian, Ubuntu, etc. | 
**project_id** | **str** | ID of the parent project if the image is a project image | [optional] 
**size** | **int** | total size in bytes | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**version** | **str** | Version of the operating system | 

## Example

```python
from oxide.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print(Image.to_json())

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_from_dict = Image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


