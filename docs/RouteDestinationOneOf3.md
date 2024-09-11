# RouteDestinationOneOf3

Route applies to traffic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.route_destination_one_of3 import RouteDestinationOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of RouteDestinationOneOf3 from a JSON string
route_destination_one_of3_instance = RouteDestinationOneOf3.from_json(json)
# print the JSON string representation of the object
print(RouteDestinationOneOf3.to_json())

# convert the object into a dict
route_destination_one_of3_dict = route_destination_one_of3_instance.to_dict()
# create an instance of RouteDestinationOneOf3 from a dict
route_destination_one_of3_from_dict = RouteDestinationOneOf3.from_dict(route_destination_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


