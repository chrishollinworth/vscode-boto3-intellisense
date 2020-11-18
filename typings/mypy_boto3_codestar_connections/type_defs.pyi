"""
Main interface for codestar-connections service type definitions.

Usage::

    ```python
    from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

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
    "ResponseMetadata",
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
        "ProviderType": Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"],
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
        "ProviderType": Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"],
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
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
    "_OptionalCreateConnectionOutputTypeDef",
    {"Tags": List["TagTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateConnectionOutputTypeDef(
    _RequiredCreateConnectionOutputTypeDef, _OptionalCreateConnectionOutputTypeDef
):
    pass


CreateHostOutputTypeDef = TypedDict(
    "CreateHostOutputTypeDef", {"HostArn": str, "ResponseMetadata": "ResponseMetadata"}, total=False
)

GetConnectionOutputTypeDef = TypedDict(
    "GetConnectionOutputTypeDef",
    {"Connection": "ConnectionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetHostOutputTypeDef = TypedDict(
    "GetHostOutputTypeDef",
    {
        "Name": str,
        "Status": str,
        "ProviderType": Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"],
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListConnectionsOutputTypeDef = TypedDict(
    "ListConnectionsOutputTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListHostsOutputTypeDef = TypedDict(
    "ListHostsOutputTypeDef",
    {"Hosts": List["HostTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"Tags": List["TagTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)
