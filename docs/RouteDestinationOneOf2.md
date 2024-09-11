# RouteDestinationOneOf2

Route applies to traffic destined for the given VPC.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.route_destination_one_of2 import RouteDestinationOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of RouteDestinationOneOf2 from a JSON string
route_destination_one_of2_instance = RouteDestinationOneOf2.from_json(json)
# print the JSON string representation of the object
print(RouteDestinationOneOf2.to_json())

# convert the object into a dict
route_destination_one_of2_dict = route_destination_one_of2_instance.to_dict()
# create an instance of RouteDestinationOneOf2 from a dict
route_destination_one_of2_from_dict = RouteDestinationOneOf2.from_dict(route_destination_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


