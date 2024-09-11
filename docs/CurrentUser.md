# CurrentUser

Info about the current user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human-readable name that can identify the user | 
**id** | **str** |  | 
**silo_id** | **str** | Uuid of the silo to which this user belongs | 
**silo_name** | **str** | Name of the silo to which this user belongs. | 

## Example

```python
from oxide.models.current_user import CurrentUser

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentUser from a JSON string
current_user_instance = CurrentUser.from_json(json)
# print the JSON string representation of the object
print(CurrentUser.to_json())

# convert the object into a dict
current_user_dict = current_user_instance.to_dict()
# create an instance of CurrentUser from a dict
current_user_from_dict = CurrentUser.from_dict(current_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


