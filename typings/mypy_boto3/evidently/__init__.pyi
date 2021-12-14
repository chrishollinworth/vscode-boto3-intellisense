"""
Main interface for evidently service.

Usage::

    ```python
    import boto3
    from mypy_boto3_evidently import (
        Client,
        CloudWatchEvidentlyClient,
        ListExperimentsPaginator,
        ListFeaturesPaginator,
        ListLaunchesPaginator,
        ListProjectsPaginator,
    )

    session = boto3.Session()

    client: CloudWatchEvidentlyClient = boto3.client("evidently")
    session_client: CloudWatchEvidentlyClient = session.client("evidently")

    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_features_paginator: ListFeaturesPaginator = client.get_paginator("list_features")
    list_launches_paginator: ListLaunchesPaginator = client.get_paginator("list_launches")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from .client import CloudWatchEvidentlyClient
from .paginator import (
    ListExperimentsPaginator,
    ListFeaturesPaginator,
    ListLaunchesPaginator,
    ListProjectsPaginator,
)

Client = CloudWatchEvidentlyClient

__all__ = (
    "Client",
    "CloudWatchEvidentlyClient",
    "ListExperimentsPaginator",
    "ListFeaturesPaginator",
    "ListLaunchesPaginator",
    "ListProjectsPaginator",
)
