# PhysicalDiskPolicyOneOf1

The operator has indicated that the disk has been permanently removed from service.  This is a terminal state: once a particular disk ID is expunged, it will never return to service. (The actual hardware may be reused, but it will be treated as a brand-new disk.)  An expunged disk is always non-provisionable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 

## Example

```python
from oxide.models.physical_disk_policy_one_of1 import PhysicalDiskPolicyOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalDiskPolicyOneOf1 from a JSON string
physical_disk_policy_one_of1_instance = PhysicalDiskPolicyOneOf1.from_json(json)
# print the JSON string representation of the object
print(PhysicalDiskPolicyOneOf1.to_json())

# convert the object into a dict
physical_disk_policy_one_of1_dict = physical_disk_policy_one_of1_instance.to_dict()
# create an instance of PhysicalDiskPolicyOneOf1 from a dict
physical_disk_policy_one_of1_from_dict = PhysicalDiskPolicyOneOf1.from_dict(physical_disk_policy_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


