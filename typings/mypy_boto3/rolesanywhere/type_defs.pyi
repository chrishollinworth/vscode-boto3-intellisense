"""
Type annotations for rolesanywhere service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rolesanywhere.type_defs import AttributeMappingTypeDef

    data: AttributeMappingTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import CertificateFieldType, NotificationEventType, TrustAnchorTypeType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AttributeMappingTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateTrustAnchorRequestRequestTypeDef",
    "CredentialSummaryTypeDef",
    "CrlDetailResponseTypeDef",
    "CrlDetailTypeDef",
    "DeleteAttributeMappingRequestRequestTypeDef",
    "DeleteAttributeMappingResponseTypeDef",
    "ImportCrlRequestRequestTypeDef",
    "InstancePropertyTypeDef",
    "ListCrlsResponseTypeDef",
    "ListProfilesResponseTypeDef",
    "ListRequestRequestTypeDef",
    "ListSubjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustAnchorsResponseTypeDef",
    "MappingRuleTypeDef",
    "NotificationSettingDetailTypeDef",
    "NotificationSettingKeyTypeDef",
    "NotificationSettingTypeDef",
    "PaginatorConfigTypeDef",
    "ProfileDetailResponseTypeDef",
    "ProfileDetailTypeDef",
    "PutAttributeMappingRequestRequestTypeDef",
    "PutAttributeMappingResponseTypeDef",
    "PutNotificationSettingsRequestRequestTypeDef",
    "PutNotificationSettingsResponseTypeDef",
    "ResetNotificationSettingsRequestRequestTypeDef",
    "ResetNotificationSettingsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ScalarCrlRequestRequestTypeDef",
    "ScalarProfileRequestRequestTypeDef",
    "ScalarSubjectRequestRequestTypeDef",
    "ScalarTrustAnchorRequestRequestTypeDef",
    "SourceDataTypeDef",
    "SourceTypeDef",
    "SubjectDetailResponseTypeDef",
    "SubjectDetailTypeDef",
    "SubjectSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrustAnchorDetailResponseTypeDef",
    "TrustAnchorDetailTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCrlRequestRequestTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "UpdateTrustAnchorRequestRequestTypeDef",
)

AttributeMappingTypeDef = TypedDict(
    "AttributeMappingTypeDef",
    {
        "certificateField": CertificateFieldType,
        "mappingRules": List["MappingRuleTypeDef"],
    },
    total=False,
)

_RequiredCreateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestRequestTypeDef",
    {
        "name": str,
        "roleArns": List[str],
    },
)
_OptionalCreateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestRequestTypeDef",
    {
        "durationSeconds": int,
        "enabled": bool,
        "managedPolicyArns": List[str],
        "requireInstanceProperties": bool,
        "sessionPolicy": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProfileRequestRequestTypeDef(
    _RequiredCreateProfileRequestRequestTypeDef, _OptionalCreateProfileRequestRequestTypeDef
):
    pass

_RequiredCreateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrustAnchorRequestRequestTypeDef",
    {
        "name": str,
        "source": "SourceTypeDef",
    },
)
_OptionalCreateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrustAnchorRequestRequestTypeDef",
    {
        "enabled": bool,
        "notificationSettings": List["NotificationSettingTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrustAnchorRequestRequestTypeDef(
    _RequiredCreateTrustAnchorRequestRequestTypeDef, _OptionalCreateTrustAnchorRequestRequestTypeDef
):
    pass

CredentialSummaryTypeDef = TypedDict(
    "CredentialSummaryTypeDef",
    {
        "enabled": bool,
        "failed": bool,
        "issuer": str,
        "seenAt": datetime,
        "serialNumber": str,
        "x509CertificateData": str,
    },
    total=False,
)

CrlDetailResponseTypeDef = TypedDict(
    "CrlDetailResponseTypeDef",
    {
        "crl": "CrlDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CrlDetailTypeDef = TypedDict(
    "CrlDetailTypeDef",
    {
        "createdAt": datetime,
        "crlArn": str,
        "crlData": bytes,
        "crlId": str,
        "enabled": bool,
        "name": str,
        "trustAnchorArn": str,
        "updatedAt": datetime,
    },
    total=False,
)

_RequiredDeleteAttributeMappingRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAttributeMappingRequestRequestTypeDef",
    {
        "certificateField": CertificateFieldType,
        "profileId": str,
    },
)
_OptionalDeleteAttributeMappingRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAttributeMappingRequestRequestTypeDef",
    {
        "specifiers": List[str],
    },
    total=False,
)

class DeleteAttributeMappingRequestRequestTypeDef(
    _RequiredDeleteAttributeMappingRequestRequestTypeDef,
    _OptionalDeleteAttributeMappingRequestRequestTypeDef,
):
    pass

DeleteAttributeMappingResponseTypeDef = TypedDict(
    "DeleteAttributeMappingResponseTypeDef",
    {
        "profile": "ProfileDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportCrlRequestRequestTypeDef = TypedDict(
    "_RequiredImportCrlRequestRequestTypeDef",
    {
        "crlData": Union[bytes, IO[bytes], StreamingBody],
        "name": str,
        "trustAnchorArn": str,
    },
)
_OptionalImportCrlRequestRequestTypeDef = TypedDict(
    "_OptionalImportCrlRequestRequestTypeDef",
    {
        "enabled": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportCrlRequestRequestTypeDef(
    _RequiredImportCrlRequestRequestTypeDef, _OptionalImportCrlRequestRequestTypeDef
):
    pass

InstancePropertyTypeDef = TypedDict(
    "InstancePropertyTypeDef",
    {
        "failed": bool,
        "properties": Dict[str, str],
        "seenAt": datetime,
    },
    total=False,
)

ListCrlsResponseTypeDef = TypedDict(
    "ListCrlsResponseTypeDef",
    {
        "crls": List["CrlDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "nextToken": str,
        "profiles": List["ProfileDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRequestRequestTypeDef = TypedDict(
    "ListRequestRequestTypeDef",
    {
        "nextToken": str,
        "pageSize": int,
    },
    total=False,
)

ListSubjectsResponseTypeDef = TypedDict(
    "ListSubjectsResponseTypeDef",
    {
        "nextToken": str,
        "subjects": List["SubjectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrustAnchorsResponseTypeDef = TypedDict(
    "ListTrustAnchorsResponseTypeDef",
    {
        "nextToken": str,
        "trustAnchors": List["TrustAnchorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MappingRuleTypeDef = TypedDict(
    "MappingRuleTypeDef",
    {
        "specifier": str,
    },
)

_RequiredNotificationSettingDetailTypeDef = TypedDict(
    "_RequiredNotificationSettingDetailTypeDef",
    {
        "enabled": bool,
        "event": NotificationEventType,
    },
)
_OptionalNotificationSettingDetailTypeDef = TypedDict(
    "_OptionalNotificationSettingDetailTypeDef",
    {
        "channel": Literal["ALL"],
        "configuredBy": str,
        "threshold": int,
    },
    total=False,
)

class NotificationSettingDetailTypeDef(
    _RequiredNotificationSettingDetailTypeDef, _OptionalNotificationSettingDetailTypeDef
):
    pass

_RequiredNotificationSettingKeyTypeDef = TypedDict(
    "_RequiredNotificationSettingKeyTypeDef",
    {
        "event": NotificationEventType,
    },
)
_OptionalNotificationSettingKeyTypeDef = TypedDict(
    "_OptionalNotificationSettingKeyTypeDef",
    {
        "channel": Literal["ALL"],
    },
    total=False,
)

class NotificationSettingKeyTypeDef(
    _RequiredNotificationSettingKeyTypeDef, _OptionalNotificationSettingKeyTypeDef
):
    pass

_RequiredNotificationSettingTypeDef = TypedDict(
    "_RequiredNotificationSettingTypeDef",
    {
        "enabled": bool,
        "event": NotificationEventType,
    },
)
_OptionalNotificationSettingTypeDef = TypedDict(
    "_OptionalNotificationSettingTypeDef",
    {
        "channel": Literal["ALL"],
        "threshold": int,
    },
    total=False,
)

class NotificationSettingTypeDef(
    _RequiredNotificationSettingTypeDef, _OptionalNotificationSettingTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ProfileDetailResponseTypeDef = TypedDict(
    "ProfileDetailResponseTypeDef",
    {
        "profile": "ProfileDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProfileDetailTypeDef = TypedDict(
    "ProfileDetailTypeDef",
    {
        "attributeMappings": List["AttributeMappingTypeDef"],
        "createdAt": datetime,
        "createdBy": str,
        "durationSeconds": int,
        "enabled": bool,
        "managedPolicyArns": List[str],
        "name": str,
        "profileArn": str,
        "profileId": str,
        "requireInstanceProperties": bool,
        "roleArns": List[str],
        "sessionPolicy": str,
        "updatedAt": datetime,
    },
    total=False,
)

PutAttributeMappingRequestRequestTypeDef = TypedDict(
    "PutAttributeMappingRequestRequestTypeDef",
    {
        "certificateField": CertificateFieldType,
        "mappingRules": List["MappingRuleTypeDef"],
        "profileId": str,
    },
)

PutAttributeMappingResponseTypeDef = TypedDict(
    "PutAttributeMappingResponseTypeDef",
    {
        "profile": "ProfileDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutNotificationSettingsRequestRequestTypeDef = TypedDict(
    "PutNotificationSettingsRequestRequestTypeDef",
    {
        "notificationSettings": List["NotificationSettingTypeDef"],
        "trustAnchorId": str,
    },
)

PutNotificationSettingsResponseTypeDef = TypedDict(
    "PutNotificationSettingsResponseTypeDef",
    {
        "trustAnchor": "TrustAnchorDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetNotificationSettingsRequestRequestTypeDef = TypedDict(
    "ResetNotificationSettingsRequestRequestTypeDef",
    {
        "notificationSettingKeys": List["NotificationSettingKeyTypeDef"],
        "trustAnchorId": str,
    },
)

ResetNotificationSettingsResponseTypeDef = TypedDict(
    "ResetNotificationSettingsResponseTypeDef",
    {
        "trustAnchor": "TrustAnchorDetailTypeDef",
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

ScalarCrlRequestRequestTypeDef = TypedDict(
    "ScalarCrlRequestRequestTypeDef",
    {
        "crlId": str,
    },
)

ScalarProfileRequestRequestTypeDef = TypedDict(
    "ScalarProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)

ScalarSubjectRequestRequestTypeDef = TypedDict(
    "ScalarSubjectRequestRequestTypeDef",
    {
        "subjectId": str,
    },
)

ScalarTrustAnchorRequestRequestTypeDef = TypedDict(
    "ScalarTrustAnchorRequestRequestTypeDef",
    {
        "trustAnchorId": str,
    },
)

SourceDataTypeDef = TypedDict(
    "SourceDataTypeDef",
    {
        "acmPcaArn": str,
        "x509CertificateData": str,
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "sourceData": "SourceDataTypeDef",
        "sourceType": TrustAnchorTypeType,
    },
    total=False,
)

SubjectDetailResponseTypeDef = TypedDict(
    "SubjectDetailResponseTypeDef",
    {
        "subject": "SubjectDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubjectDetailTypeDef = TypedDict(
    "SubjectDetailTypeDef",
    {
        "createdAt": datetime,
        "credentials": List["CredentialSummaryTypeDef"],
        "enabled": bool,
        "instanceProperties": List["InstancePropertyTypeDef"],
        "lastSeenAt": datetime,
        "subjectArn": str,
        "subjectId": str,
        "updatedAt": datetime,
        "x509Subject": str,
    },
    total=False,
)

SubjectSummaryTypeDef = TypedDict(
    "SubjectSummaryTypeDef",
    {
        "createdAt": datetime,
        "enabled": bool,
        "lastSeenAt": datetime,
        "subjectArn": str,
        "subjectId": str,
        "updatedAt": datetime,
        "x509Subject": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TrustAnchorDetailResponseTypeDef = TypedDict(
    "TrustAnchorDetailResponseTypeDef",
    {
        "trustAnchor": "TrustAnchorDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TrustAnchorDetailTypeDef = TypedDict(
    "TrustAnchorDetailTypeDef",
    {
        "createdAt": datetime,
        "enabled": bool,
        "name": str,
        "notificationSettings": List["NotificationSettingDetailTypeDef"],
        "source": "SourceTypeDef",
        "trustAnchorArn": str,
        "trustAnchorId": str,
        "updatedAt": datetime,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateCrlRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCrlRequestRequestTypeDef",
    {
        "crlId": str,
    },
)
_OptionalUpdateCrlRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCrlRequestRequestTypeDef",
    {
        "crlData": Union[bytes, IO[bytes], StreamingBody],
        "name": str,
    },
    total=False,
)

class UpdateCrlRequestRequestTypeDef(
    _RequiredUpdateCrlRequestRequestTypeDef, _OptionalUpdateCrlRequestRequestTypeDef
):
    pass

_RequiredUpdateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)
_OptionalUpdateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileRequestRequestTypeDef",
    {
        "durationSeconds": int,
        "managedPolicyArns": List[str],
        "name": str,
        "roleArns": List[str],
        "sessionPolicy": str,
    },
    total=False,
)

class UpdateProfileRequestRequestTypeDef(
    _RequiredUpdateProfileRequestRequestTypeDef, _OptionalUpdateProfileRequestRequestTypeDef
):
    pass

_RequiredUpdateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustAnchorRequestRequestTypeDef",
    {
        "trustAnchorId": str,
    },
)
_OptionalUpdateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustAnchorRequestRequestTypeDef",
    {
        "name": str,
        "source": "SourceTypeDef",
    },
    total=False,
)

class UpdateTrustAnchorRequestRequestTypeDef(
    _RequiredUpdateTrustAnchorRequestRequestTypeDef, _OptionalUpdateTrustAnchorRequestRequestTypeDef
):
    pass
