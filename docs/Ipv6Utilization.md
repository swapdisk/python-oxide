# Ipv6Utilization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | **str** | The number of IPv6 addresses allocated from this pool. A 128-bit integer string to match the capacity field. | 
**capacity** | **str** | The total number of IPv6 addresses in the pool, i.e., the sum of the lengths of the IPv6 ranges. An IPv6 range can contain up to 2^128 addresses, so we represent this value in JSON as a numeric string with a custom \&quot;uint128\&quot; format. | 

## Example

```python
from oxide.models.ipv6_utilization import Ipv6Utilization

# TODO update the JSON string below
json = "{}"
# create an instance of Ipv6Utilization from a JSON string
ipv6_utilization_instance = Ipv6Utilization.from_json(json)
# print the JSON string representation of the object
print(Ipv6Utilization.to_json())

# convert the object into a dict
ipv6_utilization_dict = ipv6_utilization_instance.to_dict()
# create an instance of Ipv6Utilization from a dict
ipv6_utilization_from_dict = Ipv6Utilization.from_dict(ipv6_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


