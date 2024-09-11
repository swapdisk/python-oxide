# DiskResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Disk]**](Disk.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.disk_results_page import DiskResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of DiskResultsPage from a JSON string
disk_results_page_instance = DiskResultsPage.from_json(json)
# print the JSON string representation of the object
print(DiskResultsPage.to_json())

# convert the object into a dict
disk_results_page_dict = disk_results_page_instance.to_dict()
# create an instance of DiskResultsPage from a dict
disk_results_page_from_dict = DiskResultsPage.from_dict(disk_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


