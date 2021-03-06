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
from swagger_client.model.account import Account  # noqa: F401,E501

class Ghost(Account):
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
        'address': 'str',
        'alias': 'str',
        'active_tokens_count': 'int',
        'token_balances_count': 'int',
        'token_transfers_count': 'int',
        'first_activity': 'int',
        'first_activity_time': 'datetime',
        'last_activity': 'int',
        'last_activity_time': 'datetime',
        'metadata': 'object'
    }
    if hasattr(Account, "swagger_types"):
        swagger_types.update(Account.swagger_types)

    attribute_map = {
        'type': 'type',
        'address': 'address',
        'alias': 'alias',
        'active_tokens_count': 'activeTokensCount',
        'token_balances_count': 'tokenBalancesCount',
        'token_transfers_count': 'tokenTransfersCount',
        'first_activity': 'firstActivity',
        'first_activity_time': 'firstActivityTime',
        'last_activity': 'lastActivity',
        'last_activity_time': 'lastActivityTime',
        'metadata': 'metadata'
    }
    if hasattr(Account, "attribute_map"):
        attribute_map.update(Account.attribute_map)

    def __init__(self, type=None, address=None, alias=None, active_tokens_count=None, token_balances_count=None, token_transfers_count=None, first_activity=None, first_activity_time=None, last_activity=None, last_activity_time=None, metadata=None, *args, **kwargs):  # noqa: E501
        """Ghost - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._address = None
        self._alias = None
        self._active_tokens_count = None
        self._token_balances_count = None
        self._token_transfers_count = None
        self._first_activity = None
        self._first_activity_time = None
        self._last_activity = None
        self._last_activity_time = None
        self._metadata = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if address is not None:
            self.address = address
        if alias is not None:
            self.alias = alias
        if active_tokens_count is not None:
            self.active_tokens_count = active_tokens_count
        if token_balances_count is not None:
            self.token_balances_count = token_balances_count
        if token_transfers_count is not None:
            self.token_transfers_count = token_transfers_count
        if first_activity is not None:
            self.first_activity = first_activity
        if first_activity_time is not None:
            self.first_activity_time = first_activity_time
        if last_activity is not None:
            self.last_activity = last_activity
        if last_activity_time is not None:
            self.last_activity_time = last_activity_time
        if metadata is not None:
            self.metadata = metadata
        Account.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this Ghost.  # noqa: E501

        Type of the account, `ghost` - contract that has been met among token holders, but hasn't been originated  # noqa: E501

        :return: The type of this Ghost.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Ghost.

        Type of the account, `ghost` - contract that has been met among token holders, but hasn't been originated  # noqa: E501

        :param type: The type of this Ghost.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def address(self):
        """Gets the address of this Ghost.  # noqa: E501

        Address of the contract  # noqa: E501

        :return: The address of this Ghost.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Ghost.

        Address of the contract  # noqa: E501

        :param address: The address of this Ghost.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def alias(self):
        """Gets the alias of this Ghost.  # noqa: E501

        Name of the ghost contract  # noqa: E501

        :return: The alias of this Ghost.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Ghost.

        Name of the ghost contract  # noqa: E501

        :param alias: The alias of this Ghost.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def active_tokens_count(self):
        """Gets the active_tokens_count of this Ghost.  # noqa: E501

        Number of account tokens with non-zero balances  # noqa: E501

        :return: The active_tokens_count of this Ghost.  # noqa: E501
        :rtype: int
        """
        return self._active_tokens_count

    @active_tokens_count.setter
    def active_tokens_count(self, active_tokens_count):
        """Sets the active_tokens_count of this Ghost.

        Number of account tokens with non-zero balances  # noqa: E501

        :param active_tokens_count: The active_tokens_count of this Ghost.  # noqa: E501
        :type: int
        """

        self._active_tokens_count = active_tokens_count

    @property
    def token_balances_count(self):
        """Gets the token_balances_count of this Ghost.  # noqa: E501

        Number of tokens the account ever had  # noqa: E501

        :return: The token_balances_count of this Ghost.  # noqa: E501
        :rtype: int
        """
        return self._token_balances_count

    @token_balances_count.setter
    def token_balances_count(self, token_balances_count):
        """Sets the token_balances_count of this Ghost.

        Number of tokens the account ever had  # noqa: E501

        :param token_balances_count: The token_balances_count of this Ghost.  # noqa: E501
        :type: int
        """

        self._token_balances_count = token_balances_count

    @property
    def token_transfers_count(self):
        """Gets the token_transfers_count of this Ghost.  # noqa: E501

        Number of token transfers from/to the account  # noqa: E501

        :return: The token_transfers_count of this Ghost.  # noqa: E501
        :rtype: int
        """
        return self._token_transfers_count

    @token_transfers_count.setter
    def token_transfers_count(self, token_transfers_count):
        """Sets the token_transfers_count of this Ghost.

        Number of token transfers from/to the account  # noqa: E501

        :param token_transfers_count: The token_transfers_count of this Ghost.  # noqa: E501
        :type: int
        """

        self._token_transfers_count = token_transfers_count

    @property
    def first_activity(self):
        """Gets the first_activity of this Ghost.  # noqa: E501

        Block height at which the ghost contract appeared first time  # noqa: E501

        :return: The first_activity of this Ghost.  # noqa: E501
        :rtype: int
        """
        return self._first_activity

    @first_activity.setter
    def first_activity(self, first_activity):
        """Sets the first_activity of this Ghost.

        Block height at which the ghost contract appeared first time  # noqa: E501

        :param first_activity: The first_activity of this Ghost.  # noqa: E501
        :type: int
        """

        self._first_activity = first_activity

    @property
    def first_activity_time(self):
        """Gets the first_activity_time of this Ghost.  # noqa: E501

        Block datetime at which the ghost contract appeared first time (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The first_activity_time of this Ghost.  # noqa: E501
        :rtype: datetime
        """
        return self._first_activity_time

    @first_activity_time.setter
    def first_activity_time(self, first_activity_time):
        """Sets the first_activity_time of this Ghost.

        Block datetime at which the ghost contract appeared first time (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param first_activity_time: The first_activity_time of this Ghost.  # noqa: E501
        :type: datetime
        """

        self._first_activity_time = first_activity_time

    @property
    def last_activity(self):
        """Gets the last_activity of this Ghost.  # noqa: E501

        Height of the block in which the ghost contract state was changed last time  # noqa: E501

        :return: The last_activity of this Ghost.  # noqa: E501
        :rtype: int
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """Sets the last_activity of this Ghost.

        Height of the block in which the ghost contract state was changed last time  # noqa: E501

        :param last_activity: The last_activity of this Ghost.  # noqa: E501
        :type: int
        """

        self._last_activity = last_activity

    @property
    def last_activity_time(self):
        """Gets the last_activity_time of this Ghost.  # noqa: E501

        Datetime of the block in which the ghost contract state was changed last time (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The last_activity_time of this Ghost.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity_time

    @last_activity_time.setter
    def last_activity_time(self, last_activity_time):
        """Sets the last_activity_time of this Ghost.

        Datetime of the block in which the ghost contract state was changed last time (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param last_activity_time: The last_activity_time of this Ghost.  # noqa: E501
        :type: datetime
        """

        self._last_activity_time = last_activity_time

    @property
    def metadata(self):
        """Gets the metadata of this Ghost.  # noqa: E501

        Metadata of the ghost contract (alias, logo, website, contacts, etc)  # noqa: E501

        :return: The metadata of this Ghost.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Ghost.

        Metadata of the ghost contract (alias, logo, website, contacts, etc)  # noqa: E501

        :param metadata: The metadata of this Ghost.  # noqa: E501
        :type: object
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
        if issubclass(Ghost, dict):
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
        if not isinstance(other, Ghost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
