"""
Type annotations for securityhub service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_securityhub import SecurityHubClient

    client: SecurityHubClient = boto3.client("securityhub")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ControlStatusType, RecordStateType, VerificationStateType
from .paginator import (
    GetEnabledStandardsPaginator,
    GetFindingsPaginator,
    GetInsightsPaginator,
    ListEnabledProductsForImportPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
)
from .type_defs import (
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
    DescribeOrganizationConfigurationResponseTypeDef,
    DescribeProductsResponseTypeDef,
    DescribeStandardsControlsResponseTypeDef,
    DescribeStandardsResponseTypeDef,
    EnableImportFindingsForProductResponseTypeDef,
    GetAdministratorAccountResponseTypeDef,
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
    ListOrganizationAdminAccountsResponseTypeDef,
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

class SecurityHubClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        SecurityHubClient exceptions.
        """
    def accept_administrator_invitation(
        self, *, AdministratorId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        Accepts the invitation to be a member account and be monitored by the Security
        Hub administrator account that the invitation was sent from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.accept_administrator_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#accept_administrator_invitation)
        """
    def accept_invitation(self, *, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#accept_invitation)
        """
    def batch_disable_standards(
        self, *, StandardsSubscriptionArns: List[str]
    ) -> BatchDisableStandardsResponseTypeDef:
        """
        Disables the standards specified by the provided `StandardsSubscriptionArns` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.batch_disable_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_disable_standards)
        """
    def batch_enable_standards(
        self, *, StandardsSubscriptionRequests: List["StandardsSubscriptionRequestTypeDef"]
    ) -> BatchEnableStandardsResponseTypeDef:
        """
        Enables the standards specified by the provided `StandardsArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.batch_enable_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_enable_standards)
        """
    def batch_import_findings(
        self, *, Findings: List["AwsSecurityFindingTypeDef"]
    ) -> BatchImportFindingsResponseTypeDef:
        """
        Imports security findings generated from an integrated product into Security
        Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.batch_import_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_import_findings)
        """
    def batch_update_findings(
        self,
        *,
        FindingIdentifiers: List["AwsSecurityFindingIdentifierTypeDef"],
        Note: "NoteUpdateTypeDef" = None,
        Severity: "SeverityUpdateTypeDef" = None,
        VerificationState: VerificationStateType = None,
        Confidence: int = None,
        Criticality: int = None,
        Types: List[str] = None,
        UserDefinedFields: Dict[str, str] = None,
        Workflow: "WorkflowUpdateTypeDef" = None,
        RelatedFindings: List["RelatedFindingTypeDef"] = None
    ) -> BatchUpdateFindingsResponseTypeDef:
        """
        Used by Security Hub customers to update information about their investigation
        into a finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.batch_update_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_update_findings)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#can_paginate)
        """
    def create_action_target(
        self, *, Name: str, Description: str, Id: str
    ) -> CreateActionTargetResponseTypeDef:
        """
        Creates a custom action target in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.create_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_action_target)
        """
    def create_insight(
        self, *, Name: str, Filters: "AwsSecurityFindingFiltersTypeDef", GroupByAttribute: str
    ) -> CreateInsightResponseTypeDef:
        """
        Creates a custom insight in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.create_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_insight)
        """
    def create_members(
        self, *, AccountDetails: List["AccountDetailsTypeDef"]
    ) -> CreateMembersResponseTypeDef:
        """
        Creates a member association in Security Hub between the specified accounts and
        the account used to make the request, which is the administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_members)
        """
    def decline_invitations(self, *, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        Declines invitations to become a member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.decline_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#decline_invitations)
        """
    def delete_action_target(self, *, ActionTargetArn: str) -> DeleteActionTargetResponseTypeDef:
        """
        Deletes a custom action target from Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.delete_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_action_target)
        """
    def delete_insight(self, *, InsightArn: str) -> DeleteInsightResponseTypeDef:
        """
        Deletes the insight specified by the `InsightArn` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.delete_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_insight)
        """
    def delete_invitations(self, *, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        Deletes invitations received by the Amazon Web Services account to become a
        member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.delete_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_invitations)
        """
    def delete_members(self, *, AccountIds: List[str]) -> DeleteMembersResponseTypeDef:
        """
        Deletes the specified member accounts from Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_members)
        """
    def describe_action_targets(
        self, *, ActionTargetArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeActionTargetsResponseTypeDef:
        """
        Returns a list of the custom action targets in Security Hub in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.describe_action_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_action_targets)
        """
    def describe_hub(self, *, HubArn: str = None) -> DescribeHubResponseTypeDef:
        """
        Returns details about the Hub resource in your account, including the `HubArn`
        and the time when you enabled Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.describe_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_hub)
        """
    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Returns information about the Organizations configuration for Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_organization_configuration)
        """
    def describe_products(
        self, *, NextToken: str = None, MaxResults: int = None, ProductArn: str = None
    ) -> DescribeProductsResponseTypeDef:
        """
        Returns information about product integrations in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.describe_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_products)
        """
    def describe_standards(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsResponseTypeDef:
        """
        Returns a list of the available standards in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.describe_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_standards)
        """
    def describe_standards_controls(
        self, *, StandardsSubscriptionArn: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsControlsResponseTypeDef:
        """
        Returns a list of security standards controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.describe_standards_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_standards_controls)
        """
    def disable_import_findings_for_product(self, *, ProductSubscriptionArn: str) -> Dict[str, Any]:
        """
        Disables the integration of the specified product with Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.disable_import_findings_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable_import_findings_for_product)
        """
    def disable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        Disables a Security Hub administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable_organization_admin_account)
        """
    def disable_security_hub(self) -> Dict[str, Any]:
        """
        Disables Security Hub in your account only in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.disable_security_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable_security_hub)
        """
    def disassociate_from_administrator_account(self) -> Dict[str, Any]:
        """
        Disassociates the current Security Hub member account from the associated
        administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate_from_administrator_account)
        """
    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate_from_master_account)
        """
    def disassociate_members(self, *, AccountIds: List[str]) -> Dict[str, Any]:
        """
        Disassociates the specified member accounts from the associated administrator
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.disassociate_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate_members)
        """
    def enable_import_findings_for_product(
        self, *, ProductArn: str
    ) -> EnableImportFindingsForProductResponseTypeDef:
        """
        Enables the integration of a partner product with Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.enable_import_findings_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable_import_findings_for_product)
        """
    def enable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        Designates the Security Hub administrator account for an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable_organization_admin_account)
        """
    def enable_security_hub(
        self, *, Tags: Dict[str, str] = None, EnableDefaultStandards: bool = None
    ) -> Dict[str, Any]:
        """
        Enables Security Hub for your account in the current Region or the Region you
        specify in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.enable_security_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable_security_hub)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#generate_presigned_url)
        """
    def get_administrator_account(self) -> GetAdministratorAccountResponseTypeDef:
        """
        Provides the details for the Security Hub administrator account for the current
        member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_administrator_account)
        """
    def get_enabled_standards(
        self,
        *,
        StandardsSubscriptionArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetEnabledStandardsResponseTypeDef:
        """
        Returns a list of the standards that are currently enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_enabled_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_enabled_standards)
        """
    def get_findings(
        self,
        *,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        SortCriteria: List["SortCriterionTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetFindingsResponseTypeDef:
        """
        Returns a list of findings that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_findings)
        """
    def get_insight_results(self, *, InsightArn: str) -> GetInsightResultsResponseTypeDef:
        """
        Lists the results of the Security Hub insight specified by the insight ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_insight_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_insight_results)
        """
    def get_insights(
        self, *, InsightArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> GetInsightsResponseTypeDef:
        """
        Lists and describes insights for the specified insight ARNs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_insights)
        """
    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        Returns the count of all Security Hub membership invitations that were sent to
        the current member account, not including the currently accepted invitation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_invitations_count)
        """
    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_master_account)
        """
    def get_members(self, *, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        Returns the details for the Security Hub member accounts for the specified
        account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_members)
        """
    def invite_members(self, *, AccountIds: List[str]) -> InviteMembersResponseTypeDef:
        """
        Invites other Amazon Web Services accounts to become member accounts for the
        Security Hub administrator account that the invitation is sent from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.invite_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#invite_members)
        """
    def list_enabled_products_for_import(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListEnabledProductsForImportResponseTypeDef:
        """
        Lists all findings-generating solutions (products) that you are subscribed to
        receive findings from in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.list_enabled_products_for_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_enabled_products_for_import)
        """
    def list_invitations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        Lists all Security Hub membership invitations that were sent to the current
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_invitations)
        """
    def list_members(
        self, *, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ListMembersResponseTypeDef:
        """
        Lists details about all member accounts for the current Security Hub
        administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_members)
        """
    def list_organization_admin_accounts(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        Lists the Security Hub administrator accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_organization_admin_accounts)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#untag_resource)
        """
    def update_action_target(
        self, *, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates the name and description of a custom action target in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.update_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_action_target)
        """
    def update_findings(
        self,
        *,
        Filters: "AwsSecurityFindingFiltersTypeDef",
        Note: "NoteUpdateTypeDef" = None,
        RecordState: RecordStateType = None
    ) -> Dict[str, Any]:
        """
        `UpdateFindings` is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.update_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_findings)
        """
    def update_insight(
        self,
        *,
        InsightArn: str,
        Name: str = None,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        GroupByAttribute: str = None
    ) -> Dict[str, Any]:
        """
        Updates the Security Hub insight identified by the specified insight ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.update_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_insight)
        """
    def update_organization_configuration(self, *, AutoEnable: bool) -> Dict[str, Any]:
        """
        Used to update the configuration related to Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_organization_configuration)
        """
    def update_security_hub_configuration(
        self, *, AutoEnableControls: bool = None
    ) -> Dict[str, Any]:
        """
        Updates configuration options for Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.update_security_hub_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_security_hub_configuration)
        """
    def update_standards_control(
        self,
        *,
        StandardsControlArn: str,
        ControlStatus: ControlStatusType = None,
        DisabledReason: str = None
    ) -> Dict[str, Any]:
        """
        Used to control whether an individual security standard control is enabled or
        disabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Client.update_standards_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_standards_control)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_enabled_standards"]
    ) -> GetEnabledStandardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getenabledstandardspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_findings"]) -> GetFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getfindingspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_insights"]) -> GetInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getinsightspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> ListEnabledProductsForImportPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listenabledproductsforimportpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listinvitationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listmemberspaginator)
        """
