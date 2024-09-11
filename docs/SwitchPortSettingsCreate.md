# SwitchPortSettingsCreate

Parameters for creating switch port settings. Switch port settings are the central data structure for setting up external networking. Switch port settings include link, interface, route, address and dynamic network protocol configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**Dict[str, AddressConfig]**](AddressConfig.md) | Addresses indexed by interface name. | 
**bgp_peers** | [**Dict[str, BgpPeerConfig]**](BgpPeerConfig.md) | BGP peers indexed by interface name. | 
**description** | **str** |  | 
**groups** | [**List[NameOrId]**](NameOrId.md) |  | 
**interfaces** | [**Dict[str, SwitchInterfaceConfigCreate]**](SwitchInterfaceConfigCreate.md) | Interfaces indexed by link name. | 
**links** | [**Dict[str, LinkConfigCreate]**](LinkConfigCreate.md) | Links indexed by phy name. On ports that are not broken out, this is always phy0. On a 2x breakout the options are phy0 and phy1, on 4x phy0-phy3, etc. | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**port_config** | [**SwitchPortConfigCreate**](SwitchPortConfigCreate.md) |  | 
**routes** | [**Dict[str, RouteConfig]**](RouteConfig.md) | Routes indexed by interface name. | 

## Example

```python
from oxide.models.switch_port_settings_create import SwitchPortSettingsCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortSettingsCreate from a JSON string
switch_port_settings_create_instance = SwitchPortSettingsCreate.from_json(json)
# print the JSON string representation of the object
print(SwitchPortSettingsCreate.to_json())

# convert the object into a dict
switch_port_settings_create_dict = switch_port_settings_create_instance.to_dict()
# create an instance of SwitchPortSettingsCreate from a dict
switch_port_settings_create_from_dict = SwitchPortSettingsCreate.from_dict(switch_port_settings_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


