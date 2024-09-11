# RouteTarget

A `RouteTarget` describes the possible locations that traffic matching a route destination can be sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.route_target import RouteTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTarget from a JSON string
route_target_instance = RouteTarget.from_json(json)
# print the JSON string representation of the object
print(RouteTarget.to_json())

# convert the object into a dict
route_target_dict = route_target_instance.to_dict()
# create an instance of RouteTarget from a dict
route_target_from_dict = RouteTarget.from_dict(route_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


