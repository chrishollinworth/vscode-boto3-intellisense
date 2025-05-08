"""
Type annotations for cloud9 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloud9/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloud9.client import Cloud9Client
    from mypy_boto3_cloud9.paginator import (
        DescribeEnvironmentMembershipsPaginator,
        ListEnvironmentsPaginator,
    )

    session = Session()
    client: Cloud9Client = session.client("cloud9")

    describe_environment_memberships_paginator: DescribeEnvironmentMembershipsPaginator = client.get_paginator("describe_environment_memberships")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeEnvironmentMembershipsRequestPaginateTypeDef,
    DescribeEnvironmentMembershipsResultTypeDef,
    ListEnvironmentsRequestPaginateTypeDef,
    ListEnvironmentsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DescribeEnvironmentMembershipsPaginator", "ListEnvironmentsPaginator")

if TYPE_CHECKING:
    _DescribeEnvironmentMembershipsPaginatorBase = Paginator[
        DescribeEnvironmentMembershipsResultTypeDef
    ]
else:
    _DescribeEnvironmentMembershipsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEnvironmentMembershipsPaginator(_DescribeEnvironmentMembershipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/DescribeEnvironmentMemberships.html#Cloud9.Paginator.DescribeEnvironmentMemberships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloud9/paginators/#describeenvironmentmembershipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEnvironmentMembershipsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEnvironmentMembershipsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/DescribeEnvironmentMemberships.html#Cloud9.Paginator.DescribeEnvironmentMemberships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloud9/paginators/#describeenvironmentmembershipspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsResultTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/ListEnvironments.html#Cloud9.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloud9/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/ListEnvironments.html#Cloud9.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloud9/paginators/#listenvironmentspaginator)
        """
