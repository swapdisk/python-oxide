# DeviceAuthVerify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_code** | **str** |  | 

## Example

```python
from oxide.models.device_auth_verify import DeviceAuthVerify

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAuthVerify from a JSON string
device_auth_verify_instance = DeviceAuthVerify.from_json(json)
# print the JSON string representation of the object
print(DeviceAuthVerify.to_json())

# convert the object into a dict
device_auth_verify_dict = device_auth_verify_instance.to_dict()
# create an instance of DeviceAuthVerify from a dict
device_auth_verify_from_dict = DeviceAuthVerify.from_dict(device_auth_verify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


