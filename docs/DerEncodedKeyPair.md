# DerEncodedKeyPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** | request signing private key (base64 encoded der file) | 
**public_cert** | **str** | request signing public certificate (base64 encoded der file) | 

## Example

```python
from oxide.models.der_encoded_key_pair import DerEncodedKeyPair

# TODO update the JSON string below
json = "{}"
# create an instance of DerEncodedKeyPair from a JSON string
der_encoded_key_pair_instance = DerEncodedKeyPair.from_json(json)
# print the JSON string representation of the object
print(DerEncodedKeyPair.to_json())

# convert the object into a dict
der_encoded_key_pair_dict = der_encoded_key_pair_instance.to_dict()
# create an instance of DerEncodedKeyPair from a dict
der_encoded_key_pair_from_dict = DerEncodedKeyPair.from_dict(der_encoded_key_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


