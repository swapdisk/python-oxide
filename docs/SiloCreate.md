# SiloCreate

Create-time parameters for a `Silo`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_group_name** | **str** | If set, this group will be created during Silo creation and granted the \&quot;Silo Admin\&quot; role. Identity providers can assert that users belong to this group and those users can log in and further initialize the Silo.  Note that if configuring a SAML based identity provider, group_attribute_name must be set for users to be considered part of a group. See &#x60;SamlIdentityProviderCreate&#x60; for more information. | [optional] 
**description** | **str** |  | 
**discoverable** | **bool** |  | 
**identity_mode** | [**SiloIdentityMode**](SiloIdentityMode.md) |  | 
**mapped_fleet_roles** | **Dict[str, List[FleetRole]]** | Mapping of which Fleet roles are conferred by each Silo role  The default is that no Fleet roles are conferred by any Silo roles unless there&#39;s a corresponding entry in this map. | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**quotas** | [**SiloQuotasCreate**](SiloQuotasCreate.md) | Limits the amount of provisionable CPU, memory, and storage in the Silo. CPU and memory are only consumed by running instances, while storage is consumed by any disk or snapshot. A value of 0 means that resource is *not* provisionable. | 
**tls_certificates** | [**List[CertificateCreate]**](CertificateCreate.md) | Initial TLS certificates to be used for the new Silo&#39;s console and API endpoints.  These should be valid for the Silo&#39;s DNS name(s). | 

## Example

```python
from oxide.models.silo_create import SiloCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SiloCreate from a JSON string
silo_create_instance = SiloCreate.from_json(json)
# print the JSON string representation of the object
print(SiloCreate.to_json())

# convert the object into a dict
silo_create_dict = silo_create_instance.to_dict()
# create an instance of SiloCreate from a dict
silo_create_from_dict = SiloCreate.from_dict(silo_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


