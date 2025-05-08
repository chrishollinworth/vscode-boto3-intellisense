"""
Type annotations for payment-cryptography service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_payment_cryptography.type_defs import AliasTypeDef

    data: AliasTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    DeriveKeyUsageType,
    KeyAlgorithmType,
    KeyCheckValueAlgorithmType,
    KeyClassType,
    KeyDerivationFunctionType,
    KeyDerivationHashAlgorithmType,
    KeyExportabilityType,
    KeyMaterialTypeType,
    KeyOriginType,
    KeyStateType,
    KeyUsageType,
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
    "AliasTypeDef",
    "CreateAliasInputTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateKeyInputTypeDef",
    "CreateKeyOutputTypeDef",
    "DeleteAliasInputTypeDef",
    "DeleteKeyInputTypeDef",
    "DeleteKeyOutputTypeDef",
    "DiffieHellmanDerivationDataTypeDef",
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
    "GetKeyInputTypeDef",
    "GetKeyOutputTypeDef",
    "GetParametersForExportInputTypeDef",
    "GetParametersForExportOutputTypeDef",
    "GetParametersForImportInputTypeDef",
    "GetParametersForImportOutputTypeDef",
    "GetPublicKeyCertificateInputTypeDef",
    "GetPublicKeyCertificateOutputTypeDef",
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

class AliasTypeDef(TypedDict):
    AliasName: str
    KeyArn: NotRequired[str]

class CreateAliasInputTypeDef(TypedDict):
    AliasName: str
    KeyArn: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

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

class ImportTr31KeyBlockTypeDef(TypedDict):
    WrappingKeyIdentifier: str
    WrappedKeyBlock: str

class ImportTr34KeyBlockTypeDef(TypedDict):
    CertificateAuthorityPublicKeyIdentifier: str
    SigningKeyCertificate: str
    ImportToken: str
    WrappedKeyBlock: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    RandomNonce: NotRequired[str]

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

class CreateAliasOutputTypeDef(TypedDict):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAliasOutputTypeDef(TypedDict):
    Alias: AliasTypeDef
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

class ListAliasesOutputTypeDef(TypedDict):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateAliasOutputTypeDef(TypedDict):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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
    ExportToken: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    RandomNonce: NotRequired[str]
    KeyBlockHeaders: NotRequired[KeyBlockHeadersTypeDef]

class ListKeysOutputTypeDef(TypedDict):
    Keys: List[KeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

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

class ExportKeyMaterialTypeDef(TypedDict):
    Tr31KeyBlock: NotRequired[ExportTr31KeyBlockTypeDef]
    Tr34KeyBlock: NotRequired[ExportTr34KeyBlockTypeDef]
    KeyCryptogram: NotRequired[ExportKeyCryptogramTypeDef]
    DiffieHellmanTr31KeyBlock: NotRequired[ExportDiffieHellmanTr31KeyBlockTypeDef]

class ImportKeyInputTypeDef(TypedDict):
    KeyMaterial: ImportKeyMaterialTypeDef
    KeyCheckValueAlgorithm: NotRequired[KeyCheckValueAlgorithmType]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ExportKeyInputTypeDef(TypedDict):
    KeyMaterial: ExportKeyMaterialTypeDef
    ExportKeyIdentifier: str
    ExportAttributes: NotRequired[ExportAttributesTypeDef]
