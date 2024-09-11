# InstanceCreate

Create-time parameters for an `Instance`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**disks** | [**List[InstanceDiskAttachment]**](InstanceDiskAttachment.md) | The disks to be created or attached for this instance. | [optional] [default to []]
**external_ips** | [**List[ExternalIpCreate]**](ExternalIpCreate.md) | The external IP addresses provided to this instance.  By default, all instances have outbound connectivity, but no inbound connectivity. These external addresses can be used to provide a fixed, known IP address for making inbound connections to the instance. | [optional] [default to []]
**hostname** | **str** | A hostname identifies a host on a network, and is usually a dot-delimited sequence of labels, where each label contains only letters, digits, or the hyphen. See RFCs 1035 and 952 for more details. | 
**memory** | **int** | Byte count to express memory or storage capacity. | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**ncpus** | **int** | The number of CPUs in an Instance | 
**network_interfaces** | [**InstanceNetworkInterfaceAttachment**](InstanceNetworkInterfaceAttachment.md) | The network interfaces to be created for this instance. | [optional] 
**ssh_public_keys** | [**List[NameOrId]**](NameOrId.md) | An allowlist of SSH public keys to be transferred to the instance via cloud-init during instance creation.  If not provided, all SSH public keys from the user&#39;s profile will be sent. If an empty list is provided, no public keys will be transmitted to the instance. | [optional] 
**start** | **bool** | Should this instance be started upon creation; true by default. | [optional] [default to True]
**user_data** | **bytearray** | User data for instance initialization systems (such as cloud-init). Must be a Base64-encoded string, as specified in RFC 4648 § 4 (+ and / characters with padding). Maximum 32 KiB unencoded data. | [optional] [default to '[B@1763992e']

## Example

```python
from oxide.models.instance_create import InstanceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceCreate from a JSON string
instance_create_instance = InstanceCreate.from_json(json)
# print the JSON string representation of the object
print(InstanceCreate.to_json())

# convert the object into a dict
instance_create_dict = instance_create_instance.to_dict()
# create an instance of InstanceCreate from a dict
instance_create_from_dict = InstanceCreate.from_dict(instance_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


