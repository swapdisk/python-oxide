# DiskSourceOneOf3

Create a blank disk that will accept bulk writes or pull blocks from an external source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | [**BlockSize**](BlockSize.md) |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.disk_source_one_of3 import DiskSourceOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSourceOneOf3 from a JSON string
disk_source_one_of3_instance = DiskSourceOneOf3.from_json(json)
# print the JSON string representation of the object
print(DiskSourceOneOf3.to_json())

# convert the object into a dict
disk_source_one_of3_dict = disk_source_one_of3_instance.to_dict()
# create an instance of DiskSourceOneOf3 from a dict
disk_source_one_of3_from_dict = DiskSourceOneOf3.from_dict(disk_source_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


