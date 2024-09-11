# SledProvisionPolicyParams

Parameters for `sled_set_provision_policy`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**SledProvisionPolicy**](SledProvisionPolicy.md) | The provision state. | 

## Example

```python
from oxide.models.sled_provision_policy_params import SledProvisionPolicyParams

# TODO update the JSON string below
json = "{}"
# create an instance of SledProvisionPolicyParams from a JSON string
sled_provision_policy_params_instance = SledProvisionPolicyParams.from_json(json)
# print the JSON string representation of the object
print(SledProvisionPolicyParams.to_json())

# convert the object into a dict
sled_provision_policy_params_dict = sled_provision_policy_params_instance.to_dict()
# create an instance of SledProvisionPolicyParams from a dict
sled_provision_policy_params_from_dict = SledProvisionPolicyParams.from_dict(sled_provision_policy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


