# ExternalIpOneOf1

A Floating IP is a well-known IP address which can be attached and detached from instances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**instance_id** | **str** | The ID of the instance that this Floating IP is attached to, if it is presently in use. | [optional] 
**ip** | **str** | The IP address held by this resource. | 
**ip_pool_id** | **str** | The ID of the IP pool this resource belongs to. | 
**kind** | **str** |  | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**project_id** | **str** | The project this resource exists within. | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.external_ip_one_of1 import ExternalIpOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIpOneOf1 from a JSON string
external_ip_one_of1_instance = ExternalIpOneOf1.from_json(json)
# print the JSON string representation of the object
print(ExternalIpOneOf1.to_json())

# convert the object into a dict
external_ip_one_of1_dict = external_ip_one_of1_instance.to_dict()
# create an instance of ExternalIpOneOf1 from a dict
external_ip_one_of1_from_dict = ExternalIpOneOf1.from_dict(external_ip_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


