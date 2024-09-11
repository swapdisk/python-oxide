# SiloRolePolicy

Policy for a particular resource  Note that the Policy only describes access granted explicitly for this resource.  The policies of parent resources can also cause a user to have access to this resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_assignments** | [**List[SiloRoleRoleAssignment]**](SiloRoleRoleAssignment.md) | Roles directly assigned on this resource | 

## Example

```python
from oxide.models.silo_role_policy import SiloRolePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SiloRolePolicy from a JSON string
silo_role_policy_instance = SiloRolePolicy.from_json(json)
# print the JSON string representation of the object
print(SiloRolePolicy.to_json())

# convert the object into a dict
silo_role_policy_dict = silo_role_policy_instance.to_dict()
# create an instance of SiloRolePolicy from a dict
silo_role_policy_from_dict = SiloRolePolicy.from_dict(silo_role_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


