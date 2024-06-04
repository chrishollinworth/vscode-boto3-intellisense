"""
Main interface for sagemaker-geospatial service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_geospatial import (
        Client,
        ListEarthObservationJobsPaginator,
        ListRasterDataCollectionsPaginator,
        ListVectorEnrichmentJobsPaginator,
        SageMakergeospatialcapabilitiesClient,
    )

    session = boto3.Session()

    client: SageMakergeospatialcapabilitiesClient = boto3.client("sagemaker-geospatial")
    session_client: SageMakergeospatialcapabilitiesClient = session.client("sagemaker-geospatial")

    list_earth_observation_jobs_paginator: ListEarthObservationJobsPaginator = client.get_paginator("list_earth_observation_jobs")
    list_raster_data_collections_paginator: ListRasterDataCollectionsPaginator = client.get_paginator("list_raster_data_collections")
    list_vector_enrichment_jobs_paginator: ListVectorEnrichmentJobsPaginator = client.get_paginator("list_vector_enrichment_jobs")
    ```
"""

from .client import SageMakergeospatialcapabilitiesClient
from .paginator import (
    ListEarthObservationJobsPaginator,
    ListRasterDataCollectionsPaginator,
    ListVectorEnrichmentJobsPaginator,
)

Client = SageMakergeospatialcapabilitiesClient

__all__ = (
    "Client",
    "ListEarthObservationJobsPaginator",
    "ListRasterDataCollectionsPaginator",
    "ListVectorEnrichmentJobsPaginator",
    "SageMakergeospatialcapabilitiesClient",
)
