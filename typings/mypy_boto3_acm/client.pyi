# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for acm service client

Usage::

    ```python
    import boto3
    from mypy_boto3_acm import ACMClient

    client: ACMClient = boto3.client("acm")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_acm.paginator import ListCertificatesPaginator
from mypy_boto3_acm.type_defs import (
    CertificateOptionsTypeDef,
    DescribeCertificateResponseTypeDef,
    DomainValidationOptionTypeDef,
    ExportCertificateResponseTypeDef,
    FiltersTypeDef,
    GetCertificateResponseTypeDef,
    ImportCertificateResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListTagsForCertificateResponseTypeDef,
    RequestCertificateResponseTypeDef,
    TagTypeDef,
)
from mypy_boto3_acm.waiter import CertificateValidatedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ACMClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InvalidArgsException: Type[Boto3ClientError]
    InvalidArnException: Type[Boto3ClientError]
    InvalidDomainValidationOptionsException: Type[Boto3ClientError]
    InvalidParameterException: Type[Boto3ClientError]
    InvalidStateException: Type[Boto3ClientError]
    InvalidTagException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    RequestInProgressException: Type[Boto3ClientError]
    ResourceInUseException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    TagPolicyException: Type[Boto3ClientError]
    TooManyTagsException: Type[Boto3ClientError]


class ACMClient:
    """
    [ACM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client)
    """

    exceptions: Exceptions

    def add_tags_to_certificate(self, CertificateArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.add_tags_to_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.add_tags_to_certificate)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.can_paginate)
        """

    def delete_certificate(self, CertificateArn: str) -> None:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.delete_certificate)
        """

    def describe_certificate(self, CertificateArn: str) -> DescribeCertificateResponseTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.describe_certificate)
        """

    def export_certificate(
        self, CertificateArn: str, Passphrase: Union[bytes, IO[bytes]]
    ) -> ExportCertificateResponseTypeDef:
        """
        [Client.export_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.export_certificate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.generate_presigned_url)
        """

    def get_certificate(self, CertificateArn: str) -> GetCertificateResponseTypeDef:
        """
        [Client.get_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.get_certificate)
        """

    def import_certificate(
        self,
        Certificate: Union[bytes, IO[bytes]],
        PrivateKey: Union[bytes, IO[bytes]],
        CertificateArn: str = None,
        CertificateChain: Union[bytes, IO[bytes]] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ImportCertificateResponseTypeDef:
        """
        [Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.import_certificate)
        """

    def list_certificates(
        self,
        CertificateStatuses: List[
            Literal[
                "PENDING_VALIDATION",
                "ISSUED",
                "INACTIVE",
                "EXPIRED",
                "VALIDATION_TIMED_OUT",
                "REVOKED",
                "FAILED",
            ]
        ] = None,
        Includes: FiltersTypeDef = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> ListCertificatesResponseTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.list_certificates)
        """

    def list_tags_for_certificate(
        self, CertificateArn: str
    ) -> ListTagsForCertificateResponseTypeDef:
        """
        [Client.list_tags_for_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.list_tags_for_certificate)
        """

    def remove_tags_from_certificate(self, CertificateArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.remove_tags_from_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.remove_tags_from_certificate)
        """

    def renew_certificate(self, CertificateArn: str) -> None:
        """
        [Client.renew_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.renew_certificate)
        """

    def request_certificate(
        self,
        DomainName: str,
        ValidationMethod: Literal["EMAIL", "DNS"] = None,
        SubjectAlternativeNames: List[str] = None,
        IdempotencyToken: str = None,
        DomainValidationOptions: List[DomainValidationOptionTypeDef] = None,
        Options: "CertificateOptionsTypeDef" = None,
        CertificateAuthorityArn: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> RequestCertificateResponseTypeDef:
        """
        [Client.request_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.request_certificate)
        """

    def resend_validation_email(
        self, CertificateArn: str, Domain: str, ValidationDomain: str
    ) -> None:
        """
        [Client.resend_validation_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.resend_validation_email)
        """

    def update_certificate_options(
        self, CertificateArn: str, Options: "CertificateOptionsTypeDef"
    ) -> None:
        """
        [Client.update_certificate_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Client.update_certificate_options)
        """

    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Paginator.ListCertificates)
        """

    def get_waiter(
        self, waiter_name: Literal["certificate_validated"]
    ) -> CertificateValidatedWaiter:
        """
        [Waiter.CertificateValidated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm.html#ACM.Waiter.CertificateValidated)
        """
