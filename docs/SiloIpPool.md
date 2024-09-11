# SiloIpPool

An IP pool in the context of a silo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**is_default** | **bool** | When a pool is the default for a silo, floating IPs and instance ephemeral IPs will come from that pool when no other pool is specified. There can be at most one default for a given silo. | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.silo_ip_pool import SiloIpPool

# TODO update the JSON string below
json = "{}"
# create an instance of SiloIpPool from a JSON string
silo_ip_pool_instance = SiloIpPool.from_json(json)
# print the JSON string representation of the object
print(SiloIpPool.to_json())

# convert the object into a dict
silo_ip_pool_dict = silo_ip_pool_instance.to_dict()
# create an instance of SiloIpPool from a dict
silo_ip_pool_from_dict = SiloIpPool.from_dict(silo_ip_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


