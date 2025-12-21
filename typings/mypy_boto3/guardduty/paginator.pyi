"""
Type annotations for guardduty service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_guardduty.client import GuardDutyClient
    from mypy_boto3_guardduty.paginator import (
        DescribeMalwareScansPaginator,
        ListCoveragePaginator,
        ListDetectorsPaginator,
        ListFiltersPaginator,
        ListFindingsPaginator,
        ListIPSetsPaginator,
        ListInvitationsPaginator,
        ListMalwareScansPaginator,
        ListMembersPaginator,
        ListOrganizationAdminAccountsPaginator,
        ListThreatEntitySetsPaginator,
        ListThreatIntelSetsPaginator,
        ListTrustedEntitySetsPaginator,
    )

    session = Session()
    client: GuardDutyClient = session.client("guardduty")

    describe_malware_scans_paginator: DescribeMalwareScansPaginator = client.get_paginator("describe_malware_scans")
    list_coverage_paginator: ListCoveragePaginator = client.get_paginator("list_coverage")
    list_detectors_paginator: ListDetectorsPaginator = client.get_paginator("list_detectors")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_ip_sets_paginator: ListIPSetsPaginator = client.get_paginator("list_ip_sets")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_malware_scans_paginator: ListMalwareScansPaginator = client.get_paginator("list_malware_scans")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    list_threat_entity_sets_paginator: ListThreatEntitySetsPaginator = client.get_paginator("list_threat_entity_sets")
    list_threat_intel_sets_paginator: ListThreatIntelSetsPaginator = client.get_paginator("list_threat_intel_sets")
    list_trusted_entity_sets_paginator: ListTrustedEntitySetsPaginator = client.get_paginator("list_trusted_entity_sets")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeMalwareScansRequestPaginateTypeDef,
    DescribeMalwareScansResponseTypeDef,
    ListCoverageRequestPaginateTypeDef,
    ListCoverageResponseTypeDef,
    ListDetectorsRequestPaginateTypeDef,
    ListDetectorsResponseTypeDef,
    ListFiltersRequestPaginateTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingsRequestPaginateTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsRequestPaginateTypeDef,
    ListInvitationsResponseTypeDef,
    ListIPSetsRequestPaginateTypeDef,
    ListIPSetsResponseTypeDef,
    ListMalwareScansRequestPaginateTypeDef,
    ListMalwareScansResponseTypeDef,
    ListMembersRequestPaginateTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsRequestPaginateTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListThreatEntitySetsRequestPaginateTypeDef,
    ListThreatEntitySetsResponseTypeDef,
    ListThreatIntelSetsRequestPaginateTypeDef,
    ListThreatIntelSetsResponseTypeDef,
    ListTrustedEntitySetsRequestPaginateTypeDef,
    ListTrustedEntitySetsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeMalwareScansPaginator",
    "ListCoveragePaginator",
    "ListDetectorsPaginator",
    "ListFiltersPaginator",
    "ListFindingsPaginator",
    "ListIPSetsPaginator",
    "ListInvitationsPaginator",
    "ListMalwareScansPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
    "ListThreatEntitySetsPaginator",
    "ListThreatIntelSetsPaginator",
    "ListTrustedEntitySetsPaginator",
)

if TYPE_CHECKING:
    _DescribeMalwareScansPaginatorBase = Paginator[DescribeMalwareScansResponseTypeDef]
else:
    _DescribeMalwareScansPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMalwareScansPaginator(_DescribeMalwareScansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/DescribeMalwareScans.html#GuardDuty.Paginator.DescribeMalwareScans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#describemalwarescanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMalwareScansRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMalwareScansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/DescribeMalwareScans.html#GuardDuty.Paginator.DescribeMalwareScans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#describemalwarescanspaginator)
        """

if TYPE_CHECKING:
    _ListCoveragePaginatorBase = Paginator[ListCoverageResponseTypeDef]
else:
    _ListCoveragePaginatorBase = Paginator  # type: ignore[assignment]

