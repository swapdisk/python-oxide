# InstanceSerialConsoleData

Contents of an Instance's serial console buffer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[int]** | The bytes starting from the requested offset up to either the end of the buffer or the request&#39;s &#x60;max_bytes&#x60;. Provided as a u8 array rather than a string, as it may not be UTF-8. | 
**last_byte_offset** | **int** | The absolute offset since boot (suitable for use as &#x60;byte_offset&#x60; in a subsequent request) of the last byte returned in &#x60;data&#x60;. | 

## Example

```python
from oxide.models.instance_serial_console_data import InstanceSerialConsoleData

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSerialConsoleData from a JSON string
instance_serial_console_data_instance = InstanceSerialConsoleData.from_json(json)
# print the JSON string representation of the object
print(InstanceSerialConsoleData.to_json())

# convert the object into a dict
instance_serial_console_data_dict = instance_serial_console_data_instance.to_dict()
# create an instance of InstanceSerialConsoleData from a dict
instance_serial_console_data_from_dict = InstanceSerialConsoleData.from_dict(instance_serial_console_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


