# ValueArrayOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**values** | **List[Optional[int]]** |  | 

## Example

```python
from oxide.models.value_array_one_of import ValueArrayOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ValueArrayOneOf from a JSON string
value_array_one_of_instance = ValueArrayOneOf.from_json(json)
# print the JSON string representation of the object
print(ValueArrayOneOf.to_json())

# convert the object into a dict
value_array_one_of_dict = value_array_one_of_instance.to_dict()
# create an instance of ValueArrayOneOf from a dict
value_array_one_of_from_dict = ValueArrayOneOf.from_dict(value_array_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


