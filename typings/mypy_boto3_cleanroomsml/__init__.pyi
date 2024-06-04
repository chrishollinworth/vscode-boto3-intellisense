"""
Main interface for cleanroomsml service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cleanroomsml import (
        CleanRoomsMLClient,
        Client,
        ListAudienceExportJobsPaginator,
        ListAudienceGenerationJobsPaginator,
        ListAudienceModelsPaginator,
        ListConfiguredAudienceModelsPaginator,
        ListTrainingDatasetsPaginator,
    )

    session = boto3.Session()

    client: CleanRoomsMLClient = boto3.client("cleanroomsml")
    session_client: CleanRoomsMLClient = session.client("cleanroomsml")

    list_audience_export_jobs_paginator: ListAudienceExportJobsPaginator = client.get_paginator("list_audience_export_jobs")
    list_audience_generation_jobs_paginator: ListAudienceGenerationJobsPaginator = client.get_paginator("list_audience_generation_jobs")
    list_audience_models_paginator: ListAudienceModelsPaginator = client.get_paginator("list_audience_models")
    list_configured_audience_models_paginator: ListConfiguredAudienceModelsPaginator = client.get_paginator("list_configured_audience_models")
    list_training_datasets_paginator: ListTrainingDatasetsPaginator = client.get_paginator("list_training_datasets")
    ```
"""

from .client import CleanRoomsMLClient
from .paginator import (
    ListAudienceExportJobsPaginator,
    ListAudienceGenerationJobsPaginator,
    ListAudienceModelsPaginator,
    ListConfiguredAudienceModelsPaginator,
    ListTrainingDatasetsPaginator,
)

Client = CleanRoomsMLClient

__all__ = (
    "CleanRoomsMLClient",
    "Client",
    "ListAudienceExportJobsPaginator",
    "ListAudienceGenerationJobsPaginator",
    "ListAudienceModelsPaginator",
    "ListConfiguredAudienceModelsPaginator",
    "ListTrainingDatasetsPaginator",
)
