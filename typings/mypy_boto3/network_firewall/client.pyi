"""
Type annotations for network-firewall service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_network_firewall.client import NetworkFirewallClient

    session = Session()
    client: NetworkFirewallClient = session.client("network-firewall")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetAnalysisReportResultsPaginator,
    ListAnalysisReportsPaginator,
    ListFirewallPoliciesPaginator,
    ListFirewallsPaginator,
    ListFlowOperationResultsPaginator,
    ListFlowOperationsPaginator,
    ListRuleGroupsPaginator,
    ListTagsForResourcePaginator,
    ListTLSInspectionConfigurationsPaginator,
)
from .type_defs import (
    AssociateFirewallPolicyRequestTypeDef,
    AssociateFirewallPolicyResponseTypeDef,
    AssociateSubnetsRequestTypeDef,
    AssociateSubnetsResponseTypeDef,
    CreateFirewallPolicyRequestTypeDef,
    CreateFirewallPolicyResponseTypeDef,
    CreateFirewallRequestTypeDef,
    CreateFirewallResponseTypeDef,
    CreateRuleGroupRequestTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateTLSInspectionConfigurationRequestTypeDef,
    CreateTLSInspectionConfigurationResponseTypeDef,
    DeleteFirewallPolicyRequestTypeDef,
    DeleteFirewallPolicyResponseTypeDef,
    DeleteFirewallRequestTypeDef,
    DeleteFirewallResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteRuleGroupRequestTypeDef,
    DeleteRuleGroupResponseTypeDef,
    DeleteTLSInspectionConfigurationRequestTypeDef,
    DeleteTLSInspectionConfigurationResponseTypeDef,
    DescribeFirewallPolicyRequestTypeDef,
    DescribeFirewallPolicyResponseTypeDef,
    DescribeFirewallRequestTypeDef,
    DescribeFirewallResponseTypeDef,
    DescribeFlowOperationRequestTypeDef,
    DescribeFlowOperationResponseTypeDef,
    DescribeLoggingConfigurationRequestTypeDef,
    DescribeLoggingConfigurationResponseTypeDef,
    DescribeResourcePolicyRequestTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeRuleGroupMetadataRequestTypeDef,
    DescribeRuleGroupMetadataResponseTypeDef,
    DescribeRuleGroupRequestTypeDef,
    DescribeRuleGroupResponseTypeDef,
    DescribeTLSInspectionConfigurationRequestTypeDef,
    DescribeTLSInspectionConfigurationResponseTypeDef,
    DisassociateSubnetsRequestTypeDef,
    DisassociateSubnetsResponseTypeDef,
    GetAnalysisReportResultsRequestTypeDef,
    GetAnalysisReportResultsResponseTypeDef,
    ListAnalysisReportsRequestTypeDef,
    ListAnalysisReportsResponseTypeDef,
    ListFirewallPoliciesRequestTypeDef,
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsRequestTypeDef,
    ListFirewallsResponseTypeDef,
    ListFlowOperationResultsRequestTypeDef,
    ListFlowOperationResultsResponseTypeDef,
    ListFlowOperationsRequestTypeDef,
    ListFlowOperationsResponseTypeDef,
    ListRuleGroupsRequestTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTLSInspectionConfigurationsRequestTypeDef,
    ListTLSInspectionConfigurationsResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    StartAnalysisReportRequestTypeDef,
    StartAnalysisReportResponseTypeDef,
    StartFlowCaptureRequestTypeDef,
    StartFlowCaptureResponseTypeDef,
    StartFlowFlushRequestTypeDef,
    StartFlowFlushResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateFirewallAnalysisSettingsRequestTypeDef,
    UpdateFirewallAnalysisSettingsResponseTypeDef,
    UpdateFirewallDeleteProtectionRequestTypeDef,
    UpdateFirewallDeleteProtectionResponseTypeDef,
    UpdateFirewallDescriptionRequestTypeDef,
    UpdateFirewallDescriptionResponseTypeDef,
    UpdateFirewallEncryptionConfigurationRequestTypeDef,
    UpdateFirewallEncryptionConfigurationResponseTypeDef,
    UpdateFirewallPolicyChangeProtectionRequestTypeDef,
    UpdateFirewallPolicyChangeProtectionResponseTypeDef,
    UpdateFirewallPolicyRequestTypeDef,
    UpdateFirewallPolicyResponseTypeDef,
    UpdateLoggingConfigurationRequestTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
    UpdateRuleGroupRequestTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateSubnetChangeProtectionRequestTypeDef,
    UpdateSubnetChangeProtectionResponseTypeDef,
    UpdateTLSInspectionConfigurationRequestTypeDef,
    UpdateTLSInspectionConfigurationResponseTypeDef,
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

__all__ = ("NetworkFirewallClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResourcePolicyException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LogDestinationPermissionException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceOwnerCheckException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class NetworkFirewallClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NetworkFirewallClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#generate_presigned_url)
        """

    def associate_firewall_policy(
        self, **kwargs: Unpack[AssociateFirewallPolicyRequestTypeDef]
    ) -> AssociateFirewallPolicyResponseTypeDef:
        """
        Associates a <a>FirewallPolicy</a> to a <a>Firewall</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/associate_firewall_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#associate_firewall_policy)
        """

    def associate_subnets(
        self, **kwargs: Unpack[AssociateSubnetsRequestTypeDef]
    ) -> AssociateSubnetsResponseTypeDef:
        """
        Associates the specified subnets in the Amazon VPC to the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/associate_subnets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#associate_subnets)
        """

    def create_firewall(
        self, **kwargs: Unpack[CreateFirewallRequestTypeDef]
    ) -> CreateFirewallResponseTypeDef:
        """
        Creates an Network Firewall <a>Firewall</a> and accompanying
        <a>FirewallStatus</a> for a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/create_firewall.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#create_firewall)
        """

    def create_firewall_policy(
        self, **kwargs: Unpack[CreateFirewallPolicyRequestTypeDef]
    ) -> CreateFirewallPolicyResponseTypeDef:
        """
        Creates the firewall policy for the firewall according to the specifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/create_firewall_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#create_firewall_policy)
        """

    def create_rule_group(
        self, **kwargs: Unpack[CreateRuleGroupRequestTypeDef]
    ) -> CreateRuleGroupResponseTypeDef:
        """
        Creates the specified stateless or stateful rule group, which includes the
        rules for network traffic inspection, a capacity setting, and tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/create_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#create_rule_group)
        """

    def create_tls_inspection_configuration(
        self, **kwargs: Unpack[CreateTLSInspectionConfigurationRequestTypeDef]
    ) -> CreateTLSInspectionConfigurationResponseTypeDef:
        """
        Creates an Network Firewall TLS inspection configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/create_tls_inspection_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#create_tls_inspection_configuration)
        """

    def delete_firewall(
        self, **kwargs: Unpack[DeleteFirewallRequestTypeDef]
    ) -> DeleteFirewallResponseTypeDef:
        """
        Deletes the specified <a>Firewall</a> and its <a>FirewallStatus</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/delete_firewall.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#delete_firewall)
        """

    def delete_firewall_policy(
        self, **kwargs: Unpack[DeleteFirewallPolicyRequestTypeDef]
    ) -> DeleteFirewallPolicyResponseTypeDef:
        """
        Deletes the specified <a>FirewallPolicy</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/delete_firewall_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#delete_firewall_policy)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource policy that you created in a <a>PutResourcePolicy</a>
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#delete_resource_policy)
        """

    def delete_rule_group(
        self, **kwargs: Unpack[DeleteRuleGroupRequestTypeDef]
    ) -> DeleteRuleGroupResponseTypeDef:
        """
        Deletes the specified <a>RuleGroup</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/delete_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#delete_rule_group)
        """

    def delete_tls_inspection_configuration(
        self, **kwargs: Unpack[DeleteTLSInspectionConfigurationRequestTypeDef]
    ) -> DeleteTLSInspectionConfigurationResponseTypeDef:
        """
        Deletes the specified <a>TLSInspectionConfiguration</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/delete_tls_inspection_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#delete_tls_inspection_configuration)
        """

    def describe_firewall(
        self, **kwargs: Unpack[DescribeFirewallRequestTypeDef]
    ) -> DescribeFirewallResponseTypeDef:
        """
        Returns the data objects for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_firewall.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_firewall)
        """

    def describe_firewall_policy(
        self, **kwargs: Unpack[DescribeFirewallPolicyRequestTypeDef]
    ) -> DescribeFirewallPolicyResponseTypeDef:
        """
        Returns the data objects for the specified firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_firewall_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_firewall_policy)
        """

    def describe_flow_operation(
        self, **kwargs: Unpack[DescribeFlowOperationRequestTypeDef]
    ) -> DescribeFlowOperationResponseTypeDef:
        """
        Returns key information about a specific flow operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_flow_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_flow_operation)
        """

    def describe_logging_configuration(
        self, **kwargs: Unpack[DescribeLoggingConfigurationRequestTypeDef]
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        Returns the logging configuration for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_logging_configuration)
        """

    def describe_resource_policy(
        self, **kwargs: Unpack[DescribeResourcePolicyRequestTypeDef]
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Retrieves a resource policy that you created in a <a>PutResourcePolicy</a>
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_resource_policy)
        """

    def describe_rule_group(
        self, **kwargs: Unpack[DescribeRuleGroupRequestTypeDef]
    ) -> DescribeRuleGroupResponseTypeDef:
        """
        Returns the data objects for the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_rule_group)
        """

    def describe_rule_group_metadata(
        self, **kwargs: Unpack[DescribeRuleGroupMetadataRequestTypeDef]
    ) -> DescribeRuleGroupMetadataResponseTypeDef:
        """
        High-level information about a rule group, returned by operations like create
        and describe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_rule_group_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_rule_group_metadata)
        """

    def describe_tls_inspection_configuration(
        self, **kwargs: Unpack[DescribeTLSInspectionConfigurationRequestTypeDef]
    ) -> DescribeTLSInspectionConfigurationResponseTypeDef:
        """
        Returns the data objects for the specified TLS inspection configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/describe_tls_inspection_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#describe_tls_inspection_configuration)
        """

    def disassociate_subnets(
        self, **kwargs: Unpack[DisassociateSubnetsRequestTypeDef]
    ) -> DisassociateSubnetsResponseTypeDef:
        """
        Removes the specified subnet associations from the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/disassociate_subnets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#disassociate_subnets)
        """

    def get_analysis_report_results(
        self, **kwargs: Unpack[GetAnalysisReportResultsRequestTypeDef]
    ) -> GetAnalysisReportResultsResponseTypeDef:
        """
        The results of a <code>COMPLETED</code> analysis report generated with
        <a>StartAnalysisReport</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_analysis_report_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_analysis_report_results)
        """

    def list_analysis_reports(
        self, **kwargs: Unpack[ListAnalysisReportsRequestTypeDef]
    ) -> ListAnalysisReportsResponseTypeDef:
        """
        Returns a list of all traffic analysis reports generated within the last 30
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_analysis_reports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_analysis_reports)
        """

    def list_firewall_policies(
        self, **kwargs: Unpack[ListFirewallPoliciesRequestTypeDef]
    ) -> ListFirewallPoliciesResponseTypeDef:
        """
        Retrieves the metadata for the firewall policies that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_firewall_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_firewall_policies)
        """

    def list_firewalls(
        self, **kwargs: Unpack[ListFirewallsRequestTypeDef]
    ) -> ListFirewallsResponseTypeDef:
        """
        Retrieves the metadata for the firewalls that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_firewalls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_firewalls)
        """

    def list_flow_operation_results(
        self, **kwargs: Unpack[ListFlowOperationResultsRequestTypeDef]
    ) -> ListFlowOperationResultsResponseTypeDef:
        """
        Returns the results of a specific flow operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_flow_operation_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_flow_operation_results)
        """

    def list_flow_operations(
        self, **kwargs: Unpack[ListFlowOperationsRequestTypeDef]
    ) -> ListFlowOperationsResponseTypeDef:
        """
        Returns a list of all flow operations ran in a specific firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_flow_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_flow_operations)
        """

    def list_rule_groups(
        self, **kwargs: Unpack[ListRuleGroupsRequestTypeDef]
    ) -> ListRuleGroupsResponseTypeDef:
        """
        Retrieves the metadata for the rule groups that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_rule_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_rule_groups)
        """

    def list_tls_inspection_configurations(
        self, **kwargs: Unpack[ListTLSInspectionConfigurationsRequestTypeDef]
    ) -> ListTLSInspectionConfigurationsResponseTypeDef:
        """
        Retrieves the metadata for the TLS inspection configurations that you have
        defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_tls_inspection_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_tls_inspection_configurations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#list_tags_for_resource)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates or updates an IAM policy for your rule group or firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#put_resource_policy)
        """

    def start_analysis_report(
        self, **kwargs: Unpack[StartAnalysisReportRequestTypeDef]
    ) -> StartAnalysisReportResponseTypeDef:
        """
        Generates a traffic analysis report for the timeframe and traffic type you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/start_analysis_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#start_analysis_report)
        """

    def start_flow_capture(
        self, **kwargs: Unpack[StartFlowCaptureRequestTypeDef]
    ) -> StartFlowCaptureResponseTypeDef:
        """
        Begins capturing the flows in a firewall, according to the filters you define.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/start_flow_capture.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#start_flow_capture)
        """

    def start_flow_flush(
        self, **kwargs: Unpack[StartFlowFlushRequestTypeDef]
    ) -> StartFlowFlushResponseTypeDef:
        """
        Begins the flushing of traffic from the firewall, according to the filters you
        define.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/start_flow_flush.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#start_flow_flush)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the tags with the specified keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#untag_resource)
        """

    def update_firewall_analysis_settings(
        self, **kwargs: Unpack[UpdateFirewallAnalysisSettingsRequestTypeDef]
    ) -> UpdateFirewallAnalysisSettingsResponseTypeDef:
        """
        Enables specific types of firewall analysis on a specific firewall you define.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_firewall_analysis_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_firewall_analysis_settings)
        """

    def update_firewall_delete_protection(
        self, **kwargs: Unpack[UpdateFirewallDeleteProtectionRequestTypeDef]
    ) -> UpdateFirewallDeleteProtectionResponseTypeDef:
        """
        Modifies the flag, <code>DeleteProtection</code>, which indicates whether it is
        possible to delete the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_firewall_delete_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_firewall_delete_protection)
        """

    def update_firewall_description(
        self, **kwargs: Unpack[UpdateFirewallDescriptionRequestTypeDef]
    ) -> UpdateFirewallDescriptionResponseTypeDef:
        """
        Modifies the description for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_firewall_description.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_firewall_description)
        """

    def update_firewall_encryption_configuration(
        self, **kwargs: Unpack[UpdateFirewallEncryptionConfigurationRequestTypeDef]
    ) -> UpdateFirewallEncryptionConfigurationResponseTypeDef:
        """
        A complex type that contains settings for encryption of your firewall resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_firewall_encryption_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_firewall_encryption_configuration)
        """

    def update_firewall_policy(
        self, **kwargs: Unpack[UpdateFirewallPolicyRequestTypeDef]
    ) -> UpdateFirewallPolicyResponseTypeDef:
        """
        Updates the properties of the specified firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_firewall_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_firewall_policy)
        """

    def update_firewall_policy_change_protection(
        self, **kwargs: Unpack[UpdateFirewallPolicyChangeProtectionRequestTypeDef]
    ) -> UpdateFirewallPolicyChangeProtectionResponseTypeDef:
        """
        Modifies the flag, <code>ChangeProtection</code>, which indicates whether it is
        possible to change the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_firewall_policy_change_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_firewall_policy_change_protection)
        """

    def update_logging_configuration(
        self, **kwargs: Unpack[UpdateLoggingConfigurationRequestTypeDef]
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Sets the logging configuration for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_logging_configuration)
        """

    def update_rule_group(
        self, **kwargs: Unpack[UpdateRuleGroupRequestTypeDef]
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        Updates the rule settings for the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_rule_group)
        """

    def update_subnet_change_protection(
        self, **kwargs: Unpack[UpdateSubnetChangeProtectionRequestTypeDef]
    ) -> UpdateSubnetChangeProtectionResponseTypeDef:
        """
        <p/>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_subnet_change_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_subnet_change_protection)
        """

    def update_tls_inspection_configuration(
        self, **kwargs: Unpack[UpdateTLSInspectionConfigurationRequestTypeDef]
    ) -> UpdateTLSInspectionConfigurationResponseTypeDef:
        """
        Updates the TLS inspection configuration settings for the specified TLS
        inspection configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/update_tls_inspection_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#update_tls_inspection_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_analysis_report_results"]
    ) -> GetAnalysisReportResultsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_analysis_reports"]
    ) -> ListAnalysisReportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_policies"]
    ) -> ListFirewallPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewalls"]
    ) -> ListFirewallsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flow_operation_results"]
    ) -> ListFlowOperationResultsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flow_operations"]
    ) -> ListFlowOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rule_groups"]
    ) -> ListRuleGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tls_inspection_configurations"]
    ) -> ListTLSInspectionConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client/#get_paginator)
        """
