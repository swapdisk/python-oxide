# PhysicalDiskState

The current state of the disk, as determined by Nexus.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.physical_disk_state import PhysicalDiskState

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalDiskState from a JSON string
physical_disk_state_instance = PhysicalDiskState.from_json(json)
# print the JSON string representation of the object
print(PhysicalDiskState.to_json())

# convert the object into a dict
physical_disk_state_dict = physical_disk_state_instance.to_dict()
# create an instance of PhysicalDiskState from a dict
physical_disk_state_from_dict = PhysicalDiskState.from_dict(physical_disk_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


