# ProjectRolePolicy

Policy for a particular resource  Note that the Policy only describes access granted explicitly for this resource.  The policies of parent resources can also cause a user to have access to this resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_assignments** | [**List[ProjectRoleRoleAssignment]**](ProjectRoleRoleAssignment.md) | Roles directly assigned on this resource | 

## Example

```python
from oxide.models.project_role_policy import ProjectRolePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRolePolicy from a JSON string
project_role_policy_instance = ProjectRolePolicy.from_json(json)
# print the JSON string representation of the object
print(ProjectRolePolicy.to_json())

# convert the object into a dict
project_role_policy_dict = project_role_policy_instance.to_dict()
# create an instance of ProjectRolePolicy from a dict
project_role_policy_from_dict = ProjectRolePolicy.from_dict(project_role_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


