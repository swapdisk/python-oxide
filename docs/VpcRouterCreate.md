# VpcRouterCreate

Create-time parameters for a `VpcRouter`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.vpc_router_create import VpcRouterCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VpcRouterCreate from a JSON string
vpc_router_create_instance = VpcRouterCreate.from_json(json)
# print the JSON string representation of the object
print(VpcRouterCreate.to_json())

# convert the object into a dict
vpc_router_create_dict = vpc_router_create_instance.to_dict()
# create an instance of VpcRouterCreate from a dict
vpc_router_create_from_dict = VpcRouterCreate.from_dict(vpc_router_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


