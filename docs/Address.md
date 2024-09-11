# Address

An address tied to an address lot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**IpNet**](IpNet.md) | The address and prefix length of this address. | 
**address_lot** | [**NameOrId**](NameOrId.md) | The address lot this address is drawn from. | 
**vlan_id** | **int** | Optional VLAN ID for this address | [optional] 

## Example

```python
from oxide.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


