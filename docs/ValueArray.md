# ValueArray

List of data values for one timeseries.  Each element is an option, where `None` represents a missing sample.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**values** | [**List[Optional[Distributiondouble]]**](Distributiondouble.md) |  | 

## Example

```python
from oxide.models.value_array import ValueArray

# TODO update the JSON string below
json = "{}"
# create an instance of ValueArray from a JSON string
value_array_instance = ValueArray.from_json(json)
# print the JSON string representation of the object
print(ValueArray.to_json())

# convert the object into a dict
value_array_dict = value_array_instance.to_dict()
# create an instance of ValueArray from a dict
value_array_from_dict = ValueArray.from_dict(value_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


