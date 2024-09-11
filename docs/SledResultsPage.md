# SledResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Sled]**](Sled.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.sled_results_page import SledResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SledResultsPage from a JSON string
sled_results_page_instance = SledResultsPage.from_json(json)
# print the JSON string representation of the object
print(SledResultsPage.to_json())

# convert the object into a dict
sled_results_page_dict = sled_results_page_instance.to_dict()
# create an instance of SledResultsPage from a dict
sled_results_page_from_dict = SledResultsPage.from_dict(sled_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


