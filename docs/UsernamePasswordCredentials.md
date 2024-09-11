# UsernamePasswordCredentials

Credentials for local user login

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Passwords may be subject to additional constraints. | 
**username** | **str** | Usernames must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Usernames cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.username_password_credentials import UsernamePasswordCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of UsernamePasswordCredentials from a JSON string
username_password_credentials_instance = UsernamePasswordCredentials.from_json(json)
# print the JSON string representation of the object
print(UsernamePasswordCredentials.to_json())

# convert the object into a dict
username_password_credentials_dict = username_password_credentials_instance.to_dict()
# create an instance of UsernamePasswordCredentials from a dict
username_password_credentials_from_dict = UsernamePasswordCredentials.from_dict(username_password_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


