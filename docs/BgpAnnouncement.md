# BgpAnnouncement

A BGP announcement tied to an address lot block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lot_block_id** | **str** | The address block the IP network being announced is drawn from. | 
**announce_set_id** | **str** | The id of the set this announcement is a part of. | 
**network** | [**IpNet**](IpNet.md) | The IP network being announced. | 

## Example

```python
from oxide.models.bgp_announcement import BgpAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAnnouncement from a JSON string
bgp_announcement_instance = BgpAnnouncement.from_json(json)
# print the JSON string representation of the object
print(BgpAnnouncement.to_json())

# convert the object into a dict
bgp_announcement_dict = bgp_announcement_instance.to_dict()
# create an instance of BgpAnnouncement from a dict
bgp_announcement_from_dict = BgpAnnouncement.from_dict(bgp_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


