"""
Main interface for sagemaker-geospatial service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_geospatial import (
        Client,
        ListEarthObservationJobsPaginator,
        ListRasterDataCollectionsPaginator,
        ListVectorEnrichmentJobsPaginator,
        SageMakergeospatialcapabilitiesClient,
    )

    session = Session()
    client: SageMakergeospatialcapabilitiesClient = session.client("sagemaker-geospatial")

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
