# UserCreate

Create-time parameters for a `User`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | username used to log in | 
**password** | [**UserPassword**](UserPassword.md) | how to set the user&#39;s login password | 

## Example

```python
from oxide.models.user_create import UserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreate from a JSON string
user_create_instance = UserCreate.from_json(json)
# print the JSON string representation of the object
print(UserCreate.to_json())

# convert the object into a dict
user_create_dict = user_create_instance.to_dict()
# create an instance of UserCreate from a dict
user_create_from_dict = UserCreate.from_dict(user_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


