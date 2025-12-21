"""
Type annotations for partnercentral-account service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_partnercentral_account.type_defs import AcceptConnectionInvitationRequestTypeDef

    data: AcceptConnectionInvitationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AccessTypeType,
    ConnectionTypeStatusType,
    ConnectionTypeType,
    IndustrySegmentType,
    InvitationStatusType,
    ParticipantTypeType,
    PrimarySolutionTypeType,
    ProfileTaskStatusType,
    ProfileValidationErrorReasonType,
    ProfileVisibilityType,
    VerificationStatusType,
    VerificationTypeType,
)

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
    "AcceptConnectionInvitationRequestTypeDef",
    "AcceptConnectionInvitationResponseTypeDef",
    "AccountSummaryTypeDef",
    "AllianceLeadContactTypeDef",
    "AssociateAwsTrainingCertificationEmailDomainRequestTypeDef",
    "BusinessVerificationDetailsTypeDef",
    "BusinessVerificationResponseTypeDef",
    "CancelConnectionInvitationRequestTypeDef",
    "CancelConnectionInvitationResponseTypeDef",
    "CancelConnectionRequestTypeDef",
    "CancelConnectionResponseTypeDef",
    "CancelProfileUpdateTaskRequestTypeDef",
    "CancelProfileUpdateTaskResponseTypeDef",
    "ConnectionInvitationSummaryTypeDef",
    "ConnectionSummaryTypeDef",
    "ConnectionTypeDef",
    "ConnectionTypeDetailTypeDef",
    "ConnectionTypeSummaryTypeDef",
    "CreateConnectionInvitationRequestTypeDef",
    "CreateConnectionInvitationResponseTypeDef",
    "CreatePartnerRequestTypeDef",
    "CreatePartnerResponseTypeDef",
    "DisassociateAwsTrainingCertificationEmailDomainRequestTypeDef",
    "ErrorDetailTypeDef",
    "GetAllianceLeadContactRequestTypeDef",
    "GetAllianceLeadContactResponseTypeDef",
    "GetConnectionInvitationRequestTypeDef",
    "GetConnectionInvitationResponseTypeDef",
    "GetConnectionPreferencesRequestTypeDef",
    "GetConnectionPreferencesResponseTypeDef",
    "GetConnectionRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetPartnerRequestTypeDef",
    "GetPartnerResponseTypeDef",
    "GetProfileUpdateTaskRequestTypeDef",
    "GetProfileUpdateTaskResponseTypeDef",
    "GetProfileVisibilityRequestTypeDef",
    "GetProfileVisibilityResponseTypeDef",
    "GetVerificationRequestTypeDef",
    "GetVerificationResponseTypeDef",
    "ListConnectionInvitationsRequestPaginateTypeDef",
    "ListConnectionInvitationsRequestTypeDef",
    "ListConnectionInvitationsResponseTypeDef",
    "ListConnectionsRequestPaginateTypeDef",
    "ListConnectionsRequestTypeDef",
    "ListConnectionsResponseTypeDef",
    "ListPartnersRequestPaginateTypeDef",
    "ListPartnersRequestTypeDef",
    "ListPartnersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocalizedContentTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantTypeDef",
    "PartnerDomainTypeDef",
    "PartnerProfileSummaryTypeDef",
    "PartnerProfileTypeDef",
    "PartnerSummaryTypeDef",
    "PutAllianceLeadContactRequestTypeDef",
    "PutAllianceLeadContactResponseTypeDef",
    "PutProfileVisibilityRequestTypeDef",
    "PutProfileVisibilityResponseTypeDef",
    "RegistrantVerificationResponseTypeDef",
    "RejectConnectionInvitationRequestTypeDef",
    "RejectConnectionInvitationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SellerProfileSummaryTypeDef",
    "SendEmailVerificationCodeRequestTypeDef",
    "StartProfileUpdateTaskRequestTypeDef",
    "StartProfileUpdateTaskResponseTypeDef",
    "StartVerificationRequestTypeDef",
    "StartVerificationResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TaskDetailsOutputTypeDef",
    "TaskDetailsTypeDef",
    "TaskDetailsUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectionPreferencesRequestTypeDef",
    "UpdateConnectionPreferencesResponseTypeDef",
    "VerificationDetailsTypeDef",
    "VerificationResponseDetailsTypeDef",
)

class AcceptConnectionInvitationRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    ClientToken: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AccountSummaryTypeDef(TypedDict):
    Name: str

class AllianceLeadContactTypeDef(TypedDict):
    FirstName: str
    LastName: str
    Email: str
    BusinessTitle: str

class AssociateAwsTrainingCertificationEmailDomainRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    Email: str
    EmailVerificationCode: str
    ClientToken: NotRequired[str]

class BusinessVerificationDetailsTypeDef(TypedDict):
    LegalName: str
    RegistrationId: str
    CountryCode: str
    JurisdictionOfIncorporation: NotRequired[str]

class CancelConnectionInvitationRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    ClientToken: str

class CancelConnectionRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    ConnectionType: ConnectionTypeType
    Reason: str
    ClientToken: str

class CancelProfileUpdateTaskRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    TaskId: str
    ClientToken: NotRequired[str]

class ErrorDetailTypeDef(TypedDict):
    Locale: str
    Message: str
    Reason: ProfileValidationErrorReasonType

class ConnectionInvitationSummaryTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    ConnectionType: ConnectionTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    OtherParticipantIdentifier: str
    ParticipantType: ParticipantTypeType
    Status: InvitationStatusType
    ConnectionId: NotRequired[str]
    ExpiresAt: NotRequired[datetime]

class CreateConnectionInvitationRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    ConnectionType: ConnectionTypeType
    Email: str
    Message: str
    Name: str
    ReceiverIdentifier: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class PartnerDomainTypeDef(TypedDict):
    DomainName: str
    RegisteredAt: datetime

class DisassociateAwsTrainingCertificationEmailDomainRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    DomainName: str
    ClientToken: NotRequired[str]

class GetAllianceLeadContactRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetConnectionInvitationRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetConnectionPreferencesRequestTypeDef(TypedDict):
    Catalog: str

class GetConnectionRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetPartnerRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetProfileUpdateTaskRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetProfileVisibilityRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetVerificationRequestTypeDef(TypedDict):
    VerificationType: VerificationTypeType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListConnectionInvitationsRequestTypeDef(TypedDict):
    Catalog: str
    NextToken: NotRequired[str]
    ConnectionType: NotRequired[ConnectionTypeType]
    MaxResults: NotRequired[int]
    OtherParticipantIdentifiers: NotRequired[Sequence[str]]
    ParticipantType: NotRequired[ParticipantTypeType]
    Status: NotRequired[InvitationStatusType]

class ListConnectionsRequestTypeDef(TypedDict):
    Catalog: str
    NextToken: NotRequired[str]
    ConnectionType: NotRequired[str]
    MaxResults: NotRequired[int]
    OtherParticipantIdentifiers: NotRequired[Sequence[str]]

class ListPartnersRequestTypeDef(TypedDict):
    Catalog: str
    NextToken: NotRequired[str]

class PartnerSummaryTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    LegalName: str
    CreatedAt: datetime

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class LocalizedContentTypeDef(TypedDict):
    DisplayName: str
    Description: str
    WebsiteUrl: str
    LogoUrl: str
    Locale: str

class PartnerProfileSummaryTypeDef(TypedDict):
    Id: str
    Name: str

class SellerProfileSummaryTypeDef(TypedDict):
    Id: str
    Name: str

class PutProfileVisibilityRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    Visibility: ProfileVisibilityType

class RegistrantVerificationResponseTypeDef(TypedDict):
    CompletionUrl: str
    CompletionUrlExpiresAt: datetime

class RejectConnectionInvitationRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    ClientToken: str
    Reason: NotRequired[str]

class SendEmailVerificationCodeRequestTypeDef(TypedDict):
    Catalog: str
    Email: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConnectionPreferencesRequestTypeDef(TypedDict):
    Catalog: str
    Revision: int
    AccessType: AccessTypeType
    ExcludedParticipantIdentifiers: NotRequired[Sequence[str]]

class CancelConnectionInvitationResponseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ExpiresAt: datetime
    OtherParticipantIdentifier: str
    ParticipantType: ParticipantTypeType
    Status: InvitationStatusType
    InvitationMessage: str
    InviterEmail: str
    InviterName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionInvitationResponseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ExpiresAt: datetime
    OtherParticipantIdentifier: str
    ParticipantType: ParticipantTypeType
    Status: InvitationStatusType
    InvitationMessage: str
    InviterEmail: str
    InviterName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionInvitationResponseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ExpiresAt: datetime
    OtherParticipantIdentifier: str
    ParticipantType: ParticipantTypeType
    Status: InvitationStatusType
    InvitationMessage: str
    InviterEmail: str
    InviterName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionPreferencesResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    AccessType: AccessTypeType
    ExcludedParticipantIds: List[str]
    UpdatedAt: datetime
    Revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileVisibilityResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    Visibility: ProfileVisibilityType
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutProfileVisibilityResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    Visibility: ProfileVisibilityType
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectConnectionInvitationResponseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ExpiresAt: datetime
    OtherParticipantIdentifier: str
    ParticipantType: ParticipantTypeType
    Status: InvitationStatusType
    InvitationMessage: str
    InviterEmail: str
    InviterName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectionPreferencesResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    AccessType: AccessTypeType
    ExcludedParticipantIds: List[str]
    UpdatedAt: datetime
    Revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetAllianceLeadContactResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    AllianceLeadContact: AllianceLeadContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAllianceLeadContactRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    AllianceLeadContact: AllianceLeadContactTypeDef
    EmailVerificationCode: NotRequired[str]

class PutAllianceLeadContactResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    AllianceLeadContact: AllianceLeadContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BusinessVerificationResponseTypeDef(TypedDict):
    BusinessVerificationDetails: BusinessVerificationDetailsTypeDef

class VerificationDetailsTypeDef(TypedDict):
    BusinessVerificationDetails: NotRequired[BusinessVerificationDetailsTypeDef]
    RegistrantVerificationDetails: NotRequired[Mapping[str, Any]]

class ListConnectionInvitationsResponseTypeDef(TypedDict):
    ConnectionInvitationSummaries: List[ConnectionInvitationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreatePartnerRequestTypeDef(TypedDict):
    Catalog: str
    LegalName: str
    PrimarySolutionType: PrimarySolutionTypeType
    AllianceLeadContact: AllianceLeadContactTypeDef
    EmailVerificationCode: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ListConnectionInvitationsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    ConnectionType: NotRequired[ConnectionTypeType]
    OtherParticipantIdentifiers: NotRequired[Sequence[str]]
    ParticipantType: NotRequired[ParticipantTypeType]
    Status: NotRequired[InvitationStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectionsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    ConnectionType: NotRequired[str]
    OtherParticipantIdentifiers: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPartnersRequestPaginateTypeDef(TypedDict):
    Catalog: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPartnersResponseTypeDef(TypedDict):
    PartnerSummaryList: List[PartnerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PartnerProfileTypeDef(TypedDict):
    DisplayName: str
    Description: str
    WebsiteUrl: str
    LogoUrl: str
    PrimarySolutionType: PrimarySolutionTypeType
    IndustrySegments: List[IndustrySegmentType]
    TranslationSourceLocale: str
    LocalizedContents: NotRequired[List[LocalizedContentTypeDef]]
    ProfileId: NotRequired[str]

class TaskDetailsOutputTypeDef(TypedDict):
    DisplayName: str
    Description: str
    WebsiteUrl: str
    LogoUrl: str
    PrimarySolutionType: PrimarySolutionTypeType
    IndustrySegments: List[IndustrySegmentType]
    TranslationSourceLocale: str
    LocalizedContents: NotRequired[List[LocalizedContentTypeDef]]

class TaskDetailsTypeDef(TypedDict):
    DisplayName: str
    Description: str
    WebsiteUrl: str
    LogoUrl: str
    PrimarySolutionType: PrimarySolutionTypeType
    IndustrySegments: Sequence[IndustrySegmentType]
    TranslationSourceLocale: str
    LocalizedContents: NotRequired[Sequence[LocalizedContentTypeDef]]

class ParticipantTypeDef(TypedDict):
    PartnerProfile: NotRequired[PartnerProfileSummaryTypeDef]
    SellerProfile: NotRequired[SellerProfileSummaryTypeDef]
    Account: NotRequired[AccountSummaryTypeDef]

class VerificationResponseDetailsTypeDef(TypedDict):
    BusinessVerificationResponse: NotRequired[BusinessVerificationResponseTypeDef]
    RegistrantVerificationResponse: NotRequired[RegistrantVerificationResponseTypeDef]

class StartVerificationRequestTypeDef(TypedDict):
    ClientToken: NotRequired[str]
    VerificationDetails: NotRequired[VerificationDetailsTypeDef]

class CreatePartnerResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    LegalName: str
    CreatedAt: datetime
    Profile: PartnerProfileTypeDef
    AwsTrainingCertificationEmailDomains: List[PartnerDomainTypeDef]
    AllianceLeadContact: AllianceLeadContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartnerResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    LegalName: str
    CreatedAt: datetime
    Profile: PartnerProfileTypeDef
    AwsTrainingCertificationEmailDomains: List[PartnerDomainTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelProfileUpdateTaskResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    TaskId: str
    TaskDetails: TaskDetailsOutputTypeDef
    StartedAt: datetime
    Status: ProfileTaskStatusType
    EndedAt: datetime
    ErrorDetailList: List[ErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileUpdateTaskResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    TaskId: str
    TaskDetails: TaskDetailsOutputTypeDef
    StartedAt: datetime
    Status: ProfileTaskStatusType
    EndedAt: datetime
    ErrorDetailList: List[ErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartProfileUpdateTaskResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    Id: str
    TaskId: str
    TaskDetails: TaskDetailsOutputTypeDef
    StartedAt: datetime
    Status: ProfileTaskStatusType
    EndedAt: datetime
    ErrorDetailList: List[ErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

TaskDetailsUnionTypeDef = Union[TaskDetailsTypeDef, TaskDetailsOutputTypeDef]

class ConnectionTypeDetailTypeDef(TypedDict):
    CreatedAt: datetime
    InviterEmail: str
    InviterName: str
    Status: ConnectionTypeStatusType
    OtherParticipant: ParticipantTypeDef
    CanceledAt: NotRequired[datetime]
    CanceledBy: NotRequired[str]

class ConnectionTypeSummaryTypeDef(TypedDict):
    Status: ConnectionTypeStatusType
    OtherParticipant: ParticipantTypeDef

class GetVerificationResponseTypeDef(TypedDict):
    VerificationType: VerificationTypeType
    VerificationStatus: VerificationStatusType
    VerificationStatusReason: str
    VerificationResponseDetails: VerificationResponseDetailsTypeDef
    StartedAt: datetime
    CompletedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartVerificationResponseTypeDef(TypedDict):
    VerificationType: VerificationTypeType
    VerificationStatus: VerificationStatusType
    VerificationStatusReason: str
    VerificationResponseDetails: VerificationResponseDetailsTypeDef
    StartedAt: datetime
    CompletedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartProfileUpdateTaskRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    TaskDetails: TaskDetailsUnionTypeDef
    ClientToken: NotRequired[str]

class CancelConnectionResponseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    OtherParticipantAccountId: str
    UpdatedAt: datetime
    ConnectionTypes: Dict[ConnectionTypeType, ConnectionTypeDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    OtherParticipantAccountId: str
    UpdatedAt: datetime
    ConnectionTypes: Dict[ConnectionTypeType, ConnectionTypeDetailTypeDef]

class GetConnectionResponseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    OtherParticipantAccountId: str
    UpdatedAt: datetime
    ConnectionTypes: Dict[ConnectionTypeType, ConnectionTypeDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionSummaryTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    OtherParticipantAccountId: str
    UpdatedAt: datetime
    ConnectionTypes: Dict[ConnectionTypeType, ConnectionTypeSummaryTypeDef]

class AcceptConnectionInvitationResponseTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectionsResponseTypeDef(TypedDict):
    ConnectionSummaries: List[ConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
