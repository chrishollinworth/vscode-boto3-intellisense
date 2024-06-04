"""
Type annotations for cleanrooms service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cleanrooms import CleanRoomsServiceClient
    from mypy_boto3_cleanrooms.paginator import (
        ListAnalysisTemplatesPaginator,
        ListCollaborationAnalysisTemplatesPaginator,
        ListCollaborationConfiguredAudienceModelAssociationsPaginator,
        ListCollaborationPrivacyBudgetTemplatesPaginator,
        ListCollaborationPrivacyBudgetsPaginator,
        ListCollaborationsPaginator,
        ListConfiguredAudienceModelAssociationsPaginator,
        ListConfiguredTableAssociationsPaginator,
        ListConfiguredTablesPaginator,
        ListMembersPaginator,
        ListMembershipsPaginator,
        ListPrivacyBudgetTemplatesPaginator,
        ListPrivacyBudgetsPaginator,
        ListProtectedQueriesPaginator,
        ListSchemasPaginator,
    )

    client: CleanRoomsServiceClient = boto3.client("cleanrooms")

    list_analysis_templates_paginator: ListAnalysisTemplatesPaginator = client.get_paginator("list_analysis_templates")
    list_collaboration_analysis_templates_paginator: ListCollaborationAnalysisTemplatesPaginator = client.get_paginator("list_collaboration_analysis_templates")
    list_collaboration_configured_audience_model_associations_paginator: ListCollaborationConfiguredAudienceModelAssociationsPaginator = client.get_paginator("list_collaboration_configured_audience_model_associations")
    list_collaboration_privacy_budget_templates_paginator: ListCollaborationPrivacyBudgetTemplatesPaginator = client.get_paginator("list_collaboration_privacy_budget_templates")
    list_collaboration_privacy_budgets_paginator: ListCollaborationPrivacyBudgetsPaginator = client.get_paginator("list_collaboration_privacy_budgets")
    list_collaborations_paginator: ListCollaborationsPaginator = client.get_paginator("list_collaborations")
    list_configured_audience_model_associations_paginator: ListConfiguredAudienceModelAssociationsPaginator = client.get_paginator("list_configured_audience_model_associations")
    list_configured_table_associations_paginator: ListConfiguredTableAssociationsPaginator = client.get_paginator("list_configured_table_associations")
    list_configured_tables_paginator: ListConfiguredTablesPaginator = client.get_paginator("list_configured_tables")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_memberships_paginator: ListMembershipsPaginator = client.get_paginator("list_memberships")
    list_privacy_budget_templates_paginator: ListPrivacyBudgetTemplatesPaginator = client.get_paginator("list_privacy_budget_templates")
    list_privacy_budgets_paginator: ListPrivacyBudgetsPaginator = client.get_paginator("list_privacy_budgets")
    list_protected_queries_paginator: ListProtectedQueriesPaginator = client.get_paginator("list_protected_queries")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    ```
"""

import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import FilterableMemberStatusType, MembershipStatusType, ProtectedQueryStatusType
from .type_defs import (
    ListAnalysisTemplatesOutputTypeDef,
    ListCollaborationAnalysisTemplatesOutputTypeDef,
    ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef,
    ListCollaborationPrivacyBudgetsOutputTypeDef,
    ListCollaborationPrivacyBudgetTemplatesOutputTypeDef,
    ListCollaborationsOutputTypeDef,
    ListConfiguredAudienceModelAssociationsOutputTypeDef,
    ListConfiguredTableAssociationsOutputTypeDef,
    ListConfiguredTablesOutputTypeDef,
    ListMembershipsOutputTypeDef,
    ListMembersOutputTypeDef,
    ListPrivacyBudgetsOutputTypeDef,
    ListPrivacyBudgetTemplatesOutputTypeDef,
    ListProtectedQueriesOutputTypeDef,
    ListSchemasOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListAnalysisTemplatesPaginator",
    "ListCollaborationAnalysisTemplatesPaginator",
    "ListCollaborationConfiguredAudienceModelAssociationsPaginator",
    "ListCollaborationPrivacyBudgetTemplatesPaginator",
    "ListCollaborationPrivacyBudgetsPaginator",
    "ListCollaborationsPaginator",
    "ListConfiguredAudienceModelAssociationsPaginator",
    "ListConfiguredTableAssociationsPaginator",
    "ListConfiguredTablesPaginator",
    "ListMembersPaginator",
    "ListMembershipsPaginator",
    "ListPrivacyBudgetTemplatesPaginator",
    "ListPrivacyBudgetsPaginator",
    "ListProtectedQueriesPaginator",
    "ListSchemasPaginator",
)

class ListAnalysisTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListAnalysisTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listanalysistemplatespaginator)
    """

    def paginate(
        self, *, membershipIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalysisTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListAnalysisTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listanalysistemplatespaginator)
        """

class ListCollaborationAnalysisTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationAnalysisTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationanalysistemplatespaginator)
    """

    def paginate(
        self, *, collaborationIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollaborationAnalysisTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationAnalysisTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationanalysistemplatespaginator)
        """

class ListCollaborationConfiguredAudienceModelAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationConfiguredAudienceModelAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationconfiguredaudiencemodelassociationspaginator)
    """

    def paginate(
        self, *, collaborationIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationConfiguredAudienceModelAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationconfiguredaudiencemodelassociationspaginator)
        """

class ListCollaborationPrivacyBudgetTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgetTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationprivacybudgettemplatespaginator)
    """

    def paginate(
        self, *, collaborationIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollaborationPrivacyBudgetTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgetTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationprivacybudgettemplatespaginator)
        """

class ListCollaborationPrivacyBudgetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationprivacybudgetspaginator)
    """

    def paginate(
        self,
        *,
        collaborationIdentifier: str,
        privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollaborationPrivacyBudgetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationprivacybudgetspaginator)
        """

class ListCollaborationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationspaginator)
    """

    def paginate(
        self,
        *,
        memberStatus: FilterableMemberStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollaborationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationspaginator)
        """

class ListConfiguredAudienceModelAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredAudienceModelAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredaudiencemodelassociationspaginator)
    """

    def paginate(
        self, *, membershipIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfiguredAudienceModelAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredAudienceModelAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredaudiencemodelassociationspaginator)
        """

class ListConfiguredTableAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredTableAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredtableassociationspaginator)
    """

    def paginate(
        self, *, membershipIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfiguredTableAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredTableAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredtableassociationspaginator)
        """

class ListConfiguredTablesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredTables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredtablespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfiguredTablesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredTables.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredtablespaginator)
        """

class ListMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listmemberspaginator)
    """

    def paginate(
        self, *, collaborationIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listmemberspaginator)
        """

class ListMembershipsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListMemberships)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listmembershipspaginator)
    """

    def paginate(
        self,
        *,
        status: MembershipStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembershipsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListMemberships.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listmembershipspaginator)
        """

class ListPrivacyBudgetTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListPrivacyBudgetTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprivacybudgettemplatespaginator)
    """

    def paginate(
        self, *, membershipIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrivacyBudgetTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListPrivacyBudgetTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprivacybudgettemplatespaginator)
        """

class ListPrivacyBudgetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListPrivacyBudgets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprivacybudgetspaginator)
    """

    def paginate(
        self,
        *,
        membershipIdentifier: str,
        privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrivacyBudgetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListPrivacyBudgets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprivacybudgetspaginator)
        """

class ListProtectedQueriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListProtectedQueries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprotectedqueriespaginator)
    """

    def paginate(
        self,
        *,
        membershipIdentifier: str,
        status: ProtectedQueryStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProtectedQueriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListProtectedQueries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprotectedqueriespaginator)
        """

class ListSchemasPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListSchemas)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listschemaspaginator)
    """

    def paginate(
        self,
        *,
        collaborationIdentifier: str,
        schemaType: Literal["TABLE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemasOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListSchemas.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listschemaspaginator)
        """
