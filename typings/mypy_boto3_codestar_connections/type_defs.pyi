"""
Type annotations for codestar-connections service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ConnectionStatusType, ProviderTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ConnectionTypeDef",
    "CreateConnectionInputRequestTypeDef",
    "CreateConnectionOutputTypeDef",
    "CreateHostInputRequestTypeDef",
    "CreateHostOutputTypeDef",
    "DeleteConnectionInputRequestTypeDef",
    "DeleteHostInputRequestTypeDef",
    "GetConnectionInputRequestTypeDef",
    "GetConnectionOutputTypeDef",
    "GetHostInputRequestTypeDef",
    "GetHostOutputTypeDef",
    "HostTypeDef",
    "ListConnectionsInputRequestTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListHostsInputRequestTypeDef",
    "ListHostsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateHostInputRequestTypeDef",
    "VpcConfigurationTypeDef",
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": ProviderTypeType,
        "OwnerAccountId": str,
        "ConnectionStatus": ConnectionStatusType,
        "HostArn": str,
    },
    total=False,
)

_RequiredCreateConnectionInputRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionInputRequestTypeDef",
    {
        "ConnectionName": str,
    },
)
_OptionalCreateConnectionInputRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionInputRequestTypeDef",
    {
        "ProviderType": ProviderTypeType,
        "Tags": List["TagTypeDef"],
        "HostArn": str,
    },
    total=False,
)

class CreateConnectionInputRequestTypeDef(
    _RequiredCreateConnectionInputRequestTypeDef, _OptionalCreateConnectionInputRequestTypeDef
):
    pass

CreateConnectionOutputTypeDef = TypedDict(
    "CreateConnectionOutputTypeDef",
    {
        "ConnectionArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHostInputRequestTypeDef = TypedDict(
    "_RequiredCreateHostInputRequestTypeDef",
    {
        "Name": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
    },
)
_OptionalCreateHostInputRequestTypeDef = TypedDict(
    "_OptionalCreateHostInputRequestTypeDef",
    {
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateHostInputRequestTypeDef(
    _RequiredCreateHostInputRequestTypeDef, _OptionalCreateHostInputRequestTypeDef
):
    pass

CreateHostOutputTypeDef = TypedDict(
    "CreateHostOutputTypeDef",
    {
        "HostArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionInputRequestTypeDef = TypedDict(
    "DeleteConnectionInputRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

DeleteHostInputRequestTypeDef = TypedDict(
    "DeleteHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)

GetConnectionInputRequestTypeDef = TypedDict(
    "GetConnectionInputRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

GetConnectionOutputTypeDef = TypedDict(
    "GetConnectionOutputTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostInputRequestTypeDef = TypedDict(
    "GetHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)

GetHostOutputTypeDef = TypedDict(
    "GetHostOutputTypeDef",
    {
        "Name": str,
        "Status": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "Name": str,
        "HostArn": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)

ListConnectionsInputRequestTypeDef = TypedDict(
    "ListConnectionsInputRequestTypeDef",
    {
        "ProviderTypeFilter": ProviderTypeType,
        "HostArnFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectionsOutputTypeDef = TypedDict(
    "ListConnectionsOutputTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostsInputRequestTypeDef = TypedDict(
    "ListHostsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHostsOutputTypeDef = TypedDict(
    "ListHostsOutputTypeDef",
    {
        "Hosts": List["HostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateHostInputRequestTypeDef = TypedDict(
    "_RequiredUpdateHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)
_OptionalUpdateHostInputRequestTypeDef = TypedDict(
    "_OptionalUpdateHostInputRequestTypeDef",
    {
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
    total=False,
)

class UpdateHostInputRequestTypeDef(
    _RequiredUpdateHostInputRequestTypeDef, _OptionalUpdateHostInputRequestTypeDef
):
    pass

_RequiredVpcConfigurationTypeDef = TypedDict(
    "_RequiredVpcConfigurationTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)
_OptionalVpcConfigurationTypeDef = TypedDict(
    "_OptionalVpcConfigurationTypeDef",
    {
        "TlsCertificate": str,
    },
    total=False,
)

class VpcConfigurationTypeDef(_RequiredVpcConfigurationTypeDef, _OptionalVpcConfigurationTypeDef):
    pass
