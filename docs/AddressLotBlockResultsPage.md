# AddressLotBlockResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AddressLotBlock]**](AddressLotBlock.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.address_lot_block_results_page import AddressLotBlockResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLotBlockResultsPage from a JSON string
address_lot_block_results_page_instance = AddressLotBlockResultsPage.from_json(json)
# print the JSON string representation of the object
print(AddressLotBlockResultsPage.to_json())

# convert the object into a dict
address_lot_block_results_page_dict = address_lot_block_results_page_instance.to_dict()
# create an instance of AddressLotBlockResultsPage from a dict
address_lot_block_results_page_from_dict = AddressLotBlockResultsPage.from_dict(address_lot_block_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


