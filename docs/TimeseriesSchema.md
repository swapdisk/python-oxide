# TimeseriesSchema

The schema for a timeseries.  This includes the name of the timeseries, as well as the datum type of its metric and the schema for each field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authz_scope** | [**AuthzScope**](AuthzScope.md) |  | 
**created** | **datetime** |  | 
**datum_type** | [**DatumType**](DatumType.md) |  | 
**description** | [**TimeseriesDescription**](TimeseriesDescription.md) |  | 
**field_schema** | [**List[FieldSchema]**](FieldSchema.md) |  | 
**timeseries_name** | **str** | Names are constructed by concatenating the target and metric names with &#39;:&#39;. Target and metric names must be lowercase alphanumeric characters with &#39;_&#39; separating words. | 
**units** | [**Units**](Units.md) |  | 
**version** | **int** |  | 

## Example

```python
from oxide.models.timeseries_schema import TimeseriesSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesSchema from a JSON string
timeseries_schema_instance = TimeseriesSchema.from_json(json)
# print the JSON string representation of the object
print(TimeseriesSchema.to_json())

# convert the object into a dict
timeseries_schema_dict = timeseries_schema_instance.to_dict()
# create an instance of TimeseriesSchema from a dict
timeseries_schema_from_dict = TimeseriesSchema.from_dict(timeseries_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


