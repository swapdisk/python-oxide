# SamlIdentityProvider

Identity-related metadata that's included in nearly all public API objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_url** | **str** | Service provider endpoint where the response will be sent | 
**description** | **str** | human-readable free-form text about a resource | 
**group_attribute_name** | **str** | If set, attributes with this name will be considered to denote a user&#39;s group membership, where the values will be the group names. | [optional] 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**idp_entity_id** | **str** | IdP&#39;s entity id | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**public_cert** | **str** | Optional request signing public certificate (base64 encoded der file) | [optional] 
**slo_url** | **str** | Service provider endpoint where the idp should send log out requests | 
**sp_client_id** | **str** | SP&#39;s client id | 
**technical_contact_email** | **str** | Customer&#39;s technical contact for saml configuration | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.saml_identity_provider import SamlIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SamlIdentityProvider from a JSON string
saml_identity_provider_instance = SamlIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(SamlIdentityProvider.to_json())

# convert the object into a dict
saml_identity_provider_dict = saml_identity_provider_instance.to_dict()
# create an instance of SamlIdentityProvider from a dict
saml_identity_provider_from_dict = SamlIdentityProvider.from_dict(saml_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


