"""
Type annotations for rolesanywhere service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rolesanywhere.type_defs import CreateProfileRequestRequestTypeDef

    data: CreateProfileRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import TrustAnchorTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateProfileRequestRequestTypeDef",
    "CreateTrustAnchorRequestRequestTypeDef",
    "CredentialSummaryTypeDef",
    "CrlDetailResponseTypeDef",
    "CrlDetailTypeDef",
    "ImportCrlRequestRequestTypeDef",
    "InstancePropertyTypeDef",
    "ListCrlsResponseTypeDef",
    "ListProfilesResponseTypeDef",
    "ListRequestRequestTypeDef",
    "ListSubjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustAnchorsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProfileDetailResponseTypeDef",
    "ProfileDetailTypeDef",
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
