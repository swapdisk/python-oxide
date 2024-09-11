# ExternalIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP address held by this resource. | 
**kind** | **str** |  | 
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**instance_id** | **str** | The ID of the instance that this Floating IP is attached to, if it is presently in use. | [optional] 
**ip_pool_id** | **str** | The ID of the IP pool this resource belongs to. | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**project_id** | **str** | The project this resource exists within. | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.external_ip import ExternalIp

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIp from a JSON string
external_ip_instance = ExternalIp.from_json(json)
# print the JSON string representation of the object
print(ExternalIp.to_json())

# convert the object into a dict
external_ip_dict = external_ip_instance.to_dict()
# create an instance of ExternalIp from a dict
external_ip_from_dict = ExternalIp.from_dict(external_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


