# IpPoolSiloLink

A link between an IP pool and a silo that allows one to allocate IPs from the pool within the silo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_pool_id** | **str** |  | 
**is_default** | **bool** | When a pool is the default for a silo, floating IPs and instance ephemeral IPs will come from that pool when no other pool is specified. There can be at most one default for a given silo. | 
**silo_id** | **str** |  | 

## Example

```python
from oxide.models.ip_pool_silo_link import IpPoolSiloLink

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolSiloLink from a JSON string
ip_pool_silo_link_instance = IpPoolSiloLink.from_json(json)
# print the JSON string representation of the object
print(IpPoolSiloLink.to_json())

# convert the object into a dict
ip_pool_silo_link_dict = ip_pool_silo_link_instance.to_dict()
# create an instance of IpPoolSiloLink from a dict
ip_pool_silo_link_from_dict = IpPoolSiloLink.from_dict(ip_pool_silo_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


