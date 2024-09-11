# ProjectRoleRoleAssignment

Describes the assignment of a particular role on a particular resource to a particular identity (user, group, etc.)  The resource is not part of this structure.  Rather, `RoleAssignment`s are put into a `Policy` and that Policy is applied to a particular resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** |  | 
**identity_type** | [**IdentityType**](IdentityType.md) |  | 
**role_name** | [**ProjectRole**](ProjectRole.md) |  | 

## Example

```python
from oxide.models.project_role_role_assignment import ProjectRoleRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRoleRoleAssignment from a JSON string
project_role_role_assignment_instance = ProjectRoleRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(ProjectRoleRoleAssignment.to_json())

# convert the object into a dict
project_role_role_assignment_dict = project_role_role_assignment_instance.to_dict()
# create an instance of ProjectRoleRoleAssignment from a dict
project_role_role_assignment_from_dict = ProjectRoleRoleAssignment.from_dict(project_role_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


