"""
Type annotations for appstream service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appstream.client import AppStreamClient
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

    session = Session()
    client: AppStreamClient = session.client("appstream")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeDirectoryConfigsRequestPaginateTypeDef,
    DescribeDirectoryConfigsResultTypeDef,
    DescribeFleetsRequestPaginateTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeImageBuildersRequestPaginateTypeDef,
    DescribeImageBuildersResultTypeDef,
    DescribeImagesRequestPaginateTypeDef,
    DescribeImagesResultTypeDef,
    DescribeSessionsRequestPaginateTypeDef,
    DescribeSessionsResultTypeDef,
    DescribeStacksRequestPaginateTypeDef,
    DescribeStacksResultTypeDef,
    DescribeUsersRequestPaginateTypeDef,
    DescribeUsersResultTypeDef,
    DescribeUserStackAssociationsRequestPaginateTypeDef,
    DescribeUserStackAssociationsResultTypeDef,
    ListAssociatedFleetsRequestPaginateTypeDef,
    ListAssociatedFleetsResultTypeDef,
    ListAssociatedStacksRequestPaginateTypeDef,
    ListAssociatedStacksResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _DescribeDirectoryConfigsPaginatorBase = Paginator[DescribeDirectoryConfigsResultTypeDef]
else:
    _DescribeDirectoryConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDirectoryConfigsPaginator(_DescribeDirectoryConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeDirectoryConfigs.html#AppStream.Paginator.DescribeDirectoryConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describedirectoryconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDirectoryConfigsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDirectoryConfigsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeDirectoryConfigs.html#AppStream.Paginator.DescribeDirectoryConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describedirectoryconfigspaginator)
        """

if TYPE_CHECKING:
    _DescribeFleetsPaginatorBase = Paginator[DescribeFleetsResultTypeDef]
else:
    _DescribeFleetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFleetsPaginator(_DescribeFleetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeFleets.html#AppStream.Paginator.DescribeFleets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describefleetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFleetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeFleets.html#AppStream.Paginator.DescribeFleets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describefleetspaginator)
        """

if TYPE_CHECKING:
    _DescribeImageBuildersPaginatorBase = Paginator[DescribeImageBuildersResultTypeDef]
else:
    _DescribeImageBuildersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImageBuildersPaginator(_DescribeImageBuildersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeImageBuilders.html#AppStream.Paginator.DescribeImageBuilders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeimagebuilderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImageBuildersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImageBuildersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeImageBuilders.html#AppStream.Paginator.DescribeImageBuilders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeimagebuilderspaginator)
        """

if TYPE_CHECKING:
    _DescribeImagesPaginatorBase = Paginator[DescribeImagesResultTypeDef]
else:
    _DescribeImagesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImagesPaginator(_DescribeImagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeImages.html#AppStream.Paginator.DescribeImages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeimagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImagesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeImages.html#AppStream.Paginator.DescribeImages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeimagespaginator)
        """

if TYPE_CHECKING:
    _DescribeSessionsPaginatorBase = Paginator[DescribeSessionsResultTypeDef]
else:
    _DescribeSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSessionsPaginator(_DescribeSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeSessions.html#AppStream.Paginator.DescribeSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describesessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSessionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSessionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeSessions.html#AppStream.Paginator.DescribeSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describesessionspaginator)
        """

if TYPE_CHECKING:
    _DescribeStacksPaginatorBase = Paginator[DescribeStacksResultTypeDef]
else:
    _DescribeStacksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStacksPaginator(_DescribeStacksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeStacks.html#AppStream.Paginator.DescribeStacks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describestackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeStacksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeStacks.html#AppStream.Paginator.DescribeStacks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describestackspaginator)
        """

if TYPE_CHECKING:
    _DescribeUserStackAssociationsPaginatorBase = Paginator[
        DescribeUserStackAssociationsResultTypeDef
    ]
else:
    _DescribeUserStackAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUserStackAssociationsPaginator(_DescribeUserStackAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeUserStackAssociations.html#AppStream.Paginator.DescribeUserStackAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeuserstackassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUserStackAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeUserStackAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeUserStackAssociations.html#AppStream.Paginator.DescribeUserStackAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeuserstackassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeUsersPaginatorBase = Paginator[DescribeUsersResultTypeDef]
else:
    _DescribeUsersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUsersPaginator(_DescribeUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeUsers.html#AppStream.Paginator.DescribeUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUsersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeUsersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/DescribeUsers.html#AppStream.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#describeuserspaginator)
        """

if TYPE_CHECKING:
    _ListAssociatedFleetsPaginatorBase = Paginator[ListAssociatedFleetsResultTypeDef]
else:
    _ListAssociatedFleetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedFleetsPaginator(_ListAssociatedFleetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/ListAssociatedFleets.html#AppStream.Paginator.ListAssociatedFleets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#listassociatedfleetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedFleetsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/ListAssociatedFleets.html#AppStream.Paginator.ListAssociatedFleets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#listassociatedfleetspaginator)
        """

if TYPE_CHECKING:
    _ListAssociatedStacksPaginatorBase = Paginator[ListAssociatedStacksResultTypeDef]
else:
    _ListAssociatedStacksPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedStacksPaginator(_ListAssociatedStacksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/ListAssociatedStacks.html#AppStream.Paginator.ListAssociatedStacks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#listassociatedstackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedStacksRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedStacksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/paginator/ListAssociatedStacks.html#AppStream.Paginator.ListAssociatedStacks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators/#listassociatedstackspaginator)
        """
