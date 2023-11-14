"""
Main interface for codeguruprofiler service.

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguruprofiler import (
        Client,
        CodeGuruProfilerClient,
        ListProfileTimesPaginator,
    )

    session = boto3.Session()

    client: CodeGuruProfilerClient = boto3.client("codeguruprofiler")
    session_client: CodeGuruProfilerClient = session.client("codeguruprofiler")

    list_profile_times_paginator: ListProfileTimesPaginator = client.get_paginator("list_profile_times")
    ```
"""
from .client import CodeGuruProfilerClient
from .paginator import ListProfileTimesPaginator

Client = CodeGuruProfilerClient

__all__ = ("Client", "CodeGuruProfilerClient", "ListProfileTimesPaginator")
