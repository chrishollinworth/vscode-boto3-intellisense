# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for acm-pca service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_acm_pca import ACMPCAClient
    from mypy_boto3_acm_pca.waiter import (
        AuditReportCreatedWaiter,
        CertificateAuthorityCSRCreatedWaiter,
        CertificateIssuedWaiter,
    )

    client: ACMPCAClient = boto3.client("acm-pca")

    audit_report_created_waiter: AuditReportCreatedWaiter = client.get_waiter("audit_report_created")
    certificate_authority_csr_created_waiter: CertificateAuthorityCSRCreatedWaiter = client.get_waiter("certificate_authority_csr_created")
    certificate_issued_waiter: CertificateIssuedWaiter = client.get_waiter("certificate_issued")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_acm_pca.type_defs import WaiterConfigTypeDef

__all__ = (
    "AuditReportCreatedWaiter",
    "CertificateAuthorityCSRCreatedWaiter",
    "CertificateIssuedWaiter",
)


class AuditReportCreatedWaiter(Boto3Waiter):
    """
    [Waiter.AuditReportCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.AuditReportCreated)
    """

    def wait(
        self,
        CertificateAuthorityArn: str,
        AuditReportId: str,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [AuditReportCreated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.AuditReportCreated.wait)
        """


class CertificateAuthorityCSRCreatedWaiter(Boto3Waiter):
    """
    [Waiter.CertificateAuthorityCSRCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated)
    """

    def wait(self, CertificateAuthorityArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [CertificateAuthorityCSRCreated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated.wait)
        """


class CertificateIssuedWaiter(Boto3Waiter):
    """
    [Waiter.CertificateIssued documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateIssued)
    """

    def wait(
        self,
        CertificateAuthorityArn: str,
        CertificateArn: str,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CertificateIssued.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateIssued.wait)
        """
