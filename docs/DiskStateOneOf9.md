# DiskStateOneOf9

Disk is being detached from the given Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from oxide.models.disk_state_one_of9 import DiskStateOneOf9

# TODO update the JSON string below
json = "{}"
# create an instance of DiskStateOneOf9 from a JSON string
disk_state_one_of9_instance = DiskStateOneOf9.from_json(json)
# print the JSON string representation of the object
print(DiskStateOneOf9.to_json())

# convert the object into a dict
disk_state_one_of9_dict = disk_state_one_of9_instance.to_dict()
# create an instance of DiskStateOneOf9 from a dict
disk_state_one_of9_from_dict = DiskStateOneOf9.from_dict(disk_state_one_of9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


