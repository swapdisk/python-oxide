# RouteDestination

A `RouteDestination` is used to match traffic with a routing rule, on the destination of that traffic.  When traffic is to be sent to a destination that is within a given `RouteDestination`, the corresponding `RouterRoute` applies, and traffic will be forward to the `RouteTarget` for that rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.route_destination import RouteDestination

# TODO update the JSON string below
json = "{}"
# create an instance of RouteDestination from a JSON string
route_destination_instance = RouteDestination.from_json(json)
# print the JSON string representation of the object
print(RouteDestination.to_json())

# convert the object into a dict
route_destination_dict = route_destination_instance.to_dict()
# create an instance of RouteDestination from a dict
route_destination_from_dict = RouteDestination.from_dict(route_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


