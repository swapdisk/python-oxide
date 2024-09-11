# SiloResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Silo]**](Silo.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.silo_results_page import SiloResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SiloResultsPage from a JSON string
silo_results_page_instance = SiloResultsPage.from_json(json)
# print the JSON string representation of the object
print(SiloResultsPage.to_json())

# convert the object into a dict
silo_results_page_dict = silo_results_page_instance.to_dict()
# create an instance of SiloResultsPage from a dict
silo_results_page_from_dict = SiloResultsPage.from_dict(silo_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


