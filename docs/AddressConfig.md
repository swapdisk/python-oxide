# AddressConfig

A set of addresses associated with a port configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[Address]**](Address.md) | The set of addresses assigned to the port configuration. | 

## Example

```python
from oxide.models.address_config import AddressConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AddressConfig from a JSON string
address_config_instance = AddressConfig.from_json(json)
# print the JSON string representation of the object
print(AddressConfig.to_json())

# convert the object into a dict
address_config_dict = address_config_instance.to_dict()
# create an instance of AddressConfig from a dict
address_config_from_dict = AddressConfig.from_dict(address_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


