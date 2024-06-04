"""
Type annotations for payment-cryptography-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_payment_cryptography_data import PaymentCryptographyDataPlaneClient

    client: PaymentCryptographyDataPlaneClient = boto3.client("payment-cryptography-data")
    ```
"""

from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import MajorKeyDerivationModeType, PinBlockFormatForPinDataType
from .type_defs import (
    CardGenerationAttributesTypeDef,
    CardVerificationAttributesTypeDef,
    CryptogramAuthResponseTypeDef,
    DecryptDataOutputTypeDef,
    DukptAttributesTypeDef,
    DukptDerivationAttributesTypeDef,
    EncryptDataOutputTypeDef,
    EncryptionDecryptionAttributesTypeDef,
    GenerateCardValidationDataOutputTypeDef,
    GenerateMacOutputTypeDef,
    GeneratePinDataOutputTypeDef,
    MacAttributesTypeDef,
    PinGenerationAttributesTypeDef,
    PinVerificationAttributesTypeDef,
    ReEncryptDataOutputTypeDef,
    ReEncryptionAttributesTypeDef,
    SessionKeyDerivationTypeDef,
    TranslatePinDataOutputTypeDef,
    TranslationIsoFormatsTypeDef,
    VerifyAuthRequestCryptogramOutputTypeDef,
    VerifyCardValidationDataOutputTypeDef,
    VerifyMacOutputTypeDef,
    VerifyPinDataOutputTypeDef,
)

__all__ = ("PaymentCryptographyDataPlaneClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]
    VerificationFailedException: Type[BotocoreClientError]

class PaymentCryptographyDataPlaneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PaymentCryptographyDataPlaneClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#close)
        """

    def decrypt_data(
        self,
        *,
        CipherText: str,
        DecryptionAttributes: "EncryptionDecryptionAttributesTypeDef",
        KeyIdentifier: str
    ) -> DecryptDataOutputTypeDef:
        """
        Decrypts ciphertext data to plaintext using a symmetric (TDES, AES), asymmetric
        (RSA), or derived (DUKPT or EMV) encryption key scheme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.decrypt_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#decrypt_data)
        """

    def encrypt_data(
        self,
        *,
        EncryptionAttributes: "EncryptionDecryptionAttributesTypeDef",
        KeyIdentifier: str,
        PlainText: str
    ) -> EncryptDataOutputTypeDef:
        """
        Encrypts plaintext data to ciphertext using a symmetric (TDES, AES), asymmetric
        (RSA), or derived (DUKPT or EMV) encryption key scheme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.encrypt_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#encrypt_data)
        """

    def generate_card_validation_data(
        self,
        *,
        GenerationAttributes: "CardGenerationAttributesTypeDef",
        KeyIdentifier: str,
        PrimaryAccountNumber: str,
        ValidationDataLength: int = None
    ) -> GenerateCardValidationDataOutputTypeDef:
        """
        Generates card-related validation data using algorithms such as Card
        Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2),
        or Card Security Codes (CSC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.generate_card_validation_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#generate_card_validation_data)
        """

    def generate_mac(
        self,
        *,
        GenerationAttributes: "MacAttributesTypeDef",
        KeyIdentifier: str,
        MessageData: str,
        MacLength: int = None
    ) -> GenerateMacOutputTypeDef:
        """
        Generates a Message Authentication Code (MAC) cryptogram within Amazon Web
        Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.generate_mac)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#generate_mac)
        """

    def generate_pin_data(
        self,
        *,
        EncryptionKeyIdentifier: str,
        GenerationAttributes: "PinGenerationAttributesTypeDef",
        GenerationKeyIdentifier: str,
        PinBlockFormat: PinBlockFormatForPinDataType,
        PrimaryAccountNumber: str,
        PinDataLength: int = None
    ) -> GeneratePinDataOutputTypeDef:
        """
        Generates pin-related data such as PIN, PIN Verification Value (PVV), PIN Block,
        and PIN Offset during new card issuance or reissuance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.generate_pin_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#generate_pin_data)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#generate_presigned_url)
        """

    def re_encrypt_data(
        self,
        *,
        CipherText: str,
        IncomingEncryptionAttributes: "ReEncryptionAttributesTypeDef",
        IncomingKeyIdentifier: str,
        OutgoingEncryptionAttributes: "ReEncryptionAttributesTypeDef",
        OutgoingKeyIdentifier: str
    ) -> ReEncryptDataOutputTypeDef:
        """
        Re-encrypt ciphertext using DUKPT, Symmetric and Asymmetric Data Encryption
        Keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.re_encrypt_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#re_encrypt_data)
        """

    def translate_pin_data(
        self,
        *,
        EncryptedPinBlock: str,
        IncomingKeyIdentifier: str,
        IncomingTranslationAttributes: "TranslationIsoFormatsTypeDef",
        OutgoingKeyIdentifier: str,
        OutgoingTranslationAttributes: "TranslationIsoFormatsTypeDef",
        IncomingDukptAttributes: "DukptDerivationAttributesTypeDef" = None,
        OutgoingDukptAttributes: "DukptDerivationAttributesTypeDef" = None
    ) -> TranslatePinDataOutputTypeDef:
        """
        Translates encrypted PIN block from and to ISO 9564 formats 0,1,3,4.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.translate_pin_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#translate_pin_data)
        """

    def verify_auth_request_cryptogram(
        self,
        *,
        AuthRequestCryptogram: str,
        KeyIdentifier: str,
        MajorKeyDerivationMode: MajorKeyDerivationModeType,
        SessionKeyDerivationAttributes: "SessionKeyDerivationTypeDef",
        TransactionData: str,
        AuthResponseAttributes: "CryptogramAuthResponseTypeDef" = None
    ) -> VerifyAuthRequestCryptogramOutputTypeDef:
        """
        Verifies Authorization Request Cryptogram (ARQC) for a EMV chip payment card
        authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.verify_auth_request_cryptogram)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#verify_auth_request_cryptogram)
        """

    def verify_card_validation_data(
        self,
        *,
        KeyIdentifier: str,
        PrimaryAccountNumber: str,
        ValidationData: str,
        VerificationAttributes: "CardVerificationAttributesTypeDef"
    ) -> VerifyCardValidationDataOutputTypeDef:
        """
        Verifies card-related validation data using algorithms such as Card Verification
        Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2) and Card
        Security Codes (CSC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.verify_card_validation_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#verify_card_validation_data)
        """

    def verify_mac(
        self,
        *,
        KeyIdentifier: str,
        Mac: str,
        MessageData: str,
        VerificationAttributes: "MacAttributesTypeDef",
        MacLength: int = None
    ) -> VerifyMacOutputTypeDef:
        """
        Verifies a Message Authentication Code (MAC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.verify_mac)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#verify_mac)
        """

    def verify_pin_data(
        self,
        *,
        EncryptedPinBlock: str,
        EncryptionKeyIdentifier: str,
        PinBlockFormat: PinBlockFormatForPinDataType,
        PrimaryAccountNumber: str,
        VerificationAttributes: "PinVerificationAttributesTypeDef",
        VerificationKeyIdentifier: str,
        DukptAttributes: "DukptAttributesTypeDef" = None,
        PinDataLength: int = None
    ) -> VerifyPinDataOutputTypeDef:
        """
        Verifies pin-related data such as PIN and PIN Offset using algorithms including
        VISA PVV and IBM3624.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client.verify_pin_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client.html#verify_pin_data)
        """
