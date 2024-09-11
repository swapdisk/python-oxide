# DiskSourceOneOf1

Create a disk from a disk snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.disk_source_one_of1 import DiskSourceOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSourceOneOf1 from a JSON string
disk_source_one_of1_instance = DiskSourceOneOf1.from_json(json)
# print the JSON string representation of the object
print(DiskSourceOneOf1.to_json())

# convert the object into a dict
disk_source_one_of1_dict = disk_source_one_of1_instance.to_dict()
# create an instance of DiskSourceOneOf1 from a dict
disk_source_one_of1_from_dict = DiskSourceOneOf1.from_dict(disk_source_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


