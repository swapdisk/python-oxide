# PhysicalDiskPolicy

The operator-defined policy of a physical disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 

## Example

```python
from oxide.models.physical_disk_policy import PhysicalDiskPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalDiskPolicy from a JSON string
physical_disk_policy_instance = PhysicalDiskPolicy.from_json(json)
# print the JSON string representation of the object
print(PhysicalDiskPolicy.to_json())

# convert the object into a dict
physical_disk_policy_dict = physical_disk_policy_instance.to_dict()
# create an instance of PhysicalDiskPolicy from a dict
physical_disk_policy_from_dict = PhysicalDiskPolicy.from_dict(physical_disk_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


