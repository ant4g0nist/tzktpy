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

class Delegator(object):
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
        'type': 'str',
        'alias': 'str',
        'address': 'str',
        'balance': 'int',
        'delegation_level': 'int',
        'delegation_time': 'datetime'
    }

    attribute_map = {
        'type': 'type',
        'alias': 'alias',
        'address': 'address',
        'balance': 'balance',
        'delegation_level': 'delegationLevel',
        'delegation_time': 'delegationTime'
    }

    def __init__(self, type=None, alias=None, address=None, balance=None, delegation_level=None, delegation_time=None):  # noqa: E501
        """Delegator - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._alias = None
        self._address = None
        self._balance = None
        self._delegation_level = None
        self._delegation_time = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if alias is not None:
            self.alias = alias
        if address is not None:
            self.address = address
        if balance is not None:
            self.balance = balance
        if delegation_level is not None:
            self.delegation_level = delegation_level
        if delegation_time is not None:
            self.delegation_time = delegation_time

    @property
    def type(self):
        """Gets the type of this Delegator.  # noqa: E501

        Delegator type ('contract' for KT.. address or 'user' for tz.. address)  # noqa: E501

        :return: The type of this Delegator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Delegator.

        Delegator type ('contract' for KT.. address or 'user' for tz.. address)  # noqa: E501

        :param type: The type of this Delegator.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def alias(self):
        """Gets the alias of this Delegator.  # noqa: E501

        Name of the project behind the account or account description  # noqa: E501

        :return: The alias of this Delegator.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Delegator.

        Name of the project behind the account or account description  # noqa: E501

        :param alias: The alias of this Delegator.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def address(self):
        """Gets the address of this Delegator.  # noqa: E501

        Public key hash of the account  # noqa: E501

        :return: The address of this Delegator.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Delegator.

        Public key hash of the account  # noqa: E501

        :param address: The address of this Delegator.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def balance(self):
        """Gets the balance of this Delegator.  # noqa: E501

        Account balance (micro tez)  # noqa: E501

        :return: The balance of this Delegator.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Delegator.

        Account balance (micro tez)  # noqa: E501

        :param balance: The balance of this Delegator.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def delegation_level(self):
        """Gets the delegation_level of this Delegator.  # noqa: E501

        Block height of last delegation operation  # noqa: E501

        :return: The delegation_level of this Delegator.  # noqa: E501
        :rtype: int
        """
        return self._delegation_level

    @delegation_level.setter
    def delegation_level(self, delegation_level):
        """Sets the delegation_level of this Delegator.

        Block height of last delegation operation  # noqa: E501

        :param delegation_level: The delegation_level of this Delegator.  # noqa: E501
        :type: int
        """

        self._delegation_level = delegation_level

    @property
    def delegation_time(self):
        """Gets the delegation_time of this Delegator.  # noqa: E501

        Block datetime of last delegation operation (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The delegation_time of this Delegator.  # noqa: E501
        :rtype: datetime
        """
        return self._delegation_time

    @delegation_time.setter
    def delegation_time(self, delegation_time):
        """Sets the delegation_time of this Delegator.

        Block datetime of last delegation operation (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param delegation_time: The delegation_time of this Delegator.  # noqa: E501
        :type: datetime
        """

        self._delegation_time = delegation_time

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
        if issubclass(Delegator, dict):
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
        if not isinstance(other, Delegator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
