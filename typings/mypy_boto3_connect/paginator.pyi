"""
Type annotations for connect service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_connect.client import ConnectClient
    from mypy_boto3_connect.paginator import (
        GetMetricDataPaginator,
        ListAgentStatusesPaginator,
        ListApprovedOriginsPaginator,
        ListAuthenticationProfilesPaginator,
        ListBotsPaginator,
        ListContactEvaluationsPaginator,
        ListContactFlowModuleAliasesPaginator,
        ListContactFlowModuleVersionsPaginator,
        ListContactFlowModulesPaginator,
        ListContactFlowVersionsPaginator,
        ListContactFlowsPaginator,
        ListContactReferencesPaginator,
        ListDataTableAttributesPaginator,
        ListDataTablePrimaryValuesPaginator,
        ListDataTableValuesPaginator,
        ListDataTablesPaginator,
        ListDefaultVocabulariesPaginator,
        ListEvaluationFormVersionsPaginator,
        ListEvaluationFormsPaginator,
        ListFlowAssociationsPaginator,
        ListHoursOfOperationOverridesPaginator,
        ListHoursOfOperationsPaginator,
        ListInstanceAttributesPaginator,
        ListInstanceStorageConfigsPaginator,
        ListInstancesPaginator,
        ListIntegrationAssociationsPaginator,
        ListLambdaFunctionsPaginator,
        ListLexBotsPaginator,
        ListPhoneNumbersPaginator,
        ListPhoneNumbersV2Paginator,
        ListPredefinedAttributesPaginator,
        ListPromptsPaginator,
        ListQueueQuickConnectsPaginator,
        ListQueuesPaginator,
        ListQuickConnectsPaginator,
        ListRoutingProfileManualAssignmentQueuesPaginator,
        ListRoutingProfileQueuesPaginator,
        ListRoutingProfilesPaginator,
        ListRulesPaginator,
        ListSecurityKeysPaginator,
        ListSecurityProfileApplicationsPaginator,
        ListSecurityProfilePermissionsPaginator,
        ListSecurityProfilesPaginator,
        ListTaskTemplatesPaginator,
        ListTrafficDistributionGroupUsersPaginator,
        ListTrafficDistributionGroupsPaginator,
        ListUseCasesPaginator,
        ListUserHierarchyGroupsPaginator,
        ListUserProficienciesPaginator,
        ListUsersPaginator,
        ListViewVersionsPaginator,
        ListViewsPaginator,
        ListWorkspacePagesPaginator,
        ListWorkspacesPaginator,
        SearchAgentStatusesPaginator,
        SearchAvailablePhoneNumbersPaginator,
        SearchContactFlowModulesPaginator,
        SearchContactFlowsPaginator,
        SearchContactsPaginator,
        SearchDataTablesPaginator,
        SearchHoursOfOperationOverridesPaginator,
        SearchHoursOfOperationsPaginator,
        SearchPredefinedAttributesPaginator,
        SearchPromptsPaginator,
        SearchQueuesPaginator,
        SearchQuickConnectsPaginator,
        SearchResourceTagsPaginator,
        SearchRoutingProfilesPaginator,
        SearchSecurityProfilesPaginator,
        SearchUserHierarchyGroupsPaginator,
        SearchUsersPaginator,
        SearchViewsPaginator,
        SearchVocabulariesPaginator,
        SearchWorkspaceAssociationsPaginator,
        SearchWorkspacesPaginator,
    )

    session = Session()
    client: ConnectClient = session.client("connect")

    get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
    list_agent_statuses_paginator: ListAgentStatusesPaginator = client.get_paginator("list_agent_statuses")
    list_approved_origins_paginator: ListApprovedOriginsPaginator = client.get_paginator("list_approved_origins")
    list_authentication_profiles_paginator: ListAuthenticationProfilesPaginator = client.get_paginator("list_authentication_profiles")
    list_bots_paginator: ListBotsPaginator = client.get_paginator("list_bots")
    list_contact_evaluations_paginator: ListContactEvaluationsPaginator = client.get_paginator("list_contact_evaluations")
    list_contact_flow_module_aliases_paginator: ListContactFlowModuleAliasesPaginator = client.get_paginator("list_contact_flow_module_aliases")
    list_contact_flow_module_versions_paginator: ListContactFlowModuleVersionsPaginator = client.get_paginator("list_contact_flow_module_versions")
    list_contact_flow_modules_paginator: ListContactFlowModulesPaginator = client.get_paginator("list_contact_flow_modules")
    list_contact_flow_versions_paginator: ListContactFlowVersionsPaginator = client.get_paginator("list_contact_flow_versions")
    list_contact_flows_paginator: ListContactFlowsPaginator = client.get_paginator("list_contact_flows")
    list_contact_references_paginator: ListContactReferencesPaginator = client.get_paginator("list_contact_references")
    list_data_table_attributes_paginator: ListDataTableAttributesPaginator = client.get_paginator("list_data_table_attributes")
    list_data_table_primary_values_paginator: ListDataTablePrimaryValuesPaginator = client.get_paginator("list_data_table_primary_values")
    list_data_table_values_paginator: ListDataTableValuesPaginator = client.get_paginator("list_data_table_values")
    list_data_tables_paginator: ListDataTablesPaginator = client.get_paginator("list_data_tables")
    list_default_vocabularies_paginator: ListDefaultVocabulariesPaginator = client.get_paginator("list_default_vocabularies")
    list_evaluation_form_versions_paginator: ListEvaluationFormVersionsPaginator = client.get_paginator("list_evaluation_form_versions")
    list_evaluation_forms_paginator: ListEvaluationFormsPaginator = client.get_paginator("list_evaluation_forms")
    list_flow_associations_paginator: ListFlowAssociationsPaginator = client.get_paginator("list_flow_associations")
    list_hours_of_operation_overrides_paginator: ListHoursOfOperationOverridesPaginator = client.get_paginator("list_hours_of_operation_overrides")
    list_hours_of_operations_paginator: ListHoursOfOperationsPaginator = client.get_paginator("list_hours_of_operations")
    list_instance_attributes_paginator: ListInstanceAttributesPaginator = client.get_paginator("list_instance_attributes")
    list_instance_storage_configs_paginator: ListInstanceStorageConfigsPaginator = client.get_paginator("list_instance_storage_configs")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_integration_associations_paginator: ListIntegrationAssociationsPaginator = client.get_paginator("list_integration_associations")
    list_lambda_functions_paginator: ListLambdaFunctionsPaginator = client.get_paginator("list_lambda_functions")
    list_lex_bots_paginator: ListLexBotsPaginator = client.get_paginator("list_lex_bots")
    list_phone_numbers_paginator: ListPhoneNumbersPaginator = client.get_paginator("list_phone_numbers")
    list_phone_numbers_v2_paginator: ListPhoneNumbersV2Paginator = client.get_paginator("list_phone_numbers_v2")
    list_predefined_attributes_paginator: ListPredefinedAttributesPaginator = client.get_paginator("list_predefined_attributes")
    list_prompts_paginator: ListPromptsPaginator = client.get_paginator("list_prompts")
    list_queue_quick_connects_paginator: ListQueueQuickConnectsPaginator = client.get_paginator("list_queue_quick_connects")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    list_quick_connects_paginator: ListQuickConnectsPaginator = client.get_paginator("list_quick_connects")
    list_routing_profile_manual_assignment_queues_paginator: ListRoutingProfileManualAssignmentQueuesPaginator = client.get_paginator("list_routing_profile_manual_assignment_queues")
    list_routing_profile_queues_paginator: ListRoutingProfileQueuesPaginator = client.get_paginator("list_routing_profile_queues")
    list_routing_profiles_paginator: ListRoutingProfilesPaginator = client.get_paginator("list_routing_profiles")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_security_keys_paginator: ListSecurityKeysPaginator = client.get_paginator("list_security_keys")
    list_security_profile_applications_paginator: ListSecurityProfileApplicationsPaginator = client.get_paginator("list_security_profile_applications")
    list_security_profile_permissions_paginator: ListSecurityProfilePermissionsPaginator = client.get_paginator("list_security_profile_permissions")
    list_security_profiles_paginator: ListSecurityProfilesPaginator = client.get_paginator("list_security_profiles")
    list_task_templates_paginator: ListTaskTemplatesPaginator = client.get_paginator("list_task_templates")
    list_traffic_distribution_group_users_paginator: ListTrafficDistributionGroupUsersPaginator = client.get_paginator("list_traffic_distribution_group_users")
    list_traffic_distribution_groups_paginator: ListTrafficDistributionGroupsPaginator = client.get_paginator("list_traffic_distribution_groups")
    list_use_cases_paginator: ListUseCasesPaginator = client.get_paginator("list_use_cases")
    list_user_hierarchy_groups_paginator: ListUserHierarchyGroupsPaginator = client.get_paginator("list_user_hierarchy_groups")
    list_user_proficiencies_paginator: ListUserProficienciesPaginator = client.get_paginator("list_user_proficiencies")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_view_versions_paginator: ListViewVersionsPaginator = client.get_paginator("list_view_versions")
    list_views_paginator: ListViewsPaginator = client.get_paginator("list_views")
    list_workspace_pages_paginator: ListWorkspacePagesPaginator = client.get_paginator("list_workspace_pages")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    search_agent_statuses_paginator: SearchAgentStatusesPaginator = client.get_paginator("search_agent_statuses")
    search_available_phone_numbers_paginator: SearchAvailablePhoneNumbersPaginator = client.get_paginator("search_available_phone_numbers")
    search_contact_flow_modules_paginator: SearchContactFlowModulesPaginator = client.get_paginator("search_contact_flow_modules")
    search_contact_flows_paginator: SearchContactFlowsPaginator = client.get_paginator("search_contact_flows")
    search_contacts_paginator: SearchContactsPaginator = client.get_paginator("search_contacts")
    search_data_tables_paginator: SearchDataTablesPaginator = client.get_paginator("search_data_tables")
    search_hours_of_operation_overrides_paginator: SearchHoursOfOperationOverridesPaginator = client.get_paginator("search_hours_of_operation_overrides")
    search_hours_of_operations_paginator: SearchHoursOfOperationsPaginator = client.get_paginator("search_hours_of_operations")
    search_predefined_attributes_paginator: SearchPredefinedAttributesPaginator = client.get_paginator("search_predefined_attributes")
    search_prompts_paginator: SearchPromptsPaginator = client.get_paginator("search_prompts")
    search_queues_paginator: SearchQueuesPaginator = client.get_paginator("search_queues")
    search_quick_connects_paginator: SearchQuickConnectsPaginator = client.get_paginator("search_quick_connects")
    search_resource_tags_paginator: SearchResourceTagsPaginator = client.get_paginator("search_resource_tags")
    search_routing_profiles_paginator: SearchRoutingProfilesPaginator = client.get_paginator("search_routing_profiles")
    search_security_profiles_paginator: SearchSecurityProfilesPaginator = client.get_paginator("search_security_profiles")
    search_user_hierarchy_groups_paginator: SearchUserHierarchyGroupsPaginator = client.get_paginator("search_user_hierarchy_groups")
    search_users_paginator: SearchUsersPaginator = client.get_paginator("search_users")
    search_views_paginator: SearchViewsPaginator = client.get_paginator("search_views")
    search_vocabularies_paginator: SearchVocabulariesPaginator = client.get_paginator("search_vocabularies")
    search_workspace_associations_paginator: SearchWorkspaceAssociationsPaginator = client.get_paginator("search_workspace_associations")
    search_workspaces_paginator: SearchWorkspacesPaginator = client.get_paginator("search_workspaces")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetMetricDataRequestPaginateTypeDef,
    GetMetricDataResponseTypeDef,
    ListAgentStatusRequestPaginateTypeDef,
    ListAgentStatusResponseTypeDef,
    ListApprovedOriginsRequestPaginateTypeDef,
    ListApprovedOriginsResponseTypeDef,
    ListAuthenticationProfilesRequestPaginateTypeDef,
    ListAuthenticationProfilesResponseTypeDef,
    ListBotsRequestPaginateTypeDef,
    ListBotsResponseTypeDef,
    ListContactEvaluationsRequestPaginateTypeDef,
    ListContactEvaluationsResponseTypeDef,
    ListContactFlowModuleAliasesRequestPaginateTypeDef,
    ListContactFlowModuleAliasesResponseTypeDef,
    ListContactFlowModulesRequestPaginateTypeDef,
    ListContactFlowModulesResponseTypeDef,
    ListContactFlowModuleVersionsRequestPaginateTypeDef,
    ListContactFlowModuleVersionsResponseTypeDef,
    ListContactFlowsRequestPaginateTypeDef,
    ListContactFlowsResponseTypeDef,
    ListContactFlowVersionsRequestPaginateTypeDef,
    ListContactFlowVersionsResponseTypeDef,
    ListContactReferencesRequestPaginateTypeDef,
    ListContactReferencesResponseTypeDef,
    ListDataTableAttributesRequestPaginateTypeDef,
    ListDataTableAttributesResponseTypeDef,
    ListDataTablePrimaryValuesRequestPaginateTypeDef,
    ListDataTablePrimaryValuesResponseTypeDef,
    ListDataTablesRequestPaginateTypeDef,
    ListDataTablesResponseTypeDef,
    ListDataTableValuesRequestPaginateTypeDef,
    ListDataTableValuesResponseTypeDef,
    ListDefaultVocabulariesRequestPaginateTypeDef,
    ListDefaultVocabulariesResponseTypeDef,
    ListEvaluationFormsRequestPaginateTypeDef,
    ListEvaluationFormsResponseTypeDef,
    ListEvaluationFormVersionsRequestPaginateTypeDef,
    ListEvaluationFormVersionsResponseTypeDef,
    ListFlowAssociationsRequestPaginateTypeDef,
    ListFlowAssociationsResponseTypeDef,
    ListHoursOfOperationOverridesRequestPaginateTypeDef,
    ListHoursOfOperationOverridesResponseTypeDef,
    ListHoursOfOperationsRequestPaginateTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListInstanceAttributesRequestPaginateTypeDef,
    ListInstanceAttributesResponseTypeDef,
    ListInstancesRequestPaginateTypeDef,
    ListInstancesResponseTypeDef,
    ListInstanceStorageConfigsRequestPaginateTypeDef,
    ListInstanceStorageConfigsResponseTypeDef,
    ListIntegrationAssociationsRequestPaginateTypeDef,
    ListIntegrationAssociationsResponseTypeDef,
    ListLambdaFunctionsRequestPaginateTypeDef,
    ListLambdaFunctionsResponseTypeDef,
    ListLexBotsRequestPaginateTypeDef,
    ListLexBotsResponseTypeDef,
    ListPhoneNumbersRequestPaginateTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListPhoneNumbersV2RequestPaginateTypeDef,
    ListPhoneNumbersV2ResponseTypeDef,
    ListPredefinedAttributesRequestPaginateTypeDef,
    ListPredefinedAttributesResponseTypeDef,
    ListPromptsRequestPaginateTypeDef,
    ListPromptsResponseTypeDef,
    ListQueueQuickConnectsRequestPaginateTypeDef,
    ListQueueQuickConnectsResponseTypeDef,
    ListQueuesRequestPaginateTypeDef,
    ListQueuesResponseTypeDef,
    ListQuickConnectsRequestPaginateTypeDef,
    ListQuickConnectsResponseTypeDef,
    ListRoutingProfileManualAssignmentQueuesRequestPaginateTypeDef,
    ListRoutingProfileManualAssignmentQueuesResponseTypeDef,
    ListRoutingProfileQueuesRequestPaginateTypeDef,
    ListRoutingProfileQueuesResponseTypeDef,
    ListRoutingProfilesRequestPaginateTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListRulesRequestPaginateTypeDef,
    ListRulesResponseTypeDef,
    ListSecurityKeysRequestPaginateTypeDef,
    ListSecurityKeysResponseTypeDef,
    ListSecurityProfileApplicationsRequestPaginateTypeDef,
    ListSecurityProfileApplicationsResponseTypeDef,
    ListSecurityProfilePermissionsRequestPaginateTypeDef,
    ListSecurityProfilePermissionsResponseTypeDef,
    ListSecurityProfilesRequestPaginateTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListTaskTemplatesRequestPaginateTypeDef,
    ListTaskTemplatesResponseTypeDef,
    ListTrafficDistributionGroupsRequestPaginateTypeDef,
    ListTrafficDistributionGroupsResponseTypeDef,
    ListTrafficDistributionGroupUsersRequestPaginateTypeDef,
    ListTrafficDistributionGroupUsersResponseTypeDef,
    ListUseCasesRequestPaginateTypeDef,
    ListUseCasesResponseTypeDef,
    ListUserHierarchyGroupsRequestPaginateTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUserProficienciesRequestPaginateTypeDef,
    ListUserProficienciesResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
    ListViewsRequestPaginateTypeDef,
    ListViewsResponseTypeDef,
    ListViewVersionsRequestPaginateTypeDef,
    ListViewVersionsResponseTypeDef,
    ListWorkspacePagesRequestPaginateTypeDef,
    ListWorkspacePagesResponseTypeDef,
    ListWorkspacesRequestPaginateTypeDef,
    ListWorkspacesResponseTypeDef,
    SearchAgentStatusesRequestPaginateTypeDef,
    SearchAgentStatusesResponseTypeDef,
    SearchAvailablePhoneNumbersRequestPaginateTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    SearchContactFlowModulesRequestPaginateTypeDef,
    SearchContactFlowModulesResponseTypeDef,
    SearchContactFlowsRequestPaginateTypeDef,
    SearchContactFlowsResponseTypeDef,
    SearchContactsRequestPaginateTypeDef,
    SearchContactsResponsePaginatorTypeDef,
    SearchDataTablesRequestPaginateTypeDef,
    SearchDataTablesResponseTypeDef,
    SearchHoursOfOperationOverridesRequestPaginateTypeDef,
    SearchHoursOfOperationOverridesResponseTypeDef,
    SearchHoursOfOperationsRequestPaginateTypeDef,
    SearchHoursOfOperationsResponseTypeDef,
    SearchPredefinedAttributesRequestPaginateTypeDef,
    SearchPredefinedAttributesResponseTypeDef,
    SearchPromptsRequestPaginateTypeDef,
    SearchPromptsResponseTypeDef,
    SearchQueuesRequestPaginateTypeDef,
    SearchQueuesResponseTypeDef,
    SearchQuickConnectsRequestPaginateTypeDef,
    SearchQuickConnectsResponseTypeDef,
    SearchResourceTagsRequestPaginateTypeDef,
    SearchResourceTagsResponseTypeDef,
    SearchRoutingProfilesRequestPaginateTypeDef,
    SearchRoutingProfilesResponseTypeDef,
    SearchSecurityProfilesRequestPaginateTypeDef,
    SearchSecurityProfilesResponseTypeDef,
    SearchUserHierarchyGroupsRequestPaginateTypeDef,
    SearchUserHierarchyGroupsResponseTypeDef,
    SearchUsersRequestPaginateTypeDef,
    SearchUsersResponseTypeDef,
    SearchViewsRequestPaginateTypeDef,
    SearchViewsResponseTypeDef,
    SearchVocabulariesRequestPaginateTypeDef,
    SearchVocabulariesResponseTypeDef,
    SearchWorkspaceAssociationsRequestPaginateTypeDef,
    SearchWorkspaceAssociationsResponseTypeDef,
    SearchWorkspacesRequestPaginateTypeDef,
    SearchWorkspacesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetMetricDataPaginator",
    "ListAgentStatusesPaginator",
    "ListApprovedOriginsPaginator",
    "ListAuthenticationProfilesPaginator",
    "ListBotsPaginator",
    "ListContactEvaluationsPaginator",
    "ListContactFlowModuleAliasesPaginator",
    "ListContactFlowModuleVersionsPaginator",
    "ListContactFlowModulesPaginator",
    "ListContactFlowVersionsPaginator",
    "ListContactFlowsPaginator",
    "ListContactReferencesPaginator",
    "ListDataTableAttributesPaginator",
    "ListDataTablePrimaryValuesPaginator",
    "ListDataTableValuesPaginator",
    "ListDataTablesPaginator",
    "ListDefaultVocabulariesPaginator",
    "ListEvaluationFormVersionsPaginator",
    "ListEvaluationFormsPaginator",
    "ListFlowAssociationsPaginator",
    "ListHoursOfOperationOverridesPaginator",
    "ListHoursOfOperationsPaginator",
    "ListInstanceAttributesPaginator",
    "ListInstanceStorageConfigsPaginator",
    "ListInstancesPaginator",
    "ListIntegrationAssociationsPaginator",
    "ListLambdaFunctionsPaginator",
    "ListLexBotsPaginator",
    "ListPhoneNumbersPaginator",
    "ListPhoneNumbersV2Paginator",
    "ListPredefinedAttributesPaginator",
    "ListPromptsPaginator",
    "ListQueueQuickConnectsPaginator",
    "ListQueuesPaginator",
    "ListQuickConnectsPaginator",
    "ListRoutingProfileManualAssignmentQueuesPaginator",
    "ListRoutingProfileQueuesPaginator",
    "ListRoutingProfilesPaginator",
    "ListRulesPaginator",
    "ListSecurityKeysPaginator",
    "ListSecurityProfileApplicationsPaginator",
    "ListSecurityProfilePermissionsPaginator",
    "ListSecurityProfilesPaginator",
    "ListTaskTemplatesPaginator",
    "ListTrafficDistributionGroupUsersPaginator",
    "ListTrafficDistributionGroupsPaginator",
    "ListUseCasesPaginator",
    "ListUserHierarchyGroupsPaginator",
    "ListUserProficienciesPaginator",
    "ListUsersPaginator",
    "ListViewVersionsPaginator",
    "ListViewsPaginator",
    "ListWorkspacePagesPaginator",
    "ListWorkspacesPaginator",
    "SearchAgentStatusesPaginator",
    "SearchAvailablePhoneNumbersPaginator",
    "SearchContactFlowModulesPaginator",
    "SearchContactFlowsPaginator",
    "SearchContactsPaginator",
    "SearchDataTablesPaginator",
    "SearchHoursOfOperationOverridesPaginator",
    "SearchHoursOfOperationsPaginator",
    "SearchPredefinedAttributesPaginator",
    "SearchPromptsPaginator",
    "SearchQueuesPaginator",
    "SearchQuickConnectsPaginator",
    "SearchResourceTagsPaginator",
    "SearchRoutingProfilesPaginator",
    "SearchSecurityProfilesPaginator",
    "SearchUserHierarchyGroupsPaginator",
    "SearchUsersPaginator",
    "SearchViewsPaginator",
    "SearchVocabulariesPaginator",
    "SearchWorkspaceAssociationsPaginator",
    "SearchWorkspacesPaginator",
)

if TYPE_CHECKING:
    _GetMetricDataPaginatorBase = Paginator[GetMetricDataResponseTypeDef]
else:
    _GetMetricDataPaginatorBase = Paginator  # type: ignore[assignment]

class GetMetricDataPaginator(_GetMetricDataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/GetMetricData.html#Connect.Paginator.GetMetricData)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#getmetricdatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetMetricDataRequestPaginateTypeDef]
    ) -> PageIterator[GetMetricDataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/GetMetricData.html#Connect.Paginator.GetMetricData.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#getmetricdatapaginator)
        """

