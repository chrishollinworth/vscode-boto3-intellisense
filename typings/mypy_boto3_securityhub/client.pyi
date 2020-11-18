# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for securityhub service client

Usage::

    ```python
    import boto3
    from mypy_boto3_securityhub import SecurityHubClient

    client: SecurityHubClient = boto3.client("securityhub")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_securityhub.paginator import (
    GetEnabledStandardsPaginator,
    GetFindingsPaginator,
    GetInsightsPaginator,
    ListEnabledProductsForImportPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
)
from mypy_boto3_securityhub.type_defs import (
    AccountDetailsTypeDef,
    AwsSecurityFindingFiltersTypeDef,
    AwsSecurityFindingIdentifierTypeDef,
    AwsSecurityFindingTypeDef,
    BatchDisableStandardsResponseTypeDef,
    BatchEnableStandardsResponseTypeDef,
    BatchImportFindingsResponseTypeDef,
    BatchUpdateFindingsResponseTypeDef,
    CreateActionTargetResponseTypeDef,
    CreateInsightResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteActionTargetResponseTypeDef,
    DeleteInsightResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeActionTargetsResponseTypeDef,
    DescribeHubResponseTypeDef,
    DescribeProductsResponseTypeDef,
    DescribeStandardsControlsResponseTypeDef,
    DescribeStandardsResponseTypeDef,
    EnableImportFindingsForProductResponseTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightResultsResponseTypeDef,
    GetInsightsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMembersResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NoteUpdateTypeDef,
    RelatedFindingTypeDef,
    SeverityUpdateTypeDef,
    SortCriterionTypeDef,
    StandardsSubscriptionRequestTypeDef,
    WorkflowUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SecurityHubClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidAccessException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class SecurityHubClient:
    """
    [SecurityHub.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_invitation(self, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.accept_invitation)
        """

    def batch_disable_standards(
        self, StandardsSubscriptionArns: List[str]
    ) -> BatchDisableStandardsResponseTypeDef:
        """
        [Client.batch_disable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.batch_disable_standards)
        """

    def batch_enable_standards(
        self, StandardsSubscriptionRequests: List[StandardsSubscriptionRequestTypeDef]
    ) -> BatchEnableStandardsResponseTypeDef:
        """
        [Client.batch_enable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.batch_enable_standards)
        """

    def batch_import_findings(
        self, Findings: List["AwsSecurityFindingTypeDef"]
    ) -> BatchImportFindingsResponseTypeDef:
        """
        [Client.batch_import_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.batch_import_findings)
        """

    def batch_update_findings(
        self,
        FindingIdentifiers: List["AwsSecurityFindingIdentifierTypeDef"],
        Note: NoteUpdateTypeDef = None,
        Severity: SeverityUpdateTypeDef = None,
        VerificationState: Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ] = None,
        Confidence: int = None,
        Criticality: int = None,
        Types: List[str] = None,
        UserDefinedFields: Dict[str, str] = None,
        Workflow: WorkflowUpdateTypeDef = None,
        RelatedFindings: List["RelatedFindingTypeDef"] = None,
    ) -> BatchUpdateFindingsResponseTypeDef:
        """
        [Client.batch_update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.batch_update_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.can_paginate)
        """

    def create_action_target(
        self, Name: str, Description: str, Id: str
    ) -> CreateActionTargetResponseTypeDef:
        """
        [Client.create_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.create_action_target)
        """

    def create_insight(
        self, Name: str, Filters: "AwsSecurityFindingFiltersTypeDef", GroupByAttribute: str
    ) -> CreateInsightResponseTypeDef:
        """
        [Client.create_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.create_insight)
        """

    def create_members(
        self, AccountDetails: List[AccountDetailsTypeDef] = None
    ) -> CreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.create_members)
        """

    def decline_invitations(self, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.decline_invitations)
        """

    def delete_action_target(self, ActionTargetArn: str) -> DeleteActionTargetResponseTypeDef:
        """
        [Client.delete_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.delete_action_target)
        """

    def delete_insight(self, InsightArn: str) -> DeleteInsightResponseTypeDef:
        """
        [Client.delete_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.delete_insight)
        """

    def delete_invitations(self, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.delete_invitations)
        """

    def delete_members(self, AccountIds: List[str] = None) -> DeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.delete_members)
        """

    def describe_action_targets(
        self, ActionTargetArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeActionTargetsResponseTypeDef:
        """
        [Client.describe_action_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.describe_action_targets)
        """

    def describe_hub(self, HubArn: str = None) -> DescribeHubResponseTypeDef:
        """
        [Client.describe_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.describe_hub)
        """

    def describe_products(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeProductsResponseTypeDef:
        """
        [Client.describe_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.describe_products)
        """

    def describe_standards(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsResponseTypeDef:
        """
        [Client.describe_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.describe_standards)
        """

    def describe_standards_controls(
        self, StandardsSubscriptionArn: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsControlsResponseTypeDef:
        """
        [Client.describe_standards_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.describe_standards_controls)
        """

    def disable_import_findings_for_product(self, ProductSubscriptionArn: str) -> Dict[str, Any]:
        """
        [Client.disable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.disable_import_findings_for_product)
        """

    def disable_security_hub(self) -> Dict[str, Any]:
        """
        [Client.disable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.disable_security_hub)
        """

    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        [Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_master_account)
        """

    def disassociate_members(self, AccountIds: List[str] = None) -> Dict[str, Any]:
        """
        [Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.disassociate_members)
        """

    def enable_import_findings_for_product(
        self, ProductArn: str
    ) -> EnableImportFindingsForProductResponseTypeDef:
        """
        [Client.enable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.enable_import_findings_for_product)
        """

    def enable_security_hub(
        self, Tags: Dict[str, str] = None, EnableDefaultStandards: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.enable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.enable_security_hub)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.generate_presigned_url)
        """

    def get_enabled_standards(
        self,
        StandardsSubscriptionArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetEnabledStandardsResponseTypeDef:
        """
        [Client.get_enabled_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.get_enabled_standards)
        """

    def get_findings(
        self,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetFindingsResponseTypeDef:
        """
        [Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.get_findings)
        """

    def get_insight_results(self, InsightArn: str) -> GetInsightResultsResponseTypeDef:
        """
        [Client.get_insight_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.get_insight_results)
        """

    def get_insights(
        self, InsightArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> GetInsightsResponseTypeDef:
        """
        [Client.get_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.get_insights)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.get_invitations_count)
        """

    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        [Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.get_master_account)
        """

    def get_members(self, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.get_members)
        """

    def invite_members(self, AccountIds: List[str] = None) -> InviteMembersResponseTypeDef:
        """
        [Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.invite_members)
        """

    def list_enabled_products_for_import(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListEnabledProductsForImportResponseTypeDef:
        """
        [Client.list_enabled_products_for_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.list_enabled_products_for_import)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.list_invitations)
        """

    def list_members(
        self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.list_members)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.untag_resource)
        """

    def update_action_target(
        self, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.update_action_target)
        """

    def update_findings(
        self,
        Filters: "AwsSecurityFindingFiltersTypeDef",
        Note: NoteUpdateTypeDef = None,
        RecordState: Literal["ACTIVE", "ARCHIVED"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.update_findings)
        """

    def update_insight(
        self,
        InsightArn: str,
        Name: str = None,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        GroupByAttribute: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.update_insight)
        """

    def update_security_hub_configuration(self, AutoEnableControls: bool = None) -> Dict[str, Any]:
        """
        [Client.update_security_hub_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.update_security_hub_configuration)
        """

    def update_standards_control(
        self,
        StandardsControlArn: str,
        ControlStatus: Literal["ENABLED", "DISABLED"] = None,
        DisabledReason: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_standards_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Client.update_standards_control)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_enabled_standards"]
    ) -> GetEnabledStandardsPaginator:
        """
        [Paginator.GetEnabledStandards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_findings"]) -> GetFindingsPaginator:
        """
        [Paginator.GetFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_insights"]) -> GetInsightsPaginator:
        """
        [Paginator.GetInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> ListEnabledProductsForImportPaginator:
        """
        [Paginator.ListEnabledProductsForImport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)
        """
