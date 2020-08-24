# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for appstream service client paginators.

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
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_appstream.type_defs import (
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    [Paginator.DescribeDirectoryConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)
    """

    def paginate(
        self, DirectoryNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectoryConfigsResultTypeDef]:
        """
        [DescribeDirectoryConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs.paginate)
        """


class DescribeFleetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)
    """

    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetsResultTypeDef]:
        """
        [DescribeFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeFleets.paginate)
        """


class DescribeImageBuildersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImageBuilders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)
    """

    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImageBuildersResultTypeDef]:
        """
        [DescribeImageBuilders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders.paginate)
        """


class DescribeImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeImages)
    """

    def paginate(
        self,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: Literal["PUBLIC", "PRIVATE", "SHARED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeImagesResultTypeDef]:
        """
        [DescribeImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeImages.paginate)
        """


class DescribeSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)
    """

    def paginate(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSessionsResultTypeDef]:
        """
        [DescribeSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeSessions.paginate)
        """


class DescribeStacksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)
    """

    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStacksResultTypeDef]:
        """
        [DescribeStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeStacks.paginate)
        """


class DescribeUserStackAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUserStackAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)
    """

    def paginate(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeUserStackAssociationsResultTypeDef]:
        """
        [DescribeUserStackAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations.paginate)
        """


class DescribeUsersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)
    """

    def paginate(
        self,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeUsersResultTypeDef]:
        """
        [DescribeUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeUsers.paginate)
        """


class ListAssociatedFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociatedFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)
    """

    def paginate(
        self, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedFleetsResultTypeDef]:
        """
        [ListAssociatedFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets.paginate)
        """


class ListAssociatedStacksPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociatedStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)
    """

    def paginate(
        self, FleetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedStacksResultTypeDef]:
        """
        [ListAssociatedStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks.paginate)
        """
