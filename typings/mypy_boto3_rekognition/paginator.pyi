# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for rekognition service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_rekognition import RekognitionClient
    from mypy_boto3_rekognition.paginator import (
        DescribeProjectVersionsPaginator,
        DescribeProjectsPaginator,
        ListCollectionsPaginator,
        ListFacesPaginator,
        ListStreamProcessorsPaginator,
    )

    client: RekognitionClient = boto3.client("rekognition")

    describe_project_versions_paginator: DescribeProjectVersionsPaginator = client.get_paginator("describe_project_versions")
    describe_projects_paginator: DescribeProjectsPaginator = client.get_paginator("describe_projects")
    list_collections_paginator: ListCollectionsPaginator = client.get_paginator("list_collections")
    list_faces_paginator: ListFacesPaginator = client.get_paginator("list_faces")
    list_stream_processors_paginator: ListStreamProcessorsPaginator = client.get_paginator("list_stream_processors")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_rekognition.type_defs import (
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListFacesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
)


class DescribeProjectVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeProjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)
    """

    def paginate(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeProjectVersionsResponseTypeDef]:
        """
        [DescribeProjectVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions.paginate)
        """


class DescribeProjectsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeProjectsResponseTypeDef]:
        """
        [DescribeProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects.paginate)
        """


class ListCollectionsPaginator(Boto3Paginator):
    """
    [Paginator.ListCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollectionsResponseTypeDef]:
        """
        [ListCollections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListCollections.paginate)
        """


class ListFacesPaginator(Boto3Paginator):
    """
    [Paginator.ListFaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)
    """

    def paginate(
        self, CollectionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFacesResponseTypeDef]:
        """
        [ListFaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListFaces.paginate)
        """


class ListStreamProcessorsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamProcessors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamProcessorsResponseTypeDef]:
        """
        [ListStreamProcessors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors.paginate)
        """
