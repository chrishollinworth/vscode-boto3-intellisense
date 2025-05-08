"""
Type annotations for route53-recovery-readiness service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53_recovery_readiness.client import Route53RecoveryReadinessClient
    from mypy_boto3_route53_recovery_readiness.paginator import (
        GetCellReadinessSummaryPaginator,
        GetReadinessCheckResourceStatusPaginator,
        GetReadinessCheckStatusPaginator,
        GetRecoveryGroupReadinessSummaryPaginator,
        ListCellsPaginator,
        ListCrossAccountAuthorizationsPaginator,
        ListReadinessChecksPaginator,
        ListRecoveryGroupsPaginator,
        ListResourceSetsPaginator,
        ListRulesPaginator,
    )

    session = Session()
    client: Route53RecoveryReadinessClient = session.client("route53-recovery-readiness")

    get_cell_readiness_summary_paginator: GetCellReadinessSummaryPaginator = client.get_paginator("get_cell_readiness_summary")
    get_readiness_check_resource_status_paginator: GetReadinessCheckResourceStatusPaginator = client.get_paginator("get_readiness_check_resource_status")
    get_readiness_check_status_paginator: GetReadinessCheckStatusPaginator = client.get_paginator("get_readiness_check_status")
    get_recovery_group_readiness_summary_paginator: GetRecoveryGroupReadinessSummaryPaginator = client.get_paginator("get_recovery_group_readiness_summary")
    list_cells_paginator: ListCellsPaginator = client.get_paginator("list_cells")
    list_cross_account_authorizations_paginator: ListCrossAccountAuthorizationsPaginator = client.get_paginator("list_cross_account_authorizations")
    list_readiness_checks_paginator: ListReadinessChecksPaginator = client.get_paginator("list_readiness_checks")
    list_recovery_groups_paginator: ListRecoveryGroupsPaginator = client.get_paginator("list_recovery_groups")
    list_resource_sets_paginator: ListResourceSetsPaginator = client.get_paginator("list_resource_sets")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetCellReadinessSummaryRequestPaginateTypeDef,
    GetCellReadinessSummaryResponseTypeDef,
    GetReadinessCheckResourceStatusRequestPaginateTypeDef,
    GetReadinessCheckResourceStatusResponseTypeDef,
    GetReadinessCheckStatusRequestPaginateTypeDef,
    GetReadinessCheckStatusResponseTypeDef,
    GetRecoveryGroupReadinessSummaryRequestPaginateTypeDef,
    GetRecoveryGroupReadinessSummaryResponseTypeDef,
    ListCellsRequestPaginateTypeDef,
    ListCellsResponseTypeDef,
    ListCrossAccountAuthorizationsRequestPaginateTypeDef,
    ListCrossAccountAuthorizationsResponseTypeDef,
    ListReadinessChecksRequestPaginateTypeDef,
    ListReadinessChecksResponseTypeDef,
    ListRecoveryGroupsRequestPaginateTypeDef,
    ListRecoveryGroupsResponseTypeDef,
    ListResourceSetsRequestPaginateTypeDef,
    ListResourceSetsResponseTypeDef,
    ListRulesRequestPaginateTypeDef,
    ListRulesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetCellReadinessSummaryPaginator",
    "GetReadinessCheckResourceStatusPaginator",
    "GetReadinessCheckStatusPaginator",
    "GetRecoveryGroupReadinessSummaryPaginator",
    "ListCellsPaginator",
    "ListCrossAccountAuthorizationsPaginator",
    "ListReadinessChecksPaginator",
    "ListRecoveryGroupsPaginator",
    "ListResourceSetsPaginator",
    "ListRulesPaginator",
)

if TYPE_CHECKING:
    _GetCellReadinessSummaryPaginatorBase = Paginator[GetCellReadinessSummaryResponseTypeDef]
else:
    _GetCellReadinessSummaryPaginatorBase = Paginator  # type: ignore[assignment]

class GetCellReadinessSummaryPaginator(_GetCellReadinessSummaryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetCellReadinessSummary.html#Route53RecoveryReadiness.Paginator.GetCellReadinessSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getcellreadinesssummarypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCellReadinessSummaryRequestPaginateTypeDef]
    ) -> PageIterator[GetCellReadinessSummaryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetCellReadinessSummary.html#Route53RecoveryReadiness.Paginator.GetCellReadinessSummary.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getcellreadinesssummarypaginator)
        """

if TYPE_CHECKING:
    _GetReadinessCheckResourceStatusPaginatorBase = Paginator[
        GetReadinessCheckResourceStatusResponseTypeDef
    ]
else:
    _GetReadinessCheckResourceStatusPaginatorBase = Paginator  # type: ignore[assignment]

