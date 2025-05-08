"""
Main interface for cleanrooms service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cleanrooms import (
        CleanRoomsServiceClient,
        Client,
        ListAnalysisTemplatesPaginator,
        ListCollaborationAnalysisTemplatesPaginator,
        ListCollaborationConfiguredAudienceModelAssociationsPaginator,
        ListCollaborationIdNamespaceAssociationsPaginator,
        ListCollaborationPrivacyBudgetTemplatesPaginator,
        ListCollaborationPrivacyBudgetsPaginator,
        ListCollaborationsPaginator,
        ListConfiguredAudienceModelAssociationsPaginator,
        ListConfiguredTableAssociationsPaginator,
        ListConfiguredTablesPaginator,
        ListIdMappingTablesPaginator,
        ListIdNamespaceAssociationsPaginator,
        ListMembersPaginator,
        ListMembershipsPaginator,
        ListPrivacyBudgetTemplatesPaginator,
        ListPrivacyBudgetsPaginator,
        ListProtectedJobsPaginator,
        ListProtectedQueriesPaginator,
        ListSchemasPaginator,
    )

    session = Session()
    client: CleanRoomsServiceClient = session.client("cleanrooms")

    list_analysis_templates_paginator: ListAnalysisTemplatesPaginator = client.get_paginator("list_analysis_templates")
    list_collaboration_analysis_templates_paginator: ListCollaborationAnalysisTemplatesPaginator = client.get_paginator("list_collaboration_analysis_templates")
    list_collaboration_configured_audience_model_associations_paginator: ListCollaborationConfiguredAudienceModelAssociationsPaginator = client.get_paginator("list_collaboration_configured_audience_model_associations")
    list_collaboration_id_namespace_associations_paginator: ListCollaborationIdNamespaceAssociationsPaginator = client.get_paginator("list_collaboration_id_namespace_associations")
    list_collaboration_privacy_budget_templates_paginator: ListCollaborationPrivacyBudgetTemplatesPaginator = client.get_paginator("list_collaboration_privacy_budget_templates")
    list_collaboration_privacy_budgets_paginator: ListCollaborationPrivacyBudgetsPaginator = client.get_paginator("list_collaboration_privacy_budgets")
    list_collaborations_paginator: ListCollaborationsPaginator = client.get_paginator("list_collaborations")
    list_configured_audience_model_associations_paginator: ListConfiguredAudienceModelAssociationsPaginator = client.get_paginator("list_configured_audience_model_associations")
    list_configured_table_associations_paginator: ListConfiguredTableAssociationsPaginator = client.get_paginator("list_configured_table_associations")
    list_configured_tables_paginator: ListConfiguredTablesPaginator = client.get_paginator("list_configured_tables")
    list_id_mapping_tables_paginator: ListIdMappingTablesPaginator = client.get_paginator("list_id_mapping_tables")
    list_id_namespace_associations_paginator: ListIdNamespaceAssociationsPaginator = client.get_paginator("list_id_namespace_associations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_memberships_paginator: ListMembershipsPaginator = client.get_paginator("list_memberships")
    list_privacy_budget_templates_paginator: ListPrivacyBudgetTemplatesPaginator = client.get_paginator("list_privacy_budget_templates")
    list_privacy_budgets_paginator: ListPrivacyBudgetsPaginator = client.get_paginator("list_privacy_budgets")
    list_protected_jobs_paginator: ListProtectedJobsPaginator = client.get_paginator("list_protected_jobs")
    list_protected_queries_paginator: ListProtectedQueriesPaginator = client.get_paginator("list_protected_queries")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    ```
"""

from .client import CleanRoomsServiceClient
from .paginator import (
    ListAnalysisTemplatesPaginator,
    ListCollaborationAnalysisTemplatesPaginator,
    ListCollaborationConfiguredAudienceModelAssociationsPaginator,
    ListCollaborationIdNamespaceAssociationsPaginator,
    ListCollaborationPrivacyBudgetsPaginator,
    ListCollaborationPrivacyBudgetTemplatesPaginator,
    ListCollaborationsPaginator,
    ListConfiguredAudienceModelAssociationsPaginator,
    ListConfiguredTableAssociationsPaginator,
    ListConfiguredTablesPaginator,
    ListIdMappingTablesPaginator,
    ListIdNamespaceAssociationsPaginator,
    ListMembershipsPaginator,
    ListMembersPaginator,
    ListPrivacyBudgetsPaginator,
    ListPrivacyBudgetTemplatesPaginator,
    ListProtectedJobsPaginator,
    ListProtectedQueriesPaginator,
    ListSchemasPaginator,
)

Client = CleanRoomsServiceClient

__all__ = (
    "CleanRoomsServiceClient",
    "Client",
    "ListAnalysisTemplatesPaginator",
    "ListCollaborationAnalysisTemplatesPaginator",
    "ListCollaborationConfiguredAudienceModelAssociationsPaginator",
    "ListCollaborationIdNamespaceAssociationsPaginator",
    "ListCollaborationPrivacyBudgetTemplatesPaginator",
    "ListCollaborationPrivacyBudgetsPaginator",
    "ListCollaborationsPaginator",
    "ListConfiguredAudienceModelAssociationsPaginator",
    "ListConfiguredTableAssociationsPaginator",
    "ListConfiguredTablesPaginator",
    "ListIdMappingTablesPaginator",
    "ListIdNamespaceAssociationsPaginator",
    "ListMembersPaginator",
    "ListMembershipsPaginator",
    "ListPrivacyBudgetTemplatesPaginator",
    "ListPrivacyBudgetsPaginator",
    "ListProtectedJobsPaginator",
    "ListProtectedQueriesPaginator",
    "ListSchemasPaginator",
)
