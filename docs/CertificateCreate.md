# CertificateCreate

Create-time parameters for a `Certificate`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | PEM-formatted string containing public certificate chain | 
**description** | **str** |  | 
**key** | **str** | PEM-formatted string containing private key | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**service** | [**ServiceUsingCertificate**](ServiceUsingCertificate.md) | The service using this certificate | 

## Example

```python
from oxide.models.certificate_create import CertificateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateCreate from a JSON string
certificate_create_instance = CertificateCreate.from_json(json)
# print the JSON string representation of the object
print(CertificateCreate.to_json())

# convert the object into a dict
certificate_create_dict = certificate_create_instance.to_dict()
# create an instance of CertificateCreate from a dict
certificate_create_from_dict = CertificateCreate.from_dict(certificate_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