class ListCoveragePaginator(_ListCoveragePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListCoverage.html#GuardDuty.Paginator.ListCoverage)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listcoveragepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoverageRequestPaginateTypeDef]
    ) -> PageIterator[ListCoverageResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListCoverage.html#GuardDuty.Paginator.ListCoverage.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listcoveragepaginator)
        """

if TYPE_CHECKING:
    _ListDetectorsPaginatorBase = Paginator[ListDetectorsResponseTypeDef]
else:
    _ListDetectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDetectorsPaginator(_ListDetectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListDetectors.html#GuardDuty.Paginator.ListDetectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listdetectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDetectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListDetectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListDetectors.html#GuardDuty.Paginator.ListDetectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listdetectorspaginator)
        """

if TYPE_CHECKING:
    _ListFiltersPaginatorBase = Paginator[ListFiltersResponseTypeDef]
else:
    _ListFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class ListFiltersPaginator(_ListFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListFilters.html#GuardDuty.Paginator.ListFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFiltersRequestPaginateTypeDef]
    ) -> PageIterator[ListFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListFilters.html#GuardDuty.Paginator.ListFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listfilterspaginator)
        """

if TYPE_CHECKING:
    _ListFindingsPaginatorBase = Paginator[ListFindingsResponseTypeDef]
else:
    _ListFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsPaginator(_ListFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListFindings.html#GuardDuty.Paginator.ListFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListFindings.html#GuardDuty.Paginator.ListFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listfindingspaginator)
        """

if TYPE_CHECKING:
    _ListIPSetsPaginatorBase = Paginator[ListIPSetsResponseTypeDef]
else:
    _ListIPSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIPSetsPaginator(_ListIPSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListIPSets.html#GuardDuty.Paginator.ListIPSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listipsetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIPSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListIPSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListIPSets.html#GuardDuty.Paginator.ListIPSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listipsetspaginator)
        """

if TYPE_CHECKING:
    _ListInvitationsPaginatorBase = Paginator[ListInvitationsResponseTypeDef]
else:
    _ListInvitationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvitationsPaginator(_ListInvitationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListInvitations.html#GuardDuty.Paginator.ListInvitations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listinvitationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvitationsRequestPaginateTypeDef]
    ) -> PageIterator[ListInvitationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListInvitations.html#GuardDuty.Paginator.ListInvitations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listinvitationspaginator)
        """

if TYPE_CHECKING:
    _ListMalwareScansPaginatorBase = Paginator[ListMalwareScansResponseTypeDef]
else:
    _ListMalwareScansPaginatorBase = Paginator  # type: ignore[assignment]

class ListMalwareScansPaginator(_ListMalwareScansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListMalwareScans.html#GuardDuty.Paginator.ListMalwareScans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listmalwarescanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMalwareScansRequestPaginateTypeDef]
    ) -> PageIterator[ListMalwareScansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListMalwareScans.html#GuardDuty.Paginator.ListMalwareScans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listmalwarescanspaginator)
        """

if TYPE_CHECKING:
    _ListMembersPaginatorBase = Paginator[ListMembersResponseTypeDef]
else:
    _ListMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListMembersPaginator(_ListMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListMembers.html#GuardDuty.Paginator.ListMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListMembers.html#GuardDuty.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listmemberspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationAdminAccountsPaginatorBase = Paginator[
        ListOrganizationAdminAccountsResponseTypeDef
    ]
else:
    _ListOrganizationAdminAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationAdminAccountsPaginator(_ListOrganizationAdminAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListOrganizationAdminAccounts.html#GuardDuty.Paginator.ListOrganizationAdminAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listorganizationadminaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationAdminAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationAdminAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListOrganizationAdminAccounts.html#GuardDuty.Paginator.ListOrganizationAdminAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listorganizationadminaccountspaginator)
        """

if TYPE_CHECKING:
    _ListThreatEntitySetsPaginatorBase = Paginator[ListThreatEntitySetsResponseTypeDef]
else:
    _ListThreatEntitySetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListThreatEntitySetsPaginator(_ListThreatEntitySetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListThreatEntitySets.html#GuardDuty.Paginator.ListThreatEntitySets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listthreatentitysetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListThreatEntitySetsRequestPaginateTypeDef]
    ) -> PageIterator[ListThreatEntitySetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListThreatEntitySets.html#GuardDuty.Paginator.ListThreatEntitySets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listthreatentitysetspaginator)
        """

if TYPE_CHECKING:
    _ListThreatIntelSetsPaginatorBase = Paginator[ListThreatIntelSetsResponseTypeDef]
else:
    _ListThreatIntelSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListThreatIntelSetsPaginator(_ListThreatIntelSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListThreatIntelSets.html#GuardDuty.Paginator.ListThreatIntelSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listthreatintelsetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListThreatIntelSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListThreatIntelSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListThreatIntelSets.html#GuardDuty.Paginator.ListThreatIntelSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listthreatintelsetspaginator)
        """

if TYPE_CHECKING:
    _ListTrustedEntitySetsPaginatorBase = Paginator[ListTrustedEntitySetsResponseTypeDef]
else:
    _ListTrustedEntitySetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrustedEntitySetsPaginator(_ListTrustedEntitySetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListTrustedEntitySets.html#GuardDuty.Paginator.ListTrustedEntitySets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listtrustedentitysetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrustedEntitySetsRequestPaginateTypeDef]
    ) -> PageIterator[ListTrustedEntitySetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty/paginator/ListTrustedEntitySets.html#GuardDuty.Paginator.ListTrustedEntitySets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators/#listtrustedentitysetspaginator)
        """
