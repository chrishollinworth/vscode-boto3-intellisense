# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for fms service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_fms import FMSClient
    from mypy_boto3_fms.paginator import (
        ListComplianceStatusPaginator,
        ListMemberAccountsPaginator,
        ListPoliciesPaginator,
    )

    client: FMSClient = boto3.client("fms")

    list_compliance_status_paginator: ListComplianceStatusPaginator = client.get_paginator("list_compliance_status")
    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_fms.type_defs import (
    ListComplianceStatusResponseTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListComplianceStatusPaginator", "ListMemberAccountsPaginator", "ListPoliciesPaginator")


class ListComplianceStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListComplianceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)
    """

    def paginate(
        self, PolicyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComplianceStatusResponseTypeDef]:
        """
        [ListComplianceStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fms.html#FMS.Paginator.ListComplianceStatus.paginate)
        """


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMemberAccountsResponseTypeDef]:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fms.html#FMS.Paginator.ListMemberAccounts.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fms.html#FMS.Paginator.ListPolicies)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fms.html#FMS.Paginator.ListPolicies.paginate)
        """
