# SwitchPortResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SwitchPort]**](SwitchPort.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.switch_port_results_page import SwitchPortResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortResultsPage from a JSON string
switch_port_results_page_instance = SwitchPortResultsPage.from_json(json)
# print the JSON string representation of the object
print(SwitchPortResultsPage.to_json())

# convert the object into a dict
switch_port_results_page_dict = switch_port_results_page_instance.to_dict()
# create an instance of SwitchPortResultsPage from a dict
switch_port_results_page_from_dict = SwitchPortResultsPage.from_dict(switch_port_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


