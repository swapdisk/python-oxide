# SledProvisionPolicy

The operator-defined provision policy of a sled.  This controls whether new resources are going to be provisioned on this sled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.sled_provision_policy import SledProvisionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SledProvisionPolicy from a JSON string
sled_provision_policy_instance = SledProvisionPolicy.from_json(json)
# print the JSON string representation of the object
print(SledProvisionPolicy.to_json())

# convert the object into a dict
sled_provision_policy_dict = sled_provision_policy_instance.to_dict()
# create an instance of SledProvisionPolicy from a dict
sled_provision_policy_from_dict = SledProvisionPolicy.from_dict(sled_provision_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


