# AddressLot

Represents an address lot object, containing the id of the lot that can be used in other API calls.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**kind** | [**AddressLotKind**](AddressLotKind.md) | Desired use of &#x60;AddressLot&#x60; | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.address_lot import AddressLot

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLot from a JSON string
address_lot_instance = AddressLot.from_json(json)
# print the JSON string representation of the object
print(AddressLot.to_json())

# convert the object into a dict
address_lot_dict = address_lot_instance.to_dict()
# create an instance of AddressLot from a dict
address_lot_from_dict = AddressLot.from_dict(address_lot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


