# Distributionint64

A distribution is a sequence of bins and counts in those bins, and some statistical information tracked to compute the mean, standard deviation, and quantile estimates.  Min, max, and the p-* quantiles are treated as optional due to the possibility of distribution operations, like subtraction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bins** | **List[int]** |  | 
**counts** | **List[int]** |  | 
**max** | **int** |  | [optional] 
**min** | **int** |  | [optional] 
**p50** | [**Quantile**](Quantile.md) |  | [optional] 
**p90** | [**Quantile**](Quantile.md) |  | [optional] 
**p99** | [**Quantile**](Quantile.md) |  | [optional] 
**squared_mean** | **float** |  | 
**sum_of_samples** | **int** |  | 

## Example

```python
from oxide.models.distributionint64 import Distributionint64

# TODO update the JSON string below
json = "{}"
# create an instance of Distributionint64 from a JSON string
distributionint64_instance = Distributionint64.from_json(json)
# print the JSON string representation of the object
print(Distributionint64.to_json())

# convert the object into a dict
distributionint64_dict = distributionint64_instance.to_dict()
# create an instance of Distributionint64 from a dict
distributionint64_from_dict = Distributionint64.from_dict(distributionint64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


