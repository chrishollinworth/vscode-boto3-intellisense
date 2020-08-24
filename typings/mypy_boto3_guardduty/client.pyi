# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for guardduty service client

Usage::

    ```python
    import boto3
    from mypy_boto3_guardduty import GuardDutyClient

    client: GuardDutyClient = boto3.client("guardduty")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_guardduty.paginator import (
    ListDetectorsPaginator,
    ListFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListIPSetsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListThreatIntelSetsPaginator,
)
from mypy_boto3_guardduty.type_defs import (
    AccountDetailTypeDef,
    CreateDetectorResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateMembersResponseTypeDef,
    CreatePublishingDestinationResponseTypeDef,
    CreateThreatIntelSetResponseTypeDef,
    DataSourceConfigurationsTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DescribePublishingDestinationResponseTypeDef,
    DestinationPropertiesTypeDef,
    DisassociateMembersResponseTypeDef,
    FindingCriteriaTypeDef,
    GetDetectorResponseTypeDef,
    GetFilterResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingsStatisticsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMemberDetectorsResponseTypeDef,
    GetMembersResponseTypeDef,
    GetThreatIntelSetResponseTypeDef,
    GetUsageStatisticsResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListDetectorsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListPublishingDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThreatIntelSetsResponseTypeDef,
    OrganizationDataSourceConfigurationsTypeDef,
    SortCriteriaTypeDef,
    StartMonitoringMembersResponseTypeDef,
    StopMonitoringMembersResponseTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateMemberDetectorsResponseTypeDef,
    UsageCriteriaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GuardDutyClient",)


class Exceptions:
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    InternalServerErrorException: Type[Boto3ClientError]


class GuardDutyClient:
    """
    [GuardDuty.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client)
    """

    exceptions: Exceptions

    def accept_invitation(
        self, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.accept_invitation)
        """

    def archive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Client.archive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.archive_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.can_paginate)
        """

    def create_detector(
        self,
        Enable: bool,
        ClientToken: str = None,
        FindingPublishingFrequency: Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"] = None,
        DataSources: DataSourceConfigurationsTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateDetectorResponseTypeDef:
        """
        [Client.create_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.create_detector)
        """

    def create_filter(
        self,
        DetectorId: str,
        Name: str,
        FindingCriteria: "FindingCriteriaTypeDef",
        Description: str = None,
        Action: Literal["NOOP", "ARCHIVE"] = None,
        Rank: int = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateFilterResponseTypeDef:
        """
        [Client.create_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.create_filter)
        """

    def create_ip_set(
        self,
        DetectorId: str,
        Name: str,
        Format: Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateIPSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.create_ip_set)
        """

    def create_members(
        self, DetectorId: str, AccountDetails: List[AccountDetailTypeDef]
    ) -> CreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.create_members)
        """

    def create_publishing_destination(
        self,
        DetectorId: str,
        DestinationType: Literal["S3"],
        DestinationProperties: "DestinationPropertiesTypeDef",
        ClientToken: str = None,
    ) -> CreatePublishingDestinationResponseTypeDef:
        """
        [Client.create_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.create_publishing_destination)
        """

    def create_sample_findings(
        self, DetectorId: str, FindingTypes: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_sample_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.create_sample_findings)
        """

    def create_threat_intel_set(
        self,
        DetectorId: str,
        Name: str,
        Format: Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateThreatIntelSetResponseTypeDef:
        """
        [Client.create_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.create_threat_intel_set)
        """

    def decline_invitations(self, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.decline_invitations)
        """

    def delete_detector(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Client.delete_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.delete_detector)
        """

    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        """
        [Client.delete_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.delete_filter)
        """

    def delete_invitations(self, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.delete_invitations)
        """

    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.delete_ip_set)
        """

    def delete_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> DeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.delete_members)
        """

    def delete_publishing_destination(self, DetectorId: str, DestinationId: str) -> Dict[str, Any]:
        """
        [Client.delete_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.delete_publishing_destination)
        """

    def delete_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict[str, Any]:
        """
        [Client.delete_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.delete_threat_intel_set)
        """

    def describe_organization_configuration(
        self, DetectorId: str
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        [Client.describe_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.describe_organization_configuration)
        """

    def describe_publishing_destination(
        self, DetectorId: str, DestinationId: str
    ) -> DescribePublishingDestinationResponseTypeDef:
        """
        [Client.describe_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.describe_publishing_destination)
        """

    def disable_organization_admin_account(self, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Client.disable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.disable_organization_admin_account)
        """

    def disassociate_from_master_account(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_master_account)
        """

    def disassociate_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> DisassociateMembersResponseTypeDef:
        """
        [Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.disassociate_members)
        """

    def enable_organization_admin_account(self, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Client.enable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.enable_organization_admin_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.generate_presigned_url)
        """

    def get_detector(self, DetectorId: str) -> GetDetectorResponseTypeDef:
        """
        [Client.get_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_detector)
        """

    def get_filter(self, DetectorId: str, FilterName: str) -> GetFilterResponseTypeDef:
        """
        [Client.get_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_filter)
        """

    def get_findings(
        self, DetectorId: str, FindingIds: List[str], SortCriteria: SortCriteriaTypeDef = None
    ) -> GetFindingsResponseTypeDef:
        """
        [Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_findings)
        """

    def get_findings_statistics(
        self,
        DetectorId: str,
        FindingStatisticTypes: List[Literal["COUNT_BY_SEVERITY"]],
        FindingCriteria: "FindingCriteriaTypeDef" = None,
    ) -> GetFindingsStatisticsResponseTypeDef:
        """
        [Client.get_findings_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_findings_statistics)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_invitations_count)
        """

    def get_ip_set(self, DetectorId: str, IpSetId: str) -> GetIPSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_ip_set)
        """

    def get_master_account(self, DetectorId: str) -> GetMasterAccountResponseTypeDef:
        """
        [Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_master_account)
        """

    def get_member_detectors(
        self, DetectorId: str, AccountIds: List[str]
    ) -> GetMemberDetectorsResponseTypeDef:
        """
        [Client.get_member_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_member_detectors)
        """

    def get_members(self, DetectorId: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_members)
        """

    def get_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> GetThreatIntelSetResponseTypeDef:
        """
        [Client.get_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_threat_intel_set)
        """

    def get_usage_statistics(
        self,
        DetectorId: str,
        UsageStatisticType: Literal[
            "SUM_BY_ACCOUNT", "SUM_BY_DATA_SOURCE", "SUM_BY_RESOURCE", "TOP_RESOURCES"
        ],
        UsageCriteria: UsageCriteriaTypeDef,
        Unit: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetUsageStatisticsResponseTypeDef:
        """
        [Client.get_usage_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.get_usage_statistics)
        """

    def invite_members(
        self,
        DetectorId: str,
        AccountIds: List[str],
        DisableEmailNotification: bool = None,
        Message: str = None,
    ) -> InviteMembersResponseTypeDef:
        """
        [Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.invite_members)
        """

    def list_detectors(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListDetectorsResponseTypeDef:
        """
        [Client.list_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_detectors)
        """

    def list_filters(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFiltersResponseTypeDef:
        """
        [Client.list_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_filters)
        """

    def list_findings(
        self,
        DetectorId: str,
        FindingCriteria: "FindingCriteriaTypeDef" = None,
        SortCriteria: SortCriteriaTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_findings)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_invitations)
        """

    def list_ip_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_ip_sets)
        """

    def list_members(
        self,
        DetectorId: str,
        MaxResults: int = None,
        NextToken: str = None,
        OnlyAssociated: str = None,
    ) -> ListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_members)
        """

    def list_organization_admin_accounts(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        [Client.list_organization_admin_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_organization_admin_accounts)
        """

    def list_publishing_destinations(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPublishingDestinationsResponseTypeDef:
        """
        [Client.list_publishing_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_publishing_destinations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_tags_for_resource)
        """

    def list_threat_intel_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListThreatIntelSetsResponseTypeDef:
        """
        [Client.list_threat_intel_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.list_threat_intel_sets)
        """

    def start_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> StartMonitoringMembersResponseTypeDef:
        """
        [Client.start_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.start_monitoring_members)
        """

    def stop_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> StopMonitoringMembersResponseTypeDef:
        """
        [Client.stop_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.stop_monitoring_members)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.tag_resource)
        """

    def unarchive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Client.unarchive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.unarchive_findings)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.untag_resource)
        """

    def update_detector(
        self,
        DetectorId: str,
        Enable: bool = None,
        FindingPublishingFrequency: Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"] = None,
        DataSources: DataSourceConfigurationsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_detector)
        """

    def update_filter(
        self,
        DetectorId: str,
        FilterName: str,
        Description: str = None,
        Action: Literal["NOOP", "ARCHIVE"] = None,
        Rank: int = None,
        FindingCriteria: "FindingCriteriaTypeDef" = None,
    ) -> UpdateFilterResponseTypeDef:
        """
        [Client.update_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_filter)
        """

    def update_findings_feedback(
        self,
        DetectorId: str,
        FindingIds: List[str],
        Feedback: Literal["USEFUL", "NOT_USEFUL"],
        Comments: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_findings_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_findings_feedback)
        """

    def update_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_ip_set)
        """

    def update_member_detectors(
        self,
        DetectorId: str,
        AccountIds: List[str],
        DataSources: DataSourceConfigurationsTypeDef = None,
    ) -> UpdateMemberDetectorsResponseTypeDef:
        """
        [Client.update_member_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_member_detectors)
        """

    def update_organization_configuration(
        self,
        DetectorId: str,
        AutoEnable: bool,
        DataSources: OrganizationDataSourceConfigurationsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_organization_configuration)
        """

    def update_publishing_destination(
        self,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: "DestinationPropertiesTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_publishing_destination)
        """

    def update_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Client.update_threat_intel_set)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_detectors"]) -> ListDetectorsPaginator:
        """
        [Paginator.ListDetectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_sets"]) -> ListIPSetsPaginator:
        """
        [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Paginator.ListOrganizationAdminAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListOrganizationAdminAccounts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_threat_intel_sets"]
    ) -> ListThreatIntelSetsPaginator:
        """
        [Paginator.ListThreatIntelSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
