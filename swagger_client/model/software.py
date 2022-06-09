# coding: utf-8

"""
    TzKT API

    # Introduction  TzKT Explorer provides free REST API and WebSocket API for accessing detailed Tezos blockchain data and helps developers build more services and applications on top of Tezos. TzKT is an open-source project, so you can easily clone and build it and use it as a self-hosted service to avoid any risks of depending on third-party services.  TzKT API is available for the following Tezos networks with the following base URLs:  - Mainnet: `https://api.tzkt.io/` or `https://api.mainnet.tzkt.io/` ([view docs](https://api.tzkt.io))  - Hangzhounet: `https://api.hangzhounet.tzkt.io/` ([view docs](https://api.hangzhounet.tzkt.io)) - Ithacanet: `https://api.ithacanet.tzkt.io/` ([view docs](https://api.ithacanet.tzkt.io))  We also provide a staging environment for testing newest features and pre-updating client applications before deploying to production:  - Mainnet staging: `https://staging.api.tzkt.io/` or `https://staging.api.mainnet.tzkt.io/` ([view docs](https://staging.api.tzkt.io))  Feel free to contact us if you have any questions or feature requests. Your feedback really helps us make TzKT better!  - Discord: https://discord.gg/aG8XKuwsQd - Telegram: https://t.me/baking_bad_chat - Slack: https://tezos-dev.slack.com/archives/CV5NX7F2L - Twitter: https://twitter.com/TezosBakingBad - Email: hello@baking-bad.org  And don't forget to star TzKT project [on GitHub](https://github.com/baking-bad/tzkt) ;)  # Terms of Use  TzKT API is free for everyone and for both commercial and non-commercial usage.  If your application or service uses the TzKT API in any forms: directly on frontend or indirectly on backend, you must mention that fact on your website or application by placing the label **\"Powered by TzKT API\"** or **\"Built with TzKT API\"** with a direct link to [tzkt.io](https://tzkt.io).   # Rate Limits  There will be no rate limits as long as our servers can handle the load without additional infrastructure costs. However, any apparent abuse will be prevented by setting targeted rate limits.  Check out [Tezos Explorer API Best Practices](https://baking-bad.org/blog/tag/TzKT/) and in particular [how to optimize requests count](https://baking-bad.org/blog/2020/07/29/tezos-explorer-api-tzkt-how-often-to-make-requests/).  ---   # noqa: E501

    OpenAPI spec version: v1.8.3
    Contact: hello@baking-bad.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Software(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'short_hash': 'str',
        'first_level': 'int',
        'first_time': 'datetime',
        'last_level': 'int',
        'last_time': 'datetime',
        'blocks_count': 'int',
        'metadata': 'OneOfSoftwareMetadata'
    }

    attribute_map = {
        'short_hash': 'shortHash',
        'first_level': 'firstLevel',
        'first_time': 'firstTime',
        'last_level': 'lastLevel',
        'last_time': 'lastTime',
        'blocks_count': 'blocksCount',
        'metadata': 'metadata'
    }

    def __init__(self, short_hash=None, first_level=None, first_time=None, last_level=None, last_time=None, blocks_count=None, metadata=None):  # noqa: E501
        """Software - a model defined in Swagger"""  # noqa: E501
        self._short_hash = None
        self._first_level = None
        self._first_time = None
        self._last_level = None
        self._last_time = None
        self._blocks_count = None
        self._metadata = None
        self.discriminator = None
        if short_hash is not None:
            self.short_hash = short_hash
        if first_level is not None:
            self.first_level = first_level
        if first_time is not None:
            self.first_time = first_time
        if last_level is not None:
            self.last_level = last_level
        if last_time is not None:
            self.last_time = last_time
        if blocks_count is not None:
            self.blocks_count = blocks_count
        if metadata is not None:
            self.metadata = metadata

    @property
    def short_hash(self):
        """Gets the short_hash of this Software.  # noqa: E501

        Software ID (short commit hash)  # noqa: E501

        :return: The short_hash of this Software.  # noqa: E501
        :rtype: str
        """
        return self._short_hash

    @short_hash.setter
    def short_hash(self, short_hash):
        """Sets the short_hash of this Software.

        Software ID (short commit hash)  # noqa: E501

        :param short_hash: The short_hash of this Software.  # noqa: E501
        :type: str
        """

        self._short_hash = short_hash

    @property
    def first_level(self):
        """Gets the first_level of this Software.  # noqa: E501

        Level of the first block baked with this software  # noqa: E501

        :return: The first_level of this Software.  # noqa: E501
        :rtype: int
        """
        return self._first_level

    @first_level.setter
    def first_level(self, first_level):
        """Sets the first_level of this Software.

        Level of the first block baked with this software  # noqa: E501

        :param first_level: The first_level of this Software.  # noqa: E501
        :type: int
        """

        self._first_level = first_level

    @property
    def first_time(self):
        """Gets the first_time of this Software.  # noqa: E501

        Datetime of the first block baked with this software  # noqa: E501

        :return: The first_time of this Software.  # noqa: E501
        :rtype: datetime
        """
        return self._first_time

    @first_time.setter
    def first_time(self, first_time):
        """Sets the first_time of this Software.

        Datetime of the first block baked with this software  # noqa: E501

        :param first_time: The first_time of this Software.  # noqa: E501
        :type: datetime
        """

        self._first_time = first_time

    @property
    def last_level(self):
        """Gets the last_level of this Software.  # noqa: E501

        Level of the last block baked with this software  # noqa: E501

        :return: The last_level of this Software.  # noqa: E501
        :rtype: int
        """
        return self._last_level

    @last_level.setter
    def last_level(self, last_level):
        """Sets the last_level of this Software.

        Level of the last block baked with this software  # noqa: E501

        :param last_level: The last_level of this Software.  # noqa: E501
        :type: int
        """

        self._last_level = last_level

    @property
    def last_time(self):
        """Gets the last_time of this Software.  # noqa: E501

        Datetime of the last block baked with this software  # noqa: E501

        :return: The last_time of this Software.  # noqa: E501
        :rtype: datetime
        """
        return self._last_time

    @last_time.setter
    def last_time(self, last_time):
        """Sets the last_time of this Software.

        Datetime of the last block baked with this software  # noqa: E501

        :param last_time: The last_time of this Software.  # noqa: E501
        :type: datetime
        """

        self._last_time = last_time

    @property
    def blocks_count(self):
        """Gets the blocks_count of this Software.  # noqa: E501

        Total number of blocks baked with this software  # noqa: E501

        :return: The blocks_count of this Software.  # noqa: E501
        :rtype: int
        """
        return self._blocks_count

    @blocks_count.setter
    def blocks_count(self, blocks_count):
        """Sets the blocks_count of this Software.

        Total number of blocks baked with this software  # noqa: E501

        :param blocks_count: The blocks_count of this Software.  # noqa: E501
        :type: int
        """

        self._blocks_count = blocks_count

    @property
    def metadata(self):
        """Gets the metadata of this Software.  # noqa: E501

        Offchain metadata  # noqa: E501

        :return: The metadata of this Software.  # noqa: E501
        :rtype: OneOfSoftwareMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Software.

        Offchain metadata  # noqa: E501

        :param metadata: The metadata of this Software.  # noqa: E501
        :type: OneOfSoftwareMetadata
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Software, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Software):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other