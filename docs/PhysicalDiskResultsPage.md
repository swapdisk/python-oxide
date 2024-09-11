# PhysicalDiskResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PhysicalDisk]**](PhysicalDisk.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.physical_disk_results_page import PhysicalDiskResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalDiskResultsPage from a JSON string
physical_disk_results_page_instance = PhysicalDiskResultsPage.from_json(json)
# print the JSON string representation of the object
print(PhysicalDiskResultsPage.to_json())

# convert the object into a dict
physical_disk_results_page_dict = physical_disk_results_page_instance.to_dict()
# create an instance of PhysicalDiskResultsPage from a dict
physical_disk_results_page_from_dict = PhysicalDiskResultsPage.from_dict(physical_disk_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


