# BfdSessionEnable

Information about a bidirectional forwarding detection (BFD) session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detection_threshold** | **int** | The negotiated Control packet transmission interval, multiplied by this variable, will be the Detection Time for this session (as seen by the remote system) | 
**local** | **str** | Address the Oxide switch will listen on for BFD traffic. If &#x60;None&#x60; then the unspecified address (0.0.0.0 or ::) is used. | [optional] 
**mode** | [**BfdMode**](BfdMode.md) | Select either single-hop (RFC 5881) or multi-hop (RFC 5883) | 
**remote** | **str** | Address of the remote peer to establish a BFD session with. | 
**required_rx** | **int** | The minimum interval, in microseconds, between received BFD Control packets that this system requires | 
**switch** | **str** | The switch to enable this session on. Must be &#x60;switch0&#x60; or &#x60;switch1&#x60;. | 

## Example

```python
from oxide.models.bfd_session_enable import BfdSessionEnable

# TODO update the JSON string below
json = "{}"
# create an instance of BfdSessionEnable from a JSON string
bfd_session_enable_instance = BfdSessionEnable.from_json(json)
# print the JSON string representation of the object
print(BfdSessionEnable.to_json())

# convert the object into a dict
bfd_session_enable_dict = bfd_session_enable_instance.to_dict()
# create an instance of BfdSessionEnable from a dict
bfd_session_enable_from_dict = BfdSessionEnable.from_dict(bfd_session_enable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


