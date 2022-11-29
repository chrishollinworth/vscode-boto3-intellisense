"""
Type annotations for signer service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_signer import signerClient
    from mypy_boto3_signer.waiter import (
        SuccessfulSigningJobWaiter,
    )

    client: signerClient = boto3.client("signer")

    successful_signing_job_waiter: SuccessfulSigningJobWaiter = client.get_waiter("successful_signing_job")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("SuccessfulSigningJobWaiter",)

class SuccessfulSigningJobWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/signer.html#signer.Waiter.SuccessfulSigningJob)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/waiters.html#successfulsigningjobwaiter)
    """

    def wait(self, *, jobId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/signer.html#signer.Waiter.SuccessfulSigningJob.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/waiters.html#successfulsigningjobwaiter)
        """
