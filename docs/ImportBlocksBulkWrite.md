# ImportBlocksBulkWrite

Parameters for importing blocks with a bulk write

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_encoded_data** | **str** |  | 
**offset** | **int** |  | 

## Example

```python
from oxide.models.import_blocks_bulk_write import ImportBlocksBulkWrite

# TODO update the JSON string below
json = "{}"
# create an instance of ImportBlocksBulkWrite from a JSON string
import_blocks_bulk_write_instance = ImportBlocksBulkWrite.from_json(json)
# print the JSON string representation of the object
print(ImportBlocksBulkWrite.to_json())

# convert the object into a dict
import_blocks_bulk_write_dict = import_blocks_bulk_write_instance.to_dict()
# create an instance of ImportBlocksBulkWrite from a dict
import_blocks_bulk_write_from_dict = ImportBlocksBulkWrite.from_dict(import_blocks_bulk_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


