# IpPoolRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ip_pool_id** | **str** |  | 
**range** | [**IpRange**](IpRange.md) |  | 
**time_created** | **datetime** |  | 

## Example

```python
from oxide.models.ip_pool_range import IpPoolRange

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolRange from a JSON string
ip_pool_range_instance = IpPoolRange.from_json(json)
# print the JSON string representation of the object
print(IpPoolRange.to_json())

# convert the object into a dict
ip_pool_range_dict = ip_pool_range_instance.to_dict()
# create an instance of IpPoolRange from a dict
ip_pool_range_from_dict = IpPoolRange.from_dict(ip_pool_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


