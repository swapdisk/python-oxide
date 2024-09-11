# AddressLotBlockCreate

Parameters for creating an address lot block. Fist and last addresses are inclusive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_address** | **str** | The first address in the lot (inclusive). | 
**last_address** | **str** | The last address in the lot (inclusive). | 

## Example

```python
from oxide.models.address_lot_block_create import AddressLotBlockCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLotBlockCreate from a JSON string
address_lot_block_create_instance = AddressLotBlockCreate.from_json(json)
# print the JSON string representation of the object
print(AddressLotBlockCreate.to_json())

# convert the object into a dict
address_lot_block_create_dict = address_lot_block_create_instance.to_dict()
# create an instance of AddressLotBlockCreate from a dict
address_lot_block_create_from_dict = AddressLotBlockCreate.from_dict(address_lot_block_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


