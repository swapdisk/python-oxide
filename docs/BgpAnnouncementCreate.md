# BgpAnnouncementCreate

A BGP announcement tied to a particular address lot block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lot_block** | [**NameOrId**](NameOrId.md) | Address lot this announcement is drawn from. | 
**network** | [**IpNet**](IpNet.md) | The network being announced. | 

## Example

```python
from oxide.models.bgp_announcement_create import BgpAnnouncementCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAnnouncementCreate from a JSON string
bgp_announcement_create_instance = BgpAnnouncementCreate.from_json(json)
# print the JSON string representation of the object
print(BgpAnnouncementCreate.to_json())

# convert the object into a dict
bgp_announcement_create_dict = bgp_announcement_create_instance.to_dict()
# create an instance of BgpAnnouncementCreate from a dict
bgp_announcement_create_from_dict = BgpAnnouncementCreate.from_dict(bgp_announcement_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


