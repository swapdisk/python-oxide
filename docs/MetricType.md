# MetricType

The type of the metric itself, indicating what its values represent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.metric_type import MetricType

# TODO update the JSON string below
json = "{}"
# create an instance of MetricType from a JSON string
metric_type_instance = MetricType.from_json(json)
# print the JSON string representation of the object
print(MetricType.to_json())

# convert the object into a dict
metric_type_dict = metric_type_instance.to_dict()
# create an instance of MetricType from a dict
metric_type_from_dict = MetricType.from_dict(metric_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


