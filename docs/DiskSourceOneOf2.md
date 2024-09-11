# DiskSourceOneOf2

Create a disk from an image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.disk_source_one_of2 import DiskSourceOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSourceOneOf2 from a JSON string
disk_source_one_of2_instance = DiskSourceOneOf2.from_json(json)
# print the JSON string representation of the object
print(DiskSourceOneOf2.to_json())

# convert the object into a dict
disk_source_one_of2_dict = disk_source_one_of2_instance.to_dict()
# create an instance of DiskSourceOneOf2 from a dict
disk_source_one_of2_from_dict = DiskSourceOneOf2.from_dict(disk_source_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


