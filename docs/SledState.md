# SledState

The current state of the sled, as determined by Nexus.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.sled_state import SledState

# TODO update the JSON string below
json = "{}"
# create an instance of SledState from a JSON string
sled_state_instance = SledState.from_json(json)
# print the JSON string representation of the object
print(SledState.to_json())

# convert the object into a dict
sled_state_dict = sled_state_instance.to_dict()
# create an instance of SledState from a dict
sled_state_from_dict = SledState.from_dict(sled_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


