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
from typing import Union

from .literals import ClusterStatusType, EncryptionStatusType, EncryptionTypeType

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
    "DeleteClusterInputTypeDef",
    "DeleteClusterOutputTypeDef",
    "DeleteClusterPolicyInputTypeDef",
    "DeleteClusterPolicyOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionDetailsTypeDef",
    "GetClusterInputTypeDef",
    "GetClusterInputWaitExtraTypeDef",
    "GetClusterInputWaitTypeDef",
    "GetClusterOutputTypeDef",
    "GetClusterPolicyInputTypeDef",
    "GetClusterPolicyOutputTypeDef",
    "GetVpcEndpointServiceNameInputTypeDef",
    "GetVpcEndpointServiceNameOutputTypeDef",
    "ListClustersInputPaginateTypeDef",
    "ListClustersInputTypeDef",
    "ListClustersOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MultiRegionPropertiesOutputTypeDef",
    "MultiRegionPropertiesTypeDef",
    "MultiRegionPropertiesUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PutClusterPolicyInputTypeDef",
    "PutClusterPolicyOutputTypeDef",
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

class EncryptionDetailsTypeDef(TypedDict):
    encryptionType: EncryptionTypeType
    encryptionStatus: EncryptionStatusType
    kmsKeyArn: NotRequired[str]

class MultiRegionPropertiesOutputTypeDef(TypedDict):
    witnessRegion: NotRequired[str]
    clusters: NotRequired[List[str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteClusterInputTypeDef(TypedDict):
    identifier: str
    clientToken: NotRequired[str]

class DeleteClusterPolicyInputTypeDef(TypedDict):
    identifier: str
    expectedPolicyVersion: NotRequired[str]
    clientToken: NotRequired[str]

class GetClusterInputTypeDef(TypedDict):
    identifier: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetClusterPolicyInputTypeDef(TypedDict):
    identifier: str

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

class MultiRegionPropertiesTypeDef(TypedDict):
    witnessRegion: NotRequired[str]
    clusters: NotRequired[Sequence[str]]

class PutClusterPolicyInputTypeDef(TypedDict):
    identifier: str
    policy: str
    bypassPolicyLockoutSafetyCheck: NotRequired[bool]
    expectedPolicyVersion: NotRequired[str]
    clientToken: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    multiRegionProperties: MultiRegionPropertiesOutputTypeDef
    encryptionDetails: EncryptionDetailsTypeDef
    deletionProtectionEnabled: bool
    endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterPolicyOutputTypeDef(TypedDict):
    policyVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    multiRegionProperties: MultiRegionPropertiesOutputTypeDef
    tags: Dict[str, str]
    encryptionDetails: EncryptionDetailsTypeDef
    endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterPolicyOutputTypeDef(TypedDict):
    policy: str
    policyVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcEndpointServiceNameOutputTypeDef(TypedDict):
    serviceName: str
    clusterVpcEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersOutputTypeDef(TypedDict):
    clusters: List[ClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutClusterPolicyOutputTypeDef(TypedDict):
    policyVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterOutputTypeDef(TypedDict):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterInputWaitExtraTypeDef(TypedDict):
    identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetClusterInputWaitTypeDef(TypedDict):
    identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class ListClustersInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

MultiRegionPropertiesUnionTypeDef = Union[
    MultiRegionPropertiesTypeDef, MultiRegionPropertiesOutputTypeDef
]

class CreateClusterInputTypeDef(TypedDict):
    deletionProtectionEnabled: NotRequired[bool]
    kmsEncryptionKey: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    multiRegionProperties: NotRequired[MultiRegionPropertiesUnionTypeDef]
    policy: NotRequired[str]
    bypassPolicyLockoutSafetyCheck: NotRequired[bool]

class UpdateClusterInputTypeDef(TypedDict):
    identifier: str
    deletionProtectionEnabled: NotRequired[bool]
    kmsEncryptionKey: NotRequired[str]
    clientToken: NotRequired[str]
    multiRegionProperties: NotRequired[MultiRegionPropertiesUnionTypeDef]
