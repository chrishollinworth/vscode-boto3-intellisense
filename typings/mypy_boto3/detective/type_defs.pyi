"""
Type annotations for detective service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_detective/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_detective.type_defs import AcceptInvitationRequestTypeDef

    data: AcceptInvitationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DatasourcePackageIngestStateType,
    DatasourcePackageType,
    EntityTypeType,
    FieldType,
    IndicatorTypeType,
    InvitationTypeType,
    MemberDisabledReasonType,
    MemberStatusType,
    SeverityType,
    SortOrderType,
    StateType,
    StatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptInvitationRequestTypeDef",
    "AccountTypeDef",
    "AdministratorTypeDef",
    "BatchGetGraphMemberDatasourcesRequestTypeDef",
    "BatchGetGraphMemberDatasourcesResponseTypeDef",
    "BatchGetMembershipDatasourcesRequestTypeDef",
    "BatchGetMembershipDatasourcesResponseTypeDef",
    "CreateGraphRequestTypeDef",
    "CreateGraphResponseTypeDef",
    "CreateMembersRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "DatasourcePackageIngestDetailTypeDef",
    "DatasourcePackageUsageInfoTypeDef",
    "DateFilterTypeDef",
    "DeleteGraphRequestTypeDef",
    "DeleteMembersRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeOrganizationConfigurationRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DisassociateMembershipRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableOrganizationAdminAccountRequestTypeDef",
    "FilterCriteriaTypeDef",
    "FlaggedIpAddressDetailTypeDef",
    "GetInvestigationRequestTypeDef",
    "GetInvestigationResponseTypeDef",
    "GetMembersRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GraphTypeDef",
    "ImpossibleTravelDetailTypeDef",
    "IndicatorDetailTypeDef",
    "IndicatorTypeDef",
    "InvestigationDetailTypeDef",
    "ListDatasourcePackagesRequestTypeDef",
    "ListDatasourcePackagesResponseTypeDef",
    "ListGraphsRequestTypeDef",
    "ListGraphsResponseTypeDef",
    "ListIndicatorsRequestTypeDef",
    "ListIndicatorsResponseTypeDef",
    "ListInvestigationsRequestTypeDef",
    "ListInvestigationsResponseTypeDef",
    "ListInvitationsRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberDetailTypeDef",
    "MembershipDatasourcesTypeDef",
    "NewAsoDetailTypeDef",
    "NewGeolocationDetailTypeDef",
    "NewUserAgentDetailTypeDef",
    "RejectInvitationRequestTypeDef",
    "RelatedFindingDetailTypeDef",
    "RelatedFindingGroupDetailTypeDef",
    "ResponseMetadataTypeDef",
    "SortCriteriaTypeDef",
    "StartInvestigationRequestTypeDef",
    "StartInvestigationResponseTypeDef",
    "StartMonitoringMemberRequestTypeDef",
    "StringFilterTypeDef",
    "TTPsObservedDetailTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampForCollectionTypeDef",
    "TimestampTypeDef",
    "UnprocessedAccountTypeDef",
    "UnprocessedGraphTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatasourcePackagesRequestTypeDef",
    "UpdateInvestigationStateRequestTypeDef",
    "UpdateOrganizationConfigurationRequestTypeDef",
)

class AcceptInvitationRequestTypeDef(TypedDict):
    GraphArn: str

class AccountTypeDef(TypedDict):
    AccountId: str
    EmailAddress: str

class AdministratorTypeDef(TypedDict):
    AccountId: NotRequired[str]
    GraphArn: NotRequired[str]
    DelegationTime: NotRequired[datetime]

class BatchGetGraphMemberDatasourcesRequestTypeDef(TypedDict):
    GraphArn: str
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class UnprocessedAccountTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Reason: NotRequired[str]

class BatchGetMembershipDatasourcesRequestTypeDef(TypedDict):
    GraphArns: Sequence[str]

class UnprocessedGraphTypeDef(TypedDict):
    GraphArn: NotRequired[str]
    Reason: NotRequired[str]

class CreateGraphRequestTypeDef(TypedDict):
    Tags: NotRequired[Mapping[str, str]]

class TimestampForCollectionTypeDef(TypedDict):
    Timestamp: NotRequired[datetime]

class DatasourcePackageUsageInfoTypeDef(TypedDict):
    VolumeUsageInBytes: NotRequired[int]
    VolumeUsageUpdateTime: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class DeleteGraphRequestTypeDef(TypedDict):
    GraphArn: str

class DeleteMembersRequestTypeDef(TypedDict):
    GraphArn: str
    AccountIds: Sequence[str]

class DescribeOrganizationConfigurationRequestTypeDef(TypedDict):
    GraphArn: str

class DisassociateMembershipRequestTypeDef(TypedDict):
    GraphArn: str

class EnableOrganizationAdminAccountRequestTypeDef(TypedDict):
    AccountId: str

class StringFilterTypeDef(TypedDict):
    Value: str

class FlaggedIpAddressDetailTypeDef(TypedDict):
    IpAddress: NotRequired[str]
    Reason: NotRequired[Literal["AWS_THREAT_INTELLIGENCE"]]

class GetInvestigationRequestTypeDef(TypedDict):
    GraphArn: str
    InvestigationId: str

class GetMembersRequestTypeDef(TypedDict):
    GraphArn: str
    AccountIds: Sequence[str]

class GraphTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreatedTime: NotRequired[datetime]

class ImpossibleTravelDetailTypeDef(TypedDict):
    StartingIpAddress: NotRequired[str]
    EndingIpAddress: NotRequired[str]
    StartingLocation: NotRequired[str]
    EndingLocation: NotRequired[str]
    HourlyTimeDelta: NotRequired[int]

class NewAsoDetailTypeDef(TypedDict):
    Aso: NotRequired[str]
    IsNewForEntireAccount: NotRequired[bool]

class NewGeolocationDetailTypeDef(TypedDict):
    Location: NotRequired[str]
    IpAddress: NotRequired[str]
    IsNewForEntireAccount: NotRequired[bool]

class NewUserAgentDetailTypeDef(TypedDict):
    UserAgent: NotRequired[str]
    IsNewForEntireAccount: NotRequired[bool]

RelatedFindingDetailTypeDef = TypedDict(
    "RelatedFindingDetailTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)

class RelatedFindingGroupDetailTypeDef(TypedDict):
    Id: NotRequired[str]

class TTPsObservedDetailTypeDef(TypedDict):
    Tactic: NotRequired[str]
    Technique: NotRequired[str]
    Procedure: NotRequired[str]
    IpAddress: NotRequired[str]
    APIName: NotRequired[str]
    APISuccessCount: NotRequired[int]
    APIFailureCount: NotRequired[int]

class InvestigationDetailTypeDef(TypedDict):
    InvestigationId: NotRequired[str]
    Severity: NotRequired[SeverityType]
    Status: NotRequired[StatusType]
    State: NotRequired[StateType]
    CreatedTime: NotRequired[datetime]
    EntityArn: NotRequired[str]
    EntityType: NotRequired[EntityTypeType]

class ListDatasourcePackagesRequestTypeDef(TypedDict):
    GraphArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListGraphsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListIndicatorsRequestTypeDef(TypedDict):
    GraphArn: str
    InvestigationId: str
    IndicatorType: NotRequired[IndicatorTypeType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SortCriteriaTypeDef(TypedDict):
    Field: NotRequired[FieldType]
    SortOrder: NotRequired[SortOrderType]

class ListInvitationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMembersRequestTypeDef(TypedDict):
    GraphArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListOrganizationAdminAccountsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class RejectInvitationRequestTypeDef(TypedDict):
    GraphArn: str

class StartMonitoringMemberRequestTypeDef(TypedDict):
    GraphArn: str
    AccountId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDatasourcePackagesRequestTypeDef(TypedDict):
    GraphArn: str
    DatasourcePackages: Sequence[DatasourcePackageType]

class UpdateInvestigationStateRequestTypeDef(TypedDict):
    GraphArn: str
    InvestigationId: str
    State: StateType

class UpdateOrganizationConfigurationRequestTypeDef(TypedDict):
    GraphArn: str
    AutoEnable: NotRequired[bool]

class CreateMembersRequestTypeDef(TypedDict):
    GraphArn: str
    Accounts: Sequence[AccountTypeDef]
    Message: NotRequired[str]
    DisableEmailNotification: NotRequired[bool]

class CreateGraphResponseTypeDef(TypedDict):
    GraphArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(TypedDict):
    AutoEnable: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvestigationResponseTypeDef(TypedDict):
    GraphArn: str
    InvestigationId: str
    EntityArn: str
    EntityType: EntityTypeType
    CreatedTime: datetime
    ScopeStartTime: datetime
    ScopeEndTime: datetime
    Status: StatusType
    Severity: SeverityType
    State: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationAdminAccountsResponseTypeDef(TypedDict):
    Administrators: List[AdministratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartInvestigationResponseTypeDef(TypedDict):
    InvestigationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(TypedDict):
    AccountIds: List[str]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DatasourcePackageIngestDetailTypeDef(TypedDict):
    DatasourcePackageIngestState: NotRequired[DatasourcePackageIngestStateType]
    LastIngestStateChange: NotRequired[
        Dict[DatasourcePackageIngestStateType, TimestampForCollectionTypeDef]
    ]

class MembershipDatasourcesTypeDef(TypedDict):
    AccountId: NotRequired[str]
    GraphArn: NotRequired[str]
    DatasourcePackageIngestHistory: NotRequired[
        Dict[
            DatasourcePackageType,
            Dict[DatasourcePackageIngestStateType, TimestampForCollectionTypeDef],
        ]
    ]

class MemberDetailTypeDef(TypedDict):
    AccountId: NotRequired[str]
    EmailAddress: NotRequired[str]
    GraphArn: NotRequired[str]
    MasterId: NotRequired[str]
    AdministratorId: NotRequired[str]
    Status: NotRequired[MemberStatusType]
    DisabledReason: NotRequired[MemberDisabledReasonType]
    InvitedTime: NotRequired[datetime]
    UpdatedTime: NotRequired[datetime]
    VolumeUsageInBytes: NotRequired[int]
    VolumeUsageUpdatedTime: NotRequired[datetime]
    PercentOfGraphUtilization: NotRequired[float]
    PercentOfGraphUtilizationUpdatedTime: NotRequired[datetime]
    InvitationType: NotRequired[InvitationTypeType]
    VolumeUsageByDatasourcePackage: NotRequired[
        Dict[DatasourcePackageType, DatasourcePackageUsageInfoTypeDef]
    ]
    DatasourcePackageIngestStates: NotRequired[
        Dict[DatasourcePackageType, DatasourcePackageIngestStateType]
    ]

class DateFilterTypeDef(TypedDict):
    StartInclusive: TimestampTypeDef
    EndInclusive: TimestampTypeDef

class StartInvestigationRequestTypeDef(TypedDict):
    GraphArn: str
    EntityArn: str
    ScopeStartTime: TimestampTypeDef
    ScopeEndTime: TimestampTypeDef

class ListGraphsResponseTypeDef(TypedDict):
    GraphList: List[GraphTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class IndicatorDetailTypeDef(TypedDict):
    TTPsObservedDetail: NotRequired[TTPsObservedDetailTypeDef]
    ImpossibleTravelDetail: NotRequired[ImpossibleTravelDetailTypeDef]
    FlaggedIpAddressDetail: NotRequired[FlaggedIpAddressDetailTypeDef]
    NewGeolocationDetail: NotRequired[NewGeolocationDetailTypeDef]
    NewAsoDetail: NotRequired[NewAsoDetailTypeDef]
    NewUserAgentDetail: NotRequired[NewUserAgentDetailTypeDef]
    RelatedFindingDetail: NotRequired[RelatedFindingDetailTypeDef]
    RelatedFindingGroupDetail: NotRequired[RelatedFindingGroupDetailTypeDef]

class ListInvestigationsResponseTypeDef(TypedDict):
    InvestigationDetails: List[InvestigationDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDatasourcePackagesResponseTypeDef(TypedDict):
    DatasourcePackages: Dict[DatasourcePackageType, DatasourcePackageIngestDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchGetGraphMemberDatasourcesResponseTypeDef(TypedDict):
    MemberDatasources: List[MembershipDatasourcesTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetMembershipDatasourcesResponseTypeDef(TypedDict):
    MembershipDatasources: List[MembershipDatasourcesTypeDef]
    UnprocessedGraphs: List[UnprocessedGraphTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembersResponseTypeDef(TypedDict):
    Members: List[MemberDetailTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembersResponseTypeDef(TypedDict):
    MemberDetails: List[MemberDetailTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(TypedDict):
    Invitations: List[MemberDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMembersResponseTypeDef(TypedDict):
    MemberDetails: List[MemberDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FilterCriteriaTypeDef(TypedDict):
    Severity: NotRequired[StringFilterTypeDef]
    Status: NotRequired[StringFilterTypeDef]
    State: NotRequired[StringFilterTypeDef]
    EntityArn: NotRequired[StringFilterTypeDef]
    CreatedTime: NotRequired[DateFilterTypeDef]

class IndicatorTypeDef(TypedDict):
    IndicatorType: NotRequired[IndicatorTypeType]
    IndicatorDetail: NotRequired[IndicatorDetailTypeDef]

class ListInvestigationsRequestTypeDef(TypedDict):
    GraphArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    FilterCriteria: NotRequired[FilterCriteriaTypeDef]
    SortCriteria: NotRequired[SortCriteriaTypeDef]

class ListIndicatorsResponseTypeDef(TypedDict):
    GraphArn: str
    InvestigationId: str
    Indicators: List[IndicatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
