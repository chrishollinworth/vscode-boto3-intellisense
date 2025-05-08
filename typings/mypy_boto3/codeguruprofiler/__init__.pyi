"""
Main interface for codeguruprofiler service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codeguruprofiler import (
        Client,
        CodeGuruProfilerClient,
        ListProfileTimesPaginator,
    )

    session = Session()
    client: CodeGuruProfilerClient = session.client("codeguruprofiler")

    list_profile_times_paginator: ListProfileTimesPaginator = client.get_paginator("list_profile_times")
    ```
"""

from .client import CodeGuruProfilerClient
from .paginator import ListProfileTimesPaginator

Client = CodeGuruProfilerClient

__all__ = ("Client", "CodeGuruProfilerClient", "ListProfileTimesPaginator")
