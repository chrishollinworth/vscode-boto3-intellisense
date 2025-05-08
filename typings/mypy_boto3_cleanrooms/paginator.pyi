"""
Type annotations for cleanrooms service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cleanrooms.client import CleanRoomsServiceClient
    from mypy_boto3_cleanrooms.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAnalysisTemplatesInputPaginateTypeDef,
    ListAnalysisTemplatesOutputTypeDef,
    ListCollaborationAnalysisTemplatesInputPaginateTypeDef,
    ListCollaborationAnalysisTemplatesOutputTypeDef,
    ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef,
    ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef,
    ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef,
    ListCollaborationIdNamespaceAssociationsOutputTypeDef,
    ListCollaborationPrivacyBudgetsInputPaginateTypeDef,
    ListCollaborationPrivacyBudgetsOutputTypeDef,
    ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef,
    ListCollaborationPrivacyBudgetTemplatesOutputTypeDef,
    ListCollaborationsInputPaginateTypeDef,
    ListCollaborationsOutputTypeDef,
    ListConfiguredAudienceModelAssociationsInputPaginateTypeDef,
    ListConfiguredAudienceModelAssociationsOutputTypeDef,
    ListConfiguredTableAssociationsInputPaginateTypeDef,
    ListConfiguredTableAssociationsOutputTypeDef,
    ListConfiguredTablesInputPaginateTypeDef,
    ListConfiguredTablesOutputTypeDef,
    ListIdMappingTablesInputPaginateTypeDef,
    ListIdMappingTablesOutputTypeDef,
    ListIdNamespaceAssociationsInputPaginateTypeDef,
    ListIdNamespaceAssociationsOutputTypeDef,
    ListMembershipsInputPaginateTypeDef,
    ListMembershipsOutputTypeDef,
    ListMembersInputPaginateTypeDef,
    ListMembersOutputTypeDef,
    ListPrivacyBudgetsInputPaginateTypeDef,
    ListPrivacyBudgetsOutputTypeDef,
    ListPrivacyBudgetTemplatesInputPaginateTypeDef,
    ListPrivacyBudgetTemplatesOutputTypeDef,
    ListProtectedJobsInputPaginateTypeDef,
    ListProtectedJobsOutputTypeDef,
    ListProtectedQueriesInputPaginateTypeDef,
    ListProtectedQueriesOutputTypeDef,
    ListSchemasInputPaginateTypeDef,
    ListSchemasOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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

if TYPE_CHECKING:
    _ListAnalysisTemplatesPaginatorBase = Paginator[ListAnalysisTemplatesOutputTypeDef]
else:
    _ListAnalysisTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnalysisTemplatesPaginator(_ListAnalysisTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListAnalysisTemplates.html#CleanRoomsService.Paginator.ListAnalysisTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listanalysistemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnalysisTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListAnalysisTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListAnalysisTemplates.html#CleanRoomsService.Paginator.ListAnalysisTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listanalysistemplatespaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationAnalysisTemplatesPaginatorBase = Paginator[
        ListCollaborationAnalysisTemplatesOutputTypeDef
    ]
else:
    _ListCollaborationAnalysisTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationAnalysisTemplatesPaginator(_ListCollaborationAnalysisTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationAnalysisTemplates.html#CleanRoomsService.Paginator.ListCollaborationAnalysisTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationanalysistemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationAnalysisTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListCollaborationAnalysisTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationAnalysisTemplates.html#CleanRoomsService.Paginator.ListCollaborationAnalysisTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationanalysistemplatespaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationConfiguredAudienceModelAssociationsPaginatorBase = Paginator[
        ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef
    ]
else:
    _ListCollaborationConfiguredAudienceModelAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationConfiguredAudienceModelAssociationsPaginator(
    _ListCollaborationConfiguredAudienceModelAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationConfiguredAudienceModelAssociations.html#CleanRoomsService.Paginator.ListCollaborationConfiguredAudienceModelAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationconfiguredaudiencemodelassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef],
    ) -> PageIterator[ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationConfiguredAudienceModelAssociations.html#CleanRoomsService.Paginator.ListCollaborationConfiguredAudienceModelAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationconfiguredaudiencemodelassociationspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationIdNamespaceAssociationsPaginatorBase = Paginator[
        ListCollaborationIdNamespaceAssociationsOutputTypeDef
    ]
else:
    _ListCollaborationIdNamespaceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationIdNamespaceAssociationsPaginator(
    _ListCollaborationIdNamespaceAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationIdNamespaceAssociations.html#CleanRoomsService.Paginator.ListCollaborationIdNamespaceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationidnamespaceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef]
    ) -> PageIterator[ListCollaborationIdNamespaceAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationIdNamespaceAssociations.html#CleanRoomsService.Paginator.ListCollaborationIdNamespaceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationidnamespaceassociationspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationPrivacyBudgetTemplatesPaginatorBase = Paginator[
        ListCollaborationPrivacyBudgetTemplatesOutputTypeDef
    ]
else:
    _ListCollaborationPrivacyBudgetTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationPrivacyBudgetTemplatesPaginator(
    _ListCollaborationPrivacyBudgetTemplatesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationPrivacyBudgetTemplates.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgetTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationprivacybudgettemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListCollaborationPrivacyBudgetTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationPrivacyBudgetTemplates.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgetTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationprivacybudgettemplatespaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationPrivacyBudgetsPaginatorBase = Paginator[
        ListCollaborationPrivacyBudgetsOutputTypeDef
    ]
else:
    _ListCollaborationPrivacyBudgetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationPrivacyBudgetsPaginator(_ListCollaborationPrivacyBudgetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationPrivacyBudgets.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationprivacybudgetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationPrivacyBudgetsInputPaginateTypeDef]
    ) -> PageIterator[ListCollaborationPrivacyBudgetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborationPrivacyBudgets.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationprivacybudgetspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationsPaginatorBase = Paginator[ListCollaborationsOutputTypeDef]
else:
    _ListCollaborationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationsPaginator(_ListCollaborationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborations.html#CleanRoomsService.Paginator.ListCollaborations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationsInputPaginateTypeDef]
    ) -> PageIterator[ListCollaborationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListCollaborations.html#CleanRoomsService.Paginator.ListCollaborations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listcollaborationspaginator)
        """

