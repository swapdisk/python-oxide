# ImportExportPolicy

Define policy relating to the import and export of prefixes from a BGP peer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | [**List[IpNet]**](IpNet.md) |  | 

## Example

```python
from oxide.models.import_export_policy import ImportExportPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ImportExportPolicy from a JSON string
import_export_policy_instance = ImportExportPolicy.from_json(json)
# print the JSON string representation of the object
print(ImportExportPolicy.to_json())

# convert the object into a dict
import_export_policy_dict = import_export_policy_instance.to_dict()
# create an instance of ImportExportPolicy from a dict
import_export_policy_from_dict = ImportExportPolicy.from_dict(import_export_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


