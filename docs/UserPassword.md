# UserPassword

Parameters for setting a user's password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**value** | **str** | Passwords may be subject to additional constraints. | 

## Example

```python
from oxide.models.user_password import UserPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UserPassword from a JSON string
user_password_instance = UserPassword.from_json(json)
# print the JSON string representation of the object
print(UserPassword.to_json())

# convert the object into a dict
user_password_dict = user_password_instance.to_dict()
# create an instance of UserPassword from a dict
user_password_from_dict = UserPassword.from_dict(user_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


