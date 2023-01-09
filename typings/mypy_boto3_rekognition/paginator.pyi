"""
Type annotations for rekognition service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_rekognition import RekognitionClient
    from mypy_boto3_rekognition.paginator import (
        DescribeProjectVersionsPaginator,
        DescribeProjectsPaginator,
        ListCollectionsPaginator,
        ListDatasetEntriesPaginator,
        ListDatasetLabelsPaginator,
        ListFacesPaginator,
        ListProjectPoliciesPaginator,
        ListStreamProcessorsPaginator,
    )

    client: RekognitionClient = boto3.client("rekognition")

    describe_project_versions_paginator: DescribeProjectVersionsPaginator = client.get_paginator("describe_project_versions")
    describe_projects_paginator: DescribeProjectsPaginator = client.get_paginator("describe_projects")
    list_collections_paginator: ListCollectionsPaginator = client.get_paginator("list_collections")
    list_dataset_entries_paginator: ListDatasetEntriesPaginator = client.get_paginator("list_dataset_entries")
    list_dataset_labels_paginator: ListDatasetLabelsPaginator = client.get_paginator("list_dataset_labels")
    list_faces_paginator: ListFacesPaginator = client.get_paginator("list_faces")
    list_project_policies_paginator: ListProjectPoliciesPaginator = client.get_paginator("list_project_policies")
    list_stream_processors_paginator: ListStreamProcessorsPaginator = client.get_paginator("list_stream_processors")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListDatasetLabelsResponseTypeDef,
    ListFacesResponseTypeDef,
    ListProjectPoliciesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListDatasetEntriesPaginator",
    "ListDatasetLabelsPaginator",
    "ListFacesPaginator",
    "ListProjectPoliciesPaginator",
    "ListStreamProcessorsPaginator",
)

class DescribeProjectVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectversionspaginator)
    """

    def paginate(
        self,
        *,
        ProjectArn: str,
        VersionNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeProjectVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectversionspaginator)
        """

class DescribeProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectspaginator)
    """

    def paginate(
        self, *, ProjectNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectspaginator)
        """

class ListCollectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listcollectionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListCollections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listcollectionspaginator)
        """

class ListDatasetEntriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListDatasetEntries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listdatasetentriespaginator)
    """

    def paginate(
        self,
        *,
        DatasetArn: str,
        ContainsLabels: List[str] = None,
        Labeled: bool = None,
        SourceRefContains: str = None,
        HasErrors: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetEntriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListDatasetEntries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listdatasetentriespaginator)
        """

class ListDatasetLabelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListDatasetLabels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listdatasetlabelspaginator)
    """

    def paginate(
        self, *, DatasetArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetLabelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListDatasetLabels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listdatasetlabelspaginator)
        """

class ListFacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listfacespaginator)
    """

    def paginate(
        self, *, CollectionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListFaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listfacespaginator)
        """

class ListProjectPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListProjectPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listprojectpoliciespaginator)
    """

    def paginate(
        self, *, ProjectArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListProjectPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listprojectpoliciespaginator)
        """

class ListStreamProcessorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#liststreamprocessorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamProcessorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#liststreamprocessorspaginator)
        """
