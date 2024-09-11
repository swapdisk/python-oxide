# RouterRoute

A route defines a rule that governs where traffic should be sent based on its destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**destination** | [**RouteDestination**](RouteDestination.md) | Selects which traffic this routing rule will apply to. | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**kind** | [**RouterRouteKind**](RouterRouteKind.md) | Describes the kind of router. Set at creation. &#x60;read-only&#x60; | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**target** | [**RouteTarget**](RouteTarget.md) | The location that matched packets should be forwarded to. | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**vpc_router_id** | **str** | The ID of the VPC Router to which the route belongs | 

## Example

```python
from oxide.models.router_route import RouterRoute

# TODO update the JSON string below
json = "{}"
# create an instance of RouterRoute from a JSON string
router_route_instance = RouterRoute.from_json(json)
# print the JSON string representation of the object
print(RouterRoute.to_json())

# convert the object into a dict
router_route_dict = router_route_instance.to_dict()
# create an instance of RouterRoute from a dict
router_route_from_dict = RouterRoute.from_dict(router_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


