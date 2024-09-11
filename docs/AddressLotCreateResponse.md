# AddressLotCreateResponse

An address lot and associated blocks resulting from creating an address lot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**List[AddressLotBlock]**](AddressLotBlock.md) | The address lot blocks that were created. | 
**lot** | [**AddressLot**](AddressLot.md) | The address lot that was created. | 

## Example

```python
from oxide.models.address_lot_create_response import AddressLotCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLotCreateResponse from a JSON string
address_lot_create_response_instance = AddressLotCreateResponse.from_json(json)
# print the JSON string representation of the object
print(AddressLotCreateResponse.to_json())

# convert the object into a dict
address_lot_create_response_dict = address_lot_create_response_instance.to_dict()
# create an instance of AddressLotCreateResponse from a dict
address_lot_create_response_from_dict = AddressLotCreateResponse.from_dict(address_lot_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


