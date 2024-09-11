# NameSortMode

Supported set of sort modes for scanning by name only  Currently, we only support scanning in ascending order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.name_sort_mode import NameSortMode

# TODO update the JSON string below
json = "{}"
# create an instance of NameSortMode from a JSON string
name_sort_mode_instance = NameSortMode.from_json(json)
# print the JSON string representation of the object
print(NameSortMode.to_json())

# convert the object into a dict
name_sort_mode_dict = name_sort_mode_instance.to_dict()
# create an instance of NameSortMode from a dict
name_sort_mode_from_dict = NameSortMode.from_dict(name_sort_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


