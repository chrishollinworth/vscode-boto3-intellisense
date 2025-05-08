"""
Main interface for codeguru-reviewer service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codeguru_reviewer import (
        Client,
        CodeGuruReviewerClient,
        CodeReviewCompletedWaiter,
        ListRepositoryAssociationsPaginator,
        RepositoryAssociationSucceededWaiter,
    )

    session = Session()
    client: CodeGuruReviewerClient = session.client("codeguru-reviewer")

    code_review_completed_waiter: CodeReviewCompletedWaiter = client.get_waiter("code_review_completed")
    repository_association_succeeded_waiter: RepositoryAssociationSucceededWaiter = client.get_waiter("repository_association_succeeded")

    list_repository_associations_paginator: ListRepositoryAssociationsPaginator = client.get_paginator("list_repository_associations")
    ```
"""

from .client import CodeGuruReviewerClient
from .paginator import ListRepositoryAssociationsPaginator
from .waiter import CodeReviewCompletedWaiter, RepositoryAssociationSucceededWaiter

Client = CodeGuruReviewerClient

__all__ = (
    "Client",
    "CodeGuruReviewerClient",
    "CodeReviewCompletedWaiter",
    "ListRepositoryAssociationsPaginator",
    "RepositoryAssociationSucceededWaiter",
)
