# LldpLinkConfigCreate

The LLDP configuration associated with a port.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **str** | The LLDP chassis identifier TLV. | [optional] 
**enabled** | **bool** | Whether or not LLDP is enabled. | 
**link_description** | **str** | The LLDP link description TLV. | [optional] 
**link_name** | **str** | The LLDP link name TLV. | [optional] 
**management_ip** | **str** | The LLDP management IP TLV. | [optional] 
**system_description** | **str** | The LLDP system description TLV. | [optional] 
**system_name** | **str** | The LLDP system name TLV. | [optional] 

## Example

```python
from oxide.models.lldp_link_config_create import LldpLinkConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LldpLinkConfigCreate from a JSON string
lldp_link_config_create_instance = LldpLinkConfigCreate.from_json(json)
# print the JSON string representation of the object
print(LldpLinkConfigCreate.to_json())

# convert the object into a dict
lldp_link_config_create_dict = lldp_link_config_create_instance.to_dict()
# create an instance of LldpLinkConfigCreate from a dict
lldp_link_config_create_from_dict = LldpLinkConfigCreate.from_dict(lldp_link_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


