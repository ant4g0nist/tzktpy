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

class Commitment(object):
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
        'address': 'str',
        'balance': 'int',
        'activated': 'bool',
        'activation_level': 'int',
        'activation_time': 'datetime',
        'activated_account': 'OneOfCommitmentActivatedAccount'
    }

    attribute_map = {
        'address': 'address',
        'balance': 'balance',
        'activated': 'activated',
        'activation_level': 'activationLevel',
        'activation_time': 'activationTime',
        'activated_account': 'activatedAccount'
    }

    def __init__(self, address=None, balance=None, activated=None, activation_level=None, activation_time=None, activated_account=None):  # noqa: E501
        """Commitment - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._balance = None
        self._activated = None
        self._activation_level = None
        self._activation_time = None
        self._activated_account = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if balance is not None:
            self.balance = balance
        if activated is not None:
            self.activated = activated
        if activation_level is not None:
            self.activation_level = activation_level
        if activation_time is not None:
            self.activation_time = activation_time
        if activated_account is not None:
            self.activated_account = activated_account

    @property
    def address(self):
        """Gets the address of this Commitment.  # noqa: E501

        Blinded address of the account  # noqa: E501

        :return: The address of this Commitment.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Commitment.

        Blinded address of the account  # noqa: E501

        :param address: The address of this Commitment.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def balance(self):
        """Gets the balance of this Commitment.  # noqa: E501

        Account balance to be activated  # noqa: E501

        :return: The balance of this Commitment.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Commitment.

        Account balance to be activated  # noqa: E501

        :param balance: The balance of this Commitment.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def activated(self):
        """Gets the activated of this Commitment.  # noqa: E501

        Flag showing whether the account has been activated or not.  # noqa: E501

        :return: The activated of this Commitment.  # noqa: E501
        :rtype: bool
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this Commitment.

        Flag showing whether the account has been activated or not.  # noqa: E501

        :param activated: The activated of this Commitment.  # noqa: E501
        :type: bool
        """

        self._activated = activated

    @property
    def activation_level(self):
        """Gets the activation_level of this Commitment.  # noqa: E501

        Level of the block at which the account has been activated. `null` if the account is not activated yet.  # noqa: E501

        :return: The activation_level of this Commitment.  # noqa: E501
        :rtype: int
        """
        return self._activation_level

    @activation_level.setter
    def activation_level(self, activation_level):
        """Sets the activation_level of this Commitment.

        Level of the block at which the account has been activated. `null` if the account is not activated yet.  # noqa: E501

        :param activation_level: The activation_level of this Commitment.  # noqa: E501
        :type: int
        """

        self._activation_level = activation_level

    @property
    def activation_time(self):
        """Gets the activation_time of this Commitment.  # noqa: E501

        Datetime of the block at which the account has been activated (ISO 8601, e.g. `2020-02-20T02:40:57Z`). `null` if the account is not activated yet.  # noqa: E501

        :return: The activation_time of this Commitment.  # noqa: E501
        :rtype: datetime
        """
        return self._activation_time

    @activation_time.setter
    def activation_time(self, activation_time):
        """Sets the activation_time of this Commitment.

        Datetime of the block at which the account has been activated (ISO 8601, e.g. `2020-02-20T02:40:57Z`). `null` if the account is not activated yet.  # noqa: E501

        :param activation_time: The activation_time of this Commitment.  # noqa: E501
        :type: datetime
        """

        self._activation_time = activation_time

    @property
    def activated_account(self):
        """Gets the activated_account of this Commitment.  # noqa: E501

        Info about activated account. `null` if the account is not activated yet.  # noqa: E501

        :return: The activated_account of this Commitment.  # noqa: E501
        :rtype: OneOfCommitmentActivatedAccount
        """
        return self._activated_account

    @activated_account.setter
    def activated_account(self, activated_account):
        """Sets the activated_account of this Commitment.

        Info about activated account. `null` if the account is not activated yet.  # noqa: E501

        :param activated_account: The activated_account of this Commitment.  # noqa: E501
        :type: OneOfCommitmentActivatedAccount
        """

        self._activated_account = activated_account

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
        if issubclass(Commitment, dict):
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
        if not isinstance(other, Commitment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
