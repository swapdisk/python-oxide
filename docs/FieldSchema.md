# FieldSchema

The name and type information for a field of a timeseries schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**field_type** | [**FieldType**](FieldType.md) |  | 
**name** | **str** |  | 
**source** | [**FieldSource**](FieldSource.md) |  | 

## Example

```python
from oxide.models.field_schema import FieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FieldSchema from a JSON string
field_schema_instance = FieldSchema.from_json(json)
# print the JSON string representation of the object
print(FieldSchema.to_json())

# convert the object into a dict
field_schema_dict = field_schema_instance.to_dict()
# create an instance of FieldSchema from a dict
field_schema_from_dict = FieldSchema.from_dict(field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


