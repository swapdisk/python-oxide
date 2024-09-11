# DiskState

State of a Disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**instance** | **str** |  | 

## Example

```python
from oxide.models.disk_state import DiskState

# TODO update the JSON string below
json = "{}"
# create an instance of DiskState from a JSON string
disk_state_instance = DiskState.from_json(json)
# print the JSON string representation of the object
print(DiskState.to_json())

# convert the object into a dict
disk_state_dict = disk_state_instance.to_dict()
# create an instance of DiskState from a dict
disk_state_from_dict = DiskState.from_dict(disk_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


