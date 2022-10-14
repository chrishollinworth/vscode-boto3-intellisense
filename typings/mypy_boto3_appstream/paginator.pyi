"""
Type annotations for appstream service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_appstream import AppStreamClient
    from mypy_boto3_appstream.paginator import (
        DescribeDirectoryConfigsPaginator,
        DescribeFleetsPaginator,
        DescribeImageBuildersPaginator,
        DescribeImagesPaginator,
        DescribeSessionsPaginator,
        DescribeStacksPaginator,
        DescribeUserStackAssociationsPaginator,
        DescribeUsersPaginator,
        ListAssociatedFleetsPaginator,
        ListAssociatedStacksPaginator,
    )

    client: AppStreamClient = boto3.client("appstream")

    describe_directory_configs_paginator: DescribeDirectoryConfigsPaginator = client.get_paginator("describe_directory_configs")
    describe_fleets_paginator: DescribeFleetsPaginator = client.get_paginator("describe_fleets")
    describe_image_builders_paginator: DescribeImageBuildersPaginator = client.get_paginator("describe_image_builders")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_sessions_paginator: DescribeSessionsPaginator = client.get_paginator("describe_sessions")
    describe_stacks_paginator: DescribeStacksPaginator = client.get_paginator("describe_stacks")
    describe_user_stack_associations_paginator: DescribeUserStackAssociationsPaginator = client.get_paginator("describe_user_stack_associations")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    list_associated_fleets_paginator: ListAssociatedFleetsPaginator = client.get_paginator("list_associated_fleets")
    list_associated_stacks_paginator: ListAssociatedStacksPaginator = client.get_paginator("list_associated_stacks")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import AuthenticationTypeType, VisibilityTypeType
from .type_defs import (
    DescribeDirectoryConfigsResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeImageBuildersResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeSessionsResultTypeDef,
    DescribeStacksResultTypeDef,
    DescribeUsersResultTypeDef,
    DescribeUserStackAssociationsResultTypeDef,
    ListAssociatedFleetsResultTypeDef,
    ListAssociatedStacksResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeDirectoryConfigsPaginator",
    "DescribeFleetsPaginator",
    "DescribeImageBuildersPaginator",
    "DescribeImagesPaginator",
    "DescribeSessionsPaginator",
    "DescribeStacksPaginator",
    "DescribeUserStackAssociationsPaginator",
    "DescribeUsersPaginator",
    "ListAssociatedFleetsPaginator",
    "ListAssociatedStacksPaginator",
)

class DescribeDirectoryConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describedirectoryconfigspaginator)
    """

    def paginate(
        self, *, DirectoryNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectoryConfigsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describedirectoryconfigspaginator)
        """

class DescribeFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describefleetspaginator)
    """

    def paginate(
        self, *, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describefleetspaginator)
        """

class DescribeImageBuildersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagebuilderspaginator)
    """

    def paginate(
        self, *, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImageBuildersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagebuilderspaginator)
        """

class DescribeImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagespaginator)
    """

    def paginate(
        self,
        *,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: VisibilityTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagespaginator)
        """

class DescribeSessionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describesessionspaginator)
    """

    def paginate(
        self,
        *,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        AuthenticationType: AuthenticationTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSessionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeSessions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describesessionspaginator)
        """

class DescribeStacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describestackspaginator)
    """

    def paginate(
        self, *, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStacksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeStacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describestackspaginator)
        """

class DescribeUserStackAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserstackassociationspaginator)
    """

    def paginate(
        self,
        *,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: AuthenticationTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUserStackAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserstackassociationspaginator)
        """

class DescribeUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserspaginator)
    """

    def paginate(
        self,
        *,
        AuthenticationType: AuthenticationTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUsersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserspaginator)
        """

class ListAssociatedFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedfleetspaginator)
    """

    def paginate(
        self, *, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedfleetspaginator)
        """

class ListAssociatedStacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedstackspaginator)
    """

    def paginate(
        self, *, FleetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedStacksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedstackspaginator)
        """
