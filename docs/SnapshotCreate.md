# SnapshotCreate

Create-time parameters for a `Snapshot`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**disk** | [**NameOrId**](NameOrId.md) | The disk to be snapshotted | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.snapshot_create import SnapshotCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCreate from a JSON string
snapshot_create_instance = SnapshotCreate.from_json(json)
# print the JSON string representation of the object
print(SnapshotCreate.to_json())

# convert the object into a dict
snapshot_create_dict = snapshot_create_instance.to_dict()
# create an instance of SnapshotCreate from a dict
snapshot_create_from_dict = SnapshotCreate.from_dict(snapshot_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


