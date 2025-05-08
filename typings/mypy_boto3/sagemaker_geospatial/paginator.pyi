"""
Type annotations for sagemaker-geospatial service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient
    from mypy_boto3_sagemaker_geospatial.paginator import (
        ListEarthObservationJobsPaginator,
        ListRasterDataCollectionsPaginator,
        ListVectorEnrichmentJobsPaginator,
    )

    session = Session()
    client: SageMakergeospatialcapabilitiesClient = session.client("sagemaker-geospatial")

    list_earth_observation_jobs_paginator: ListEarthObservationJobsPaginator = client.get_paginator("list_earth_observation_jobs")
    list_raster_data_collections_paginator: ListRasterDataCollectionsPaginator = client.get_paginator("list_raster_data_collections")
    list_vector_enrichment_jobs_paginator: ListVectorEnrichmentJobsPaginator = client.get_paginator("list_vector_enrichment_jobs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEarthObservationJobInputPaginateTypeDef,
    ListEarthObservationJobOutputTypeDef,
    ListRasterDataCollectionsInputPaginateTypeDef,
    ListRasterDataCollectionsOutputTypeDef,
    ListVectorEnrichmentJobInputPaginateTypeDef,
    ListVectorEnrichmentJobOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListEarthObservationJobsPaginator",
    "ListRasterDataCollectionsPaginator",
    "ListVectorEnrichmentJobsPaginator",
)

if TYPE_CHECKING:
    _ListEarthObservationJobsPaginatorBase = Paginator[ListEarthObservationJobOutputTypeDef]
else:
    _ListEarthObservationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEarthObservationJobsPaginator(_ListEarthObservationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial/paginator/ListEarthObservationJobs.html#SageMakergeospatialcapabilities.Paginator.ListEarthObservationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators/#listearthobservationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEarthObservationJobInputPaginateTypeDef]
    ) -> PageIterator[ListEarthObservationJobOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial/paginator/ListEarthObservationJobs.html#SageMakergeospatialcapabilities.Paginator.ListEarthObservationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators/#listearthobservationjobspaginator)
        """

if TYPE_CHECKING:
    _ListRasterDataCollectionsPaginatorBase = Paginator[ListRasterDataCollectionsOutputTypeDef]
else:
    _ListRasterDataCollectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRasterDataCollectionsPaginator(_ListRasterDataCollectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial/paginator/ListRasterDataCollections.html#SageMakergeospatialcapabilities.Paginator.ListRasterDataCollections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators/#listrasterdatacollectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRasterDataCollectionsInputPaginateTypeDef]
    ) -> PageIterator[ListRasterDataCollectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial/paginator/ListRasterDataCollections.html#SageMakergeospatialcapabilities.Paginator.ListRasterDataCollections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators/#listrasterdatacollectionspaginator)
        """

if TYPE_CHECKING:
    _ListVectorEnrichmentJobsPaginatorBase = Paginator[ListVectorEnrichmentJobOutputTypeDef]
else:
    _ListVectorEnrichmentJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVectorEnrichmentJobsPaginator(_ListVectorEnrichmentJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial/paginator/ListVectorEnrichmentJobs.html#SageMakergeospatialcapabilities.Paginator.ListVectorEnrichmentJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators/#listvectorenrichmentjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVectorEnrichmentJobInputPaginateTypeDef]
    ) -> PageIterator[ListVectorEnrichmentJobOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial/paginator/ListVectorEnrichmentJobs.html#SageMakergeospatialcapabilities.Paginator.ListVectorEnrichmentJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/paginators/#listvectorenrichmentjobspaginator)
        """
