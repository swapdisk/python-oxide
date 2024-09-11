# Distributiondouble

A distribution is a sequence of bins and counts in those bins, and some statistical information tracked to compute the mean, standard deviation, and quantile estimates.  Min, max, and the p-* quantiles are treated as optional due to the possibility of distribution operations, like subtraction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bins** | **List[float]** |  | 
**counts** | **List[int]** |  | 
**max** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**p50** | [**Quantile**](Quantile.md) |  | [optional] 
**p90** | [**Quantile**](Quantile.md) |  | [optional] 
**p99** | [**Quantile**](Quantile.md) |  | [optional] 
**squared_mean** | **float** |  | 
**sum_of_samples** | **float** |  | 

## Example

```python
from oxide.models.distributiondouble import Distributiondouble

# TODO update the JSON string below
json = "{}"
# create an instance of Distributiondouble from a JSON string
distributiondouble_instance = Distributiondouble.from_json(json)
# print the JSON string representation of the object
print(Distributiondouble.to_json())

# convert the object into a dict
distributiondouble_dict = distributiondouble_instance.to_dict()
# create an instance of Distributiondouble from a dict
distributiondouble_from_dict = Distributiondouble.from_dict(distributiondouble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


