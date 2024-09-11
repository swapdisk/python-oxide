# FieldValue

The `FieldValue` contains the value of a target or metric field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **bool** |  | 

## Example

```python
from oxide.models.field_value import FieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of FieldValue from a JSON string
field_value_instance = FieldValue.from_json(json)
# print the JSON string representation of the object
print(FieldValue.to_json())

# convert the object into a dict
field_value_dict = field_value_instance.to_dict()
# create an instance of FieldValue from a dict
field_value_from_dict = FieldValue.from_dict(field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


