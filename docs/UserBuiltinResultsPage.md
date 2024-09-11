# UserBuiltinResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserBuiltin]**](UserBuiltin.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.user_builtin_results_page import UserBuiltinResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of UserBuiltinResultsPage from a JSON string
user_builtin_results_page_instance = UserBuiltinResultsPage.from_json(json)
# print the JSON string representation of the object
print(UserBuiltinResultsPage.to_json())

# convert the object into a dict
user_builtin_results_page_dict = user_builtin_results_page_instance.to_dict()
# create an instance of UserBuiltinResultsPage from a dict
user_builtin_results_page_from_dict = UserBuiltinResultsPage.from_dict(user_builtin_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


