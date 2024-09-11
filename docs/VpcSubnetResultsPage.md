# VpcSubnetResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VpcSubnet]**](VpcSubnet.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.vpc_subnet_results_page import VpcSubnetResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of VpcSubnetResultsPage from a JSON string
vpc_subnet_results_page_instance = VpcSubnetResultsPage.from_json(json)
# print the JSON string representation of the object
print(VpcSubnetResultsPage.to_json())

# convert the object into a dict
vpc_subnet_results_page_dict = vpc_subnet_results_page_instance.to_dict()
# create an instance of VpcSubnetResultsPage from a dict
vpc_subnet_results_page_from_dict = VpcSubnetResultsPage.from_dict(vpc_subnet_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


