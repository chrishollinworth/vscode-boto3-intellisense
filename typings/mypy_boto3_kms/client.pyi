"""
Type annotations for kms service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kms.client import KMSClient

    session = Session()
    client: KMSClient = session.client("kms")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeCustomKeyStoresPaginator,
    ListAliasesPaginator,
    ListGrantsPaginator,
    ListKeyPoliciesPaginator,
    ListKeyRotationsPaginator,
    ListKeysPaginator,
    ListResourceTagsPaginator,
    ListRetirableGrantsPaginator,
)
from .type_defs import (
    CancelKeyDeletionRequestTypeDef,
    CancelKeyDeletionResponseTypeDef,
    ConnectCustomKeyStoreRequestTypeDef,
    CreateAliasRequestTypeDef,
    CreateCustomKeyStoreRequestTypeDef,
    CreateCustomKeyStoreResponseTypeDef,
    CreateGrantRequestTypeDef,
    CreateGrantResponseTypeDef,
    CreateKeyRequestTypeDef,
    CreateKeyResponseTypeDef,
    DecryptRequestTypeDef,
    DecryptResponseTypeDef,
    DeleteAliasRequestTypeDef,
    DeleteCustomKeyStoreRequestTypeDef,
    DeleteImportedKeyMaterialRequestTypeDef,
    DeriveSharedSecretRequestTypeDef,
    DeriveSharedSecretResponseTypeDef,
    DescribeCustomKeyStoresRequestTypeDef,
    DescribeCustomKeyStoresResponseTypeDef,
    DescribeKeyRequestTypeDef,
    DescribeKeyResponseTypeDef,
    DisableKeyRequestTypeDef,
    DisableKeyRotationRequestTypeDef,
    DisconnectCustomKeyStoreRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableKeyRequestTypeDef,
    EnableKeyRotationRequestTypeDef,
    EncryptRequestTypeDef,
    EncryptResponseTypeDef,
    GenerateDataKeyPairRequestTypeDef,
    GenerateDataKeyPairResponseTypeDef,
    GenerateDataKeyPairWithoutPlaintextRequestTypeDef,
    GenerateDataKeyPairWithoutPlaintextResponseTypeDef,
    GenerateDataKeyRequestTypeDef,
    GenerateDataKeyResponseTypeDef,
    GenerateDataKeyWithoutPlaintextRequestTypeDef,
    GenerateDataKeyWithoutPlaintextResponseTypeDef,
    GenerateMacRequestTypeDef,
    GenerateMacResponseTypeDef,
    GenerateRandomRequestTypeDef,
    GenerateRandomResponseTypeDef,
    GetKeyPolicyRequestTypeDef,
    GetKeyPolicyResponseTypeDef,
    GetKeyRotationStatusRequestTypeDef,
    GetKeyRotationStatusResponseTypeDef,
    GetParametersForImportRequestTypeDef,
    GetParametersForImportResponseTypeDef,
    GetPublicKeyRequestTypeDef,
    GetPublicKeyResponseTypeDef,
    ImportKeyMaterialRequestTypeDef,
    ListAliasesRequestTypeDef,
    ListAliasesResponseTypeDef,
    ListGrantsRequestTypeDef,
    ListGrantsResponseTypeDef,
    ListKeyPoliciesRequestTypeDef,
    ListKeyPoliciesResponseTypeDef,
    ListKeyRotationsRequestTypeDef,
    ListKeyRotationsResponseTypeDef,
    ListKeysRequestTypeDef,
    ListKeysResponseTypeDef,
    ListResourceTagsRequestTypeDef,
    ListResourceTagsResponseTypeDef,
    ListRetirableGrantsRequestTypeDef,
    PutKeyPolicyRequestTypeDef,
    ReEncryptRequestTypeDef,
    ReEncryptResponseTypeDef,
    ReplicateKeyRequestTypeDef,
    ReplicateKeyResponseTypeDef,
    RetireGrantRequestTypeDef,
    RevokeGrantRequestTypeDef,
    RotateKeyOnDemandRequestTypeDef,
    RotateKeyOnDemandResponseTypeDef,
    ScheduleKeyDeletionRequestTypeDef,
    ScheduleKeyDeletionResponseTypeDef,
    SignRequestTypeDef,
    SignResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAliasRequestTypeDef,
    UpdateCustomKeyStoreRequestTypeDef,
    UpdateKeyDescriptionRequestTypeDef,
    UpdatePrimaryRegionRequestTypeDef,
    VerifyMacRequestTypeDef,
    VerifyMacResponseTypeDef,
    VerifyRequestTypeDef,
    VerifyResponseTypeDef,
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

__all__ = ("KMSClient",)

class Exceptions(BaseClientExceptions):
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CloudHsmClusterInUseException: Type[BotocoreClientError]
    CloudHsmClusterInvalidConfigurationException: Type[BotocoreClientError]
    CloudHsmClusterNotActiveException: Type[BotocoreClientError]
    CloudHsmClusterNotFoundException: Type[BotocoreClientError]
    CloudHsmClusterNotRelatedException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CustomKeyStoreHasCMKsException: Type[BotocoreClientError]
    CustomKeyStoreInvalidStateException: Type[BotocoreClientError]
    CustomKeyStoreNameInUseException: Type[BotocoreClientError]
    CustomKeyStoreNotFoundException: Type[BotocoreClientError]
    DependencyTimeoutException: Type[BotocoreClientError]
    DisabledException: Type[BotocoreClientError]
    DryRunOperationException: Type[BotocoreClientError]
    ExpiredImportTokenException: Type[BotocoreClientError]
    IncorrectKeyException: Type[BotocoreClientError]
    IncorrectKeyMaterialException: Type[BotocoreClientError]
    IncorrectTrustAnchorException: Type[BotocoreClientError]
    InvalidAliasNameException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidCiphertextException: Type[BotocoreClientError]
    InvalidGrantIdException: Type[BotocoreClientError]
    InvalidGrantTokenException: Type[BotocoreClientError]
    InvalidImportTokenException: Type[BotocoreClientError]
    InvalidKeyUsageException: Type[BotocoreClientError]
    InvalidMarkerException: Type[BotocoreClientError]
    KMSInternalException: Type[BotocoreClientError]
    KMSInvalidMacException: Type[BotocoreClientError]
    KMSInvalidSignatureException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KeyUnavailableException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TagException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    XksKeyAlreadyInUseException: Type[BotocoreClientError]
    XksKeyInvalidConfigurationException: Type[BotocoreClientError]
    XksKeyNotFoundException: Type[BotocoreClientError]
    XksProxyIncorrectAuthenticationCredentialException: Type[BotocoreClientError]
    XksProxyInvalidConfigurationException: Type[BotocoreClientError]
    XksProxyInvalidResponseException: Type[BotocoreClientError]
    XksProxyUriEndpointInUseException: Type[BotocoreClientError]
    XksProxyUriInUseException: Type[BotocoreClientError]
    XksProxyUriUnreachableException: Type[BotocoreClientError]
    XksProxyVpcEndpointServiceInUseException: Type[BotocoreClientError]
    XksProxyVpcEndpointServiceInvalidConfigurationException: Type[BotocoreClientError]
    XksProxyVpcEndpointServiceNotFoundException: Type[BotocoreClientError]

class KMSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KMSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#generate_presigned_url)
        """

    def cancel_key_deletion(
        self, **kwargs: Unpack[CancelKeyDeletionRequestTypeDef]
    ) -> CancelKeyDeletionResponseTypeDef:
        """
        Cancels the deletion of a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/cancel_key_deletion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#cancel_key_deletion)
        """

    def connect_custom_key_store(
        self, **kwargs: Unpack[ConnectCustomKeyStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Connects or reconnects a <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html">custom
        key store</a> to its backing key store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/connect_custom_key_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#connect_custom_key_store)
        """

    def create_alias(
        self, **kwargs: Unpack[CreateAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a friendly name for a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/create_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#create_alias)
        """

    def create_custom_key_store(
        self, **kwargs: Unpack[CreateCustomKeyStoreRequestTypeDef]
    ) -> CreateCustomKeyStoreResponseTypeDef:
        """
        Creates a <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html">custom
        key store</a> backed by a key store that you own and manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/create_custom_key_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#create_custom_key_store)
        """

    def create_grant(
        self, **kwargs: Unpack[CreateGrantRequestTypeDef]
    ) -> CreateGrantResponseTypeDef:
        """
        Adds a grant to a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/create_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#create_grant)
        """

    def create_key(self, **kwargs: Unpack[CreateKeyRequestTypeDef]) -> CreateKeyResponseTypeDef:
        """
        Creates a unique customer managed <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms-keys">KMS
        key</a> in your Amazon Web Services account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/create_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#create_key)
        """

    def decrypt(self, **kwargs: Unpack[DecryptRequestTypeDef]) -> DecryptResponseTypeDef:
        """
        Decrypts ciphertext that was encrypted by a KMS key using any of the following
        operations:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/decrypt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#decrypt)
        """

    def delete_alias(
        self, **kwargs: Unpack[DeleteAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/delete_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#delete_alias)
        """

    def delete_custom_key_store(
        self, **kwargs: Unpack[DeleteCustomKeyStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html">custom
        key store</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/delete_custom_key_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#delete_custom_key_store)
        """

    def delete_imported_key_material(
        self, **kwargs: Unpack[DeleteImportedKeyMaterialRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes key material that was previously imported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/delete_imported_key_material.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#delete_imported_key_material)
        """

    def derive_shared_secret(
        self, **kwargs: Unpack[DeriveSharedSecretRequestTypeDef]
    ) -> DeriveSharedSecretResponseTypeDef:
        """
        Derives a shared secret using a key agreement algorithm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/derive_shared_secret.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#derive_shared_secret)
        """

    def describe_custom_key_stores(
        self, **kwargs: Unpack[DescribeCustomKeyStoresRequestTypeDef]
    ) -> DescribeCustomKeyStoresResponseTypeDef:
        """
        Gets information about <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html">custom
        key stores</a> in the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/describe_custom_key_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#describe_custom_key_stores)
        """

    def describe_key(
        self, **kwargs: Unpack[DescribeKeyRequestTypeDef]
    ) -> DescribeKeyResponseTypeDef:
        """
        Provides detailed information about a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/describe_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#describe_key)
        """

    def disable_key(
        self, **kwargs: Unpack[DisableKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the state of a KMS key to disabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/disable_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#disable_key)
        """

    def disable_key_rotation(
        self, **kwargs: Unpack[DisableKeyRotationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html">automatic
        rotation of the key material</a> of the specified symmetric encryption KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/disable_key_rotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#disable_key_rotation)
        """

    def disconnect_custom_key_store(
        self, **kwargs: Unpack[DisconnectCustomKeyStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disconnects the <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html">custom
        key store</a> from its backing key store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/disconnect_custom_key_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#disconnect_custom_key_store)
        """

    def enable_key(self, **kwargs: Unpack[EnableKeyRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Sets the key state of a KMS key to enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/enable_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#enable_key)
        """

    def enable_key_rotation(
        self, **kwargs: Unpack[EnableKeyRotationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotating-keys-enable-disable">automatic
        rotation of the key material</a> of the specified symmetric encryption KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/enable_key_rotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#enable_key_rotation)
        """

    def encrypt(self, **kwargs: Unpack[EncryptRequestTypeDef]) -> EncryptResponseTypeDef:
        """
        Encrypts plaintext of up to 4,096 bytes using a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/encrypt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#encrypt)
        """

    def generate_data_key(
        self, **kwargs: Unpack[GenerateDataKeyRequestTypeDef]
    ) -> GenerateDataKeyResponseTypeDef:
        """
        Returns a unique symmetric data key for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_data_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#generate_data_key)
        """

    def generate_data_key_pair(
        self, **kwargs: Unpack[GenerateDataKeyPairRequestTypeDef]
    ) -> GenerateDataKeyPairResponseTypeDef:
        """
        Returns a unique asymmetric data key pair for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_data_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#generate_data_key_pair)
        """

    def generate_data_key_pair_without_plaintext(
        self, **kwargs: Unpack[GenerateDataKeyPairWithoutPlaintextRequestTypeDef]
    ) -> GenerateDataKeyPairWithoutPlaintextResponseTypeDef:
        """
        Returns a unique asymmetric data key pair for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_data_key_pair_without_plaintext.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#generate_data_key_pair_without_plaintext)
        """

    def generate_data_key_without_plaintext(
        self, **kwargs: Unpack[GenerateDataKeyWithoutPlaintextRequestTypeDef]
    ) -> GenerateDataKeyWithoutPlaintextResponseTypeDef:
        """
        Returns a unique symmetric data key for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_data_key_without_plaintext.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#generate_data_key_without_plaintext)
        """

    def generate_mac(
        self, **kwargs: Unpack[GenerateMacRequestTypeDef]
    ) -> GenerateMacResponseTypeDef:
        """
        Generates a hash-based message authentication code (HMAC) for a message using
        an HMAC KMS key and a MAC algorithm that the key supports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_mac.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#generate_mac)
        """

    def generate_random(
        self, **kwargs: Unpack[GenerateRandomRequestTypeDef]
    ) -> GenerateRandomResponseTypeDef:
        """
        Returns a random byte string that is cryptographically secure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_random.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#generate_random)
        """

    def get_key_policy(
        self, **kwargs: Unpack[GetKeyPolicyRequestTypeDef]
    ) -> GetKeyPolicyResponseTypeDef:
        """
        Gets a key policy attached to the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_key_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_key_policy)
        """

    def get_key_rotation_status(
        self, **kwargs: Unpack[GetKeyRotationStatusRequestTypeDef]
    ) -> GetKeyRotationStatusResponseTypeDef:
        """
        Provides detailed information about the rotation status for a KMS key,
        including whether <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html">automatic
        rotation of the key material</a> is enabled for the specified KMS key, the <a
        href="https://docs.aws.amazon.com/kms/l...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_key_rotation_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_key_rotation_status)
        """

    def get_parameters_for_import(
        self, **kwargs: Unpack[GetParametersForImportRequestTypeDef]
    ) -> GetParametersForImportResponseTypeDef:
        """
        Returns the public key and an import token you need to import or reimport key
        material for a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_parameters_for_import.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_parameters_for_import)
        """

    def get_public_key(
        self, **kwargs: Unpack[GetPublicKeyRequestTypeDef]
    ) -> GetPublicKeyResponseTypeDef:
        """
        Returns the public key of an asymmetric KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_public_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_public_key)
        """

    def import_key_material(
        self, **kwargs: Unpack[ImportKeyMaterialRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Imports or reimports key material into an existing KMS key that was created
        without key material.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/import_key_material.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#import_key_material)
        """

    def list_aliases(
        self, **kwargs: Unpack[ListAliasesRequestTypeDef]
    ) -> ListAliasesResponseTypeDef:
        """
        Gets a list of aliases in the caller's Amazon Web Services account and region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/list_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#list_aliases)
        """

    def list_grants(self, **kwargs: Unpack[ListGrantsRequestTypeDef]) -> ListGrantsResponseTypeDef:
        """
        Gets a list of all grants for the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/list_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#list_grants)
        """

    def list_key_policies(
        self, **kwargs: Unpack[ListKeyPoliciesRequestTypeDef]
    ) -> ListKeyPoliciesResponseTypeDef:
        """
        Gets the names of the key policies that are attached to a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/list_key_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#list_key_policies)
        """

    def list_key_rotations(
        self, **kwargs: Unpack[ListKeyRotationsRequestTypeDef]
    ) -> ListKeyRotationsResponseTypeDef:
        """
        Returns information about all completed key material rotations for the
        specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/list_key_rotations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#list_key_rotations)
        """

    def list_keys(self, **kwargs: Unpack[ListKeysRequestTypeDef]) -> ListKeysResponseTypeDef:
        """
        Gets a list of all KMS keys in the caller's Amazon Web Services account and
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/list_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#list_keys)
        """

    def list_resource_tags(
        self, **kwargs: Unpack[ListResourceTagsRequestTypeDef]
    ) -> ListResourceTagsResponseTypeDef:
        """
        Returns all tags on the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/list_resource_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#list_resource_tags)
        """

    def list_retirable_grants(
        self, **kwargs: Unpack[ListRetirableGrantsRequestTypeDef]
    ) -> ListGrantsResponseTypeDef:
        """
        Returns information about all grants in the Amazon Web Services account and
        Region that have the specified retiring principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/list_retirable_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#list_retirable_grants)
        """

    def put_key_policy(
        self, **kwargs: Unpack[PutKeyPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches a key policy to the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/put_key_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#put_key_policy)
        """

    def re_encrypt(self, **kwargs: Unpack[ReEncryptRequestTypeDef]) -> ReEncryptResponseTypeDef:
        """
        Decrypts ciphertext and then reencrypts it entirely within KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/re_encrypt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#re_encrypt)
        """

    def replicate_key(
        self, **kwargs: Unpack[ReplicateKeyRequestTypeDef]
    ) -> ReplicateKeyResponseTypeDef:
        """
        Replicates a multi-Region key into the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/replicate_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#replicate_key)
        """

    def retire_grant(
        self, **kwargs: Unpack[RetireGrantRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/retire_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#retire_grant)
        """

    def revoke_grant(
        self, **kwargs: Unpack[RevokeGrantRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/revoke_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#revoke_grant)
        """

    def rotate_key_on_demand(
        self, **kwargs: Unpack[RotateKeyOnDemandRequestTypeDef]
    ) -> RotateKeyOnDemandResponseTypeDef:
        """
        Immediately initiates rotation of the key material of the specified symmetric
        encryption KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/rotate_key_on_demand.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#rotate_key_on_demand)
        """

    def schedule_key_deletion(
        self, **kwargs: Unpack[ScheduleKeyDeletionRequestTypeDef]
    ) -> ScheduleKeyDeletionResponseTypeDef:
        """
        Schedules the deletion of a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/schedule_key_deletion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#schedule_key_deletion)
        """

    def sign(self, **kwargs: Unpack[SignRequestTypeDef]) -> SignResponseTypeDef:
        """
        Creates a <a href="https://en.wikipedia.org/wiki/Digital_signature">digital
        signature</a> for a message or message digest by using the private key in an
        asymmetric signing KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/sign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#sign)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or edits tags on a <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">customer
        managed key</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes tags from a <a
        href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">customer
        managed key</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#untag_resource)
        """

    def update_alias(
        self, **kwargs: Unpack[UpdateAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an existing KMS alias with a different KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/update_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#update_alias)
        """

    def update_custom_key_store(
        self, **kwargs: Unpack[UpdateCustomKeyStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Changes the properties of a custom key store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/update_custom_key_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#update_custom_key_store)
        """

    def update_key_description(
        self, **kwargs: Unpack[UpdateKeyDescriptionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the description of a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/update_key_description.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#update_key_description)
        """

    def update_primary_region(
        self, **kwargs: Unpack[UpdatePrimaryRegionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the primary key of a multi-Region key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/update_primary_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#update_primary_region)
        """

    def verify(self, **kwargs: Unpack[VerifyRequestTypeDef]) -> VerifyResponseTypeDef:
        """
        Verifies a digital signature that was generated by the <a>Sign</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/verify.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#verify)
        """

    def verify_mac(self, **kwargs: Unpack[VerifyMacRequestTypeDef]) -> VerifyMacResponseTypeDef:
        """
        Verifies the hash-based message authentication code (HMAC) for a specified
        message, HMAC KMS key, and MAC algorithm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/verify_mac.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#verify_mac)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_custom_key_stores"]
    ) -> DescribeCustomKeyStoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_aliases"]
    ) -> ListAliasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_grants"]
    ) -> ListGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_key_policies"]
    ) -> ListKeyPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_key_rotations"]
    ) -> ListKeyRotationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_keys"]
    ) -> ListKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_tags"]
    ) -> ListResourceTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_retirable_grants"]
    ) -> ListRetirableGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/client/#get_paginator)
        """
