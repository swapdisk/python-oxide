# LldpLinkConfig

A link layer discovery protocol (LLDP) service configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **str** | The LLDP chassis identifier TLV. | [optional] 
**enabled** | **bool** | Whether or not the LLDP service is enabled. | 
**id** | **str** | The id of this LLDP service instance. | 
**link_description** | **str** | The LLDP link description TLV. | [optional] 
**link_name** | **str** | The LLDP link name TLV. | [optional] 
**management_ip** | [**IpNet**](IpNet.md) | The LLDP management IP TLV. | [optional] 
**system_description** | **str** | The LLDP system description TLV. | [optional] 
**system_name** | **str** | The LLDP system name TLV. | [optional] 

## Example

```python
from oxide.models.lldp_link_config import LldpLinkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LldpLinkConfig from a JSON string
lldp_link_config_instance = LldpLinkConfig.from_json(json)
# print the JSON string representation of the object
print(LldpLinkConfig.to_json())

# convert the object into a dict
lldp_link_config_dict = lldp_link_config_instance.to_dict()
# create an instance of LldpLinkConfig from a dict
lldp_link_config_from_dict = LldpLinkConfig.from_dict(lldp_link_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


