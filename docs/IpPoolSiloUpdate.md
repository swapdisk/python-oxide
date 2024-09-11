# IpPoolSiloUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | When a pool is the default for a silo, floating IPs and instance ephemeral IPs will come from that pool when no other pool is specified. There can be at most one default for a given silo, so when a pool is made default, an existing default will remain linked but will no longer be the default. | 

## Example

```python
from oxide.models.ip_pool_silo_update import IpPoolSiloUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolSiloUpdate from a JSON string
ip_pool_silo_update_instance = IpPoolSiloUpdate.from_json(json)
# print the JSON string representation of the object
print(IpPoolSiloUpdate.to_json())

# convert the object into a dict
ip_pool_silo_update_dict = ip_pool_silo_update_instance.to_dict()
# create an instance of IpPoolSiloUpdate from a dict
ip_pool_silo_update_from_dict = IpPoolSiloUpdate.from_dict(ip_pool_silo_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


