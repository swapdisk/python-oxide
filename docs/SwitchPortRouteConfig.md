# SwitchPortRouteConfig

A route configuration for a port settings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst** | [**IpNet**](IpNet.md) | The route&#39;s destination network. | 
**gw** | [**IpNet**](IpNet.md) | The route&#39;s gateway address. | 
**interface_name** | **str** | The interface name this route configuration is assigned to. | 
**local_pref** | **int** | Local preference indicating priority within and across protocols. | [optional] 
**port_settings_id** | **str** | The port settings object this route configuration belongs to. | 
**vlan_id** | **int** | The VLAN identifier for the route. Use this if the gateway is reachable over an 802.1Q tagged L2 segment. | [optional] 

## Example

```python
from oxide.models.switch_port_route_config import SwitchPortRouteConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortRouteConfig from a JSON string
switch_port_route_config_instance = SwitchPortRouteConfig.from_json(json)
# print the JSON string representation of the object
print(SwitchPortRouteConfig.to_json())

# convert the object into a dict
switch_port_route_config_dict = switch_port_route_config_instance.to_dict()
# create an instance of SwitchPortRouteConfig from a dict
switch_port_route_config_from_dict = SwitchPortRouteConfig.from_dict(switch_port_route_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


