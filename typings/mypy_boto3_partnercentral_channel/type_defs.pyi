"""
Type annotations for partnercentral-channel service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_partnercentral_channel.type_defs import AcceptChannelHandshakeDetailTypeDef

    data: AcceptChannelHandshakeDetailTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AssociationTypeType,
    CoverageType,
    HandshakeStatusType,
    HandshakeTypeType,
    ParticipantTypeType,
    ProgramManagementAccountStatusType,
    ProgramType,
    ProviderType,
    ResaleAccountModelType,
    SectorType,
    ServicePeriodTypeType,
    SortOrderType,
)

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
    "AcceptChannelHandshakeDetailTypeDef",
    "AcceptChannelHandshakeRequestTypeDef",
    "AcceptChannelHandshakeResponseTypeDef",
    "CancelChannelHandshakeDetailTypeDef",
    "CancelChannelHandshakeRequestTypeDef",
    "CancelChannelHandshakeResponseTypeDef",
    "ChannelHandshakePayloadTypeDef",
    "ChannelHandshakeSummaryTypeDef",
    "CreateChannelHandshakeDetailTypeDef",
    "CreateChannelHandshakeRequestTypeDef",
    "CreateChannelHandshakeResponseTypeDef",
    "CreateProgramManagementAccountDetailTypeDef",
    "CreateProgramManagementAccountRequestTypeDef",
    "CreateProgramManagementAccountResponseTypeDef",
    "CreateRelationshipDetailTypeDef",
    "CreateRelationshipRequestTypeDef",
    "CreateRelationshipResponseTypeDef",
    "DeleteProgramManagementAccountRequestTypeDef",
    "DeleteRelationshipRequestTypeDef",
    "GetRelationshipRequestTypeDef",
    "GetRelationshipResponseTypeDef",
    "HandshakeDetailTypeDef",
    "ListChannelHandshakesRequestPaginateTypeDef",
    "ListChannelHandshakesRequestTypeDef",
    "ListChannelHandshakesResponseTypeDef",
    "ListChannelHandshakesTypeFiltersTypeDef",
    "ListChannelHandshakesTypeSortTypeDef",
    "ListProgramManagementAccountsRequestPaginateTypeDef",
    "ListProgramManagementAccountsRequestTypeDef",
    "ListProgramManagementAccountsResponseTypeDef",
    "ListProgramManagementAccountsSortBaseTypeDef",
    "ListRelationshipsRequestPaginateTypeDef",
    "ListRelationshipsRequestTypeDef",
    "ListRelationshipsResponseTypeDef",
    "ListRelationshipsSortBaseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PartnerLedSupportTypeDef",
    "ProgramManagementAccountHandshakeDetailTypeDef",
    "ProgramManagementAccountSummaryTypeDef",
    "ProgramManagementAccountTypeFiltersTypeDef",
    "ProgramManagementAccountTypeSortTypeDef",
    "RejectChannelHandshakeDetailTypeDef",
    "RejectChannelHandshakeRequestTypeDef",
    "RejectChannelHandshakeResponseTypeDef",
    "RelationshipDetailTypeDef",
    "RelationshipSummaryTypeDef",
    "ResoldBusinessTypeDef",
    "ResoldEnterpriseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeServicePeriodHandshakeDetailTypeDef",
    "RevokeServicePeriodPayloadTypeDef",
    "RevokeServicePeriodTypeFiltersTypeDef",
    "RevokeServicePeriodTypeSortTypeDef",
    "StartServicePeriodHandshakeDetailTypeDef",
    "StartServicePeriodPayloadTypeDef",
    "StartServicePeriodTypeFiltersTypeDef",
    "StartServicePeriodTypeSortTypeDef",
    "SupportPlanTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateProgramManagementAccountDetailTypeDef",
    "UpdateProgramManagementAccountRequestTypeDef",
    "UpdateProgramManagementAccountResponseTypeDef",
    "UpdateRelationshipDetailTypeDef",
    "UpdateRelationshipRequestTypeDef",
    "UpdateRelationshipResponseTypeDef",
)

AcceptChannelHandshakeDetailTypeDef = TypedDict(
    "AcceptChannelHandshakeDetailTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[HandshakeStatusType],
    },
)

class AcceptChannelHandshakeRequestTypeDef(TypedDict):
    catalog: str
    identifier: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

CancelChannelHandshakeDetailTypeDef = TypedDict(
    "CancelChannelHandshakeDetailTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[HandshakeStatusType],
    },
)

class CancelChannelHandshakeRequestTypeDef(TypedDict):
    catalog: str
    identifier: str

class RevokeServicePeriodPayloadTypeDef(TypedDict):
    programManagementAccountIdentifier: str
    note: NotRequired[str]

CreateChannelHandshakeDetailTypeDef = TypedDict(
    "CreateChannelHandshakeDetailTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
    },
)

class TagTypeDef(TypedDict):
    key: str
    value: str

CreateProgramManagementAccountDetailTypeDef = TypedDict(
    "CreateProgramManagementAccountDetailTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
    },
)
CreateRelationshipDetailTypeDef = TypedDict(
    "CreateRelationshipDetailTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
    },
)

class DeleteProgramManagementAccountRequestTypeDef(TypedDict):
    catalog: str
    identifier: str
    clientToken: NotRequired[str]

class DeleteRelationshipRequestTypeDef(TypedDict):
    catalog: str
    identifier: str
    programManagementAccountIdentifier: str
    clientToken: NotRequired[str]

class GetRelationshipRequestTypeDef(TypedDict):
    catalog: str
    programManagementAccountIdentifier: str
    identifier: str

RelationshipDetailTypeDef = TypedDict(
    "RelationshipDetailTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
        "catalog": NotRequired[str],
        "associationType": NotRequired[AssociationTypeType],
        "programManagementAccountId": NotRequired[str],
        "associatedAccountId": NotRequired[str],
        "displayName": NotRequired[str],
        "resaleAccountModel": NotRequired[ResaleAccountModelType],
        "sector": NotRequired[SectorType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "startDate": NotRequired[datetime],
    },
)

class ProgramManagementAccountHandshakeDetailTypeDef(TypedDict):
    program: NotRequired[ProgramType]

class RevokeServicePeriodHandshakeDetailTypeDef(TypedDict):
    note: NotRequired[str]
    servicePeriodType: NotRequired[ServicePeriodTypeType]
    minimumNoticeDays: NotRequired[str]
    startDate: NotRequired[datetime]
    endDate: NotRequired[datetime]

class StartServicePeriodHandshakeDetailTypeDef(TypedDict):
    note: NotRequired[str]
    servicePeriodType: NotRequired[ServicePeriodTypeType]
    minimumNoticeDays: NotRequired[str]
    startDate: NotRequired[datetime]
    endDate: NotRequired[datetime]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ProgramManagementAccountTypeFiltersTypeDef(TypedDict):
    programs: NotRequired[Sequence[ProgramType]]

class RevokeServicePeriodTypeFiltersTypeDef(TypedDict):
    servicePeriodTypes: NotRequired[Sequence[ServicePeriodTypeType]]

class StartServicePeriodTypeFiltersTypeDef(TypedDict):
    servicePeriodTypes: NotRequired[Sequence[ServicePeriodTypeType]]

class ProgramManagementAccountTypeSortTypeDef(TypedDict):
    sortOrder: SortOrderType
    sortBy: Literal["UpdatedAt"]

class RevokeServicePeriodTypeSortTypeDef(TypedDict):
    sortOrder: SortOrderType
    sortBy: Literal["UpdatedAt"]

class StartServicePeriodTypeSortTypeDef(TypedDict):
    sortOrder: SortOrderType
    sortBy: Literal["UpdatedAt"]

class ListProgramManagementAccountsSortBaseTypeDef(TypedDict):
    sortOrder: SortOrderType
    sortBy: Literal["UpdatedAt"]

ProgramManagementAccountSummaryTypeDef = TypedDict(
    "ProgramManagementAccountSummaryTypeDef",
    {
        "id": NotRequired[str],
        "revision": NotRequired[str],
        "catalog": NotRequired[str],
        "program": NotRequired[ProgramType],
        "displayName": NotRequired[str],
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "startDate": NotRequired[datetime],
        "status": NotRequired[ProgramManagementAccountStatusType],
    },
)

class ListRelationshipsSortBaseTypeDef(TypedDict):
    sortOrder: SortOrderType
    sortBy: Literal["UpdatedAt"]

RelationshipSummaryTypeDef = TypedDict(
    "RelationshipSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
        "catalog": NotRequired[str],
        "associationType": NotRequired[AssociationTypeType],
        "programManagementAccountId": NotRequired[str],
        "associatedAccountId": NotRequired[str],
        "displayName": NotRequired[str],
        "sector": NotRequired[SectorType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "startDate": NotRequired[datetime],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PartnerLedSupportTypeDef(TypedDict):
    coverage: CoverageType
    tamLocation: str
    provider: NotRequired[ProviderType]

RejectChannelHandshakeDetailTypeDef = TypedDict(
    "RejectChannelHandshakeDetailTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[HandshakeStatusType],
    },
)

class RejectChannelHandshakeRequestTypeDef(TypedDict):
    catalog: str
    identifier: str

class ResoldBusinessTypeDef(TypedDict):
    coverage: CoverageType

class ResoldEnterpriseTypeDef(TypedDict):
    coverage: CoverageType
    tamLocation: str
    chargeAccountId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UpdateProgramManagementAccountDetailTypeDef = TypedDict(
    "UpdateProgramManagementAccountDetailTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "revision": NotRequired[str],
        "displayName": NotRequired[str],
    },
)

class UpdateProgramManagementAccountRequestTypeDef(TypedDict):
    catalog: str
    identifier: str
    revision: NotRequired[str]
    displayName: NotRequired[str]

UpdateRelationshipDetailTypeDef = TypedDict(
    "UpdateRelationshipDetailTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
        "displayName": NotRequired[str],
    },
)

class AcceptChannelHandshakeResponseTypeDef(TypedDict):
    channelHandshakeDetail: AcceptChannelHandshakeDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelChannelHandshakeResponseTypeDef(TypedDict):
    channelHandshakeDetail: CancelChannelHandshakeDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelHandshakeResponseTypeDef(TypedDict):
    channelHandshakeDetail: CreateChannelHandshakeDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProgramManagementAccountRequestTypeDef(TypedDict):
    catalog: str
    program: ProgramType
    displayName: str
    accountId: str
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateProgramManagementAccountResponseTypeDef(TypedDict):
    programManagementAccountDetail: CreateProgramManagementAccountDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelationshipResponseTypeDef(TypedDict):
    relationshipDetail: CreateRelationshipDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationshipResponseTypeDef(TypedDict):
    relationshipDetail: RelationshipDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HandshakeDetailTypeDef(TypedDict):
    startServicePeriodHandshakeDetail: NotRequired[StartServicePeriodHandshakeDetailTypeDef]
    revokeServicePeriodHandshakeDetail: NotRequired[RevokeServicePeriodHandshakeDetailTypeDef]
    programManagementAccountHandshakeDetail: NotRequired[
        ProgramManagementAccountHandshakeDetailTypeDef
    ]

class ListChannelHandshakesTypeFiltersTypeDef(TypedDict):
    startServicePeriodTypeFilters: NotRequired[StartServicePeriodTypeFiltersTypeDef]
    revokeServicePeriodTypeFilters: NotRequired[RevokeServicePeriodTypeFiltersTypeDef]
    programManagementAccountTypeFilters: NotRequired[ProgramManagementAccountTypeFiltersTypeDef]

class ListChannelHandshakesTypeSortTypeDef(TypedDict):
    startServicePeriodTypeSort: NotRequired[StartServicePeriodTypeSortTypeDef]
    revokeServicePeriodTypeSort: NotRequired[RevokeServicePeriodTypeSortTypeDef]
    programManagementAccountTypeSort: NotRequired[ProgramManagementAccountTypeSortTypeDef]

class ListProgramManagementAccountsRequestPaginateTypeDef(TypedDict):
    catalog: str
    displayNames: NotRequired[Sequence[str]]
    programs: NotRequired[Sequence[ProgramType]]
    accountIds: NotRequired[Sequence[str]]
    statuses: NotRequired[Sequence[ProgramManagementAccountStatusType]]
    sort: NotRequired[ListProgramManagementAccountsSortBaseTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProgramManagementAccountsRequestTypeDef(TypedDict):
    catalog: str
    maxResults: NotRequired[int]
    displayNames: NotRequired[Sequence[str]]
    programs: NotRequired[Sequence[ProgramType]]
    accountIds: NotRequired[Sequence[str]]
    statuses: NotRequired[Sequence[ProgramManagementAccountStatusType]]
    sort: NotRequired[ListProgramManagementAccountsSortBaseTypeDef]
    nextToken: NotRequired[str]

class ListProgramManagementAccountsResponseTypeDef(TypedDict):
    items: List[ProgramManagementAccountSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRelationshipsRequestPaginateTypeDef(TypedDict):
    catalog: str
    associatedAccountIds: NotRequired[Sequence[str]]
    associationTypes: NotRequired[Sequence[AssociationTypeType]]
    displayNames: NotRequired[Sequence[str]]
    programManagementAccountIdentifiers: NotRequired[Sequence[str]]
    sort: NotRequired[ListRelationshipsSortBaseTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRelationshipsRequestTypeDef(TypedDict):
    catalog: str
    maxResults: NotRequired[int]
    associatedAccountIds: NotRequired[Sequence[str]]
    associationTypes: NotRequired[Sequence[AssociationTypeType]]
    displayNames: NotRequired[Sequence[str]]
    programManagementAccountIdentifiers: NotRequired[Sequence[str]]
    sort: NotRequired[ListRelationshipsSortBaseTypeDef]
    nextToken: NotRequired[str]

class ListRelationshipsResponseTypeDef(TypedDict):
    items: List[RelationshipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RejectChannelHandshakeResponseTypeDef(TypedDict):
    channelHandshakeDetail: RejectChannelHandshakeDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SupportPlanTypeDef(TypedDict):
    resoldBusiness: NotRequired[ResoldBusinessTypeDef]
    resoldEnterprise: NotRequired[ResoldEnterpriseTypeDef]
    partnerLedSupport: NotRequired[PartnerLedSupportTypeDef]

class StartServicePeriodPayloadTypeDef(TypedDict):
    programManagementAccountIdentifier: str
    servicePeriodType: ServicePeriodTypeType
    note: NotRequired[str]
    minimumNoticeDays: NotRequired[str]
    endDate: NotRequired[TimestampTypeDef]

class UpdateProgramManagementAccountResponseTypeDef(TypedDict):
    programManagementAccountDetail: UpdateProgramManagementAccountDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRelationshipResponseTypeDef(TypedDict):
    relationshipDetail: UpdateRelationshipDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ChannelHandshakeSummaryTypeDef = TypedDict(
    "ChannelHandshakeSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "catalog": NotRequired[str],
        "handshakeType": NotRequired[HandshakeTypeType],
        "ownerAccountId": NotRequired[str],
        "senderAccountId": NotRequired[str],
        "senderDisplayName": NotRequired[str],
        "receiverAccountId": NotRequired[str],
        "associatedResourceId": NotRequired[str],
        "detail": NotRequired[HandshakeDetailTypeDef],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "status": NotRequired[HandshakeStatusType],
    },
)

class ListChannelHandshakesRequestPaginateTypeDef(TypedDict):
    handshakeType: HandshakeTypeType
    catalog: str
    participantType: ParticipantTypeType
    statuses: NotRequired[Sequence[HandshakeStatusType]]
    associatedResourceIdentifiers: NotRequired[Sequence[str]]
    handshakeTypeFilters: NotRequired[ListChannelHandshakesTypeFiltersTypeDef]
    handshakeTypeSort: NotRequired[ListChannelHandshakesTypeSortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListChannelHandshakesRequestTypeDef(TypedDict):
    handshakeType: HandshakeTypeType
    catalog: str
    participantType: ParticipantTypeType
    maxResults: NotRequired[int]
    statuses: NotRequired[Sequence[HandshakeStatusType]]
    associatedResourceIdentifiers: NotRequired[Sequence[str]]
    handshakeTypeFilters: NotRequired[ListChannelHandshakesTypeFiltersTypeDef]
    handshakeTypeSort: NotRequired[ListChannelHandshakesTypeSortTypeDef]
    nextToken: NotRequired[str]

class CreateRelationshipRequestTypeDef(TypedDict):
    catalog: str
    associationType: AssociationTypeType
    programManagementAccountIdentifier: str
    associatedAccountId: str
    displayName: str
    sector: SectorType
    resaleAccountModel: NotRequired[ResaleAccountModelType]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    requestedSupportPlan: NotRequired[SupportPlanTypeDef]

class UpdateRelationshipRequestTypeDef(TypedDict):
    catalog: str
    identifier: str
    programManagementAccountIdentifier: str
    revision: NotRequired[str]
    displayName: NotRequired[str]
    requestedSupportPlan: NotRequired[SupportPlanTypeDef]

class ChannelHandshakePayloadTypeDef(TypedDict):
    startServicePeriodPayload: NotRequired[StartServicePeriodPayloadTypeDef]
    revokeServicePeriodPayload: NotRequired[RevokeServicePeriodPayloadTypeDef]

class ListChannelHandshakesResponseTypeDef(TypedDict):
    items: List[ChannelHandshakeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateChannelHandshakeRequestTypeDef(TypedDict):
    handshakeType: HandshakeTypeType
    catalog: str
    associatedResourceIdentifier: str
    payload: NotRequired[ChannelHandshakePayloadTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
