"""
Type annotations for taxsettings service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_taxsettings import TaxSettingsClient

    client: TaxSettingsClient = boto3.client("taxsettings")
    ```
"""

import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListTaxRegistrationsPaginator
from .type_defs import (
    BatchDeleteTaxRegistrationResponseTypeDef,
    BatchPutTaxRegistrationResponseTypeDef,
    DestinationS3LocationTypeDef,
    GetTaxRegistrationDocumentResponseTypeDef,
    GetTaxRegistrationResponseTypeDef,
    ListTaxRegistrationsResponseTypeDef,
    PutTaxRegistrationResponseTypeDef,
    TaxDocumentMetadataTypeDef,
    TaxRegistrationEntryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TaxSettingsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TaxSettingsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TaxSettingsClient exceptions.
        """

    def batch_delete_tax_registration(
        self, *, accountIds: List[str]
    ) -> BatchDeleteTaxRegistrationResponseTypeDef:
        """
        Deletes tax registration for multiple accounts in batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.batch_delete_tax_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#batch_delete_tax_registration)
        """

    def batch_put_tax_registration(
        self, *, accountIds: List[str], taxRegistrationEntry: "TaxRegistrationEntryTypeDef"
    ) -> BatchPutTaxRegistrationResponseTypeDef:
        """
        Adds or updates tax registration for multiple accounts in batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.batch_put_tax_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#batch_put_tax_registration)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#close)
        """

    def delete_tax_registration(self, *, accountId: str = None) -> Dict[str, Any]:
        """
        Deletes tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.delete_tax_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#delete_tax_registration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#generate_presigned_url)
        """

    def get_tax_registration(self, *, accountId: str = None) -> GetTaxRegistrationResponseTypeDef:
        """
        Retrieves tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.get_tax_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#get_tax_registration)
        """

    def get_tax_registration_document(
        self,
        *,
        destinationS3Location: "DestinationS3LocationTypeDef",
        taxDocumentMetadata: "TaxDocumentMetadataTypeDef"
    ) -> GetTaxRegistrationDocumentResponseTypeDef:
        """
        Downloads your tax documents to the Amazon S3 bucket that you specify in your
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.get_tax_registration_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#get_tax_registration_document)
        """

    def list_tax_registrations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListTaxRegistrationsResponseTypeDef:
        """
        Retrieves the tax registration of accounts listed in a consolidated billing
        family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.list_tax_registrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#list_tax_registrations)
        """

    def put_tax_registration(
        self, *, taxRegistrationEntry: "TaxRegistrationEntryTypeDef", accountId: str = None
    ) -> PutTaxRegistrationResponseTypeDef:
        """
        Adds or updates tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Client.put_tax_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client.html#put_tax_registration)
        """

    def get_paginator(
        self, operation_name: Literal["list_tax_registrations"]
    ) -> ListTaxRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/taxsettings.html#TaxSettings.Paginator.ListTaxRegistrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators.html#listtaxregistrationspaginator)
        """