if TYPE_CHECKING:
    _ListConfiguredAudienceModelAssociationsPaginatorBase = Paginator[
        ListConfiguredAudienceModelAssociationsOutputTypeDef
    ]
else:
    _ListConfiguredAudienceModelAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfiguredAudienceModelAssociationsPaginator(
    _ListConfiguredAudienceModelAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListConfiguredAudienceModelAssociations.html#CleanRoomsService.Paginator.ListConfiguredAudienceModelAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listconfiguredaudiencemodelassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfiguredAudienceModelAssociationsInputPaginateTypeDef]
    ) -> PageIterator[ListConfiguredAudienceModelAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListConfiguredAudienceModelAssociations.html#CleanRoomsService.Paginator.ListConfiguredAudienceModelAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listconfiguredaudiencemodelassociationspaginator)
        """

if TYPE_CHECKING:
    _ListConfiguredTableAssociationsPaginatorBase = Paginator[
        ListConfiguredTableAssociationsOutputTypeDef
    ]
else:
    _ListConfiguredTableAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfiguredTableAssociationsPaginator(_ListConfiguredTableAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListConfiguredTableAssociations.html#CleanRoomsService.Paginator.ListConfiguredTableAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listconfiguredtableassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfiguredTableAssociationsInputPaginateTypeDef]
    ) -> PageIterator[ListConfiguredTableAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListConfiguredTableAssociations.html#CleanRoomsService.Paginator.ListConfiguredTableAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listconfiguredtableassociationspaginator)
        """

if TYPE_CHECKING:
    _ListConfiguredTablesPaginatorBase = Paginator[ListConfiguredTablesOutputTypeDef]
else:
    _ListConfiguredTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfiguredTablesPaginator(_ListConfiguredTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListConfiguredTables.html#CleanRoomsService.Paginator.ListConfiguredTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listconfiguredtablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfiguredTablesInputPaginateTypeDef]
    ) -> PageIterator[ListConfiguredTablesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListConfiguredTables.html#CleanRoomsService.Paginator.ListConfiguredTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listconfiguredtablespaginator)
        """

if TYPE_CHECKING:
    _ListIdMappingTablesPaginatorBase = Paginator[ListIdMappingTablesOutputTypeDef]
else:
    _ListIdMappingTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdMappingTablesPaginator(_ListIdMappingTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListIdMappingTables.html#CleanRoomsService.Paginator.ListIdMappingTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listidmappingtablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdMappingTablesInputPaginateTypeDef]
    ) -> PageIterator[ListIdMappingTablesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListIdMappingTables.html#CleanRoomsService.Paginator.ListIdMappingTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listidmappingtablespaginator)
        """

if TYPE_CHECKING:
    _ListIdNamespaceAssociationsPaginatorBase = Paginator[ListIdNamespaceAssociationsOutputTypeDef]
else:
    _ListIdNamespaceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdNamespaceAssociationsPaginator(_ListIdNamespaceAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListIdNamespaceAssociations.html#CleanRoomsService.Paginator.ListIdNamespaceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listidnamespaceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdNamespaceAssociationsInputPaginateTypeDef]
    ) -> PageIterator[ListIdNamespaceAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListIdNamespaceAssociations.html#CleanRoomsService.Paginator.ListIdNamespaceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listidnamespaceassociationspaginator)
        """

if TYPE_CHECKING:
    _ListMembersPaginatorBase = Paginator[ListMembersOutputTypeDef]
else:
    _ListMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListMembersPaginator(_ListMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListMembers.html#CleanRoomsService.Paginator.ListMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMembersInputPaginateTypeDef]
    ) -> PageIterator[ListMembersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListMembers.html#CleanRoomsService.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listmemberspaginator)
        """

if TYPE_CHECKING:
    _ListMembershipsPaginatorBase = Paginator[ListMembershipsOutputTypeDef]
else:
    _ListMembershipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMembershipsPaginator(_ListMembershipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListMemberships.html#CleanRoomsService.Paginator.ListMemberships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listmembershipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMembershipsInputPaginateTypeDef]
    ) -> PageIterator[ListMembershipsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListMemberships.html#CleanRoomsService.Paginator.ListMemberships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listmembershipspaginator)
        """

if TYPE_CHECKING:
    _ListPrivacyBudgetTemplatesPaginatorBase = Paginator[ListPrivacyBudgetTemplatesOutputTypeDef]
else:
    _ListPrivacyBudgetTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPrivacyBudgetTemplatesPaginator(_ListPrivacyBudgetTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListPrivacyBudgetTemplates.html#CleanRoomsService.Paginator.ListPrivacyBudgetTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprivacybudgettemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPrivacyBudgetTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListPrivacyBudgetTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListPrivacyBudgetTemplates.html#CleanRoomsService.Paginator.ListPrivacyBudgetTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprivacybudgettemplatespaginator)
        """

if TYPE_CHECKING:
    _ListPrivacyBudgetsPaginatorBase = Paginator[ListPrivacyBudgetsOutputTypeDef]
else:
    _ListPrivacyBudgetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPrivacyBudgetsPaginator(_ListPrivacyBudgetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListPrivacyBudgets.html#CleanRoomsService.Paginator.ListPrivacyBudgets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprivacybudgetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPrivacyBudgetsInputPaginateTypeDef]
    ) -> PageIterator[ListPrivacyBudgetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListPrivacyBudgets.html#CleanRoomsService.Paginator.ListPrivacyBudgets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprivacybudgetspaginator)
        """

if TYPE_CHECKING:
    _ListProtectedJobsPaginatorBase = Paginator[ListProtectedJobsOutputTypeDef]
else:
    _ListProtectedJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProtectedJobsPaginator(_ListProtectedJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListProtectedJobs.html#CleanRoomsService.Paginator.ListProtectedJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprotectedjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProtectedJobsInputPaginateTypeDef]
    ) -> PageIterator[ListProtectedJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListProtectedJobs.html#CleanRoomsService.Paginator.ListProtectedJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprotectedjobspaginator)
        """

if TYPE_CHECKING:
    _ListProtectedQueriesPaginatorBase = Paginator[ListProtectedQueriesOutputTypeDef]
else:
    _ListProtectedQueriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProtectedQueriesPaginator(_ListProtectedQueriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListProtectedQueries.html#CleanRoomsService.Paginator.ListProtectedQueries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprotectedqueriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProtectedQueriesInputPaginateTypeDef]
    ) -> PageIterator[ListProtectedQueriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListProtectedQueries.html#CleanRoomsService.Paginator.ListProtectedQueries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listprotectedqueriespaginator)
        """

if TYPE_CHECKING:
    _ListSchemasPaginatorBase = Paginator[ListSchemasOutputTypeDef]
else:
    _ListSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemasPaginator(_ListSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListSchemas.html#CleanRoomsService.Paginator.ListSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemasInputPaginateTypeDef]
    ) -> PageIterator[ListSchemasOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/paginator/ListSchemas.html#CleanRoomsService.Paginator.ListSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators/#listschemaspaginator)
        """
