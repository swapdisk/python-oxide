# FleetRolePolicy

Policy for a particular resource  Note that the Policy only describes access granted explicitly for this resource.  The policies of parent resources can also cause a user to have access to this resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_assignments** | [**List[FleetRoleRoleAssignment]**](FleetRoleRoleAssignment.md) | Roles directly assigned on this resource | 

## Example

```python
from oxide.models.fleet_role_policy import FleetRolePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of FleetRolePolicy from a JSON string
fleet_role_policy_instance = FleetRolePolicy.from_json(json)
# print the JSON string representation of the object
print(FleetRolePolicy.to_json())

# convert the object into a dict
fleet_role_policy_dict = fleet_role_policy_instance.to_dict()
# create an instance of FleetRolePolicy from a dict
fleet_role_policy_from_dict = FleetRolePolicy.from_dict(fleet_role_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


