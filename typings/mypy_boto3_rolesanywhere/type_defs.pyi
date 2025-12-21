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
    threshold: NotRequired[int]
    channel: NotRequired[Literal["ALL"]]

class CredentialSummaryTypeDef(TypedDict):
    seenAt: NotRequired[datetime]
    serialNumber: NotRequired[str]
    issuer: NotRequired[str]
    enabled: NotRequired[bool]
    x509CertificateData: NotRequired[str]
    failed: NotRequired[bool]

class CrlDetailTypeDef(TypedDict):
    crlId: NotRequired[str]
    crlArn: NotRequired[str]
    name: NotRequired[str]
    enabled: NotRequired[bool]
    crlData: NotRequired[bytes]
    trustAnchorArn: NotRequired[str]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteAttributeMappingRequestTypeDef(TypedDict):
    profileId: str
    certificateField: CertificateFieldType
    specifiers: NotRequired[Sequence[str]]

class InstancePropertyTypeDef(TypedDict):
    seenAt: NotRequired[datetime]
    properties: NotRequired[Dict[str, str]]
    failed: NotRequired[bool]

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
    subjectArn: NotRequired[str]
    subjectId: NotRequired[str]
    enabled: NotRequired[bool]
    x509Subject: NotRequired[str]
    lastSeenAt: NotRequired[datetime]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class NotificationSettingDetailTypeDef(TypedDict):
    enabled: bool
    event: NotificationEventType
    threshold: NotRequired[int]
    channel: NotRequired[Literal["ALL"]]
    configuredBy: NotRequired[str]

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
    x509CertificateData: NotRequired[str]
    acmPcaArn: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateProfileRequestTypeDef(TypedDict):
    profileId: str
    name: NotRequired[str]
    sessionPolicy: NotRequired[str]
    roleArns: NotRequired[Sequence[str]]
    managedPolicyArns: NotRequired[Sequence[str]]
    durationSeconds: NotRequired[int]
    acceptRoleSessionName: NotRequired[bool]

class AttributeMappingTypeDef(TypedDict):
    certificateField: NotRequired[CertificateFieldType]
    mappingRules: NotRequired[List[MappingRuleTypeDef]]

class PutAttributeMappingRequestTypeDef(TypedDict):
    profileId: str
    certificateField: CertificateFieldType
    mappingRules: Sequence[MappingRuleTypeDef]

class UpdateCrlRequestTypeDef(TypedDict):
    crlId: str
    name: NotRequired[str]
    crlData: NotRequired[BlobTypeDef]

class CreateProfileRequestTypeDef(TypedDict):
    name: str
    roleArns: Sequence[str]
    requireInstanceProperties: NotRequired[bool]
    sessionPolicy: NotRequired[str]
    managedPolicyArns: NotRequired[Sequence[str]]
    durationSeconds: NotRequired[int]
    enabled: NotRequired[bool]
    tags: NotRequired[Sequence[TagTypeDef]]
    acceptRoleSessionName: NotRequired[bool]

class ImportCrlRequestTypeDef(TypedDict):
    name: str
    crlData: BlobTypeDef
    trustAnchorArn: str
    enabled: NotRequired[bool]
    tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class PutNotificationSettingsRequestTypeDef(TypedDict):
    trustAnchorId: str
    notificationSettings: Sequence[NotificationSettingTypeDef]

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
    subjectArn: NotRequired[str]
    subjectId: NotRequired[str]
    enabled: NotRequired[bool]
    x509Subject: NotRequired[str]
    lastSeenAt: NotRequired[datetime]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    credentials: NotRequired[List[CredentialSummaryTypeDef]]
    instanceProperties: NotRequired[List[InstancePropertyTypeDef]]

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
    trustAnchorId: str
    notificationSettingKeys: Sequence[NotificationSettingKeyTypeDef]

class SourceTypeDef(TypedDict):
    sourceType: NotRequired[TrustAnchorTypeType]
    sourceData: NotRequired[SourceDataTypeDef]

class ProfileDetailTypeDef(TypedDict):
    profileId: NotRequired[str]
    profileArn: NotRequired[str]
    name: NotRequired[str]
    requireInstanceProperties: NotRequired[bool]
    enabled: NotRequired[bool]
    createdBy: NotRequired[str]
    sessionPolicy: NotRequired[str]
    roleArns: NotRequired[List[str]]
    managedPolicyArns: NotRequired[List[str]]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    durationSeconds: NotRequired[int]
    acceptRoleSessionName: NotRequired[bool]
    attributeMappings: NotRequired[List[AttributeMappingTypeDef]]

class SubjectDetailResponseTypeDef(TypedDict):
    subject: SubjectDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustAnchorRequestTypeDef(TypedDict):
    name: str
    source: SourceTypeDef
    enabled: NotRequired[bool]
    tags: NotRequired[Sequence[TagTypeDef]]
    notificationSettings: NotRequired[Sequence[NotificationSettingTypeDef]]

class TrustAnchorDetailTypeDef(TypedDict):
    trustAnchorId: NotRequired[str]
    trustAnchorArn: NotRequired[str]
    name: NotRequired[str]
    source: NotRequired[SourceTypeDef]
    enabled: NotRequired[bool]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    notificationSettings: NotRequired[List[NotificationSettingDetailTypeDef]]

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
