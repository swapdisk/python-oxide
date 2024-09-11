# MeasurementResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Measurement]**](Measurement.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.measurement_results_page import MeasurementResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementResultsPage from a JSON string
measurement_results_page_instance = MeasurementResultsPage.from_json(json)
# print the JSON string representation of the object
print(MeasurementResultsPage.to_json())

# convert the object into a dict
measurement_results_page_dict = measurement_results_page_instance.to_dict()
# create an instance of MeasurementResultsPage from a dict
measurement_results_page_from_dict = MeasurementResultsPage.from_dict(measurement_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


