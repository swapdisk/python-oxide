# ServiceUsingCertificate

The service intended to use this certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from oxide.models.service_using_certificate import ServiceUsingCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUsingCertificate from a JSON string
service_using_certificate_instance = ServiceUsingCertificate.from_json(json)
# print the JSON string representation of the object
print(ServiceUsingCertificate.to_json())

# convert the object into a dict
service_using_certificate_dict = service_using_certificate_instance.to_dict()
# create an instance of ServiceUsingCertificate from a dict
service_using_certificate_from_dict = ServiceUsingCertificate.from_dict(service_using_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


