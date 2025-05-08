"""
Type annotations for elastictranscoder service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elastictranscoder.client import ElasticTranscoderClient
    from mypy_boto3_elastictranscoder.waiter import (
        JobCompleteWaiter,
    )

    session = Session()
    client: ElasticTranscoderClient = session.client("elastictranscoder")

    job_complete_waiter: JobCompleteWaiter = client.get_waiter("job_complete")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import ReadJobRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("JobCompleteWaiter",)

class JobCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/waiter/JobComplete.html#ElasticTranscoder.Waiter.JobComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/waiters/#jobcompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[ReadJobRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/waiter/JobComplete.html#ElasticTranscoder.Waiter.JobComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/waiters/#jobcompletewaiter)
        """
