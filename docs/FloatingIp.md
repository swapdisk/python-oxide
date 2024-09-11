# FloatingIp

A Floating IP is a well-known IP address which can be attached and detached from instances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**instance_id** | **str** | The ID of the instance that this Floating IP is attached to, if it is presently in use. | [optional] 
**ip** | **str** | The IP address held by this resource. | 
**ip_pool_id** | **str** | The ID of the IP pool this resource belongs to. | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**project_id** | **str** | The project this resource exists within. | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.floating_ip import FloatingIp

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIp from a JSON string
floating_ip_instance = FloatingIp.from_json(json)
# print the JSON string representation of the object
print(FloatingIp.to_json())

# convert the object into a dict
floating_ip_dict = floating_ip_instance.to_dict()
# create an instance of FloatingIp from a dict
floating_ip_from_dict = FloatingIp.from_dict(floating_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


