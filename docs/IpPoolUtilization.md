# IpPoolUtilization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**Ipv4Utilization**](Ipv4Utilization.md) | Number of allocated and total available IPv4 addresses in pool | 
**ipv6** | [**Ipv6Utilization**](Ipv6Utilization.md) | Number of allocated and total available IPv6 addresses in pool | 

## Example

```python
from oxide.models.ip_pool_utilization import IpPoolUtilization

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolUtilization from a JSON string
ip_pool_utilization_instance = IpPoolUtilization.from_json(json)
# print the JSON string representation of the object
print(IpPoolUtilization.to_json())

# convert the object into a dict
ip_pool_utilization_dict = ip_pool_utilization_instance.to_dict()
# create an instance of IpPoolUtilization from a dict
ip_pool_utilization_from_dict = IpPoolUtilization.from_dict(ip_pool_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


