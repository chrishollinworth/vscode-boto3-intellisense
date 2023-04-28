"""
Type annotations for sagemaker-geospatial service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker_geospatial import SageMakergeospatialcapabilitiesClient
    from mypy_boto3_sagemaker_geospatial.paginator import (
        ListEarthObservationJobsPaginator,
        ListRasterDataCollectionsPaginator,
        ListVectorEnrichmentJobsPaginator,
    )

    client: SageMakergeospatialcapabilitiesClient = boto3.client("sagemaker-geospatial")

    list_earth_observation_jobs_paginator: ListEarthObservationJobsPaginator = client.get_paginator("list_earth_observation_jobs")
    list_raster_data_collections_paginator: ListRasterDataCollectionsPaginator = client.get_paginator("list_raster_data_collections")
    list_vector_enrichment_jobs_paginator: ListVectorEnrichmentJobsPaginator = client.get_paginator("list_vector_enrichment_jobs")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import EarthObservationJobStatusType, SortOrderType
from .type_defs import (
    ListEarthObservationJobOutputTypeDef,
    ListRasterDataCollectionsOutputTypeDef,
    ListVectorEnrichmentJobOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListEarthObservationJobsPaginator",
    "ListRasterDataCollectionsPaginator",
    "ListVectorEnrichmentJobsPaginator",
)

class ListEarthObservationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/sagemaker-geospatial.html#SageMakergeospatialcapabilities.Paginator.ListEarthObservationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators.html#listearthobservationjobspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: str = None,
        SortOrder: SortOrderType = None,
        StatusEquals: EarthObservationJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEarthObservationJobOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/sagemaker-geospatial.html#SageMakergeospatialcapabilities.Paginator.ListEarthObservationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators.html#listearthobservationjobspaginator)
        """

class ListRasterDataCollectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/sagemaker-geospatial.html#SageMakergeospatialcapabilities.Paginator.ListRasterDataCollections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators.html#listrasterdatacollectionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRasterDataCollectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/sagemaker-geospatial.html#SageMakergeospatialcapabilities.Paginator.ListRasterDataCollections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators.html#listrasterdatacollectionspaginator)
        """

class ListVectorEnrichmentJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/sagemaker-geospatial.html#SageMakergeospatialcapabilities.Paginator.ListVectorEnrichmentJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators.html#listvectorenrichmentjobspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: str = None,
        SortOrder: SortOrderType = None,
        StatusEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVectorEnrichmentJobOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/sagemaker-geospatial.html#SageMakergeospatialcapabilities.Paginator.ListVectorEnrichmentJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators.html#listvectorenrichmentjobspaginator)
        """
