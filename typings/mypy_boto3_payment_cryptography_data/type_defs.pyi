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
        "CardHolderVerificationValue": "CardHolderVerificationValueTypeDef",
        "CardVerificationValue1": "CardVerificationValue1TypeDef",
        "CardVerificationValue2": "CardVerificationValue2TypeDef",
        "DynamicCardVerificationCode": "DynamicCardVerificationCodeTypeDef",
        "DynamicCardVerificationValue": "DynamicCardVerificationValueTypeDef",
    },
    total=False,
)

CardHolderVerificationValueTypeDef = TypedDict(
    "CardHolderVerificationValueTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "UnpredictableNumber": str,
    },
)

CardVerificationAttributesTypeDef = TypedDict(
    "CardVerificationAttributesTypeDef",
    {
        "AmexCardSecurityCodeVersion1": "AmexCardSecurityCodeVersion1TypeDef",
        "AmexCardSecurityCodeVersion2": "AmexCardSecurityCodeVersion2TypeDef",
        "CardHolderVerificationValue": "CardHolderVerificationValueTypeDef",
        "CardVerificationValue1": "CardVerificationValue1TypeDef",
        "CardVerificationValue2": "CardVerificationValue2TypeDef",
        "DiscoverDynamicCardVerificationCode": "DiscoverDynamicCardVerificationCodeTypeDef",
        "DynamicCardVerificationCode": "DynamicCardVerificationCodeTypeDef",
        "DynamicCardVerificationValue": "DynamicCardVerificationValueTypeDef",
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

DecryptDataInputRequestTypeDef = TypedDict(
    "DecryptDataInputRequestTypeDef",
    {
        "CipherText": str,
        "DecryptionAttributes": "EncryptionDecryptionAttributesTypeDef",
        "KeyIdentifier": str,
    },
)

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
        "ApplicationTransactionCounter": str,
        "CardExpiryDate": str,
        "UnpredictableNumber": str,
    },
)

DukptAttributesTypeDef = TypedDict(
    "DukptAttributesTypeDef",
    {
        "DukptDerivationType": DukptDerivationTypeType,
        "KeySerialNumber": str,
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
        "DukptKeyDerivationType": DukptDerivationTypeType,
        "DukptKeyVariant": DukptKeyVariantType,
        "InitializationVector": str,
        "Mode": DukptEncryptionModeType,
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
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "TrackData": str,
        "UnpredictableNumber": str,
    },
)

DynamicCardVerificationValueTypeDef = TypedDict(
    "DynamicCardVerificationValueTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "CardExpiryDate": str,
        "PanSequenceNumber": str,
        "ServiceCode": str,
    },
)

_RequiredEmvEncryptionAttributesTypeDef = TypedDict(
    "_RequiredEmvEncryptionAttributesTypeDef",
    {
        "MajorKeyDerivationMode": EmvMajorKeyDerivationModeType,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
        "SessionDerivationData": str,
    },
)
_OptionalEmvEncryptionAttributesTypeDef = TypedDict(
    "_OptionalEmvEncryptionAttributesTypeDef",
    {
        "InitializationVector": str,
        "Mode": EmvEncryptionModeType,
    },
    total=False,
)

class EmvEncryptionAttributesTypeDef(
    _RequiredEmvEncryptionAttributesTypeDef, _OptionalEmvEncryptionAttributesTypeDef
):
    pass

EncryptDataInputRequestTypeDef = TypedDict(
    "EncryptDataInputRequestTypeDef",
    {
        "EncryptionAttributes": "EncryptionDecryptionAttributesTypeDef",
        "KeyIdentifier": str,
        "PlainText": str,
    },
)

