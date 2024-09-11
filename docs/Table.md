# Table

A table represents one or more timeseries with the same schema.  A table is the result of an OxQL query. It contains a name, usually the name of the timeseries schema from which the data is derived, and any number of timeseries, which contain the actual data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**timeseries** | [**Dict[str, Timeseries]**](Timeseries.md) |  | 

## Example

```python
from oxide.models.table import Table

# TODO update the JSON string below
json = "{}"
# create an instance of Table from a JSON string
table_instance = Table.from_json(json)
# print the JSON string representation of the object
print(Table.to_json())

# convert the object into a dict
table_dict = table_instance.to_dict()
# create an instance of Table from a dict
table_from_dict = Table.from_dict(table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


