# FloatingIpResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FloatingIp]**](FloatingIp.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.floating_ip_results_page import FloatingIpResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIpResultsPage from a JSON string
floating_ip_results_page_instance = FloatingIpResultsPage.from_json(json)
# print the JSON string representation of the object
print(FloatingIpResultsPage.to_json())

# convert the object into a dict
floating_ip_results_page_dict = floating_ip_results_page_instance.to_dict()
# create an instance of FloatingIpResultsPage from a dict
floating_ip_results_page_from_dict = FloatingIpResultsPage.from_dict(floating_ip_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