EncryptDataOutputTypeDef = TypedDict(
    "EncryptDataOutputTypeDef",
    {
        "CipherText": str,
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionDecryptionAttributesTypeDef = TypedDict(
    "EncryptionDecryptionAttributesTypeDef",
    {
        "Asymmetric": "AsymmetricEncryptionAttributesTypeDef",
        "Dukpt": "DukptEncryptionAttributesTypeDef",
        "Emv": "EmvEncryptionAttributesTypeDef",
        "Symmetric": "SymmetricEncryptionAttributesTypeDef",
    },
    total=False,
)

_RequiredGenerateCardValidationDataInputRequestTypeDef = TypedDict(
    "_RequiredGenerateCardValidationDataInputRequestTypeDef",
    {
        "GenerationAttributes": "CardGenerationAttributesTypeDef",
        "KeyIdentifier": str,
        "PrimaryAccountNumber": str,
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
        "GenerationAttributes": "MacAttributesTypeDef",
        "KeyIdentifier": str,
        "MessageData": str,
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
        "EncryptionKeyIdentifier": str,
        "GenerationAttributes": "PinGenerationAttributesTypeDef",
        "GenerationKeyIdentifier": str,
        "PinBlockFormat": PinBlockFormatForPinDataType,
        "PrimaryAccountNumber": str,
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
        "EncryptedPinBlock": str,
        "EncryptionKeyArn": str,
        "EncryptionKeyCheckValue": str,
        "GenerationKeyArn": str,
        "GenerationKeyCheckValue": str,
        "PinData": "PinDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Ibm3624NaturalPinTypeDef = TypedDict(
    "Ibm3624NaturalPinTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)

Ibm3624PinFromOffsetTypeDef = TypedDict(
    "Ibm3624PinFromOffsetTypeDef",
    {
        "DecimalizationTable": str,
        "PinOffset": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)

Ibm3624PinOffsetTypeDef = TypedDict(
    "Ibm3624PinOffsetTypeDef",
    {
        "DecimalizationTable": str,
        "EncryptedPinBlock": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)

Ibm3624PinVerificationTypeDef = TypedDict(
    "Ibm3624PinVerificationTypeDef",
    {
        "DecimalizationTable": str,
        "PinOffset": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)

Ibm3624RandomPinTypeDef = TypedDict(
    "Ibm3624RandomPinTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)

_RequiredMacAlgorithmDukptTypeDef = TypedDict(
    "_RequiredMacAlgorithmDukptTypeDef",
    {
        "DukptKeyVariant": DukptKeyVariantType,
        "KeySerialNumber": str,
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
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
        "SessionKeyDerivationMode": SessionKeyDerivationModeType,
        "SessionKeyDerivationValue": "SessionKeyDerivationValueTypeDef",
    },
)

MacAttributesTypeDef = TypedDict(
    "MacAttributesTypeDef",
    {
        "Algorithm": MacAlgorithmType,
        "DukptCmac": "MacAlgorithmDukptTypeDef",
        "DukptIso9797Algorithm1": "MacAlgorithmDukptTypeDef",
        "DukptIso9797Algorithm3": "MacAlgorithmDukptTypeDef",
        "EmvMac": "MacAlgorithmEmvTypeDef",
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
        "Ibm3624NaturalPin": "Ibm3624NaturalPinTypeDef",
        "Ibm3624PinFromOffset": "Ibm3624PinFromOffsetTypeDef",
        "Ibm3624PinOffset": "Ibm3624PinOffsetTypeDef",
        "Ibm3624RandomPin": "Ibm3624RandomPinTypeDef",
        "VisaPin": "VisaPinTypeDef",
        "VisaPinVerificationValue": "VisaPinVerificationValueTypeDef",
    },
    total=False,
)

PinVerificationAttributesTypeDef = TypedDict(
    "PinVerificationAttributesTypeDef",
    {
        "Ibm3624Pin": "Ibm3624PinVerificationTypeDef",
        "VisaPin": "VisaPinVerificationTypeDef",
    },
    total=False,
)

ReEncryptDataInputRequestTypeDef = TypedDict(
    "ReEncryptDataInputRequestTypeDef",
    {
        "CipherText": str,
        "IncomingEncryptionAttributes": "ReEncryptionAttributesTypeDef",
        "IncomingKeyIdentifier": str,
        "OutgoingEncryptionAttributes": "ReEncryptionAttributesTypeDef",
        "OutgoingKeyIdentifier": str,
    },
)

ReEncryptDataOutputTypeDef = TypedDict(
    "ReEncryptDataOutputTypeDef",
    {
        "CipherText": str,
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReEncryptionAttributesTypeDef = TypedDict(
    "ReEncryptionAttributesTypeDef",
    {
        "Dukpt": "DukptEncryptionAttributesTypeDef",
        "Symmetric": "SymmetricEncryptionAttributesTypeDef",
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
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
    },
)

SessionKeyDerivationTypeDef = TypedDict(
    "SessionKeyDerivationTypeDef",
    {
        "Amex": "SessionKeyAmexTypeDef",
        "Emv2000": "SessionKeyEmv2000TypeDef",
        "EmvCommon": "SessionKeyEmvCommonTypeDef",
        "Mastercard": "SessionKeyMastercardTypeDef",
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
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
    },
)

SessionKeyEmvCommonTypeDef = TypedDict(
    "SessionKeyEmvCommonTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
    },
)

SessionKeyMastercardTypeDef = TypedDict(
    "SessionKeyMastercardTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
        "UnpredictableNumber": str,
    },
)

SessionKeyVisaTypeDef = TypedDict(
    "SessionKeyVisaTypeDef",
    {
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
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
        "EncryptedPinBlock": str,
        "IncomingKeyIdentifier": str,
        "IncomingTranslationAttributes": "TranslationIsoFormatsTypeDef",
        "OutgoingKeyIdentifier": str,
        "OutgoingTranslationAttributes": "TranslationIsoFormatsTypeDef",
    },
)
_OptionalTranslatePinDataInputRequestTypeDef = TypedDict(
    "_OptionalTranslatePinDataInputRequestTypeDef",
    {
        "IncomingDukptAttributes": "DukptDerivationAttributesTypeDef",
        "OutgoingDukptAttributes": "DukptDerivationAttributesTypeDef",
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
        "KeyArn": str,
        "KeyCheckValue": str,
        "PinBlock": str,
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
        "AuthRequestCryptogram": str,
        "KeyIdentifier": str,
        "MajorKeyDerivationMode": MajorKeyDerivationModeType,
        "SessionKeyDerivationAttributes": "SessionKeyDerivationTypeDef",
        "TransactionData": str,
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
        "AuthResponseValue": str,
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyCardValidationDataInputRequestTypeDef = TypedDict(
    "VerifyCardValidationDataInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "PrimaryAccountNumber": str,
        "ValidationData": str,
        "VerificationAttributes": "CardVerificationAttributesTypeDef",
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
        "Mac": str,
        "MessageData": str,
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
        "EncryptedPinBlock": str,
        "EncryptionKeyIdentifier": str,
        "PinBlockFormat": PinBlockFormatForPinDataType,
        "PrimaryAccountNumber": str,
        "VerificationAttributes": "PinVerificationAttributesTypeDef",
        "VerificationKeyIdentifier": str,
    },
)
_OptionalVerifyPinDataInputRequestTypeDef = TypedDict(
    "_OptionalVerifyPinDataInputRequestTypeDef",
    {
        "DukptAttributes": "DukptAttributesTypeDef",
        "PinDataLength": int,
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
        "EncryptionKeyArn": str,
        "EncryptionKeyCheckValue": str,
        "VerificationKeyArn": str,
        "VerificationKeyCheckValue": str,
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
