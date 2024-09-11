# SnapshotResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Snapshot]**](Snapshot.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.snapshot_results_page import SnapshotResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResultsPage from a JSON string
snapshot_results_page_instance = SnapshotResultsPage.from_json(json)
# print the JSON string representation of the object
print(SnapshotResultsPage.to_json())

# convert the object into a dict
snapshot_results_page_dict = snapshot_results_page_instance.to_dict()
# create an instance of SnapshotResultsPage from a dict
snapshot_results_page_from_dict = SnapshotResultsPage.from_dict(snapshot_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


