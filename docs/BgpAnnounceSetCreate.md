# BgpAnnounceSetCreate

Parameters for creating a named set of BGP announcements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | [**List[BgpAnnouncementCreate]**](BgpAnnouncementCreate.md) | The announcements in this set. | 
**description** | **str** |  | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.bgp_announce_set_create import BgpAnnounceSetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAnnounceSetCreate from a JSON string
bgp_announce_set_create_instance = BgpAnnounceSetCreate.from_json(json)
# print the JSON string representation of the object
print(BgpAnnounceSetCreate.to_json())

# convert the object into a dict
bgp_announce_set_create_dict = bgp_announce_set_create_instance.to_dict()
# create an instance of BgpAnnounceSetCreate from a dict
bgp_announce_set_create_from_dict = BgpAnnounceSetCreate.from_dict(bgp_announce_set_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


