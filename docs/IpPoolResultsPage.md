# IpPoolResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IpPool]**](IpPool.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.ip_pool_results_page import IpPoolResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolResultsPage from a JSON string
ip_pool_results_page_instance = IpPoolResultsPage.from_json(json)
# print the JSON string representation of the object
print(IpPoolResultsPage.to_json())

# convert the object into a dict
ip_pool_results_page_dict = ip_pool_results_page_instance.to_dict()
# create an instance of IpPoolResultsPage from a dict
ip_pool_results_page_from_dict = IpPoolResultsPage.from_dict(ip_pool_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


