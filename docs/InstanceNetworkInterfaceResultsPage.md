# InstanceNetworkInterfaceResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InstanceNetworkInterface]**](InstanceNetworkInterface.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.instance_network_interface_results_page import InstanceNetworkInterfaceResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceNetworkInterfaceResultsPage from a JSON string
instance_network_interface_results_page_instance = InstanceNetworkInterfaceResultsPage.from_json(json)
# print the JSON string representation of the object
print(InstanceNetworkInterfaceResultsPage.to_json())

# convert the object into a dict
instance_network_interface_results_page_dict = instance_network_interface_results_page_instance.to_dict()
# create an instance of InstanceNetworkInterfaceResultsPage from a dict
instance_network_interface_results_page_from_dict = InstanceNetworkInterfaceResultsPage.from_dict(instance_network_interface_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


