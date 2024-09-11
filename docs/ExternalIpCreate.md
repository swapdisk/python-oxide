# ExternalIpCreate

Parameters for creating an external IP address for instances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | [**NameOrId**](NameOrId.md) |  | [optional] 
**type** | **str** |  | 
**floating_ip** | [**NameOrId**](NameOrId.md) |  | 

## Example

```python
from oxide.models.external_ip_create import ExternalIpCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIpCreate from a JSON string
external_ip_create_instance = ExternalIpCreate.from_json(json)
# print the JSON string representation of the object
print(ExternalIpCreate.to_json())

# convert the object into a dict
external_ip_create_dict = external_ip_create_instance.to_dict()
# create an instance of ExternalIpCreate from a dict
external_ip_create_from_dict = ExternalIpCreate.from_dict(external_ip_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


