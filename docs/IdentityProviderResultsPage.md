# IdentityProviderResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IdentityProvider]**](IdentityProvider.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.identity_provider_results_page import IdentityProviderResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderResultsPage from a JSON string
identity_provider_results_page_instance = IdentityProviderResultsPage.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderResultsPage.to_json())

# convert the object into a dict
identity_provider_results_page_dict = identity_provider_results_page_instance.to_dict()
# create an instance of IdentityProviderResultsPage from a dict
identity_provider_results_page_from_dict = IdentityProviderResultsPage.from_dict(identity_provider_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


