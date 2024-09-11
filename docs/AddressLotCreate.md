# AddressLotCreate

Parameters for creating an address lot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**List[AddressLotBlockCreate]**](AddressLotBlockCreate.md) | The blocks to add along with the new address lot. | 
**description** | **str** |  | 
**kind** | [**AddressLotKind**](AddressLotKind.md) | The kind of address lot to create. | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.address_lot_create import AddressLotCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLotCreate from a JSON string
address_lot_create_instance = AddressLotCreate.from_json(json)
# print the JSON string representation of the object
print(AddressLotCreate.to_json())

# convert the object into a dict
address_lot_create_dict = address_lot_create_instance.to_dict()
# create an instance of AddressLotCreate from a dict
address_lot_create_from_dict = AddressLotCreate.from_dict(address_lot_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


