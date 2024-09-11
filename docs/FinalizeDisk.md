# FinalizeDisk

Parameters for finalizing a disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_name** | **str** | If specified a snapshot of the disk will be created with the given name during finalization. If not specified, a snapshot for the disk will _not_ be created. A snapshot can be manually created once the disk transitions into the &#x60;Detached&#x60; state. | [optional] 

## Example

```python
from oxide.models.finalize_disk import FinalizeDisk

# TODO update the JSON string below
json = "{}"
# create an instance of FinalizeDisk from a JSON string
finalize_disk_instance = FinalizeDisk.from_json(json)
# print the JSON string representation of the object
print(FinalizeDisk.to_json())

# convert the object into a dict
finalize_disk_dict = finalize_disk_instance.to_dict()
# create an instance of FinalizeDisk from a dict
finalize_disk_from_dict = FinalizeDisk.from_dict(finalize_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


