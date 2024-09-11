# Vpc

View of a VPC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**dns_name** | **str** | The name used for the VPC in DNS. | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**ipv6_prefix** | **str** | The unique local IPv6 address range for subnets in this VPC | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**project_id** | **str** | id for the project containing this VPC | 
**system_router_id** | **str** | id for the system router where subnet default routes are registered | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.vpc import Vpc

# TODO update the JSON string below
json = "{}"
# create an instance of Vpc from a JSON string
vpc_instance = Vpc.from_json(json)
# print the JSON string representation of the object
print(Vpc.to_json())

# convert the object into a dict
vpc_dict = vpc_instance.to_dict()
# create an instance of Vpc from a dict
vpc_from_dict = Vpc.from_dict(vpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