class GetReadinessCheckResourceStatusPaginator(_GetReadinessCheckResourceStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetReadinessCheckResourceStatus.html#Route53RecoveryReadiness.Paginator.GetReadinessCheckResourceStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getreadinesscheckresourcestatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetReadinessCheckResourceStatusRequestPaginateTypeDef]
    ) -> PageIterator[GetReadinessCheckResourceStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetReadinessCheckResourceStatus.html#Route53RecoveryReadiness.Paginator.GetReadinessCheckResourceStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getreadinesscheckresourcestatuspaginator)
        """

if TYPE_CHECKING:
    _GetReadinessCheckStatusPaginatorBase = Paginator[GetReadinessCheckStatusResponseTypeDef]
else:
    _GetReadinessCheckStatusPaginatorBase = Paginator  # type: ignore[assignment]

class GetReadinessCheckStatusPaginator(_GetReadinessCheckStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetReadinessCheckStatus.html#Route53RecoveryReadiness.Paginator.GetReadinessCheckStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getreadinesscheckstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetReadinessCheckStatusRequestPaginateTypeDef]
    ) -> PageIterator[GetReadinessCheckStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetReadinessCheckStatus.html#Route53RecoveryReadiness.Paginator.GetReadinessCheckStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getreadinesscheckstatuspaginator)
        """

if TYPE_CHECKING:
    _GetRecoveryGroupReadinessSummaryPaginatorBase = Paginator[
        GetRecoveryGroupReadinessSummaryResponseTypeDef
    ]
else:
    _GetRecoveryGroupReadinessSummaryPaginatorBase = Paginator  # type: ignore[assignment]

class GetRecoveryGroupReadinessSummaryPaginator(_GetRecoveryGroupReadinessSummaryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetRecoveryGroupReadinessSummary.html#Route53RecoveryReadiness.Paginator.GetRecoveryGroupReadinessSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getrecoverygroupreadinesssummarypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRecoveryGroupReadinessSummaryRequestPaginateTypeDef]
    ) -> PageIterator[GetRecoveryGroupReadinessSummaryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/GetRecoveryGroupReadinessSummary.html#Route53RecoveryReadiness.Paginator.GetRecoveryGroupReadinessSummary.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#getrecoverygroupreadinesssummarypaginator)
        """

if TYPE_CHECKING:
    _ListCellsPaginatorBase = Paginator[ListCellsResponseTypeDef]
else:
    _ListCellsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCellsPaginator(_ListCellsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListCells.html#Route53RecoveryReadiness.Paginator.ListCells)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listcellspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCellsRequestPaginateTypeDef]
    ) -> PageIterator[ListCellsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListCells.html#Route53RecoveryReadiness.Paginator.ListCells.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listcellspaginator)
        """

if TYPE_CHECKING:
    _ListCrossAccountAuthorizationsPaginatorBase = Paginator[
        ListCrossAccountAuthorizationsResponseTypeDef
    ]
else:
    _ListCrossAccountAuthorizationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCrossAccountAuthorizationsPaginator(_ListCrossAccountAuthorizationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListCrossAccountAuthorizations.html#Route53RecoveryReadiness.Paginator.ListCrossAccountAuthorizations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listcrossaccountauthorizationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCrossAccountAuthorizationsRequestPaginateTypeDef]
    ) -> PageIterator[ListCrossAccountAuthorizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListCrossAccountAuthorizations.html#Route53RecoveryReadiness.Paginator.ListCrossAccountAuthorizations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listcrossaccountauthorizationspaginator)
        """

if TYPE_CHECKING:
    _ListReadinessChecksPaginatorBase = Paginator[ListReadinessChecksResponseTypeDef]
else:
    _ListReadinessChecksPaginatorBase = Paginator  # type: ignore[assignment]

class ListReadinessChecksPaginator(_ListReadinessChecksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListReadinessChecks.html#Route53RecoveryReadiness.Paginator.ListReadinessChecks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listreadinesscheckspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReadinessChecksRequestPaginateTypeDef]
    ) -> PageIterator[ListReadinessChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListReadinessChecks.html#Route53RecoveryReadiness.Paginator.ListReadinessChecks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listreadinesscheckspaginator)
        """

if TYPE_CHECKING:
    _ListRecoveryGroupsPaginatorBase = Paginator[ListRecoveryGroupsResponseTypeDef]
else:
    _ListRecoveryGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecoveryGroupsPaginator(_ListRecoveryGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListRecoveryGroups.html#Route53RecoveryReadiness.Paginator.ListRecoveryGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listrecoverygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecoveryGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecoveryGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListRecoveryGroups.html#Route53RecoveryReadiness.Paginator.ListRecoveryGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listrecoverygroupspaginator)
        """

if TYPE_CHECKING:
    _ListResourceSetsPaginatorBase = Paginator[ListResourceSetsResponseTypeDef]
else:
    _ListResourceSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceSetsPaginator(_ListResourceSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListResourceSets.html#Route53RecoveryReadiness.Paginator.ListResourceSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listresourcesetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListResourceSets.html#Route53RecoveryReadiness.Paginator.ListResourceSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listresourcesetspaginator)
        """

if TYPE_CHECKING:
    _ListRulesPaginatorBase = Paginator[ListRulesResponseTypeDef]
else:
    _ListRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRulesPaginator(_ListRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListRules.html#Route53RecoveryReadiness.Paginator.ListRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/paginator/ListRules.html#Route53RecoveryReadiness.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/paginators/#listrulespaginator)
        """
