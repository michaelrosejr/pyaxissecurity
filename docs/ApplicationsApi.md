# pyaxissecurity.ApplicationsApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_create**](ApplicationsApi.md#applications_create) | **POST** /api/v1.0/Applications | Create a New Application
[**applications_delete**](ApplicationsApi.md#applications_delete) | **DELETE** /api/v1.0/Applications/{id} | Delete Application by ID
[**applications_get_by_id**](ApplicationsApi.md#applications_get_by_id) | **GET** /api/v1.0/Applications/{id} | Get Application by ID
[**applications_query**](ApplicationsApi.md#applications_query) | **GET** /api/v1.0/Applications | Get Applications
[**applications_update**](ApplicationsApi.md#applications_update) | **PUT** /api/v1.0/Applications/{id} | Update an Existing Application


# **applications_create**
> applications_create(app_model)

Create a New Application

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
api_instance = pyaxissecurity.ApplicationsApi(pyaxissecurity.ApiClient(configuration))
app_model = pyaxissecurity.ApplicationModelV1() # ApplicationModelV1 | 

try:
    # Create a New Application
    api_instance.applications_create(app_model)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_model** | [**ApplicationModelV1**](ApplicationModelV1.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_delete**
> applications_delete(id)

Delete Application by ID

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
api_instance = pyaxissecurity.ApplicationsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Application by ID
    api_instance.applications_delete(id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_delete: %s\n" % e)
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

# **applications_get_by_id**
> applications_get_by_id(id)

Get Application by ID

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
api_instance = pyaxissecurity.ApplicationsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Application by ID
    api_instance.applications_get_by_id(id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_get_by_id: %s\n" % e)
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

# **applications_query**
> applications_query(page_number=page_number, page_size=page_size)

Get Applications

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
api_instance = pyaxissecurity.ApplicationsApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get Applications
    api_instance.applications_query(page_number=page_number, page_size=page_size)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_update**
> applications_update(id, app_model)

Update an Existing Application

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
api_instance = pyaxissecurity.ApplicationsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
app_model = pyaxissecurity.ApplicationModelV1() # ApplicationModelV1 | 

try:
    # Update an Existing Application
    api_instance.applications_update(id, app_model)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_model** | [**ApplicationModelV1**](ApplicationModelV1.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

