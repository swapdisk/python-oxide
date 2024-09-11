# OxqlQueryResult

The result of a successful OxQL query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | [**List[Table]**](Table.md) | Tables resulting from the query, each containing timeseries. | 

## Example

```python
from oxide.models.oxql_query_result import OxqlQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of OxqlQueryResult from a JSON string
oxql_query_result_instance = OxqlQueryResult.from_json(json)
# print the JSON string representation of the object
print(OxqlQueryResult.to_json())

# convert the object into a dict
oxql_query_result_dict = oxql_query_result_instance.to_dict()
# create an instance of OxqlQueryResult from a dict
oxql_query_result_from_dict = OxqlQueryResult.from_dict(oxql_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


