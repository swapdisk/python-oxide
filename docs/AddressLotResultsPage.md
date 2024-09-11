# AddressLotResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AddressLot]**](AddressLot.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.address_lot_results_page import AddressLotResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLotResultsPage from a JSON string
address_lot_results_page_instance = AddressLotResultsPage.from_json(json)
# print the JSON string representation of the object
print(AddressLotResultsPage.to_json())

# convert the object into a dict
address_lot_results_page_dict = address_lot_results_page_instance.to_dict()
# create an instance of AddressLotResultsPage from a dict
address_lot_results_page_from_dict = AddressLotResultsPage.from_dict(address_lot_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


