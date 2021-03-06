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

class State(object):
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
        'chain': 'str',
        'chain_id': 'str',
        'cycle': 'int',
        'level': 'int',
        'hash': 'str',
        'protocol': 'str',
        'next_protocol': 'str',
        'timestamp': 'datetime',
        'voting_epoch': 'int',
        'voting_period': 'int',
        'known_level': 'int',
        'last_sync': 'datetime',
        'synced': 'bool',
        'quote_level': 'int',
        'quote_btc': 'float',
        'quote_eur': 'float',
        'quote_usd': 'float',
        'quote_cny': 'float',
        'quote_jpy': 'float',
        'quote_krw': 'float',
        'quote_eth': 'float',
        'quote_gbp': 'float'
    }

    attribute_map = {
        'chain': 'chain',
        'chain_id': 'chainId',
        'cycle': 'cycle',
        'level': 'level',
        'hash': 'hash',
        'protocol': 'protocol',
        'next_protocol': 'nextProtocol',
        'timestamp': 'timestamp',
        'voting_epoch': 'votingEpoch',
        'voting_period': 'votingPeriod',
        'known_level': 'knownLevel',
        'last_sync': 'lastSync',
        'synced': 'synced',
        'quote_level': 'quoteLevel',
        'quote_btc': 'quoteBtc',
        'quote_eur': 'quoteEur',
        'quote_usd': 'quoteUsd',
        'quote_cny': 'quoteCny',
        'quote_jpy': 'quoteJpy',
        'quote_krw': 'quoteKrw',
        'quote_eth': 'quoteEth',
        'quote_gbp': 'quoteGbp'
    }

    def __init__(self, chain=None, chain_id=None, cycle=None, level=None, hash=None, protocol=None, next_protocol=None, timestamp=None, voting_epoch=None, voting_period=None, known_level=None, last_sync=None, synced=None, quote_level=None, quote_btc=None, quote_eur=None, quote_usd=None, quote_cny=None, quote_jpy=None, quote_krw=None, quote_eth=None, quote_gbp=None):  # noqa: E501
        """State - a model defined in Swagger"""  # noqa: E501
        self._chain = None
        self._chain_id = None
        self._cycle = None
        self._level = None
        self._hash = None
        self._protocol = None
        self._next_protocol = None
        self._timestamp = None
        self._voting_epoch = None
        self._voting_period = None
        self._known_level = None
        self._last_sync = None
        self._synced = None
        self._quote_level = None
        self._quote_btc = None
        self._quote_eur = None
        self._quote_usd = None
        self._quote_cny = None
        self._quote_jpy = None
        self._quote_krw = None
        self._quote_eth = None
        self._quote_gbp = None
        self.discriminator = None
        if chain is not None:
            self.chain = chain
        if chain_id is not None:
            self.chain_id = chain_id
        if cycle is not None:
            self.cycle = cycle
        if level is not None:
            self.level = level
        if hash is not None:
            self.hash = hash
        if protocol is not None:
            self.protocol = protocol
        if next_protocol is not None:
            self.next_protocol = next_protocol
        if timestamp is not None:
            self.timestamp = timestamp
        if voting_epoch is not None:
            self.voting_epoch = voting_epoch
        if voting_period is not None:
            self.voting_period = voting_period
        if known_level is not None:
            self.known_level = known_level
        if last_sync is not None:
            self.last_sync = last_sync
        if synced is not None:
            self.synced = synced
        if quote_level is not None:
            self.quote_level = quote_level
        if quote_btc is not None:
            self.quote_btc = quote_btc
        if quote_eur is not None:
            self.quote_eur = quote_eur
        if quote_usd is not None:
            self.quote_usd = quote_usd
        if quote_cny is not None:
            self.quote_cny = quote_cny
        if quote_jpy is not None:
            self.quote_jpy = quote_jpy
        if quote_krw is not None:
            self.quote_krw = quote_krw
        if quote_eth is not None:
            self.quote_eth = quote_eth
        if quote_gbp is not None:
            self.quote_gbp = quote_gbp

    @property
    def chain(self):
        """Gets the chain of this State.  # noqa: E501

        Alias name of the chain (or \"private\" if it's not on the list of known chains)  # noqa: E501

        :return: The chain of this State.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this State.

        Alias name of the chain (or \"private\" if it's not on the list of known chains)  # noqa: E501

        :param chain: The chain of this State.  # noqa: E501
        :type: str
        """

        self._chain = chain

    @property
    def chain_id(self):
        """Gets the chain_id of this State.  # noqa: E501

        Unique identifier of the chain  # noqa: E501

        :return: The chain_id of this State.  # noqa: E501
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this State.

        Unique identifier of the chain  # noqa: E501

        :param chain_id: The chain_id of this State.  # noqa: E501
        :type: str
        """

        self._chain_id = chain_id

    @property
    def cycle(self):
        """Gets the cycle of this State.  # noqa: E501

        Current cycle  # noqa: E501

        :return: The cycle of this State.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this State.

        Current cycle  # noqa: E501

        :param cycle: The cycle of this State.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def level(self):
        """Gets the level of this State.  # noqa: E501

        The height of the last block from the genesis block  # noqa: E501

        :return: The level of this State.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this State.

        The height of the last block from the genesis block  # noqa: E501

        :param level: The level of this State.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def hash(self):
        """Gets the hash of this State.  # noqa: E501

        Block hash  # noqa: E501

        :return: The hash of this State.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this State.

        Block hash  # noqa: E501

        :param hash: The hash of this State.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def protocol(self):
        """Gets the protocol of this State.  # noqa: E501

        Current protocol hash  # noqa: E501

        :return: The protocol of this State.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this State.

        Current protocol hash  # noqa: E501

        :param protocol: The protocol of this State.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def next_protocol(self):
        """Gets the next_protocol of this State.  # noqa: E501

        Next block protocol hash  # noqa: E501

        :return: The next_protocol of this State.  # noqa: E501
        :rtype: str
        """
        return self._next_protocol

    @next_protocol.setter
    def next_protocol(self, next_protocol):
        """Sets the next_protocol of this State.

        Next block protocol hash  # noqa: E501

        :param next_protocol: The next_protocol of this State.  # noqa: E501
        :type: str
        """

        self._next_protocol = next_protocol

    @property
    def timestamp(self):
        """Gets the timestamp of this State.  # noqa: E501

        The datetime at which the last block is claimed to have been created (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The timestamp of this State.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this State.

        The datetime at which the last block is claimed to have been created (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param timestamp: The timestamp of this State.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def voting_epoch(self):
        """Gets the voting_epoch of this State.  # noqa: E501

        Current voting epoch index, starting from zero  # noqa: E501

        :return: The voting_epoch of this State.  # noqa: E501
        :rtype: int
        """
        return self._voting_epoch

    @voting_epoch.setter
    def voting_epoch(self, voting_epoch):
        """Sets the voting_epoch of this State.

        Current voting epoch index, starting from zero  # noqa: E501

        :param voting_epoch: The voting_epoch of this State.  # noqa: E501
        :type: int
        """

        self._voting_epoch = voting_epoch

    @property
    def voting_period(self):
        """Gets the voting_period of this State.  # noqa: E501

        Current voting period index, starting from zero  # noqa: E501

        :return: The voting_period of this State.  # noqa: E501
        :rtype: int
        """
        return self._voting_period

    @voting_period.setter
    def voting_period(self, voting_period):
        """Sets the voting_period of this State.

        Current voting period index, starting from zero  # noqa: E501

        :param voting_period: The voting_period of this State.  # noqa: E501
        :type: int
        """

        self._voting_period = voting_period

    @property
    def known_level(self):
        """Gets the known_level of this State.  # noqa: E501

        The height of the last known block from the genesis block  # noqa: E501

        :return: The known_level of this State.  # noqa: E501
        :rtype: int
        """
        return self._known_level

    @known_level.setter
    def known_level(self, known_level):
        """Sets the known_level of this State.

        The height of the last known block from the genesis block  # noqa: E501

        :param known_level: The known_level of this State.  # noqa: E501
        :type: int
        """

        self._known_level = known_level

    @property
    def last_sync(self):
        """Gets the last_sync of this State.  # noqa: E501

        The datetime of last TzKT indexer synchronization (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The last_sync of this State.  # noqa: E501
        :rtype: datetime
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this State.

        The datetime of last TzKT indexer synchronization (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param last_sync: The last_sync of this State.  # noqa: E501
        :type: datetime
        """

        self._last_sync = last_sync

    @property
    def synced(self):
        """Gets the synced of this State.  # noqa: E501

        State of TzKT indexer synchronization  # noqa: E501

        :return: The synced of this State.  # noqa: E501
        :rtype: bool
        """
        return self._synced

    @synced.setter
    def synced(self, synced):
        """Sets the synced of this State.

        State of TzKT indexer synchronization  # noqa: E501

        :param synced: The synced of this State.  # noqa: E501
        :type: bool
        """

        self._synced = synced

    @property
    def quote_level(self):
        """Gets the quote_level of this State.  # noqa: E501

        The height of the block where quotes were updated last time  # noqa: E501

        :return: The quote_level of this State.  # noqa: E501
        :rtype: int
        """
        return self._quote_level

    @quote_level.setter
    def quote_level(self, quote_level):
        """Sets the quote_level of this State.

        The height of the block where quotes were updated last time  # noqa: E501

        :param quote_level: The quote_level of this State.  # noqa: E501
        :type: int
        """

        self._quote_level = quote_level

    @property
    def quote_btc(self):
        """Gets the quote_btc of this State.  # noqa: E501

        Last known XTZ/BTC price  # noqa: E501

        :return: The quote_btc of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_btc

    @quote_btc.setter
    def quote_btc(self, quote_btc):
        """Sets the quote_btc of this State.

        Last known XTZ/BTC price  # noqa: E501

        :param quote_btc: The quote_btc of this State.  # noqa: E501
        :type: float
        """

        self._quote_btc = quote_btc

    @property
    def quote_eur(self):
        """Gets the quote_eur of this State.  # noqa: E501

        Last known XTZ/EUR price  # noqa: E501

        :return: The quote_eur of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_eur

    @quote_eur.setter
    def quote_eur(self, quote_eur):
        """Sets the quote_eur of this State.

        Last known XTZ/EUR price  # noqa: E501

        :param quote_eur: The quote_eur of this State.  # noqa: E501
        :type: float
        """

        self._quote_eur = quote_eur

    @property
    def quote_usd(self):
        """Gets the quote_usd of this State.  # noqa: E501

        Last known XTZ/USD price  # noqa: E501

        :return: The quote_usd of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_usd

    @quote_usd.setter
    def quote_usd(self, quote_usd):
        """Sets the quote_usd of this State.

        Last known XTZ/USD price  # noqa: E501

        :param quote_usd: The quote_usd of this State.  # noqa: E501
        :type: float
        """

        self._quote_usd = quote_usd

    @property
    def quote_cny(self):
        """Gets the quote_cny of this State.  # noqa: E501

        Last known XTZ/CNY price  # noqa: E501

        :return: The quote_cny of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_cny

    @quote_cny.setter
    def quote_cny(self, quote_cny):
        """Sets the quote_cny of this State.

        Last known XTZ/CNY price  # noqa: E501

        :param quote_cny: The quote_cny of this State.  # noqa: E501
        :type: float
        """

        self._quote_cny = quote_cny

    @property
    def quote_jpy(self):
        """Gets the quote_jpy of this State.  # noqa: E501

        Last known XTZ/JPY price  # noqa: E501

        :return: The quote_jpy of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_jpy

    @quote_jpy.setter
    def quote_jpy(self, quote_jpy):
        """Sets the quote_jpy of this State.

        Last known XTZ/JPY price  # noqa: E501

        :param quote_jpy: The quote_jpy of this State.  # noqa: E501
        :type: float
        """

        self._quote_jpy = quote_jpy

    @property
    def quote_krw(self):
        """Gets the quote_krw of this State.  # noqa: E501

        Last known XTZ/KRW price  # noqa: E501

        :return: The quote_krw of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_krw

    @quote_krw.setter
    def quote_krw(self, quote_krw):
        """Sets the quote_krw of this State.

        Last known XTZ/KRW price  # noqa: E501

        :param quote_krw: The quote_krw of this State.  # noqa: E501
        :type: float
        """

        self._quote_krw = quote_krw

    @property
    def quote_eth(self):
        """Gets the quote_eth of this State.  # noqa: E501

        Last known XTZ/ETH price  # noqa: E501

        :return: The quote_eth of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_eth

    @quote_eth.setter
    def quote_eth(self, quote_eth):
        """Sets the quote_eth of this State.

        Last known XTZ/ETH price  # noqa: E501

        :param quote_eth: The quote_eth of this State.  # noqa: E501
        :type: float
        """

        self._quote_eth = quote_eth

    @property
    def quote_gbp(self):
        """Gets the quote_gbp of this State.  # noqa: E501

        Last known XTZ/GBP price  # noqa: E501

        :return: The quote_gbp of this State.  # noqa: E501
        :rtype: float
        """
        return self._quote_gbp

    @quote_gbp.setter
    def quote_gbp(self, quote_gbp):
        """Sets the quote_gbp of this State.

        Last known XTZ/GBP price  # noqa: E501

        :param quote_gbp: The quote_gbp of this State.  # noqa: E501
        :type: float
        """

        self._quote_gbp = quote_gbp

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
        if issubclass(State, dict):
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
        if not isinstance(other, State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
