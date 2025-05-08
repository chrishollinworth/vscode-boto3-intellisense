"""
Type annotations for payment-cryptography service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_payment_cryptography.client import PaymentCryptographyControlPlaneClient

    session = Session()
    client: PaymentCryptographyControlPlaneClient = session.client("payment-cryptography")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListAliasesPaginator, ListKeysPaginator, ListTagsForResourcePaginator
from .type_defs import (
    CreateAliasInputTypeDef,
    CreateAliasOutputTypeDef,
    CreateKeyInputTypeDef,
    CreateKeyOutputTypeDef,
    DeleteAliasInputTypeDef,
    DeleteKeyInputTypeDef,
    DeleteKeyOutputTypeDef,
    ExportKeyInputTypeDef,
    ExportKeyOutputTypeDef,
    GetAliasInputTypeDef,
    GetAliasOutputTypeDef,
    GetKeyInputTypeDef,
    GetKeyOutputTypeDef,
    GetParametersForExportInputTypeDef,
    GetParametersForExportOutputTypeDef,
    GetParametersForImportInputTypeDef,
    GetParametersForImportOutputTypeDef,
    GetPublicKeyCertificateInputTypeDef,
    GetPublicKeyCertificateOutputTypeDef,
    ImportKeyInputTypeDef,
    ImportKeyOutputTypeDef,
    ListAliasesInputTypeDef,
    ListAliasesOutputTypeDef,
    ListKeysInputTypeDef,
    ListKeysOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    RestoreKeyInputTypeDef,
    RestoreKeyOutputTypeDef,
    StartKeyUsageInputTypeDef,
    StartKeyUsageOutputTypeDef,
    StopKeyUsageInputTypeDef,
    StopKeyUsageOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateAliasInputTypeDef,
    UpdateAliasOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("PaymentCryptographyControlPlaneClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PaymentCryptographyControlPlaneClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#generate_presigned_url)
        """

    def create_alias(self, **kwargs: Unpack[CreateAliasInputTypeDef]) -> CreateAliasOutputTypeDef:
        """
        Creates an <i>alias</i>, or a friendly name, for an Amazon Web Services Payment
        Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/create_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#create_alias)
        """

    def create_key(self, **kwargs: Unpack[CreateKeyInputTypeDef]) -> CreateKeyOutputTypeDef:
        """
        Creates an Amazon Web Services Payment Cryptography key, a logical
        representation of a cryptographic key, that is unique in your account and
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/create_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#create_key)
        """

    def delete_alias(self, **kwargs: Unpack[DeleteAliasInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the alias, but doesn't affect the underlying key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/delete_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#delete_alias)
        """

    def delete_key(self, **kwargs: Unpack[DeleteKeyInputTypeDef]) -> DeleteKeyOutputTypeDef:
        """
        Deletes the key material and metadata associated with Amazon Web Services
        Payment Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/delete_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#delete_key)
        """

    def export_key(self, **kwargs: Unpack[ExportKeyInputTypeDef]) -> ExportKeyOutputTypeDef:
        """
        Exports a key from Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/export_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#export_key)
        """

    def get_alias(self, **kwargs: Unpack[GetAliasInputTypeDef]) -> GetAliasOutputTypeDef:
        """
        Gets the Amazon Web Services Payment Cryptography key associated with the alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_alias)
        """

    def get_key(self, **kwargs: Unpack[GetKeyInputTypeDef]) -> GetKeyOutputTypeDef:
        """
        Gets the key material for an Amazon Web Services Payment Cryptography key,
        including the immutable and mutable data specified when the key was created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_key)
        """

    def get_parameters_for_export(
        self, **kwargs: Unpack[GetParametersForExportInputTypeDef]
    ) -> GetParametersForExportOutputTypeDef:
        """
        Gets the export token and the signing key certificate to initiate a TR-34 key
        export from Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_parameters_for_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_parameters_for_export)
        """

    def get_parameters_for_import(
        self, **kwargs: Unpack[GetParametersForImportInputTypeDef]
    ) -> GetParametersForImportOutputTypeDef:
        """
        Gets the import token and the wrapping key certificate in PEM format (base64
        encoded) to initiate a TR-34 WrappedKeyBlock or a RSA WrappedKeyCryptogram
        import into Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_parameters_for_import.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_parameters_for_import)
        """

    def get_public_key_certificate(
        self, **kwargs: Unpack[GetPublicKeyCertificateInputTypeDef]
    ) -> GetPublicKeyCertificateOutputTypeDef:
        """
        Gets the public key certificate of the asymmetric key pair that exists within
        Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_public_key_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_public_key_certificate)
        """

    def import_key(self, **kwargs: Unpack[ImportKeyInputTypeDef]) -> ImportKeyOutputTypeDef:
        """
        Imports symmetric keys and public key certificates in PEM format (base64
        encoded) into Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/import_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#import_key)
        """

    def list_aliases(self, **kwargs: Unpack[ListAliasesInputTypeDef]) -> ListAliasesOutputTypeDef:
        """
        Lists the aliases for all keys in the caller's Amazon Web Services account and
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/list_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#list_aliases)
        """

    def list_keys(self, **kwargs: Unpack[ListKeysInputTypeDef]) -> ListKeysOutputTypeDef:
        """
        Lists the keys in the caller's Amazon Web Services account and Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/list_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#list_keys)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags for an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#list_tags_for_resource)
        """

    def restore_key(self, **kwargs: Unpack[RestoreKeyInputTypeDef]) -> RestoreKeyOutputTypeDef:
        """
        Cancels a scheduled key deletion during the waiting period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/restore_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#restore_key)
        """

    def start_key_usage(
        self, **kwargs: Unpack[StartKeyUsageInputTypeDef]
    ) -> StartKeyUsageOutputTypeDef:
        """
        Enables an Amazon Web Services Payment Cryptography key, which makes it active
        for cryptographic operations within Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/start_key_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#start_key_usage)
        """

    def stop_key_usage(
        self, **kwargs: Unpack[StopKeyUsageInputTypeDef]
    ) -> StopKeyUsageOutputTypeDef:
        """
        Disables an Amazon Web Services Payment Cryptography key, which makes it
        inactive within Amazon Web Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/stop_key_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#stop_key_usage)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds or edits tags on an Amazon Web Services Payment Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a tag from an Amazon Web Services Payment Cryptography key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#untag_resource)
        """

    def update_alias(self, **kwargs: Unpack[UpdateAliasInputTypeDef]) -> UpdateAliasOutputTypeDef:
        """
        Associates an existing Amazon Web Services Payment Cryptography alias with a
        different key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/update_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#update_alias)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_aliases"]
    ) -> ListAliasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_keys"]
    ) -> ListKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/client/#get_paginator)
        """
