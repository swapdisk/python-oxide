# BgpAnnounceSet

Represents a BGP announce set by id. The id can be used with other API calls to view and manage the announce set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.bgp_announce_set import BgpAnnounceSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAnnounceSet from a JSON string
bgp_announce_set_instance = BgpAnnounceSet.from_json(json)
# print the JSON string representation of the object
print(BgpAnnounceSet.to_json())

# convert the object into a dict
bgp_announce_set_dict = bgp_announce_set_instance.to_dict()
# create an instance of BgpAnnounceSet from a dict
bgp_announce_set_from_dict = BgpAnnounceSet.from_dict(bgp_announce_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


