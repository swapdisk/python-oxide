# Values

A single list of values, for one dimension of a timeseries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_type** | [**MetricType**](MetricType.md) | The type of this metric. | 
**values** | [**ValueArray**](ValueArray.md) | The data values. | 

## Example

```python
from oxide.models.values import Values

# TODO update the JSON string below
json = "{}"
# create an instance of Values from a JSON string
values_instance = Values.from_json(json)
# print the JSON string representation of the object
print(Values.to_json())

# convert the object into a dict
values_dict = values_instance.to_dict()
# create an instance of Values from a dict
values_from_dict = Values.from_dict(values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


