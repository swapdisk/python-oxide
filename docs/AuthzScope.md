# AuthzScope

Authorization scope for a timeseries.  This describes the level at which a user must be authorized to read data from a timeseries. For example, fleet-scoping means the data is only visible to an operator or fleet reader. Project-scoped, on the other hand, indicates that a user will see data limited to the projects on which they have read permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.authz_scope import AuthzScope

# TODO update the JSON string below
json = "{}"
# create an instance of AuthzScope from a JSON string
authz_scope_instance = AuthzScope.from_json(json)
# print the JSON string representation of the object
print(AuthzScope.to_json())

# convert the object into a dict
authz_scope_dict = authz_scope_instance.to_dict()
# create an instance of AuthzScope from a dict
authz_scope_from_dict = AuthzScope.from_dict(authz_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


