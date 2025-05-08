"""
Type annotations for rolesanywhere service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_rolesanywhere.type_defs import MappingRuleTypeDef

    data: MappingRuleTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import CertificateFieldType, NotificationEventType, TrustAnchorTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AttributeMappingTypeDef",
    "BlobTypeDef",
    "CreateProfileRequestTypeDef",
    "CreateTrustAnchorRequestTypeDef",
    "CredentialSummaryTypeDef",
    "CrlDetailResponseTypeDef",
    "CrlDetailTypeDef",
    "DeleteAttributeMappingRequestTypeDef",
    "DeleteAttributeMappingResponseTypeDef",
    "ImportCrlRequestTypeDef",
    "InstancePropertyTypeDef",
    "ListCrlsResponseTypeDef",
    "ListProfilesResponseTypeDef",
    "ListRequestPaginateExtraExtraExtraTypeDef",
    "ListRequestPaginateExtraExtraTypeDef",
    "ListRequestPaginateExtraTypeDef",
    "ListRequestPaginateTypeDef",
    "ListRequestRequestExtraExtraTypeDef",
    "ListRequestRequestExtraTypeDef",
    "ListRequestRequestTypeDef",
    "ListRequestTypeDef",
    "ListSubjectsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustAnchorsResponseTypeDef",
    "MappingRuleTypeDef",
    "NotificationSettingDetailTypeDef",
    "NotificationSettingKeyTypeDef",
    "NotificationSettingTypeDef",
    "PaginatorConfigTypeDef",
    "ProfileDetailResponseTypeDef",
    "ProfileDetailTypeDef",
    "PutAttributeMappingRequestTypeDef",
    "PutAttributeMappingResponseTypeDef",
    "PutNotificationSettingsRequestTypeDef",
    "PutNotificationSettingsResponseTypeDef",
    "ResetNotificationSettingsRequestTypeDef",
    "ResetNotificationSettingsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ScalarCrlRequestRequestExtraExtraTypeDef",
    "ScalarCrlRequestRequestExtraTypeDef",
    "ScalarCrlRequestRequestTypeDef",
    "ScalarCrlRequestTypeDef",
    "ScalarProfileRequestRequestExtraExtraTypeDef",
    "ScalarProfileRequestRequestExtraTypeDef",
    "ScalarProfileRequestRequestTypeDef",
    "ScalarProfileRequestTypeDef",
    "ScalarSubjectRequestTypeDef",
    "ScalarTrustAnchorRequestRequestExtraExtraTypeDef",
    "ScalarTrustAnchorRequestRequestExtraTypeDef",
    "ScalarTrustAnchorRequestRequestTypeDef",
    "ScalarTrustAnchorRequestTypeDef",
    "SourceDataTypeDef",
    "SourceTypeDef",
    "SubjectDetailResponseTypeDef",
    "SubjectDetailTypeDef",
    "SubjectSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TrustAnchorDetailResponseTypeDef",
    "TrustAnchorDetailTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCrlRequestTypeDef",
    "UpdateProfileRequestTypeDef",
    "UpdateTrustAnchorRequestTypeDef",
)

class MappingRuleTypeDef(TypedDict):
    specifier: str

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class TagTypeDef(TypedDict):
    key: str
    value: str

class NotificationSettingTypeDef(TypedDict):
    enabled: bool
    event: NotificationEventType
    channel: NotRequired[Literal["ALL"]]
    threshold: NotRequired[int]

class CredentialSummaryTypeDef(TypedDict):
    enabled: NotRequired[bool]
    failed: NotRequired[bool]
    issuer: NotRequired[str]
    seenAt: NotRequired[datetime]
    serialNumber: NotRequired[str]
    x509CertificateData: NotRequired[str]

class CrlDetailTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    crlArn: NotRequired[str]
    crlData: NotRequired[bytes]
    crlId: NotRequired[str]
    enabled: NotRequired[bool]
    name: NotRequired[str]
    trustAnchorArn: NotRequired[str]
    updatedAt: NotRequired[datetime]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteAttributeMappingRequestTypeDef(TypedDict):
    certificateField: CertificateFieldType
    profileId: str
    specifiers: NotRequired[Sequence[str]]

class InstancePropertyTypeDef(TypedDict):
    failed: NotRequired[bool]
    properties: NotRequired[Dict[str, str]]
    seenAt: NotRequired[datetime]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListRequestRequestExtraExtraTypeDef(TypedDict):
    nextToken: NotRequired[str]
    pageSize: NotRequired[int]

class ListRequestRequestExtraTypeDef(TypedDict):
    nextToken: NotRequired[str]
    pageSize: NotRequired[int]

class ListRequestRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    pageSize: NotRequired[int]

class ListRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    pageSize: NotRequired[int]

class SubjectSummaryTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    enabled: NotRequired[bool]
    lastSeenAt: NotRequired[datetime]
    subjectArn: NotRequired[str]
    subjectId: NotRequired[str]
    updatedAt: NotRequired[datetime]
    x509Subject: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class NotificationSettingDetailTypeDef(TypedDict):
    enabled: bool
    event: NotificationEventType
    channel: NotRequired[Literal["ALL"]]
    configuredBy: NotRequired[str]
    threshold: NotRequired[int]

class NotificationSettingKeyTypeDef(TypedDict):
    event: NotificationEventType
    channel: NotRequired[Literal["ALL"]]

class ScalarCrlRequestRequestExtraExtraTypeDef(TypedDict):
    crlId: str

class ScalarCrlRequestRequestExtraTypeDef(TypedDict):
    crlId: str

class ScalarCrlRequestRequestTypeDef(TypedDict):
    crlId: str

class ScalarCrlRequestTypeDef(TypedDict):
    crlId: str

class ScalarProfileRequestRequestExtraExtraTypeDef(TypedDict):
    profileId: str

class ScalarProfileRequestRequestExtraTypeDef(TypedDict):
    profileId: str

class ScalarProfileRequestRequestTypeDef(TypedDict):
    profileId: str

class ScalarProfileRequestTypeDef(TypedDict):
    profileId: str

class ScalarSubjectRequestTypeDef(TypedDict):
    subjectId: str

class ScalarTrustAnchorRequestRequestExtraExtraTypeDef(TypedDict):
    trustAnchorId: str

class ScalarTrustAnchorRequestRequestExtraTypeDef(TypedDict):
    trustAnchorId: str

class ScalarTrustAnchorRequestRequestTypeDef(TypedDict):
    trustAnchorId: str

class ScalarTrustAnchorRequestTypeDef(TypedDict):
    trustAnchorId: str

class SourceDataTypeDef(TypedDict):
    acmPcaArn: NotRequired[str]
    x509CertificateData: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateProfileRequestTypeDef(TypedDict):
    profileId: str
    acceptRoleSessionName: NotRequired[bool]
    durationSeconds: NotRequired[int]
    managedPolicyArns: NotRequired[Sequence[str]]
    name: NotRequired[str]
    roleArns: NotRequired[Sequence[str]]
    sessionPolicy: NotRequired[str]

class AttributeMappingTypeDef(TypedDict):
    certificateField: NotRequired[CertificateFieldType]
    mappingRules: NotRequired[List[MappingRuleTypeDef]]

class PutAttributeMappingRequestTypeDef(TypedDict):
    certificateField: CertificateFieldType
    mappingRules: Sequence[MappingRuleTypeDef]
    profileId: str

class UpdateCrlRequestTypeDef(TypedDict):
    crlId: str
    crlData: NotRequired[BlobTypeDef]
    name: NotRequired[str]

class CreateProfileRequestTypeDef(TypedDict):
    name: str
    roleArns: Sequence[str]
    acceptRoleSessionName: NotRequired[bool]
    durationSeconds: NotRequired[int]
    enabled: NotRequired[bool]
    managedPolicyArns: NotRequired[Sequence[str]]
    requireInstanceProperties: NotRequired[bool]
    sessionPolicy: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class ImportCrlRequestTypeDef(TypedDict):
    crlData: BlobTypeDef
    name: str
    trustAnchorArn: str
    enabled: NotRequired[bool]
    tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class PutNotificationSettingsRequestTypeDef(TypedDict):
    notificationSettings: Sequence[NotificationSettingTypeDef]
    trustAnchorId: str

class CrlDetailResponseTypeDef(TypedDict):
    crl: CrlDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrlsResponseTypeDef(TypedDict):
    crls: List[CrlDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubjectDetailTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    credentials: NotRequired[List[CredentialSummaryTypeDef]]
    enabled: NotRequired[bool]
    instanceProperties: NotRequired[List[InstancePropertyTypeDef]]
    lastSeenAt: NotRequired[datetime]
    subjectArn: NotRequired[str]
    subjectId: NotRequired[str]
    updatedAt: NotRequired[datetime]
    x509Subject: NotRequired[str]

class ListRequestPaginateExtraExtraExtraTypeDef(TypedDict):
    pageSize: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRequestPaginateExtraExtraTypeDef(TypedDict):
    pageSize: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRequestPaginateExtraTypeDef(TypedDict):
    pageSize: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRequestPaginateTypeDef(TypedDict):
    pageSize: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubjectsResponseTypeDef(TypedDict):
    subjects: List[SubjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ResetNotificationSettingsRequestTypeDef(TypedDict):
    notificationSettingKeys: Sequence[NotificationSettingKeyTypeDef]
    trustAnchorId: str

class SourceTypeDef(TypedDict):
    sourceData: NotRequired[SourceDataTypeDef]
    sourceType: NotRequired[TrustAnchorTypeType]

class ProfileDetailTypeDef(TypedDict):
    acceptRoleSessionName: NotRequired[bool]
    attributeMappings: NotRequired[List[AttributeMappingTypeDef]]
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    durationSeconds: NotRequired[int]
    enabled: NotRequired[bool]
    managedPolicyArns: NotRequired[List[str]]
    name: NotRequired[str]
    profileArn: NotRequired[str]
    profileId: NotRequired[str]
    requireInstanceProperties: NotRequired[bool]
    roleArns: NotRequired[List[str]]
    sessionPolicy: NotRequired[str]
    updatedAt: NotRequired[datetime]

class SubjectDetailResponseTypeDef(TypedDict):
    subject: SubjectDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustAnchorRequestTypeDef(TypedDict):
    name: str
    source: SourceTypeDef
    enabled: NotRequired[bool]
    notificationSettings: NotRequired[Sequence[NotificationSettingTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class TrustAnchorDetailTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    enabled: NotRequired[bool]
    name: NotRequired[str]
    notificationSettings: NotRequired[List[NotificationSettingDetailTypeDef]]
    source: NotRequired[SourceTypeDef]
    trustAnchorArn: NotRequired[str]
    trustAnchorId: NotRequired[str]
    updatedAt: NotRequired[datetime]

class UpdateTrustAnchorRequestTypeDef(TypedDict):
    trustAnchorId: str
    name: NotRequired[str]
    source: NotRequired[SourceTypeDef]

class DeleteAttributeMappingResponseTypeDef(TypedDict):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilesResponseTypeDef(TypedDict):
    profiles: List[ProfileDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ProfileDetailResponseTypeDef(TypedDict):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAttributeMappingResponseTypeDef(TypedDict):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustAnchorsResponseTypeDef(TypedDict):
    trustAnchors: List[TrustAnchorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutNotificationSettingsResponseTypeDef(TypedDict):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetNotificationSettingsResponseTypeDef(TypedDict):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TrustAnchorDetailResponseTypeDef(TypedDict):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
