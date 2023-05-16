# pyaxissecurity.ApplicationGroupsApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_groups_create**](ApplicationGroupsApi.md#application_groups_create) | **POST** /api/v1.0/tags | Create a New Application Group
[**application_groups_delete**](ApplicationGroupsApi.md#application_groups_delete) | **DELETE** /api/v1.0/tags/{id} | Delete Application Group by ID
[**application_groups_get_by_id**](ApplicationGroupsApi.md#application_groups_get_by_id) | **GET** /api/v1.0/tags/{id} | Get Application Group by ID
[**application_groups_query**](ApplicationGroupsApi.md#application_groups_query) | **GET** /api/v1.0/tags | Get Application Groups
[**application_groups_update**](ApplicationGroupsApi.md#application_groups_update) | **PUT** /api/v1.0/tags/{id} | Update an Existing Application Group


# **application_groups_create**
> application_groups_create(application_group_model)

Create a New Application Group

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
api_instance = pyaxissecurity.ApplicationGroupsApi(pyaxissecurity.ApiClient(configuration))
application_group_model = pyaxissecurity.ApplicationGroupModelV1() # ApplicationGroupModelV1 | 

try:
    # Create a New Application Group
    api_instance.application_groups_create(application_group_model)
except ApiException as e:
    print("Exception when calling ApplicationGroupsApi->application_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_group_model** | [**ApplicationGroupModelV1**](ApplicationGroupModelV1.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_groups_delete**
> application_groups_delete(id)

Delete Application Group by ID

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
api_instance = pyaxissecurity.ApplicationGroupsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Application Group by ID
    api_instance.application_groups_delete(id)
except ApiException as e:
    print("Exception when calling ApplicationGroupsApi->application_groups_delete: %s\n" % e)
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

# **application_groups_get_by_id**
> application_groups_get_by_id(id)

Get Application Group by ID

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
api_instance = pyaxissecurity.ApplicationGroupsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Application Group by ID
    api_instance.application_groups_get_by_id(id)
except ApiException as e:
    print("Exception when calling ApplicationGroupsApi->application_groups_get_by_id: %s\n" % e)
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

# **application_groups_query**
> application_groups_query(page_number=page_number, page_size=page_size)

Get Application Groups

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
api_instance = pyaxissecurity.ApplicationGroupsApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get Application Groups
    api_instance.application_groups_query(page_number=page_number, page_size=page_size)
except ApiException as e:
    print("Exception when calling ApplicationGroupsApi->application_groups_query: %s\n" % e)
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

# **application_groups_update**
> application_groups_update(id, application_group_model)

Update an Existing Application Group

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
api_instance = pyaxissecurity.ApplicationGroupsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
application_group_model = pyaxissecurity.ApplicationGroupModelV1() # ApplicationGroupModelV1 | 

try:
    # Update an Existing Application Group
    api_instance.application_groups_update(id, application_group_model)
except ApiException as e:
    print("Exception when calling ApplicationGroupsApi->application_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **application_group_model** | [**ApplicationGroupModelV1**](ApplicationGroupModelV1.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

