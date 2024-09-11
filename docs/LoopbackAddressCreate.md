# LoopbackAddressCreate

Parameters for creating a loopback address on a particular rack switch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address to create. | 
**address_lot** | [**NameOrId**](NameOrId.md) | The name or id of the address lot this loopback address will pull an address from. | 
**anycast** | **bool** | Address is an anycast address. This allows the address to be assigned to multiple locations simultaneously. | 
**mask** | **int** | The subnet mask to use for the address. | 
**rack_id** | **str** | The containing the switch this loopback address will be configured on. | 
**switch_location** | **str** | The location of the switch within the rack this loopback address will be configured on. | 

## Example

```python
from oxide.models.loopback_address_create import LoopbackAddressCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LoopbackAddressCreate from a JSON string
loopback_address_create_instance = LoopbackAddressCreate.from_json(json)
# print the JSON string representation of the object
print(LoopbackAddressCreate.to_json())

# convert the object into a dict
loopback_address_create_dict = loopback_address_create_instance.to_dict()
# create an instance of LoopbackAddressCreate from a dict
loopback_address_create_from_dict = LoopbackAddressCreate.from_dict(loopback_address_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


