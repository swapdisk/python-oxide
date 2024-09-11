# Cumulativefloat

A cumulative or counter data type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | 
**value** | **float** |  | 

## Example

```python
from oxide.models.cumulativefloat import Cumulativefloat

# TODO update the JSON string below
json = "{}"
# create an instance of Cumulativefloat from a JSON string
cumulativefloat_instance = Cumulativefloat.from_json(json)
# print the JSON string representation of the object
print(Cumulativefloat.to_json())

# convert the object into a dict
cumulativefloat_dict = cumulativefloat_instance.to_dict()
# create an instance of Cumulativefloat from a dict
cumulativefloat_from_dict = Cumulativefloat.from_dict(cumulativefloat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


