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

class RelatedContract(object):
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
        'kind': 'str',
        'alias': 'str',
        'address': 'str',
        'balance': 'int',
        'delegate': 'OneOfRelatedContractDelegate',
        'creation_level': 'int',
        'creation_time': 'datetime'
    }

    attribute_map = {
        'kind': 'kind',
        'alias': 'alias',
        'address': 'address',
        'balance': 'balance',
        'delegate': 'delegate',
        'creation_level': 'creationLevel',
        'creation_time': 'creationTime'
    }

    def __init__(self, kind=None, alias=None, address=None, balance=None, delegate=None, creation_level=None, creation_time=None):  # noqa: E501
        """RelatedContract - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self._alias = None
        self._address = None
        self._balance = None
        self._delegate = None
        self._creation_level = None
        self._creation_time = None
        self.discriminator = None
        if kind is not None:
            self.kind = kind
        if alias is not None:
            self.alias = alias
        if address is not None:
            self.address = address
        if balance is not None:
            self.balance = balance
        if delegate is not None:
            self.delegate = delegate
        if creation_level is not None:
            self.creation_level = creation_level
        if creation_time is not None:
            self.creation_time = creation_time

    @property
    def kind(self):
        """Gets the kind of this RelatedContract.  # noqa: E501

        Kind of the contract (`delegator_contract` or `smart_contract`), where `delegator_contract` - manager.tz smart contract for delegation purpose only  # noqa: E501

        :return: The kind of this RelatedContract.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this RelatedContract.

        Kind of the contract (`delegator_contract` or `smart_contract`), where `delegator_contract` - manager.tz smart contract for delegation purpose only  # noqa: E501

        :param kind: The kind of this RelatedContract.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def alias(self):
        """Gets the alias of this RelatedContract.  # noqa: E501

        Name of the project behind the contract or contract description  # noqa: E501

        :return: The alias of this RelatedContract.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this RelatedContract.

        Name of the project behind the contract or contract description  # noqa: E501

        :param alias: The alias of this RelatedContract.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def address(self):
        """Gets the address of this RelatedContract.  # noqa: E501

        Public key hash of the contract  # noqa: E501

        :return: The address of this RelatedContract.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RelatedContract.

        Public key hash of the contract  # noqa: E501

        :param address: The address of this RelatedContract.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def balance(self):
        """Gets the balance of this RelatedContract.  # noqa: E501

        Contract balance (micro tez)  # noqa: E501

        :return: The balance of this RelatedContract.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this RelatedContract.

        Contract balance (micro tez)  # noqa: E501

        :param balance: The balance of this RelatedContract.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def delegate(self):
        """Gets the delegate of this RelatedContract.  # noqa: E501

        Information about the current delegate of the contract. `null` if it's not delegated  # noqa: E501

        :return: The delegate of this RelatedContract.  # noqa: E501
        :rtype: OneOfRelatedContractDelegate
        """
        return self._delegate

    @delegate.setter
    def delegate(self, delegate):
        """Sets the delegate of this RelatedContract.

        Information about the current delegate of the contract. `null` if it's not delegated  # noqa: E501

        :param delegate: The delegate of this RelatedContract.  # noqa: E501
        :type: OneOfRelatedContractDelegate
        """

        self._delegate = delegate

    @property
    def creation_level(self):
        """Gets the creation_level of this RelatedContract.  # noqa: E501

        Height of the block where the contract was created  # noqa: E501

        :return: The creation_level of this RelatedContract.  # noqa: E501
        :rtype: int
        """
        return self._creation_level

    @creation_level.setter
    def creation_level(self, creation_level):
        """Sets the creation_level of this RelatedContract.

        Height of the block where the contract was created  # noqa: E501

        :param creation_level: The creation_level of this RelatedContract.  # noqa: E501
        :type: int
        """

        self._creation_level = creation_level

    @property
    def creation_time(self):
        """Gets the creation_time of this RelatedContract.  # noqa: E501

        Datetime of the block where the contract was created (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The creation_time of this RelatedContract.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this RelatedContract.

        Datetime of the block where the contract was created (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param creation_time: The creation_time of this RelatedContract.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

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
        if issubclass(RelatedContract, dict):
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
        if not isinstance(other, RelatedContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other