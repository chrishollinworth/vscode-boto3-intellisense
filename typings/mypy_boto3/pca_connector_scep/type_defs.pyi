"""
Type annotations for pca-connector-scep service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pca_connector_scep.type_defs import ChallengeMetadataSummaryTypeDef

    data: ChallengeMetadataSummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ConnectorStatusReasonType, ConnectorStatusType, ConnectorTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ChallengeMetadataSummaryTypeDef",
    "ChallengeMetadataTypeDef",
    "ChallengeTypeDef",
    "ConnectorSummaryTypeDef",
    "ConnectorTypeDef",
    "CreateChallengeRequestRequestTypeDef",
    "CreateChallengeResponseTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "DeleteChallengeRequestRequestTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "GetChallengeMetadataRequestRequestTypeDef",
    "GetChallengeMetadataResponseTypeDef",
    "GetChallengePasswordRequestRequestTypeDef",
    "GetChallengePasswordResponseTypeDef",
    "GetConnectorRequestRequestTypeDef",
    "GetConnectorResponseTypeDef",
    "IntuneConfigurationTypeDef",
    "ListChallengeMetadataRequestRequestTypeDef",
    "ListChallengeMetadataResponseTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MobileDeviceManagementTypeDef",
    "OpenIdConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

ChallengeMetadataSummaryTypeDef = TypedDict(
    "ChallengeMetadataSummaryTypeDef",
    {
        "Arn": str,
        "ConnectorArn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ChallengeMetadataTypeDef = TypedDict(
    "ChallengeMetadataTypeDef",
    {
        "Arn": str,
        "ConnectorArn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ChallengeTypeDef = TypedDict(
    "ChallengeTypeDef",
    {
        "Arn": str,
        "ConnectorArn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Password": str,
    },
    total=False,
)

ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "Arn": str,
        "CertificateAuthorityArn": str,
        "Type": ConnectorTypeType,
        "MobileDeviceManagement": "MobileDeviceManagementTypeDef",
        "OpenIdConfiguration": "OpenIdConfigurationTypeDef",
        "Status": ConnectorStatusType,
        "StatusReason": ConnectorStatusReasonType,
        "Endpoint": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "Arn": str,
        "CertificateAuthorityArn": str,
        "Type": ConnectorTypeType,
        "MobileDeviceManagement": "MobileDeviceManagementTypeDef",
        "OpenIdConfiguration": "OpenIdConfigurationTypeDef",
        "Status": ConnectorStatusType,
        "StatusReason": ConnectorStatusReasonType,
        "Endpoint": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

_RequiredCreateChallengeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChallengeRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)
_OptionalCreateChallengeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChallengeRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateChallengeRequestRequestTypeDef(
    _RequiredCreateChallengeRequestRequestTypeDef, _OptionalCreateChallengeRequestRequestTypeDef
):
    pass

CreateChallengeResponseTypeDef = TypedDict(
    "CreateChallengeResponseTypeDef",
    {
        "Challenge": "ChallengeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalCreateConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorRequestRequestTypeDef",
    {
        "MobileDeviceManagement": "MobileDeviceManagementTypeDef",
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateConnectorRequestRequestTypeDef(
    _RequiredCreateConnectorRequestRequestTypeDef, _OptionalCreateConnectorRequestRequestTypeDef
):
    pass

CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "ConnectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChallengeRequestRequestTypeDef = TypedDict(
    "DeleteChallengeRequestRequestTypeDef",
    {
        "ChallengeArn": str,
    },
)

DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)

GetChallengeMetadataRequestRequestTypeDef = TypedDict(
    "GetChallengeMetadataRequestRequestTypeDef",
    {
        "ChallengeArn": str,
    },
)

GetChallengeMetadataResponseTypeDef = TypedDict(
    "GetChallengeMetadataResponseTypeDef",
    {
        "ChallengeMetadata": "ChallengeMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChallengePasswordRequestRequestTypeDef = TypedDict(
    "GetChallengePasswordRequestRequestTypeDef",
    {
        "ChallengeArn": str,
    },
)

GetChallengePasswordResponseTypeDef = TypedDict(
    "GetChallengePasswordResponseTypeDef",
    {
        "Password": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorRequestRequestTypeDef = TypedDict(
    "GetConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)

GetConnectorResponseTypeDef = TypedDict(
    "GetConnectorResponseTypeDef",
    {
        "Connector": "ConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntuneConfigurationTypeDef = TypedDict(
    "IntuneConfigurationTypeDef",
    {
        "AzureApplicationId": str,
        "Domain": str,
    },
)

_RequiredListChallengeMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredListChallengeMetadataRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)
_OptionalListChallengeMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalListChallengeMetadataRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChallengeMetadataRequestRequestTypeDef(
    _RequiredListChallengeMetadataRequestRequestTypeDef,
    _OptionalListChallengeMetadataRequestRequestTypeDef,
):
    pass

ListChallengeMetadataResponseTypeDef = TypedDict(
    "ListChallengeMetadataResponseTypeDef",
    {
        "Challenges": List["ChallengeMetadataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "Connectors": List["ConnectorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MobileDeviceManagementTypeDef = TypedDict(
    "MobileDeviceManagementTypeDef",
    {
        "Intune": "IntuneConfigurationTypeDef",
    },
    total=False,
)

OpenIdConfigurationTypeDef = TypedDict(
    "OpenIdConfigurationTypeDef",
    {
        "Issuer": str,
        "Subject": str,
        "Audience": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
