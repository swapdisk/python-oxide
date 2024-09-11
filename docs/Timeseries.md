# Timeseries

A timeseries contains a timestamped set of values from one source.  This includes the typed key-value pairs that uniquely identify it, and the set of timestamps and data values from it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**Dict[str, FieldValue]**](FieldValue.md) |  | 
**points** | [**Points**](Points.md) |  | 

## Example

```python
from oxide.models.timeseries import Timeseries

# TODO update the JSON string below
json = "{}"
# create an instance of Timeseries from a JSON string
timeseries_instance = Timeseries.from_json(json)
# print the JSON string representation of the object
print(Timeseries.to_json())

# convert the object into a dict
timeseries_dict = timeseries_instance.to_dict()
# create an instance of Timeseries from a dict
timeseries_from_dict = Timeseries.from_dict(timeseries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


