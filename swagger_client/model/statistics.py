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

class Statistics(object):
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
        'cycle': 'int',
        '_date': 'datetime',
        'level': 'int',
        'timestamp': 'datetime',
        'total_supply': 'int',
        'circulating_supply': 'int',
        'total_bootstrapped': 'int',
        'total_commitments': 'int',
        'total_activated': 'int',
        'total_created': 'int',
        'total_burned': 'int',
        'total_banished': 'int',
        'total_frozen': 'int',
        'quote': 'OneOfStatisticsQuote',
        'total_vested': 'int'
    }

    attribute_map = {
        'cycle': 'cycle',
        '_date': 'date',
        'level': 'level',
        'timestamp': 'timestamp',
        'total_supply': 'totalSupply',
        'circulating_supply': 'circulatingSupply',
        'total_bootstrapped': 'totalBootstrapped',
        'total_commitments': 'totalCommitments',
        'total_activated': 'totalActivated',
        'total_created': 'totalCreated',
        'total_burned': 'totalBurned',
        'total_banished': 'totalBanished',
        'total_frozen': 'totalFrozen',
        'quote': 'quote',
        'total_vested': 'totalVested'
    }

    def __init__(self, cycle=None, _date=None, level=None, timestamp=None, total_supply=None, circulating_supply=None, total_bootstrapped=None, total_commitments=None, total_activated=None, total_created=None, total_burned=None, total_banished=None, total_frozen=None, quote=None, total_vested=None):  # noqa: E501
        """Statistics - a model defined in Swagger"""  # noqa: E501
        self._cycle = None
        self.__date = None
        self._level = None
        self._timestamp = None
        self._total_supply = None
        self._circulating_supply = None
        self._total_bootstrapped = None
        self._total_commitments = None
        self._total_activated = None
        self._total_created = None
        self._total_burned = None
        self._total_banished = None
        self._total_frozen = None
        self._quote = None
        self._total_vested = None
        self.discriminator = None
        if cycle is not None:
            self.cycle = cycle
        if _date is not None:
            self._date = _date
        if level is not None:
            self.level = level
        if timestamp is not None:
            self.timestamp = timestamp
        if total_supply is not None:
            self.total_supply = total_supply
        if circulating_supply is not None:
            self.circulating_supply = circulating_supply
        if total_bootstrapped is not None:
            self.total_bootstrapped = total_bootstrapped
        if total_commitments is not None:
            self.total_commitments = total_commitments
        if total_activated is not None:
            self.total_activated = total_activated
        if total_created is not None:
            self.total_created = total_created
        if total_burned is not None:
            self.total_burned = total_burned
        if total_banished is not None:
            self.total_banished = total_banished
        if total_frozen is not None:
            self.total_frozen = total_frozen
        if quote is not None:
            self.quote = quote
        if total_vested is not None:
            self.total_vested = total_vested

    @property
    def cycle(self):
        """Gets the cycle of this Statistics.  # noqa: E501

        Cycle at the end of which the statistics has been calculated. This field is only present in cyclic statistics.  # noqa: E501

        :return: The cycle of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this Statistics.

        Cycle at the end of which the statistics has been calculated. This field is only present in cyclic statistics.  # noqa: E501

        :param cycle: The cycle of this Statistics.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def _date(self):
        """Gets the _date of this Statistics.  # noqa: E501

        Day at the end of which the statistics has been calculated. This field is only present in daily statistics.  # noqa: E501

        :return: The _date of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Statistics.

        Day at the end of which the statistics has been calculated. This field is only present in daily statistics.  # noqa: E501

        :param _date: The _date of this Statistics.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def level(self):
        """Gets the level of this Statistics.  # noqa: E501

        Level of the block at which the statistics has been calculated  # noqa: E501

        :return: The level of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Statistics.

        Level of the block at which the statistics has been calculated  # noqa: E501

        :param level: The level of this Statistics.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def timestamp(self):
        """Gets the timestamp of this Statistics.  # noqa: E501

        Timestamp of the block at which the statistics has been calculated (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The timestamp of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Statistics.

        Timestamp of the block at which the statistics has been calculated (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param timestamp: The timestamp of this Statistics.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def total_supply(self):
        """Gets the total_supply of this Statistics.  # noqa: E501

        Total supply - all existing tokens (including locked vested funds and frozen funds) plus not yet activated fundraiser tokens  # noqa: E501

        :return: The total_supply of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_supply

    @total_supply.setter
    def total_supply(self, total_supply):
        """Sets the total_supply of this Statistics.

        Total supply - all existing tokens (including locked vested funds and frozen funds) plus not yet activated fundraiser tokens  # noqa: E501

        :param total_supply: The total_supply of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_supply = total_supply

    @property
    def circulating_supply(self):
        """Gets the circulating_supply of this Statistics.  # noqa: E501

        Circulating supply - all active tokens which can affect supply and demand (can be spent/transferred)  # noqa: E501

        :return: The circulating_supply of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._circulating_supply

    @circulating_supply.setter
    def circulating_supply(self, circulating_supply):
        """Sets the circulating_supply of this Statistics.

        Circulating supply - all active tokens which can affect supply and demand (can be spent/transferred)  # noqa: E501

        :param circulating_supply: The circulating_supply of this Statistics.  # noqa: E501
        :type: int
        """

        self._circulating_supply = circulating_supply

    @property
    def total_bootstrapped(self):
        """Gets the total_bootstrapped of this Statistics.  # noqa: E501

        Total amount of tokens initially created when starting the blockchain  # noqa: E501

        :return: The total_bootstrapped of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_bootstrapped

    @total_bootstrapped.setter
    def total_bootstrapped(self, total_bootstrapped):
        """Sets the total_bootstrapped of this Statistics.

        Total amount of tokens initially created when starting the blockchain  # noqa: E501

        :param total_bootstrapped: The total_bootstrapped of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_bootstrapped = total_bootstrapped

    @property
    def total_commitments(self):
        """Gets the total_commitments of this Statistics.  # noqa: E501

        Total commitment amount (tokens to be activated by fundraisers)  # noqa: E501

        :return: The total_commitments of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_commitments

    @total_commitments.setter
    def total_commitments(self, total_commitments):
        """Sets the total_commitments of this Statistics.

        Total commitment amount (tokens to be activated by fundraisers)  # noqa: E501

        :param total_commitments: The total_commitments of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_commitments = total_commitments

    @property
    def total_activated(self):
        """Gets the total_activated of this Statistics.  # noqa: E501

        Total amount of tokens activated by fundraisers  # noqa: E501

        :return: The total_activated of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_activated

    @total_activated.setter
    def total_activated(self, total_activated):
        """Sets the total_activated of this Statistics.

        Total amount of tokens activated by fundraisers  # noqa: E501

        :param total_activated: The total_activated of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_activated = total_activated

    @property
    def total_created(self):
        """Gets the total_created of this Statistics.  # noqa: E501

        Total amount of created/issued tokens  # noqa: E501

        :return: The total_created of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_created

    @total_created.setter
    def total_created(self, total_created):
        """Sets the total_created of this Statistics.

        Total amount of created/issued tokens  # noqa: E501

        :param total_created: The total_created of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_created = total_created

    @property
    def total_burned(self):
        """Gets the total_burned of this Statistics.  # noqa: E501

        Total amount of burned tokens  # noqa: E501

        :return: The total_burned of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_burned

    @total_burned.setter
    def total_burned(self, total_burned):
        """Sets the total_burned of this Statistics.

        Total amount of burned tokens  # noqa: E501

        :param total_burned: The total_burned of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_burned = total_burned

    @property
    def total_banished(self):
        """Gets the total_banished of this Statistics.  # noqa: E501

        Total amount of tokens sent to the null-address, which is equivalent to burning  # noqa: E501

        :return: The total_banished of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_banished

    @total_banished.setter
    def total_banished(self, total_banished):
        """Sets the total_banished of this Statistics.

        Total amount of tokens sent to the null-address, which is equivalent to burning  # noqa: E501

        :param total_banished: The total_banished of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_banished = total_banished

    @property
    def total_frozen(self):
        """Gets the total_frozen of this Statistics.  # noqa: E501

        Total amount of frozen tokens (frozen security deposits, frozen rewards and frozen fees)  # noqa: E501

        :return: The total_frozen of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_frozen

    @total_frozen.setter
    def total_frozen(self, total_frozen):
        """Sets the total_frozen of this Statistics.

        Total amount of frozen tokens (frozen security deposits, frozen rewards and frozen fees)  # noqa: E501

        :param total_frozen: The total_frozen of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_frozen = total_frozen

    @property
    def quote(self):
        """Gets the quote of this Statistics.  # noqa: E501

        Injected historical quote at the time of the block at which the statistics has been calculated  # noqa: E501

        :return: The quote of this Statistics.  # noqa: E501
        :rtype: OneOfStatisticsQuote
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this Statistics.

        Injected historical quote at the time of the block at which the statistics has been calculated  # noqa: E501

        :param quote: The quote of this Statistics.  # noqa: E501
        :type: OneOfStatisticsQuote
        """

        self._quote = quote

    @property
    def total_vested(self):
        """Gets the total_vested of this Statistics.  # noqa: E501

        [DEPRECATED]  # noqa: E501

        :return: The total_vested of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_vested

    @total_vested.setter
    def total_vested(self, total_vested):
        """Sets the total_vested of this Statistics.

        [DEPRECATED]  # noqa: E501

        :param total_vested: The total_vested of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_vested = total_vested

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
        if issubclass(Statistics, dict):
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
        if not isinstance(other, Statistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
