"""
Type annotations for socialmessaging service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_socialmessaging.type_defs import WhatsAppSignupCallbackTypeDef

    data: WhatsAppSignupCallbackTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import RegistrationStatusType

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
    "AssociateWhatsAppBusinessAccountInputTypeDef",
    "AssociateWhatsAppBusinessAccountOutputTypeDef",
    "BlobTypeDef",
    "CreateWhatsAppMessageTemplateFromLibraryInputTypeDef",
    "CreateWhatsAppMessageTemplateFromLibraryOutputTypeDef",
    "CreateWhatsAppMessageTemplateInputTypeDef",
    "CreateWhatsAppMessageTemplateMediaInputTypeDef",
    "CreateWhatsAppMessageTemplateMediaOutputTypeDef",
    "CreateWhatsAppMessageTemplateOutputTypeDef",
    "DeleteWhatsAppMessageMediaInputTypeDef",
    "DeleteWhatsAppMessageMediaOutputTypeDef",
    "DeleteWhatsAppMessageTemplateInputTypeDef",
    "DisassociateWhatsAppBusinessAccountInputTypeDef",
    "GetLinkedWhatsAppBusinessAccountInputTypeDef",
    "GetLinkedWhatsAppBusinessAccountOutputTypeDef",
    "GetLinkedWhatsAppBusinessAccountPhoneNumberInputTypeDef",
    "GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef",
    "GetWhatsAppMessageMediaInputTypeDef",
    "GetWhatsAppMessageMediaOutputTypeDef",
    "GetWhatsAppMessageTemplateInputTypeDef",
    "GetWhatsAppMessageTemplateOutputTypeDef",
    "LibraryTemplateBodyInputsTypeDef",
    "LibraryTemplateButtonInputTypeDef",
    "LibraryTemplateButtonListTypeDef",
    "LinkedWhatsAppBusinessAccountIdMetaDataTypeDef",
    "LinkedWhatsAppBusinessAccountSummaryTypeDef",
    "LinkedWhatsAppBusinessAccountTypeDef",
    "ListLinkedWhatsAppBusinessAccountsInputPaginateTypeDef",
    "ListLinkedWhatsAppBusinessAccountsInputTypeDef",
    "ListLinkedWhatsAppBusinessAccountsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWhatsAppMessageTemplatesInputPaginateTypeDef",
    "ListWhatsAppMessageTemplatesInputTypeDef",
    "ListWhatsAppMessageTemplatesOutputTypeDef",
    "ListWhatsAppTemplateLibraryInputPaginateTypeDef",
    "ListWhatsAppTemplateLibraryInputTypeDef",
    "ListWhatsAppTemplateLibraryOutputTypeDef",
    "MetaLibraryTemplateDefinitionTypeDef",
    "MetaLibraryTemplateTypeDef",
    "PaginatorConfigTypeDef",
    "PostWhatsAppMessageMediaInputTypeDef",
    "PostWhatsAppMessageMediaOutputTypeDef",
    "PutWhatsAppBusinessAccountEventDestinationsInputTypeDef",
    "ResponseMetadataTypeDef",
    "S3FileTypeDef",
    "S3PresignedUrlTypeDef",
    "SendWhatsAppMessageInputTypeDef",
    "SendWhatsAppMessageOutputTypeDef",
    "TagResourceInputTypeDef",
    "TagResourceOutputTypeDef",
    "TagTypeDef",
    "TemplateSummaryTypeDef",
    "UntagResourceInputTypeDef",
    "UntagResourceOutputTypeDef",
    "UpdateWhatsAppMessageTemplateInputTypeDef",
    "WabaPhoneNumberSetupFinalizationTypeDef",
    "WabaSetupFinalizationTypeDef",
    "WhatsAppBusinessAccountEventDestinationTypeDef",
    "WhatsAppPhoneNumberDetailTypeDef",
    "WhatsAppPhoneNumberSummaryTypeDef",
    "WhatsAppSetupFinalizationTypeDef",
    "WhatsAppSignupCallbackResultTypeDef",
    "WhatsAppSignupCallbackTypeDef",
)

class WhatsAppSignupCallbackTypeDef(TypedDict):
    accessToken: str
    callbackUrl: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class S3FileTypeDef(TypedDict):
    bucketName: str
    key: str

class DeleteWhatsAppMessageMediaInputTypeDef(TypedDict):
    mediaId: str
    originationPhoneNumberId: str

DeleteWhatsAppMessageTemplateInputTypeDef = TypedDict(
    "DeleteWhatsAppMessageTemplateInputTypeDef",
    {
        "id": str,
        "templateName": str,
        "metaTemplateId": NotRequired[str],
        "deleteAllLanguages": NotRequired[bool],
    },
)
DisassociateWhatsAppBusinessAccountInputTypeDef = TypedDict(
    "DisassociateWhatsAppBusinessAccountInputTypeDef",
    {
        "id": str,
    },
)
GetLinkedWhatsAppBusinessAccountInputTypeDef = TypedDict(
    "GetLinkedWhatsAppBusinessAccountInputTypeDef",
    {
        "id": str,
    },
)
GetLinkedWhatsAppBusinessAccountPhoneNumberInputTypeDef = TypedDict(
    "GetLinkedWhatsAppBusinessAccountPhoneNumberInputTypeDef",
    {
        "id": str,
    },
)

class WhatsAppPhoneNumberDetailTypeDef(TypedDict):
    arn: str
    phoneNumber: str
    phoneNumberId: str
    metaPhoneNumberId: str
    displayPhoneNumberName: str
    displayPhoneNumber: str
    qualityRating: str
    dataLocalizationRegion: NotRequired[str]

class S3PresignedUrlTypeDef(TypedDict):
    url: str
    headers: Mapping[str, str]

GetWhatsAppMessageTemplateInputTypeDef = TypedDict(
    "GetWhatsAppMessageTemplateInputTypeDef",
    {
        "metaTemplateId": str,
        "id": str,
    },
)

class LibraryTemplateBodyInputsTypeDef(TypedDict):
    addContactNumber: NotRequired[bool]
    addLearnMoreLink: NotRequired[bool]
    addSecurityRecommendation: NotRequired[bool]
    addTrackPackageLink: NotRequired[bool]
    codeExpirationMinutes: NotRequired[int]

LibraryTemplateButtonInputTypeDef = TypedDict(
    "LibraryTemplateButtonInputTypeDef",
    {
        "type": NotRequired[str],
        "phoneNumber": NotRequired[str],
        "url": NotRequired[Mapping[str, str]],
        "otpType": NotRequired[str],
        "zeroTapTermsAccepted": NotRequired[bool],
        "supportedApps": NotRequired[Sequence[Mapping[str, str]]],
    },
)
LibraryTemplateButtonListTypeDef = TypedDict(
    "LibraryTemplateButtonListTypeDef",
    {
        "type": NotRequired[str],
        "text": NotRequired[str],
        "phoneNumber": NotRequired[str],
        "url": NotRequired[str],
        "otpType": NotRequired[str],
        "zeroTapTermsAccepted": NotRequired[bool],
        "supportedApps": NotRequired[List[Dict[str, str]]],
    },
)

class WhatsAppBusinessAccountEventDestinationTypeDef(TypedDict):
    eventDestinationArn: str
    roleArn: NotRequired[str]

class WhatsAppPhoneNumberSummaryTypeDef(TypedDict):
    arn: str
    phoneNumber: str
    phoneNumberId: str
    metaPhoneNumberId: str
    displayPhoneNumberName: str
    displayPhoneNumber: str
    qualityRating: str
    dataLocalizationRegion: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListLinkedWhatsAppBusinessAccountsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class TagTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

ListWhatsAppMessageTemplatesInputTypeDef = TypedDict(
    "ListWhatsAppMessageTemplatesInputTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class TemplateSummaryTypeDef(TypedDict):
    templateName: NotRequired[str]
    metaTemplateId: NotRequired[str]
    templateStatus: NotRequired[str]
    templateQualityScore: NotRequired[str]
    templateLanguage: NotRequired[str]
    templateCategory: NotRequired[str]

ListWhatsAppTemplateLibraryInputTypeDef = TypedDict(
    "ListWhatsAppTemplateLibraryInputTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Mapping[str, str]],
    },
)

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateWhatsAppMessageTemplateFromLibraryOutputTypeDef(TypedDict):
    metaTemplateId: str
    templateStatus: str
    category: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatsAppMessageTemplateMediaOutputTypeDef(TypedDict):
    metaHeaderHandle: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatsAppMessageTemplateOutputTypeDef(TypedDict):
    metaTemplateId: str
    templateStatus: str
    category: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWhatsAppMessageMediaOutputTypeDef(TypedDict):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetWhatsAppMessageMediaOutputTypeDef(TypedDict):
    mimeType: str
    fileSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetWhatsAppMessageTemplateOutputTypeDef(TypedDict):
    template: str
    ResponseMetadata: ResponseMetadataTypeDef

class PostWhatsAppMessageMediaOutputTypeDef(TypedDict):
    mediaId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendWhatsAppMessageOutputTypeDef(TypedDict):
    messageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceOutputTypeDef(TypedDict):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceOutputTypeDef(TypedDict):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

CreateWhatsAppMessageTemplateInputTypeDef = TypedDict(
    "CreateWhatsAppMessageTemplateInputTypeDef",
    {
        "templateDefinition": BlobTypeDef,
        "id": str,
    },
)

class SendWhatsAppMessageInputTypeDef(TypedDict):
    originationPhoneNumberId: str
    message: BlobTypeDef
    metaApiVersion: str

UpdateWhatsAppMessageTemplateInputTypeDef = TypedDict(
    "UpdateWhatsAppMessageTemplateInputTypeDef",
    {
        "id": str,
        "metaTemplateId": str,
        "templateCategory": NotRequired[str],
        "templateComponents": NotRequired[BlobTypeDef],
    },
)
CreateWhatsAppMessageTemplateMediaInputTypeDef = TypedDict(
    "CreateWhatsAppMessageTemplateMediaInputTypeDef",
    {
        "id": str,
        "sourceS3File": NotRequired[S3FileTypeDef],
    },
)

class GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef(TypedDict):
    phoneNumber: WhatsAppPhoneNumberDetailTypeDef
    linkedWhatsAppBusinessAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class LinkedWhatsAppBusinessAccountIdMetaDataTypeDef(TypedDict):
    accountName: NotRequired[str]
    registrationStatus: NotRequired[RegistrationStatusType]
    unregisteredWhatsAppPhoneNumbers: NotRequired[List[WhatsAppPhoneNumberDetailTypeDef]]
    wabaId: NotRequired[str]

class GetWhatsAppMessageMediaInputTypeDef(TypedDict):
    mediaId: str
    originationPhoneNumberId: str
    metadataOnly: NotRequired[bool]
    destinationS3PresignedUrl: NotRequired[S3PresignedUrlTypeDef]
    destinationS3File: NotRequired[S3FileTypeDef]

class PostWhatsAppMessageMediaInputTypeDef(TypedDict):
    originationPhoneNumberId: str
    sourceS3PresignedUrl: NotRequired[S3PresignedUrlTypeDef]
    sourceS3File: NotRequired[S3FileTypeDef]

class MetaLibraryTemplateTypeDef(TypedDict):
    templateName: str
    libraryTemplateName: str
    templateCategory: str
    templateLanguage: str
    libraryTemplateButtonInputs: NotRequired[Sequence[LibraryTemplateButtonInputTypeDef]]
    libraryTemplateBodyInputs: NotRequired[LibraryTemplateBodyInputsTypeDef]

class MetaLibraryTemplateDefinitionTypeDef(TypedDict):
    templateName: NotRequired[str]
    templateLanguage: NotRequired[str]
    templateCategory: NotRequired[str]
    templateTopic: NotRequired[str]
    templateUseCase: NotRequired[str]
    templateIndustry: NotRequired[List[str]]
    templateHeader: NotRequired[str]
    templateBody: NotRequired[str]
    templateButtons: NotRequired[List[LibraryTemplateButtonListTypeDef]]
    templateId: NotRequired[str]

LinkedWhatsAppBusinessAccountSummaryTypeDef = TypedDict(
    "LinkedWhatsAppBusinessAccountSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "wabaId": str,
        "registrationStatus": RegistrationStatusType,
        "linkDate": datetime,
        "wabaName": str,
        "eventDestinations": List[WhatsAppBusinessAccountEventDestinationTypeDef],
    },
)
PutWhatsAppBusinessAccountEventDestinationsInputTypeDef = TypedDict(
    "PutWhatsAppBusinessAccountEventDestinationsInputTypeDef",
    {
        "id": str,
        "eventDestinations": Sequence[WhatsAppBusinessAccountEventDestinationTypeDef],
    },
)
LinkedWhatsAppBusinessAccountTypeDef = TypedDict(
    "LinkedWhatsAppBusinessAccountTypeDef",
    {
        "arn": str,
        "id": str,
        "wabaId": str,
        "registrationStatus": RegistrationStatusType,
        "linkDate": datetime,
        "wabaName": str,
        "eventDestinations": List[WhatsAppBusinessAccountEventDestinationTypeDef],
        "phoneNumbers": List[WhatsAppPhoneNumberSummaryTypeDef],
    },
)

class ListLinkedWhatsAppBusinessAccountsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListWhatsAppMessageTemplatesInputPaginateTypeDef = TypedDict(
    "ListWhatsAppMessageTemplatesInputPaginateTypeDef",
    {
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWhatsAppTemplateLibraryInputPaginateTypeDef = TypedDict(
    "ListWhatsAppTemplateLibraryInputPaginateTypeDef",
    {
        "id": str,
        "filters": NotRequired[Mapping[str, str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListTagsForResourceOutputTypeDef(TypedDict):
    statusCode: int
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

WabaPhoneNumberSetupFinalizationTypeDef = TypedDict(
    "WabaPhoneNumberSetupFinalizationTypeDef",
    {
        "id": str,
        "twoFactorPin": str,
        "dataLocalizationRegion": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
WabaSetupFinalizationTypeDef = TypedDict(
    "WabaSetupFinalizationTypeDef",
    {
        "id": NotRequired[str],
        "eventDestinations": NotRequired[Sequence[WhatsAppBusinessAccountEventDestinationTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)

class ListWhatsAppMessageTemplatesOutputTypeDef(TypedDict):
    templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class WhatsAppSignupCallbackResultTypeDef(TypedDict):
    associateInProgressToken: NotRequired[str]
    linkedAccountsWithIncompleteSetup: NotRequired[
        Dict[str, LinkedWhatsAppBusinessAccountIdMetaDataTypeDef]
    ]

CreateWhatsAppMessageTemplateFromLibraryInputTypeDef = TypedDict(
    "CreateWhatsAppMessageTemplateFromLibraryInputTypeDef",
    {
        "metaLibraryTemplate": MetaLibraryTemplateTypeDef,
        "id": str,
    },
)

class ListWhatsAppTemplateLibraryOutputTypeDef(TypedDict):
    metaLibraryTemplates: List[MetaLibraryTemplateDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListLinkedWhatsAppBusinessAccountsOutputTypeDef(TypedDict):
    linkedAccounts: List[LinkedWhatsAppBusinessAccountSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetLinkedWhatsAppBusinessAccountOutputTypeDef(TypedDict):
    account: LinkedWhatsAppBusinessAccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WhatsAppSetupFinalizationTypeDef(TypedDict):
    associateInProgressToken: str
    phoneNumbers: Sequence[WabaPhoneNumberSetupFinalizationTypeDef]
    phoneNumberParent: NotRequired[str]
    waba: NotRequired[WabaSetupFinalizationTypeDef]

class AssociateWhatsAppBusinessAccountOutputTypeDef(TypedDict):
    signupCallbackResult: WhatsAppSignupCallbackResultTypeDef
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateWhatsAppBusinessAccountInputTypeDef(TypedDict):
    signupCallback: NotRequired[WhatsAppSignupCallbackTypeDef]
    setupFinalization: NotRequired[WhatsAppSetupFinalizationTypeDef]
