# LinkConfigCreate

Switch link configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoneg** | **bool** | Whether or not to set autonegotiation | 
**fec** | [**LinkFec**](LinkFec.md) | The forward error correction mode of the link. | 
**lldp** | [**LldpLinkConfigCreate**](LldpLinkConfigCreate.md) | The link-layer discovery protocol (LLDP) configuration for the link. | 
**mtu** | **int** | Maximum transmission unit for the link. | 
**speed** | [**LinkSpeed**](LinkSpeed.md) | The speed of the link. | 

## Example

```python
from oxide.models.link_config_create import LinkConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LinkConfigCreate from a JSON string
link_config_create_instance = LinkConfigCreate.from_json(json)
# print the JSON string representation of the object
print(LinkConfigCreate.to_json())

# convert the object into a dict
link_config_create_dict = link_config_create_instance.to_dict()
# create an instance of LinkConfigCreate from a dict
link_config_create_from_dict = LinkConfigCreate.from_dict(link_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


