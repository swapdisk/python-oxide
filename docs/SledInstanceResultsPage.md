# SledInstanceResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SledInstance]**](SledInstance.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.sled_instance_results_page import SledInstanceResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SledInstanceResultsPage from a JSON string
sled_instance_results_page_instance = SledInstanceResultsPage.from_json(json)
# print the JSON string representation of the object
print(SledInstanceResultsPage.to_json())

# convert the object into a dict
sled_instance_results_page_dict = sled_instance_results_page_instance.to_dict()
# create an instance of SledInstanceResultsPage from a dict
sled_instance_results_page_from_dict = SledInstanceResultsPage.from_dict(sled_instance_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


