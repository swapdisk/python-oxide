# VpcRouterResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VpcRouter]**](VpcRouter.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.vpc_router_results_page import VpcRouterResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of VpcRouterResultsPage from a JSON string
vpc_router_results_page_instance = VpcRouterResultsPage.from_json(json)
# print the JSON string representation of the object
print(VpcRouterResultsPage.to_json())

# convert the object into a dict
vpc_router_results_page_dict = vpc_router_results_page_instance.to_dict()
# create an instance of VpcRouterResultsPage from a dict
vpc_router_results_page_from_dict = VpcRouterResultsPage.from_dict(vpc_router_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


