"""
Type annotations for rekognition service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rekognition.client import RekognitionClient
    from mypy_boto3_rekognition.paginator import (
        DescribeProjectVersionsPaginator,
        DescribeProjectsPaginator,
        ListCollectionsPaginator,
        ListDatasetEntriesPaginator,
        ListDatasetLabelsPaginator,
        ListFacesPaginator,
        ListProjectPoliciesPaginator,
        ListStreamProcessorsPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: RekognitionClient = session.client("rekognition")

    describe_project_versions_paginator: DescribeProjectVersionsPaginator = client.get_paginator("describe_project_versions")
    describe_projects_paginator: DescribeProjectsPaginator = client.get_paginator("describe_projects")
    list_collections_paginator: ListCollectionsPaginator = client.get_paginator("list_collections")
    list_dataset_entries_paginator: ListDatasetEntriesPaginator = client.get_paginator("list_dataset_entries")
    list_dataset_labels_paginator: ListDatasetLabelsPaginator = client.get_paginator("list_dataset_labels")
    list_faces_paginator: ListFacesPaginator = client.get_paginator("list_faces")
    list_project_policies_paginator: ListProjectPoliciesPaginator = client.get_paginator("list_project_policies")
    list_stream_processors_paginator: ListStreamProcessorsPaginator = client.get_paginator("list_stream_processors")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeProjectsRequestPaginateTypeDef,
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsRequestPaginateTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    ListCollectionsRequestPaginateTypeDef,
    ListCollectionsResponseTypeDef,
    ListDatasetEntriesRequestPaginateTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListDatasetLabelsRequestPaginateTypeDef,
    ListDatasetLabelsResponseTypeDef,
    ListFacesRequestPaginateTypeDef,
    ListFacesResponseTypeDef,
    ListProjectPoliciesRequestPaginateTypeDef,
    ListProjectPoliciesResponseTypeDef,
    ListStreamProcessorsRequestPaginateTypeDef,
    ListStreamProcessorsResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListDatasetEntriesPaginator",
    "ListDatasetLabelsPaginator",
    "ListFacesPaginator",
    "ListProjectPoliciesPaginator",
    "ListStreamProcessorsPaginator",
    "ListUsersPaginator",
)

if TYPE_CHECKING:
    _DescribeProjectVersionsPaginatorBase = Paginator[DescribeProjectVersionsResponseTypeDef]
else:
    _DescribeProjectVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeProjectVersionsPaginator(_DescribeProjectVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/DescribeProjectVersions.html#Rekognition.Paginator.DescribeProjectVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#describeprojectversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeProjectVersionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeProjectVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/DescribeProjectVersions.html#Rekognition.Paginator.DescribeProjectVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#describeprojectversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeProjectsPaginatorBase = Paginator[DescribeProjectsResponseTypeDef]
else:
    _DescribeProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeProjectsPaginator(_DescribeProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/DescribeProjects.html#Rekognition.Paginator.DescribeProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#describeprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeProjectsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/DescribeProjects.html#Rekognition.Paginator.DescribeProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#describeprojectspaginator)
        """

if TYPE_CHECKING:
    _ListCollectionsPaginatorBase = Paginator[ListCollectionsResponseTypeDef]
else:
    _ListCollectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollectionsPaginator(_ListCollectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListCollections.html#Rekognition.Paginator.ListCollections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listcollectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListCollectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListCollections.html#Rekognition.Paginator.ListCollections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listcollectionspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetEntriesPaginatorBase = Paginator[ListDatasetEntriesResponseTypeDef]
else:
    _ListDatasetEntriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetEntriesPaginator(_ListDatasetEntriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListDatasetEntries.html#Rekognition.Paginator.ListDatasetEntries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listdatasetentriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetEntriesRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetEntriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListDatasetEntries.html#Rekognition.Paginator.ListDatasetEntries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listdatasetentriespaginator)
        """

if TYPE_CHECKING:
    _ListDatasetLabelsPaginatorBase = Paginator[ListDatasetLabelsResponseTypeDef]
else:
    _ListDatasetLabelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetLabelsPaginator(_ListDatasetLabelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListDatasetLabels.html#Rekognition.Paginator.ListDatasetLabels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listdatasetlabelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetLabelsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetLabelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListDatasetLabels.html#Rekognition.Paginator.ListDatasetLabels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listdatasetlabelspaginator)
        """

if TYPE_CHECKING:
    _ListFacesPaginatorBase = Paginator[ListFacesResponseTypeDef]
else:
    _ListFacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFacesPaginator(_ListFacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListFaces.html#Rekognition.Paginator.ListFaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listfacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFacesRequestPaginateTypeDef]
    ) -> PageIterator[ListFacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListFaces.html#Rekognition.Paginator.ListFaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listfacespaginator)
        """

if TYPE_CHECKING:
    _ListProjectPoliciesPaginatorBase = Paginator[ListProjectPoliciesResponseTypeDef]
else:
    _ListProjectPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectPoliciesPaginator(_ListProjectPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListProjectPolicies.html#Rekognition.Paginator.ListProjectPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listprojectpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListProjectPolicies.html#Rekognition.Paginator.ListProjectPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listprojectpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListStreamProcessorsPaginatorBase = Paginator[ListStreamProcessorsResponseTypeDef]
else:
    _ListStreamProcessorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamProcessorsPaginator(_ListStreamProcessorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListStreamProcessors.html#Rekognition.Paginator.ListStreamProcessors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#liststreamprocessorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamProcessorsRequestPaginateTypeDef]
    ) -> PageIterator[ListStreamProcessorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListStreamProcessors.html#Rekognition.Paginator.ListStreamProcessors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#liststreamprocessorspaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListUsers.html#Rekognition.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/paginator/ListUsers.html#Rekognition.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators/#listuserspaginator)
        """
