# UserPasswordOneOf

Sets the user's password to the provided value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**value** | **str** | Passwords may be subject to additional constraints. | 

## Example

```python
from oxide.models.user_password_one_of import UserPasswordOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of UserPasswordOneOf from a JSON string
user_password_one_of_instance = UserPasswordOneOf.from_json(json)
# print the JSON string representation of the object
print(UserPasswordOneOf.to_json())

# convert the object into a dict
user_password_one_of_dict = user_password_one_of_instance.to_dict()
# create an instance of UserPasswordOneOf from a dict
user_password_one_of_from_dict = UserPasswordOneOf.from_dict(user_password_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


