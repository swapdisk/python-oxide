# GroupResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Group]**](Group.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.group_results_page import GroupResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResultsPage from a JSON string
group_results_page_instance = GroupResultsPage.from_json(json)
# print the JSON string representation of the object
print(GroupResultsPage.to_json())

# convert the object into a dict
group_results_page_dict = group_results_page_instance.to_dict()
# create an instance of GroupResultsPage from a dict
group_results_page_from_dict = GroupResultsPage.from_dict(group_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


