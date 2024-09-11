# SwitchInterfaceKindOneOf

Primary interfaces are associated with physical links. There is exactly one primary interface per physical link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from oxide.models.switch_interface_kind_one_of import SwitchInterfaceKindOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchInterfaceKindOneOf from a JSON string
switch_interface_kind_one_of_instance = SwitchInterfaceKindOneOf.from_json(json)
# print the JSON string representation of the object
print(SwitchInterfaceKindOneOf.to_json())

# convert the object into a dict
switch_interface_kind_one_of_dict = switch_interface_kind_one_of_instance.to_dict()
# create an instance of SwitchInterfaceKindOneOf from a dict
switch_interface_kind_one_of_from_dict = SwitchInterfaceKindOneOf.from_dict(switch_interface_kind_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


