"""
Type annotations for elastictranscoder service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_elastictranscoder import ElasticTranscoderClient
    from mypy_boto3_elastictranscoder.waiter import (
        JobCompleteWaiter,
    )

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")

    job_complete_waiter: JobCompleteWaiter = client.get_waiter("job_complete")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("JobCompleteWaiter",)

class JobCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/waiters.html#jobcompletewaiter)
    """

    def wait(self, *, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/waiters.html#jobcompletewaiter)
        """
