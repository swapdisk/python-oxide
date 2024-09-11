# UserPasswordOneOf1

Invalidates any current password (disabling password authentication)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 

## Example

```python
from oxide.models.user_password_one_of1 import UserPasswordOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of UserPasswordOneOf1 from a JSON string
user_password_one_of1_instance = UserPasswordOneOf1.from_json(json)
# print the JSON string representation of the object
print(UserPasswordOneOf1.to_json())

# convert the object into a dict
user_password_one_of1_dict = user_password_one_of1_instance.to_dict()
# create an instance of UserPasswordOneOf1 from a dict
user_password_one_of1_from_dict = UserPasswordOneOf1.from_dict(user_password_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


