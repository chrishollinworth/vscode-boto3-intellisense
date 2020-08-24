# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for acm service client waiters.

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

from mypy_boto3_acm.type_defs import WaiterConfigTypeDef

__all__ = ("CertificateValidatedWaiter",)


class CertificateValidatedWaiter(Boto3Waiter):
    """
    [Waiter.CertificateValidated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Waiter.CertificateValidated)
    """

    def wait(self, CertificateArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [CertificateValidated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Waiter.CertificateValidated.wait)
        """
