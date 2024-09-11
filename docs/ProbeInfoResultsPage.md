# ProbeInfoResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProbeInfo]**](ProbeInfo.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.probe_info_results_page import ProbeInfoResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeInfoResultsPage from a JSON string
probe_info_results_page_instance = ProbeInfoResultsPage.from_json(json)
# print the JSON string representation of the object
print(ProbeInfoResultsPage.to_json())

# convert the object into a dict
probe_info_results_page_dict = probe_info_results_page_instance.to_dict()
# create an instance of ProbeInfoResultsPage from a dict
probe_info_results_page_from_dict = ProbeInfoResultsPage.from_dict(probe_info_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


