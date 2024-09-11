# Ipv4Range

A non-decreasing IPv4 address range, inclusive of both ends.  The first address must be less than or equal to the last address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | 
**last** | **str** |  | 

## Example

```python
from oxide.models.ipv4_range import Ipv4Range

# TODO update the JSON string below
json = "{}"
# create an instance of Ipv4Range from a JSON string
ipv4_range_instance = Ipv4Range.from_json(json)
# print the JSON string representation of the object
print(Ipv4Range.to_json())

# convert the object into a dict
ipv4_range_dict = ipv4_range_instance.to_dict()
# create an instance of Ipv4Range from a dict
ipv4_range_from_dict = Ipv4Range.from_dict(ipv4_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


