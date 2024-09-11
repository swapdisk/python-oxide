# SwitchResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Switch]**](Switch.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.switch_results_page import SwitchResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchResultsPage from a JSON string
switch_results_page_instance = SwitchResultsPage.from_json(json)
# print the JSON string representation of the object
print(SwitchResultsPage.to_json())

# convert the object into a dict
switch_results_page_dict = switch_results_page_instance.to_dict()
# create an instance of SwitchResultsPage from a dict
switch_results_page_from_dict = SwitchResultsPage.from_dict(switch_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


