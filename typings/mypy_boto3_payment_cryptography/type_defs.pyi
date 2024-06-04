"""
Type annotations for payment-cryptography service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/type_defs.html)

Usage::

    ```python
    from mypy_boto3_payment_cryptography.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    KeyAlgorithmType,
    KeyCheckValueAlgorithmType,
    KeyClassType,
    KeyExportabilityType,
    KeyMaterialTypeType,
    KeyOriginType,
    KeyStateType,
    KeyUsageType,
    WrappedKeyMaterialFormatType,
    WrappingKeySpecType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AliasTypeDef",
    "CreateAliasInputRequestTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateKeyInputRequestTypeDef",
    "CreateKeyOutputTypeDef",
    "DeleteAliasInputRequestTypeDef",
    "DeleteKeyInputRequestTypeDef",
    "DeleteKeyOutputTypeDef",
    "ExportAttributesTypeDef",
    "ExportDukptInitialKeyTypeDef",
    "ExportKeyCryptogramTypeDef",
    "ExportKeyInputRequestTypeDef",
    "ExportKeyMaterialTypeDef",
    "ExportKeyOutputTypeDef",
    "ExportTr31KeyBlockTypeDef",
    "ExportTr34KeyBlockTypeDef",
    "GetAliasInputRequestTypeDef",
    "GetAliasOutputTypeDef",
    "GetKeyInputRequestTypeDef",
    "GetKeyOutputTypeDef",
    "GetParametersForExportInputRequestTypeDef",
    "GetParametersForExportOutputTypeDef",
    "GetParametersForImportInputRequestTypeDef",
    "GetParametersForImportOutputTypeDef",
    "GetPublicKeyCertificateInputRequestTypeDef",
    "GetPublicKeyCertificateOutputTypeDef",
    "ImportKeyCryptogramTypeDef",
    "ImportKeyInputRequestTypeDef",
    "ImportKeyMaterialTypeDef",
    "ImportKeyOutputTypeDef",
    "ImportTr31KeyBlockTypeDef",
    "ImportTr34KeyBlockTypeDef",
    "KeyAttributesTypeDef",
    "KeyBlockHeadersTypeDef",
    "KeyModesOfUseTypeDef",
    "KeySummaryTypeDef",
    "KeyTypeDef",
    "ListAliasesInputRequestTypeDef",
    "ListAliasesOutputTypeDef",
    "ListKeysInputRequestTypeDef",
    "ListKeysOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreKeyInputRequestTypeDef",
    "RestoreKeyOutputTypeDef",
    "RootCertificatePublicKeyTypeDef",
    "StartKeyUsageInputRequestTypeDef",
    "StartKeyUsageOutputTypeDef",
    "StopKeyUsageInputRequestTypeDef",
    "StopKeyUsageOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TrustedCertificatePublicKeyTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAliasInputRequestTypeDef",
    "UpdateAliasOutputTypeDef",
    "WrappedKeyTypeDef",
)

_RequiredAliasTypeDef = TypedDict(
    "_RequiredAliasTypeDef",
    {
        "AliasName": str,
    },
)
_OptionalAliasTypeDef = TypedDict(
    "_OptionalAliasTypeDef",
    {
        "KeyArn": str,
    },
    total=False,
)

class AliasTypeDef(_RequiredAliasTypeDef, _OptionalAliasTypeDef):
    pass

_RequiredCreateAliasInputRequestTypeDef = TypedDict(
    "_RequiredCreateAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)
_OptionalCreateAliasInputRequestTypeDef = TypedDict(
    "_OptionalCreateAliasInputRequestTypeDef",
    {
        "KeyArn": str,
    },
    total=False,
)

class CreateAliasInputRequestTypeDef(
    _RequiredCreateAliasInputRequestTypeDef, _OptionalCreateAliasInputRequestTypeDef
):
    pass

CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKeyInputRequestTypeDef = TypedDict(
    "_RequiredCreateKeyInputRequestTypeDef",
    {
        "KeyAttributes": "KeyAttributesTypeDef",
        "Exportable": bool,
    },
)
_OptionalCreateKeyInputRequestTypeDef = TypedDict(
    "_OptionalCreateKeyInputRequestTypeDef",
    {
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateKeyInputRequestTypeDef(
    _RequiredCreateKeyInputRequestTypeDef, _OptionalCreateKeyInputRequestTypeDef
):
    pass

CreateKeyOutputTypeDef = TypedDict(
    "CreateKeyOutputTypeDef",
    {
        "Key": "KeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAliasInputRequestTypeDef = TypedDict(
    "DeleteAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)

_RequiredDeleteKeyInputRequestTypeDef = TypedDict(
    "_RequiredDeleteKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
_OptionalDeleteKeyInputRequestTypeDef = TypedDict(
    "_OptionalDeleteKeyInputRequestTypeDef",
    {
        "DeleteKeyInDays": int,
    },
    total=False,
)

class DeleteKeyInputRequestTypeDef(
    _RequiredDeleteKeyInputRequestTypeDef, _OptionalDeleteKeyInputRequestTypeDef
):
    pass

DeleteKeyOutputTypeDef = TypedDict(
    "DeleteKeyOutputTypeDef",
    {
        "Key": "KeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportAttributesTypeDef = TypedDict(
    "ExportAttributesTypeDef",
    {
        "ExportDukptInitialKey": "ExportDukptInitialKeyTypeDef",
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
    },
    total=False,
)

ExportDukptInitialKeyTypeDef = TypedDict(
    "ExportDukptInitialKeyTypeDef",
    {
        "KeySerialNumber": str,
    },
)

_RequiredExportKeyCryptogramTypeDef = TypedDict(
    "_RequiredExportKeyCryptogramTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "WrappingKeyCertificate": str,
    },
)
_OptionalExportKeyCryptogramTypeDef = TypedDict(
    "_OptionalExportKeyCryptogramTypeDef",
    {
        "WrappingSpec": WrappingKeySpecType,
    },
    total=False,
)

class ExportKeyCryptogramTypeDef(
    _RequiredExportKeyCryptogramTypeDef, _OptionalExportKeyCryptogramTypeDef
):
    pass

_RequiredExportKeyInputRequestTypeDef = TypedDict(
    "_RequiredExportKeyInputRequestTypeDef",
    {
        "KeyMaterial": "ExportKeyMaterialTypeDef",
        "ExportKeyIdentifier": str,
    },
)
_OptionalExportKeyInputRequestTypeDef = TypedDict(
    "_OptionalExportKeyInputRequestTypeDef",
    {
        "ExportAttributes": "ExportAttributesTypeDef",
    },
    total=False,
)

class ExportKeyInputRequestTypeDef(
    _RequiredExportKeyInputRequestTypeDef, _OptionalExportKeyInputRequestTypeDef
):
    pass

ExportKeyMaterialTypeDef = TypedDict(
    "ExportKeyMaterialTypeDef",
    {
        "Tr31KeyBlock": "ExportTr31KeyBlockTypeDef",
        "Tr34KeyBlock": "ExportTr34KeyBlockTypeDef",
        "KeyCryptogram": "ExportKeyCryptogramTypeDef",
    },
    total=False,
)

ExportKeyOutputTypeDef = TypedDict(
    "ExportKeyOutputTypeDef",
    {
        "WrappedKey": "WrappedKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportTr31KeyBlockTypeDef = TypedDict(
    "_RequiredExportTr31KeyBlockTypeDef",
    {
        "WrappingKeyIdentifier": str,
    },
)
_OptionalExportTr31KeyBlockTypeDef = TypedDict(
    "_OptionalExportTr31KeyBlockTypeDef",
    {
        "KeyBlockHeaders": "KeyBlockHeadersTypeDef",
    },
    total=False,
)

class ExportTr31KeyBlockTypeDef(
    _RequiredExportTr31KeyBlockTypeDef, _OptionalExportTr31KeyBlockTypeDef
):
    pass

_RequiredExportTr34KeyBlockTypeDef = TypedDict(
    "_RequiredExportTr34KeyBlockTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "WrappingKeyCertificate": str,
        "ExportToken": str,
        "KeyBlockFormat": Literal["X9_TR34_2012"],
    },
)
_OptionalExportTr34KeyBlockTypeDef = TypedDict(
    "_OptionalExportTr34KeyBlockTypeDef",
    {
        "RandomNonce": str,
        "KeyBlockHeaders": "KeyBlockHeadersTypeDef",
    },
    total=False,
)

class ExportTr34KeyBlockTypeDef(
    _RequiredExportTr34KeyBlockTypeDef, _OptionalExportTr34KeyBlockTypeDef
):
    pass

GetAliasInputRequestTypeDef = TypedDict(
    "GetAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)

GetAliasOutputTypeDef = TypedDict(
    "GetAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyInputRequestTypeDef = TypedDict(
    "GetKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)

GetKeyOutputTypeDef = TypedDict(
    "GetKeyOutputTypeDef",
    {
        "Key": "KeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersForExportInputRequestTypeDef = TypedDict(
    "GetParametersForExportInputRequestTypeDef",
    {
        "KeyMaterialType": KeyMaterialTypeType,
        "SigningKeyAlgorithm": KeyAlgorithmType,
    },
)

GetParametersForExportOutputTypeDef = TypedDict(
    "GetParametersForExportOutputTypeDef",
    {
        "SigningKeyCertificate": str,
        "SigningKeyCertificateChain": str,
        "SigningKeyAlgorithm": KeyAlgorithmType,
        "ExportToken": str,
        "ParametersValidUntilTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersForImportInputRequestTypeDef = TypedDict(
    "GetParametersForImportInputRequestTypeDef",
    {
        "KeyMaterialType": KeyMaterialTypeType,
        "WrappingKeyAlgorithm": KeyAlgorithmType,
    },
)

GetParametersForImportOutputTypeDef = TypedDict(
    "GetParametersForImportOutputTypeDef",
    {
        "WrappingKeyCertificate": str,
        "WrappingKeyCertificateChain": str,
        "WrappingKeyAlgorithm": KeyAlgorithmType,
        "ImportToken": str,
        "ParametersValidUntilTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyCertificateInputRequestTypeDef = TypedDict(
    "GetPublicKeyCertificateInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)

GetPublicKeyCertificateOutputTypeDef = TypedDict(
    "GetPublicKeyCertificateOutputTypeDef",
    {
        "KeyCertificate": str,
        "KeyCertificateChain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportKeyCryptogramTypeDef = TypedDict(
    "_RequiredImportKeyCryptogramTypeDef",
    {
        "KeyAttributes": "KeyAttributesTypeDef",
        "Exportable": bool,
        "WrappedKeyCryptogram": str,
        "ImportToken": str,
    },
)
_OptionalImportKeyCryptogramTypeDef = TypedDict(
    "_OptionalImportKeyCryptogramTypeDef",
    {
        "WrappingSpec": WrappingKeySpecType,
    },
    total=False,
)

class ImportKeyCryptogramTypeDef(
    _RequiredImportKeyCryptogramTypeDef, _OptionalImportKeyCryptogramTypeDef
):
    pass

_RequiredImportKeyInputRequestTypeDef = TypedDict(
    "_RequiredImportKeyInputRequestTypeDef",
    {
        "KeyMaterial": "ImportKeyMaterialTypeDef",
    },
)
_OptionalImportKeyInputRequestTypeDef = TypedDict(
    "_OptionalImportKeyInputRequestTypeDef",
    {
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportKeyInputRequestTypeDef(
    _RequiredImportKeyInputRequestTypeDef, _OptionalImportKeyInputRequestTypeDef
):
    pass

ImportKeyMaterialTypeDef = TypedDict(
    "ImportKeyMaterialTypeDef",
    {
        "RootCertificatePublicKey": "RootCertificatePublicKeyTypeDef",
        "TrustedCertificatePublicKey": "TrustedCertificatePublicKeyTypeDef",
        "Tr31KeyBlock": "ImportTr31KeyBlockTypeDef",
        "Tr34KeyBlock": "ImportTr34KeyBlockTypeDef",
        "KeyCryptogram": "ImportKeyCryptogramTypeDef",
    },
    total=False,
)

ImportKeyOutputTypeDef = TypedDict(
    "ImportKeyOutputTypeDef",
    {
        "Key": "KeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportTr31KeyBlockTypeDef = TypedDict(
    "ImportTr31KeyBlockTypeDef",
    {
        "WrappingKeyIdentifier": str,
        "WrappedKeyBlock": str,
    },
)

_RequiredImportTr34KeyBlockTypeDef = TypedDict(
    "_RequiredImportTr34KeyBlockTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "SigningKeyCertificate": str,
        "ImportToken": str,
        "WrappedKeyBlock": str,
        "KeyBlockFormat": Literal["X9_TR34_2012"],
    },
)
_OptionalImportTr34KeyBlockTypeDef = TypedDict(
    "_OptionalImportTr34KeyBlockTypeDef",
    {
        "RandomNonce": str,
    },
    total=False,
)

class ImportTr34KeyBlockTypeDef(
    _RequiredImportTr34KeyBlockTypeDef, _OptionalImportTr34KeyBlockTypeDef
):
    pass

KeyAttributesTypeDef = TypedDict(
    "KeyAttributesTypeDef",
    {
        "KeyUsage": KeyUsageType,
        "KeyClass": KeyClassType,
        "KeyAlgorithm": KeyAlgorithmType,
        "KeyModesOfUse": "KeyModesOfUseTypeDef",
    },
)

KeyBlockHeadersTypeDef = TypedDict(
    "KeyBlockHeadersTypeDef",
    {
        "KeyModesOfUse": "KeyModesOfUseTypeDef",
        "KeyExportability": KeyExportabilityType,
        "KeyVersion": str,
        "OptionalBlocks": Dict[str, str],
    },
    total=False,
)

KeyModesOfUseTypeDef = TypedDict(
    "KeyModesOfUseTypeDef",
    {
        "Encrypt": bool,
        "Decrypt": bool,
        "Wrap": bool,
        "Unwrap": bool,
        "Generate": bool,
        "Sign": bool,
        "Verify": bool,
        "DeriveKey": bool,
        "NoRestrictions": bool,
    },
    total=False,
)

KeySummaryTypeDef = TypedDict(
    "KeySummaryTypeDef",
    {
        "KeyArn": str,
        "KeyState": KeyStateType,
        "KeyAttributes": "KeyAttributesTypeDef",
        "KeyCheckValue": str,
        "Exportable": bool,
        "Enabled": bool,
    },
)

_RequiredKeyTypeDef = TypedDict(
    "_RequiredKeyTypeDef",
    {
        "KeyArn": str,
        "KeyAttributes": "KeyAttributesTypeDef",
        "KeyCheckValue": str,
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
        "Enabled": bool,
        "Exportable": bool,
        "KeyState": KeyStateType,
        "KeyOrigin": KeyOriginType,
        "CreateTimestamp": datetime,
    },
)
_OptionalKeyTypeDef = TypedDict(
    "_OptionalKeyTypeDef",
    {
        "UsageStartTimestamp": datetime,
        "UsageStopTimestamp": datetime,
        "DeletePendingTimestamp": datetime,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

class KeyTypeDef(_RequiredKeyTypeDef, _OptionalKeyTypeDef):
    pass

ListAliasesInputRequestTypeDef = TypedDict(
    "ListAliasesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeysInputRequestTypeDef = TypedDict(
    "ListKeysInputRequestTypeDef",
    {
        "KeyState": KeyStateType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListKeysOutputTypeDef = TypedDict(
    "ListKeysOutputTypeDef",
    {
        "Keys": List["KeySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RestoreKeyInputRequestTypeDef = TypedDict(
    "RestoreKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)

RestoreKeyOutputTypeDef = TypedDict(
    "RestoreKeyOutputTypeDef",
    {
        "Key": "KeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RootCertificatePublicKeyTypeDef = TypedDict(
    "RootCertificatePublicKeyTypeDef",
    {
        "KeyAttributes": "KeyAttributesTypeDef",
        "PublicKeyCertificate": str,
    },
)

StartKeyUsageInputRequestTypeDef = TypedDict(
    "StartKeyUsageInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)

StartKeyUsageOutputTypeDef = TypedDict(
    "StartKeyUsageOutputTypeDef",
    {
        "Key": "KeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopKeyUsageInputRequestTypeDef = TypedDict(
    "StopKeyUsageInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)

StopKeyUsageOutputTypeDef = TypedDict(
    "StopKeyUsageOutputTypeDef",
    {
        "Key": "KeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

TrustedCertificatePublicKeyTypeDef = TypedDict(
    "TrustedCertificatePublicKeyTypeDef",
    {
        "KeyAttributes": "KeyAttributesTypeDef",
        "PublicKeyCertificate": str,
        "CertificateAuthorityPublicKeyIdentifier": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAliasInputRequestTypeDef = TypedDict(
    "_RequiredUpdateAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)
_OptionalUpdateAliasInputRequestTypeDef = TypedDict(
    "_OptionalUpdateAliasInputRequestTypeDef",
    {
        "KeyArn": str,
    },
    total=False,
)

class UpdateAliasInputRequestTypeDef(
    _RequiredUpdateAliasInputRequestTypeDef, _OptionalUpdateAliasInputRequestTypeDef
):
    pass

UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWrappedKeyTypeDef = TypedDict(
    "_RequiredWrappedKeyTypeDef",
    {
        "WrappingKeyArn": str,
        "WrappedKeyMaterialFormat": WrappedKeyMaterialFormatType,
        "KeyMaterial": str,
    },
)
_OptionalWrappedKeyTypeDef = TypedDict(
    "_OptionalWrappedKeyTypeDef",
    {
        "KeyCheckValue": str,
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
    },
    total=False,
)

class WrappedKeyTypeDef(_RequiredWrappedKeyTypeDef, _OptionalWrappedKeyTypeDef):
    pass
