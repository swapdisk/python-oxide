# UninitializedSledId

The unique hardware ID for a sled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part** | **str** |  | 
**serial** | **str** |  | 

## Example

```python
from oxide.models.uninitialized_sled_id import UninitializedSledId

# TODO update the JSON string below
json = "{}"
# create an instance of UninitializedSledId from a JSON string
uninitialized_sled_id_instance = UninitializedSledId.from_json(json)
# print the JSON string representation of the object
print(UninitializedSledId.to_json())

# convert the object into a dict
uninitialized_sled_id_dict = uninitialized_sled_id_instance.to_dict()
# create an instance of UninitializedSledId from a dict
uninitialized_sled_id_from_dict = UninitializedSledId.from_dict(uninitialized_sled_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


