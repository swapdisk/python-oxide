# BgpPeerStatus

The current status of a BGP peer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **str** | IP address of the peer. | 
**local_asn** | **int** | Local autonomous system number. | 
**remote_asn** | **int** | Remote autonomous system number. | 
**state** | [**BgpPeerState**](BgpPeerState.md) | State of the peer. | 
**state_duration_millis** | **int** | Time of last state change. | 
**switch** | [**SwitchLocation**](SwitchLocation.md) | Switch with the peer session. | 

## Example

```python
from oxide.models.bgp_peer_status import BgpPeerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeerStatus from a JSON string
bgp_peer_status_instance = BgpPeerStatus.from_json(json)
# print the JSON string representation of the object
print(BgpPeerStatus.to_json())

# convert the object into a dict
bgp_peer_status_dict = bgp_peer_status_instance.to_dict()
# create an instance of BgpPeerStatus from a dict
bgp_peer_status_from_dict = BgpPeerStatus.from_dict(bgp_peer_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


