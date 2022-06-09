# coding: utf-8

"""
    TzKT API

    # Introduction  TzKT Explorer provides free REST API and WebSocket API for accessing detailed Tezos blockchain data and helps developers build more services and applications on top of Tezos. TzKT is an open-source project, so you can easily clone and build it and use it as a self-hosted service to avoid any risks of depending on third-party services.  TzKT API is available for the following Tezos networks with the following base URLs:  - Mainnet: `https://api.tzkt.io/` or `https://api.mainnet.tzkt.io/` ([view docs](https://api.tzkt.io))  - Hangzhounet: `https://api.hangzhounet.tzkt.io/` ([view docs](https://api.hangzhounet.tzkt.io)) - Ithacanet: `https://api.ithacanet.tzkt.io/` ([view docs](https://api.ithacanet.tzkt.io))  We also provide a staging environment for testing newest features and pre-updating client applications before deploying to production:  - Mainnet staging: `https://staging.api.tzkt.io/` or `https://staging.api.mainnet.tzkt.io/` ([view docs](https://staging.api.tzkt.io))  Feel free to contact us if you have any questions or feature requests. Your feedback really helps us make TzKT better!  - Discord: https://discord.gg/aG8XKuwsQd - Telegram: https://t.me/baking_bad_chat - Slack: https://tezos-dev.slack.com/archives/CV5NX7F2L - Twitter: https://twitter.com/TezosBakingBad - Email: hello@baking-bad.org  And don't forget to star TzKT project [on GitHub](https://github.com/baking-bad/tzkt) ;)  # Terms of Use  TzKT API is free for everyone and for both commercial and non-commercial usage.  If your application or service uses the TzKT API in any forms: directly on frontend or indirectly on backend, you must mention that fact on your website or application by placing the label **\"Powered by TzKT API\"** or **\"Built with TzKT API\"** with a direct link to [tzkt.io](https://tzkt.io).   # Rate Limits  There will be no rate limits as long as our servers can handle the load without additional infrastructure costs. However, any apparent abuse will be prevented by setting targeted rate limits.  Check out [Tezos Explorer API Best Practices](https://baking-bad.org/blog/tag/TzKT/) and in particular [how to optimize requests count](https://baking-bad.org/blog/2020/07/29/tezos-explorer-api-tzkt-how-often-to-make-requests/).  ---   # noqa: E501

    OpenAPI spec version: v1.8.3
    Contact: hello@baking-bad.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.tzktpy.blocks_api import BlocksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBlocksApi(unittest.TestCase):
    """BlocksApi unit test stubs"""

    def setUp(self):
        self.api = BlocksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_blocks_get(self):
        """Test case for blocks_get

        Get blocks  # noqa: E501
        """
        pass

    def test_blocks_get_by_date(self):
        """Test case for blocks_get_by_date

        Get block by timestamp  # noqa: E501
        """
        pass

    def test_blocks_get_by_date2(self):
        """Test case for blocks_get_by_date2

        Get level by timestamp  # noqa: E501
        """
        pass

    def test_blocks_get_by_hash(self):
        """Test case for blocks_get_by_hash

        Get block by hash  # noqa: E501
        """
        pass

    def test_blocks_get_by_level(self):
        """Test case for blocks_get_by_level

        Get block by level  # noqa: E501
        """
        pass

    def test_blocks_get_by_level2(self):
        """Test case for blocks_get_by_level2

        Get timestamp by level  # noqa: E501
        """
        pass

    def test_blocks_get_count(self):
        """Test case for blocks_get_count

        Get blocks count  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
