# SshKeyResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SshKey]**](SshKey.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.ssh_key_results_page import SshKeyResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyResultsPage from a JSON string
ssh_key_results_page_instance = SshKeyResultsPage.from_json(json)
# print the JSON string representation of the object
print(SshKeyResultsPage.to_json())

# convert the object into a dict
ssh_key_results_page_dict = ssh_key_results_page_instance.to_dict()
# create an instance of SshKeyResultsPage from a dict
ssh_key_results_page_from_dict = SshKeyResultsPage.from_dict(ssh_key_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


