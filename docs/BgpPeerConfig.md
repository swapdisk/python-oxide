# BgpPeerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peers** | [**List[BgpPeer]**](BgpPeer.md) |  | 

## Example

```python
from oxide.models.bgp_peer_config import BgpPeerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeerConfig from a JSON string
bgp_peer_config_instance = BgpPeerConfig.from_json(json)
# print the JSON string representation of the object
print(BgpPeerConfig.to_json())

# convert the object into a dict
bgp_peer_config_dict = bgp_peer_config_instance.to_dict()
# create an instance of BgpPeerConfig from a dict
bgp_peer_config_from_dict = BgpPeerConfig.from_dict(bgp_peer_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


