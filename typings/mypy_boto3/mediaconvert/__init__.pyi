"""
Main interface for mediaconvert service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediaconvert import (
        Client,
        DescribeEndpointsPaginator,
        ListJobTemplatesPaginator,
        ListJobsPaginator,
        ListPresetsPaginator,
        ListQueuesPaginator,
        ListVersionsPaginator,
        MediaConvertClient,
        SearchJobsPaginator,
    )

    session = Session()
    client: MediaConvertClient = session.client("mediaconvert")

    describe_endpoints_paginator: DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
    list_job_templates_paginator: ListJobTemplatesPaginator = client.get_paginator("list_job_templates")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    list_versions_paginator: ListVersionsPaginator = client.get_paginator("list_versions")
    search_jobs_paginator: SearchJobsPaginator = client.get_paginator("search_jobs")
    ```
"""

from .client import MediaConvertClient
from .paginator import (
    DescribeEndpointsPaginator,
    ListJobsPaginator,
    ListJobTemplatesPaginator,
    ListPresetsPaginator,
    ListQueuesPaginator,
    ListVersionsPaginator,
    SearchJobsPaginator,
)

Client = MediaConvertClient

__all__ = (
    "Client",
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
    "ListVersionsPaginator",
    "MediaConvertClient",
    "SearchJobsPaginator",
)
