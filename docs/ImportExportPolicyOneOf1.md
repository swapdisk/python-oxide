# ImportExportPolicyOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | [**List[IpNet]**](IpNet.md) |  | 

## Example

```python
from oxide.models.import_export_policy_one_of1 import ImportExportPolicyOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ImportExportPolicyOneOf1 from a JSON string
import_export_policy_one_of1_instance = ImportExportPolicyOneOf1.from_json(json)
# print the JSON string representation of the object
print(ImportExportPolicyOneOf1.to_json())

# convert the object into a dict
import_export_policy_one_of1_dict = import_export_policy_one_of1_instance.to_dict()
# create an instance of ImportExportPolicyOneOf1 from a dict
import_export_policy_one_of1_from_dict = ImportExportPolicyOneOf1.from_dict(import_export_policy_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


