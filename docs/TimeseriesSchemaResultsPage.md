# TimeseriesSchemaResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TimeseriesSchema]**](TimeseriesSchema.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.timeseries_schema_results_page import TimeseriesSchemaResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesSchemaResultsPage from a JSON string
timeseries_schema_results_page_instance = TimeseriesSchemaResultsPage.from_json(json)
# print the JSON string representation of the object
print(TimeseriesSchemaResultsPage.to_json())

# convert the object into a dict
timeseries_schema_results_page_dict = timeseries_schema_results_page_instance.to_dict()
# create an instance of TimeseriesSchemaResultsPage from a dict
timeseries_schema_results_page_from_dict = TimeseriesSchemaResultsPage.from_dict(timeseries_schema_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


