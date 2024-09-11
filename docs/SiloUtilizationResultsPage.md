# SiloUtilizationResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SiloUtilization]**](SiloUtilization.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.silo_utilization_results_page import SiloUtilizationResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SiloUtilizationResultsPage from a JSON string
silo_utilization_results_page_instance = SiloUtilizationResultsPage.from_json(json)
# print the JSON string representation of the object
print(SiloUtilizationResultsPage.to_json())

# convert the object into a dict
silo_utilization_results_page_dict = silo_utilization_results_page_instance.to_dict()
# create an instance of SiloUtilizationResultsPage from a dict
silo_utilization_results_page_from_dict = SiloUtilizationResultsPage.from_dict(silo_utilization_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


