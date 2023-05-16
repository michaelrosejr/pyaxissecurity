# pyaxissecurity.SwgCategoryApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**swg_category_create**](SwgCategoryApi.md#swg_category_create) | **POST** /api/v1.0/webcategories | Create a New Web Category
[**swg_category_delete**](SwgCategoryApi.md#swg_category_delete) | **DELETE** /api/v1.0/webcategories/{id} | Delete Web Category by ID
[**swg_category_get_by_id**](SwgCategoryApi.md#swg_category_get_by_id) | **GET** /api/v1.0/webcategories/{id} | Get Web Category by ID
[**swg_category_query**](SwgCategoryApi.md#swg_category_query) | **GET** /api/v1.0/webcategories | Get Web Categories
[**swg_category_update**](SwgCategoryApi.md#swg_category_update) | **PUT** /api/v1.0/webcategories/{id} | Update an Existing Web Category


# **swg_category_create**
> SwgCategoryModelV1 swg_category_create(category_model)

Create a New Web Category

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.SwgCategoryApi(pyaxissecurity.ApiClient(configuration))
category_model = pyaxissecurity.SwgCategoryModelV1() # SwgCategoryModelV1 | 

try:
    # Create a New Web Category
    api_response = api_instance.swg_category_create(category_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwgCategoryApi->swg_category_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_model** | [**SwgCategoryModelV1**](SwgCategoryModelV1.md)|  | 

### Return type

[**SwgCategoryModelV1**](SwgCategoryModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swg_category_delete**
> swg_category_delete(id)

Delete Web Category by ID

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.SwgCategoryApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Web Category by ID
    api_instance.swg_category_delete(id)
except ApiException as e:
    print("Exception when calling SwgCategoryApi->swg_category_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swg_category_get_by_id**
> SwgCategoryModelV1 swg_category_get_by_id(id)

Get Web Category by ID

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.SwgCategoryApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Web Category by ID
    api_response = api_instance.swg_category_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwgCategoryApi->swg_category_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SwgCategoryModelV1**](SwgCategoryModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swg_category_query**
> PagedApiResponseOfIEnumerableOfSwgCategoryModelV1 swg_category_query(page_number=page_number, page_size=page_size)

Get Web Categories

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.SwgCategoryApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get Web Categories
    api_response = api_instance.swg_category_query(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwgCategoryApi->swg_category_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PagedApiResponseOfIEnumerableOfSwgCategoryModelV1**](PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swg_category_update**
> SwgCategoryModelV1 swg_category_update(id, category_model)

Update an Existing Web Category

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.SwgCategoryApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
category_model = pyaxissecurity.SwgCategoryModelV1() # SwgCategoryModelV1 | 

try:
    # Update an Existing Web Category
    api_response = api_instance.swg_category_update(id, category_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwgCategoryApi->swg_category_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **category_model** | [**SwgCategoryModelV1**](SwgCategoryModelV1.md)|  | 

### Return type

[**SwgCategoryModelV1**](SwgCategoryModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

