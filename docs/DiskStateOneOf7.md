# DiskStateOneOf7

Disk is being attached to the given Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from oxide.models.disk_state_one_of7 import DiskStateOneOf7

# TODO update the JSON string below
json = "{}"
# create an instance of DiskStateOneOf7 from a JSON string
disk_state_one_of7_instance = DiskStateOneOf7.from_json(json)
# print the JSON string representation of the object
print(DiskStateOneOf7.to_json())

# convert the object into a dict
disk_state_one_of7_dict = disk_state_one_of7_instance.to_dict()
# create an instance of DiskStateOneOf7 from a dict
disk_state_one_of7_from_dict = DiskStateOneOf7.from_dict(disk_state_one_of7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


