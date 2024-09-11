# LoopbackAddress

A loopback address is an address that is assigned to a rack switch but is not associated with any particular port.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**IpNet**](IpNet.md) | The loopback IP address and prefix length. | 
**address_lot_block_id** | **str** | The address lot block this address came from. | 
**id** | **str** | The id of the loopback address. | 
**rack_id** | **str** | The id of the rack where this loopback address is assigned. | 
**switch_location** | **str** | Switch location where this loopback address is assigned. | 

## Example

```python
from oxide.models.loopback_address import LoopbackAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LoopbackAddress from a JSON string
loopback_address_instance = LoopbackAddress.from_json(json)
# print the JSON string representation of the object
print(LoopbackAddress.to_json())

# convert the object into a dict
loopback_address_dict = loopback_address_instance.to_dict()
# create an instance of LoopbackAddress from a dict
loopback_address_from_dict = LoopbackAddress.from_dict(loopback_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


