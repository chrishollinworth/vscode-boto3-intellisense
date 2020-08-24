"""
Main interface for codeguru-reviewer service.

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguru_reviewer import (
        Client,
        CodeGuruReviewerClient,
        ListRepositoryAssociationsPaginator,
    )

    session = boto3.Session()

    client: CodeGuruReviewerClient = boto3.client("codeguru-reviewer")
    session_client: CodeGuruReviewerClient = session.client("codeguru-reviewer")

    list_repository_associations_paginator: ListRepositoryAssociationsPaginator = client.get_paginator("list_repository_associations")
    ```
"""
from mypy_boto3_codeguru_reviewer.client import CodeGuruReviewerClient
from mypy_boto3_codeguru_reviewer.paginator import ListRepositoryAssociationsPaginator

Client = CodeGuruReviewerClient


__all__ = ("Client", "CodeGuruReviewerClient", "ListRepositoryAssociationsPaginator")
