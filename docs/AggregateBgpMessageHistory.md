# AggregateBgpMessageHistory

BGP message history for rack switches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_histories** | [**List[SwitchBgpHistory]**](SwitchBgpHistory.md) | BGP history organized by switch. | 

## Example

```python
from oxide.models.aggregate_bgp_message_history import AggregateBgpMessageHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateBgpMessageHistory from a JSON string
aggregate_bgp_message_history_instance = AggregateBgpMessageHistory.from_json(json)
# print the JSON string representation of the object
print(AggregateBgpMessageHistory.to_json())

# convert the object into a dict
aggregate_bgp_message_history_dict = aggregate_bgp_message_history_instance.to_dict()
# create an instance of AggregateBgpMessageHistory from a dict
aggregate_bgp_message_history_from_dict = AggregateBgpMessageHistory.from_dict(aggregate_bgp_message_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


