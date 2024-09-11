# BfdSessionDisable

Information needed to disable a BFD session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote** | **str** | Address of the remote peer to disable a BFD session for. | 
**switch** | **str** | The switch to enable this session on. Must be &#x60;switch0&#x60; or &#x60;switch1&#x60;. | 

## Example

```python
from oxide.models.bfd_session_disable import BfdSessionDisable

# TODO update the JSON string below
json = "{}"
# create an instance of BfdSessionDisable from a JSON string
bfd_session_disable_instance = BfdSessionDisable.from_json(json)
# print the JSON string representation of the object
print(BfdSessionDisable.to_json())

# convert the object into a dict
bfd_session_disable_dict = bfd_session_disable_instance.to_dict()
# create an instance of BfdSessionDisable from a dict
bfd_session_disable_from_dict = BfdSessionDisable.from_dict(bfd_session_disable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


