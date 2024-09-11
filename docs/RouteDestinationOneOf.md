# RouteDestinationOneOf

Route applies to traffic destined for a specific IP address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from oxide.models.route_destination_one_of import RouteDestinationOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RouteDestinationOneOf from a JSON string
route_destination_one_of_instance = RouteDestinationOneOf.from_json(json)
# print the JSON string representation of the object
print(RouteDestinationOneOf.to_json())

# convert the object into a dict
route_destination_one_of_dict = route_destination_one_of_instance.to_dict()
# create an instance of RouteDestinationOneOf from a dict
route_destination_one_of_from_dict = RouteDestinationOneOf.from_dict(route_destination_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


