# RouterRouteUpdate

Updateable properties of a `RouterRoute`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**destination** | [**RouteDestination**](RouteDestination.md) | Selects which traffic this routing rule will apply to. | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | [optional] 
**target** | [**RouteTarget**](RouteTarget.md) | The location that matched packets should be forwarded to. | 

## Example

```python
from oxide.models.router_route_update import RouterRouteUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RouterRouteUpdate from a JSON string
router_route_update_instance = RouterRouteUpdate.from_json(json)
# print the JSON string representation of the object
print(RouterRouteUpdate.to_json())

# convert the object into a dict
router_route_update_dict = router_route_update_instance.to_dict()
# create an instance of RouterRouteUpdate from a dict
router_route_update_from_dict = RouterRouteUpdate.from_dict(router_route_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


