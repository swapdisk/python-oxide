# BgpConfigResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BgpConfig]**](BgpConfig.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.bgp_config_results_page import BgpConfigResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of BgpConfigResultsPage from a JSON string
bgp_config_results_page_instance = BgpConfigResultsPage.from_json(json)
# print the JSON string representation of the object
print(BgpConfigResultsPage.to_json())

# convert the object into a dict
bgp_config_results_page_dict = bgp_config_results_page_instance.to_dict()
# create an instance of BgpConfigResultsPage from a dict
bgp_config_results_page_from_dict = BgpConfigResultsPage.from_dict(bgp_config_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


