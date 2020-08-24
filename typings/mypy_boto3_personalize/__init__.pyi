"""
Main interface for personalize service.

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize import (
        Client,
        ListBatchInferenceJobsPaginator,
        ListCampaignsPaginator,
        ListDatasetGroupsPaginator,
        ListDatasetImportJobsPaginator,
        ListDatasetsPaginator,
        ListEventTrackersPaginator,
        ListRecipesPaginator,
        ListSchemasPaginator,
        ListSolutionVersionsPaginator,
        ListSolutionsPaginator,
        PersonalizeClient,
    )

    session = boto3.Session()

    client: PersonalizeClient = boto3.client("personalize")
    session_client: PersonalizeClient = session.client("personalize")

    list_batch_inference_jobs_paginator: ListBatchInferenceJobsPaginator = client.get_paginator("list_batch_inference_jobs")
    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
    list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_event_trackers_paginator: ListEventTrackersPaginator = client.get_paginator("list_event_trackers")
    list_recipes_paginator: ListRecipesPaginator = client.get_paginator("list_recipes")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_solution_versions_paginator: ListSolutionVersionsPaginator = client.get_paginator("list_solution_versions")
    list_solutions_paginator: ListSolutionsPaginator = client.get_paginator("list_solutions")
    ```
"""
from mypy_boto3_personalize.client import PersonalizeClient
from mypy_boto3_personalize.paginator import (
    ListBatchInferenceJobsPaginator,
    ListCampaignsPaginator,
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListEventTrackersPaginator,
    ListRecipesPaginator,
    ListSchemasPaginator,
    ListSolutionsPaginator,
    ListSolutionVersionsPaginator,
)

Client = PersonalizeClient


__all__ = (
    "Client",
    "ListBatchInferenceJobsPaginator",
    "ListCampaignsPaginator",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListEventTrackersPaginator",
    "ListRecipesPaginator",
    "ListSchemasPaginator",
    "ListSolutionVersionsPaginator",
    "ListSolutionsPaginator",
    "PersonalizeClient",
)
