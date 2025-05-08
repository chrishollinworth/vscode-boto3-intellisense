"""
Type annotations for payment-cryptography-data service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_payment_cryptography_data.type_defs import CurrentPinAttributesTypeDef

    data: CurrentPinAttributesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from .literals import (
    DukptDerivationTypeType,
    DukptEncryptionModeType,
    DukptKeyVariantType,
    EmvEncryptionModeType,
    EmvMajorKeyDerivationModeType,
    EncryptionModeType,
    KeyCheckValueAlgorithmType,
    KeyDerivationFunctionType,
    KeyDerivationHashAlgorithmType,
    MacAlgorithmType,
    MajorKeyDerivationModeType,
    PaddingTypeType,
    PinBlockFormatForEmvPinChangeType,
    PinBlockFormatForPinDataType,
    PinBlockLengthPositionType,
    PinBlockPaddingTypeType,
    SessionKeyDerivationModeType,
    SymmetricKeyAlgorithmType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AmexAttributesTypeDef",
    "AmexCardSecurityCodeVersion1TypeDef",
    "AmexCardSecurityCodeVersion2TypeDef",
    "AsymmetricEncryptionAttributesTypeDef",
    "CardGenerationAttributesTypeDef",
    "CardHolderVerificationValueTypeDef",
    "CardVerificationAttributesTypeDef",
    "CardVerificationValue1TypeDef",
    "CardVerificationValue2TypeDef",
    "CryptogramAuthResponseTypeDef",
    "CryptogramVerificationArpcMethod1TypeDef",
    "CryptogramVerificationArpcMethod2TypeDef",
    "CurrentPinAttributesTypeDef",
    "DecryptDataInputTypeDef",
    "DecryptDataOutputTypeDef",
    "DerivationMethodAttributesTypeDef",
    "DiscoverDynamicCardVerificationCodeTypeDef",
    "DukptAttributesTypeDef",
    "DukptDerivationAttributesTypeDef",
    "DukptEncryptionAttributesTypeDef",
    "DynamicCardVerificationCodeTypeDef",
    "DynamicCardVerificationValueTypeDef",
    "EcdhDerivationAttributesTypeDef",
    "Emv2000AttributesTypeDef",
    "EmvCommonAttributesTypeDef",
    "EmvEncryptionAttributesTypeDef",
    "EncryptDataInputTypeDef",
    "EncryptDataOutputTypeDef",
    "EncryptionDecryptionAttributesTypeDef",
    "GenerateCardValidationDataInputTypeDef",
    "GenerateCardValidationDataOutputTypeDef",
    "GenerateMacEmvPinChangeInputTypeDef",
    "GenerateMacEmvPinChangeOutputTypeDef",
    "GenerateMacInputTypeDef",
    "GenerateMacOutputTypeDef",
    "GeneratePinDataInputTypeDef",
    "GeneratePinDataOutputTypeDef",
    "Ibm3624NaturalPinTypeDef",
    "Ibm3624PinFromOffsetTypeDef",
    "Ibm3624PinOffsetTypeDef",
    "Ibm3624PinVerificationTypeDef",
    "Ibm3624RandomPinTypeDef",
    "MacAlgorithmDukptTypeDef",
    "MacAlgorithmEmvTypeDef",
    "MacAttributesTypeDef",
    "MasterCardAttributesTypeDef",
    "PinDataTypeDef",
    "PinGenerationAttributesTypeDef",
    "PinVerificationAttributesTypeDef",
    "ReEncryptDataInputTypeDef",
    "ReEncryptDataOutputTypeDef",
    "ReEncryptionAttributesTypeDef",
    "ResponseMetadataTypeDef",
    "SessionKeyAmexTypeDef",
    "SessionKeyDerivationTypeDef",
    "SessionKeyDerivationValueTypeDef",
    "SessionKeyEmv2000TypeDef",
    "SessionKeyEmvCommonTypeDef",
    "SessionKeyMastercardTypeDef",
    "SessionKeyVisaTypeDef",
    "SymmetricEncryptionAttributesTypeDef",
    "TranslatePinDataInputTypeDef",
    "TranslatePinDataOutputTypeDef",
    "TranslationIsoFormatsTypeDef",
    "TranslationPinDataIsoFormat034TypeDef",
    "VerifyAuthRequestCryptogramInputTypeDef",
    "VerifyAuthRequestCryptogramOutputTypeDef",
    "VerifyCardValidationDataInputTypeDef",
    "VerifyCardValidationDataOutputTypeDef",
    "VerifyMacInputTypeDef",
    "VerifyMacOutputTypeDef",
    "VerifyPinDataInputTypeDef",
    "VerifyPinDataOutputTypeDef",
    "VisaAmexDerivationOutputsTypeDef",
    "VisaAttributesTypeDef",
    "VisaPinTypeDef",
    "VisaPinVerificationTypeDef",
    "VisaPinVerificationValueTypeDef",
    "WrappedKeyMaterialTypeDef",
    "WrappedKeyTypeDef",
)

class CurrentPinAttributesTypeDef(TypedDict):
    CurrentPinPekIdentifier: str
    CurrentEncryptedPinBlock: str

class AmexCardSecurityCodeVersion1TypeDef(TypedDict):
    CardExpiryDate: str

class AmexCardSecurityCodeVersion2TypeDef(TypedDict):
    CardExpiryDate: str
    ServiceCode: str

class AsymmetricEncryptionAttributesTypeDef(TypedDict):
    PaddingType: NotRequired[PaddingTypeType]

class CardHolderVerificationValueTypeDef(TypedDict):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class CardVerificationValue1TypeDef(TypedDict):
    CardExpiryDate: str
    ServiceCode: str

class CardVerificationValue2TypeDef(TypedDict):
    CardExpiryDate: str

class DynamicCardVerificationCodeTypeDef(TypedDict):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    TrackData: str

class DynamicCardVerificationValueTypeDef(TypedDict):
    PanSequenceNumber: str
    CardExpiryDate: str
    ServiceCode: str
    ApplicationTransactionCounter: str

class DiscoverDynamicCardVerificationCodeTypeDef(TypedDict):
    CardExpiryDate: str
    UnpredictableNumber: str
    ApplicationTransactionCounter: str

class CryptogramVerificationArpcMethod1TypeDef(TypedDict):
    AuthResponseCode: str

class CryptogramVerificationArpcMethod2TypeDef(TypedDict):
    CardStatusUpdate: str
    ProprietaryAuthenticationData: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class Emv2000AttributesTypeDef(TypedDict):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class EmvCommonAttributesTypeDef(TypedDict):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationCryptogram: str
    Mode: EmvEncryptionModeType
    PinBlockPaddingType: PinBlockPaddingTypeType
    PinBlockLengthPosition: PinBlockLengthPositionType

class MasterCardAttributesTypeDef(TypedDict):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationCryptogram: str

class DukptAttributesTypeDef(TypedDict):
    KeySerialNumber: str
    DukptDerivationType: DukptDerivationTypeType

class DukptDerivationAttributesTypeDef(TypedDict):
    KeySerialNumber: str
    DukptKeyDerivationType: NotRequired[DukptDerivationTypeType]
    DukptKeyVariant: NotRequired[DukptKeyVariantType]

class DukptEncryptionAttributesTypeDef(TypedDict):
    KeySerialNumber: str
    Mode: NotRequired[DukptEncryptionModeType]
    DukptKeyDerivationType: NotRequired[DukptDerivationTypeType]
    DukptKeyVariant: NotRequired[DukptKeyVariantType]
    InitializationVector: NotRequired[str]

class EcdhDerivationAttributesTypeDef(TypedDict):
    CertificateAuthorityPublicKeyIdentifier: str
    PublicKeyCertificate: str
    KeyAlgorithm: SymmetricKeyAlgorithmType
    KeyDerivationFunction: KeyDerivationFunctionType
    KeyDerivationHashAlgorithm: KeyDerivationHashAlgorithmType
    SharedInformation: str

class EmvEncryptionAttributesTypeDef(TypedDict):
    MajorKeyDerivationMode: EmvMajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionDerivationData: str
    Mode: NotRequired[EmvEncryptionModeType]
    InitializationVector: NotRequired[str]

class SymmetricEncryptionAttributesTypeDef(TypedDict):
    Mode: EncryptionModeType
    InitializationVector: NotRequired[str]
    PaddingType: NotRequired[PaddingTypeType]

class VisaAmexDerivationOutputsTypeDef(TypedDict):
    AuthorizationRequestKeyArn: str
    AuthorizationRequestKeyCheckValue: str
    CurrentPinPekArn: NotRequired[str]
    CurrentPinPekKeyCheckValue: NotRequired[str]

class PinDataTypeDef(TypedDict):
    PinOffset: NotRequired[str]
    VerificationValue: NotRequired[str]

class Ibm3624NaturalPinTypeDef(TypedDict):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class Ibm3624PinFromOffsetTypeDef(TypedDict):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str

class Ibm3624PinOffsetTypeDef(TypedDict):
    EncryptedPinBlock: str
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class Ibm3624PinVerificationTypeDef(TypedDict):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str

class Ibm3624RandomPinTypeDef(TypedDict):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class MacAlgorithmDukptTypeDef(TypedDict):
    KeySerialNumber: str
    DukptKeyVariant: DukptKeyVariantType
    DukptDerivationType: NotRequired[DukptDerivationTypeType]

class SessionKeyDerivationValueTypeDef(TypedDict):
    ApplicationCryptogram: NotRequired[str]
    ApplicationTransactionCounter: NotRequired[str]

class VisaPinTypeDef(TypedDict):
    PinVerificationKeyIndex: int

class VisaPinVerificationValueTypeDef(TypedDict):
    EncryptedPinBlock: str
    PinVerificationKeyIndex: int

class VisaPinVerificationTypeDef(TypedDict):
    PinVerificationKeyIndex: int
    VerificationValue: str

class SessionKeyAmexTypeDef(TypedDict):
    PrimaryAccountNumber: str
    PanSequenceNumber: str

class SessionKeyEmv2000TypeDef(TypedDict):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class SessionKeyEmvCommonTypeDef(TypedDict):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class SessionKeyMastercardTypeDef(TypedDict):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    UnpredictableNumber: str

class SessionKeyVisaTypeDef(TypedDict):
    PrimaryAccountNumber: str
    PanSequenceNumber: str

class TranslationPinDataIsoFormat034TypeDef(TypedDict):
    PrimaryAccountNumber: str

class AmexAttributesTypeDef(TypedDict):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    AuthorizationRequestKeyIdentifier: str
    CurrentPinAttributes: NotRequired[CurrentPinAttributesTypeDef]

class VisaAttributesTypeDef(TypedDict):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    AuthorizationRequestKeyIdentifier: str
    CurrentPinAttributes: NotRequired[CurrentPinAttributesTypeDef]

class CardGenerationAttributesTypeDef(TypedDict):
    AmexCardSecurityCodeVersion1: NotRequired[AmexCardSecurityCodeVersion1TypeDef]
    AmexCardSecurityCodeVersion2: NotRequired[AmexCardSecurityCodeVersion2TypeDef]
    CardVerificationValue1: NotRequired[CardVerificationValue1TypeDef]
    CardVerificationValue2: NotRequired[CardVerificationValue2TypeDef]
    CardHolderVerificationValue: NotRequired[CardHolderVerificationValueTypeDef]
    DynamicCardVerificationCode: NotRequired[DynamicCardVerificationCodeTypeDef]
    DynamicCardVerificationValue: NotRequired[DynamicCardVerificationValueTypeDef]

class CardVerificationAttributesTypeDef(TypedDict):
    AmexCardSecurityCodeVersion1: NotRequired[AmexCardSecurityCodeVersion1TypeDef]
    AmexCardSecurityCodeVersion2: NotRequired[AmexCardSecurityCodeVersion2TypeDef]
    CardVerificationValue1: NotRequired[CardVerificationValue1TypeDef]
    CardVerificationValue2: NotRequired[CardVerificationValue2TypeDef]
    CardHolderVerificationValue: NotRequired[CardHolderVerificationValueTypeDef]
    DynamicCardVerificationCode: NotRequired[DynamicCardVerificationCodeTypeDef]
    DynamicCardVerificationValue: NotRequired[DynamicCardVerificationValueTypeDef]
    DiscoverDynamicCardVerificationCode: NotRequired[DiscoverDynamicCardVerificationCodeTypeDef]

class CryptogramAuthResponseTypeDef(TypedDict):
    ArpcMethod1: NotRequired[CryptogramVerificationArpcMethod1TypeDef]
    ArpcMethod2: NotRequired[CryptogramVerificationArpcMethod2TypeDef]

class DecryptDataOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    PlainText: str
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptDataOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateCardValidationDataOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    ValidationData: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMacOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    Mac: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReEncryptDataOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadataTypeDef

class TranslatePinDataOutputTypeDef(TypedDict):
    PinBlock: str
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyAuthRequestCryptogramOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    AuthResponseValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyCardValidationDataOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyMacOutputTypeDef(TypedDict):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyPinDataOutputTypeDef(TypedDict):
    VerificationKeyArn: str
    VerificationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class WrappedKeyMaterialTypeDef(TypedDict):
    Tr31KeyBlock: NotRequired[str]
    DiffieHellmanSymmetricKey: NotRequired[EcdhDerivationAttributesTypeDef]

class EncryptionDecryptionAttributesTypeDef(TypedDict):
    Symmetric: NotRequired[SymmetricEncryptionAttributesTypeDef]
    Asymmetric: NotRequired[AsymmetricEncryptionAttributesTypeDef]
    Dukpt: NotRequired[DukptEncryptionAttributesTypeDef]
    Emv: NotRequired[EmvEncryptionAttributesTypeDef]

class ReEncryptionAttributesTypeDef(TypedDict):
    Symmetric: NotRequired[SymmetricEncryptionAttributesTypeDef]
    Dukpt: NotRequired[DukptEncryptionAttributesTypeDef]

class GenerateMacEmvPinChangeOutputTypeDef(TypedDict):
    NewPinPekArn: str
    SecureMessagingIntegrityKeyArn: str
    SecureMessagingConfidentialityKeyArn: str
    Mac: str
    EncryptedPinBlock: str
    NewPinPekKeyCheckValue: str
    SecureMessagingIntegrityKeyCheckValue: str
    SecureMessagingConfidentialityKeyCheckValue: str
    VisaAmexDerivationOutputs: VisaAmexDerivationOutputsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GeneratePinDataOutputTypeDef(TypedDict):
    GenerationKeyArn: str
    GenerationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    EncryptedPinBlock: str
    PinData: PinDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MacAlgorithmEmvTypeDef(TypedDict):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionKeyDerivationMode: SessionKeyDerivationModeType
    SessionKeyDerivationValue: SessionKeyDerivationValueTypeDef

class PinGenerationAttributesTypeDef(TypedDict):
    VisaPin: NotRequired[VisaPinTypeDef]
    VisaPinVerificationValue: NotRequired[VisaPinVerificationValueTypeDef]
    Ibm3624PinOffset: NotRequired[Ibm3624PinOffsetTypeDef]
    Ibm3624NaturalPin: NotRequired[Ibm3624NaturalPinTypeDef]
    Ibm3624RandomPin: NotRequired[Ibm3624RandomPinTypeDef]
    Ibm3624PinFromOffset: NotRequired[Ibm3624PinFromOffsetTypeDef]

class PinVerificationAttributesTypeDef(TypedDict):
    VisaPin: NotRequired[VisaPinVerificationTypeDef]
    Ibm3624Pin: NotRequired[Ibm3624PinVerificationTypeDef]

class SessionKeyDerivationTypeDef(TypedDict):
    EmvCommon: NotRequired[SessionKeyEmvCommonTypeDef]
    Mastercard: NotRequired[SessionKeyMastercardTypeDef]
    Emv2000: NotRequired[SessionKeyEmv2000TypeDef]
    Amex: NotRequired[SessionKeyAmexTypeDef]
    Visa: NotRequired[SessionKeyVisaTypeDef]

class TranslationIsoFormatsTypeDef(TypedDict):
    IsoFormat0: NotRequired[TranslationPinDataIsoFormat034TypeDef]
    IsoFormat1: NotRequired[Mapping[str, Any]]
    IsoFormat3: NotRequired[TranslationPinDataIsoFormat034TypeDef]
    IsoFormat4: NotRequired[TranslationPinDataIsoFormat034TypeDef]

class DerivationMethodAttributesTypeDef(TypedDict):
    EmvCommon: NotRequired[EmvCommonAttributesTypeDef]
    Amex: NotRequired[AmexAttributesTypeDef]
    Visa: NotRequired[VisaAttributesTypeDef]
    Emv2000: NotRequired[Emv2000AttributesTypeDef]
    Mastercard: NotRequired[MasterCardAttributesTypeDef]

class GenerateCardValidationDataInputTypeDef(TypedDict):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    GenerationAttributes: CardGenerationAttributesTypeDef
    ValidationDataLength: NotRequired[int]

class VerifyCardValidationDataInputTypeDef(TypedDict):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    VerificationAttributes: CardVerificationAttributesTypeDef
    ValidationData: str

class WrappedKeyTypeDef(TypedDict):
    WrappedKeyMaterial: WrappedKeyMaterialTypeDef
    KeyCheckValueAlgorithm: NotRequired[KeyCheckValueAlgorithmType]

class MacAttributesTypeDef(TypedDict):
    Algorithm: NotRequired[MacAlgorithmType]
    EmvMac: NotRequired[MacAlgorithmEmvTypeDef]
    DukptIso9797Algorithm1: NotRequired[MacAlgorithmDukptTypeDef]
    DukptIso9797Algorithm3: NotRequired[MacAlgorithmDukptTypeDef]
    DukptCmac: NotRequired[MacAlgorithmDukptTypeDef]

class VerifyAuthRequestCryptogramInputTypeDef(TypedDict):
    KeyIdentifier: str
    TransactionData: str
    AuthRequestCryptogram: str
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    SessionKeyDerivationAttributes: SessionKeyDerivationTypeDef
    AuthResponseAttributes: NotRequired[CryptogramAuthResponseTypeDef]

class GenerateMacEmvPinChangeInputTypeDef(TypedDict):
    NewPinPekIdentifier: str
    NewEncryptedPinBlock: str
    PinBlockFormat: PinBlockFormatForEmvPinChangeType
    SecureMessagingIntegrityKeyIdentifier: str
    SecureMessagingConfidentialityKeyIdentifier: str
    MessageData: str
    DerivationMethodAttributes: DerivationMethodAttributesTypeDef

class DecryptDataInputTypeDef(TypedDict):
    KeyIdentifier: str
    CipherText: str
    DecryptionAttributes: EncryptionDecryptionAttributesTypeDef
    WrappedKey: NotRequired[WrappedKeyTypeDef]

class EncryptDataInputTypeDef(TypedDict):
    KeyIdentifier: str
    PlainText: str
    EncryptionAttributes: EncryptionDecryptionAttributesTypeDef
    WrappedKey: NotRequired[WrappedKeyTypeDef]

class GeneratePinDataInputTypeDef(TypedDict):
    GenerationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    GenerationAttributes: PinGenerationAttributesTypeDef
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: NotRequired[int]
    EncryptionWrappedKey: NotRequired[WrappedKeyTypeDef]

class ReEncryptDataInputTypeDef(TypedDict):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    CipherText: str
    IncomingEncryptionAttributes: ReEncryptionAttributesTypeDef
    OutgoingEncryptionAttributes: ReEncryptionAttributesTypeDef
    IncomingWrappedKey: NotRequired[WrappedKeyTypeDef]
    OutgoingWrappedKey: NotRequired[WrappedKeyTypeDef]

class TranslatePinDataInputTypeDef(TypedDict):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    IncomingTranslationAttributes: TranslationIsoFormatsTypeDef
    OutgoingTranslationAttributes: TranslationIsoFormatsTypeDef
    EncryptedPinBlock: str
    IncomingDukptAttributes: NotRequired[DukptDerivationAttributesTypeDef]
    OutgoingDukptAttributes: NotRequired[DukptDerivationAttributesTypeDef]
    IncomingWrappedKey: NotRequired[WrappedKeyTypeDef]
    OutgoingWrappedKey: NotRequired[WrappedKeyTypeDef]

class VerifyPinDataInputTypeDef(TypedDict):
    VerificationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    VerificationAttributes: PinVerificationAttributesTypeDef
    EncryptedPinBlock: str
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: NotRequired[int]
    DukptAttributes: NotRequired[DukptAttributesTypeDef]
    EncryptionWrappedKey: NotRequired[WrappedKeyTypeDef]

class GenerateMacInputTypeDef(TypedDict):
    KeyIdentifier: str
    MessageData: str
    GenerationAttributes: MacAttributesTypeDef
    MacLength: NotRequired[int]

class VerifyMacInputTypeDef(TypedDict):
    KeyIdentifier: str
    MessageData: str
    Mac: str
    VerificationAttributes: MacAttributesTypeDef
    MacLength: NotRequired[int]
