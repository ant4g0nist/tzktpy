# coding: utf-8

"""
    TzKT API

    # Introduction  TzKT Explorer provides free REST API and WebSocket API for accessing detailed Tezos blockchain data and helps developers build more services and applications on top of Tezos. TzKT is an open-source project, so you can easily clone and build it and use it as a self-hosted service to avoid any risks of depending on third-party services.  TzKT API is available for the following Tezos networks with the following base URLs:  - Mainnet: `https://api.tzkt.io/` or `https://api.mainnet.tzkt.io/` ([view docs](https://api.tzkt.io))  - Hangzhounet: `https://api.hangzhounet.tzkt.io/` ([view docs](https://api.hangzhounet.tzkt.io)) - Ithacanet: `https://api.ithacanet.tzkt.io/` ([view docs](https://api.ithacanet.tzkt.io))  We also provide a staging environment for testing newest features and pre-updating client applications before deploying to production:  - Mainnet staging: `https://staging.api.tzkt.io/` or `https://staging.api.mainnet.tzkt.io/` ([view docs](https://staging.api.tzkt.io))  Feel free to contact us if you have any questions or feature requests. Your feedback really helps us make TzKT better!  - Discord: https://discord.gg/aG8XKuwsQd - Telegram: https://t.me/baking_bad_chat - Slack: https://tezos-dev.slack.com/archives/CV5NX7F2L - Twitter: https://twitter.com/TezosBakingBad - Email: hello@baking-bad.org  And don't forget to star TzKT project [on GitHub](https://github.com/baking-bad/tzkt) ;)  # Terms of Use  TzKT API is free for everyone and for both commercial and non-commercial usage.  If your application or service uses the TzKT API in any forms: directly on frontend or indirectly on backend, you must mention that fact on your website or application by placing the label **\"Powered by TzKT API\"** or **\"Built with TzKT API\"** with a direct link to [tzkt.io](https://tzkt.io).   # Rate Limits  There will be no rate limits as long as our servers can handle the load without additional infrastructure costs. However, any apparent abuse will be prevented by setting targeted rate limits.  Check out [Tezos Explorer API Best Practices](https://baking-bad.org/blog/tag/TzKT/) and in particular [how to optimize requests count](https://baking-bad.org/blog/2020/07/29/tezos-explorer-api-tzkt-how-often-to-make-requests/).  ---   # noqa: E501

    OpenAPI spec version: v1.8.3
    Contact: hello@baking-bad.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DelegatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delegates_get(self, **kwargs):  # noqa: E501
        """Get delegates  # noqa: E501

        Returns a list of delegate accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delegates_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Active active: Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates)
        :param LastActivity2 last_activity: Filters delegates by last activity level (where the delegate was updated)
        :param Select15 select: Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes.
        :param Sort21 sort: Sorts delegators by specified field. Supported fields: `id` (default), `activationLevel`, `deactivationLevel`, `stakingBalance`, `balance`, `numDelegators`.
        :param Offset19 offset: Specifies which or how many items should be skipped
        :param int limit: Maximum number of items to return
        :return: list[Delegate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delegates_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delegates_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def delegates_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get delegates  # noqa: E501

        Returns a list of delegate accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delegates_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Active active: Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates)
        :param LastActivity2 last_activity: Filters delegates by last activity level (where the delegate was updated)
        :param Select15 select: Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes.
        :param Sort21 sort: Sorts delegators by specified field. Supported fields: `id` (default), `activationLevel`, `deactivationLevel`, `stakingBalance`, `balance`, `numDelegators`.
        :param Offset19 offset: Specifies which or how many items should be skipped
        :param int limit: Maximum number of items to return
        :return: list[Delegate]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['active', 'last_activity', 'select', 'sort', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delegates_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501
        if 'last_activity' in params:
            query_params.append(('lastActivity', params['last_activity']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/delegates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Delegate]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delegates_get_by_address(self, address, **kwargs):  # noqa: E501
        """Get delegate by address  # noqa: E501

        Returns a delegate with the specified address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delegates_get_by_address(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Delegate address (starting with tz) (required)
        :return: Delegate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delegates_get_by_address_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.delegates_get_by_address_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def delegates_get_by_address_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get delegate by address  # noqa: E501

        Returns a delegate with the specified address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delegates_get_by_address_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Delegate address (starting with tz) (required)
        :return: Delegate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delegates_get_by_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `delegates_get_by_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/delegates/{address}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Delegate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delegates_get_count(self, **kwargs):  # noqa: E501
        """Get delegates count  # noqa: E501

        Returns a number of delegate accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delegates_get_count(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Active1 active: Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delegates_get_count_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delegates_get_count_with_http_info(**kwargs)  # noqa: E501
            return data

    def delegates_get_count_with_http_info(self, **kwargs):  # noqa: E501
        """Get delegates count  # noqa: E501

        Returns a number of delegate accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delegates_get_count_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Active1 active: Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['active']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delegates_get_count" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/delegates/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)