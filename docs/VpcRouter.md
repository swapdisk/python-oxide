# VpcRouter

A VPC router defines a series of rules that indicate where traffic should be sent depending on its destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**kind** | [**VpcRouterKind**](VpcRouterKind.md) |  | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**vpc_id** | **str** | The VPC to which the router belongs. | 

## Example

```python
from oxide.models.vpc_router import VpcRouter

# TODO update the JSON string below
json = "{}"
# create an instance of VpcRouter from a JSON string
vpc_router_instance = VpcRouter.from_json(json)
# print the JSON string representation of the object
print(VpcRouter.to_json())

# convert the object into a dict
vpc_router_dict = vpc_router_instance.to_dict()
# create an instance of VpcRouter from a dict
vpc_router_from_dict = VpcRouter.from_dict(vpc_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


