# SshKeyCreate

Create-time parameters for an `SshKey`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**public_key** | **str** | SSH public key, e.g., &#x60;\&quot;ssh-ed25519 AAAAC3NzaC...\&quot;&#x60; | 

## Example

```python
from oxide.models.ssh_key_create import SshKeyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyCreate from a JSON string
ssh_key_create_instance = SshKeyCreate.from_json(json)
# print the JSON string representation of the object
print(SshKeyCreate.to_json())

# convert the object into a dict
ssh_key_create_dict = ssh_key_create_instance.to_dict()
# create an instance of SshKeyCreate from a dict
ssh_key_create_from_dict = SshKeyCreate.from_dict(ssh_key_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


