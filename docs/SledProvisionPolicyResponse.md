# SledProvisionPolicyResponse

Response to `sled_set_provision_policy`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_state** | [**SledProvisionPolicy**](SledProvisionPolicy.md) | The new provision state. | 
**old_state** | [**SledProvisionPolicy**](SledProvisionPolicy.md) | The old provision state. | 

## Example

```python
from oxide.models.sled_provision_policy_response import SledProvisionPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SledProvisionPolicyResponse from a JSON string
sled_provision_policy_response_instance = SledProvisionPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(SledProvisionPolicyResponse.to_json())

# convert the object into a dict
sled_provision_policy_response_dict = sled_provision_policy_response_instance.to_dict()
# create an instance of SledProvisionPolicyResponse from a dict
sled_provision_policy_response_from_dict = SledProvisionPolicyResponse.from_dict(sled_provision_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


