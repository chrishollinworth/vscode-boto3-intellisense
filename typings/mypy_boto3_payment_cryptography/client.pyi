"""
Type annotations for payment-cryptography service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_payment_cryptography import PaymentCryptographyControlPlaneClient

    client: PaymentCryptographyControlPlaneClient = boto3.client("payment-cryptography")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    KeyAlgorithmType,
    KeyCheckValueAlgorithmType,
    KeyMaterialTypeType,
    KeyStateType,
)
from .paginator import ListAliasesPaginator, ListKeysPaginator, ListTagsForResourcePaginator
from .type_defs import (
    CreateAliasOutputTypeDef,
    CreateKeyOutputTypeDef,
    DeleteKeyOutputTypeDef,
    ExportAttributesTypeDef,
    ExportKeyMaterialTypeDef,
    ExportKeyOutputTypeDef,
    GetAliasOutputTypeDef,
    GetKeyOutputTypeDef,
    GetParametersForExportOutputTypeDef,
    GetParametersForImportOutputTypeDef,
    GetPublicKeyCertificateOutputTypeDef,
    ImportKeyMaterialTypeDef,
    ImportKeyOutputTypeDef,
    KeyAttributesTypeDef,
    ListAliasesOutputTypeDef,
    ListKeysOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    RestoreKeyOutputTypeDef,
    StartKeyUsageOutputTypeDef,
    StopKeyUsageOutputTypeDef,
    TagTypeDef,
    UpdateAliasOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PaymentCryptographyControlPlaneClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PaymentCryptographyControlPlaneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PaymentCryptographyControlPlaneClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#close)
        """

    def create_alias(self, *, AliasName: str, KeyArn: str = None) -> CreateAliasOutputTypeDef:
        """
        Creates an *alias*, or a friendly name, for an Amazon Web Services Payment
        Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#create_alias)
        """

    def create_key(
        self,
        *,
        KeyAttributes: "KeyAttributesTypeDef",
        Exportable: bool,
        KeyCheckValueAlgorithm: KeyCheckValueAlgorithmType = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateKeyOutputTypeDef:
        """
        Creates an Amazon Web Services Payment Cryptography key, a logical
        representation of a cryptographic key, that is unique in your account and Amazon
        Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.create_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#create_key)
        """

    def delete_alias(self, *, AliasName: str) -> Dict[str, Any]:
        """
        Deletes the alias, but doesn't affect the underlying key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.delete_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#delete_alias)
        """

    def delete_key(
        self, *, KeyIdentifier: str, DeleteKeyInDays: int = None
    ) -> DeleteKeyOutputTypeDef:
        """
        Deletes the key material and metadata associated with Amazon Web Services
        Payment Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.delete_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#delete_key)
        """

    def export_key(
        self,
        *,
        KeyMaterial: "ExportKeyMaterialTypeDef",
        ExportKeyIdentifier: str,
        ExportAttributes: "ExportAttributesTypeDef" = None
    ) -> ExportKeyOutputTypeDef:
        """
        Exports a key from Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.export_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#export_key)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#generate_presigned_url)
        """

    def get_alias(self, *, AliasName: str) -> GetAliasOutputTypeDef:
        """
        Gets the Amazon Web Services Payment Cryptography key associated with the alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.get_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#get_alias)
        """

    def get_key(self, *, KeyIdentifier: str) -> GetKeyOutputTypeDef:
        """
        Gets the key material for an Amazon Web Services Payment Cryptography key,
        including the immutable and mutable data specified when the key was created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.get_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#get_key)
        """

    def get_parameters_for_export(
        self, *, KeyMaterialType: KeyMaterialTypeType, SigningKeyAlgorithm: KeyAlgorithmType
    ) -> GetParametersForExportOutputTypeDef:
        """
        Gets the export token and the signing key certificate to initiate a TR-34 key
        export from Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.get_parameters_for_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#get_parameters_for_export)
        """

    def get_parameters_for_import(
        self, *, KeyMaterialType: KeyMaterialTypeType, WrappingKeyAlgorithm: KeyAlgorithmType
    ) -> GetParametersForImportOutputTypeDef:
        """
        Gets the import token and the wrapping key certificate in PEM format (base64
        encoded) to initiate a TR-34 WrappedKeyBlock or a RSA WrappedKeyCryptogram
        import into Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.get_parameters_for_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#get_parameters_for_import)
        """

    def get_public_key_certificate(
        self, *, KeyIdentifier: str
    ) -> GetPublicKeyCertificateOutputTypeDef:
        """
        Gets the public key certificate of the asymmetric key pair that exists within
        Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.get_public_key_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#get_public_key_certificate)
        """

    def import_key(
        self,
        *,
        KeyMaterial: "ImportKeyMaterialTypeDef",
        KeyCheckValueAlgorithm: KeyCheckValueAlgorithmType = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportKeyOutputTypeDef:
        """
        Imports symmetric keys and public key certificates in PEM format (base64
        encoded) into Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.import_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#import_key)
        """

    def list_aliases(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAliasesOutputTypeDef:
        """
        Lists the aliases for all keys in the caller's Amazon Web Services account and
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#list_aliases)
        """

    def list_keys(
        self, *, KeyState: KeyStateType = None, NextToken: str = None, MaxResults: int = None
    ) -> ListKeysOutputTypeDef:
        """
        Lists the keys in the caller's Amazon Web Services account and Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.list_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#list_keys)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags for an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#list_tags_for_resource)
        """

    def restore_key(self, *, KeyIdentifier: str) -> RestoreKeyOutputTypeDef:
        """
        Cancels a scheduled key deletion during the waiting period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.restore_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#restore_key)
        """

    def start_key_usage(self, *, KeyIdentifier: str) -> StartKeyUsageOutputTypeDef:
        """
        Enables an Amazon Web Services Payment Cryptography key, which makes it active
        for cryptographic operations within Amazon Web Services Payment Cryptography
        **Cross-account use:** This operation can't be used across different Amazon Web
        Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.start_key_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#start_key_usage)
        """

    def stop_key_usage(self, *, KeyIdentifier: str) -> StopKeyUsageOutputTypeDef:
        """
        Disables an Amazon Web Services Payment Cryptography key, which makes it
        inactive within Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.stop_key_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#stop_key_usage)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds or edits tags on an Amazon Web Services Payment Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes a tag from an Amazon Web Services Payment Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#untag_resource)
        """

    def update_alias(self, *, AliasName: str, KeyArn: str = None) -> UpdateAliasOutputTypeDef:
        """
        Associates an existing Amazon Web Services Payment Cryptography alias with a
        different key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client.update_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client.html#update_alias)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listaliasespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_keys"]) -> ListKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listkeyspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listtagsforresourcepaginator)
        """
