# SiloIpPoolResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SiloIpPool]**](SiloIpPool.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.silo_ip_pool_results_page import SiloIpPoolResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SiloIpPoolResultsPage from a JSON string
silo_ip_pool_results_page_instance = SiloIpPoolResultsPage.from_json(json)
# print the JSON string representation of the object
print(SiloIpPoolResultsPage.to_json())

# convert the object into a dict
silo_ip_pool_results_page_dict = silo_ip_pool_results_page_instance.to_dict()
# create an instance of SiloIpPoolResultsPage from a dict
silo_ip_pool_results_page_from_dict = SiloIpPoolResultsPage.from_dict(silo_ip_pool_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


