"""
Type annotations for payment-cryptography service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_payment_cryptography.type_defs import AddKeyReplicationRegionsInputTypeDef

    data: AddKeyReplicationRegionsInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    As2805KeyVariantType,
    DeriveKeyUsageType,
    KeyAlgorithmType,
    KeyCheckValueAlgorithmType,
    KeyClassType,
    KeyDerivationFunctionType,
    KeyDerivationHashAlgorithmType,
    KeyExportabilityType,
    KeyMaterialTypeType,
    KeyOriginType,
    KeyReplicationStateType,
    KeyStateType,
    KeyUsageType,
    MultiRegionKeyTypeType,
    SigningAlgorithmTypeType,
    SymmetricKeyAlgorithmType,
    WrappedKeyMaterialFormatType,
    WrappingKeySpecType,
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
    "AddKeyReplicationRegionsInputTypeDef",
    "AddKeyReplicationRegionsOutputTypeDef",
    "AliasTypeDef",
    "CertificateSubjectTypeTypeDef",
    "CreateAliasInputTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateKeyInputTypeDef",
    "CreateKeyOutputTypeDef",
    "DeleteAliasInputTypeDef",
    "DeleteKeyInputTypeDef",
    "DeleteKeyOutputTypeDef",
    "DiffieHellmanDerivationDataTypeDef",
    "DisableDefaultKeyReplicationRegionsInputTypeDef",
    "DisableDefaultKeyReplicationRegionsOutputTypeDef",
    "EnableDefaultKeyReplicationRegionsInputTypeDef",
    "EnableDefaultKeyReplicationRegionsOutputTypeDef",
    "ExportAs2805KeyCryptogramTypeDef",
    "ExportAttributesTypeDef",
    "ExportDiffieHellmanTr31KeyBlockTypeDef",
    "ExportDukptInitialKeyTypeDef",
    "ExportKeyCryptogramTypeDef",
    "ExportKeyInputTypeDef",
    "ExportKeyMaterialTypeDef",
    "ExportKeyOutputTypeDef",
    "ExportTr31KeyBlockTypeDef",
    "ExportTr34KeyBlockTypeDef",
    "GetAliasInputTypeDef",
    "GetAliasOutputTypeDef",
    "GetCertificateSigningRequestInputTypeDef",
    "GetCertificateSigningRequestOutputTypeDef",
    "GetDefaultKeyReplicationRegionsOutputTypeDef",
    "GetKeyInputTypeDef",
    "GetKeyOutputTypeDef",
    "GetParametersForExportInputTypeDef",
    "GetParametersForExportOutputTypeDef",
    "GetParametersForImportInputTypeDef",
    "GetParametersForImportOutputTypeDef",
    "GetPublicKeyCertificateInputTypeDef",
    "GetPublicKeyCertificateOutputTypeDef",
    "ImportAs2805KeyCryptogramTypeDef",
    "ImportDiffieHellmanTr31KeyBlockTypeDef",
    "ImportKeyCryptogramTypeDef",
    "ImportKeyInputTypeDef",
    "ImportKeyMaterialTypeDef",
    "ImportKeyOutputTypeDef",
    "ImportTr31KeyBlockTypeDef",
    "ImportTr34KeyBlockTypeDef",
    "KeyAttributesTypeDef",
    "KeyBlockHeadersTypeDef",
    "KeyModesOfUseTypeDef",
    "KeySummaryTypeDef",
    "KeyTypeDef",
    "ListAliasesInputPaginateTypeDef",
    "ListAliasesInputTypeDef",
    "ListAliasesOutputTypeDef",
    "ListKeysInputPaginateTypeDef",
    "ListKeysInputTypeDef",
    "ListKeysOutputTypeDef",
    "ListTagsForResourceInputPaginateTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveKeyReplicationRegionsInputTypeDef",
    "RemoveKeyReplicationRegionsOutputTypeDef",
    "ReplicationStatusTypeTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreKeyInputTypeDef",
    "RestoreKeyOutputTypeDef",
    "RootCertificatePublicKeyTypeDef",
    "StartKeyUsageInputTypeDef",
    "StartKeyUsageOutputTypeDef",
    "StopKeyUsageInputTypeDef",
    "StopKeyUsageOutputTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TrustedCertificatePublicKeyTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateAliasInputTypeDef",
    "UpdateAliasOutputTypeDef",
    "WrappedKeyTypeDef",
)

class AddKeyReplicationRegionsInputTypeDef(TypedDict):
    KeyIdentifier: str
    ReplicationRegions: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AliasTypeDef(TypedDict):
    AliasName: str
    KeyArn: NotRequired[str]

class CertificateSubjectTypeTypeDef(TypedDict):
    CommonName: str
    OrganizationUnit: NotRequired[str]
    Organization: NotRequired[str]
    City: NotRequired[str]
    Country: NotRequired[str]
    StateOrProvince: NotRequired[str]
    EmailAddress: NotRequired[str]

class CreateAliasInputTypeDef(TypedDict):
    AliasName: str
    KeyArn: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteAliasInputTypeDef(TypedDict):
    AliasName: str

class DeleteKeyInputTypeDef(TypedDict):
    KeyIdentifier: str
    DeleteKeyInDays: NotRequired[int]

class DiffieHellmanDerivationDataTypeDef(TypedDict):
    SharedInformation: NotRequired[str]

class DisableDefaultKeyReplicationRegionsInputTypeDef(TypedDict):
    ReplicationRegions: Sequence[str]

class EnableDefaultKeyReplicationRegionsInputTypeDef(TypedDict):
    ReplicationRegions: Sequence[str]

class ExportAs2805KeyCryptogramTypeDef(TypedDict):
    WrappingKeyIdentifier: str
    As2805KeyVariant: As2805KeyVariantType

class ExportDukptInitialKeyTypeDef(TypedDict):
    KeySerialNumber: str

class ExportKeyCryptogramTypeDef(TypedDict):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    WrappingSpec: NotRequired[WrappingKeySpecType]

class WrappedKeyTypeDef(TypedDict):
    WrappingKeyArn: str
    WrappedKeyMaterialFormat: WrappedKeyMaterialFormatType
    KeyMaterial: str
    KeyCheckValue: NotRequired[str]
    KeyCheckValueAlgorithm: NotRequired[KeyCheckValueAlgorithmType]

class GetAliasInputTypeDef(TypedDict):
    AliasName: str

class GetKeyInputTypeDef(TypedDict):
    KeyIdentifier: str

class GetParametersForExportInputTypeDef(TypedDict):
    KeyMaterialType: KeyMaterialTypeType
    SigningKeyAlgorithm: KeyAlgorithmType

class GetParametersForImportInputTypeDef(TypedDict):
    KeyMaterialType: KeyMaterialTypeType
    WrappingKeyAlgorithm: KeyAlgorithmType

class GetPublicKeyCertificateInputTypeDef(TypedDict):
    KeyIdentifier: str

class KeyModesOfUseTypeDef(TypedDict):
    Encrypt: NotRequired[bool]
    Decrypt: NotRequired[bool]
    Wrap: NotRequired[bool]
    Unwrap: NotRequired[bool]
    Generate: NotRequired[bool]
    Sign: NotRequired[bool]
    Verify: NotRequired[bool]
    DeriveKey: NotRequired[bool]
    NoRestrictions: NotRequired[bool]

class ImportTr31KeyBlockTypeDef(TypedDict):
    WrappingKeyIdentifier: str
    WrappedKeyBlock: str

class ImportTr34KeyBlockTypeDef(TypedDict):
    CertificateAuthorityPublicKeyIdentifier: str
    SigningKeyCertificate: str
    WrappedKeyBlock: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    ImportToken: NotRequired[str]
    WrappingKeyIdentifier: NotRequired[str]
    WrappingKeyCertificate: NotRequired[str]
    RandomNonce: NotRequired[str]

class ReplicationStatusTypeTypeDef(TypedDict):
    Status: KeyReplicationStateType
    StatusMessage: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAliasesInputTypeDef(TypedDict):
    KeyArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListKeysInputTypeDef(TypedDict):
    KeyState: NotRequired[KeyStateType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RemoveKeyReplicationRegionsInputTypeDef(TypedDict):
    KeyIdentifier: str
    ReplicationRegions: Sequence[str]

class RestoreKeyInputTypeDef(TypedDict):
    KeyIdentifier: str

class StartKeyUsageInputTypeDef(TypedDict):
    KeyIdentifier: str

class StopKeyUsageInputTypeDef(TypedDict):
    KeyIdentifier: str

class UntagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAliasInputTypeDef(TypedDict):
    AliasName: str
    KeyArn: NotRequired[str]

class DisableDefaultKeyReplicationRegionsOutputTypeDef(TypedDict):
    EnabledReplicationRegions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDefaultKeyReplicationRegionsOutputTypeDef(TypedDict):
    EnabledReplicationRegions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateSigningRequestOutputTypeDef(TypedDict):
    CertificateSigningRequest: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultKeyReplicationRegionsOutputTypeDef(TypedDict):
    EnabledReplicationRegions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForExportOutputTypeDef(TypedDict):
    SigningKeyCertificate: str
    SigningKeyCertificateChain: str
    SigningKeyAlgorithm: KeyAlgorithmType
    ExportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForImportOutputTypeDef(TypedDict):
    WrappingKeyCertificate: str
    WrappingKeyCertificateChain: str
    WrappingKeyAlgorithm: KeyAlgorithmType
    ImportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyCertificateOutputTypeDef(TypedDict):
    KeyCertificate: str
    KeyCertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAliasOutputTypeDef(TypedDict):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAliasOutputTypeDef(TypedDict):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesOutputTypeDef(TypedDict):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateAliasOutputTypeDef(TypedDict):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateSigningRequestInputTypeDef(TypedDict):
    KeyIdentifier: str
    SigningAlgorithm: SigningAlgorithmTypeType
    CertificateSubject: CertificateSubjectTypeTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ImportDiffieHellmanTr31KeyBlockTypeDef(TypedDict):
    PrivateKeyIdentifier: str
    CertificateAuthorityPublicKeyIdentifier: str
    PublicKeyCertificate: str
    DeriveKeyAlgorithm: SymmetricKeyAlgorithmType
    KeyDerivationFunction: KeyDerivationFunctionType
    KeyDerivationHashAlgorithm: KeyDerivationHashAlgorithmType
    DerivationData: DiffieHellmanDerivationDataTypeDef
    WrappedKeyBlock: str

class ExportAttributesTypeDef(TypedDict):
    ExportDukptInitialKey: NotRequired[ExportDukptInitialKeyTypeDef]
    KeyCheckValueAlgorithm: NotRequired[KeyCheckValueAlgorithmType]

class ExportKeyOutputTypeDef(TypedDict):
    WrappedKey: WrappedKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportAs2805KeyCryptogramTypeDef(TypedDict):
    As2805KeyVariant: As2805KeyVariantType
    KeyModesOfUse: KeyModesOfUseTypeDef
    KeyAlgorithm: KeyAlgorithmType
    Exportable: bool
    WrappingKeyIdentifier: str
    WrappedKeyCryptogram: str

class KeyAttributesTypeDef(TypedDict):
    KeyUsage: KeyUsageType
    KeyClass: KeyClassType
    KeyAlgorithm: KeyAlgorithmType
    KeyModesOfUse: KeyModesOfUseTypeDef

class KeyBlockHeadersTypeDef(TypedDict):
    KeyModesOfUse: NotRequired[KeyModesOfUseTypeDef]
    KeyExportability: NotRequired[KeyExportabilityType]
    KeyVersion: NotRequired[str]
    OptionalBlocks: NotRequired[Mapping[str, str]]

class ListAliasesInputPaginateTypeDef(TypedDict):
    KeyArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKeysInputPaginateTypeDef(TypedDict):
    KeyState: NotRequired[KeyStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceInputPaginateTypeDef(TypedDict):
    ResourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class CreateKeyInputTypeDef(TypedDict):
    KeyAttributes: KeyAttributesTypeDef
    Exportable: bool
    KeyCheckValueAlgorithm: NotRequired[KeyCheckValueAlgorithmType]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DeriveKeyUsage: NotRequired[DeriveKeyUsageType]
    ReplicationRegions: NotRequired[Sequence[str]]

class ImportKeyCryptogramTypeDef(TypedDict):
    KeyAttributes: KeyAttributesTypeDef
    Exportable: bool
    WrappedKeyCryptogram: str
    ImportToken: str
    WrappingSpec: NotRequired[WrappingKeySpecType]

class KeySummaryTypeDef(TypedDict):
    KeyArn: str
    KeyState: KeyStateType
    KeyAttributes: KeyAttributesTypeDef
    KeyCheckValue: str
    Exportable: bool
    Enabled: bool
    MultiRegionKeyType: NotRequired[MultiRegionKeyTypeType]
    PrimaryRegion: NotRequired[str]

class KeyTypeDef(TypedDict):
    KeyArn: str
    KeyAttributes: KeyAttributesTypeDef
    KeyCheckValue: str
    KeyCheckValueAlgorithm: KeyCheckValueAlgorithmType
    Enabled: bool
    Exportable: bool
    KeyState: KeyStateType
    KeyOrigin: KeyOriginType
    CreateTimestamp: datetime
    UsageStartTimestamp: NotRequired[datetime]
    UsageStopTimestamp: NotRequired[datetime]
    DeletePendingTimestamp: NotRequired[datetime]
    DeleteTimestamp: NotRequired[datetime]
    DeriveKeyUsage: NotRequired[DeriveKeyUsageType]
    MultiRegionKeyType: NotRequired[MultiRegionKeyTypeType]
    PrimaryRegion: NotRequired[str]
    ReplicationStatus: NotRequired[Dict[str, ReplicationStatusTypeTypeDef]]
    UsingDefaultReplicationRegions: NotRequired[bool]

class RootCertificatePublicKeyTypeDef(TypedDict):
    KeyAttributes: KeyAttributesTypeDef
    PublicKeyCertificate: str

class TrustedCertificatePublicKeyTypeDef(TypedDict):
    KeyAttributes: KeyAttributesTypeDef
    PublicKeyCertificate: str
    CertificateAuthorityPublicKeyIdentifier: str

class ExportDiffieHellmanTr31KeyBlockTypeDef(TypedDict):
    PrivateKeyIdentifier: str
    CertificateAuthorityPublicKeyIdentifier: str
    PublicKeyCertificate: str
    DeriveKeyAlgorithm: SymmetricKeyAlgorithmType
    KeyDerivationFunction: KeyDerivationFunctionType
    KeyDerivationHashAlgorithm: KeyDerivationHashAlgorithmType
    DerivationData: DiffieHellmanDerivationDataTypeDef
    KeyBlockHeaders: NotRequired[KeyBlockHeadersTypeDef]

class ExportTr31KeyBlockTypeDef(TypedDict):
    WrappingKeyIdentifier: str
    KeyBlockHeaders: NotRequired[KeyBlockHeadersTypeDef]

class ExportTr34KeyBlockTypeDef(TypedDict):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    ExportToken: NotRequired[str]
    SigningKeyIdentifier: NotRequired[str]
    SigningKeyCertificate: NotRequired[str]
    RandomNonce: NotRequired[str]
    KeyBlockHeaders: NotRequired[KeyBlockHeadersTypeDef]

class ListKeysOutputTypeDef(TypedDict):
    Keys: List[KeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AddKeyReplicationRegionsOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKeyOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeyOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportKeyOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveKeyReplicationRegionsOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreKeyOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartKeyUsageOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopKeyUsageOutputTypeDef(TypedDict):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportKeyMaterialTypeDef(TypedDict):
    RootCertificatePublicKey: NotRequired[RootCertificatePublicKeyTypeDef]
    TrustedCertificatePublicKey: NotRequired[TrustedCertificatePublicKeyTypeDef]
    Tr31KeyBlock: NotRequired[ImportTr31KeyBlockTypeDef]
    Tr34KeyBlock: NotRequired[ImportTr34KeyBlockTypeDef]
    KeyCryptogram: NotRequired[ImportKeyCryptogramTypeDef]
    DiffieHellmanTr31KeyBlock: NotRequired[ImportDiffieHellmanTr31KeyBlockTypeDef]
    As2805KeyCryptogram: NotRequired[ImportAs2805KeyCryptogramTypeDef]

class ExportKeyMaterialTypeDef(TypedDict):
    Tr31KeyBlock: NotRequired[ExportTr31KeyBlockTypeDef]
    Tr34KeyBlock: NotRequired[ExportTr34KeyBlockTypeDef]
    KeyCryptogram: NotRequired[ExportKeyCryptogramTypeDef]
    DiffieHellmanTr31KeyBlock: NotRequired[ExportDiffieHellmanTr31KeyBlockTypeDef]
    As2805KeyCryptogram: NotRequired[ExportAs2805KeyCryptogramTypeDef]

class ImportKeyInputTypeDef(TypedDict):
    KeyMaterial: ImportKeyMaterialTypeDef
    KeyCheckValueAlgorithm: NotRequired[KeyCheckValueAlgorithmType]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ReplicationRegions: NotRequired[Sequence[str]]

class ExportKeyInputTypeDef(TypedDict):
    KeyMaterial: ExportKeyMaterialTypeDef
    ExportKeyIdentifier: str
    ExportAttributes: NotRequired[ExportAttributesTypeDef]
