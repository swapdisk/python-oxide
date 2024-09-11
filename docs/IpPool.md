# IpPool

A collection of IP ranges. If a pool is linked to a silo, IP addresses from the pool can be allocated within that silo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.ip_pool import IpPool

# TODO update the JSON string below
json = "{}"
# create an instance of IpPool from a JSON string
ip_pool_instance = IpPool.from_json(json)
# print the JSON string representation of the object
print(IpPool.to_json())

# convert the object into a dict
ip_pool_dict = ip_pool_instance.to_dict()
# create an instance of IpPool from a dict
ip_pool_from_dict = IpPool.from_dict(ip_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


