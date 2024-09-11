# SwitchPortLinkConfig

A link configuration for a port settings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoneg** | **bool** | Whether or not the link has autonegotiation enabled. | 
**fec** | [**LinkFec**](LinkFec.md) | The forward error correction mode of the link. | 
**link_name** | **str** | The name of this link. | 
**lldp_link_config_id** | **str** | The link-layer discovery protocol service configuration id for this link. | [optional] 
**mtu** | **int** | The maximum transmission unit for this link. | 
**port_settings_id** | **str** | The port settings this link configuration belongs to. | 
**speed** | [**LinkSpeed**](LinkSpeed.md) | The configured speed of the link. | 

## Example

```python
from oxide.models.switch_port_link_config import SwitchPortLinkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortLinkConfig from a JSON string
switch_port_link_config_instance = SwitchPortLinkConfig.from_json(json)
# print the JSON string representation of the object
print(SwitchPortLinkConfig.to_json())

# convert the object into a dict
switch_port_link_config_dict = switch_port_link_config_instance.to_dict()
# create an instance of SwitchPortLinkConfig from a dict
switch_port_link_config_from_dict = SwitchPortLinkConfig.from_dict(switch_port_link_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


