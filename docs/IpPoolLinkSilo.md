# IpPoolLinkSilo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | When a pool is the default for a silo, floating IPs and instance ephemeral IPs will come from that pool when no other pool is specified. There can be at most one default for a given silo. | 
**silo** | [**NameOrId**](NameOrId.md) |  | 

## Example

```python
from oxide.models.ip_pool_link_silo import IpPoolLinkSilo

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolLinkSilo from a JSON string
ip_pool_link_silo_instance = IpPoolLinkSilo.from_json(json)
# print the JSON string representation of the object
print(IpPoolLinkSilo.to_json())

# convert the object into a dict
ip_pool_link_silo_dict = ip_pool_link_silo_instance.to_dict()
# create an instance of IpPoolLinkSilo from a dict
ip_pool_link_silo_from_dict = IpPoolLinkSilo.from_dict(ip_pool_link_silo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


