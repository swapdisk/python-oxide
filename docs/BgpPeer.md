# BgpPeer

A BGP peer configuration for an interface. Includes the set of announcements that will be advertised to the peer identified by `addr`. The `bgp_config` parameter is a reference to global BGP parameters. The `interface_name` indicates what interface the peer should be contacted on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **str** | The address of the host to peer with. | 
**allowed_export** | [**ImportExportPolicy**](ImportExportPolicy.md) | Define export policy for a peer. | 
**allowed_import** | [**ImportExportPolicy**](ImportExportPolicy.md) | Define import policy for a peer. | 
**bgp_config** | [**NameOrId**](NameOrId.md) | The global BGP configuration used for establishing a session with this peer. | 
**communities** | **List[int]** | Include the provided communities in updates sent to the peer. | 
**connect_retry** | **int** | How long to to wait between TCP connection retries (seconds). | 
**delay_open** | **int** | How long to delay sending an open request after establishing a TCP session (seconds). | 
**enforce_first_as** | **bool** | Enforce that the first AS in paths received from this peer is the peer&#39;s AS. | 
**hold_time** | **int** | How long to hold peer connections between keepalives (seconds). | 
**idle_hold_time** | **int** | How long to hold a peer in idle before attempting a new session (seconds). | 
**interface_name** | **str** | The name of interface to peer on. This is relative to the port configuration this BGP peer configuration is a part of. For example this value could be phy0 to refer to a primary physical interface. Or it could be vlan47 to refer to a VLAN interface. | 
**keepalive** | **int** | How often to send keepalive requests (seconds). | 
**local_pref** | **int** | Apply a local preference to routes received from this peer. | [optional] 
**md5_auth_key** | **str** | Use the given key for TCP-MD5 authentication with the peer. | [optional] 
**min_ttl** | **int** | Require messages from a peer have a minimum IP time to live field. | [optional] 
**multi_exit_discriminator** | **int** | Apply the provided multi-exit discriminator (MED) updates sent to the peer. | [optional] 
**remote_asn** | **int** | Require that a peer has a specified ASN. | [optional] 
**vlan_id** | **int** | Associate a VLAN ID with a peer. | [optional] 

## Example

```python
from oxide.models.bgp_peer import BgpPeer

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeer from a JSON string
bgp_peer_instance = BgpPeer.from_json(json)
# print the JSON string representation of the object
print(BgpPeer.to_json())

# convert the object into a dict
bgp_peer_dict = bgp_peer_instance.to_dict()
# create an instance of BgpPeer from a dict
bgp_peer_from_dict = BgpPeer.from_dict(bgp_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


