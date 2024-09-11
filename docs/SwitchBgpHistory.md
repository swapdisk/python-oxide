# SwitchBgpHistory

BGP message history for a particular switch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history** | **Dict[str, object]** | Message history indexed by peer address. | 
**switch** | [**SwitchLocation**](SwitchLocation.md) | Switch this message history is associated with. | 

## Example

```python
from oxide.models.switch_bgp_history import SwitchBgpHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchBgpHistory from a JSON string
switch_bgp_history_instance = SwitchBgpHistory.from_json(json)
# print the JSON string representation of the object
print(SwitchBgpHistory.to_json())

# convert the object into a dict
switch_bgp_history_dict = switch_bgp_history_instance.to_dict()
# create an instance of SwitchBgpHistory from a dict
switch_bgp_history_from_dict = SwitchBgpHistory.from_dict(switch_bgp_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


