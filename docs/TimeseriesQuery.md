# TimeseriesQuery

A timeseries query string, written in the Oximeter query language.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | A timeseries query string, written in the Oximeter query language. | 

## Example

```python
from oxide.models.timeseries_query import TimeseriesQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesQuery from a JSON string
timeseries_query_instance = TimeseriesQuery.from_json(json)
# print the JSON string representation of the object
print(TimeseriesQuery.to_json())

# convert the object into a dict
timeseries_query_dict = timeseries_query_instance.to_dict()
# create an instance of TimeseriesQuery from a dict
timeseries_query_from_dict = TimeseriesQuery.from_dict(timeseries_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


