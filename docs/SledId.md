# SledId

The unique ID of a sled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from oxide.models.sled_id import SledId

# TODO update the JSON string below
json = "{}"
# create an instance of SledId from a JSON string
sled_id_instance = SledId.from_json(json)
# print the JSON string representation of the object
print(SledId.to_json())

# convert the object into a dict
sled_id_dict = sled_id_instance.to_dict()
# create an instance of SledId from a dict
sled_id_from_dict = SledId.from_dict(sled_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


