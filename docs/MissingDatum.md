# MissingDatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_type** | [**DatumType**](DatumType.md) |  | 
**start_time** | **datetime** |  | [optional] 

## Example

```python
from oxide.models.missing_datum import MissingDatum

# TODO update the JSON string below
json = "{}"
# create an instance of MissingDatum from a JSON string
missing_datum_instance = MissingDatum.from_json(json)
# print the JSON string representation of the object
print(MissingDatum.to_json())

# convert the object into a dict
missing_datum_dict = missing_datum_instance.to_dict()
# create an instance of MissingDatum from a dict
missing_datum_from_dict = MissingDatum.from_dict(missing_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


