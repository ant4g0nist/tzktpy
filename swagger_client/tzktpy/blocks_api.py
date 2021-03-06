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


class BlocksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def blocks_get(self, **kwargs):  # noqa: E501
        """Get blocks  # noqa: E501

        Returns a list of blocks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Baker1 baker: [DEPRECATED]
        :param str anyof: Filters by any of the specified fields. Example: `anyof.proposer.producer=tz1...`.
        :param Proposer proposer: Filters blocks by block proposer. Allowed fields for `.eqx` mode: none.
        :param Producer producer: Filters blocks by block producer. Allowed fields for `.eqx` mode: none.
        :param Level2 level: Filters blocks by level.
        :param Timestamp2 timestamp: Filters blocks by timestamp.
        :param Priority priority: [DEPRECATED]
        :param BlockRound block_round: Filters blocks by block round.
        :param Select5 select: Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes.
        :param Sort10 sort: Sorts blocks by specified field. Supported fields: `id` (default), `level`, `payloadRound`, `blockRound`, `validations`, `reward`, `bonus`, `fees`.
        :param Offset8 offset: Specifies which or how many items should be skipped
        :param int limit: Maximum number of items to return
        :param Quote2 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: list[Block]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.blocks_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def blocks_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get blocks  # noqa: E501

        Returns a list of blocks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Baker1 baker: [DEPRECATED]
        :param str anyof: Filters by any of the specified fields. Example: `anyof.proposer.producer=tz1...`.
        :param Proposer proposer: Filters blocks by block proposer. Allowed fields for `.eqx` mode: none.
        :param Producer producer: Filters blocks by block producer. Allowed fields for `.eqx` mode: none.
        :param Level2 level: Filters blocks by level.
        :param Timestamp2 timestamp: Filters blocks by timestamp.
        :param Priority priority: [DEPRECATED]
        :param BlockRound block_round: Filters blocks by block round.
        :param Select5 select: Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes.
        :param Sort10 sort: Sorts blocks by specified field. Supported fields: `id` (default), `level`, `payloadRound`, `blockRound`, `validations`, `reward`, `bonus`, `fees`.
        :param Offset8 offset: Specifies which or how many items should be skipped
        :param int limit: Maximum number of items to return
        :param Quote2 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: list[Block]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['baker', 'anyof', 'proposer', 'producer', 'level', 'timestamp', 'priority', 'block_round', 'select', 'sort', 'offset', 'limit', 'quote']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'baker' in params:
            query_params.append(('baker', params['baker']))  # noqa: E501
        if 'anyof' in params:
            query_params.append(('anyof', params['anyof']))  # noqa: E501
        if 'proposer' in params:
            query_params.append(('proposer', params['proposer']))  # noqa: E501
        if 'producer' in params:
            query_params.append(('producer', params['producer']))  # noqa: E501
        if 'level' in params:
            query_params.append(('level', params['level']))  # noqa: E501
        if 'timestamp' in params:
            query_params.append(('timestamp', params['timestamp']))  # noqa: E501
        if 'priority' in params:
            query_params.append(('priority', params['priority']))  # noqa: E501
        if 'block_round' in params:
            query_params.append(('blockRound', params['block_round']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'quote' in params:
            query_params.append(('quote', params['quote']))  # noqa: E501

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
            '/v1/blocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Block]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_get_by_date(self, timestamp, **kwargs):  # noqa: E501
        """Get block by timestamp  # noqa: E501

        Returns a block closest to the specified timestamp.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_date(timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime timestamp: Timestamp, e.g. `2020-01-01T00:00:00Z` (required)
        :param bool operations: Flag indicating whether to include block operations into returned object or not
        :param Micheline11 micheline: Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string
        :param Quote5 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: Block
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.blocks_get_by_date_with_http_info(timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_by_date_with_http_info(timestamp, **kwargs)  # noqa: E501
            return data

    def blocks_get_by_date_with_http_info(self, timestamp, **kwargs):  # noqa: E501
        """Get block by timestamp  # noqa: E501

        Returns a block closest to the specified timestamp.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_date_with_http_info(timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime timestamp: Timestamp, e.g. `2020-01-01T00:00:00Z` (required)
        :param bool operations: Flag indicating whether to include block operations into returned object or not
        :param Micheline11 micheline: Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string
        :param Quote5 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: Block
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['timestamp', 'operations', 'micheline', 'quote']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get_by_date" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'timestamp' is set
        if ('timestamp' not in params or
                params['timestamp'] is None):
            raise ValueError("Missing the required parameter `timestamp` when calling `blocks_get_by_date`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'timestamp' in params:
            path_params['timestamp'] = params['timestamp']  # noqa: E501

        query_params = []
        if 'operations' in params:
            query_params.append(('operations', params['operations']))  # noqa: E501
        if 'micheline' in params:
            query_params.append(('micheline', params['micheline']))  # noqa: E501
        if 'quote' in params:
            query_params.append(('quote', params['quote']))  # noqa: E501

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
            '/v1/blocks/{timestamp}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Block',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_get_by_date2(self, timestamp, **kwargs):  # noqa: E501
        """Get level by timestamp  # noqa: E501

        Returns a level of the block closest to the specified timestamp.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_date2(timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime timestamp: Timestamp, e.g. `2020-01-01T00:00:00Z` (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.blocks_get_by_date2_with_http_info(timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_by_date2_with_http_info(timestamp, **kwargs)  # noqa: E501
            return data

    def blocks_get_by_date2_with_http_info(self, timestamp, **kwargs):  # noqa: E501
        """Get level by timestamp  # noqa: E501

        Returns a level of the block closest to the specified timestamp.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_date2_with_http_info(timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime timestamp: Timestamp, e.g. `2020-01-01T00:00:00Z` (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get_by_date2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'timestamp' is set
        if ('timestamp' not in params or
                params['timestamp'] is None):
            raise ValueError("Missing the required parameter `timestamp` when calling `blocks_get_by_date2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'timestamp' in params:
            path_params['timestamp'] = params['timestamp']  # noqa: E501

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
            '/v1/blocks/{timestamp}/level', 'GET',
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

    def blocks_get_by_hash(self, hash, **kwargs):  # noqa: E501
        """Get block by hash  # noqa: E501

        Returns a block with the specified hash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_hash(hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hash: Block hash (required)
        :param bool operations: Flag indicating whether to include block operations into returned object or not
        :param Micheline9 micheline: Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string
        :param Quote3 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: Block
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.blocks_get_by_hash_with_http_info(hash, **kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_by_hash_with_http_info(hash, **kwargs)  # noqa: E501
            return data

    def blocks_get_by_hash_with_http_info(self, hash, **kwargs):  # noqa: E501
        """Get block by hash  # noqa: E501

        Returns a block with the specified hash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_hash_with_http_info(hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hash: Block hash (required)
        :param bool operations: Flag indicating whether to include block operations into returned object or not
        :param Micheline9 micheline: Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string
        :param Quote3 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: Block
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hash', 'operations', 'micheline', 'quote']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get_by_hash" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hash' is set
        if ('hash' not in params or
                params['hash'] is None):
            raise ValueError("Missing the required parameter `hash` when calling `blocks_get_by_hash`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hash' in params:
            path_params['hash'] = params['hash']  # noqa: E501

        query_params = []
        if 'operations' in params:
            query_params.append(('operations', params['operations']))  # noqa: E501
        if 'micheline' in params:
            query_params.append(('micheline', params['micheline']))  # noqa: E501
        if 'quote' in params:
            query_params.append(('quote', params['quote']))  # noqa: E501

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
            '/v1/blocks/{hash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Block',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_get_by_level(self, level, **kwargs):  # noqa: E501
        """Get block by level  # noqa: E501

        Returns a block at the specified level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_level(level, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int level: Block level (required)
        :param bool operations: Flag indicating whether to include block operations into returned object or not
        :param Micheline10 micheline: Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string
        :param Quote4 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: Block
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.blocks_get_by_level_with_http_info(level, **kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_by_level_with_http_info(level, **kwargs)  # noqa: E501
            return data

    def blocks_get_by_level_with_http_info(self, level, **kwargs):  # noqa: E501
        """Get block by level  # noqa: E501

        Returns a block at the specified level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_level_with_http_info(level, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int level: Block level (required)
        :param bool operations: Flag indicating whether to include block operations into returned object or not
        :param Micheline10 micheline: Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string
        :param Quote4 quote: Comma-separated list of ticker symbols to inject historical prices into response
        :return: Block
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['level', 'operations', 'micheline', 'quote']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get_by_level" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'level' is set
        if ('level' not in params or
                params['level'] is None):
            raise ValueError("Missing the required parameter `level` when calling `blocks_get_by_level`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'level' in params:
            path_params['level'] = params['level']  # noqa: E501

        query_params = []
        if 'operations' in params:
            query_params.append(('operations', params['operations']))  # noqa: E501
        if 'micheline' in params:
            query_params.append(('micheline', params['micheline']))  # noqa: E501
        if 'quote' in params:
            query_params.append(('quote', params['quote']))  # noqa: E501

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
            '/v1/blocks/{level}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Block',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_get_by_level2(self, level, **kwargs):  # noqa: E501
        """Get timestamp by level  # noqa: E501

        Returns a timestamp of the block at the specified level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_level2(level, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int level: Block level (required)
        :return: datetime
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.blocks_get_by_level2_with_http_info(level, **kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_by_level2_with_http_info(level, **kwargs)  # noqa: E501
            return data

    def blocks_get_by_level2_with_http_info(self, level, **kwargs):  # noqa: E501
        """Get timestamp by level  # noqa: E501

        Returns a timestamp of the block at the specified level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_by_level2_with_http_info(level, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int level: Block level (required)
        :return: datetime
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['level']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get_by_level2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'level' is set
        if ('level' not in params or
                params['level'] is None):
            raise ValueError("Missing the required parameter `level` when calling `blocks_get_by_level2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'level' in params:
            path_params['level'] = params['level']  # noqa: E501

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
            '/v1/blocks/{level}/timestamp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='datetime',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_get_count(self, **kwargs):  # noqa: E501
        """Get blocks count  # noqa: E501

        Returns the total number of blocks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_count(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.blocks_get_count_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_count_with_http_info(**kwargs)  # noqa: E501
            return data

    def blocks_get_count_with_http_info(self, **kwargs):  # noqa: E501
        """Get blocks count  # noqa: E501

        Returns the total number of blocks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.blocks_get_count_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get_count" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/blocks/count', 'GET',
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
