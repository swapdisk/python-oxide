# RouteTargetOneOf

Forward traffic to a particular IP address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from oxide.models.route_target_one_of import RouteTargetOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTargetOneOf from a JSON string
route_target_one_of_instance = RouteTargetOneOf.from_json(json)
# print the JSON string representation of the object
print(RouteTargetOneOf.to_json())

# convert the object into a dict
route_target_one_of_dict = route_target_one_of_instance.to_dict()
# create an instance of RouteTargetOneOf from a dict
route_target_one_of_from_dict = RouteTargetOneOf.from_dict(route_target_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


