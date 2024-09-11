# VpcResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Vpc]**](Vpc.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.vpc_results_page import VpcResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of VpcResultsPage from a JSON string
vpc_results_page_instance = VpcResultsPage.from_json(json)
# print the JSON string representation of the object
print(VpcResultsPage.to_json())

# convert the object into a dict
vpc_results_page_dict = vpc_results_page_instance.to_dict()
# create an instance of VpcResultsPage from a dict
vpc_results_page_from_dict = VpcResultsPage.from_dict(vpc_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


