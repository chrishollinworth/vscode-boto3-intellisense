"""
Type annotations for acm service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_acm import ACMClient

    client: ACMClient = boto3.client("acm")
    ```
"""

import sys
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import CertificateStatusType, KeyAlgorithmType, SortOrderType, ValidationMethodType
from .paginator import ListCertificatesPaginator
from .type_defs import (
    CertificateOptionsTypeDef,
    DescribeCertificateResponseTypeDef,
    DomainValidationOptionTypeDef,
    ExpiryEventsConfigurationTypeDef,
    ExportCertificateResponseTypeDef,
    FiltersTypeDef,
    GetAccountConfigurationResponseTypeDef,
    GetCertificateResponseTypeDef,
    ImportCertificateResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListTagsForCertificateResponseTypeDef,
    RequestCertificateResponseTypeDef,
    TagTypeDef,
)
from .waiter import CertificateValidatedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ACMClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InvalidArgsException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidDomainValidationOptionsException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    RequestInProgressException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagPolicyException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ACMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ACMClient exceptions.
        """

    def add_tags_to_certificate(self, *, CertificateArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        Adds one or more tags to an ACM certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.add_tags_to_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#add_tags_to_certificate)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#close)
        """

    def delete_certificate(self, *, CertificateArn: str) -> None:
        """
        Deletes a certificate and its associated private key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.delete_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#delete_certificate)
        """

    def describe_certificate(self, *, CertificateArn: str) -> DescribeCertificateResponseTypeDef:
        """
        Returns detailed metadata about the specified ACM certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.describe_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#describe_certificate)
        """

    def export_certificate(
        self, *, CertificateArn: str, Passphrase: Union[bytes, IO[bytes], StreamingBody]
    ) -> ExportCertificateResponseTypeDef:
        """
        Exports a private certificate issued by a private certificate authority (CA) for
        use anywhere.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.export_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#export_certificate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#generate_presigned_url)
        """

    def get_account_configuration(self) -> GetAccountConfigurationResponseTypeDef:
        """
        Returns the account configuration options associated with an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.get_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#get_account_configuration)
        """

    def get_certificate(self, *, CertificateArn: str) -> GetCertificateResponseTypeDef:
        """
        Retrieves an Amazon-issued certificate and its certificate chain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.get_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#get_certificate)
        """

    def import_certificate(
        self,
        *,
        Certificate: Union[bytes, IO[bytes], StreamingBody],
        PrivateKey: Union[bytes, IO[bytes], StreamingBody],
        CertificateArn: str = None,
        CertificateChain: Union[bytes, IO[bytes], StreamingBody] = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportCertificateResponseTypeDef:
        """
        Imports a certificate into Certificate Manager (ACM) to use with services that
        are integrated with ACM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.import_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#import_certificate)
        """

    def list_certificates(
        self,
        *,
        CertificateStatuses: List[CertificateStatusType] = None,
        Includes: "FiltersTypeDef" = None,
        NextToken: str = None,
        MaxItems: int = None,
        SortBy: Literal["CREATED_AT"] = None,
        SortOrder: SortOrderType = None
    ) -> ListCertificatesResponseTypeDef:
        """
        Retrieves a list of certificate ARNs and domain names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.list_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#list_certificates)
        """

    def list_tags_for_certificate(
        self, *, CertificateArn: str
    ) -> ListTagsForCertificateResponseTypeDef:
        """
        Lists the tags that have been applied to the ACM certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.list_tags_for_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#list_tags_for_certificate)
        """

    def put_account_configuration(
        self, *, IdempotencyToken: str, ExpiryEvents: "ExpiryEventsConfigurationTypeDef" = None
    ) -> None:
        """
        Adds or modifies account-level configurations in ACM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.put_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#put_account_configuration)
        """

    def remove_tags_from_certificate(
        self, *, CertificateArn: str, Tags: List["TagTypeDef"]
    ) -> None:
        """
        Remove one or more tags from an ACM certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.remove_tags_from_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#remove_tags_from_certificate)
        """

    def renew_certificate(self, *, CertificateArn: str) -> None:
        """
        Renews an eligible ACM certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.renew_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#renew_certificate)
        """

    def request_certificate(
        self,
        *,
        DomainName: str,
        ValidationMethod: ValidationMethodType = None,
        SubjectAlternativeNames: List[str] = None,
        IdempotencyToken: str = None,
        DomainValidationOptions: List["DomainValidationOptionTypeDef"] = None,
        Options: "CertificateOptionsTypeDef" = None,
        CertificateAuthorityArn: str = None,
        Tags: List["TagTypeDef"] = None,
        KeyAlgorithm: KeyAlgorithmType = None
    ) -> RequestCertificateResponseTypeDef:
        """
        Requests an ACM certificate for use with other Amazon Web Services services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.request_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#request_certificate)
        """

    def resend_validation_email(
        self, *, CertificateArn: str, Domain: str, ValidationDomain: str
    ) -> None:
        """
        Resends the email that requests domain ownership validation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.resend_validation_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#resend_validation_email)
        """

    def update_certificate_options(
        self, *, CertificateArn: str, Options: "CertificateOptionsTypeDef"
    ) -> None:
        """
        Updates a certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Client.update_certificate_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/client.html#update_certificate_options)
        """

    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Paginator.ListCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/paginators.html#listcertificatespaginator)
        """

    def get_waiter(
        self, waiter_name: Literal["certificate_validated"]
    ) -> CertificateValidatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/acm.html#ACM.Waiter.CertificateValidated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/waiters.html#certificatevalidatedwaiter)
        """
