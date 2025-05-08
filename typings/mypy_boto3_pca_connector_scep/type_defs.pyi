"""
Type annotations for pca-connector-scep service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_pca_connector_scep.type_defs import ChallengeMetadataSummaryTypeDef

    data: ChallengeMetadataSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import ConnectorStatusReasonType, ConnectorStatusType, ConnectorTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ChallengeMetadataSummaryTypeDef",
    "ChallengeMetadataTypeDef",
    "ChallengeTypeDef",
    "ConnectorSummaryTypeDef",
    "ConnectorTypeDef",
    "CreateChallengeRequestTypeDef",
    "CreateChallengeResponseTypeDef",
    "CreateConnectorRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "DeleteChallengeRequestTypeDef",
    "DeleteConnectorRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetChallengeMetadataRequestTypeDef",
    "GetChallengeMetadataResponseTypeDef",
    "GetChallengePasswordRequestTypeDef",
    "GetChallengePasswordResponseTypeDef",
    "GetConnectorRequestTypeDef",
    "GetConnectorResponseTypeDef",
    "IntuneConfigurationTypeDef",
    "ListChallengeMetadataRequestPaginateTypeDef",
    "ListChallengeMetadataRequestTypeDef",
    "ListChallengeMetadataResponseTypeDef",
    "ListConnectorsRequestPaginateTypeDef",
    "ListConnectorsRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MobileDeviceManagementTypeDef",
    "OpenIdConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
)

class ChallengeMetadataSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    ConnectorArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]

class ChallengeMetadataTypeDef(TypedDict):
    Arn: NotRequired[str]
    ConnectorArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]

class ChallengeTypeDef(TypedDict):
    Arn: NotRequired[str]
    ConnectorArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    Password: NotRequired[str]

class OpenIdConfigurationTypeDef(TypedDict):
    Issuer: NotRequired[str]
    Subject: NotRequired[str]
    Audience: NotRequired[str]

class CreateChallengeRequestTypeDef(TypedDict):
    ConnectorArn: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteChallengeRequestTypeDef(TypedDict):
    ChallengeArn: str

class DeleteConnectorRequestTypeDef(TypedDict):
    ConnectorArn: str

class GetChallengeMetadataRequestTypeDef(TypedDict):
    ChallengeArn: str

class GetChallengePasswordRequestTypeDef(TypedDict):
    ChallengeArn: str

class GetConnectorRequestTypeDef(TypedDict):
    ConnectorArn: str

class IntuneConfigurationTypeDef(TypedDict):
    AzureApplicationId: str
    Domain: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChallengeMetadataRequestTypeDef(TypedDict):
    ConnectorArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListConnectorsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateChallengeResponseTypeDef(TypedDict):
    Challenge: ChallengeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorResponseTypeDef(TypedDict):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChallengeMetadataResponseTypeDef(TypedDict):
    ChallengeMetadata: ChallengeMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChallengePasswordResponseTypeDef(TypedDict):
    Password: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChallengeMetadataResponseTypeDef(TypedDict):
    Challenges: List[ChallengeMetadataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MobileDeviceManagementTypeDef(TypedDict):
    Intune: NotRequired[IntuneConfigurationTypeDef]

class ListChallengeMetadataRequestPaginateTypeDef(TypedDict):
    ConnectorArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "Type": NotRequired[ConnectorTypeType],
        "MobileDeviceManagement": NotRequired[MobileDeviceManagementTypeDef],
        "OpenIdConfiguration": NotRequired[OpenIdConfigurationTypeDef],
        "Status": NotRequired[ConnectorStatusType],
        "StatusReason": NotRequired[ConnectorStatusReasonType],
        "Endpoint": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "Type": NotRequired[ConnectorTypeType],
        "MobileDeviceManagement": NotRequired[MobileDeviceManagementTypeDef],
        "OpenIdConfiguration": NotRequired[OpenIdConfigurationTypeDef],
        "Status": NotRequired[ConnectorStatusType],
        "StatusReason": NotRequired[ConnectorStatusReasonType],
        "Endpoint": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)

class CreateConnectorRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    MobileDeviceManagement: NotRequired[MobileDeviceManagementTypeDef]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ListConnectorsResponseTypeDef(TypedDict):
    Connectors: List[ConnectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetConnectorResponseTypeDef(TypedDict):
    Connector: ConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
