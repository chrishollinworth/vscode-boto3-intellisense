"""
Type annotations for cloudcontrol service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudcontrol import CloudControlApiClient
    from mypy_boto3_cloudcontrol.paginator import (
        ListResourceRequestsPaginator,
        ListResourcesPaginator,
    )

    client: CloudControlApiClient = boto3.client("cloudcontrol")

    list_resource_requests_paginator: ListResourceRequestsPaginator = client.get_paginator("list_resource_requests")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListResourceRequestsOutputTypeDef,
    ListResourcesOutputTypeDef,
    PaginatorConfigTypeDef,
    ResourceRequestStatusFilterTypeDef,
)

__all__ = ("ListResourceRequestsPaginator", "ListResourcesPaginator")

class ListResourceRequestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudcontrol.html#CloudControlApi.Paginator.ListResourceRequests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators.html#listresourcerequestspaginator)
    """

    def paginate(
        self,
        *,
        ResourceRequestStatusFilter: "ResourceRequestStatusFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceRequestsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudcontrol.html#CloudControlApi.Paginator.ListResourceRequests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators.html#listresourcerequestspaginator)
        """

class ListResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudcontrol.html#CloudControlApi.Paginator.ListResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators.html#listresourcespaginator)
    """

    def paginate(
        self,
        *,
        TypeName: str,
        TypeVersionId: str = None,
        RoleArn: str = None,
        ResourceModel: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudcontrol.html#CloudControlApi.Paginator.ListResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators.html#listresourcespaginator)
        """
