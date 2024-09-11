# ExternalIpCreateOneOf1

An IP address providing both inbound and outbound access. The address is an existing floating IP object assigned to the current project.  The floating IP must not be in use by another instance or service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floating_ip** | [**NameOrId**](NameOrId.md) |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.external_ip_create_one_of1 import ExternalIpCreateOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIpCreateOneOf1 from a JSON string
external_ip_create_one_of1_instance = ExternalIpCreateOneOf1.from_json(json)
# print the JSON string representation of the object
print(ExternalIpCreateOneOf1.to_json())

# convert the object into a dict
external_ip_create_one_of1_dict = external_ip_create_one_of1_instance.to_dict()
# create an instance of ExternalIpCreateOneOf1 from a dict
external_ip_create_one_of1_from_dict = ExternalIpCreateOneOf1.from_dict(external_ip_create_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


