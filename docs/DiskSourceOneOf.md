# DiskSourceOneOf

Create a blank disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | [**BlockSize**](BlockSize.md) | size of blocks for this Disk. valid values are: 512, 2048, or 4096 | 
**type** | **str** |  | 

## Example

```python
from oxide.models.disk_source_one_of import DiskSourceOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSourceOneOf from a JSON string
disk_source_one_of_instance = DiskSourceOneOf.from_json(json)
# print the JSON string representation of the object
print(DiskSourceOneOf.to_json())

# convert the object into a dict
disk_source_one_of_dict = disk_source_one_of_instance.to_dict()
# create an instance of DiskSourceOneOf from a dict
disk_source_one_of_from_dict = DiskSourceOneOf.from_dict(disk_source_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


