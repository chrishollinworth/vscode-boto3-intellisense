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
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AutoEnableStandardsType,
    ControlFindingGeneratorType,
    ControlStatusType,
    RecordStateType,
    RuleStatusType,
    VerificationStateType,
)
from .paginator import (
    DescribeActionTargetsPaginator,
    DescribeProductsPaginator,
    DescribeStandardsControlsPaginator,
    DescribeStandardsPaginator,
    GetEnabledStandardsPaginator,
    GetFindingHistoryPaginator,
    GetFindingsPaginator,
    GetInsightsPaginator,
    ListConfigurationPoliciesPaginator,
    ListConfigurationPolicyAssociationsPaginator,
    ListEnabledProductsForImportPaginator,
    ListFindingAggregatorsPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListSecurityControlDefinitionsPaginator,
    ListStandardsControlAssociationsPaginator,
)
from .type_defs import (
    AccountDetailsTypeDef,
    AssociationFiltersTypeDef,
    AutomationRulesActionTypeDef,
    AutomationRulesFindingFiltersTypeDef,
    AwsSecurityFindingFiltersTypeDef,
    AwsSecurityFindingIdentifierTypeDef,
    AwsSecurityFindingTypeDef,
    BatchDeleteAutomationRulesResponseTypeDef,
    BatchDisableStandardsResponseTypeDef,
    BatchEnableStandardsResponseTypeDef,
    BatchGetAutomationRulesResponseTypeDef,
    BatchGetConfigurationPolicyAssociationsResponseTypeDef,
    BatchGetSecurityControlsResponseTypeDef,
    BatchGetStandardsControlAssociationsResponseTypeDef,
    BatchImportFindingsResponseTypeDef,
    BatchUpdateAutomationRulesResponseTypeDef,
    BatchUpdateFindingsResponseTypeDef,
    BatchUpdateStandardsControlAssociationsResponseTypeDef,
    ConfigurationPolicyAssociationTypeDef,
    CreateActionTargetResponseTypeDef,
    CreateAutomationRuleResponseTypeDef,
    CreateConfigurationPolicyResponseTypeDef,
    CreateFindingAggregatorResponseTypeDef,
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
    GetConfigurationPolicyAssociationResponseTypeDef,
    GetConfigurationPolicyResponseTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingAggregatorResponseTypeDef,
    GetFindingHistoryResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightResultsResponseTypeDef,
    GetInsightsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMembersResponseTypeDef,
    GetSecurityControlDefinitionResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListAutomationRulesResponseTypeDef,
    ListConfigurationPoliciesResponseTypeDef,
    ListConfigurationPolicyAssociationsResponseTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListFindingAggregatorsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListSecurityControlDefinitionsResponseTypeDef,
    ListStandardsControlAssociationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NoteUpdateTypeDef,
    OrganizationConfigurationTypeDef,
    ParameterConfigurationTypeDef,
    PolicyTypeDef,
    RelatedFindingTypeDef,
    SeverityUpdateTypeDef,
    SortCriterionTypeDef,
    StandardsControlAssociationIdTypeDef,
    StandardsControlAssociationUpdateTypeDef,
    StandardsSubscriptionRequestTypeDef,
    StartConfigurationPolicyAssociationResponseTypeDef,
    TargetTypeDef,
    UpdateAutomationRulesRequestItemTypeDef,
    UpdateConfigurationPolicyResponseTypeDef,
    UpdateFindingAggregatorResponseTypeDef,
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
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class SecurityHubClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.accept_administrator_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#accept_administrator_invitation)
        """

    def accept_invitation(self, *, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#accept_invitation)
        """

    def batch_delete_automation_rules(
        self, *, AutomationRulesArns: List[str]
    ) -> BatchDeleteAutomationRulesResponseTypeDef:
        """
        Deletes one or more automation rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_delete_automation_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_delete_automation_rules)
        """

    def batch_disable_standards(
        self, *, StandardsSubscriptionArns: List[str]
    ) -> BatchDisableStandardsResponseTypeDef:
        """
        Disables the standards specified by the provided `StandardsSubscriptionArns`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_disable_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_disable_standards)
        """

    def batch_enable_standards(
        self, *, StandardsSubscriptionRequests: List["StandardsSubscriptionRequestTypeDef"]
    ) -> BatchEnableStandardsResponseTypeDef:
        """
        Enables the standards specified by the provided `StandardsArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_enable_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_enable_standards)
        """

    def batch_get_automation_rules(
        self, *, AutomationRulesArns: List[str]
    ) -> BatchGetAutomationRulesResponseTypeDef:
        """
        Retrieves a list of details for automation rules based on rule Amazon Resource
        Names (ARNs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_get_automation_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_get_automation_rules)
        """

    def batch_get_configuration_policy_associations(
        self,
        *,
        ConfigurationPolicyAssociationIdentifiers: List["ConfigurationPolicyAssociationTypeDef"]
    ) -> BatchGetConfigurationPolicyAssociationsResponseTypeDef:
        """
        Returns associations between an Security Hub configuration and a batch of target
        accounts, organizational units, or the root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_get_configuration_policy_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_get_configuration_policy_associations)
        """

    def batch_get_security_controls(
        self, *, SecurityControlIds: List[str]
    ) -> BatchGetSecurityControlsResponseTypeDef:
        """
        Provides details about a batch of security controls for the current Amazon Web
        Services account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_get_security_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_get_security_controls)
        """

    def batch_get_standards_control_associations(
        self, *, StandardsControlAssociationIds: List["StandardsControlAssociationIdTypeDef"]
    ) -> BatchGetStandardsControlAssociationsResponseTypeDef:
        """
        For a batch of security controls and standards, identifies whether each control
        is currently enabled or disabled in a standard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_get_standards_control_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_get_standards_control_associations)
        """

    def batch_import_findings(
        self, *, Findings: List["AwsSecurityFindingTypeDef"]
    ) -> BatchImportFindingsResponseTypeDef:
        """
        Imports security findings generated by a finding provider into Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_import_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_import_findings)
        """

    def batch_update_automation_rules(
        self, *, UpdateAutomationRulesRequestItems: List["UpdateAutomationRulesRequestItemTypeDef"]
    ) -> BatchUpdateAutomationRulesResponseTypeDef:
        """
        Updates one or more automation rules based on rule Amazon Resource Names (ARNs)
        and input parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_update_automation_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_update_automation_rules)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_update_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_update_findings)
        """

    def batch_update_standards_control_associations(
        self,
        *,
        StandardsControlAssociationUpdates: List["StandardsControlAssociationUpdateTypeDef"]
    ) -> BatchUpdateStandardsControlAssociationsResponseTypeDef:
        """
        For a batch of security controls and standards, this operation updates the
        enablement status of a control in a standard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.batch_update_standards_control_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch_update_standards_control_associations)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#close)
        """

    def create_action_target(
        self, *, Name: str, Description: str, Id: str
    ) -> CreateActionTargetResponseTypeDef:
        """
        Creates a custom action target in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.create_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_action_target)
        """

    def create_automation_rule(
        self,
        *,
        RuleOrder: int,
        RuleName: str,
        Description: str,
        Criteria: "AutomationRulesFindingFiltersTypeDef",
        Actions: List["AutomationRulesActionTypeDef"],
        Tags: Dict[str, str] = None,
        RuleStatus: RuleStatusType = None,
        IsTerminal: bool = None
    ) -> CreateAutomationRuleResponseTypeDef:
        """
        Creates an automation rule based on input parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.create_automation_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_automation_rule)
        """

    def create_configuration_policy(
        self,
        *,
        Name: str,
        ConfigurationPolicy: "PolicyTypeDef",
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateConfigurationPolicyResponseTypeDef:
        """
        Creates a configuration policy with the defined configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.create_configuration_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_configuration_policy)
        """

    def create_finding_aggregator(
        self, *, RegionLinkingMode: str, Regions: List[str] = None
    ) -> CreateFindingAggregatorResponseTypeDef:
        """
        Used to enable finding aggregation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.create_finding_aggregator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_finding_aggregator)
        """

    def create_insight(
        self, *, Name: str, Filters: "AwsSecurityFindingFiltersTypeDef", GroupByAttribute: str
    ) -> CreateInsightResponseTypeDef:
        """
        Creates a custom insight in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.create_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_insight)
        """

    def create_members(
        self, *, AccountDetails: List["AccountDetailsTypeDef"]
    ) -> CreateMembersResponseTypeDef:
        """
        Creates a member association in Security Hub between the specified accounts and
        the account used to make the request, which is the administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create_members)
        """

    def decline_invitations(self, *, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        Declines invitations to become a member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.decline_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#decline_invitations)
        """

    def delete_action_target(self, *, ActionTargetArn: str) -> DeleteActionTargetResponseTypeDef:
        """
        Deletes a custom action target from Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.delete_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_action_target)
        """

    def delete_configuration_policy(self, *, Identifier: str) -> Dict[str, Any]:
        """
        Deletes a configuration policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.delete_configuration_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_configuration_policy)
        """

    def delete_finding_aggregator(self, *, FindingAggregatorArn: str) -> Dict[str, Any]:
        """
        Deletes a finding aggregator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.delete_finding_aggregator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_finding_aggregator)
        """

    def delete_insight(self, *, InsightArn: str) -> DeleteInsightResponseTypeDef:
        """
        Deletes the insight specified by the `InsightArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.delete_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_insight)
        """

    def delete_invitations(self, *, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        Deletes invitations received by the Amazon Web Services account to become a
        member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.delete_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_invitations)
        """

    def delete_members(self, *, AccountIds: List[str]) -> DeleteMembersResponseTypeDef:
        """
        Deletes the specified member accounts from Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete_members)
        """

    def describe_action_targets(
        self, *, ActionTargetArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeActionTargetsResponseTypeDef:
        """
        Returns a list of the custom action targets in Security Hub in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.describe_action_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_action_targets)
        """

    def describe_hub(self, *, HubArn: str = None) -> DescribeHubResponseTypeDef:
        """
        Returns details about the Hub resource in your account, including the `HubArn`
        and the time when you enabled Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.describe_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_hub)
        """

    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Returns information about the way your organization is configured in Security
        Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_organization_configuration)
        """

    def describe_products(
        self, *, NextToken: str = None, MaxResults: int = None, ProductArn: str = None
    ) -> DescribeProductsResponseTypeDef:
        """
        Returns information about product integrations in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.describe_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_products)
        """

    def describe_standards(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsResponseTypeDef:
        """
        Returns a list of the available standards in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.describe_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_standards)
        """

    def describe_standards_controls(
        self, *, StandardsSubscriptionArn: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsControlsResponseTypeDef:
        """
        Returns a list of security standards controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.describe_standards_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe_standards_controls)
        """

    def disable_import_findings_for_product(self, *, ProductSubscriptionArn: str) -> Dict[str, Any]:
        """
        Disables the integration of the specified product with Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.disable_import_findings_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable_import_findings_for_product)
        """

    def disable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        Disables a Security Hub administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable_organization_admin_account)
        """

    def disable_security_hub(self) -> Dict[str, Any]:
        """
        Disables Security Hub in your account only in the current Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.disable_security_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable_security_hub)
        """

    def disassociate_from_administrator_account(self) -> Dict[str, Any]:
        """
        Disassociates the current Security Hub member account from the associated
        administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate_from_administrator_account)
        """

    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate_from_master_account)
        """

    def disassociate_members(self, *, AccountIds: List[str]) -> Dict[str, Any]:
        """
        Disassociates the specified member accounts from the associated administrator
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.disassociate_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate_members)
        """

    def enable_import_findings_for_product(
        self, *, ProductArn: str
    ) -> EnableImportFindingsForProductResponseTypeDef:
        """
        Enables the integration of a partner product with Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.enable_import_findings_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable_import_findings_for_product)
        """

    def enable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        Designates the Security Hub administrator account for an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable_organization_admin_account)
        """

    def enable_security_hub(
        self,
        *,
        Tags: Dict[str, str] = None,
        EnableDefaultStandards: bool = None,
        ControlFindingGenerator: ControlFindingGeneratorType = None
    ) -> Dict[str, Any]:
        """
        Enables Security Hub for your account in the current Region or the Region you
        specify in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.enable_security_hub)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#generate_presigned_url)
        """

    def get_administrator_account(self) -> GetAdministratorAccountResponseTypeDef:
        """
        Provides the details for the Security Hub administrator account for the current
        member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_administrator_account)
        """

    def get_configuration_policy(self, *, Identifier: str) -> GetConfigurationPolicyResponseTypeDef:
        """
        Provides information about a configuration policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_configuration_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_configuration_policy)
        """

    def get_configuration_policy_association(
        self, *, Target: "TargetTypeDef"
    ) -> GetConfigurationPolicyAssociationResponseTypeDef:
        """
        Returns the association between a configuration and a target account,
        organizational unit, or the root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_configuration_policy_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_configuration_policy_association)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_enabled_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_enabled_standards)
        """

    def get_finding_aggregator(
        self, *, FindingAggregatorArn: str
    ) -> GetFindingAggregatorResponseTypeDef:
        """
        Returns the current finding aggregation configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_finding_aggregator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_finding_aggregator)
        """

    def get_finding_history(
        self,
        *,
        FindingIdentifier: "AwsSecurityFindingIdentifierTypeDef",
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetFindingHistoryResponseTypeDef:
        """
        Returns history for a Security Hub finding in the last 90 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_finding_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_finding_history)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_findings)
        """

    def get_insight_results(self, *, InsightArn: str) -> GetInsightResultsResponseTypeDef:
        """
        Lists the results of the Security Hub insight specified by the insight ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_insight_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_insight_results)
        """

    def get_insights(
        self, *, InsightArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> GetInsightsResponseTypeDef:
        """
        Lists and describes insights for the specified insight ARNs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_insights)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        Returns the count of all Security Hub membership invitations that were sent to
        the current member account, not including the currently accepted invitation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_invitations_count)
        """

    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_master_account)
        """

    def get_members(self, *, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        Returns the details for the Security Hub member accounts for the specified
        account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_members)
        """

    def get_security_control_definition(
        self, *, SecurityControlId: str
    ) -> GetSecurityControlDefinitionResponseTypeDef:
        """
        Retrieves the definition of a security control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.get_security_control_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get_security_control_definition)
        """

    def invite_members(self, *, AccountIds: List[str]) -> InviteMembersResponseTypeDef:
        """
        Invites other Amazon Web Services accounts to become member accounts for the
        Security Hub administrator account that the invitation is sent from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.invite_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#invite_members)
        """

    def list_automation_rules(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAutomationRulesResponseTypeDef:
        """
        A list of automation rules and their metadata for the calling account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_automation_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_automation_rules)
        """

    def list_configuration_policies(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListConfigurationPoliciesResponseTypeDef:
        """
        Lists the configuration policies that the Security Hub delegated administrator
        has created for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_configuration_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_configuration_policies)
        """

    def list_configuration_policy_associations(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: "AssociationFiltersTypeDef" = None
    ) -> ListConfigurationPolicyAssociationsResponseTypeDef:
        """
        Provides information about the associations for your configuration policies and
        self-managed behavior.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_configuration_policy_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_configuration_policy_associations)
        """

    def list_enabled_products_for_import(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListEnabledProductsForImportResponseTypeDef:
        """
        Lists all findings-generating solutions (products) that you are subscribed to
        receive findings from in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_enabled_products_for_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_enabled_products_for_import)
        """

    def list_finding_aggregators(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListFindingAggregatorsResponseTypeDef:
        """
        If finding aggregation is enabled, then `ListFindingAggregators` returns the ARN
        of the finding aggregator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_finding_aggregators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_finding_aggregators)
        """

    def list_invitations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        Lists all Security Hub membership invitations that were sent to the current
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_invitations)
        """

    def list_members(
        self, *, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ListMembersResponseTypeDef:
        """
        Lists details about all member accounts for the current Security Hub
        administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_members)
        """

    def list_organization_admin_accounts(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        Lists the Security Hub administrator accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_organization_admin_accounts)
        """

    def list_security_control_definitions(
        self, *, StandardsArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListSecurityControlDefinitionsResponseTypeDef:
        """
        Lists all of the security controls that apply to a specified standard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_security_control_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_security_control_definitions)
        """

    def list_standards_control_associations(
        self, *, SecurityControlId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListStandardsControlAssociationsResponseTypeDef:
        """
        Specifies whether a control is currently enabled or disabled in each enabled
        standard in the calling account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_standards_control_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_standards_control_associations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list_tags_for_resource)
        """

    def start_configuration_policy_association(
        self, *, ConfigurationPolicyIdentifier: str, Target: "TargetTypeDef"
    ) -> StartConfigurationPolicyAssociationResponseTypeDef:
        """
        Associates a target account, organizational unit, or the root with a specified
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.start_configuration_policy_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#start_configuration_policy_association)
        """

    def start_configuration_policy_disassociation(
        self, *, ConfigurationPolicyIdentifier: str, Target: "TargetTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Disassociates a target account, organizational unit, or the root from a
        specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.start_configuration_policy_disassociation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#start_configuration_policy_disassociation)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#untag_resource)
        """

    def update_action_target(
        self, *, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates the name and description of a custom action target in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_action_target)
        """

    def update_configuration_policy(
        self,
        *,
        Identifier: str,
        Name: str = None,
        Description: str = None,
        UpdatedReason: str = None,
        ConfigurationPolicy: "PolicyTypeDef" = None
    ) -> UpdateConfigurationPolicyResponseTypeDef:
        """
        Updates a configuration policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_configuration_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_configuration_policy)
        """

    def update_finding_aggregator(
        self, *, FindingAggregatorArn: str, RegionLinkingMode: str, Regions: List[str] = None
    ) -> UpdateFindingAggregatorResponseTypeDef:
        """
        Updates the finding aggregation configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_finding_aggregator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_finding_aggregator)
        """

    def update_findings(
        self,
        *,
        Filters: "AwsSecurityFindingFiltersTypeDef",
        Note: "NoteUpdateTypeDef" = None,
        RecordState: RecordStateType = None
    ) -> Dict[str, Any]:
        """
        `UpdateFindings` is a deprecated operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_findings)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_insight)
        """

    def update_organization_configuration(
        self,
        *,
        AutoEnable: bool,
        AutoEnableStandards: AutoEnableStandardsType = None,
        OrganizationConfiguration: "OrganizationConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration of your organization in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_organization_configuration)
        """

    def update_security_control(
        self,
        *,
        SecurityControlId: str,
        Parameters: Dict[str, "ParameterConfigurationTypeDef"],
        LastUpdateReason: str = None
    ) -> Dict[str, Any]:
        """
        Updates the properties of a security control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_security_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_security_control)
        """

    def update_security_hub_configuration(
        self,
        *,
        AutoEnableControls: bool = None,
        ControlFindingGenerator: ControlFindingGeneratorType = None
    ) -> Dict[str, Any]:
        """
        Updates configuration options for Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_security_hub_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Client.update_standards_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update_standards_control)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_action_targets"]
    ) -> DescribeActionTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.DescribeActionTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#describeactiontargetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_products"]
    ) -> DescribeProductsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.DescribeProducts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#describeproductspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_standards"]
    ) -> DescribeStandardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.DescribeStandards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#describestandardspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_standards_controls"]
    ) -> DescribeStandardsControlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.DescribeStandardsControls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#describestandardscontrolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_enabled_standards"]
    ) -> GetEnabledStandardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getenabledstandardspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_finding_history"]
    ) -> GetFindingHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.GetFindingHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getfindinghistorypaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_findings"]) -> GetFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getfindingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_insights"]) -> GetInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getinsightspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_policies"]
    ) -> ListConfigurationPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListConfigurationPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listconfigurationpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_policy_associations"]
    ) -> ListConfigurationPolicyAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListConfigurationPolicyAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listconfigurationpolicyassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> ListEnabledProductsForImportPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listenabledproductsforimportpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_finding_aggregators"]
    ) -> ListFindingAggregatorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListFindingAggregators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listfindingaggregatorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listinvitationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listmemberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListOrganizationAdminAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listorganizationadminaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_control_definitions"]
    ) -> ListSecurityControlDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListSecurityControlDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listsecuritycontroldefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_standards_control_associations"]
    ) -> ListStandardsControlAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/securityhub.html#SecurityHub.Paginator.ListStandardsControlAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#liststandardscontrolassociationspaginator)
        """
