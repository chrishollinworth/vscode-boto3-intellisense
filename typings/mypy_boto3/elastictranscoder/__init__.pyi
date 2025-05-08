"""
Main interface for elastictranscoder service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_elastictranscoder import (
        Client,
        ElasticTranscoderClient,
        JobCompleteWaiter,
        ListJobsByPipelinePaginator,
        ListJobsByStatusPaginator,
        ListPipelinesPaginator,
        ListPresetsPaginator,
    )

    session = Session()
    client: ElasticTranscoderClient = session.client("elastictranscoder")

    job_complete_waiter: JobCompleteWaiter = client.get_waiter("job_complete")

    list_jobs_by_pipeline_paginator: ListJobsByPipelinePaginator = client.get_paginator("list_jobs_by_pipeline")
    list_jobs_by_status_paginator: ListJobsByStatusPaginator = client.get_paginator("list_jobs_by_status")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
    ```
"""

from .client import ElasticTranscoderClient
from .paginator import (
    ListJobsByPipelinePaginator,
    ListJobsByStatusPaginator,
    ListPipelinesPaginator,
    ListPresetsPaginator,
)
from .waiter import JobCompleteWaiter

Client = ElasticTranscoderClient

__all__ = (
    "Client",
    "ElasticTranscoderClient",
    "JobCompleteWaiter",
    "ListJobsByPipelinePaginator",
    "ListJobsByStatusPaginator",
    "ListPipelinesPaginator",
    "ListPresetsPaginator",
)
