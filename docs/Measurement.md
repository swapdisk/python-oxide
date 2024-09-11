# Measurement

A `Measurement` is a timestamped datum from a single metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum** | [**Datum**](Datum.md) |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from oxide.models.measurement import Measurement

# TODO update the JSON string below
json = "{}"
# create an instance of Measurement from a JSON string
measurement_instance = Measurement.from_json(json)
# print the JSON string representation of the object
print(Measurement.to_json())

# convert the object into a dict
measurement_dict = measurement_instance.to_dict()
# create an instance of Measurement from a dict
measurement_from_dict = Measurement.from_dict(measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


