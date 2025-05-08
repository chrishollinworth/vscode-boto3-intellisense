"""
Type annotations for dsql service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_dsql.type_defs import ClusterSummaryTypeDef

    data: ClusterSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import ClusterStatusType

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
    "ClusterSummaryTypeDef",
    "CreateClusterInputTypeDef",
    "CreateClusterOutputTypeDef",
    "CreateMultiRegionClustersInputTypeDef",
    "CreateMultiRegionClustersOutputTypeDef",
    "DeleteClusterInputTypeDef",
    "DeleteClusterOutputTypeDef",
    "DeleteMultiRegionClustersInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetClusterInputTypeDef",
    "GetClusterInputWaitExtraTypeDef",
    "GetClusterInputWaitTypeDef",
    "GetClusterOutputTypeDef",
    "GetVpcEndpointServiceNameInputTypeDef",
    "GetVpcEndpointServiceNameOutputTypeDef",
    "LinkedClusterPropertiesTypeDef",
    "ListClustersInputPaginateTypeDef",
    "ListClustersInputTypeDef",
    "ListClustersOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateClusterInputTypeDef",
    "UpdateClusterOutputTypeDef",
    "WaiterConfigTypeDef",
)

class ClusterSummaryTypeDef(TypedDict):
    identifier: str
    arn: str

class CreateClusterInputTypeDef(TypedDict):
    deletionProtectionEnabled: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class LinkedClusterPropertiesTypeDef(TypedDict):
    deletionProtectionEnabled: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class DeleteClusterInputTypeDef(TypedDict):
    identifier: str
    clientToken: NotRequired[str]

class DeleteMultiRegionClustersInputTypeDef(TypedDict):
    linkedClusterArns: Sequence[str]
    clientToken: NotRequired[str]

class GetClusterInputTypeDef(TypedDict):
    identifier: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetVpcEndpointServiceNameInputTypeDef(TypedDict):
    identifier: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListClustersInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateClusterInputTypeDef(TypedDict):
    identifier: str
    deletionProtectionEnabled: NotRequired[bool]
    clientToken: NotRequired[str]

class CreateClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultiRegionClustersOutputTypeDef(TypedDict):
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcEndpointServiceNameOutputTypeDef(TypedDict):
    serviceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersOutputTypeDef(TypedDict):
    clusters: List[ClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultiRegionClustersInputTypeDef(TypedDict):
    linkedRegionList: Sequence[str]
    witnessRegion: str
    clusterProperties: NotRequired[Mapping[str, LinkedClusterPropertiesTypeDef]]
    clientToken: NotRequired[str]

class GetClusterInputWaitExtraTypeDef(TypedDict):
    identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetClusterInputWaitTypeDef(TypedDict):
    identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class ListClustersInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]
