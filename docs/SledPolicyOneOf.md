# SledPolicyOneOf

The operator has indicated that the sled is in-service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**provision_policy** | [**SledProvisionPolicy**](SledProvisionPolicy.md) | Determines whether new resources can be provisioned onto the sled. | 

## Example

```python
from oxide.models.sled_policy_one_of import SledPolicyOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of SledPolicyOneOf from a JSON string
sled_policy_one_of_instance = SledPolicyOneOf.from_json(json)
# print the JSON string representation of the object
print(SledPolicyOneOf.to_json())

# convert the object into a dict
sled_policy_one_of_dict = sled_policy_one_of_instance.to_dict()
# create an instance of SledPolicyOneOf from a dict
sled_policy_one_of_from_dict = SledPolicyOneOf.from_dict(sled_policy_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


