# SiloRoleRoleAssignment

Describes the assignment of a particular role on a particular resource to a particular identity (user, group, etc.)  The resource is not part of this structure.  Rather, `RoleAssignment`s are put into a `Policy` and that Policy is applied to a particular resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** |  | 
**identity_type** | [**IdentityType**](IdentityType.md) |  | 
**role_name** | [**SiloRole**](SiloRole.md) |  | 

## Example

```python
from oxide.models.silo_role_role_assignment import SiloRoleRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of SiloRoleRoleAssignment from a JSON string
silo_role_role_assignment_instance = SiloRoleRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(SiloRoleRoleAssignment.to_json())

# convert the object into a dict
silo_role_role_assignment_dict = silo_role_role_assignment_instance.to_dict()
# create an instance of SiloRoleRoleAssignment from a dict
silo_role_role_assignment_from_dict = SiloRoleRoleAssignment.from_dict(silo_role_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


