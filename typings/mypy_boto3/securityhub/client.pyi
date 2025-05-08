"""
Type annotations for securityhub service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_securityhub.client import SecurityHubClient

    session = Session()
    client: SecurityHubClient = session.client("securityhub")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    AcceptAdministratorInvitationRequestTypeDef,
    AcceptInvitationRequestTypeDef,
    BatchDeleteAutomationRulesRequestTypeDef,
    BatchDeleteAutomationRulesResponseTypeDef,
    BatchDisableStandardsRequestTypeDef,
    BatchDisableStandardsResponseTypeDef,
    BatchEnableStandardsRequestTypeDef,
    BatchEnableStandardsResponseTypeDef,
    BatchGetAutomationRulesRequestTypeDef,
    BatchGetAutomationRulesResponseTypeDef,
    BatchGetConfigurationPolicyAssociationsRequestTypeDef,
    BatchGetConfigurationPolicyAssociationsResponseTypeDef,
    BatchGetSecurityControlsRequestTypeDef,
    BatchGetSecurityControlsResponseTypeDef,
    BatchGetStandardsControlAssociationsRequestTypeDef,
    BatchGetStandardsControlAssociationsResponseTypeDef,
    BatchImportFindingsRequestTypeDef,
    BatchImportFindingsResponseTypeDef,
    BatchUpdateAutomationRulesRequestTypeDef,
    BatchUpdateAutomationRulesResponseTypeDef,
    BatchUpdateFindingsRequestTypeDef,
    BatchUpdateFindingsResponseTypeDef,
    BatchUpdateStandardsControlAssociationsRequestTypeDef,
    BatchUpdateStandardsControlAssociationsResponseTypeDef,
    CreateActionTargetRequestTypeDef,
    CreateActionTargetResponseTypeDef,
    CreateAutomationRuleRequestTypeDef,
    CreateAutomationRuleResponseTypeDef,
    CreateConfigurationPolicyRequestTypeDef,
    CreateConfigurationPolicyResponseTypeDef,
    CreateFindingAggregatorRequestTypeDef,
    CreateFindingAggregatorResponseTypeDef,
    CreateInsightRequestTypeDef,
    CreateInsightResponseTypeDef,
    CreateMembersRequestTypeDef,
    CreateMembersResponseTypeDef,
    DeclineInvitationsRequestTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteActionTargetRequestTypeDef,
    DeleteActionTargetResponseTypeDef,
    DeleteConfigurationPolicyRequestTypeDef,
    DeleteFindingAggregatorRequestTypeDef,
    DeleteInsightRequestTypeDef,
    DeleteInsightResponseTypeDef,
    DeleteInvitationsRequestTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersRequestTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeActionTargetsRequestTypeDef,
    DescribeActionTargetsResponseTypeDef,
    DescribeHubRequestTypeDef,
    DescribeHubResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DescribeProductsRequestTypeDef,
    DescribeProductsResponseTypeDef,
    DescribeStandardsControlsRequestTypeDef,
    DescribeStandardsControlsResponseTypeDef,
    DescribeStandardsRequestTypeDef,
    DescribeStandardsResponseTypeDef,
    DisableImportFindingsForProductRequestTypeDef,
    DisableOrganizationAdminAccountRequestTypeDef,
    DisassociateMembersRequestTypeDef,
    EnableImportFindingsForProductRequestTypeDef,
    EnableImportFindingsForProductResponseTypeDef,
    EnableOrganizationAdminAccountRequestTypeDef,
    EnableSecurityHubRequestTypeDef,
    GetAdministratorAccountResponseTypeDef,
    GetConfigurationPolicyAssociationRequestTypeDef,
    GetConfigurationPolicyAssociationResponseTypeDef,
    GetConfigurationPolicyRequestTypeDef,
    GetConfigurationPolicyResponseTypeDef,
    GetEnabledStandardsRequestTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingAggregatorRequestTypeDef,
    GetFindingAggregatorResponseTypeDef,
    GetFindingHistoryRequestTypeDef,
    GetFindingHistoryResponseTypeDef,
    GetFindingsRequestTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightResultsRequestTypeDef,
    GetInsightResultsResponseTypeDef,
    GetInsightsRequestTypeDef,
    GetInsightsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMembersRequestTypeDef,
    GetMembersResponseTypeDef,
    GetSecurityControlDefinitionRequestTypeDef,
    GetSecurityControlDefinitionResponseTypeDef,
    InviteMembersRequestTypeDef,
    InviteMembersResponseTypeDef,
    ListAutomationRulesRequestTypeDef,
    ListAutomationRulesResponseTypeDef,
    ListConfigurationPoliciesRequestTypeDef,
    ListConfigurationPoliciesResponseTypeDef,
    ListConfigurationPolicyAssociationsRequestTypeDef,
    ListConfigurationPolicyAssociationsResponseTypeDef,
    ListEnabledProductsForImportRequestTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListFindingAggregatorsRequestTypeDef,
    ListFindingAggregatorsResponseTypeDef,
    ListInvitationsRequestTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersRequestTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsRequestTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListSecurityControlDefinitionsRequestTypeDef,
    ListSecurityControlDefinitionsResponseTypeDef,
    ListStandardsControlAssociationsRequestTypeDef,
    ListStandardsControlAssociationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartConfigurationPolicyAssociationRequestTypeDef,
    StartConfigurationPolicyAssociationResponseTypeDef,
    StartConfigurationPolicyDisassociationRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateActionTargetRequestTypeDef,
    UpdateConfigurationPolicyRequestTypeDef,
    UpdateConfigurationPolicyResponseTypeDef,
    UpdateFindingAggregatorRequestTypeDef,
    UpdateFindingAggregatorResponseTypeDef,
    UpdateFindingsRequestTypeDef,
    UpdateInsightRequestTypeDef,
    UpdateOrganizationConfigurationRequestTypeDef,
    UpdateSecurityControlRequestTypeDef,
    UpdateSecurityHubConfigurationRequestTypeDef,
    UpdateStandardsControlRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SecurityHubClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SecurityHubClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#generate_presigned_url)
        """

    def accept_administrator_invitation(
        self, **kwargs: Unpack[AcceptAdministratorInvitationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        We recommend using Organizations instead of Security Hub invitations to manage
        your member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/accept_administrator_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#accept_administrator_invitation)
        """

    def accept_invitation(self, **kwargs: Unpack[AcceptInvitationRequestTypeDef]) -> Dict[str, Any]:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/accept_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#accept_invitation)
        """

    def batch_delete_automation_rules(
        self, **kwargs: Unpack[BatchDeleteAutomationRulesRequestTypeDef]
    ) -> BatchDeleteAutomationRulesResponseTypeDef:
        """
        Deletes one or more automation rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_delete_automation_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_delete_automation_rules)
        """

    def batch_disable_standards(
        self, **kwargs: Unpack[BatchDisableStandardsRequestTypeDef]
    ) -> BatchDisableStandardsResponseTypeDef:
        """
        Disables the standards specified by the provided
        <code>StandardsSubscriptionArns</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_disable_standards.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_disable_standards)
        """

    def batch_enable_standards(
        self, **kwargs: Unpack[BatchEnableStandardsRequestTypeDef]
    ) -> BatchEnableStandardsResponseTypeDef:
        """
        Enables the standards specified by the provided <code>StandardsArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_enable_standards.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_enable_standards)
        """

    def batch_get_automation_rules(
        self, **kwargs: Unpack[BatchGetAutomationRulesRequestTypeDef]
    ) -> BatchGetAutomationRulesResponseTypeDef:
        """
        Retrieves a list of details for automation rules based on rule Amazon Resource
        Names (ARNs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_get_automation_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_get_automation_rules)
        """

    def batch_get_configuration_policy_associations(
        self, **kwargs: Unpack[BatchGetConfigurationPolicyAssociationsRequestTypeDef]
    ) -> BatchGetConfigurationPolicyAssociationsResponseTypeDef:
        """
        Returns associations between an Security Hub configuration and a batch of
        target accounts, organizational units, or the root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_get_configuration_policy_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_get_configuration_policy_associations)
        """

    def batch_get_security_controls(
        self, **kwargs: Unpack[BatchGetSecurityControlsRequestTypeDef]
    ) -> BatchGetSecurityControlsResponseTypeDef:
        """
        Provides details about a batch of security controls for the current Amazon Web
        Services account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_get_security_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_get_security_controls)
        """

    def batch_get_standards_control_associations(
        self, **kwargs: Unpack[BatchGetStandardsControlAssociationsRequestTypeDef]
    ) -> BatchGetStandardsControlAssociationsResponseTypeDef:
        """
        For a batch of security controls and standards, identifies whether each control
        is currently enabled or disabled in a standard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_get_standards_control_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_get_standards_control_associations)
        """

    def batch_import_findings(
        self, **kwargs: Unpack[BatchImportFindingsRequestTypeDef]
    ) -> BatchImportFindingsResponseTypeDef:
        """
        Imports security findings generated by a finding provider into Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_import_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_import_findings)
        """

    def batch_update_automation_rules(
        self, **kwargs: Unpack[BatchUpdateAutomationRulesRequestTypeDef]
    ) -> BatchUpdateAutomationRulesResponseTypeDef:
        """
        Updates one or more automation rules based on rule Amazon Resource Names (ARNs)
        and input parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_update_automation_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_update_automation_rules)
        """

    def batch_update_findings(
        self, **kwargs: Unpack[BatchUpdateFindingsRequestTypeDef]
    ) -> BatchUpdateFindingsResponseTypeDef:
        """
        Used by Security Hub customers to update information about their investigation
        into a finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_update_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_update_findings)
        """

    def batch_update_standards_control_associations(
        self, **kwargs: Unpack[BatchUpdateStandardsControlAssociationsRequestTypeDef]
    ) -> BatchUpdateStandardsControlAssociationsResponseTypeDef:
        """
        For a batch of security controls and standards, this operation updates the
        enablement status of a control in a standard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/batch_update_standards_control_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#batch_update_standards_control_associations)
        """

    def create_action_target(
        self, **kwargs: Unpack[CreateActionTargetRequestTypeDef]
    ) -> CreateActionTargetResponseTypeDef:
        """
        Creates a custom action target in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/create_action_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#create_action_target)
        """

    def create_automation_rule(
        self, **kwargs: Unpack[CreateAutomationRuleRequestTypeDef]
    ) -> CreateAutomationRuleResponseTypeDef:
        """
        Creates an automation rule based on input parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/create_automation_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#create_automation_rule)
        """

    def create_configuration_policy(
        self, **kwargs: Unpack[CreateConfigurationPolicyRequestTypeDef]
    ) -> CreateConfigurationPolicyResponseTypeDef:
        """
        Creates a configuration policy with the defined configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/create_configuration_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#create_configuration_policy)
        """

    def create_finding_aggregator(
        self, **kwargs: Unpack[CreateFindingAggregatorRequestTypeDef]
    ) -> CreateFindingAggregatorResponseTypeDef:
        """
        The <i>aggregation Region</i> is now called the <i>home Region</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/create_finding_aggregator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#create_finding_aggregator)
        """

    def create_insight(
        self, **kwargs: Unpack[CreateInsightRequestTypeDef]
    ) -> CreateInsightResponseTypeDef:
        """
        Creates a custom insight in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/create_insight.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#create_insight)
        """

    def create_members(
        self, **kwargs: Unpack[CreateMembersRequestTypeDef]
    ) -> CreateMembersResponseTypeDef:
        """
        Creates a member association in Security Hub between the specified accounts and
        the account used to make the request, which is the administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/create_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#create_members)
        """

    def decline_invitations(
        self, **kwargs: Unpack[DeclineInvitationsRequestTypeDef]
    ) -> DeclineInvitationsResponseTypeDef:
        """
        We recommend using Organizations instead of Security Hub invitations to manage
        your member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/decline_invitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#decline_invitations)
        """

    def delete_action_target(
        self, **kwargs: Unpack[DeleteActionTargetRequestTypeDef]
    ) -> DeleteActionTargetResponseTypeDef:
        """
        Deletes a custom action target from Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/delete_action_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#delete_action_target)
        """

    def delete_configuration_policy(
        self, **kwargs: Unpack[DeleteConfigurationPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a configuration policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/delete_configuration_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#delete_configuration_policy)
        """

    def delete_finding_aggregator(
        self, **kwargs: Unpack[DeleteFindingAggregatorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The <i>aggregation Region</i> is now called the <i>home Region</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/delete_finding_aggregator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#delete_finding_aggregator)
        """

    def delete_insight(
        self, **kwargs: Unpack[DeleteInsightRequestTypeDef]
    ) -> DeleteInsightResponseTypeDef:
        """
        Deletes the insight specified by the <code>InsightArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/delete_insight.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#delete_insight)
        """

    def delete_invitations(
        self, **kwargs: Unpack[DeleteInvitationsRequestTypeDef]
    ) -> DeleteInvitationsResponseTypeDef:
        """
        We recommend using Organizations instead of Security Hub invitations to manage
        your member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/delete_invitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#delete_invitations)
        """

    def delete_members(
        self, **kwargs: Unpack[DeleteMembersRequestTypeDef]
    ) -> DeleteMembersResponseTypeDef:
        """
        Deletes the specified member accounts from Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/delete_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#delete_members)
        """

    def describe_action_targets(
        self, **kwargs: Unpack[DescribeActionTargetsRequestTypeDef]
    ) -> DescribeActionTargetsResponseTypeDef:
        """
        Returns a list of the custom action targets in Security Hub in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/describe_action_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#describe_action_targets)
        """

    def describe_hub(
        self, **kwargs: Unpack[DescribeHubRequestTypeDef]
    ) -> DescribeHubResponseTypeDef:
        """
        Returns details about the Hub resource in your account, including the
        <code>HubArn</code> and the time when you enabled Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/describe_hub.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#describe_hub)
        """

    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Returns information about the way your organization is configured in Security
        Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/describe_organization_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#describe_organization_configuration)
        """

    def describe_products(
        self, **kwargs: Unpack[DescribeProductsRequestTypeDef]
    ) -> DescribeProductsResponseTypeDef:
        """
        Returns information about product integrations in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/describe_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#describe_products)
        """

    def describe_standards(
        self, **kwargs: Unpack[DescribeStandardsRequestTypeDef]
    ) -> DescribeStandardsResponseTypeDef:
        """
        Returns a list of the available standards in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/describe_standards.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#describe_standards)
        """

    def describe_standards_controls(
        self, **kwargs: Unpack[DescribeStandardsControlsRequestTypeDef]
    ) -> DescribeStandardsControlsResponseTypeDef:
        """
        Returns a list of security standards controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/describe_standards_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#describe_standards_controls)
        """

    def disable_import_findings_for_product(
        self, **kwargs: Unpack[DisableImportFindingsForProductRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disables the integration of the specified product with Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/disable_import_findings_for_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#disable_import_findings_for_product)
        """

    def disable_organization_admin_account(
        self, **kwargs: Unpack[DisableOrganizationAdminAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disables a Security Hub administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/disable_organization_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#disable_organization_admin_account)
        """

    def disable_security_hub(self) -> Dict[str, Any]:
        """
        Disables Security Hub in your account only in the current Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/disable_security_hub.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#disable_security_hub)
        """

    def disassociate_from_administrator_account(self) -> Dict[str, Any]:
        """
        Disassociates the current Security Hub member account from the associated
        administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/disassociate_from_administrator_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#disassociate_from_administrator_account)
        """

    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/disassociate_from_master_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#disassociate_from_master_account)
        """

    def disassociate_members(
        self, **kwargs: Unpack[DisassociateMembersRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified member accounts from the associated administrator
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/disassociate_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#disassociate_members)
        """

    def enable_import_findings_for_product(
        self, **kwargs: Unpack[EnableImportFindingsForProductRequestTypeDef]
    ) -> EnableImportFindingsForProductResponseTypeDef:
        """
        Enables the integration of a partner product with Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/enable_import_findings_for_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#enable_import_findings_for_product)
        """

    def enable_organization_admin_account(
        self, **kwargs: Unpack[EnableOrganizationAdminAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Designates the Security Hub administrator account for an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/enable_organization_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#enable_organization_admin_account)
        """

    def enable_security_hub(
        self, **kwargs: Unpack[EnableSecurityHubRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables Security Hub for your account in the current Region or the Region you
        specify in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/enable_security_hub.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#enable_security_hub)
        """

    def get_administrator_account(self) -> GetAdministratorAccountResponseTypeDef:
        """
        Provides the details for the Security Hub administrator account for the current
        member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_administrator_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_administrator_account)
        """

    def get_configuration_policy(
        self, **kwargs: Unpack[GetConfigurationPolicyRequestTypeDef]
    ) -> GetConfigurationPolicyResponseTypeDef:
        """
        Provides information about a configuration policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_configuration_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_configuration_policy)
        """

    def get_configuration_policy_association(
        self, **kwargs: Unpack[GetConfigurationPolicyAssociationRequestTypeDef]
    ) -> GetConfigurationPolicyAssociationResponseTypeDef:
        """
        Returns the association between a configuration and a target account,
        organizational unit, or the root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_configuration_policy_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_configuration_policy_association)
        """

    def get_enabled_standards(
        self, **kwargs: Unpack[GetEnabledStandardsRequestTypeDef]
    ) -> GetEnabledStandardsResponseTypeDef:
        """
        Returns a list of the standards that are currently enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_enabled_standards.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_enabled_standards)
        """

    def get_finding_aggregator(
        self, **kwargs: Unpack[GetFindingAggregatorRequestTypeDef]
    ) -> GetFindingAggregatorResponseTypeDef:
        """
        The <i>aggregation Region</i> is now called the <i>home Region</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_finding_aggregator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_finding_aggregator)
        """

    def get_finding_history(
        self, **kwargs: Unpack[GetFindingHistoryRequestTypeDef]
    ) -> GetFindingHistoryResponseTypeDef:
        """
        Returns history for a Security Hub finding in the last 90 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_finding_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_finding_history)
        """

    def get_findings(
        self, **kwargs: Unpack[GetFindingsRequestTypeDef]
    ) -> GetFindingsResponseTypeDef:
        """
        Returns a list of findings that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_findings)
        """

    def get_insight_results(
        self, **kwargs: Unpack[GetInsightResultsRequestTypeDef]
    ) -> GetInsightResultsResponseTypeDef:
        """
        Lists the results of the Security Hub insight specified by the insight ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_insight_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_insight_results)
        """

    def get_insights(
        self, **kwargs: Unpack[GetInsightsRequestTypeDef]
    ) -> GetInsightsResponseTypeDef:
        """
        Lists and describes insights for the specified insight ARNs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_insights)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        We recommend using Organizations instead of Security Hub invitations to manage
        your member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_invitations_count.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_invitations_count)
        """

    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        This method is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_master_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_master_account)
        """

    def get_members(self, **kwargs: Unpack[GetMembersRequestTypeDef]) -> GetMembersResponseTypeDef:
        """
        Returns the details for the Security Hub member accounts for the specified
        account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_members)
        """

    def get_security_control_definition(
        self, **kwargs: Unpack[GetSecurityControlDefinitionRequestTypeDef]
    ) -> GetSecurityControlDefinitionResponseTypeDef:
        """
        Retrieves the definition of a security control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_security_control_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_security_control_definition)
        """

    def invite_members(
        self, **kwargs: Unpack[InviteMembersRequestTypeDef]
    ) -> InviteMembersResponseTypeDef:
        """
        We recommend using Organizations instead of Security Hub invitations to manage
        your member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/invite_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#invite_members)
        """

    def list_automation_rules(
        self, **kwargs: Unpack[ListAutomationRulesRequestTypeDef]
    ) -> ListAutomationRulesResponseTypeDef:
        """
        A list of automation rules and their metadata for the calling account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_automation_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_automation_rules)
        """

    def list_configuration_policies(
        self, **kwargs: Unpack[ListConfigurationPoliciesRequestTypeDef]
    ) -> ListConfigurationPoliciesResponseTypeDef:
        """
        Lists the configuration policies that the Security Hub delegated administrator
        has created for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_configuration_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_configuration_policies)
        """

    def list_configuration_policy_associations(
        self, **kwargs: Unpack[ListConfigurationPolicyAssociationsRequestTypeDef]
    ) -> ListConfigurationPolicyAssociationsResponseTypeDef:
        """
        Provides information about the associations for your configuration policies and
        self-managed behavior.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_configuration_policy_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_configuration_policy_associations)
        """

    def list_enabled_products_for_import(
        self, **kwargs: Unpack[ListEnabledProductsForImportRequestTypeDef]
    ) -> ListEnabledProductsForImportResponseTypeDef:
        """
        Lists all findings-generating solutions (products) that you are subscribed to
        receive findings from in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_enabled_products_for_import.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_enabled_products_for_import)
        """

    def list_finding_aggregators(
        self, **kwargs: Unpack[ListFindingAggregatorsRequestTypeDef]
    ) -> ListFindingAggregatorsResponseTypeDef:
        """
        If cross-Region aggregation is enabled, then
        <code>ListFindingAggregators</code> returns the Amazon Resource Name (ARN) of
        the finding aggregator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_finding_aggregators.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_finding_aggregators)
        """

    def list_invitations(
        self, **kwargs: Unpack[ListInvitationsRequestTypeDef]
    ) -> ListInvitationsResponseTypeDef:
        """
        We recommend using Organizations instead of Security Hub invitations to manage
        your member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_invitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_invitations)
        """

    def list_members(
        self, **kwargs: Unpack[ListMembersRequestTypeDef]
    ) -> ListMembersResponseTypeDef:
        """
        Lists details about all member accounts for the current Security Hub
        administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_members)
        """

    def list_organization_admin_accounts(
        self, **kwargs: Unpack[ListOrganizationAdminAccountsRequestTypeDef]
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        Lists the Security Hub administrator accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_organization_admin_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_organization_admin_accounts)
        """

    def list_security_control_definitions(
        self, **kwargs: Unpack[ListSecurityControlDefinitionsRequestTypeDef]
    ) -> ListSecurityControlDefinitionsResponseTypeDef:
        """
        Lists all of the security controls that apply to a specified standard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_security_control_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_security_control_definitions)
        """

    def list_standards_control_associations(
        self, **kwargs: Unpack[ListStandardsControlAssociationsRequestTypeDef]
    ) -> ListStandardsControlAssociationsResponseTypeDef:
        """
        Specifies whether a control is currently enabled or disabled in each enabled
        standard in the calling account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_standards_control_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_standards_control_associations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#list_tags_for_resource)
        """

    def start_configuration_policy_association(
        self, **kwargs: Unpack[StartConfigurationPolicyAssociationRequestTypeDef]
    ) -> StartConfigurationPolicyAssociationResponseTypeDef:
        """
        Associates a target account, organizational unit, or the root with a specified
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/start_configuration_policy_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#start_configuration_policy_association)
        """

    def start_configuration_policy_disassociation(
        self, **kwargs: Unpack[StartConfigurationPolicyDisassociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a target account, organizational unit, or the root from a
        specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/start_configuration_policy_disassociation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#start_configuration_policy_disassociation)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#untag_resource)
        """

    def update_action_target(
        self, **kwargs: Unpack[UpdateActionTargetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the name and description of a custom action target in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_action_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_action_target)
        """

    def update_configuration_policy(
        self, **kwargs: Unpack[UpdateConfigurationPolicyRequestTypeDef]
    ) -> UpdateConfigurationPolicyResponseTypeDef:
        """
        Updates a configuration policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_configuration_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_configuration_policy)
        """

    def update_finding_aggregator(
        self, **kwargs: Unpack[UpdateFindingAggregatorRequestTypeDef]
    ) -> UpdateFindingAggregatorResponseTypeDef:
        """
        The <i>aggregation Region</i> is now called the <i>home Region</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_finding_aggregator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_finding_aggregator)
        """

    def update_findings(self, **kwargs: Unpack[UpdateFindingsRequestTypeDef]) -> Dict[str, Any]:
        """
        <code>UpdateFindings</code> is a deprecated operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_findings)
        """

    def update_insight(self, **kwargs: Unpack[UpdateInsightRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the Security Hub insight identified by the specified insight ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_insight.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_insight)
        """

    def update_organization_configuration(
        self, **kwargs: Unpack[UpdateOrganizationConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration of your organization in Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_organization_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_organization_configuration)
        """

    def update_security_control(
        self, **kwargs: Unpack[UpdateSecurityControlRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the properties of a security control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_security_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_security_control)
        """

    def update_security_hub_configuration(
        self, **kwargs: Unpack[UpdateSecurityHubConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates configuration options for Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_security_hub_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_security_hub_configuration)
        """

    def update_standards_control(
        self, **kwargs: Unpack[UpdateStandardsControlRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Used to control whether an individual security standard control is enabled or
        disabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/update_standards_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#update_standards_control)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_action_targets"]
    ) -> DescribeActionTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_products"]
    ) -> DescribeProductsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_standards_controls"]
    ) -> DescribeStandardsControlsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_standards"]
    ) -> DescribeStandardsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_enabled_standards"]
    ) -> GetEnabledStandardsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_finding_history"]
    ) -> GetFindingHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_findings"]
    ) -> GetFindingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_insights"]
    ) -> GetInsightsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configuration_policies"]
    ) -> ListConfigurationPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configuration_policy_associations"]
    ) -> ListConfigurationPolicyAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> ListEnabledProductsForImportPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_finding_aggregators"]
    ) -> ListFindingAggregatorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_members"]
    ) -> ListMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_security_control_definitions"]
    ) -> ListSecurityControlDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_standards_control_associations"]
    ) -> ListStandardsControlAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client/#get_paginator)
        """
