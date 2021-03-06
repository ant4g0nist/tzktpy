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

class BakingRight(object):
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
        'cycle': 'int',
        'level': 'int',
        'timestamp': 'datetime',
        'round': 'int',
        'slots': 'int',
        'baker': 'OneOfBakingRightBaker',
        'status': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'type': 'type',
        'cycle': 'cycle',
        'level': 'level',
        'timestamp': 'timestamp',
        'round': 'round',
        'slots': 'slots',
        'baker': 'baker',
        'status': 'status',
        'priority': 'priority'
    }

    def __init__(self, type=None, cycle=None, level=None, timestamp=None, round=None, slots=None, baker=None, status=None, priority=None):  # noqa: E501
        """BakingRight - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._cycle = None
        self._level = None
        self._timestamp = None
        self._round = None
        self._slots = None
        self._baker = None
        self._status = None
        self._priority = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if cycle is not None:
            self.cycle = cycle
        if level is not None:
            self.level = level
        if timestamp is not None:
            self.timestamp = timestamp
        if round is not None:
            self.round = round
        if slots is not None:
            self.slots = slots
        if baker is not None:
            self.baker = baker
        if status is not None:
            self.status = status
        if priority is not None:
            self.priority = priority

    @property
    def type(self):
        """Gets the type of this BakingRight.  # noqa: E501

        Type of the right: - `baking` - right to bake (produce) a block; - `endorsing` - right to endorse (validate) a block.  # noqa: E501

        :return: The type of this BakingRight.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BakingRight.

        Type of the right: - `baking` - right to bake (produce) a block; - `endorsing` - right to endorse (validate) a block.  # noqa: E501

        :param type: The type of this BakingRight.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def cycle(self):
        """Gets the cycle of this BakingRight.  # noqa: E501

        Cycle on which the right can be realized.  # noqa: E501

        :return: The cycle of this BakingRight.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this BakingRight.

        Cycle on which the right can be realized.  # noqa: E501

        :param cycle: The cycle of this BakingRight.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def level(self):
        """Gets the level of this BakingRight.  # noqa: E501

        Level at which a block must be baked or an endorsement must be sent.  # noqa: E501

        :return: The level of this BakingRight.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this BakingRight.

        Level at which a block must be baked or an endorsement must be sent.  # noqa: E501

        :param level: The level of this BakingRight.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def timestamp(self):
        """Gets the timestamp of this BakingRight.  # noqa: E501

        Time (estimated, in case of future rights) when a block must be baked or an endorsement must be sent.  # noqa: E501

        :return: The timestamp of this BakingRight.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BakingRight.

        Time (estimated, in case of future rights) when a block must be baked or an endorsement must be sent.  # noqa: E501

        :param timestamp: The timestamp of this BakingRight.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def round(self):
        """Gets the round of this BakingRight.  # noqa: E501

        Round (0 - ???) at which the baker can propose/produce a block. If a baker at round  `0` doesn't produce a block within the given time interval, then the right goes to a baker at round` 1`, etc. For `endorsing` rights this field is always `null`.  # noqa: E501

        :return: The round of this BakingRight.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this BakingRight.

        Round (0 - ???) at which the baker can propose/produce a block. If a baker at round  `0` doesn't produce a block within the given time interval, then the right goes to a baker at round` 1`, etc. For `endorsing` rights this field is always `null`.  # noqa: E501

        :param round: The round of this BakingRight.  # noqa: E501
        :type: int
        """

        self._round = round

    @property
    def slots(self):
        """Gets the slots of this BakingRight.  # noqa: E501

        Number of slots (1 - 32) to be endorsed. For `baking` rights this field is always `null`.  # noqa: E501

        :return: The slots of this BakingRight.  # noqa: E501
        :rtype: int
        """
        return self._slots

    @slots.setter
    def slots(self, slots):
        """Sets the slots of this BakingRight.

        Number of slots (1 - 32) to be endorsed. For `baking` rights this field is always `null`.  # noqa: E501

        :param slots: The slots of this BakingRight.  # noqa: E501
        :type: int
        """

        self._slots = slots

    @property
    def baker(self):
        """Gets the baker of this BakingRight.  # noqa: E501

        Baker to which baking or endorsing right has been given.  # noqa: E501

        :return: The baker of this BakingRight.  # noqa: E501
        :rtype: OneOfBakingRightBaker
        """
        return self._baker

    @baker.setter
    def baker(self, baker):
        """Sets the baker of this BakingRight.

        Baker to which baking or endorsing right has been given.  # noqa: E501

        :param baker: The baker of this BakingRight.  # noqa: E501
        :type: OneOfBakingRightBaker
        """

        self._baker = baker

    @property
    def status(self):
        """Gets the status of this BakingRight.  # noqa: E501

        Status of the baking or endorsing right: - `future` - the right is not realized yet; - `realized` - the right was successfully realized; - `missed` - the right was not realized.  # noqa: E501

        :return: The status of this BakingRight.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BakingRight.

        Status of the baking or endorsing right: - `future` - the right is not realized yet; - `realized` - the right was successfully realized; - `missed` - the right was not realized.  # noqa: E501

        :param status: The status of this BakingRight.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def priority(self):
        """Gets the priority of this BakingRight.  # noqa: E501

        [DEPRECATED]  # noqa: E501

        :return: The priority of this BakingRight.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this BakingRight.

        [DEPRECATED]  # noqa: E501

        :param priority: The priority of this BakingRight.  # noqa: E501
        :type: int
        """

        self._priority = priority

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
        if issubclass(BakingRight, dict):
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
        if not isinstance(other, BakingRight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
