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

class NatParameter(object):
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
        'eq': 'str',
        'ne': 'str',
        'gt': 'str',
        'ge': 'str',
        'lt': 'str',
        'le': 'str',
        '_in': 'list[str]',
        'ni': 'list[str]'
    }

    attribute_map = {
        'eq': 'eq',
        'ne': 'ne',
        'gt': 'gt',
        'ge': 'ge',
        'lt': 'lt',
        'le': 'le',
        '_in': 'in',
        'ni': 'ni'
    }

    def __init__(self, eq=None, ne=None, gt=None, ge=None, lt=None, le=None, _in=None, ni=None):  # noqa: E501
        """NatParameter - a model defined in Swagger"""  # noqa: E501
        self._eq = None
        self._ne = None
        self._gt = None
        self._ge = None
        self._lt = None
        self._le = None
        self.__in = None
        self._ni = None
        self.discriminator = None
        if eq is not None:
            self.eq = eq
        if ne is not None:
            self.ne = ne
        if gt is not None:
            self.gt = gt
        if ge is not None:
            self.ge = ge
        if lt is not None:
            self.lt = lt
        if le is not None:
            self.le = le
        if _in is not None:
            self._in = _in
        if ni is not None:
            self.ni = ni

    @property
    def eq(self):
        """Gets the eq of this NatParameter.  # noqa: E501

        **Equal** filter mode (optional, i.e. `param.eq=123` is the same as `param=123`). \\ Specify a `nat` value to get items where the specified field is equal to the specified value.  Example: `?balance=1234`.  # noqa: E501

        :return: The eq of this NatParameter.  # noqa: E501
        :rtype: str
        """
        return self._eq

    @eq.setter
    def eq(self, eq):
        """Sets the eq of this NatParameter.

        **Equal** filter mode (optional, i.e. `param.eq=123` is the same as `param=123`). \\ Specify a `nat` value to get items where the specified field is equal to the specified value.  Example: `?balance=1234`.  # noqa: E501

        :param eq: The eq of this NatParameter.  # noqa: E501
        :type: str
        """

        self._eq = eq

    @property
    def ne(self):
        """Gets the ne of this NatParameter.  # noqa: E501

        **Not equal** filter mode. \\ Specify a `nat` value to get items where the specified field is not equal to the specified value.  Example: `?balance.ne=1234`.  # noqa: E501

        :return: The ne of this NatParameter.  # noqa: E501
        :rtype: str
        """
        return self._ne

    @ne.setter
    def ne(self, ne):
        """Sets the ne of this NatParameter.

        **Not equal** filter mode. \\ Specify a `nat` value to get items where the specified field is not equal to the specified value.  Example: `?balance.ne=1234`.  # noqa: E501

        :param ne: The ne of this NatParameter.  # noqa: E501
        :type: str
        """

        self._ne = ne

    @property
    def gt(self):
        """Gets the gt of this NatParameter.  # noqa: E501

        **Greater than** filter mode. \\ Specify a `nat` value to get items where the specified field is greater than the specified value.  Example: `?balance.gt=1234`.  # noqa: E501

        :return: The gt of this NatParameter.  # noqa: E501
        :rtype: str
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """Sets the gt of this NatParameter.

        **Greater than** filter mode. \\ Specify a `nat` value to get items where the specified field is greater than the specified value.  Example: `?balance.gt=1234`.  # noqa: E501

        :param gt: The gt of this NatParameter.  # noqa: E501
        :type: str
        """

        self._gt = gt

    @property
    def ge(self):
        """Gets the ge of this NatParameter.  # noqa: E501

        **Greater or equal** filter mode. \\ Specify a `nat` value to get items where the specified field is greater than equal to the specified value.  Example: `?balance.ge=1234`.  # noqa: E501

        :return: The ge of this NatParameter.  # noqa: E501
        :rtype: str
        """
        return self._ge

    @ge.setter
    def ge(self, ge):
        """Sets the ge of this NatParameter.

        **Greater or equal** filter mode. \\ Specify a `nat` value to get items where the specified field is greater than equal to the specified value.  Example: `?balance.ge=1234`.  # noqa: E501

        :param ge: The ge of this NatParameter.  # noqa: E501
        :type: str
        """

        self._ge = ge

    @property
    def lt(self):
        """Gets the lt of this NatParameter.  # noqa: E501

        **Less than** filter mode. \\ Specify a `nat` value to get items where the specified field is less than the specified value.  Example: `?balance.lt=1234`.  # noqa: E501

        :return: The lt of this NatParameter.  # noqa: E501
        :rtype: str
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this NatParameter.

        **Less than** filter mode. \\ Specify a `nat` value to get items where the specified field is less than the specified value.  Example: `?balance.lt=1234`.  # noqa: E501

        :param lt: The lt of this NatParameter.  # noqa: E501
        :type: str
        """

        self._lt = lt

    @property
    def le(self):
        """Gets the le of this NatParameter.  # noqa: E501

        **Less or equal** filter mode. \\ Specify a `nat` value to get items where the specified field is less than or equal to the specified value.  Example: `?balance.le=1234`.  # noqa: E501

        :return: The le of this NatParameter.  # noqa: E501
        :rtype: str
        """
        return self._le

    @le.setter
    def le(self, le):
        """Sets the le of this NatParameter.

        **Less or equal** filter mode. \\ Specify a `nat` value to get items where the specified field is less than or equal to the specified value.  Example: `?balance.le=1234`.  # noqa: E501

        :param le: The le of this NatParameter.  # noqa: E501
        :type: str
        """

        self._le = le

    @property
    def _in(self):
        """Gets the _in of this NatParameter.  # noqa: E501

        **In list** (any of) filter mode. \\ Specify a comma-separated list of `nat` values to get items where the specified field is equal to one of the specified values.  Example: `?level.in=12,14,52,69`.  # noqa: E501

        :return: The _in of this NatParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this NatParameter.

        **In list** (any of) filter mode. \\ Specify a comma-separated list of `nat` values to get items where the specified field is equal to one of the specified values.  Example: `?level.in=12,14,52,69`.  # noqa: E501

        :param _in: The _in of this NatParameter.  # noqa: E501
        :type: list[str]
        """

        self.__in = _in

    @property
    def ni(self):
        """Gets the ni of this NatParameter.  # noqa: E501

        **Not in list** (none of) filter mode. \\ Specify a comma-separated list of `nat` values to get items where the specified field is not equal to all the specified values.  Example: `?level.ni=12,14,52,69`.  # noqa: E501

        :return: The ni of this NatParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._ni

    @ni.setter
    def ni(self, ni):
        """Sets the ni of this NatParameter.

        **Not in list** (none of) filter mode. \\ Specify a comma-separated list of `nat` values to get items where the specified field is not equal to all the specified values.  Example: `?level.ni=12,14,52,69`.  # noqa: E501

        :param ni: The ni of this NatParameter.  # noqa: E501
        :type: list[str]
        """

        self._ni = ni

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
        if issubclass(NatParameter, dict):
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
        if not isinstance(other, NatParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
