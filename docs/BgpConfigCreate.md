# BgpConfigCreate

Parameters for creating a BGP configuration. This includes and autonomous system number (ASN) and a virtual routing and forwarding (VRF) identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | The autonomous system number of this BGP configuration. | 
**bgp_announce_set_id** | [**NameOrId**](NameOrId.md) |  | 
**description** | **str** |  | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**vrf** | **str** | Optional virtual routing and forwarding identifier for this BGP configuration. | [optional] 

## Example

```python
from oxide.models.bgp_config_create import BgpConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BgpConfigCreate from a JSON string
bgp_config_create_instance = BgpConfigCreate.from_json(json)
# print the JSON string representation of the object
print(BgpConfigCreate.to_json())

# convert the object into a dict
bgp_config_create_dict = bgp_config_create_instance.to_dict()
# create an instance of BgpConfigCreate from a dict
bgp_config_create_from_dict = BgpConfigCreate.from_dict(bgp_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


