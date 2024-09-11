# Ipv6Range

A non-decreasing IPv6 address range, inclusive of both ends.  The first address must be less than or equal to the last address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | 
**last** | **str** |  | 

## Example

```python
from oxide.models.ipv6_range import Ipv6Range

# TODO update the JSON string below
json = "{}"
# create an instance of Ipv6Range from a JSON string
ipv6_range_instance = Ipv6Range.from_json(json)
# print the JSON string representation of the object
print(Ipv6Range.to_json())

# convert the object into a dict
ipv6_range_dict = ipv6_range_instance.to_dict()
# create an instance of Ipv6Range from a dict
ipv6_range_from_dict = Ipv6Range.from_dict(ipv6_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


