"""
Type annotations for kms service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kms.type_defs import AliasListEntryTypeDef

    data: AliasListEntryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AlgorithmSpecType,
    ConnectionErrorCodeTypeType,
    ConnectionStateTypeType,
    CustomerMasterKeySpecType,
    CustomKeyStoreTypeType,
    DataKeyPairSpecType,
    DataKeySpecType,
    EncryptionAlgorithmSpecType,
    ExpirationModelTypeType,
    GrantOperationType,
    KeyManagerTypeType,
    KeySpecType,
    KeyStateType,
    KeyUsageTypeType,
    MacAlgorithmSpecType,
    MessageTypeType,
    MultiRegionKeyTypeType,
    OriginTypeType,
    RotationTypeType,
    SigningAlgorithmSpecType,
    WrappingKeySpecType,
    XksProxyConnectivityTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AliasListEntryTypeDef",
    "BlobTypeDef",
    "CancelKeyDeletionRequestTypeDef",
    "CancelKeyDeletionResponseTypeDef",
    "ConnectCustomKeyStoreRequestTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateCustomKeyStoreRequestTypeDef",
    "CreateCustomKeyStoreResponseTypeDef",
    "CreateGrantRequestTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateKeyRequestTypeDef",
    "CreateKeyResponseTypeDef",
    "CustomKeyStoresListEntryTypeDef",
    "DecryptRequestTypeDef",
    "DecryptResponseTypeDef",
    "DeleteAliasRequestTypeDef",
    "DeleteCustomKeyStoreRequestTypeDef",
    "DeleteImportedKeyMaterialRequestTypeDef",
    "DeriveSharedSecretRequestTypeDef",
    "DeriveSharedSecretResponseTypeDef",
    "DescribeCustomKeyStoresRequestPaginateTypeDef",
    "DescribeCustomKeyStoresRequestTypeDef",
    "DescribeCustomKeyStoresResponseTypeDef",
    "DescribeKeyRequestTypeDef",
    "DescribeKeyResponseTypeDef",
    "DisableKeyRequestTypeDef",
    "DisableKeyRotationRequestTypeDef",
    "DisconnectCustomKeyStoreRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableKeyRequestTypeDef",
    "EnableKeyRotationRequestTypeDef",
    "EncryptRequestTypeDef",
    "EncryptResponseTypeDef",
    "GenerateDataKeyPairRequestTypeDef",
    "GenerateDataKeyPairResponseTypeDef",
    "GenerateDataKeyPairWithoutPlaintextRequestTypeDef",
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "GenerateDataKeyRequestTypeDef",
    "GenerateDataKeyResponseTypeDef",
    "GenerateDataKeyWithoutPlaintextRequestTypeDef",
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    "GenerateMacRequestTypeDef",
    "GenerateMacResponseTypeDef",
    "GenerateRandomRequestTypeDef",
    "GenerateRandomResponseTypeDef",
    "GetKeyPolicyRequestTypeDef",
    "GetKeyPolicyResponseTypeDef",
    "GetKeyRotationStatusRequestTypeDef",
    "GetKeyRotationStatusResponseTypeDef",
    "GetParametersForImportRequestTypeDef",
    "GetParametersForImportResponseTypeDef",
    "GetPublicKeyRequestTypeDef",
    "GetPublicKeyResponseTypeDef",
    "GrantConstraintsOutputTypeDef",
    "GrantConstraintsTypeDef",
    "GrantConstraintsUnionTypeDef",
    "GrantListEntryTypeDef",
    "ImportKeyMaterialRequestTypeDef",
    "KeyListEntryTypeDef",
    "KeyMetadataTypeDef",
    "ListAliasesRequestPaginateTypeDef",
    "ListAliasesRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGrantsRequestPaginateTypeDef",
    "ListGrantsRequestTypeDef",
    "ListGrantsResponseTypeDef",
    "ListKeyPoliciesRequestPaginateTypeDef",
    "ListKeyPoliciesRequestTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "ListKeyRotationsRequestPaginateTypeDef",
    "ListKeyRotationsRequestTypeDef",
    "ListKeyRotationsResponseTypeDef",
    "ListKeysRequestPaginateTypeDef",
    "ListKeysRequestTypeDef",
    "ListKeysResponseTypeDef",
    "ListResourceTagsRequestPaginateTypeDef",
    "ListResourceTagsRequestTypeDef",
    "ListResourceTagsResponseTypeDef",
    "ListRetirableGrantsRequestPaginateTypeDef",
    "ListRetirableGrantsRequestTypeDef",
    "MultiRegionConfigurationTypeDef",
    "MultiRegionKeyTypeDef",
    "PaginatorConfigTypeDef",
    "PutKeyPolicyRequestTypeDef",
    "ReEncryptRequestTypeDef",
    "ReEncryptResponseTypeDef",
    "RecipientInfoTypeDef",
    "ReplicateKeyRequestTypeDef",
    "ReplicateKeyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetireGrantRequestTypeDef",
    "RevokeGrantRequestTypeDef",
    "RotateKeyOnDemandRequestTypeDef",
    "RotateKeyOnDemandResponseTypeDef",
    "RotationsListEntryTypeDef",
    "ScheduleKeyDeletionRequestTypeDef",
    "ScheduleKeyDeletionResponseTypeDef",
    "SignRequestTypeDef",
    "SignResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAliasRequestTypeDef",
    "UpdateCustomKeyStoreRequestTypeDef",
    "UpdateKeyDescriptionRequestTypeDef",
    "UpdatePrimaryRegionRequestTypeDef",
    "VerifyMacRequestTypeDef",
    "VerifyMacResponseTypeDef",
    "VerifyRequestTypeDef",
    "VerifyResponseTypeDef",
    "XksKeyConfigurationTypeTypeDef",
    "XksProxyAuthenticationCredentialTypeTypeDef",
    "XksProxyConfigurationTypeTypeDef",
)

class AliasListEntryTypeDef(TypedDict):
    AliasName: NotRequired[str]
    AliasArn: NotRequired[str]
    TargetKeyId: NotRequired[str]
    CreationDate: NotRequired[datetime]
    LastUpdatedDate: NotRequired[datetime]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelKeyDeletionRequestTypeDef(TypedDict):
    KeyId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ConnectCustomKeyStoreRequestTypeDef(TypedDict):
    CustomKeyStoreId: str

class CreateAliasRequestTypeDef(TypedDict):
    AliasName: str
    TargetKeyId: str

class XksProxyAuthenticationCredentialTypeTypeDef(TypedDict):
    AccessKeyId: str
    RawSecretAccessKey: str

class TagTypeDef(TypedDict):
    TagKey: str
    TagValue: str

class XksProxyConfigurationTypeTypeDef(TypedDict):
    Connectivity: NotRequired[XksProxyConnectivityTypeType]
    AccessKeyId: NotRequired[str]
    UriEndpoint: NotRequired[str]
    UriPath: NotRequired[str]
    VpcEndpointServiceName: NotRequired[str]

class DeleteAliasRequestTypeDef(TypedDict):
    AliasName: str

class DeleteCustomKeyStoreRequestTypeDef(TypedDict):
    CustomKeyStoreId: str

class DeleteImportedKeyMaterialRequestTypeDef(TypedDict):
    KeyId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeCustomKeyStoresRequestTypeDef(TypedDict):
    CustomKeyStoreId: NotRequired[str]
    CustomKeyStoreName: NotRequired[str]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class DescribeKeyRequestTypeDef(TypedDict):
    KeyId: str
    GrantTokens: NotRequired[Sequence[str]]

class DisableKeyRequestTypeDef(TypedDict):
    KeyId: str

class DisableKeyRotationRequestTypeDef(TypedDict):
    KeyId: str

class DisconnectCustomKeyStoreRequestTypeDef(TypedDict):
    CustomKeyStoreId: str

class EnableKeyRequestTypeDef(TypedDict):
    KeyId: str

class EnableKeyRotationRequestTypeDef(TypedDict):
    KeyId: str
    RotationPeriodInDays: NotRequired[int]

class GenerateDataKeyPairWithoutPlaintextRequestTypeDef(TypedDict):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: NotRequired[Mapping[str, str]]
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]

class GenerateDataKeyWithoutPlaintextRequestTypeDef(TypedDict):
    KeyId: str
    EncryptionContext: NotRequired[Mapping[str, str]]
    KeySpec: NotRequired[DataKeySpecType]
    NumberOfBytes: NotRequired[int]
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]

class GetKeyPolicyRequestTypeDef(TypedDict):
    KeyId: str
    PolicyName: NotRequired[str]

class GetKeyRotationStatusRequestTypeDef(TypedDict):
    KeyId: str

class GetParametersForImportRequestTypeDef(TypedDict):
    KeyId: str
    WrappingAlgorithm: AlgorithmSpecType
    WrappingKeySpec: WrappingKeySpecType

class GetPublicKeyRequestTypeDef(TypedDict):
    KeyId: str
    GrantTokens: NotRequired[Sequence[str]]

class GrantConstraintsOutputTypeDef(TypedDict):
    EncryptionContextSubset: NotRequired[Dict[str, str]]
    EncryptionContextEquals: NotRequired[Dict[str, str]]

class GrantConstraintsTypeDef(TypedDict):
    EncryptionContextSubset: NotRequired[Mapping[str, str]]
    EncryptionContextEquals: NotRequired[Mapping[str, str]]

TimestampTypeDef = Union[datetime, str]

class KeyListEntryTypeDef(TypedDict):
    KeyId: NotRequired[str]
    KeyArn: NotRequired[str]

class XksKeyConfigurationTypeTypeDef(TypedDict):
    Id: NotRequired[str]

class ListAliasesRequestTypeDef(TypedDict):
    KeyId: NotRequired[str]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class ListGrantsRequestTypeDef(TypedDict):
    KeyId: str
    Limit: NotRequired[int]
    Marker: NotRequired[str]
    GrantId: NotRequired[str]
    GranteePrincipal: NotRequired[str]

class ListKeyPoliciesRequestTypeDef(TypedDict):
    KeyId: str
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class ListKeyRotationsRequestTypeDef(TypedDict):
    KeyId: str
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class RotationsListEntryTypeDef(TypedDict):
    KeyId: NotRequired[str]
    RotationDate: NotRequired[datetime]
    RotationType: NotRequired[RotationTypeType]

class ListKeysRequestTypeDef(TypedDict):
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class ListResourceTagsRequestTypeDef(TypedDict):
    KeyId: str
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class ListRetirableGrantsRequestTypeDef(TypedDict):
    RetiringPrincipal: str
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class MultiRegionKeyTypeDef(TypedDict):
    Arn: NotRequired[str]
    Region: NotRequired[str]

class PutKeyPolicyRequestTypeDef(TypedDict):
    KeyId: str
    Policy: str
    PolicyName: NotRequired[str]
    BypassPolicyLockoutSafetyCheck: NotRequired[bool]

class RetireGrantRequestTypeDef(TypedDict):
    GrantToken: NotRequired[str]
    KeyId: NotRequired[str]
    GrantId: NotRequired[str]
    DryRun: NotRequired[bool]

class RevokeGrantRequestTypeDef(TypedDict):
    KeyId: str
    GrantId: str
    DryRun: NotRequired[bool]

class RotateKeyOnDemandRequestTypeDef(TypedDict):
    KeyId: str

class ScheduleKeyDeletionRequestTypeDef(TypedDict):
    KeyId: str
    PendingWindowInDays: NotRequired[int]

class UntagResourceRequestTypeDef(TypedDict):
    KeyId: str
    TagKeys: Sequence[str]

class UpdateAliasRequestTypeDef(TypedDict):
    AliasName: str
    TargetKeyId: str

class UpdateKeyDescriptionRequestTypeDef(TypedDict):
    KeyId: str
    Description: str

class UpdatePrimaryRegionRequestTypeDef(TypedDict):
    KeyId: str
    PrimaryRegion: str

class EncryptRequestTypeDef(TypedDict):
    KeyId: str
    Plaintext: BlobTypeDef
    EncryptionContext: NotRequired[Mapping[str, str]]
    GrantTokens: NotRequired[Sequence[str]]
    EncryptionAlgorithm: NotRequired[EncryptionAlgorithmSpecType]
    DryRun: NotRequired[bool]

class GenerateMacRequestTypeDef(TypedDict):
    Message: BlobTypeDef
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]

class ReEncryptRequestTypeDef(TypedDict):
    CiphertextBlob: BlobTypeDef
    DestinationKeyId: str
    SourceEncryptionContext: NotRequired[Mapping[str, str]]
    SourceKeyId: NotRequired[str]
    DestinationEncryptionContext: NotRequired[Mapping[str, str]]
    SourceEncryptionAlgorithm: NotRequired[EncryptionAlgorithmSpecType]
    DestinationEncryptionAlgorithm: NotRequired[EncryptionAlgorithmSpecType]
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]

class RecipientInfoTypeDef(TypedDict):
    KeyEncryptionAlgorithm: NotRequired[Literal["RSAES_OAEP_SHA_256"]]
    AttestationDocument: NotRequired[BlobTypeDef]

class SignRequestTypeDef(TypedDict):
    KeyId: str
    Message: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: NotRequired[MessageTypeType]
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]

class VerifyMacRequestTypeDef(TypedDict):
    Message: BlobTypeDef
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    Mac: BlobTypeDef
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]

class VerifyRequestTypeDef(TypedDict):
    KeyId: str
    Message: BlobTypeDef
    Signature: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: NotRequired[MessageTypeType]
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]

class CancelKeyDeletionResponseTypeDef(TypedDict):
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomKeyStoreResponseTypeDef(TypedDict):
    CustomKeyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantResponseTypeDef(TypedDict):
    GrantToken: str
    GrantId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DecryptResponseTypeDef(TypedDict):
    KeyId: str
    Plaintext: bytes
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class DeriveSharedSecretResponseTypeDef(TypedDict):
    KeyId: str
    SharedSecret: bytes
    CiphertextForRecipient: bytes
    KeyAgreementAlgorithm: Literal["ECDH"]
    KeyOrigin: OriginTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptResponseTypeDef(TypedDict):
    CiphertextBlob: bytes
    KeyId: str
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyPairResponseTypeDef(TypedDict):
    PrivateKeyCiphertextBlob: bytes
    PrivateKeyPlaintext: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyPairWithoutPlaintextResponseTypeDef(TypedDict):
    PrivateKeyCiphertextBlob: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyResponseTypeDef(TypedDict):
    CiphertextBlob: bytes
    Plaintext: bytes
    KeyId: str
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyWithoutPlaintextResponseTypeDef(TypedDict):
    CiphertextBlob: bytes
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMacResponseTypeDef(TypedDict):
    Mac: bytes
    MacAlgorithm: MacAlgorithmSpecType
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateRandomResponseTypeDef(TypedDict):
    Plaintext: bytes
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyPolicyResponseTypeDef(TypedDict):
    Policy: str
    PolicyName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyRotationStatusResponseTypeDef(TypedDict):
    KeyRotationEnabled: bool
    KeyId: str
    RotationPeriodInDays: int
    NextRotationDate: datetime
    OnDemandRotationStartDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForImportResponseTypeDef(TypedDict):
    KeyId: str
    ImportToken: bytes
    PublicKey: bytes
    ParametersValidTo: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyResponseTypeDef(TypedDict):
    KeyId: str
    PublicKey: bytes
    CustomerMasterKeySpec: CustomerMasterKeySpecType
    KeySpec: KeySpecType
    KeyUsage: KeyUsageTypeType
    EncryptionAlgorithms: List[EncryptionAlgorithmSpecType]
    SigningAlgorithms: List[SigningAlgorithmSpecType]
    KeyAgreementAlgorithms: List[Literal["ECDH"]]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(TypedDict):
    Aliases: List[AliasListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReEncryptResponseTypeDef(TypedDict):
    CiphertextBlob: bytes
    SourceKeyId: str
    KeyId: str
    SourceEncryptionAlgorithm: EncryptionAlgorithmSpecType
    DestinationEncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class RotateKeyOnDemandResponseTypeDef(TypedDict):
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduleKeyDeletionResponseTypeDef(TypedDict):
    KeyId: str
    DeletionDate: datetime
    KeyState: KeyStateType
    PendingWindowInDays: int
    ResponseMetadata: ResponseMetadataTypeDef

class SignResponseTypeDef(TypedDict):
    KeyId: str
    Signature: bytes
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyMacResponseTypeDef(TypedDict):
    KeyId: str
    MacValid: bool
    MacAlgorithm: MacAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyResponseTypeDef(TypedDict):
    KeyId: str
    SignatureValid: bool
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomKeyStoreRequestTypeDef(TypedDict):
    CustomKeyStoreName: str
    CloudHsmClusterId: NotRequired[str]
    TrustAnchorCertificate: NotRequired[str]
    KeyStorePassword: NotRequired[str]
    CustomKeyStoreType: NotRequired[CustomKeyStoreTypeType]
    XksProxyUriEndpoint: NotRequired[str]
    XksProxyUriPath: NotRequired[str]
    XksProxyVpcEndpointServiceName: NotRequired[str]
    XksProxyAuthenticationCredential: NotRequired[XksProxyAuthenticationCredentialTypeTypeDef]
    XksProxyConnectivity: NotRequired[XksProxyConnectivityTypeType]

class UpdateCustomKeyStoreRequestTypeDef(TypedDict):
    CustomKeyStoreId: str
    NewCustomKeyStoreName: NotRequired[str]
    KeyStorePassword: NotRequired[str]
    CloudHsmClusterId: NotRequired[str]
    XksProxyUriEndpoint: NotRequired[str]
    XksProxyUriPath: NotRequired[str]
    XksProxyVpcEndpointServiceName: NotRequired[str]
    XksProxyAuthenticationCredential: NotRequired[XksProxyAuthenticationCredentialTypeTypeDef]
    XksProxyConnectivity: NotRequired[XksProxyConnectivityTypeType]

class CreateKeyRequestTypeDef(TypedDict):
    Policy: NotRequired[str]
    Description: NotRequired[str]
    KeyUsage: NotRequired[KeyUsageTypeType]
    CustomerMasterKeySpec: NotRequired[CustomerMasterKeySpecType]
    KeySpec: NotRequired[KeySpecType]
    Origin: NotRequired[OriginTypeType]
    CustomKeyStoreId: NotRequired[str]
    BypassPolicyLockoutSafetyCheck: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    MultiRegion: NotRequired[bool]
    XksKeyId: NotRequired[str]

class ListResourceTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateKeyRequestTypeDef(TypedDict):
    KeyId: str
    ReplicaRegion: str
    Policy: NotRequired[str]
    BypassPolicyLockoutSafetyCheck: NotRequired[bool]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    KeyId: str
    Tags: Sequence[TagTypeDef]

class CustomKeyStoresListEntryTypeDef(TypedDict):
    CustomKeyStoreId: NotRequired[str]
    CustomKeyStoreName: NotRequired[str]
    CloudHsmClusterId: NotRequired[str]
    TrustAnchorCertificate: NotRequired[str]
    ConnectionState: NotRequired[ConnectionStateTypeType]
    ConnectionErrorCode: NotRequired[ConnectionErrorCodeTypeType]
    CreationDate: NotRequired[datetime]
    CustomKeyStoreType: NotRequired[CustomKeyStoreTypeType]
    XksProxyConfiguration: NotRequired[XksProxyConfigurationTypeTypeDef]

class DescribeCustomKeyStoresRequestPaginateTypeDef(TypedDict):
    CustomKeyStoreId: NotRequired[str]
    CustomKeyStoreName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAliasesRequestPaginateTypeDef(TypedDict):
    KeyId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGrantsRequestPaginateTypeDef(TypedDict):
    KeyId: str
    GrantId: NotRequired[str]
    GranteePrincipal: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKeyPoliciesRequestPaginateTypeDef(TypedDict):
    KeyId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKeyRotationsRequestPaginateTypeDef(TypedDict):
    KeyId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKeysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceTagsRequestPaginateTypeDef(TypedDict):
    KeyId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRetirableGrantsRequestPaginateTypeDef(TypedDict):
    RetiringPrincipal: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GrantListEntryTypeDef(TypedDict):
    KeyId: NotRequired[str]
    GrantId: NotRequired[str]
    Name: NotRequired[str]
    CreationDate: NotRequired[datetime]
    GranteePrincipal: NotRequired[str]
    RetiringPrincipal: NotRequired[str]
    IssuingAccount: NotRequired[str]
    Operations: NotRequired[List[GrantOperationType]]
    Constraints: NotRequired[GrantConstraintsOutputTypeDef]

GrantConstraintsUnionTypeDef = Union[GrantConstraintsTypeDef, GrantConstraintsOutputTypeDef]

class ImportKeyMaterialRequestTypeDef(TypedDict):
    KeyId: str
    ImportToken: BlobTypeDef
    EncryptedKeyMaterial: BlobTypeDef
    ValidTo: NotRequired[TimestampTypeDef]
    ExpirationModel: NotRequired[ExpirationModelTypeType]

class ListKeysResponseTypeDef(TypedDict):
    Keys: List[KeyListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyRotationsResponseTypeDef(TypedDict):
    Rotations: List[RotationsListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class MultiRegionConfigurationTypeDef(TypedDict):
    MultiRegionKeyType: NotRequired[MultiRegionKeyTypeType]
    PrimaryKey: NotRequired[MultiRegionKeyTypeDef]
    ReplicaKeys: NotRequired[List[MultiRegionKeyTypeDef]]

class DecryptRequestTypeDef(TypedDict):
    CiphertextBlob: BlobTypeDef
    EncryptionContext: NotRequired[Mapping[str, str]]
    GrantTokens: NotRequired[Sequence[str]]
    KeyId: NotRequired[str]
    EncryptionAlgorithm: NotRequired[EncryptionAlgorithmSpecType]
    Recipient: NotRequired[RecipientInfoTypeDef]
    DryRun: NotRequired[bool]

class DeriveSharedSecretRequestTypeDef(TypedDict):
    KeyId: str
    KeyAgreementAlgorithm: Literal["ECDH"]
    PublicKey: BlobTypeDef
    GrantTokens: NotRequired[Sequence[str]]
    DryRun: NotRequired[bool]
    Recipient: NotRequired[RecipientInfoTypeDef]

class GenerateDataKeyPairRequestTypeDef(TypedDict):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: NotRequired[Mapping[str, str]]
    GrantTokens: NotRequired[Sequence[str]]
    Recipient: NotRequired[RecipientInfoTypeDef]
    DryRun: NotRequired[bool]

class GenerateDataKeyRequestTypeDef(TypedDict):
    KeyId: str
    EncryptionContext: NotRequired[Mapping[str, str]]
    NumberOfBytes: NotRequired[int]
    KeySpec: NotRequired[DataKeySpecType]
    GrantTokens: NotRequired[Sequence[str]]
    Recipient: NotRequired[RecipientInfoTypeDef]
    DryRun: NotRequired[bool]

class GenerateRandomRequestTypeDef(TypedDict):
    NumberOfBytes: NotRequired[int]
    CustomKeyStoreId: NotRequired[str]
    Recipient: NotRequired[RecipientInfoTypeDef]

class DescribeCustomKeyStoresResponseTypeDef(TypedDict):
    CustomKeyStores: List[CustomKeyStoresListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListGrantsResponseTypeDef(TypedDict):
    Grants: List[GrantListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantRequestTypeDef(TypedDict):
    KeyId: str
    GranteePrincipal: str
    Operations: Sequence[GrantOperationType]
    RetiringPrincipal: NotRequired[str]
    Constraints: NotRequired[GrantConstraintsUnionTypeDef]
    GrantTokens: NotRequired[Sequence[str]]
    Name: NotRequired[str]
    DryRun: NotRequired[bool]

class KeyMetadataTypeDef(TypedDict):
    KeyId: str
    AWSAccountId: NotRequired[str]
    Arn: NotRequired[str]
    CreationDate: NotRequired[datetime]
    Enabled: NotRequired[bool]
    Description: NotRequired[str]
    KeyUsage: NotRequired[KeyUsageTypeType]
    KeyState: NotRequired[KeyStateType]
    DeletionDate: NotRequired[datetime]
    ValidTo: NotRequired[datetime]
    Origin: NotRequired[OriginTypeType]
    CustomKeyStoreId: NotRequired[str]
    CloudHsmClusterId: NotRequired[str]
    ExpirationModel: NotRequired[ExpirationModelTypeType]
    KeyManager: NotRequired[KeyManagerTypeType]
    CustomerMasterKeySpec: NotRequired[CustomerMasterKeySpecType]
    KeySpec: NotRequired[KeySpecType]
    EncryptionAlgorithms: NotRequired[List[EncryptionAlgorithmSpecType]]
    SigningAlgorithms: NotRequired[List[SigningAlgorithmSpecType]]
    KeyAgreementAlgorithms: NotRequired[List[Literal["ECDH"]]]
    MultiRegion: NotRequired[bool]
    MultiRegionConfiguration: NotRequired[MultiRegionConfigurationTypeDef]
    PendingDeletionWindowInDays: NotRequired[int]
    MacAlgorithms: NotRequired[List[MacAlgorithmSpecType]]
    XksKeyConfiguration: NotRequired[XksKeyConfigurationTypeTypeDef]

class CreateKeyResponseTypeDef(TypedDict):
    KeyMetadata: KeyMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyResponseTypeDef(TypedDict):
    KeyMetadata: KeyMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateKeyResponseTypeDef(TypedDict):
    ReplicaKeyMetadata: KeyMetadataTypeDef
    ReplicaPolicy: str
    ReplicaTags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
