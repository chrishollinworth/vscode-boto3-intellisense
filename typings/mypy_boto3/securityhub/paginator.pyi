"""
Type annotations for securityhub service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_securityhub.client import SecurityHubClient
    from mypy_boto3_securityhub.paginator import (
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

    session = Session()
    client: SecurityHubClient = session.client("securityhub")

    describe_action_targets_paginator: DescribeActionTargetsPaginator = client.get_paginator("describe_action_targets")
    describe_products_paginator: DescribeProductsPaginator = client.get_paginator("describe_products")
    describe_standards_controls_paginator: DescribeStandardsControlsPaginator = client.get_paginator("describe_standards_controls")
    describe_standards_paginator: DescribeStandardsPaginator = client.get_paginator("describe_standards")
    get_enabled_standards_paginator: GetEnabledStandardsPaginator = client.get_paginator("get_enabled_standards")
    get_finding_history_paginator: GetFindingHistoryPaginator = client.get_paginator("get_finding_history")
    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    get_insights_paginator: GetInsightsPaginator = client.get_paginator("get_insights")
    list_configuration_policies_paginator: ListConfigurationPoliciesPaginator = client.get_paginator("list_configuration_policies")
    list_configuration_policy_associations_paginator: ListConfigurationPolicyAssociationsPaginator = client.get_paginator("list_configuration_policy_associations")
    list_enabled_products_for_import_paginator: ListEnabledProductsForImportPaginator = client.get_paginator("list_enabled_products_for_import")
    list_finding_aggregators_paginator: ListFindingAggregatorsPaginator = client.get_paginator("list_finding_aggregators")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    list_security_control_definitions_paginator: ListSecurityControlDefinitionsPaginator = client.get_paginator("list_security_control_definitions")
    list_standards_control_associations_paginator: ListStandardsControlAssociationsPaginator = client.get_paginator("list_standards_control_associations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeActionTargetsRequestPaginateTypeDef,
    DescribeActionTargetsResponseTypeDef,
    DescribeProductsRequestPaginateTypeDef,
    DescribeProductsResponseTypeDef,
    DescribeStandardsControlsRequestPaginateTypeDef,
    DescribeStandardsControlsResponseTypeDef,
    DescribeStandardsRequestPaginateTypeDef,
    DescribeStandardsResponseTypeDef,
    GetEnabledStandardsRequestPaginateTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingHistoryRequestPaginateTypeDef,
    GetFindingHistoryResponseTypeDef,
    GetFindingsRequestPaginateTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightsRequestPaginateTypeDef,
    GetInsightsResponseTypeDef,
    ListConfigurationPoliciesRequestPaginateTypeDef,
    ListConfigurationPoliciesResponseTypeDef,
    ListConfigurationPolicyAssociationsRequestPaginateTypeDef,
    ListConfigurationPolicyAssociationsResponseTypeDef,
    ListEnabledProductsForImportRequestPaginateTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListFindingAggregatorsRequestPaginateTypeDef,
    ListFindingAggregatorsResponseTypeDef,
    ListInvitationsRequestPaginateTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersRequestPaginateTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsRequestPaginateTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListSecurityControlDefinitionsRequestPaginateTypeDef,
    ListSecurityControlDefinitionsResponseTypeDef,
    ListStandardsControlAssociationsRequestPaginateTypeDef,
    ListStandardsControlAssociationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeActionTargetsPaginator",
    "DescribeProductsPaginator",
    "DescribeStandardsControlsPaginator",
    "DescribeStandardsPaginator",
    "GetEnabledStandardsPaginator",
    "GetFindingHistoryPaginator",
    "GetFindingsPaginator",
    "GetInsightsPaginator",
    "ListConfigurationPoliciesPaginator",
    "ListConfigurationPolicyAssociationsPaginator",
    "ListEnabledProductsForImportPaginator",
    "ListFindingAggregatorsPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
    "ListSecurityControlDefinitionsPaginator",
    "ListStandardsControlAssociationsPaginator",
)

if TYPE_CHECKING:
    _DescribeActionTargetsPaginatorBase = Paginator[DescribeActionTargetsResponseTypeDef]
else:
    _DescribeActionTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeActionTargetsPaginator(_DescribeActionTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeActionTargets.html#SecurityHub.Paginator.DescribeActionTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describeactiontargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeActionTargetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeActionTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeActionTargets.html#SecurityHub.Paginator.DescribeActionTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describeactiontargetspaginator)
        """

