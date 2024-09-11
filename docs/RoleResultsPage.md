# RoleResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Role]**](Role.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.role_results_page import RoleResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResultsPage from a JSON string
role_results_page_instance = RoleResultsPage.from_json(json)
# print the JSON string representation of the object
print(RoleResultsPage.to_json())

# convert the object into a dict
role_results_page_dict = role_results_page_instance.to_dict()
# create an instance of RoleResultsPage from a dict
role_results_page_from_dict = RoleResultsPage.from_dict(role_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


