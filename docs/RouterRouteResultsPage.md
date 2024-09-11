# RouterRouteResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RouterRoute]**](RouterRoute.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.router_route_results_page import RouterRouteResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of RouterRouteResultsPage from a JSON string
router_route_results_page_instance = RouterRouteResultsPage.from_json(json)
# print the JSON string representation of the object
print(RouterRouteResultsPage.to_json())

# convert the object into a dict
router_route_results_page_dict = router_route_results_page_instance.to_dict()
# create an instance of RouterRouteResultsPage from a dict
router_route_results_page_from_dict = RouterRouteResultsPage.from_dict(router_route_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


