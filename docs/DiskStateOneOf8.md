# DiskStateOneOf8

Disk is attached to the given Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from oxide.models.disk_state_one_of8 import DiskStateOneOf8

# TODO update the JSON string below
json = "{}"
# create an instance of DiskStateOneOf8 from a JSON string
disk_state_one_of8_instance = DiskStateOneOf8.from_json(json)
# print the JSON string representation of the object
print(DiskStateOneOf8.to_json())

# convert the object into a dict
disk_state_one_of8_dict = disk_state_one_of8_instance.to_dict()
# create an instance of DiskStateOneOf8 from a dict
disk_state_one_of8_from_dict = DiskStateOneOf8.from_dict(disk_state_one_of8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


