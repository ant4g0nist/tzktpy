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

class BigMap(object):
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
        'ptr': 'int',
        'contract': 'OneOfBigMapContract',
        'path': 'str',
        'tags': 'list[str]',
        'active': 'bool',
        'first_level': 'int',
        'last_level': 'int',
        'total_keys': 'int',
        'active_keys': 'int',
        'updates': 'int',
        'key_type': 'object',
        'value_type': 'object'
    }

    attribute_map = {
        'ptr': 'ptr',
        'contract': 'contract',
        'path': 'path',
        'tags': 'tags',
        'active': 'active',
        'first_level': 'firstLevel',
        'last_level': 'lastLevel',
        'total_keys': 'totalKeys',
        'active_keys': 'activeKeys',
        'updates': 'updates',
        'key_type': 'keyType',
        'value_type': 'valueType'
    }

    def __init__(self, ptr=None, contract=None, path=None, tags=None, active=None, first_level=None, last_level=None, total_keys=None, active_keys=None, updates=None, key_type=None, value_type=None):  # noqa: E501
        """BigMap - a model defined in Swagger"""  # noqa: E501
        self._ptr = None
        self._contract = None
        self._path = None
        self._tags = None
        self._active = None
        self._first_level = None
        self._last_level = None
        self._total_keys = None
        self._active_keys = None
        self._updates = None
        self._key_type = None
        self._value_type = None
        self.discriminator = None
        if ptr is not None:
            self.ptr = ptr
        if contract is not None:
            self.contract = contract
        if path is not None:
            self.path = path
        if tags is not None:
            self.tags = tags
        if active is not None:
            self.active = active
        if first_level is not None:
            self.first_level = first_level
        if last_level is not None:
            self.last_level = last_level
        if total_keys is not None:
            self.total_keys = total_keys
        if active_keys is not None:
            self.active_keys = active_keys
        if updates is not None:
            self.updates = updates
        if key_type is not None:
            self.key_type = key_type
        if value_type is not None:
            self.value_type = value_type

    @property
    def ptr(self):
        """Gets the ptr of this BigMap.  # noqa: E501

        Bigmap pointer  # noqa: E501

        :return: The ptr of this BigMap.  # noqa: E501
        :rtype: int
        """
        return self._ptr

    @ptr.setter
    def ptr(self, ptr):
        """Sets the ptr of this BigMap.

        Bigmap pointer  # noqa: E501

        :param ptr: The ptr of this BigMap.  # noqa: E501
        :type: int
        """

        self._ptr = ptr

    @property
    def contract(self):
        """Gets the contract of this BigMap.  # noqa: E501

        Smart contract in which's storage the bigmap is allocated  # noqa: E501

        :return: The contract of this BigMap.  # noqa: E501
        :rtype: OneOfBigMapContract
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this BigMap.

        Smart contract in which's storage the bigmap is allocated  # noqa: E501

        :param contract: The contract of this BigMap.  # noqa: E501
        :type: OneOfBigMapContract
        """

        self._contract = contract

    @property
    def path(self):
        """Gets the path of this BigMap.  # noqa: E501

        Path to the bigmap in the contract storage   # noqa: E501

        :return: The path of this BigMap.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BigMap.

        Path to the bigmap in the contract storage   # noqa: E501

        :param path: The path of this BigMap.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def tags(self):
        """Gets the tags of this BigMap.  # noqa: E501

        List of tags ( `metadata`, `token_metadata`,`ledger`, or `null` if there are no tags)  # noqa: E501

        :return: The tags of this BigMap.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BigMap.

        List of tags ( `metadata`, `token_metadata`,`ledger`, or `null` if there are no tags)  # noqa: E501

        :param tags: The tags of this BigMap.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def active(self):
        """Gets the active of this BigMap.  # noqa: E501

        Bigmap status (`true` - active, `false` - removed)  # noqa: E501

        :return: The active of this BigMap.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BigMap.

        Bigmap status (`true` - active, `false` - removed)  # noqa: E501

        :param active: The active of this BigMap.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def first_level(self):
        """Gets the first_level of this BigMap.  # noqa: E501

        Level of the block where the bigmap was seen first time  # noqa: E501

        :return: The first_level of this BigMap.  # noqa: E501
        :rtype: int
        """
        return self._first_level

    @first_level.setter
    def first_level(self, first_level):
        """Sets the first_level of this BigMap.

        Level of the block where the bigmap was seen first time  # noqa: E501

        :param first_level: The first_level of this BigMap.  # noqa: E501
        :type: int
        """

        self._first_level = first_level

    @property
    def last_level(self):
        """Gets the last_level of this BigMap.  # noqa: E501

        Level of the block where the bigmap was seen last time  # noqa: E501

        :return: The last_level of this BigMap.  # noqa: E501
        :rtype: int
        """
        return self._last_level

    @last_level.setter
    def last_level(self, last_level):
        """Sets the last_level of this BigMap.

        Level of the block where the bigmap was seen last time  # noqa: E501

        :param last_level: The last_level of this BigMap.  # noqa: E501
        :type: int
        """

        self._last_level = last_level

    @property
    def total_keys(self):
        """Gets the total_keys of this BigMap.  # noqa: E501

        Total number of keys ever added to the bigmap  # noqa: E501

        :return: The total_keys of this BigMap.  # noqa: E501
        :rtype: int
        """
        return self._total_keys

    @total_keys.setter
    def total_keys(self, total_keys):
        """Sets the total_keys of this BigMap.

        Total number of keys ever added to the bigmap  # noqa: E501

        :param total_keys: The total_keys of this BigMap.  # noqa: E501
        :type: int
        """

        self._total_keys = total_keys

    @property
    def active_keys(self):
        """Gets the active_keys of this BigMap.  # noqa: E501

        Total number of currently active keys  # noqa: E501

        :return: The active_keys of this BigMap.  # noqa: E501
        :rtype: int
        """
        return self._active_keys

    @active_keys.setter
    def active_keys(self, active_keys):
        """Sets the active_keys of this BigMap.

        Total number of currently active keys  # noqa: E501

        :param active_keys: The active_keys of this BigMap.  # noqa: E501
        :type: int
        """

        self._active_keys = active_keys

    @property
    def updates(self):
        """Gets the updates of this BigMap.  # noqa: E501

        Total number of actions with the bigmap  # noqa: E501

        :return: The updates of this BigMap.  # noqa: E501
        :rtype: int
        """
        return self._updates

    @updates.setter
    def updates(self, updates):
        """Sets the updates of this BigMap.

        Total number of actions with the bigmap  # noqa: E501

        :param updates: The updates of this BigMap.  # noqa: E501
        :type: int
        """

        self._updates = updates

    @property
    def key_type(self):
        """Gets the key_type of this BigMap.  # noqa: E501

        Bigmap key type as JSON schema or Micheline, depending on the `micheline` query parameter.  # noqa: E501

        :return: The key_type of this BigMap.  # noqa: E501
        :rtype: object
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this BigMap.

        Bigmap key type as JSON schema or Micheline, depending on the `micheline` query parameter.  # noqa: E501

        :param key_type: The key_type of this BigMap.  # noqa: E501
        :type: object
        """

        self._key_type = key_type

    @property
    def value_type(self):
        """Gets the value_type of this BigMap.  # noqa: E501

        Bigmap value type as JSON schema or Micheline, depending on the `micheline` query parameter.  # noqa: E501

        :return: The value_type of this BigMap.  # noqa: E501
        :rtype: object
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this BigMap.

        Bigmap value type as JSON schema or Micheline, depending on the `micheline` query parameter.  # noqa: E501

        :param value_type: The value_type of this BigMap.  # noqa: E501
        :type: object
        """

        self._value_type = value_type

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
        if issubclass(BigMap, dict):
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
        if not isinstance(other, BigMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
