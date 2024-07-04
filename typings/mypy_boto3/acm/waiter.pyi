"""
Type annotations for acm service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_acm import ACMClient
    from mypy_boto3_acm.waiter import (
        CertificateValidatedWaiter,
    )

    client: ACMClient = boto3.client("acm")

    certificate_validated_waiter: CertificateValidatedWaiter = client.get_waiter("certificate_validated")
    ```
"""

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("CertificateValidatedWaiter",)

class CertificateValidatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/acm.html#ACM.Waiter.CertificateValidated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/waiters.html#certificatevalidatedwaiter)
    """

    def wait(self, *, CertificateArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/acm.html#ACM.Waiter.CertificateValidated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/waiters.html#certificatevalidatedwaiter)
        """
