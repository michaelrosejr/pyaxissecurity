# pyaxissecurity.UsersApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create**](UsersApi.md#users_create) | **POST** /api/v1.0/Users | Create a New User
[**users_delete**](UsersApi.md#users_delete) | **DELETE** /api/v1.0/Users/{id} | Delete User by ID
[**users_get_by_id**](UsersApi.md#users_get_by_id) | **GET** /api/v1.0/Users/{id} | Get User by ID
[**users_query**](UsersApi.md#users_query) | **GET** /api/v1.0/Users | Get Users
[**users_update**](UsersApi.md#users_update) | **PUT** /api/v1.0/Users/{id} | Update an Existing User


# **users_create**
> UserModelV1 users_create(user_model)

Create a New User

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
api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
user_model = pyaxissecurity.UserModelV1() # UserModelV1 | 

try:
    # Create a New User
    api_response = api_instance.users_create(user_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_model** | [**UserModelV1**](UserModelV1.md)|  | 

### Return type

[**UserModelV1**](UserModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete**
> users_delete(id)

Delete User by ID

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
api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete User by ID
    api_instance.users_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_delete: %s\n" % e)
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

# **users_get_by_id**
> UserModelV1 users_get_by_id(id)

Get User by ID

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
api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get User by ID
    api_response = api_instance.users_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserModelV1**](UserModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_query**
> PagedApiResponseOfIEnumerableOfUserModelV1 users_query(page_number=page_number, page_size=page_size)

Get Users

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
api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get Users
    api_response = api_instance.users_query(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PagedApiResponseOfIEnumerableOfUserModelV1**](PagedApiResponseOfIEnumerableOfUserModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update**
> UserModelV1 users_update(id, user_model)

Update an Existing User

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
api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
user_model = pyaxissecurity.UserModelV1() # UserModelV1 | 

try:
    # Update an Existing User
    api_response = api_instance.users_update(id, user_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_model** | [**UserModelV1**](UserModelV1.md)|  | 

### Return type

[**UserModelV1**](UserModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

