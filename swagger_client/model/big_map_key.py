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

class BigMapKey(object):
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
        'id': 'int',
        'active': 'bool',
        'hash': 'str',
        'key': 'object',
        'value': 'object',
        'first_level': 'int',
        'last_level': 'int',
        'updates': 'int'
    }

    attribute_map = {
        'id': 'id',
        'active': 'active',
        'hash': 'hash',
        'key': 'key',
        'value': 'value',
        'first_level': 'firstLevel',
        'last_level': 'lastLevel',
        'updates': 'updates'
    }

    def __init__(self, id=None, active=None, hash=None, key=None, value=None, first_level=None, last_level=None, updates=None):  # noqa: E501
        """BigMapKey - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._active = None
        self._hash = None
        self._key = None
        self._value = None
        self._first_level = None
        self._last_level = None
        self._updates = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if hash is not None:
            self.hash = hash
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if first_level is not None:
            self.first_level = first_level
        if last_level is not None:
            self.last_level = last_level
        if updates is not None:
            self.updates = updates

    @property
    def id(self):
        """Gets the id of this BigMapKey.  # noqa: E501

        Internal Id, can be used for pagination  # noqa: E501

        :return: The id of this BigMapKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BigMapKey.

        Internal Id, can be used for pagination  # noqa: E501

        :param id: The id of this BigMapKey.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this BigMapKey.  # noqa: E501

        Bigmap key status (`true` - active, `false` - removed)  # noqa: E501

        :return: The active of this BigMapKey.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BigMapKey.

        Bigmap key status (`true` - active, `false` - removed)  # noqa: E501

        :param active: The active of this BigMapKey.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def hash(self):
        """Gets the hash of this BigMapKey.  # noqa: E501

        Key hash  # noqa: E501

        :return: The hash of this BigMapKey.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this BigMapKey.

        Key hash  # noqa: E501

        :param hash: The hash of this BigMapKey.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def key(self):
        """Gets the key of this BigMapKey.  # noqa: E501

        Key in JSON or Micheline format, depending on the `micheline` query parameter.  # noqa: E501

        :return: The key of this BigMapKey.  # noqa: E501
        :rtype: object
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this BigMapKey.

        Key in JSON or Micheline format, depending on the `micheline` query parameter.  # noqa: E501

        :param key: The key of this BigMapKey.  # noqa: E501
        :type: object
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this BigMapKey.  # noqa: E501

        Value in JSON or Micheline format, depending on the `micheline` query parameter. Note, if the key is inactive (removed) it will contain the last non-null value.  # noqa: E501

        :return: The value of this BigMapKey.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BigMapKey.

        Value in JSON or Micheline format, depending on the `micheline` query parameter. Note, if the key is inactive (removed) it will contain the last non-null value.  # noqa: E501

        :param value: The value of this BigMapKey.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def first_level(self):
        """Gets the first_level of this BigMapKey.  # noqa: E501

        Level of the block where the bigmap key was seen first time  # noqa: E501

        :return: The first_level of this BigMapKey.  # noqa: E501
        :rtype: int
        """
        return self._first_level

    @first_level.setter
    def first_level(self, first_level):
        """Sets the first_level of this BigMapKey.

        Level of the block where the bigmap key was seen first time  # noqa: E501

        :param first_level: The first_level of this BigMapKey.  # noqa: E501
        :type: int
        """

        self._first_level = first_level

    @property
    def last_level(self):
        """Gets the last_level of this BigMapKey.  # noqa: E501

        Level of the block where the bigmap key was seen last time  # noqa: E501

        :return: The last_level of this BigMapKey.  # noqa: E501
        :rtype: int
        """
        return self._last_level

    @last_level.setter
    def last_level(self, last_level):
        """Sets the last_level of this BigMapKey.

        Level of the block where the bigmap key was seen last time  # noqa: E501

        :param last_level: The last_level of this BigMapKey.  # noqa: E501
        :type: int
        """

        self._last_level = last_level

    @property
    def updates(self):
        """Gets the updates of this BigMapKey.  # noqa: E501

        Total number of actions with the bigmap key  # noqa: E501

        :return: The updates of this BigMapKey.  # noqa: E501
        :rtype: int
        """
        return self._updates

    @updates.setter
    def updates(self, updates):
        """Sets the updates of this BigMapKey.

        Total number of actions with the bigmap key  # noqa: E501

        :param updates: The updates of this BigMapKey.  # noqa: E501
        :type: int
        """

        self._updates = updates

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
        if issubclass(BigMapKey, dict):
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
        if not isinstance(other, BigMapKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other