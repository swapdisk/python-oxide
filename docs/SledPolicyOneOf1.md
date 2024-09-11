# SledPolicyOneOf1

The operator has indicated that the sled has been permanently removed from service.  This is a terminal state: once a particular sled ID is expunged, it will never return to service. (The actual hardware may be reused, but it will be treated as a brand-new sled.)  An expunged sled is always non-provisionable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 

## Example

```python
from oxide.models.sled_policy_one_of1 import SledPolicyOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of SledPolicyOneOf1 from a JSON string
sled_policy_one_of1_instance = SledPolicyOneOf1.from_json(json)
# print the JSON string representation of the object
print(SledPolicyOneOf1.to_json())

# convert the object into a dict
sled_policy_one_of1_dict = sled_policy_one_of1_instance.to_dict()
# create an instance of SledPolicyOneOf1 from a dict
sled_policy_one_of1_from_dict = SledPolicyOneOf1.from_dict(sled_policy_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


