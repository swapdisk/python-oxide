# InstanceResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Instance]**](Instance.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.instance_results_page import InstanceResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceResultsPage from a JSON string
instance_results_page_instance = InstanceResultsPage.from_json(json)
# print the JSON string representation of the object
print(InstanceResultsPage.to_json())

# convert the object into a dict
instance_results_page_dict = instance_results_page_instance.to_dict()
# create an instance of InstanceResultsPage from a dict
instance_results_page_from_dict = InstanceResultsPage.from_dict(instance_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


