# ExternalIpResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExternalIp]**](ExternalIp.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.external_ip_results_page import ExternalIpResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIpResultsPage from a JSON string
external_ip_results_page_instance = ExternalIpResultsPage.from_json(json)
# print the JSON string representation of the object
print(ExternalIpResultsPage.to_json())

# convert the object into a dict
external_ip_results_page_dict = external_ip_results_page_instance.to_dict()
# create an instance of ExternalIpResultsPage from a dict
external_ip_results_page_from_dict = ExternalIpResultsPage.from_dict(external_ip_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


