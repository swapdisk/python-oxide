# UninitializedSled

A sled that has not been added to an initialized rack yet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseboard** | [**Baseboard**](Baseboard.md) |  | 
**cubby** | **int** |  | 
**rack_id** | **str** |  | 

## Example

```python
from oxide.models.uninitialized_sled import UninitializedSled

# TODO update the JSON string below
json = "{}"
# create an instance of UninitializedSled from a JSON string
uninitialized_sled_instance = UninitializedSled.from_json(json)
# print the JSON string representation of the object
print(UninitializedSled.to_json())

# convert the object into a dict
uninitialized_sled_dict = uninitialized_sled_instance.to_dict()
# create an instance of UninitializedSled from a dict
uninitialized_sled_from_dict = UninitializedSled.from_dict(uninitialized_sled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


