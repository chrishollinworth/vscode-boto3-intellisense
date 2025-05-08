"""
Type annotations for codeguru-reviewer service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codeguru_reviewer.client import CodeGuruReviewerClient
    from mypy_boto3_codeguru_reviewer.waiter import (
        CodeReviewCompletedWaiter,
        RepositoryAssociationSucceededWaiter,
    )

    session = Session()
    client: CodeGuruReviewerClient = session.client("codeguru-reviewer")

    code_review_completed_waiter: CodeReviewCompletedWaiter = client.get_waiter("code_review_completed")
    repository_association_succeeded_waiter: RepositoryAssociationSucceededWaiter = client.get_waiter("repository_association_succeeded")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeCodeReviewRequestWaitTypeDef,
    DescribeRepositoryAssociationRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CodeReviewCompletedWaiter", "RepositoryAssociationSucceededWaiter")

class CodeReviewCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer/waiter/CodeReviewCompleted.html#CodeGuruReviewer.Waiter.CodeReviewCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/waiters/#codereviewcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCodeReviewRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer/waiter/CodeReviewCompleted.html#CodeGuruReviewer.Waiter.CodeReviewCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/waiters/#codereviewcompletedwaiter)
        """

class RepositoryAssociationSucceededWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer/waiter/RepositoryAssociationSucceeded.html#CodeGuruReviewer.Waiter.RepositoryAssociationSucceeded)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/waiters/#repositoryassociationsucceededwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRepositoryAssociationRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer/waiter/RepositoryAssociationSucceeded.html#CodeGuruReviewer.Waiter.RepositoryAssociationSucceeded.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/waiters/#repositoryassociationsucceededwaiter)
        """