if TYPE_CHECKING:
    _ListAgentStatusesPaginatorBase = Paginator[ListAgentStatusResponseTypeDef]
else:
    _ListAgentStatusesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentStatusesPaginator(_ListAgentStatusesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListAgentStatuses.html#Connect.Paginator.ListAgentStatuses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listagentstatusespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentStatusRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListAgentStatuses.html#Connect.Paginator.ListAgentStatuses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listagentstatusespaginator)
        """

if TYPE_CHECKING:
    _ListApprovedOriginsPaginatorBase = Paginator[ListApprovedOriginsResponseTypeDef]
else:
    _ListApprovedOriginsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApprovedOriginsPaginator(_ListApprovedOriginsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListApprovedOrigins.html#Connect.Paginator.ListApprovedOrigins)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listapprovedoriginspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApprovedOriginsRequestPaginateTypeDef]
    ) -> PageIterator[ListApprovedOriginsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListApprovedOrigins.html#Connect.Paginator.ListApprovedOrigins.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listapprovedoriginspaginator)
        """

if TYPE_CHECKING:
    _ListAuthenticationProfilesPaginatorBase = Paginator[ListAuthenticationProfilesResponseTypeDef]
else:
    _ListAuthenticationProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAuthenticationProfilesPaginator(_ListAuthenticationProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListAuthenticationProfiles.html#Connect.Paginator.ListAuthenticationProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listauthenticationprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAuthenticationProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListAuthenticationProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListAuthenticationProfiles.html#Connect.Paginator.ListAuthenticationProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listauthenticationprofilespaginator)
        """

if TYPE_CHECKING:
    _ListBotsPaginatorBase = Paginator[ListBotsResponseTypeDef]
else:
    _ListBotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBotsPaginator(_ListBotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListBots.html#Connect.Paginator.ListBots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listbotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBotsRequestPaginateTypeDef]
    ) -> PageIterator[ListBotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListBots.html#Connect.Paginator.ListBots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listbotspaginator)
        """

if TYPE_CHECKING:
    _ListContactEvaluationsPaginatorBase = Paginator[ListContactEvaluationsResponseTypeDef]
else:
    _ListContactEvaluationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactEvaluationsPaginator(_ListContactEvaluationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactEvaluations.html#Connect.Paginator.ListContactEvaluations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactevaluationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactEvaluationsRequestPaginateTypeDef]
    ) -> PageIterator[ListContactEvaluationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactEvaluations.html#Connect.Paginator.ListContactEvaluations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactevaluationspaginator)
        """

if TYPE_CHECKING:
    _ListContactFlowModuleAliasesPaginatorBase = Paginator[
        ListContactFlowModuleAliasesResponseTypeDef
    ]
else:
    _ListContactFlowModuleAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactFlowModuleAliasesPaginator(_ListContactFlowModuleAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowModuleAliases.html#Connect.Paginator.ListContactFlowModuleAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowmodulealiasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactFlowModuleAliasesRequestPaginateTypeDef]
    ) -> PageIterator[ListContactFlowModuleAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowModuleAliases.html#Connect.Paginator.ListContactFlowModuleAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowmodulealiasespaginator)
        """

if TYPE_CHECKING:
    _ListContactFlowModuleVersionsPaginatorBase = Paginator[
        ListContactFlowModuleVersionsResponseTypeDef
    ]
else:
    _ListContactFlowModuleVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactFlowModuleVersionsPaginator(_ListContactFlowModuleVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowModuleVersions.html#Connect.Paginator.ListContactFlowModuleVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowmoduleversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactFlowModuleVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListContactFlowModuleVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowModuleVersions.html#Connect.Paginator.ListContactFlowModuleVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowmoduleversionspaginator)
        """

if TYPE_CHECKING:
    _ListContactFlowModulesPaginatorBase = Paginator[ListContactFlowModulesResponseTypeDef]
else:
    _ListContactFlowModulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactFlowModulesPaginator(_ListContactFlowModulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowModules.html#Connect.Paginator.ListContactFlowModules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowmodulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactFlowModulesRequestPaginateTypeDef]
    ) -> PageIterator[ListContactFlowModulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowModules.html#Connect.Paginator.ListContactFlowModules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowmodulespaginator)
        """

if TYPE_CHECKING:
    _ListContactFlowVersionsPaginatorBase = Paginator[ListContactFlowVersionsResponseTypeDef]
else:
    _ListContactFlowVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactFlowVersionsPaginator(_ListContactFlowVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowVersions.html#Connect.Paginator.ListContactFlowVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactFlowVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListContactFlowVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlowVersions.html#Connect.Paginator.ListContactFlowVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowversionspaginator)
        """

if TYPE_CHECKING:
    _ListContactFlowsPaginatorBase = Paginator[ListContactFlowsResponseTypeDef]
else:
    _ListContactFlowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactFlowsPaginator(_ListContactFlowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlows.html#Connect.Paginator.ListContactFlows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactFlowsRequestPaginateTypeDef]
    ) -> PageIterator[ListContactFlowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactFlows.html#Connect.Paginator.ListContactFlows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactflowspaginator)
        """

if TYPE_CHECKING:
    _ListContactReferencesPaginatorBase = Paginator[ListContactReferencesResponseTypeDef]
else:
    _ListContactReferencesPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactReferencesPaginator(_ListContactReferencesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactReferences.html#Connect.Paginator.ListContactReferences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactreferencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactReferencesRequestPaginateTypeDef]
    ) -> PageIterator[ListContactReferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListContactReferences.html#Connect.Paginator.ListContactReferences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listcontactreferencespaginator)
        """

if TYPE_CHECKING:
    _ListDataTableAttributesPaginatorBase = Paginator[ListDataTableAttributesResponseTypeDef]
else:
    _ListDataTableAttributesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataTableAttributesPaginator(_ListDataTableAttributesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTableAttributes.html#Connect.Paginator.ListDataTableAttributes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatableattributespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataTableAttributesRequestPaginateTypeDef]
    ) -> PageIterator[ListDataTableAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTableAttributes.html#Connect.Paginator.ListDataTableAttributes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatableattributespaginator)
        """

if TYPE_CHECKING:
    _ListDataTablePrimaryValuesPaginatorBase = Paginator[ListDataTablePrimaryValuesResponseTypeDef]
else:
    _ListDataTablePrimaryValuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataTablePrimaryValuesPaginator(_ListDataTablePrimaryValuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTablePrimaryValues.html#Connect.Paginator.ListDataTablePrimaryValues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatableprimaryvaluespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataTablePrimaryValuesRequestPaginateTypeDef]
    ) -> PageIterator[ListDataTablePrimaryValuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTablePrimaryValues.html#Connect.Paginator.ListDataTablePrimaryValues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatableprimaryvaluespaginator)
        """

if TYPE_CHECKING:
    _ListDataTableValuesPaginatorBase = Paginator[ListDataTableValuesResponseTypeDef]
else:
    _ListDataTableValuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataTableValuesPaginator(_ListDataTableValuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTableValues.html#Connect.Paginator.ListDataTableValues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatablevaluespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataTableValuesRequestPaginateTypeDef]
    ) -> PageIterator[ListDataTableValuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTableValues.html#Connect.Paginator.ListDataTableValues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatablevaluespaginator)
        """

if TYPE_CHECKING:
    _ListDataTablesPaginatorBase = Paginator[ListDataTablesResponseTypeDef]
else:
    _ListDataTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataTablesPaginator(_ListDataTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTables.html#Connect.Paginator.ListDataTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataTablesRequestPaginateTypeDef]
    ) -> PageIterator[ListDataTablesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDataTables.html#Connect.Paginator.ListDataTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdatatablespaginator)
        """

if TYPE_CHECKING:
    _ListDefaultVocabulariesPaginatorBase = Paginator[ListDefaultVocabulariesResponseTypeDef]
else:
    _ListDefaultVocabulariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDefaultVocabulariesPaginator(_ListDefaultVocabulariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDefaultVocabularies.html#Connect.Paginator.ListDefaultVocabularies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdefaultvocabulariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDefaultVocabulariesRequestPaginateTypeDef]
    ) -> PageIterator[ListDefaultVocabulariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListDefaultVocabularies.html#Connect.Paginator.ListDefaultVocabularies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listdefaultvocabulariespaginator)
        """

if TYPE_CHECKING:
    _ListEvaluationFormVersionsPaginatorBase = Paginator[ListEvaluationFormVersionsResponseTypeDef]
else:
    _ListEvaluationFormVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEvaluationFormVersionsPaginator(_ListEvaluationFormVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListEvaluationFormVersions.html#Connect.Paginator.ListEvaluationFormVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listevaluationformversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEvaluationFormVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListEvaluationFormVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListEvaluationFormVersions.html#Connect.Paginator.ListEvaluationFormVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listevaluationformversionspaginator)
        """

if TYPE_CHECKING:
    _ListEvaluationFormsPaginatorBase = Paginator[ListEvaluationFormsResponseTypeDef]
else:
    _ListEvaluationFormsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEvaluationFormsPaginator(_ListEvaluationFormsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListEvaluationForms.html#Connect.Paginator.ListEvaluationForms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listevaluationformspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEvaluationFormsRequestPaginateTypeDef]
    ) -> PageIterator[ListEvaluationFormsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListEvaluationForms.html#Connect.Paginator.ListEvaluationForms.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listevaluationformspaginator)
        """

if TYPE_CHECKING:
    _ListFlowAssociationsPaginatorBase = Paginator[ListFlowAssociationsResponseTypeDef]
else:
    _ListFlowAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowAssociationsPaginator(_ListFlowAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListFlowAssociations.html#Connect.Paginator.ListFlowAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listflowassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListFlowAssociations.html#Connect.Paginator.ListFlowAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listflowassociationspaginator)
        """

if TYPE_CHECKING:
    _ListHoursOfOperationOverridesPaginatorBase = Paginator[
        ListHoursOfOperationOverridesResponseTypeDef
    ]
else:
    _ListHoursOfOperationOverridesPaginatorBase = Paginator  # type: ignore[assignment]

class ListHoursOfOperationOverridesPaginator(_ListHoursOfOperationOverridesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListHoursOfOperationOverrides.html#Connect.Paginator.ListHoursOfOperationOverrides)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listhoursofoperationoverridespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHoursOfOperationOverridesRequestPaginateTypeDef]
    ) -> PageIterator[ListHoursOfOperationOverridesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListHoursOfOperationOverrides.html#Connect.Paginator.ListHoursOfOperationOverrides.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listhoursofoperationoverridespaginator)
        """

if TYPE_CHECKING:
    _ListHoursOfOperationsPaginatorBase = Paginator[ListHoursOfOperationsResponseTypeDef]
else:
    _ListHoursOfOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHoursOfOperationsPaginator(_ListHoursOfOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListHoursOfOperations.html#Connect.Paginator.ListHoursOfOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listhoursofoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHoursOfOperationsRequestPaginateTypeDef]
    ) -> PageIterator[ListHoursOfOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListHoursOfOperations.html#Connect.Paginator.ListHoursOfOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listhoursofoperationspaginator)
        """

if TYPE_CHECKING:
    _ListInstanceAttributesPaginatorBase = Paginator[ListInstanceAttributesResponseTypeDef]
else:
    _ListInstanceAttributesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstanceAttributesPaginator(_ListInstanceAttributesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListInstanceAttributes.html#Connect.Paginator.ListInstanceAttributes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listinstanceattributespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceAttributesRequestPaginateTypeDef]
    ) -> PageIterator[ListInstanceAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListInstanceAttributes.html#Connect.Paginator.ListInstanceAttributes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listinstanceattributespaginator)
        """

if TYPE_CHECKING:
    _ListInstanceStorageConfigsPaginatorBase = Paginator[ListInstanceStorageConfigsResponseTypeDef]
else:
    _ListInstanceStorageConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstanceStorageConfigsPaginator(_ListInstanceStorageConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListInstanceStorageConfigs.html#Connect.Paginator.ListInstanceStorageConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listinstancestorageconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceStorageConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListInstanceStorageConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListInstanceStorageConfigs.html#Connect.Paginator.ListInstanceStorageConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listinstancestorageconfigspaginator)
        """

if TYPE_CHECKING:
    _ListInstancesPaginatorBase = Paginator[ListInstancesResponseTypeDef]
else:
    _ListInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstancesPaginator(_ListInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListInstances.html#Connect.Paginator.ListInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListInstances.html#Connect.Paginator.ListInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listinstancespaginator)
        """

if TYPE_CHECKING:
    _ListIntegrationAssociationsPaginatorBase = Paginator[
        ListIntegrationAssociationsResponseTypeDef
    ]
else:
    _ListIntegrationAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIntegrationAssociationsPaginator(_ListIntegrationAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListIntegrationAssociations.html#Connect.Paginator.ListIntegrationAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listintegrationassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIntegrationAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListIntegrationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListIntegrationAssociations.html#Connect.Paginator.ListIntegrationAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listintegrationassociationspaginator)
        """

if TYPE_CHECKING:
    _ListLambdaFunctionsPaginatorBase = Paginator[ListLambdaFunctionsResponseTypeDef]
else:
    _ListLambdaFunctionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLambdaFunctionsPaginator(_ListLambdaFunctionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListLambdaFunctions.html#Connect.Paginator.ListLambdaFunctions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listlambdafunctionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLambdaFunctionsRequestPaginateTypeDef]
    ) -> PageIterator[ListLambdaFunctionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListLambdaFunctions.html#Connect.Paginator.ListLambdaFunctions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listlambdafunctionspaginator)
        """

if TYPE_CHECKING:
    _ListLexBotsPaginatorBase = Paginator[ListLexBotsResponseTypeDef]
else:
    _ListLexBotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLexBotsPaginator(_ListLexBotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListLexBots.html#Connect.Paginator.ListLexBots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listlexbotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLexBotsRequestPaginateTypeDef]
    ) -> PageIterator[ListLexBotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListLexBots.html#Connect.Paginator.ListLexBots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listlexbotspaginator)
        """

if TYPE_CHECKING:
    _ListPhoneNumbersPaginatorBase = Paginator[ListPhoneNumbersResponseTypeDef]
else:
    _ListPhoneNumbersPaginatorBase = Paginator  # type: ignore[assignment]

class ListPhoneNumbersPaginator(_ListPhoneNumbersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPhoneNumbers.html#Connect.Paginator.ListPhoneNumbers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listphonenumberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPhoneNumbersRequestPaginateTypeDef]
    ) -> PageIterator[ListPhoneNumbersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPhoneNumbers.html#Connect.Paginator.ListPhoneNumbers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listphonenumberspaginator)
        """

if TYPE_CHECKING:
    _ListPhoneNumbersV2PaginatorBase = Paginator[ListPhoneNumbersV2ResponseTypeDef]
else:
    _ListPhoneNumbersV2PaginatorBase = Paginator  # type: ignore[assignment]

class ListPhoneNumbersV2Paginator(_ListPhoneNumbersV2PaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPhoneNumbersV2.html#Connect.Paginator.ListPhoneNumbersV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listphonenumbersv2paginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPhoneNumbersV2RequestPaginateTypeDef]
    ) -> PageIterator[ListPhoneNumbersV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPhoneNumbersV2.html#Connect.Paginator.ListPhoneNumbersV2.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listphonenumbersv2paginator)
        """

if TYPE_CHECKING:
    _ListPredefinedAttributesPaginatorBase = Paginator[ListPredefinedAttributesResponseTypeDef]
else:
    _ListPredefinedAttributesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPredefinedAttributesPaginator(_ListPredefinedAttributesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPredefinedAttributes.html#Connect.Paginator.ListPredefinedAttributes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listpredefinedattributespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPredefinedAttributesRequestPaginateTypeDef]
    ) -> PageIterator[ListPredefinedAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPredefinedAttributes.html#Connect.Paginator.ListPredefinedAttributes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listpredefinedattributespaginator)
        """

if TYPE_CHECKING:
    _ListPromptsPaginatorBase = Paginator[ListPromptsResponseTypeDef]
else:
    _ListPromptsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPromptsPaginator(_ListPromptsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPrompts.html#Connect.Paginator.ListPrompts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listpromptspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPromptsRequestPaginateTypeDef]
    ) -> PageIterator[ListPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListPrompts.html#Connect.Paginator.ListPrompts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listpromptspaginator)
        """

if TYPE_CHECKING:
    _ListQueueQuickConnectsPaginatorBase = Paginator[ListQueueQuickConnectsResponseTypeDef]
else:
    _ListQueueQuickConnectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueueQuickConnectsPaginator(_ListQueueQuickConnectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListQueueQuickConnects.html#Connect.Paginator.ListQueueQuickConnects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listqueuequickconnectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueueQuickConnectsRequestPaginateTypeDef]
    ) -> PageIterator[ListQueueQuickConnectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListQueueQuickConnects.html#Connect.Paginator.ListQueueQuickConnects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listqueuequickconnectspaginator)
        """

if TYPE_CHECKING:
    _ListQueuesPaginatorBase = Paginator[ListQueuesResponseTypeDef]
else:
    _ListQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueuesPaginator(_ListQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListQueues.html#Connect.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListQueues.html#Connect.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listqueuespaginator)
        """

if TYPE_CHECKING:
    _ListQuickConnectsPaginatorBase = Paginator[ListQuickConnectsResponseTypeDef]
else:
    _ListQuickConnectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQuickConnectsPaginator(_ListQuickConnectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListQuickConnects.html#Connect.Paginator.ListQuickConnects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listquickconnectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQuickConnectsRequestPaginateTypeDef]
    ) -> PageIterator[ListQuickConnectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListQuickConnects.html#Connect.Paginator.ListQuickConnects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listquickconnectspaginator)
        """

if TYPE_CHECKING:
    _ListRoutingProfileManualAssignmentQueuesPaginatorBase = Paginator[
        ListRoutingProfileManualAssignmentQueuesResponseTypeDef
    ]
else:
    _ListRoutingProfileManualAssignmentQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoutingProfileManualAssignmentQueuesPaginator(
    _ListRoutingProfileManualAssignmentQueuesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRoutingProfileManualAssignmentQueues.html#Connect.Paginator.ListRoutingProfileManualAssignmentQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listroutingprofilemanualassignmentqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoutingProfileManualAssignmentQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListRoutingProfileManualAssignmentQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRoutingProfileManualAssignmentQueues.html#Connect.Paginator.ListRoutingProfileManualAssignmentQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listroutingprofilemanualassignmentqueuespaginator)
        """

if TYPE_CHECKING:
    _ListRoutingProfileQueuesPaginatorBase = Paginator[ListRoutingProfileQueuesResponseTypeDef]
else:
    _ListRoutingProfileQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoutingProfileQueuesPaginator(_ListRoutingProfileQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRoutingProfileQueues.html#Connect.Paginator.ListRoutingProfileQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listroutingprofilequeuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoutingProfileQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListRoutingProfileQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRoutingProfileQueues.html#Connect.Paginator.ListRoutingProfileQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listroutingprofilequeuespaginator)
        """

if TYPE_CHECKING:
    _ListRoutingProfilesPaginatorBase = Paginator[ListRoutingProfilesResponseTypeDef]
else:
    _ListRoutingProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoutingProfilesPaginator(_ListRoutingProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRoutingProfiles.html#Connect.Paginator.ListRoutingProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listroutingprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoutingProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListRoutingProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRoutingProfiles.html#Connect.Paginator.ListRoutingProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listroutingprofilespaginator)
        """

if TYPE_CHECKING:
    _ListRulesPaginatorBase = Paginator[ListRulesResponseTypeDef]
else:
    _ListRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRulesPaginator(_ListRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRules.html#Connect.Paginator.ListRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListRules.html#Connect.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listrulespaginator)
        """

if TYPE_CHECKING:
    _ListSecurityKeysPaginatorBase = Paginator[ListSecurityKeysResponseTypeDef]
else:
    _ListSecurityKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListSecurityKeysPaginator(_ListSecurityKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityKeys.html#Connect.Paginator.ListSecurityKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecuritykeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListSecurityKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityKeys.html#Connect.Paginator.ListSecurityKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecuritykeyspaginator)
        """

if TYPE_CHECKING:
    _ListSecurityProfileApplicationsPaginatorBase = Paginator[
        ListSecurityProfileApplicationsResponseTypeDef
    ]
else:
    _ListSecurityProfileApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSecurityProfileApplicationsPaginator(_ListSecurityProfileApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityProfileApplications.html#Connect.Paginator.ListSecurityProfileApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecurityprofileapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityProfileApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSecurityProfileApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityProfileApplications.html#Connect.Paginator.ListSecurityProfileApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecurityprofileapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListSecurityProfilePermissionsPaginatorBase = Paginator[
        ListSecurityProfilePermissionsResponseTypeDef
    ]
else:
    _ListSecurityProfilePermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSecurityProfilePermissionsPaginator(_ListSecurityProfilePermissionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityProfilePermissions.html#Connect.Paginator.ListSecurityProfilePermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecurityprofilepermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityProfilePermissionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSecurityProfilePermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityProfilePermissions.html#Connect.Paginator.ListSecurityProfilePermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecurityprofilepermissionspaginator)
        """

if TYPE_CHECKING:
    _ListSecurityProfilesPaginatorBase = Paginator[ListSecurityProfilesResponseTypeDef]
else:
    _ListSecurityProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSecurityProfilesPaginator(_ListSecurityProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityProfiles.html#Connect.Paginator.ListSecurityProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecurityprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListSecurityProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListSecurityProfiles.html#Connect.Paginator.ListSecurityProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listsecurityprofilespaginator)
        """

if TYPE_CHECKING:
    _ListTaskTemplatesPaginatorBase = Paginator[ListTaskTemplatesResponseTypeDef]
else:
    _ListTaskTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTaskTemplatesPaginator(_ListTaskTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListTaskTemplates.html#Connect.Paginator.ListTaskTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listtasktemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTaskTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListTaskTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListTaskTemplates.html#Connect.Paginator.ListTaskTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listtasktemplatespaginator)
        """

if TYPE_CHECKING:
    _ListTrafficDistributionGroupUsersPaginatorBase = Paginator[
        ListTrafficDistributionGroupUsersResponseTypeDef
    ]
else:
    _ListTrafficDistributionGroupUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrafficDistributionGroupUsersPaginator(_ListTrafficDistributionGroupUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListTrafficDistributionGroupUsers.html#Connect.Paginator.ListTrafficDistributionGroupUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listtrafficdistributiongroupuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrafficDistributionGroupUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListTrafficDistributionGroupUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListTrafficDistributionGroupUsers.html#Connect.Paginator.ListTrafficDistributionGroupUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listtrafficdistributiongroupuserspaginator)
        """

if TYPE_CHECKING:
    _ListTrafficDistributionGroupsPaginatorBase = Paginator[
        ListTrafficDistributionGroupsResponseTypeDef
    ]
else:
    _ListTrafficDistributionGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrafficDistributionGroupsPaginator(_ListTrafficDistributionGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListTrafficDistributionGroups.html#Connect.Paginator.ListTrafficDistributionGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listtrafficdistributiongroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrafficDistributionGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListTrafficDistributionGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListTrafficDistributionGroups.html#Connect.Paginator.ListTrafficDistributionGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listtrafficdistributiongroupspaginator)
        """

if TYPE_CHECKING:
    _ListUseCasesPaginatorBase = Paginator[ListUseCasesResponseTypeDef]
else:
    _ListUseCasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListUseCasesPaginator(_ListUseCasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUseCases.html#Connect.Paginator.ListUseCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listusecasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUseCasesRequestPaginateTypeDef]
    ) -> PageIterator[ListUseCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUseCases.html#Connect.Paginator.ListUseCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listusecasespaginator)
        """

if TYPE_CHECKING:
    _ListUserHierarchyGroupsPaginatorBase = Paginator[ListUserHierarchyGroupsResponseTypeDef]
else:
    _ListUserHierarchyGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUserHierarchyGroupsPaginator(_ListUserHierarchyGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUserHierarchyGroups.html#Connect.Paginator.ListUserHierarchyGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listuserhierarchygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUserHierarchyGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListUserHierarchyGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUserHierarchyGroups.html#Connect.Paginator.ListUserHierarchyGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listuserhierarchygroupspaginator)
        """

if TYPE_CHECKING:
    _ListUserProficienciesPaginatorBase = Paginator[ListUserProficienciesResponseTypeDef]
else:
    _ListUserProficienciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListUserProficienciesPaginator(_ListUserProficienciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUserProficiencies.html#Connect.Paginator.ListUserProficiencies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listuserproficienciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUserProficienciesRequestPaginateTypeDef]
    ) -> PageIterator[ListUserProficienciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUserProficiencies.html#Connect.Paginator.ListUserProficiencies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listuserproficienciespaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUsers.html#Connect.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListUsers.html#Connect.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listuserspaginator)
        """

if TYPE_CHECKING:
    _ListViewVersionsPaginatorBase = Paginator[ListViewVersionsResponseTypeDef]
else:
    _ListViewVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListViewVersionsPaginator(_ListViewVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListViewVersions.html#Connect.Paginator.ListViewVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listviewversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListViewVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListViewVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListViewVersions.html#Connect.Paginator.ListViewVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listviewversionspaginator)
        """

if TYPE_CHECKING:
    _ListViewsPaginatorBase = Paginator[ListViewsResponseTypeDef]
else:
    _ListViewsPaginatorBase = Paginator  # type: ignore[assignment]

class ListViewsPaginator(_ListViewsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListViews.html#Connect.Paginator.ListViews)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listviewspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListViewsRequestPaginateTypeDef]
    ) -> PageIterator[ListViewsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListViews.html#Connect.Paginator.ListViews.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listviewspaginator)
        """

if TYPE_CHECKING:
    _ListWorkspacePagesPaginatorBase = Paginator[ListWorkspacePagesResponseTypeDef]
else:
    _ListWorkspacePagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkspacePagesPaginator(_ListWorkspacePagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListWorkspacePages.html#Connect.Paginator.ListWorkspacePages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listworkspacepagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkspacePagesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkspacePagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListWorkspacePages.html#Connect.Paginator.ListWorkspacePages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listworkspacepagespaginator)
        """

if TYPE_CHECKING:
    _ListWorkspacesPaginatorBase = Paginator[ListWorkspacesResponseTypeDef]
else:
    _ListWorkspacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkspacesPaginator(_ListWorkspacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListWorkspaces.html#Connect.Paginator.ListWorkspaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listworkspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkspacesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/ListWorkspaces.html#Connect.Paginator.ListWorkspaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#listworkspacespaginator)
        """

if TYPE_CHECKING:
    _SearchAgentStatusesPaginatorBase = Paginator[SearchAgentStatusesResponseTypeDef]
else:
    _SearchAgentStatusesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchAgentStatusesPaginator(_SearchAgentStatusesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchAgentStatuses.html#Connect.Paginator.SearchAgentStatuses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchagentstatusespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchAgentStatusesRequestPaginateTypeDef]
    ) -> PageIterator[SearchAgentStatusesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchAgentStatuses.html#Connect.Paginator.SearchAgentStatuses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchagentstatusespaginator)
        """

if TYPE_CHECKING:
    _SearchAvailablePhoneNumbersPaginatorBase = Paginator[
        SearchAvailablePhoneNumbersResponseTypeDef
    ]
else:
    _SearchAvailablePhoneNumbersPaginatorBase = Paginator  # type: ignore[assignment]

class SearchAvailablePhoneNumbersPaginator(_SearchAvailablePhoneNumbersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchAvailablePhoneNumbers.html#Connect.Paginator.SearchAvailablePhoneNumbers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchavailablephonenumberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchAvailablePhoneNumbersRequestPaginateTypeDef]
    ) -> PageIterator[SearchAvailablePhoneNumbersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchAvailablePhoneNumbers.html#Connect.Paginator.SearchAvailablePhoneNumbers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchavailablephonenumberspaginator)
        """

if TYPE_CHECKING:
    _SearchContactFlowModulesPaginatorBase = Paginator[SearchContactFlowModulesResponseTypeDef]
else:
    _SearchContactFlowModulesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchContactFlowModulesPaginator(_SearchContactFlowModulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchContactFlowModules.html#Connect.Paginator.SearchContactFlowModules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchcontactflowmodulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchContactFlowModulesRequestPaginateTypeDef]
    ) -> PageIterator[SearchContactFlowModulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchContactFlowModules.html#Connect.Paginator.SearchContactFlowModules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchcontactflowmodulespaginator)
        """

if TYPE_CHECKING:
    _SearchContactFlowsPaginatorBase = Paginator[SearchContactFlowsResponseTypeDef]
else:
    _SearchContactFlowsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchContactFlowsPaginator(_SearchContactFlowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchContactFlows.html#Connect.Paginator.SearchContactFlows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchcontactflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchContactFlowsRequestPaginateTypeDef]
    ) -> PageIterator[SearchContactFlowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchContactFlows.html#Connect.Paginator.SearchContactFlows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchcontactflowspaginator)
        """

if TYPE_CHECKING:
    _SearchContactsPaginatorBase = Paginator[SearchContactsResponsePaginatorTypeDef]
else:
    _SearchContactsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchContactsPaginator(_SearchContactsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchContacts.html#Connect.Paginator.SearchContacts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchcontactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchContactsRequestPaginateTypeDef]
    ) -> PageIterator[SearchContactsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchContacts.html#Connect.Paginator.SearchContacts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchcontactspaginator)
        """

if TYPE_CHECKING:
    _SearchDataTablesPaginatorBase = Paginator[SearchDataTablesResponseTypeDef]
else:
    _SearchDataTablesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchDataTablesPaginator(_SearchDataTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchDataTables.html#Connect.Paginator.SearchDataTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchdatatablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchDataTablesRequestPaginateTypeDef]
    ) -> PageIterator[SearchDataTablesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchDataTables.html#Connect.Paginator.SearchDataTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchdatatablespaginator)
        """

if TYPE_CHECKING:
    _SearchHoursOfOperationOverridesPaginatorBase = Paginator[
        SearchHoursOfOperationOverridesResponseTypeDef
    ]
else:
    _SearchHoursOfOperationOverridesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchHoursOfOperationOverridesPaginator(_SearchHoursOfOperationOverridesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchHoursOfOperationOverrides.html#Connect.Paginator.SearchHoursOfOperationOverrides)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchhoursofoperationoverridespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchHoursOfOperationOverridesRequestPaginateTypeDef]
    ) -> PageIterator[SearchHoursOfOperationOverridesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchHoursOfOperationOverrides.html#Connect.Paginator.SearchHoursOfOperationOverrides.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchhoursofoperationoverridespaginator)
        """

if TYPE_CHECKING:
    _SearchHoursOfOperationsPaginatorBase = Paginator[SearchHoursOfOperationsResponseTypeDef]
else:
    _SearchHoursOfOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchHoursOfOperationsPaginator(_SearchHoursOfOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchHoursOfOperations.html#Connect.Paginator.SearchHoursOfOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchhoursofoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchHoursOfOperationsRequestPaginateTypeDef]
    ) -> PageIterator[SearchHoursOfOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchHoursOfOperations.html#Connect.Paginator.SearchHoursOfOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchhoursofoperationspaginator)
        """

if TYPE_CHECKING:
    _SearchPredefinedAttributesPaginatorBase = Paginator[SearchPredefinedAttributesResponseTypeDef]
else:
    _SearchPredefinedAttributesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchPredefinedAttributesPaginator(_SearchPredefinedAttributesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchPredefinedAttributes.html#Connect.Paginator.SearchPredefinedAttributes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchpredefinedattributespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchPredefinedAttributesRequestPaginateTypeDef]
    ) -> PageIterator[SearchPredefinedAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchPredefinedAttributes.html#Connect.Paginator.SearchPredefinedAttributes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchpredefinedattributespaginator)
        """

if TYPE_CHECKING:
    _SearchPromptsPaginatorBase = Paginator[SearchPromptsResponseTypeDef]
else:
    _SearchPromptsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchPromptsPaginator(_SearchPromptsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchPrompts.html#Connect.Paginator.SearchPrompts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchpromptspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchPromptsRequestPaginateTypeDef]
    ) -> PageIterator[SearchPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchPrompts.html#Connect.Paginator.SearchPrompts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchpromptspaginator)
        """

if TYPE_CHECKING:
    _SearchQueuesPaginatorBase = Paginator[SearchQueuesResponseTypeDef]
else:
    _SearchQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchQueuesPaginator(_SearchQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchQueues.html#Connect.Paginator.SearchQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchQueuesRequestPaginateTypeDef]
    ) -> PageIterator[SearchQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchQueues.html#Connect.Paginator.SearchQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchqueuespaginator)
        """

if TYPE_CHECKING:
    _SearchQuickConnectsPaginatorBase = Paginator[SearchQuickConnectsResponseTypeDef]
else:
    _SearchQuickConnectsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchQuickConnectsPaginator(_SearchQuickConnectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchQuickConnects.html#Connect.Paginator.SearchQuickConnects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchquickconnectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchQuickConnectsRequestPaginateTypeDef]
    ) -> PageIterator[SearchQuickConnectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchQuickConnects.html#Connect.Paginator.SearchQuickConnects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchquickconnectspaginator)
        """

if TYPE_CHECKING:
    _SearchResourceTagsPaginatorBase = Paginator[SearchResourceTagsResponseTypeDef]
else:
    _SearchResourceTagsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchResourceTagsPaginator(_SearchResourceTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchResourceTags.html#Connect.Paginator.SearchResourceTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchresourcetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchResourceTagsRequestPaginateTypeDef]
    ) -> PageIterator[SearchResourceTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchResourceTags.html#Connect.Paginator.SearchResourceTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchresourcetagspaginator)
        """

if TYPE_CHECKING:
    _SearchRoutingProfilesPaginatorBase = Paginator[SearchRoutingProfilesResponseTypeDef]
else:
    _SearchRoutingProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchRoutingProfilesPaginator(_SearchRoutingProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchRoutingProfiles.html#Connect.Paginator.SearchRoutingProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchroutingprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchRoutingProfilesRequestPaginateTypeDef]
    ) -> PageIterator[SearchRoutingProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchRoutingProfiles.html#Connect.Paginator.SearchRoutingProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchroutingprofilespaginator)
        """

if TYPE_CHECKING:
    _SearchSecurityProfilesPaginatorBase = Paginator[SearchSecurityProfilesResponseTypeDef]
else:
    _SearchSecurityProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchSecurityProfilesPaginator(_SearchSecurityProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchSecurityProfiles.html#Connect.Paginator.SearchSecurityProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchsecurityprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchSecurityProfilesRequestPaginateTypeDef]
    ) -> PageIterator[SearchSecurityProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchSecurityProfiles.html#Connect.Paginator.SearchSecurityProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchsecurityprofilespaginator)
        """

if TYPE_CHECKING:
    _SearchUserHierarchyGroupsPaginatorBase = Paginator[SearchUserHierarchyGroupsResponseTypeDef]
else:
    _SearchUserHierarchyGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchUserHierarchyGroupsPaginator(_SearchUserHierarchyGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchUserHierarchyGroups.html#Connect.Paginator.SearchUserHierarchyGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchuserhierarchygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchUserHierarchyGroupsRequestPaginateTypeDef]
    ) -> PageIterator[SearchUserHierarchyGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchUserHierarchyGroups.html#Connect.Paginator.SearchUserHierarchyGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchuserhierarchygroupspaginator)
        """

if TYPE_CHECKING:
    _SearchUsersPaginatorBase = Paginator[SearchUsersResponseTypeDef]
else:
    _SearchUsersPaginatorBase = Paginator  # type: ignore[assignment]

class SearchUsersPaginator(_SearchUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchUsers.html#Connect.Paginator.SearchUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchUsersRequestPaginateTypeDef]
    ) -> PageIterator[SearchUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchUsers.html#Connect.Paginator.SearchUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchuserspaginator)
        """

if TYPE_CHECKING:
    _SearchViewsPaginatorBase = Paginator[SearchViewsResponseTypeDef]
else:
    _SearchViewsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchViewsPaginator(_SearchViewsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchViews.html#Connect.Paginator.SearchViews)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchviewspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchViewsRequestPaginateTypeDef]
    ) -> PageIterator[SearchViewsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchViews.html#Connect.Paginator.SearchViews.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchviewspaginator)
        """

if TYPE_CHECKING:
    _SearchVocabulariesPaginatorBase = Paginator[SearchVocabulariesResponseTypeDef]
else:
    _SearchVocabulariesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchVocabulariesPaginator(_SearchVocabulariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchVocabularies.html#Connect.Paginator.SearchVocabularies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchvocabulariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchVocabulariesRequestPaginateTypeDef]
    ) -> PageIterator[SearchVocabulariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchVocabularies.html#Connect.Paginator.SearchVocabularies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchvocabulariespaginator)
        """

if TYPE_CHECKING:
    _SearchWorkspaceAssociationsPaginatorBase = Paginator[
        SearchWorkspaceAssociationsResponseTypeDef
    ]
else:
    _SearchWorkspaceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchWorkspaceAssociationsPaginator(_SearchWorkspaceAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchWorkspaceAssociations.html#Connect.Paginator.SearchWorkspaceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchworkspaceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchWorkspaceAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[SearchWorkspaceAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchWorkspaceAssociations.html#Connect.Paginator.SearchWorkspaceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchworkspaceassociationspaginator)
        """

if TYPE_CHECKING:
    _SearchWorkspacesPaginatorBase = Paginator[SearchWorkspacesResponseTypeDef]
else:
    _SearchWorkspacesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchWorkspacesPaginator(_SearchWorkspacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchWorkspaces.html#Connect.Paginator.SearchWorkspaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchworkspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchWorkspacesRequestPaginateTypeDef]
    ) -> PageIterator[SearchWorkspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/paginator/SearchWorkspaces.html#Connect.Paginator.SearchWorkspaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators/#searchworkspacespaginator)
        """
