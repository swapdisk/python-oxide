# Ipv4Utilization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | **int** | The number of IPv4 addresses allocated from this pool | 
**capacity** | **int** | The total number of IPv4 addresses in the pool, i.e., the sum of the lengths of the IPv4 ranges. Unlike IPv6 capacity, can be a 32-bit integer because there are only 2^32 IPv4 addresses. | 

## Example

```python
from oxide.models.ipv4_utilization import Ipv4Utilization

# TODO update the JSON string below
json = "{}"
# create an instance of Ipv4Utilization from a JSON string
ipv4_utilization_instance = Ipv4Utilization.from_json(json)
# print the JSON string representation of the object
print(Ipv4Utilization.to_json())

# convert the object into a dict
ipv4_utilization_dict = ipv4_utilization_instance.to_dict()
# create an instance of Ipv4Utilization from a dict
ipv4_utilization_from_dict = Ipv4Utilization.from_dict(ipv4_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


