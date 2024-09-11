# UserResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[User]**](User.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.user_results_page import UserResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of UserResultsPage from a JSON string
user_results_page_instance = UserResultsPage.from_json(json)
# print the JSON string representation of the object
print(UserResultsPage.to_json())

# convert the object into a dict
user_results_page_dict = user_results_page_instance.to_dict()
# create an instance of UserResultsPage from a dict
user_results_page_from_dict = UserResultsPage.from_dict(user_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


