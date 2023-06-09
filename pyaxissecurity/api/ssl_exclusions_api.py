# coding: utf-8

"""
    PublicAdminApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pyaxissecurity.api_client import ApiClient


class SslExclusionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ssl_exclusions_create(self, ssl_exclusion_model, **kwargs):  # noqa: E501
        """Create a New SSL Exclusion  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_create(ssl_exclusion_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SslExclusionModelV1 ssl_exclusion_model: (required)
        :return: SslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ssl_exclusions_create_with_http_info(ssl_exclusion_model, **kwargs)  # noqa: E501
        else:
            (data) = self.ssl_exclusions_create_with_http_info(ssl_exclusion_model, **kwargs)  # noqa: E501
            return data

    def ssl_exclusions_create_with_http_info(self, ssl_exclusion_model, **kwargs):  # noqa: E501
        """Create a New SSL Exclusion  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_create_with_http_info(ssl_exclusion_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SslExclusionModelV1 ssl_exclusion_model: (required)
        :return: SslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ssl_exclusion_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ssl_exclusions_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ssl_exclusion_model' is set
        if self.api_client.client_side_validation and ('ssl_exclusion_model' not in params or
                                                       params['ssl_exclusion_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ssl_exclusion_model` when calling `ssl_exclusions_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ssl_exclusion_model' in params:
            body_params = params['ssl_exclusion_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuthBearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1.0/SslExclusions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SslExclusionModelV1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ssl_exclusions_delete(self, id, **kwargs):  # noqa: E501
        """Delete SSL Exclusion by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ssl_exclusions_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.ssl_exclusions_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def ssl_exclusions_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete SSL Exclusion by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ssl_exclusions_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `ssl_exclusions_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuthBearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1.0/SslExclusions/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ssl_exclusions_get_by_id(self, id, **kwargs):  # noqa: E501
        """Get SSL Exclusion by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_get_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: SslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ssl_exclusions_get_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.ssl_exclusions_get_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def ssl_exclusions_get_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get SSL Exclusion by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_get_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: SslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ssl_exclusions_get_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `ssl_exclusions_get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuthBearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1.0/SslExclusions/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SslExclusionModelV1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ssl_exclusions_query(self, **kwargs):  # noqa: E501
        """Get SSL Exclusions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_query(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number:
        :param int page_size:
        :return: PagedApiResponseOfIEnumerableOfSslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ssl_exclusions_query_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.ssl_exclusions_query_with_http_info(**kwargs)  # noqa: E501
            return data

    def ssl_exclusions_query_with_http_info(self, **kwargs):  # noqa: E501
        """Get SSL Exclusions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_query_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number:
        :param int page_size:
        :return: PagedApiResponseOfIEnumerableOfSslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ssl_exclusions_query" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuthBearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1.0/SslExclusions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedApiResponseOfIEnumerableOfSslExclusionModelV1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ssl_exclusions_update(self, id, ssl_exclusion_model, **kwargs):  # noqa: E501
        """Update an Existing SSL Exclusion  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_update(id, ssl_exclusion_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param SslExclusionModelV1 ssl_exclusion_model: (required)
        :return: SslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ssl_exclusions_update_with_http_info(id, ssl_exclusion_model, **kwargs)  # noqa: E501
        else:
            (data) = self.ssl_exclusions_update_with_http_info(id, ssl_exclusion_model, **kwargs)  # noqa: E501
            return data

    def ssl_exclusions_update_with_http_info(self, id, ssl_exclusion_model, **kwargs):  # noqa: E501
        """Update an Existing SSL Exclusion  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_exclusions_update_with_http_info(id, ssl_exclusion_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param SslExclusionModelV1 ssl_exclusion_model: (required)
        :return: SslExclusionModelV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'ssl_exclusion_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ssl_exclusions_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `ssl_exclusions_update`")  # noqa: E501
        # verify the required parameter 'ssl_exclusion_model' is set
        if self.api_client.client_side_validation and ('ssl_exclusion_model' not in params or
                                                       params['ssl_exclusion_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ssl_exclusion_model` when calling `ssl_exclusions_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ssl_exclusion_model' in params:
            body_params = params['ssl_exclusion_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuthBearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1.0/SslExclusions/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SslExclusionModelV1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
