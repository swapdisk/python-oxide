# SwitchPortSettingsResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SwitchPortSettings]**](SwitchPortSettings.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.switch_port_settings_results_page import SwitchPortSettingsResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortSettingsResultsPage from a JSON string
switch_port_settings_results_page_instance = SwitchPortSettingsResultsPage.from_json(json)
# print the JSON string representation of the object
print(SwitchPortSettingsResultsPage.to_json())

# convert the object into a dict
switch_port_settings_results_page_dict = switch_port_settings_results_page_instance.to_dict()
# create an instance of SwitchPortSettingsResultsPage from a dict
switch_port_settings_results_page_from_dict = SwitchPortSettingsResultsPage.from_dict(switch_port_settings_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


