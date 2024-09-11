# BgpPeerState

The current state of a BGP peer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.bgp_peer_state import BgpPeerState

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeerState from a JSON string
bgp_peer_state_instance = BgpPeerState.from_json(json)
# print the JSON string representation of the object
print(BgpPeerState.to_json())

# convert the object into a dict
bgp_peer_state_dict = bgp_peer_state_instance.to_dict()
# create an instance of BgpPeerState from a dict
bgp_peer_state_from_dict = BgpPeerState.from_dict(bgp_peer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


