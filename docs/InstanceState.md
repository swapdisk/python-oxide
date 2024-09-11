# InstanceState

Running state of an Instance (primarily: booted or stopped)  This typically reflects whether it's starting, running, stopping, or stopped, but also includes states related to the Instance's lifecycle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.instance_state import InstanceState

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceState from a JSON string
instance_state_instance = InstanceState.from_json(json)
# print the JSON string representation of the object
print(InstanceState.to_json())

# convert the object into a dict
instance_state_dict = instance_state_instance.to_dict()
# create an instance of InstanceState from a dict
instance_state_from_dict = InstanceState.from_dict(instance_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


