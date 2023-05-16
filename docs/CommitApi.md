# pyaxissecurity.CommitApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_commit_changes**](CommitApi.md#commit_commit_changes) | **POST** /api/v1.0/Commit | Commit Changes


# **commit_commit_changes**
> commit_commit_changes()

Commit Changes

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
api_instance = pyaxissecurity.CommitApi(pyaxissecurity.ApiClient(configuration))

try:
    # Commit Changes
    api_instance.commit_commit_changes()
except ApiException as e:
    print("Exception when calling CommitApi->commit_commit_changes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

