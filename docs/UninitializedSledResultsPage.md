# UninitializedSledResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UninitializedSled]**](UninitializedSled.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.uninitialized_sled_results_page import UninitializedSledResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of UninitializedSledResultsPage from a JSON string
uninitialized_sled_results_page_instance = UninitializedSledResultsPage.from_json(json)
# print the JSON string representation of the object
print(UninitializedSledResultsPage.to_json())

# convert the object into a dict
uninitialized_sled_results_page_dict = uninitialized_sled_results_page_instance.to_dict()
# create an instance of UninitializedSledResultsPage from a dict
uninitialized_sled_results_page_from_dict = UninitializedSledResultsPage.from_dict(uninitialized_sled_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


