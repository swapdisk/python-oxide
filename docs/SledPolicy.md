# SledPolicy

The operator-defined policy of a sled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**provision_policy** | [**SledProvisionPolicy**](SledProvisionPolicy.md) | Determines whether new resources can be provisioned onto the sled. | 

## Example

```python
from oxide.models.sled_policy import SledPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SledPolicy from a JSON string
sled_policy_instance = SledPolicy.from_json(json)
# print the JSON string representation of the object
print(SledPolicy.to_json())

# convert the object into a dict
sled_policy_dict = sled_policy_instance.to_dict()
# create an instance of SledPolicy from a dict
sled_policy_from_dict = SledPolicy.from_dict(sled_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


