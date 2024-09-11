# BgpConfig

A base BGP configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | The autonomous system number of this BGP configuration. | 
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**vrf** | **str** | Optional virtual routing and forwarding identifier for this BGP configuration. | [optional] 

## Example

```python
from oxide.models.bgp_config import BgpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BgpConfig from a JSON string
bgp_config_instance = BgpConfig.from_json(json)
# print the JSON string representation of the object
print(BgpConfig.to_json())

# convert the object into a dict
bgp_config_dict = bgp_config_instance.to_dict()
# create an instance of BgpConfig from a dict
bgp_config_from_dict = BgpConfig.from_dict(bgp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


