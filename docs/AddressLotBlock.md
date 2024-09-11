# AddressLotBlock

An address lot block is a part of an address lot and contains a range of addresses. The range is inclusive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_address** | **str** | The first address of the block (inclusive). | 
**id** | **str** | The id of the address lot block. | 
**last_address** | **str** | The last address of the block (inclusive). | 

## Example

```python
from oxide.models.address_lot_block import AddressLotBlock

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLotBlock from a JSON string
address_lot_block_instance = AddressLotBlock.from_json(json)
# print the JSON string representation of the object
print(AddressLotBlock.to_json())

# convert the object into a dict
address_lot_block_dict = address_lot_block_instance.to_dict()
# create an instance of AddressLotBlock from a dict
address_lot_block_from_dict = AddressLotBlock.from_dict(address_lot_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


