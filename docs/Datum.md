# Datum

A `Datum` is a single sampled data point from a metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum** | [**MissingDatum**](MissingDatum.md) |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.datum import Datum

# TODO update the JSON string below
json = "{}"
# create an instance of Datum from a JSON string
datum_instance = Datum.from_json(json)
# print the JSON string representation of the object
print(Datum.to_json())

# convert the object into a dict
datum_dict = datum_instance.to_dict()
# create an instance of Datum from a dict
datum_from_dict = Datum.from_dict(datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