if TYPE_CHECKING:
    _DescribeProductsPaginatorBase = Paginator[DescribeProductsResponseTypeDef]
else:
    _DescribeProductsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeProductsPaginator(_DescribeProductsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeProducts.html#SecurityHub.Paginator.DescribeProducts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describeproductspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeProductsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeProductsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeProducts.html#SecurityHub.Paginator.DescribeProducts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describeproductspaginator)
        """

if TYPE_CHECKING:
    _DescribeStandardsControlsPaginatorBase = Paginator[DescribeStandardsControlsResponseTypeDef]
else:
    _DescribeStandardsControlsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStandardsControlsPaginator(_DescribeStandardsControlsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeStandardsControls.html#SecurityHub.Paginator.DescribeStandardsControls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describestandardscontrolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStandardsControlsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeStandardsControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeStandardsControls.html#SecurityHub.Paginator.DescribeStandardsControls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describestandardscontrolspaginator)
        """

if TYPE_CHECKING:
    _DescribeStandardsPaginatorBase = Paginator[DescribeStandardsResponseTypeDef]
else:
    _DescribeStandardsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStandardsPaginator(_DescribeStandardsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeStandards.html#SecurityHub.Paginator.DescribeStandards)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describestandardspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStandardsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeStandardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/DescribeStandards.html#SecurityHub.Paginator.DescribeStandards.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#describestandardspaginator)
        """

if TYPE_CHECKING:
    _GetEnabledStandardsPaginatorBase = Paginator[GetEnabledStandardsResponseTypeDef]
else:
    _GetEnabledStandardsPaginatorBase = Paginator  # type: ignore[assignment]

class GetEnabledStandardsPaginator(_GetEnabledStandardsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetEnabledStandards.html#SecurityHub.Paginator.GetEnabledStandards)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getenabledstandardspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetEnabledStandardsRequestPaginateTypeDef]
    ) -> PageIterator[GetEnabledStandardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetEnabledStandards.html#SecurityHub.Paginator.GetEnabledStandards.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getenabledstandardspaginator)
        """

if TYPE_CHECKING:
    _GetFindingHistoryPaginatorBase = Paginator[GetFindingHistoryResponseTypeDef]
else:
    _GetFindingHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetFindingHistoryPaginator(_GetFindingHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetFindingHistory.html#SecurityHub.Paginator.GetFindingHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getfindinghistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFindingHistoryRequestPaginateTypeDef]
    ) -> PageIterator[GetFindingHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetFindingHistory.html#SecurityHub.Paginator.GetFindingHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getfindinghistorypaginator)
        """

if TYPE_CHECKING:
    _GetFindingsPaginatorBase = Paginator[GetFindingsResponseTypeDef]
else:
    _GetFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class GetFindingsPaginator(_GetFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetFindings.html#SecurityHub.Paginator.GetFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFindingsRequestPaginateTypeDef]
    ) -> PageIterator[GetFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetFindings.html#SecurityHub.Paginator.GetFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getfindingspaginator)
        """

if TYPE_CHECKING:
    _GetInsightsPaginatorBase = Paginator[GetInsightsResponseTypeDef]
else:
    _GetInsightsPaginatorBase = Paginator  # type: ignore[assignment]

class GetInsightsPaginator(_GetInsightsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetInsights.html#SecurityHub.Paginator.GetInsights)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getinsightspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetInsightsRequestPaginateTypeDef]
    ) -> PageIterator[GetInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/GetInsights.html#SecurityHub.Paginator.GetInsights.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#getinsightspaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationPoliciesPaginatorBase = Paginator[ListConfigurationPoliciesResponseTypeDef]
else:
    _ListConfigurationPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationPoliciesPaginator(_ListConfigurationPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListConfigurationPolicies.html#SecurityHub.Paginator.ListConfigurationPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listconfigurationpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigurationPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListConfigurationPolicies.html#SecurityHub.Paginator.ListConfigurationPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listconfigurationpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationPolicyAssociationsPaginatorBase = Paginator[
        ListConfigurationPolicyAssociationsResponseTypeDef
    ]
else:
    _ListConfigurationPolicyAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationPolicyAssociationsPaginator(
    _ListConfigurationPolicyAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListConfigurationPolicyAssociations.html#SecurityHub.Paginator.ListConfigurationPolicyAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listconfigurationpolicyassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationPolicyAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigurationPolicyAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListConfigurationPolicyAssociations.html#SecurityHub.Paginator.ListConfigurationPolicyAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listconfigurationpolicyassociationspaginator)
        """

if TYPE_CHECKING:
    _ListEnabledProductsForImportPaginatorBase = Paginator[
        ListEnabledProductsForImportResponseTypeDef
    ]
else:
    _ListEnabledProductsForImportPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnabledProductsForImportPaginator(_ListEnabledProductsForImportPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListEnabledProductsForImport.html#SecurityHub.Paginator.ListEnabledProductsForImport)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listenabledproductsforimportpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnabledProductsForImportRequestPaginateTypeDef]
    ) -> PageIterator[ListEnabledProductsForImportResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListEnabledProductsForImport.html#SecurityHub.Paginator.ListEnabledProductsForImport.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listenabledproductsforimportpaginator)
        """

if TYPE_CHECKING:
    _ListFindingAggregatorsPaginatorBase = Paginator[ListFindingAggregatorsResponseTypeDef]
else:
    _ListFindingAggregatorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingAggregatorsPaginator(_ListFindingAggregatorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListFindingAggregators.html#SecurityHub.Paginator.ListFindingAggregators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listfindingaggregatorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingAggregatorsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingAggregatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListFindingAggregators.html#SecurityHub.Paginator.ListFindingAggregators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listfindingaggregatorspaginator)
        """

if TYPE_CHECKING:
    _ListInvitationsPaginatorBase = Paginator[ListInvitationsResponseTypeDef]
else:
    _ListInvitationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvitationsPaginator(_ListInvitationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListInvitations.html#SecurityHub.Paginator.ListInvitations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listinvitationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvitationsRequestPaginateTypeDef]
    ) -> PageIterator[ListInvitationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListInvitations.html#SecurityHub.Paginator.ListInvitations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listinvitationspaginator)
        """

if TYPE_CHECKING:
    _ListMembersPaginatorBase = Paginator[ListMembersResponseTypeDef]
else:
    _ListMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListMembersPaginator(_ListMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListMembers.html#SecurityHub.Paginator.ListMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListMembers.html#SecurityHub.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listmemberspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationAdminAccountsPaginatorBase = Paginator[
        ListOrganizationAdminAccountsResponseTypeDef
    ]
else:
    _ListOrganizationAdminAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationAdminAccountsPaginator(_ListOrganizationAdminAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListOrganizationAdminAccounts.html#SecurityHub.Paginator.ListOrganizationAdminAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listorganizationadminaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationAdminAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationAdminAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListOrganizationAdminAccounts.html#SecurityHub.Paginator.ListOrganizationAdminAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listorganizationadminaccountspaginator)
        """

if TYPE_CHECKING:
    _ListSecurityControlDefinitionsPaginatorBase = Paginator[
        ListSecurityControlDefinitionsResponseTypeDef
    ]
else:
    _ListSecurityControlDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSecurityControlDefinitionsPaginator(_ListSecurityControlDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListSecurityControlDefinitions.html#SecurityHub.Paginator.ListSecurityControlDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listsecuritycontroldefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityControlDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSecurityControlDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListSecurityControlDefinitions.html#SecurityHub.Paginator.ListSecurityControlDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#listsecuritycontroldefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListStandardsControlAssociationsPaginatorBase = Paginator[
        ListStandardsControlAssociationsResponseTypeDef
    ]
else:
    _ListStandardsControlAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStandardsControlAssociationsPaginator(_ListStandardsControlAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListStandardsControlAssociations.html#SecurityHub.Paginator.ListStandardsControlAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#liststandardscontrolassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStandardsControlAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListStandardsControlAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub/paginator/ListStandardsControlAssociations.html#SecurityHub.Paginator.ListStandardsControlAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators/#liststandardscontrolassociationspaginator)
        """
