# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cloud9 service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_cloud9 import Cloud9Client
    from mypy_boto3_cloud9.paginator import (
        DescribeEnvironmentMembershipsPaginator,
        ListEnvironmentsPaginator,
    )

    client: Cloud9Client = boto3.client("cloud9")

    describe_environment_memberships_paginator: DescribeEnvironmentMembershipsPaginator = client.get_paginator("describe_environment_memberships")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cloud9.type_defs import (
    DescribeEnvironmentMembershipsResultTypeDef,
    ListEnvironmentsResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DescribeEnvironmentMembershipsPaginator", "ListEnvironmentsPaginator")


class DescribeEnvironmentMembershipsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEnvironmentMemberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships)
    """

    def paginate(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[Literal["owner", "read-write", "read-only"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEnvironmentMembershipsResultTypeDef]:
        """
        [DescribeEnvironmentMemberships.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships.paginate)
        """


class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsResultTypeDef]:
        """
        [ListEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments.paginate)
        """
