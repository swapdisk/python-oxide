# IdSortMode

Supported set of sort modes for scanning by id only.  Currently, we only support scanning in ascending order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.id_sort_mode import IdSortMode

# TODO update the JSON string below
json = "{}"
# create an instance of IdSortMode from a JSON string
id_sort_mode_instance = IdSortMode.from_json(json)
# print the JSON string representation of the object
print(IdSortMode.to_json())

# convert the object into a dict
id_sort_mode_dict = id_sort_mode_instance.to_dict()
# create an instance of IdSortMode from a dict
id_sort_mode_from_dict = IdSortMode.from_dict(id_sort_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


