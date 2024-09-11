# ExternalIpCreateOneOf

An IP address providing both inbound and outbound access. The address is automatically-assigned from the provided IP Pool, or the current silo's default pool if not specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | [**NameOrId**](NameOrId.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from oxide.models.external_ip_create_one_of import ExternalIpCreateOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIpCreateOneOf from a JSON string
external_ip_create_one_of_instance = ExternalIpCreateOneOf.from_json(json)
# print the JSON string representation of the object
print(ExternalIpCreateOneOf.to_json())

# convert the object into a dict
external_ip_create_one_of_dict = external_ip_create_one_of_instance.to_dict()
# create an instance of ExternalIpCreateOneOf from a dict
external_ip_create_one_of_from_dict = ExternalIpCreateOneOf.from_dict(external_ip_create_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


