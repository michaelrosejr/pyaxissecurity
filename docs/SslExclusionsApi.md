# pyaxissecurity.SslExclusionsApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssl_exclusions_create**](SslExclusionsApi.md#ssl_exclusions_create) | **POST** /api/v1.0/SslExclusions | Create a New SSL Exclusion
[**ssl_exclusions_delete**](SslExclusionsApi.md#ssl_exclusions_delete) | **DELETE** /api/v1.0/SslExclusions/{id} | Delete SSL Exclusion by ID
[**ssl_exclusions_get_by_id**](SslExclusionsApi.md#ssl_exclusions_get_by_id) | **GET** /api/v1.0/SslExclusions/{id} | Get SSL Exclusion by ID
[**ssl_exclusions_query**](SslExclusionsApi.md#ssl_exclusions_query) | **GET** /api/v1.0/SslExclusions | Get SSL Exclusions
[**ssl_exclusions_update**](SslExclusionsApi.md#ssl_exclusions_update) | **PUT** /api/v1.0/SslExclusions/{id} | Update an Existing SSL Exclusion


# **ssl_exclusions_create**
> SslExclusionModelV1 ssl_exclusions_create(ssl_exclusion_model)

Create a New SSL Exclusion

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
api_instance = pyaxissecurity.SslExclusionsApi(pyaxissecurity.ApiClient(configuration))
ssl_exclusion_model = pyaxissecurity.SslExclusionModelV1() # SslExclusionModelV1 | 

try:
    # Create a New SSL Exclusion
    api_response = api_instance.ssl_exclusions_create(ssl_exclusion_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslExclusionsApi->ssl_exclusions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssl_exclusion_model** | [**SslExclusionModelV1**](SslExclusionModelV1.md)|  | 

### Return type

[**SslExclusionModelV1**](SslExclusionModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssl_exclusions_delete**
> ssl_exclusions_delete(id)

Delete SSL Exclusion by ID

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
api_instance = pyaxissecurity.SslExclusionsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete SSL Exclusion by ID
    api_instance.ssl_exclusions_delete(id)
except ApiException as e:
    print("Exception when calling SslExclusionsApi->ssl_exclusions_delete: %s\n" % e)
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

# **ssl_exclusions_get_by_id**
> SslExclusionModelV1 ssl_exclusions_get_by_id(id)

Get SSL Exclusion by ID

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
api_instance = pyaxissecurity.SslExclusionsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get SSL Exclusion by ID
    api_response = api_instance.ssl_exclusions_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslExclusionsApi->ssl_exclusions_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SslExclusionModelV1**](SslExclusionModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssl_exclusions_query**
> PagedApiResponseOfIEnumerableOfSslExclusionModelV1 ssl_exclusions_query(page_number=page_number, page_size=page_size)

Get SSL Exclusions

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
api_instance = pyaxissecurity.SslExclusionsApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get SSL Exclusions
    api_response = api_instance.ssl_exclusions_query(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslExclusionsApi->ssl_exclusions_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PagedApiResponseOfIEnumerableOfSslExclusionModelV1**](PagedApiResponseOfIEnumerableOfSslExclusionModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssl_exclusions_update**
> SslExclusionModelV1 ssl_exclusions_update(id, ssl_exclusion_model)

Update an Existing SSL Exclusion

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
api_instance = pyaxissecurity.SslExclusionsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
ssl_exclusion_model = pyaxissecurity.SslExclusionModelV1() # SslExclusionModelV1 | 

try:
    # Update an Existing SSL Exclusion
    api_response = api_instance.ssl_exclusions_update(id, ssl_exclusion_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslExclusionsApi->ssl_exclusions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ssl_exclusion_model** | [**SslExclusionModelV1**](SslExclusionModelV1.md)|  | 

### Return type

[**SslExclusionModelV1**](SslExclusionModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

