# LoopbackAddressResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LoopbackAddress]**](LoopbackAddress.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.loopback_address_results_page import LoopbackAddressResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of LoopbackAddressResultsPage from a JSON string
loopback_address_results_page_instance = LoopbackAddressResultsPage.from_json(json)
# print the JSON string representation of the object
print(LoopbackAddressResultsPage.to_json())

# convert the object into a dict
loopback_address_results_page_dict = loopback_address_results_page_instance.to_dict()
# create an instance of LoopbackAddressResultsPage from a dict
loopback_address_results_page_from_dict = LoopbackAddressResultsPage.from_dict(loopback_address_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


