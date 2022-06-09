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
from swagger_client.model.operation import Operation  # noqa: F401,E501

class RevelationPenaltyOperation(Operation):
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
        'id': 'int',
        'level': 'int',
        'timestamp': 'datetime',
        'block': 'str',
        'baker': 'object',
        'missed_level': 'int',
        'loss': 'int',
        'quote': 'object',
        'lost_reward': 'int',
        'lost_fees': 'int'
    }
    if hasattr(Operation, "swagger_types"):
        swagger_types.update(Operation.swagger_types)

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'level': 'level',
        'timestamp': 'timestamp',
        'block': 'block',
        'baker': 'baker',
        'missed_level': 'missedLevel',
        'loss': 'loss',
        'quote': 'quote',
        'lost_reward': 'lostReward',
        'lost_fees': 'lostFees'
    }
    if hasattr(Operation, "attribute_map"):
        attribute_map.update(Operation.attribute_map)

    def __init__(self, type=None, id=None, level=None, timestamp=None, block=None, baker=None, missed_level=None, loss=None, quote=None, lost_reward=None, lost_fees=None, *args, **kwargs):  # noqa: E501
        """RevelationPenaltyOperation - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._level = None
        self._timestamp = None
        self._block = None
        self._baker = None
        self._missed_level = None
        self._loss = None
        self._quote = None
        self._lost_reward = None
        self._lost_fees = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if level is not None:
            self.level = level
        if timestamp is not None:
            self.timestamp = timestamp
        if block is not None:
            self.block = block
        if baker is not None:
            self.baker = baker
        if missed_level is not None:
            self.missed_level = missed_level
        if loss is not None:
            self.loss = loss
        if quote is not None:
            self.quote = quote
        if lost_reward is not None:
            self.lost_reward = lost_reward
        if lost_fees is not None:
            self.lost_fees = lost_fees
        Operation.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this RevelationPenaltyOperation.  # noqa: E501

        Type of the operation, `revelation_penalty` - is operation, in which rewards were lost due to unrevealed seed nonces by the delegate (synthetic type)  # noqa: E501

        :return: The type of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RevelationPenaltyOperation.

        Type of the operation, `revelation_penalty` - is operation, in which rewards were lost due to unrevealed seed nonces by the delegate (synthetic type)  # noqa: E501

        :param type: The type of this RevelationPenaltyOperation.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this RevelationPenaltyOperation.  # noqa: E501

        Unique ID of the operation, stored in the TzKT indexer database  # noqa: E501

        :return: The id of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RevelationPenaltyOperation.

        Unique ID of the operation, stored in the TzKT indexer database  # noqa: E501

        :param id: The id of this RevelationPenaltyOperation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def level(self):
        """Gets the level of this RevelationPenaltyOperation.  # noqa: E501

        The height of the block from the genesis block, in which the operation was included  # noqa: E501

        :return: The level of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this RevelationPenaltyOperation.

        The height of the block from the genesis block, in which the operation was included  # noqa: E501

        :param level: The level of this RevelationPenaltyOperation.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def timestamp(self):
        """Gets the timestamp of this RevelationPenaltyOperation.  # noqa: E501

        Datetime of the block, in which the operation was included (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :return: The timestamp of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RevelationPenaltyOperation.

        Datetime of the block, in which the operation was included (ISO 8601, e.g. `2020-02-20T02:40:57Z`)  # noqa: E501

        :param timestamp: The timestamp of this RevelationPenaltyOperation.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def block(self):
        """Gets the block of this RevelationPenaltyOperation.  # noqa: E501

        Hash of the block, in which the operation was included  # noqa: E501

        :return: The block of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: str
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this RevelationPenaltyOperation.

        Hash of the block, in which the operation was included  # noqa: E501

        :param block: The block of this RevelationPenaltyOperation.  # noqa: E501
        :type: str
        """

        self._block = block

    @property
    def baker(self):
        """Gets the baker of this RevelationPenaltyOperation.  # noqa: E501

        Information about the delegate (baker) who has lost rewards due to unrevealed seed nonces   # noqa: E501

        :return: The baker of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: object
        """
        return self._baker

    @baker.setter
    def baker(self, baker):
        """Sets the baker of this RevelationPenaltyOperation.

        Information about the delegate (baker) who has lost rewards due to unrevealed seed nonces   # noqa: E501

        :param baker: The baker of this RevelationPenaltyOperation.  # noqa: E501
        :type: object
        """

        self._baker = baker

    @property
    def missed_level(self):
        """Gets the missed_level of this RevelationPenaltyOperation.  # noqa: E501

        Height of the block, which contains hash of the seed nonce, which was to be revealed  # noqa: E501

        :return: The missed_level of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: int
        """
        return self._missed_level

    @missed_level.setter
    def missed_level(self, missed_level):
        """Sets the missed_level of this RevelationPenaltyOperation.

        Height of the block, which contains hash of the seed nonce, which was to be revealed  # noqa: E501

        :param missed_level: The missed_level of this RevelationPenaltyOperation.  # noqa: E501
        :type: int
        """

        self._missed_level = missed_level

    @property
    def loss(self):
        """Gets the loss of this RevelationPenaltyOperation.  # noqa: E501

        Reward for baking and gathered fees from the block, which were lost due to unrevealed seed nonces (micro tez)  # noqa: E501

        :return: The loss of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: int
        """
        return self._loss

    @loss.setter
    def loss(self, loss):
        """Sets the loss of this RevelationPenaltyOperation.

        Reward for baking and gathered fees from the block, which were lost due to unrevealed seed nonces (micro tez)  # noqa: E501

        :param loss: The loss of this RevelationPenaltyOperation.  # noqa: E501
        :type: int
        """

        self._loss = loss

    @property
    def quote(self):
        """Gets the quote of this RevelationPenaltyOperation.  # noqa: E501

        Injected historical quote at the time of operation  # noqa: E501

        :return: The quote of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: object
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this RevelationPenaltyOperation.

        Injected historical quote at the time of operation  # noqa: E501

        :param quote: The quote of this RevelationPenaltyOperation.  # noqa: E501
        :type: object
        """

        self._quote = quote

    @property
    def lost_reward(self):
        """Gets the lost_reward of this RevelationPenaltyOperation.  # noqa: E501

        [DEPRECATED]  # noqa: E501

        :return: The lost_reward of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: int
        """
        return self._lost_reward

    @lost_reward.setter
    def lost_reward(self, lost_reward):
        """Sets the lost_reward of this RevelationPenaltyOperation.

        [DEPRECATED]  # noqa: E501

        :param lost_reward: The lost_reward of this RevelationPenaltyOperation.  # noqa: E501
        :type: int
        """

        self._lost_reward = lost_reward

    @property
    def lost_fees(self):
        """Gets the lost_fees of this RevelationPenaltyOperation.  # noqa: E501

        [DEPRECATED]  # noqa: E501

        :return: The lost_fees of this RevelationPenaltyOperation.  # noqa: E501
        :rtype: int
        """
        return self._lost_fees

    @lost_fees.setter
    def lost_fees(self, lost_fees):
        """Sets the lost_fees of this RevelationPenaltyOperation.

        [DEPRECATED]  # noqa: E501

        :param lost_fees: The lost_fees of this RevelationPenaltyOperation.  # noqa: E501
        :type: int
        """

        self._lost_fees = lost_fees

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
        if issubclass(RevelationPenaltyOperation, dict):
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
        if not isinstance(other, RevelationPenaltyOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other