# SamlIdentityProviderCreate

Create-time identity-related parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_url** | **str** | service provider endpoint where the response will be sent | 
**description** | **str** |  | 
**group_attribute_name** | **str** | If set, SAML attributes with this name will be considered to denote a user&#39;s group membership, where the attribute value(s) should be a comma-separated list of group names. | [optional] 
**idp_entity_id** | **str** | idp&#39;s entity id | 
**idp_metadata_source** | [**IdpMetadataSource**](IdpMetadataSource.md) | the source of an identity provider metadata descriptor | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**signing_keypair** | [**DerEncodedKeyPair**](DerEncodedKeyPair.md) | request signing key pair | [optional] 
**slo_url** | **str** | service provider endpoint where the idp should send log out requests | 
**sp_client_id** | **str** | sp&#39;s client id | 
**technical_contact_email** | **str** | customer&#39;s technical contact for saml configuration | 

## Example

```python
from oxide.models.saml_identity_provider_create import SamlIdentityProviderCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SamlIdentityProviderCreate from a JSON string
saml_identity_provider_create_instance = SamlIdentityProviderCreate.from_json(json)
# print the JSON string representation of the object
print(SamlIdentityProviderCreate.to_json())

# convert the object into a dict
saml_identity_provider_create_dict = saml_identity_provider_create_instance.to_dict()
# create an instance of SamlIdentityProviderCreate from a dict
saml_identity_provider_create_from_dict = SamlIdentityProviderCreate.from_dict(saml_identity_provider_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


