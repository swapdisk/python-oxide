# SwitchPortSettingsView

This structure contains all port settings information in one place. It's a convenience data structure for getting a complete view of a particular port's settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[SwitchPortAddressConfig]**](SwitchPortAddressConfig.md) | Layer 3 IP address settings. | 
**bgp_peers** | [**List[BgpPeer]**](BgpPeer.md) | BGP peer settings. | 
**groups** | [**List[SwitchPortSettingsGroups]**](SwitchPortSettingsGroups.md) | Switch port settings included from other switch port settings groups. | 
**interfaces** | [**List[SwitchInterfaceConfig]**](SwitchInterfaceConfig.md) | Layer 3 interface settings. | 
**link_lldp** | [**List[LldpLinkConfig]**](LldpLinkConfig.md) | Link-layer discovery protocol (LLDP) settings. | 
**links** | [**List[SwitchPortLinkConfig]**](SwitchPortLinkConfig.md) | Layer 2 link settings. | 
**port** | [**SwitchPortConfig**](SwitchPortConfig.md) | Layer 1 physical port settings. | 
**routes** | [**List[SwitchPortRouteConfig]**](SwitchPortRouteConfig.md) | IP route settings. | 
**settings** | [**SwitchPortSettings**](SwitchPortSettings.md) | The primary switch port settings handle. | 
**vlan_interfaces** | [**List[SwitchVlanInterfaceConfig]**](SwitchVlanInterfaceConfig.md) | Vlan interface settings. | 

## Example

```python
from oxide.models.switch_port_settings_view import SwitchPortSettingsView

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortSettingsView from a JSON string
switch_port_settings_view_instance = SwitchPortSettingsView.from_json(json)
# print the JSON string representation of the object
print(SwitchPortSettingsView.to_json())

# convert the object into a dict
switch_port_settings_view_dict = switch_port_settings_view_instance.to_dict()
# create an instance of SwitchPortSettingsView from a dict
switch_port_settings_view_from_dict = SwitchPortSettingsView.from_dict(switch_port_settings_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


