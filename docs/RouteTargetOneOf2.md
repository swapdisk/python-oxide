# RouteTargetOneOf2

Forward traffic to a VPC Subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.route_target_one_of2 import RouteTargetOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTargetOneOf2 from a JSON string
route_target_one_of2_instance = RouteTargetOneOf2.from_json(json)
# print the JSON string representation of the object
print(RouteTargetOneOf2.to_json())

# convert the object into a dict
route_target_one_of2_dict = route_target_one_of2_instance.to_dict()
# create an instance of RouteTargetOneOf2 from a dict
route_target_one_of2_from_dict = RouteTargetOneOf2.from_dict(route_target_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


