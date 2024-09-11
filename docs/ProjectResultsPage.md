# ProjectResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Project]**](Project.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.project_results_page import ProjectResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResultsPage from a JSON string
project_results_page_instance = ProjectResultsPage.from_json(json)
# print the JSON string representation of the object
print(ProjectResultsPage.to_json())

# convert the object into a dict
project_results_page_dict = project_results_page_instance.to_dict()
# create an instance of ProjectResultsPage from a dict
project_results_page_from_dict = ProjectResultsPage.from_dict(project_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


