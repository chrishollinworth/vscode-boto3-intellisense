"""
Type annotations for inspector2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_inspector2 import Inspector2Client

    client: Inspector2Client = boto3.client("inspector2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AggregationTypeType,
    FilterActionType,
    GroupKeyType,
    ReportFormatType,
    ResourceScanTypeType,
    ResourceTypeType,
    SbomReportFormatType,
    ScanTypeType,
    ServiceType,
)
from .paginator import (
    ListAccountPermissionsPaginator,
    ListCoveragePaginator,
    ListCoverageStatisticsPaginator,
    ListDelegatedAdminAccountsPaginator,
    ListFiltersPaginator,
    ListFindingAggregationsPaginator,
    ListFindingsPaginator,
    ListMembersPaginator,
    ListUsageTotalsPaginator,
    SearchVulnerabilitiesPaginator,
)
from .type_defs import (
    AggregationRequestTypeDef,
    AssociateMemberResponseTypeDef,
    AutoEnableTypeDef,
    BatchGetAccountStatusResponseTypeDef,
    BatchGetCodeSnippetResponseTypeDef,
    BatchGetFindingDetailsResponseTypeDef,
    BatchGetFreeTrialInfoResponseTypeDef,
    BatchGetMemberEc2DeepInspectionStatusResponseTypeDef,
    BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef,
    CancelFindingsReportResponseTypeDef,
    CancelSbomExportResponseTypeDef,
    CoverageFilterCriteriaTypeDef,
    CreateFilterResponseTypeDef,
    CreateFindingsReportResponseTypeDef,
    CreateSbomExportResponseTypeDef,
    DeleteFilterResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DestinationTypeDef,
    DisableDelegatedAdminAccountResponseTypeDef,
    DisableResponseTypeDef,
    DisassociateMemberResponseTypeDef,
    EcrConfigurationTypeDef,
    EnableDelegatedAdminAccountResponseTypeDef,
    EnableResponseTypeDef,
    FilterCriteriaTypeDef,
    GetConfigurationResponseTypeDef,
    GetDelegatedAdminAccountResponseTypeDef,
    GetEc2DeepInspectionConfigurationResponseTypeDef,
    GetEncryptionKeyResponseTypeDef,
    GetFindingsReportStatusResponseTypeDef,
    GetMemberResponseTypeDef,
    GetSbomExportResponseTypeDef,
    ListAccountPermissionsResponseTypeDef,
    ListCoverageResponseTypeDef,
    ListCoverageStatisticsResponseTypeDef,
    ListDelegatedAdminAccountsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingAggregationsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsageTotalsResponseTypeDef,
    MemberAccountEc2DeepInspectionStatusTypeDef,
    ResourceFilterCriteriaTypeDef,
    SearchVulnerabilitiesFilterCriteriaTypeDef,
    SearchVulnerabilitiesResponseTypeDef,
    SortCriteriaTypeDef,
    StringFilterTypeDef,
    UpdateEc2DeepInspectionConfigurationResponseTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateOrganizationConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Inspector2Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Inspector2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Inspector2Client exceptions.
        """
    def associate_member(self, *, accountId: str) -> AssociateMemberResponseTypeDef:
        """
        Associates an Amazon Web Services account with an Amazon Inspector delegated
        administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.associate_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#associate_member)
        """
    def batch_get_account_status(
        self, *, accountIds: List[str] = None
    ) -> BatchGetAccountStatusResponseTypeDef:
        """
        Retrieves the Amazon Inspector status of multiple Amazon Web Services accounts
        within your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.batch_get_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#batch_get_account_status)
        """
    def batch_get_code_snippet(
        self, *, findingArns: List[str]
    ) -> BatchGetCodeSnippetResponseTypeDef:
        """
        Retrieves code snippets from findings that Amazon Inspector detected code
        vulnerabilities in.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.batch_get_code_snippet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#batch_get_code_snippet)
        """
    def batch_get_finding_details(
        self, *, findingArns: List[str]
    ) -> BatchGetFindingDetailsResponseTypeDef:
        """
        Gets vulnerability details for findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.batch_get_finding_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#batch_get_finding_details)
        """
    def batch_get_free_trial_info(
        self, *, accountIds: List[str]
    ) -> BatchGetFreeTrialInfoResponseTypeDef:
        """
        Gets free trial status for multiple Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.batch_get_free_trial_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#batch_get_free_trial_info)
        """
    def batch_get_member_ec2_deep_inspection_status(
        self, *, accountIds: List[str] = None
    ) -> BatchGetMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Retrieves Amazon Inspector deep inspection activation status of multiple member
        accounts within your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.batch_get_member_ec2_deep_inspection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#batch_get_member_ec2_deep_inspection_status)
        """
    def batch_update_member_ec2_deep_inspection_status(
        self, *, accountIds: List["MemberAccountEc2DeepInspectionStatusTypeDef"]
    ) -> BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Activates or deactivates Amazon Inspector deep inspection for the provided
        member accounts in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.batch_update_member_ec2_deep_inspection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#batch_update_member_ec2_deep_inspection_status)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#can_paginate)
        """
    def cancel_findings_report(self, *, reportId: str) -> CancelFindingsReportResponseTypeDef:
        """
        Cancels the given findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.cancel_findings_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#cancel_findings_report)
        """
    def cancel_sbom_export(self, *, reportId: str) -> CancelSbomExportResponseTypeDef:
        """
        Cancels a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.cancel_sbom_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#cancel_sbom_export)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#close)
        """
    def create_filter(
        self,
        *,
        action: FilterActionType,
        filterCriteria: "FilterCriteriaTypeDef",
        name: str,
        description: str = None,
        reason: str = None,
        tags: Dict[str, str] = None
    ) -> CreateFilterResponseTypeDef:
        """
        Creates a filter resource using specified filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.create_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#create_filter)
        """
    def create_findings_report(
        self,
        *,
        reportFormat: ReportFormatType,
        s3Destination: "DestinationTypeDef",
        filterCriteria: "FilterCriteriaTypeDef" = None
    ) -> CreateFindingsReportResponseTypeDef:
        """
        Creates a finding report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.create_findings_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#create_findings_report)
        """
    def create_sbom_export(
        self,
        *,
        reportFormat: SbomReportFormatType,
        s3Destination: "DestinationTypeDef",
        resourceFilterCriteria: "ResourceFilterCriteriaTypeDef" = None
    ) -> CreateSbomExportResponseTypeDef:
        """
        Creates a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.create_sbom_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#create_sbom_export)
        """
    def delete_filter(self, *, arn: str) -> DeleteFilterResponseTypeDef:
        """
        Deletes a filter resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.delete_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#delete_filter)
        """
    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Describe Amazon Inspector configuration settings for an Amazon Web Services
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#describe_organization_configuration)
        """
    def disable(
        self, *, accountIds: List[str] = None, resourceTypes: List[ResourceScanTypeType] = None
    ) -> DisableResponseTypeDef:
        """
        Disables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.disable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#disable)
        """
    def disable_delegated_admin_account(
        self, *, delegatedAdminAccountId: str
    ) -> DisableDelegatedAdminAccountResponseTypeDef:
        """
        Disables the Amazon Inspector delegated administrator for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.disable_delegated_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#disable_delegated_admin_account)
        """
    def disassociate_member(self, *, accountId: str) -> DisassociateMemberResponseTypeDef:
        """
        Disassociates a member account from an Amazon Inspector delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.disassociate_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#disassociate_member)
        """
    def enable(
        self,
        *,
        resourceTypes: List[ResourceScanTypeType],
        accountIds: List[str] = None,
        clientToken: str = None
    ) -> EnableResponseTypeDef:
        """
        Enables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.enable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#enable)
        """
    def enable_delegated_admin_account(
        self, *, delegatedAdminAccountId: str, clientToken: str = None
    ) -> EnableDelegatedAdminAccountResponseTypeDef:
        """
        Enables the Amazon Inspector delegated administrator for your Organizations
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.enable_delegated_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#enable_delegated_admin_account)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#generate_presigned_url)
        """
    def get_configuration(self) -> GetConfigurationResponseTypeDef:
        """
        Retrieves setting configurations for Inspector scans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.get_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#get_configuration)
        """
    def get_delegated_admin_account(self) -> GetDelegatedAdminAccountResponseTypeDef:
        """
        Retrieves information about the Amazon Inspector delegated administrator for
        your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.get_delegated_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#get_delegated_admin_account)
        """
    def get_ec2_deep_inspection_configuration(
        self,
    ) -> GetEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Retrieves the activation status of Amazon Inspector deep inspection and custom
        paths associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.get_ec2_deep_inspection_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#get_ec2_deep_inspection_configuration)
        """
    def get_encryption_key(
        self, *, resourceType: ResourceTypeType, scanType: ScanTypeType
    ) -> GetEncryptionKeyResponseTypeDef:
        """
        Gets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.get_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#get_encryption_key)
        """
    def get_findings_report_status(
        self, *, reportId: str = None
    ) -> GetFindingsReportStatusResponseTypeDef:
        """
        Gets the status of a findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.get_findings_report_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#get_findings_report_status)
        """
    def get_member(self, *, accountId: str) -> GetMemberResponseTypeDef:
        """
        Gets member information for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.get_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#get_member)
        """
    def get_sbom_export(self, *, reportId: str) -> GetSbomExportResponseTypeDef:
        """
        Gets details of a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.get_sbom_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#get_sbom_export)
        """
    def list_account_permissions(
        self, *, maxResults: int = None, nextToken: str = None, service: ServiceType = None
    ) -> ListAccountPermissionsResponseTypeDef:
        """
        Lists the permissions an account has to configure Amazon Inspector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_account_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_account_permissions)
        """
    def list_coverage(
        self,
        *,
        filterCriteria: "CoverageFilterCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListCoverageResponseTypeDef:
        """
        Lists coverage details for you environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_coverage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_coverage)
        """
    def list_coverage_statistics(
        self,
        *,
        filterCriteria: "CoverageFilterCriteriaTypeDef" = None,
        groupBy: GroupKeyType = None,
        nextToken: str = None
    ) -> ListCoverageStatisticsResponseTypeDef:
        """
        Lists Amazon Inspector coverage statistics for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_coverage_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_coverage_statistics)
        """
    def list_delegated_admin_accounts(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListDelegatedAdminAccountsResponseTypeDef:
        """
        Lists information about the Amazon Inspector delegated administrator of your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_delegated_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_delegated_admin_accounts)
        """
    def list_filters(
        self,
        *,
        action: FilterActionType = None,
        arns: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListFiltersResponseTypeDef:
        """
        Lists the filters associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_filters)
        """
    def list_finding_aggregations(
        self,
        *,
        aggregationType: AggregationTypeType,
        accountIds: List["StringFilterTypeDef"] = None,
        aggregationRequest: "AggregationRequestTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListFindingAggregationsResponseTypeDef:
        """
        Lists aggregated finding data for your environment based on specific criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_finding_aggregations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_finding_aggregations)
        """
    def list_findings(
        self,
        *,
        filterCriteria: "FilterCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: "SortCriteriaTypeDef" = None
    ) -> ListFindingsResponseTypeDef:
        """
        Lists findings for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_findings)
        """
    def list_members(
        self, *, maxResults: int = None, nextToken: str = None, onlyAssociated: bool = None
    ) -> ListMembersResponseTypeDef:
        """
        List members associated with the Amazon Inspector delegated administrator for
        your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_members)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags attached to a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_tags_for_resource)
        """
    def list_usage_totals(
        self, *, accountIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> ListUsageTotalsResponseTypeDef:
        """
        Lists the Amazon Inspector usage totals over the last 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.list_usage_totals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#list_usage_totals)
        """
    def reset_encryption_key(
        self, *, resourceType: ResourceTypeType, scanType: ScanTypeType
    ) -> Dict[str, Any]:
        """
        Resets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.reset_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#reset_encryption_key)
        """
    def search_vulnerabilities(
        self, *, filterCriteria: "SearchVulnerabilitiesFilterCriteriaTypeDef", nextToken: str = None
    ) -> SearchVulnerabilitiesResponseTypeDef:
        """
        Lists Amazon Inspector coverage details for a specific vulnerability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.search_vulnerabilities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#search_vulnerabilities)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#untag_resource)
        """
    def update_configuration(
        self, *, ecrConfiguration: "EcrConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates setting configurations for your Amazon Inspector account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.update_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#update_configuration)
        """
    def update_ec2_deep_inspection_configuration(
        self, *, activateDeepInspection: bool = None, packagePaths: List[str] = None
    ) -> UpdateEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Activates, deactivates Amazon Inspector deep inspection, or updates custom paths
        for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.update_ec2_deep_inspection_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#update_ec2_deep_inspection_configuration)
        """
    def update_encryption_key(
        self, *, kmsKeyId: str, resourceType: ResourceTypeType, scanType: ScanTypeType
    ) -> Dict[str, Any]:
        """
        Updates an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.update_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#update_encryption_key)
        """
    def update_filter(
        self,
        *,
        filterArn: str,
        action: FilterActionType = None,
        description: str = None,
        filterCriteria: "FilterCriteriaTypeDef" = None,
        name: str = None,
        reason: str = None
    ) -> UpdateFilterResponseTypeDef:
        """
        Specifies the action that is to be applied to the findings that match the
        filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.update_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#update_filter)
        """
    def update_org_ec2_deep_inspection_configuration(
        self, *, orgPackagePaths: List[str]
    ) -> Dict[str, Any]:
        """
        Updates the Amazon Inspector deep inspection custom paths for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.update_org_ec2_deep_inspection_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#update_org_ec2_deep_inspection_configuration)
        """
    def update_organization_configuration(
        self, *, autoEnable: "AutoEnableTypeDef"
    ) -> UpdateOrganizationConfigurationResponseTypeDef:
        """
        Updates the configurations for your Amazon Inspector organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client.html#update_organization_configuration)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_permissions"]
    ) -> ListAccountPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListAccountPermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listaccountpermissionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_coverage"]) -> ListCoveragePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListCoverage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcoveragepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_coverage_statistics"]
    ) -> ListCoverageStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListCoverageStatistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcoveragestatisticspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_admin_accounts"]
    ) -> ListDelegatedAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListDelegatedAdminAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listdelegatedadminaccountspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListFilters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfilterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_finding_aggregations"]
    ) -> ListFindingAggregationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListFindingAggregations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfindingaggregationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfindingspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listmemberspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_totals"]
    ) -> ListUsageTotalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.ListUsageTotals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listusagetotalspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_vulnerabilities"]
    ) -> SearchVulnerabilitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/inspector2.html#Inspector2.Paginator.SearchVulnerabilities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#searchvulnerabilitiespaginator)
        """
