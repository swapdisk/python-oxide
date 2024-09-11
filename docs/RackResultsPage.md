# RackResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Rack]**](Rack.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.rack_results_page import RackResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of RackResultsPage from a JSON string
rack_results_page_instance = RackResultsPage.from_json(json)
# print the JSON string representation of the object
print(RackResultsPage.to_json())

# convert the object into a dict
rack_results_page_dict = rack_results_page_instance.to_dict()
# create an instance of RackResultsPage from a dict
rack_results_page_from_dict = RackResultsPage.from_dict(rack_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


