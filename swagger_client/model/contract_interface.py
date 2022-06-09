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

class ContractInterface(object):
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
        'storage_schema': 'OneOfContractInterfaceStorageSchema',
        'entrypoints': 'list[EntrypointInterface]',
        'big_maps': 'list[BigMapInterface]'
    }

    attribute_map = {
        'storage_schema': 'storageSchema',
        'entrypoints': 'entrypoints',
        'big_maps': 'bigMaps'
    }

    def __init__(self, storage_schema=None, entrypoints=None, big_maps=None):  # noqa: E501
        """ContractInterface - a model defined in Swagger"""  # noqa: E501
        self._storage_schema = None
        self._entrypoints = None
        self._big_maps = None
        self.discriminator = None
        if storage_schema is not None:
            self.storage_schema = storage_schema
        if entrypoints is not None:
            self.entrypoints = entrypoints
        if big_maps is not None:
            self.big_maps = big_maps

    @property
    def storage_schema(self):
        """Gets the storage_schema of this ContractInterface.  # noqa: E501

        JSON Schema of the contract storage in humanified format (as returned by API)  # noqa: E501

        :return: The storage_schema of this ContractInterface.  # noqa: E501
        :rtype: OneOfContractInterfaceStorageSchema
        """
        return self._storage_schema

    @storage_schema.setter
    def storage_schema(self, storage_schema):
        """Sets the storage_schema of this ContractInterface.

        JSON Schema of the contract storage in humanified format (as returned by API)  # noqa: E501

        :param storage_schema: The storage_schema of this ContractInterface.  # noqa: E501
        :type: OneOfContractInterfaceStorageSchema
        """

        self._storage_schema = storage_schema

    @property
    def entrypoints(self):
        """Gets the entrypoints of this ContractInterface.  # noqa: E501

        List of terminal entrypoints  # noqa: E501

        :return: The entrypoints of this ContractInterface.  # noqa: E501
        :rtype: list[EntrypointInterface]
        """
        return self._entrypoints

    @entrypoints.setter
    def entrypoints(self, entrypoints):
        """Sets the entrypoints of this ContractInterface.

        List of terminal entrypoints  # noqa: E501

        :param entrypoints: The entrypoints of this ContractInterface.  # noqa: E501
        :type: list[EntrypointInterface]
        """

        self._entrypoints = entrypoints

    @property
    def big_maps(self):
        """Gets the big_maps of this ContractInterface.  # noqa: E501

        List of currently available Big_maps  # noqa: E501

        :return: The big_maps of this ContractInterface.  # noqa: E501
        :rtype: list[BigMapInterface]
        """
        return self._big_maps

    @big_maps.setter
    def big_maps(self, big_maps):
        """Sets the big_maps of this ContractInterface.

        List of currently available Big_maps  # noqa: E501

        :param big_maps: The big_maps of this ContractInterface.  # noqa: E501
        :type: list[BigMapInterface]
        """

        self._big_maps = big_maps

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
        if issubclass(ContractInterface, dict):
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
        if not isinstance(other, ContractInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
