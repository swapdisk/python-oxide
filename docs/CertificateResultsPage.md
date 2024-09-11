# CertificateResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Certificate]**](Certificate.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.certificate_results_page import CertificateResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateResultsPage from a JSON string
certificate_results_page_instance = CertificateResultsPage.from_json(json)
# print the JSON string representation of the object
print(CertificateResultsPage.to_json())

# convert the object into a dict
certificate_results_page_dict = certificate_results_page_instance.to_dict()
# create an instance of CertificateResultsPage from a dict
certificate_results_page_from_dict = CertificateResultsPage.from_dict(certificate_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


