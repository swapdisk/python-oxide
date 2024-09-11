# EphemeralIpCreate

Parameters for creating an ephemeral IP address for an instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | [**NameOrId**](NameOrId.md) | Name or ID of the IP pool used to allocate an address | [optional] 

## Example

```python
from oxide.models.ephemeral_ip_create import EphemeralIpCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EphemeralIpCreate from a JSON string
ephemeral_ip_create_instance = EphemeralIpCreate.from_json(json)
# print the JSON string representation of the object
print(EphemeralIpCreate.to_json())

# convert the object into a dict
ephemeral_ip_create_dict = ephemeral_ip_create_instance.to_dict()
# create an instance of EphemeralIpCreate from a dict
ephemeral_ip_create_from_dict = EphemeralIpCreate.from_dict(ephemeral_ip_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


