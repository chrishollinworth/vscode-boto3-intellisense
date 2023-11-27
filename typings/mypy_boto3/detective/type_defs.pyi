"""
Type annotations for detective service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/type_defs.html)

Usage::

    ```python
    from mypy_boto3_detective.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptInvitationRequestRequestTypeDef",
    "AccountTypeDef",
    "AdministratorTypeDef",
    "BatchGetGraphMemberDatasourcesRequestRequestTypeDef",
    "BatchGetGraphMemberDatasourcesResponseTypeDef",
    "BatchGetMembershipDatasourcesRequestRequestTypeDef",
    "BatchGetMembershipDatasourcesResponseTypeDef",
    "CreateGraphRequestRequestTypeDef",
    "CreateGraphResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "DatasourcePackageIngestDetailTypeDef",
    "DatasourcePackageUsageInfoTypeDef",
    "DateFilterTypeDef",
    "DeleteGraphRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DisassociateMembershipRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "FilterCriteriaTypeDef",
    "FlaggedIpAddressDetailTypeDef",
    "GetInvestigationRequestRequestTypeDef",
    "GetInvestigationResponseTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GraphTypeDef",
    "ImpossibleTravelDetailTypeDef",
    "IndicatorDetailTypeDef",
    "IndicatorTypeDef",
    "InvestigationDetailTypeDef",
    "ListDatasourcePackagesRequestRequestTypeDef",
    "ListDatasourcePackagesResponseTypeDef",
    "ListGraphsRequestRequestTypeDef",
    "ListGraphsResponseTypeDef",
    "ListIndicatorsRequestRequestTypeDef",
    "ListIndicatorsResponseTypeDef",
    "ListInvestigationsRequestRequestTypeDef",
    "ListInvestigationsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberDetailTypeDef",
    "MembershipDatasourcesTypeDef",
    "NewAsoDetailTypeDef",
    "NewGeolocationDetailTypeDef",
    "NewUserAgentDetailTypeDef",
    "RejectInvitationRequestRequestTypeDef",
    "RelatedFindingDetailTypeDef",
    "RelatedFindingGroupDetailTypeDef",
    "ResponseMetadataTypeDef",
    "SortCriteriaTypeDef",
    "StartInvestigationRequestRequestTypeDef",
    "StartInvestigationResponseTypeDef",
    "StartMonitoringMemberRequestRequestTypeDef",
    "StringFilterTypeDef",
    "TTPsObservedDetailTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimestampForCollectionTypeDef",
    "UnprocessedAccountTypeDef",
    "UnprocessedGraphTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasourcePackagesRequestRequestTypeDef",
    "UpdateInvestigationStateRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
    },
)

AdministratorTypeDef = TypedDict(
    "AdministratorTypeDef",
    {
        "AccountId": str,
        "GraphArn": str,
        "DelegationTime": datetime,
    },
    total=False,
)

BatchGetGraphMemberDatasourcesRequestRequestTypeDef = TypedDict(
    "BatchGetGraphMemberDatasourcesRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": List[str],
    },
)

BatchGetGraphMemberDatasourcesResponseTypeDef = TypedDict(
    "BatchGetGraphMemberDatasourcesResponseTypeDef",
    {
        "MemberDatasources": List["MembershipDatasourcesTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetMembershipDatasourcesRequestRequestTypeDef = TypedDict(
    "BatchGetMembershipDatasourcesRequestRequestTypeDef",
    {
        "GraphArns": List[str],
    },
)

BatchGetMembershipDatasourcesResponseTypeDef = TypedDict(
    "BatchGetMembershipDatasourcesResponseTypeDef",
    {
        "MembershipDatasources": List["MembershipDatasourcesTypeDef"],
        "UnprocessedGraphs": List["UnprocessedGraphTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGraphRequestRequestTypeDef = TypedDict(
    "CreateGraphRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateGraphResponseTypeDef = TypedDict(
    "CreateGraphResponseTypeDef",
    {
        "GraphArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMembersRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "Accounts": List["AccountTypeDef"],
    },
)
_OptionalCreateMembersRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMembersRequestRequestTypeDef",
    {
        "Message": str,
        "DisableEmailNotification": bool,
    },
    total=False,
)

class CreateMembersRequestRequestTypeDef(
    _RequiredCreateMembersRequestRequestTypeDef, _OptionalCreateMembersRequestRequestTypeDef
):
    pass

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "Members": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatasourcePackageIngestDetailTypeDef = TypedDict(
    "DatasourcePackageIngestDetailTypeDef",
    {
        "DatasourcePackageIngestState": DatasourcePackageIngestStateType,
        "LastIngestStateChange": Dict[
            DatasourcePackageIngestStateType, "TimestampForCollectionTypeDef"
        ],
    },
    total=False,
)

DatasourcePackageUsageInfoTypeDef = TypedDict(
    "DatasourcePackageUsageInfoTypeDef",
    {
        "VolumeUsageInBytes": int,
        "VolumeUsageUpdateTime": datetime,
    },
    total=False,
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "StartInclusive": Union[datetime, str],
        "EndInclusive": Union[datetime, str],
    },
)

DeleteGraphRequestRequestTypeDef = TypedDict(
    "DeleteGraphRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": List[str],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "AccountIds": List[str],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateMembershipRequestRequestTypeDef = TypedDict(
    "DisassociateMembershipRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Severity": "StringFilterTypeDef",
        "Status": "StringFilterTypeDef",
        "State": "StringFilterTypeDef",
        "EntityArn": "StringFilterTypeDef",
        "CreatedTime": "DateFilterTypeDef",
    },
    total=False,
)

FlaggedIpAddressDetailTypeDef = TypedDict(
    "FlaggedIpAddressDetailTypeDef",
    {
        "IpAddress": str,
        "Reason": Literal["AWS_THREAT_INTELLIGENCE"],
    },
    total=False,
)

GetInvestigationRequestRequestTypeDef = TypedDict(
    "GetInvestigationRequestRequestTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
    },
)

GetInvestigationResponseTypeDef = TypedDict(
    "GetInvestigationResponseTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
        "EntityArn": str,
        "EntityType": EntityTypeType,
        "CreatedTime": datetime,
        "ScopeStartTime": datetime,
        "ScopeEndTime": datetime,
        "Status": StatusType,
        "Severity": SeverityType,
        "State": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": List[str],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphTypeDef = TypedDict(
    "GraphTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ImpossibleTravelDetailTypeDef = TypedDict(
    "ImpossibleTravelDetailTypeDef",
    {
        "StartingIpAddress": str,
        "EndingIpAddress": str,
        "StartingLocation": str,
        "EndingLocation": str,
        "HourlyTimeDelta": int,
    },
    total=False,
)

IndicatorDetailTypeDef = TypedDict(
    "IndicatorDetailTypeDef",
    {
        "TTPsObservedDetail": "TTPsObservedDetailTypeDef",
        "ImpossibleTravelDetail": "ImpossibleTravelDetailTypeDef",
        "FlaggedIpAddressDetail": "FlaggedIpAddressDetailTypeDef",
        "NewGeolocationDetail": "NewGeolocationDetailTypeDef",
        "NewAsoDetail": "NewAsoDetailTypeDef",
        "NewUserAgentDetail": "NewUserAgentDetailTypeDef",
        "RelatedFindingDetail": "RelatedFindingDetailTypeDef",
        "RelatedFindingGroupDetail": "RelatedFindingGroupDetailTypeDef",
    },
    total=False,
)

IndicatorTypeDef = TypedDict(
    "IndicatorTypeDef",
    {
        "IndicatorType": IndicatorTypeType,
        "IndicatorDetail": "IndicatorDetailTypeDef",
    },
    total=False,
)

InvestigationDetailTypeDef = TypedDict(
    "InvestigationDetailTypeDef",
    {
        "InvestigationId": str,
        "Severity": SeverityType,
        "Status": StatusType,
        "State": StateType,
        "CreatedTime": datetime,
        "EntityArn": str,
        "EntityType": EntityTypeType,
    },
    total=False,
)

_RequiredListDatasourcePackagesRequestRequestTypeDef = TypedDict(
    "_RequiredListDatasourcePackagesRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
_OptionalListDatasourcePackagesRequestRequestTypeDef = TypedDict(
    "_OptionalListDatasourcePackagesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDatasourcePackagesRequestRequestTypeDef(
    _RequiredListDatasourcePackagesRequestRequestTypeDef,
    _OptionalListDatasourcePackagesRequestRequestTypeDef,
):
    pass

ListDatasourcePackagesResponseTypeDef = TypedDict(
    "ListDatasourcePackagesResponseTypeDef",
    {
        "DatasourcePackages": Dict[DatasourcePackageType, "DatasourcePackageIngestDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGraphsRequestRequestTypeDef = TypedDict(
    "ListGraphsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListGraphsResponseTypeDef = TypedDict(
    "ListGraphsResponseTypeDef",
    {
        "GraphList": List["GraphTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIndicatorsRequestRequestTypeDef = TypedDict(
    "_RequiredListIndicatorsRequestRequestTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
    },
)
_OptionalListIndicatorsRequestRequestTypeDef = TypedDict(
    "_OptionalListIndicatorsRequestRequestTypeDef",
    {
        "IndicatorType": IndicatorTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListIndicatorsRequestRequestTypeDef(
    _RequiredListIndicatorsRequestRequestTypeDef, _OptionalListIndicatorsRequestRequestTypeDef
):
    pass

ListIndicatorsResponseTypeDef = TypedDict(
    "ListIndicatorsResponseTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
        "NextToken": str,
        "Indicators": List["IndicatorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInvestigationsRequestRequestTypeDef = TypedDict(
    "_RequiredListInvestigationsRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
_OptionalListInvestigationsRequestRequestTypeDef = TypedDict(
    "_OptionalListInvestigationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FilterCriteria": "FilterCriteriaTypeDef",
        "SortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)

class ListInvestigationsRequestRequestTypeDef(
    _RequiredListInvestigationsRequestRequestTypeDef,
    _OptionalListInvestigationsRequestRequestTypeDef,
):
    pass

ListInvestigationsResponseTypeDef = TypedDict(
    "ListInvestigationsResponseTypeDef",
    {
        "InvestigationDetails": List["InvestigationDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
_OptionalListMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListMembersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMembersRequestRequestTypeDef(
    _RequiredListMembersRequestRequestTypeDef, _OptionalListMembersRequestRequestTypeDef
):
    pass

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "Administrators": List["AdministratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberDetailTypeDef = TypedDict(
    "MemberDetailTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "AdministratorId": str,
        "Status": MemberStatusType,
        "DisabledReason": MemberDisabledReasonType,
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
        "VolumeUsageInBytes": int,
        "VolumeUsageUpdatedTime": datetime,
        "PercentOfGraphUtilization": float,
        "PercentOfGraphUtilizationUpdatedTime": datetime,
        "InvitationType": InvitationTypeType,
        "VolumeUsageByDatasourcePackage": Dict[
            DatasourcePackageType, "DatasourcePackageUsageInfoTypeDef"
        ],
        "DatasourcePackageIngestStates": Dict[
            DatasourcePackageType, DatasourcePackageIngestStateType
        ],
    },
    total=False,
)

MembershipDatasourcesTypeDef = TypedDict(
    "MembershipDatasourcesTypeDef",
    {
        "AccountId": str,
        "GraphArn": str,
        "DatasourcePackageIngestHistory": Dict[
            DatasourcePackageType,
            Dict[DatasourcePackageIngestStateType, "TimestampForCollectionTypeDef"],
        ],
    },
    total=False,
)

NewAsoDetailTypeDef = TypedDict(
    "NewAsoDetailTypeDef",
    {
        "Aso": str,
        "IsNewForEntireAccount": bool,
    },
    total=False,
)

NewGeolocationDetailTypeDef = TypedDict(
    "NewGeolocationDetailTypeDef",
    {
        "Location": str,
        "IpAddress": str,
        "IsNewForEntireAccount": bool,
    },
    total=False,
)

NewUserAgentDetailTypeDef = TypedDict(
    "NewUserAgentDetailTypeDef",
    {
        "UserAgent": str,
        "IsNewForEntireAccount": bool,
    },
    total=False,
)

RejectInvitationRequestRequestTypeDef = TypedDict(
    "RejectInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

RelatedFindingDetailTypeDef = TypedDict(
    "RelatedFindingDetailTypeDef",
    {
        "Arn": str,
        "Type": str,
        "IpAddress": str,
    },
    total=False,
)

RelatedFindingGroupDetailTypeDef = TypedDict(
    "RelatedFindingGroupDetailTypeDef",
    {
        "Id": str,
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

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "Field": FieldType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

StartInvestigationRequestRequestTypeDef = TypedDict(
    "StartInvestigationRequestRequestTypeDef",
    {
        "GraphArn": str,
        "EntityArn": str,
        "ScopeStartTime": Union[datetime, str],
        "ScopeEndTime": Union[datetime, str],
    },
)

StartInvestigationResponseTypeDef = TypedDict(
    "StartInvestigationResponseTypeDef",
    {
        "InvestigationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMonitoringMemberRequestRequestTypeDef = TypedDict(
    "StartMonitoringMemberRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountId": str,
    },
)

StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "Value": str,
    },
)

TTPsObservedDetailTypeDef = TypedDict(
    "TTPsObservedDetailTypeDef",
    {
        "Tactic": str,
        "Technique": str,
        "Procedure": str,
        "IpAddress": str,
        "APIName": str,
        "APISuccessCount": int,
        "APIFailureCount": int,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TimestampForCollectionTypeDef = TypedDict(
    "TimestampForCollectionTypeDef",
    {
        "Timestamp": datetime,
    },
    total=False,
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Reason": str,
    },
    total=False,
)

UnprocessedGraphTypeDef = TypedDict(
    "UnprocessedGraphTypeDef",
    {
        "GraphArn": str,
        "Reason": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateDatasourcePackagesRequestRequestTypeDef = TypedDict(
    "UpdateDatasourcePackagesRequestRequestTypeDef",
    {
        "GraphArn": str,
        "DatasourcePackages": List[DatasourcePackageType],
    },
)

UpdateInvestigationStateRequestRequestTypeDef = TypedDict(
    "UpdateInvestigationStateRequestRequestTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
        "State": StateType,
    },
)

_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
    },
    total=False,
)

class UpdateOrganizationConfigurationRequestRequestTypeDef(
    _RequiredUpdateOrganizationConfigurationRequestRequestTypeDef,
    _OptionalUpdateOrganizationConfigurationRequestRequestTypeDef,
):
    pass
