# UserBuiltin

View of a Built-in User  Built-in users are identities internal to the system, used when the control plane performs actions autonomously

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.user_builtin import UserBuiltin

# TODO update the JSON string below
json = "{}"
# create an instance of UserBuiltin from a JSON string
user_builtin_instance = UserBuiltin.from_json(json)
# print the JSON string representation of the object
print(UserBuiltin.to_json())

# convert the object into a dict
user_builtin_dict = user_builtin_instance.to_dict()
# create an instance of UserBuiltin from a dict
user_builtin_from_dict = UserBuiltin.from_dict(user_builtin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


