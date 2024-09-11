# RouteDestinationOneOf1

Route applies to traffic destined for a specific IP subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | [**IpNet**](IpNet.md) |  | 

## Example

```python
from oxide.models.route_destination_one_of1 import RouteDestinationOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of RouteDestinationOneOf1 from a JSON string
route_destination_one_of1_instance = RouteDestinationOneOf1.from_json(json)
# print the JSON string representation of the object
print(RouteDestinationOneOf1.to_json())

# convert the object into a dict
route_destination_one_of1_dict = route_destination_one_of1_instance.to_dict()
# create an instance of RouteDestinationOneOf1 from a dict
route_destination_one_of1_from_dict = RouteDestinationOneOf1.from_dict(route_destination_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


