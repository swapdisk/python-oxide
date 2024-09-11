# RouterRouteKind

The kind of a `RouterRoute`  The kind determines certain attributes such as if the route is modifiable and describes how or where the route was created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.router_route_kind import RouterRouteKind

# TODO update the JSON string below
json = "{}"
# create an instance of RouterRouteKind from a JSON string
router_route_kind_instance = RouterRouteKind.from_json(json)
# print the JSON string representation of the object
print(RouterRouteKind.to_json())

# convert the object into a dict
router_route_kind_dict = router_route_kind_instance.to_dict()
# create an instance of RouterRouteKind from a dict
router_route_kind_from_dict = RouterRouteKind.from_dict(router_route_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


