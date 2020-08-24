"""
Main interface for codestar-connections service type definitions.

Usage::

    ```python
    from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConnectionTypeDef",
    "HostTypeDef",
    "TagTypeDef",
    "VpcConfigurationTypeDef",
    "CreateConnectionOutputTypeDef",
    "CreateHostOutputTypeDef",
    "GetConnectionOutputTypeDef",
    "GetHostOutputTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListHostsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": Literal["Bitbucket", "GitHubEnterpriseServer"],
        "OwnerAccountId": str,
        "ConnectionStatus": Literal["PENDING", "AVAILABLE", "ERROR"],
        "HostArn": str,
    },
    total=False,
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "Name": str,
        "HostArn": str,
        "ProviderType": Literal["Bitbucket", "GitHubEnterpriseServer"],
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredVpcConfigurationTypeDef = TypedDict(
    "_RequiredVpcConfigurationTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupIds": List[str]},
)
_OptionalVpcConfigurationTypeDef = TypedDict(
    "_OptionalVpcConfigurationTypeDef", {"TlsCertificate": str}, total=False
)


class VpcConfigurationTypeDef(_RequiredVpcConfigurationTypeDef, _OptionalVpcConfigurationTypeDef):
    pass


_RequiredCreateConnectionOutputTypeDef = TypedDict(
    "_RequiredCreateConnectionOutputTypeDef", {"ConnectionArn": str}
)
_OptionalCreateConnectionOutputTypeDef = TypedDict(
    "_OptionalCreateConnectionOutputTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)


class CreateConnectionOutputTypeDef(
    _RequiredCreateConnectionOutputTypeDef, _OptionalCreateConnectionOutputTypeDef
):
    pass


CreateHostOutputTypeDef = TypedDict("CreateHostOutputTypeDef", {"HostArn": str}, total=False)

GetConnectionOutputTypeDef = TypedDict(
    "GetConnectionOutputTypeDef", {"Connection": "ConnectionTypeDef"}, total=False
)

GetHostOutputTypeDef = TypedDict(
    "GetHostOutputTypeDef",
    {
        "Name": str,
        "Status": str,
        "ProviderType": Literal["Bitbucket", "GitHubEnterpriseServer"],
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
    total=False,
)

ListConnectionsOutputTypeDef = TypedDict(
    "ListConnectionsOutputTypeDef",
    {"Connections": List["ConnectionTypeDef"], "NextToken": str},
    total=False,
)

ListHostsOutputTypeDef = TypedDict(
    "ListHostsOutputTypeDef", {"Hosts": List["HostTypeDef"], "NextToken": str}, total=False
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)
