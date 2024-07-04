"""
Type annotations for payment-cryptography-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_payment_cryptography_data.type_defs import AmexCardSecurityCodeVersion1TypeDef

    data: AmexCardSecurityCodeVersion1TypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict

from .literals import (
    DukptDerivationTypeType,
    DukptEncryptionModeType,
    DukptKeyVariantType,
    EmvEncryptionModeType,
    EmvMajorKeyDerivationModeType,
    EncryptionModeType,
    KeyCheckValueAlgorithmType,
    MacAlgorithmType,
    MajorKeyDerivationModeType,
    PaddingTypeType,
    PinBlockFormatForPinDataType,
    SessionKeyDerivationModeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
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
    "DecryptDataInputRequestTypeDef",
    "DecryptDataOutputTypeDef",
    "DiscoverDynamicCardVerificationCodeTypeDef",
    "DukptAttributesTypeDef",
    "DukptDerivationAttributesTypeDef",
    "DukptEncryptionAttributesTypeDef",
    "DynamicCardVerificationCodeTypeDef",
    "DynamicCardVerificationValueTypeDef",
    "EmvEncryptionAttributesTypeDef",
    "EncryptDataInputRequestTypeDef",
    "EncryptDataOutputTypeDef",
    "EncryptionDecryptionAttributesTypeDef",
    "GenerateCardValidationDataInputRequestTypeDef",
    "GenerateCardValidationDataOutputTypeDef",
    "GenerateMacInputRequestTypeDef",
    "GenerateMacOutputTypeDef",
    "GeneratePinDataInputRequestTypeDef",
    "GeneratePinDataOutputTypeDef",
    "Ibm3624NaturalPinTypeDef",
    "Ibm3624PinFromOffsetTypeDef",
    "Ibm3624PinOffsetTypeDef",
    "Ibm3624PinVerificationTypeDef",
    "Ibm3624RandomPinTypeDef",
    "MacAlgorithmDukptTypeDef",
    "MacAlgorithmEmvTypeDef",
    "MacAttributesTypeDef",
    "PinDataTypeDef",
    "PinGenerationAttributesTypeDef",
    "PinVerificationAttributesTypeDef",
    "ReEncryptDataInputRequestTypeDef",
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
    "TranslatePinDataInputRequestTypeDef",
    "TranslatePinDataOutputTypeDef",
    "TranslationIsoFormatsTypeDef",
    "TranslationPinDataIsoFormat034TypeDef",
    "VerifyAuthRequestCryptogramInputRequestTypeDef",
    "VerifyAuthRequestCryptogramOutputTypeDef",
    "VerifyCardValidationDataInputRequestTypeDef",
    "VerifyCardValidationDataOutputTypeDef",
    "VerifyMacInputRequestTypeDef",
    "VerifyMacOutputTypeDef",
    "VerifyPinDataInputRequestTypeDef",
    "VerifyPinDataOutputTypeDef",
    "VisaPinTypeDef",
    "VisaPinVerificationTypeDef",
    "VisaPinVerificationValueTypeDef",
    "WrappedKeyMaterialTypeDef",
    "WrappedKeyTypeDef",
)

AmexCardSecurityCodeVersion1TypeDef = TypedDict(
    "AmexCardSecurityCodeVersion1TypeDef",
    {
        "CardExpiryDate": str,
    },
)

AmexCardSecurityCodeVersion2TypeDef = TypedDict(
    "AmexCardSecurityCodeVersion2TypeDef",
    {
        "CardExpiryDate": str,
        "ServiceCode": str,
    },
)

AsymmetricEncryptionAttributesTypeDef = TypedDict(
    "AsymmetricEncryptionAttributesTypeDef",
    {
        "PaddingType": PaddingTypeType,
    },
    total=False,
)

CardGenerationAttributesTypeDef = TypedDict(
    "CardGenerationAttributesTypeDef",
    {
        "AmexCardSecurityCodeVersion1": "AmexCardSecurityCodeVersion1TypeDef",
        "AmexCardSecurityCodeVersion2": "AmexCardSecurityCodeVersion2TypeDef",
        "CardVerificationValue1": "CardVerificationValue1TypeDef",
        "CardVerificationValue2": "CardVerificationValue2TypeDef",
        "CardHolderVerificationValue": "CardHolderVerificationValueTypeDef",
        "DynamicCardVerificationCode": "DynamicCardVerificationCodeTypeDef",
        "DynamicCardVerificationValue": "DynamicCardVerificationValueTypeDef",
    },
    total=False,
)

CardHolderVerificationValueTypeDef = TypedDict(
    "CardHolderVerificationValueTypeDef",
    {
        "UnpredictableNumber": str,
        "PanSequenceNumber": str,
        "ApplicationTransactionCounter": str,
    },
)

CardVerificationAttributesTypeDef = TypedDict(
    "CardVerificationAttributesTypeDef",
    {
        "AmexCardSecurityCodeVersion1": "AmexCardSecurityCodeVersion1TypeDef",
        "AmexCardSecurityCodeVersion2": "AmexCardSecurityCodeVersion2TypeDef",
        "CardVerificationValue1": "CardVerificationValue1TypeDef",
        "CardVerificationValue2": "CardVerificationValue2TypeDef",
        "CardHolderVerificationValue": "CardHolderVerificationValueTypeDef",
        "DynamicCardVerificationCode": "DynamicCardVerificationCodeTypeDef",
        "DynamicCardVerificationValue": "DynamicCardVerificationValueTypeDef",
        "DiscoverDynamicCardVerificationCode": "DiscoverDynamicCardVerificationCodeTypeDef",
    },
    total=False,
)

CardVerificationValue1TypeDef = TypedDict(
    "CardVerificationValue1TypeDef",
    {
        "CardExpiryDate": str,
        "ServiceCode": str,
    },
)

CardVerificationValue2TypeDef = TypedDict(
    "CardVerificationValue2TypeDef",
    {
        "CardExpiryDate": str,
    },
)

CryptogramAuthResponseTypeDef = TypedDict(
    "CryptogramAuthResponseTypeDef",
    {
        "ArpcMethod1": "CryptogramVerificationArpcMethod1TypeDef",
        "ArpcMethod2": "CryptogramVerificationArpcMethod2TypeDef",
    },
    total=False,
)

CryptogramVerificationArpcMethod1TypeDef = TypedDict(
    "CryptogramVerificationArpcMethod1TypeDef",
    {
        "AuthResponseCode": str,
    },
)

_RequiredCryptogramVerificationArpcMethod2TypeDef = TypedDict(
    "_RequiredCryptogramVerificationArpcMethod2TypeDef",
    {
        "CardStatusUpdate": str,
    },
)
_OptionalCryptogramVerificationArpcMethod2TypeDef = TypedDict(
    "_OptionalCryptogramVerificationArpcMethod2TypeDef",
    {
        "ProprietaryAuthenticationData": str,
    },
    total=False,
)

class CryptogramVerificationArpcMethod2TypeDef(
    _RequiredCryptogramVerificationArpcMethod2TypeDef,
    _OptionalCryptogramVerificationArpcMethod2TypeDef,
):
    pass

_RequiredDecryptDataInputRequestTypeDef = TypedDict(
    "_RequiredDecryptDataInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "CipherText": str,
        "DecryptionAttributes": "EncryptionDecryptionAttributesTypeDef",
    },
)
_OptionalDecryptDataInputRequestTypeDef = TypedDict(
    "_OptionalDecryptDataInputRequestTypeDef",
    {
        "WrappedKey": "WrappedKeyTypeDef",
    },
    total=False,
)

class DecryptDataInputRequestTypeDef(
    _RequiredDecryptDataInputRequestTypeDef, _OptionalDecryptDataInputRequestTypeDef
):
    pass

DecryptDataOutputTypeDef = TypedDict(
    "DecryptDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "PlainText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscoverDynamicCardVerificationCodeTypeDef = TypedDict(
    "DiscoverDynamicCardVerificationCodeTypeDef",
    {
        "CardExpiryDate": str,
        "UnpredictableNumber": str,
        "ApplicationTransactionCounter": str,
    },
)

DukptAttributesTypeDef = TypedDict(
    "DukptAttributesTypeDef",
    {
        "KeySerialNumber": str,
        "DukptDerivationType": DukptDerivationTypeType,
    },
)

_RequiredDukptDerivationAttributesTypeDef = TypedDict(
    "_RequiredDukptDerivationAttributesTypeDef",
    {
        "KeySerialNumber": str,
    },
)
_OptionalDukptDerivationAttributesTypeDef = TypedDict(
    "_OptionalDukptDerivationAttributesTypeDef",
    {
        "DukptKeyDerivationType": DukptDerivationTypeType,
        "DukptKeyVariant": DukptKeyVariantType,
    },
    total=False,
)

class DukptDerivationAttributesTypeDef(
    _RequiredDukptDerivationAttributesTypeDef, _OptionalDukptDerivationAttributesTypeDef
):
    pass

_RequiredDukptEncryptionAttributesTypeDef = TypedDict(
    "_RequiredDukptEncryptionAttributesTypeDef",
    {
        "KeySerialNumber": str,
    },
)
_OptionalDukptEncryptionAttributesTypeDef = TypedDict(
    "_OptionalDukptEncryptionAttributesTypeDef",
    {
        "Mode": DukptEncryptionModeType,
        "DukptKeyDerivationType": DukptDerivationTypeType,
        "DukptKeyVariant": DukptKeyVariantType,
        "InitializationVector": str,
    },
    total=False,
)

class DukptEncryptionAttributesTypeDef(
    _RequiredDukptEncryptionAttributesTypeDef, _OptionalDukptEncryptionAttributesTypeDef
):
    pass

DynamicCardVerificationCodeTypeDef = TypedDict(
    "DynamicCardVerificationCodeTypeDef",
    {
        "UnpredictableNumber": str,
        "PanSequenceNumber": str,
        "ApplicationTransactionCounter": str,
        "TrackData": str,
    },
)

DynamicCardVerificationValueTypeDef = TypedDict(
    "DynamicCardVerificationValueTypeDef",
    {
        "PanSequenceNumber": str,
        "CardExpiryDate": str,
        "ServiceCode": str,
        "ApplicationTransactionCounter": str,
    },
)

_RequiredEmvEncryptionAttributesTypeDef = TypedDict(
    "_RequiredEmvEncryptionAttributesTypeDef",
    {
        "MajorKeyDerivationMode": EmvMajorKeyDerivationModeType,
        "PrimaryAccountNumber": str,
        "PanSequenceNumber": str,
        "SessionDerivationData": str,
    },
)
_OptionalEmvEncryptionAttributesTypeDef = TypedDict(
    "_OptionalEmvEncryptionAttributesTypeDef",
    {
        "Mode": EmvEncryptionModeType,
        "InitializationVector": str,
    },
    total=False,
)

class EmvEncryptionAttributesTypeDef(
    _RequiredEmvEncryptionAttributesTypeDef, _OptionalEmvEncryptionAttributesTypeDef
):
    pass

_RequiredEncryptDataInputRequestTypeDef = TypedDict(
    "_RequiredEncryptDataInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "PlainText": str,
        "EncryptionAttributes": "EncryptionDecryptionAttributesTypeDef",
    },
)
_OptionalEncryptDataInputRequestTypeDef = TypedDict(
    "_OptionalEncryptDataInputRequestTypeDef",
    {
        "WrappedKey": "WrappedKeyTypeDef",
    },
    total=False,
)

class EncryptDataInputRequestTypeDef(
    _RequiredEncryptDataInputRequestTypeDef, _OptionalEncryptDataInputRequestTypeDef
):
    pass

EncryptDataOutputTypeDef = TypedDict(
    "EncryptDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "CipherText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionDecryptionAttributesTypeDef = TypedDict(
    "EncryptionDecryptionAttributesTypeDef",
    {
        "Symmetric": "SymmetricEncryptionAttributesTypeDef",
        "Asymmetric": "AsymmetricEncryptionAttributesTypeDef",
        "Dukpt": "DukptEncryptionAttributesTypeDef",
        "Emv": "EmvEncryptionAttributesTypeDef",
    },
    total=False,
)

_RequiredGenerateCardValidationDataInputRequestTypeDef = TypedDict(
    "_RequiredGenerateCardValidationDataInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "PrimaryAccountNumber": str,
        "GenerationAttributes": "CardGenerationAttributesTypeDef",
    },
)
_OptionalGenerateCardValidationDataInputRequestTypeDef = TypedDict(
    "_OptionalGenerateCardValidationDataInputRequestTypeDef",
    {
        "ValidationDataLength": int,
    },
    total=False,
)

class GenerateCardValidationDataInputRequestTypeDef(
    _RequiredGenerateCardValidationDataInputRequestTypeDef,
    _OptionalGenerateCardValidationDataInputRequestTypeDef,
):
    pass

GenerateCardValidationDataOutputTypeDef = TypedDict(
    "GenerateCardValidationDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "ValidationData": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateMacInputRequestTypeDef = TypedDict(
    "_RequiredGenerateMacInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "MessageData": str,
        "GenerationAttributes": "MacAttributesTypeDef",
    },
)
_OptionalGenerateMacInputRequestTypeDef = TypedDict(
    "_OptionalGenerateMacInputRequestTypeDef",
    {
        "MacLength": int,
    },
    total=False,
)

class GenerateMacInputRequestTypeDef(
    _RequiredGenerateMacInputRequestTypeDef, _OptionalGenerateMacInputRequestTypeDef
):
    pass

GenerateMacOutputTypeDef = TypedDict(
    "GenerateMacOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "Mac": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGeneratePinDataInputRequestTypeDef = TypedDict(
    "_RequiredGeneratePinDataInputRequestTypeDef",
    {
        "GenerationKeyIdentifier": str,
        "EncryptionKeyIdentifier": str,
        "GenerationAttributes": "PinGenerationAttributesTypeDef",
        "PrimaryAccountNumber": str,
        "PinBlockFormat": PinBlockFormatForPinDataType,
    },
)
_OptionalGeneratePinDataInputRequestTypeDef = TypedDict(
    "_OptionalGeneratePinDataInputRequestTypeDef",
    {
        "PinDataLength": int,
    },
    total=False,
)

class GeneratePinDataInputRequestTypeDef(
    _RequiredGeneratePinDataInputRequestTypeDef, _OptionalGeneratePinDataInputRequestTypeDef
):
    pass

GeneratePinDataOutputTypeDef = TypedDict(
    "GeneratePinDataOutputTypeDef",
    {
        "GenerationKeyArn": str,
        "GenerationKeyCheckValue": str,
        "EncryptionKeyArn": str,
        "EncryptionKeyCheckValue": str,
        "EncryptedPinBlock": str,
        "PinData": "PinDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Ibm3624NaturalPinTypeDef = TypedDict(
    "Ibm3624NaturalPinTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationDataPadCharacter": str,
        "PinValidationData": str,
    },
)

Ibm3624PinFromOffsetTypeDef = TypedDict(
    "Ibm3624PinFromOffsetTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationDataPadCharacter": str,
        "PinValidationData": str,
        "PinOffset": str,
    },
)

Ibm3624PinOffsetTypeDef = TypedDict(
    "Ibm3624PinOffsetTypeDef",
    {
        "EncryptedPinBlock": str,
        "DecimalizationTable": str,
        "PinValidationDataPadCharacter": str,
        "PinValidationData": str,
    },
)

Ibm3624PinVerificationTypeDef = TypedDict(
    "Ibm3624PinVerificationTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationDataPadCharacter": str,
        "PinValidationData": str,
        "PinOffset": str,
    },
)

Ibm3624RandomPinTypeDef = TypedDict(
    "Ibm3624RandomPinTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationDataPadCharacter": str,
        "PinValidationData": str,
    },
)

_RequiredMacAlgorithmDukptTypeDef = TypedDict(
    "_RequiredMacAlgorithmDukptTypeDef",
    {
        "KeySerialNumber": str,
        "DukptKeyVariant": DukptKeyVariantType,
    },
)
_OptionalMacAlgorithmDukptTypeDef = TypedDict(
    "_OptionalMacAlgorithmDukptTypeDef",
    {
        "DukptDerivationType": DukptDerivationTypeType,
    },
    total=False,
)

class MacAlgorithmDukptTypeDef(
    _RequiredMacAlgorithmDukptTypeDef, _OptionalMacAlgorithmDukptTypeDef
):
    pass

MacAlgorithmEmvTypeDef = TypedDict(
    "MacAlgorithmEmvTypeDef",
    {
        "MajorKeyDerivationMode": MajorKeyDerivationModeType,
        "PrimaryAccountNumber": str,
        "PanSequenceNumber": str,
        "SessionKeyDerivationMode": SessionKeyDerivationModeType,
        "SessionKeyDerivationValue": "SessionKeyDerivationValueTypeDef",
    },
)

MacAttributesTypeDef = TypedDict(
    "MacAttributesTypeDef",
    {
        "Algorithm": MacAlgorithmType,
        "EmvMac": "MacAlgorithmEmvTypeDef",
        "DukptIso9797Algorithm1": "MacAlgorithmDukptTypeDef",
        "DukptIso9797Algorithm3": "MacAlgorithmDukptTypeDef",
        "DukptCmac": "MacAlgorithmDukptTypeDef",
    },
    total=False,
)

PinDataTypeDef = TypedDict(
    "PinDataTypeDef",
    {
        "PinOffset": str,
        "VerificationValue": str,
    },
    total=False,
)

PinGenerationAttributesTypeDef = TypedDict(
    "PinGenerationAttributesTypeDef",
    {
        "VisaPin": "VisaPinTypeDef",
        "VisaPinVerificationValue": "VisaPinVerificationValueTypeDef",
        "Ibm3624PinOffset": "Ibm3624PinOffsetTypeDef",
        "Ibm3624NaturalPin": "Ibm3624NaturalPinTypeDef",
        "Ibm3624RandomPin": "Ibm3624RandomPinTypeDef",
        "Ibm3624PinFromOffset": "Ibm3624PinFromOffsetTypeDef",
    },
    total=False,
)

PinVerificationAttributesTypeDef = TypedDict(
    "PinVerificationAttributesTypeDef",
    {
        "VisaPin": "VisaPinVerificationTypeDef",
        "Ibm3624Pin": "Ibm3624PinVerificationTypeDef",
    },
    total=False,
)

_RequiredReEncryptDataInputRequestTypeDef = TypedDict(
    "_RequiredReEncryptDataInputRequestTypeDef",
    {
        "IncomingKeyIdentifier": str,
        "OutgoingKeyIdentifier": str,
        "CipherText": str,
        "IncomingEncryptionAttributes": "ReEncryptionAttributesTypeDef",
        "OutgoingEncryptionAttributes": "ReEncryptionAttributesTypeDef",
    },
)
_OptionalReEncryptDataInputRequestTypeDef = TypedDict(
    "_OptionalReEncryptDataInputRequestTypeDef",
    {
        "IncomingWrappedKey": "WrappedKeyTypeDef",
        "OutgoingWrappedKey": "WrappedKeyTypeDef",
    },
    total=False,
)

class ReEncryptDataInputRequestTypeDef(
    _RequiredReEncryptDataInputRequestTypeDef, _OptionalReEncryptDataInputRequestTypeDef
):
    pass

ReEncryptDataOutputTypeDef = TypedDict(
    "ReEncryptDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "CipherText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReEncryptionAttributesTypeDef = TypedDict(
    "ReEncryptionAttributesTypeDef",
    {
        "Symmetric": "SymmetricEncryptionAttributesTypeDef",
        "Dukpt": "DukptEncryptionAttributesTypeDef",
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

SessionKeyAmexTypeDef = TypedDict(
    "SessionKeyAmexTypeDef",
    {
        "PrimaryAccountNumber": str,
        "PanSequenceNumber": str,
    },
)

SessionKeyDerivationTypeDef = TypedDict(
    "SessionKeyDerivationTypeDef",
    {
        "EmvCommon": "SessionKeyEmvCommonTypeDef",
        "Mastercard": "SessionKeyMastercardTypeDef",
        "Emv2000": "SessionKeyEmv2000TypeDef",
        "Amex": "SessionKeyAmexTypeDef",
        "Visa": "SessionKeyVisaTypeDef",
    },
    total=False,
)

SessionKeyDerivationValueTypeDef = TypedDict(
    "SessionKeyDerivationValueTypeDef",
    {
        "ApplicationCryptogram": str,
        "ApplicationTransactionCounter": str,
    },
    total=False,
)

SessionKeyEmv2000TypeDef = TypedDict(
    "SessionKeyEmv2000TypeDef",
    {
        "PrimaryAccountNumber": str,
        "PanSequenceNumber": str,
        "ApplicationTransactionCounter": str,
    },
)

SessionKeyEmvCommonTypeDef = TypedDict(
    "SessionKeyEmvCommonTypeDef",
    {
        "PrimaryAccountNumber": str,
        "PanSequenceNumber": str,
        "ApplicationTransactionCounter": str,
    },
)

SessionKeyMastercardTypeDef = TypedDict(
    "SessionKeyMastercardTypeDef",
    {
        "PrimaryAccountNumber": str,
        "PanSequenceNumber": str,
        "ApplicationTransactionCounter": str,
        "UnpredictableNumber": str,
    },
)

SessionKeyVisaTypeDef = TypedDict(
    "SessionKeyVisaTypeDef",
    {
        "PrimaryAccountNumber": str,
        "PanSequenceNumber": str,
    },
)

_RequiredSymmetricEncryptionAttributesTypeDef = TypedDict(
    "_RequiredSymmetricEncryptionAttributesTypeDef",
    {
        "Mode": EncryptionModeType,
    },
)
_OptionalSymmetricEncryptionAttributesTypeDef = TypedDict(
    "_OptionalSymmetricEncryptionAttributesTypeDef",
    {
        "InitializationVector": str,
        "PaddingType": PaddingTypeType,
    },
    total=False,
)

class SymmetricEncryptionAttributesTypeDef(
    _RequiredSymmetricEncryptionAttributesTypeDef, _OptionalSymmetricEncryptionAttributesTypeDef
):
    pass

_RequiredTranslatePinDataInputRequestTypeDef = TypedDict(
    "_RequiredTranslatePinDataInputRequestTypeDef",
    {
        "IncomingKeyIdentifier": str,
        "OutgoingKeyIdentifier": str,
        "IncomingTranslationAttributes": "TranslationIsoFormatsTypeDef",
        "OutgoingTranslationAttributes": "TranslationIsoFormatsTypeDef",
        "EncryptedPinBlock": str,
    },
)
_OptionalTranslatePinDataInputRequestTypeDef = TypedDict(
    "_OptionalTranslatePinDataInputRequestTypeDef",
    {
        "IncomingDukptAttributes": "DukptDerivationAttributesTypeDef",
        "OutgoingDukptAttributes": "DukptDerivationAttributesTypeDef",
        "IncomingWrappedKey": "WrappedKeyTypeDef",
        "OutgoingWrappedKey": "WrappedKeyTypeDef",
    },
    total=False,
)

class TranslatePinDataInputRequestTypeDef(
    _RequiredTranslatePinDataInputRequestTypeDef, _OptionalTranslatePinDataInputRequestTypeDef
):
    pass

TranslatePinDataOutputTypeDef = TypedDict(
    "TranslatePinDataOutputTypeDef",
    {
        "PinBlock": str,
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TranslationIsoFormatsTypeDef = TypedDict(
    "TranslationIsoFormatsTypeDef",
    {
        "IsoFormat0": "TranslationPinDataIsoFormat034TypeDef",
        "IsoFormat1": Dict[str, Any],
        "IsoFormat3": "TranslationPinDataIsoFormat034TypeDef",
        "IsoFormat4": "TranslationPinDataIsoFormat034TypeDef",
    },
    total=False,
)

TranslationPinDataIsoFormat034TypeDef = TypedDict(
    "TranslationPinDataIsoFormat034TypeDef",
    {
        "PrimaryAccountNumber": str,
    },
)

_RequiredVerifyAuthRequestCryptogramInputRequestTypeDef = TypedDict(
    "_RequiredVerifyAuthRequestCryptogramInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "TransactionData": str,
        "AuthRequestCryptogram": str,
        "MajorKeyDerivationMode": MajorKeyDerivationModeType,
        "SessionKeyDerivationAttributes": "SessionKeyDerivationTypeDef",
    },
)
_OptionalVerifyAuthRequestCryptogramInputRequestTypeDef = TypedDict(
    "_OptionalVerifyAuthRequestCryptogramInputRequestTypeDef",
    {
        "AuthResponseAttributes": "CryptogramAuthResponseTypeDef",
    },
    total=False,
)

class VerifyAuthRequestCryptogramInputRequestTypeDef(
    _RequiredVerifyAuthRequestCryptogramInputRequestTypeDef,
    _OptionalVerifyAuthRequestCryptogramInputRequestTypeDef,
):
    pass

VerifyAuthRequestCryptogramOutputTypeDef = TypedDict(
    "VerifyAuthRequestCryptogramOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "AuthResponseValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyCardValidationDataInputRequestTypeDef = TypedDict(
    "VerifyCardValidationDataInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "PrimaryAccountNumber": str,
        "VerificationAttributes": "CardVerificationAttributesTypeDef",
        "ValidationData": str,
    },
)

VerifyCardValidationDataOutputTypeDef = TypedDict(
    "VerifyCardValidationDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVerifyMacInputRequestTypeDef = TypedDict(
    "_RequiredVerifyMacInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "MessageData": str,
        "Mac": str,
        "VerificationAttributes": "MacAttributesTypeDef",
    },
)
_OptionalVerifyMacInputRequestTypeDef = TypedDict(
    "_OptionalVerifyMacInputRequestTypeDef",
    {
        "MacLength": int,
    },
    total=False,
)

class VerifyMacInputRequestTypeDef(
    _RequiredVerifyMacInputRequestTypeDef, _OptionalVerifyMacInputRequestTypeDef
):
    pass

VerifyMacOutputTypeDef = TypedDict(
    "VerifyMacOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVerifyPinDataInputRequestTypeDef = TypedDict(
    "_RequiredVerifyPinDataInputRequestTypeDef",
    {
        "VerificationKeyIdentifier": str,
        "EncryptionKeyIdentifier": str,
        "VerificationAttributes": "PinVerificationAttributesTypeDef",
        "EncryptedPinBlock": str,
        "PrimaryAccountNumber": str,
        "PinBlockFormat": PinBlockFormatForPinDataType,
    },
)
_OptionalVerifyPinDataInputRequestTypeDef = TypedDict(
    "_OptionalVerifyPinDataInputRequestTypeDef",
    {
        "PinDataLength": int,
        "DukptAttributes": "DukptAttributesTypeDef",
    },
    total=False,
)

class VerifyPinDataInputRequestTypeDef(
    _RequiredVerifyPinDataInputRequestTypeDef, _OptionalVerifyPinDataInputRequestTypeDef
):
    pass

VerifyPinDataOutputTypeDef = TypedDict(
    "VerifyPinDataOutputTypeDef",
    {
        "VerificationKeyArn": str,
        "VerificationKeyCheckValue": str,
        "EncryptionKeyArn": str,
        "EncryptionKeyCheckValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VisaPinTypeDef = TypedDict(
    "VisaPinTypeDef",
    {
        "PinVerificationKeyIndex": int,
    },
)

VisaPinVerificationTypeDef = TypedDict(
    "VisaPinVerificationTypeDef",
    {
        "PinVerificationKeyIndex": int,
        "VerificationValue": str,
    },
)

VisaPinVerificationValueTypeDef = TypedDict(
    "VisaPinVerificationValueTypeDef",
    {
        "EncryptedPinBlock": str,
        "PinVerificationKeyIndex": int,
    },
)

WrappedKeyMaterialTypeDef = TypedDict(
    "WrappedKeyMaterialTypeDef",
    {
        "Tr31KeyBlock": str,
    },
    total=False,
)

_RequiredWrappedKeyTypeDef = TypedDict(
    "_RequiredWrappedKeyTypeDef",
    {
        "WrappedKeyMaterial": "WrappedKeyMaterialTypeDef",
    },
)
_OptionalWrappedKeyTypeDef = TypedDict(
    "_OptionalWrappedKeyTypeDef",
    {
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
    },
    total=False,
)

class WrappedKeyTypeDef(_RequiredWrappedKeyTypeDef, _OptionalWrappedKeyTypeDef):
    pass
