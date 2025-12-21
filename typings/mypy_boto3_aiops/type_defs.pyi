"""
Type annotations for aiops service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_aiops/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_aiops.type_defs import CrossAccountConfigurationTypeDef

    data: CrossAccountConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import EncryptionConfigurationTypeType

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
    "CreateInvestigationGroupInputTypeDef",
    "CreateInvestigationGroupOutputTypeDef",
    "CrossAccountConfigurationTypeDef",
    "DeleteInvestigationGroupPolicyRequestTypeDef",
    "DeleteInvestigationGroupRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetInvestigationGroupPolicyRequestTypeDef",
    "GetInvestigationGroupPolicyResponseTypeDef",
    "GetInvestigationGroupRequestTypeDef",
    "GetInvestigationGroupResponseTypeDef",
    "ListInvestigationGroupsInputPaginateTypeDef",
    "ListInvestigationGroupsInputTypeDef",
    "ListInvestigationGroupsModelTypeDef",
    "ListInvestigationGroupsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutInvestigationGroupPolicyRequestTypeDef",
    "PutInvestigationGroupPolicyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateInvestigationGroupRequestTypeDef",
)

class CrossAccountConfigurationTypeDef(TypedDict):
    sourceRoleArn: NotRequired[str]

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "type": NotRequired[EncryptionConfigurationTypeType],
        "kmsKeyId": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteInvestigationGroupPolicyRequestTypeDef(TypedDict):
    identifier: str

class DeleteInvestigationGroupRequestTypeDef(TypedDict):
    identifier: str

class GetInvestigationGroupPolicyRequestTypeDef(TypedDict):
    identifier: str

class GetInvestigationGroupRequestTypeDef(TypedDict):
    identifier: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListInvestigationGroupsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListInvestigationGroupsModelTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PutInvestigationGroupPolicyRequestTypeDef(TypedDict):
    identifier: str
    policy: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateInvestigationGroupInputTypeDef(TypedDict):
    name: str
    roleArn: str
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    retentionInDays: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]
    tagKeyBoundaries: NotRequired[Sequence[str]]
    chatbotNotificationChannel: NotRequired[Mapping[str, Sequence[str]]]
    isCloudTrailEventHistoryEnabled: NotRequired[bool]
    crossAccountConfigurations: NotRequired[Sequence[CrossAccountConfigurationTypeDef]]

class UpdateInvestigationGroupRequestTypeDef(TypedDict):
    identifier: str
    roleArn: NotRequired[str]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    tagKeyBoundaries: NotRequired[Sequence[str]]
    chatbotNotificationChannel: NotRequired[Mapping[str, Sequence[str]]]
    isCloudTrailEventHistoryEnabled: NotRequired[bool]
    crossAccountConfigurations: NotRequired[Sequence[CrossAccountConfigurationTypeDef]]

class CreateInvestigationGroupOutputTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvestigationGroupPolicyResponseTypeDef(TypedDict):
    investigationGroupArn: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvestigationGroupResponseTypeDef(TypedDict):
    createdBy: str
    createdAt: int
    lastModifiedBy: str
    lastModifiedAt: int
    name: str
    arn: str
    roleArn: str
    encryptionConfiguration: EncryptionConfigurationTypeDef
    retentionInDays: int
    chatbotNotificationChannel: Dict[str, List[str]]
    tagKeyBoundaries: List[str]
    isCloudTrailEventHistoryEnabled: bool
    crossAccountConfigurations: List[CrossAccountConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutInvestigationGroupPolicyResponseTypeDef(TypedDict):
    investigationGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvestigationGroupsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInvestigationGroupsOutputTypeDef(TypedDict):
    investigationGroups: List[ListInvestigationGroupsModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
