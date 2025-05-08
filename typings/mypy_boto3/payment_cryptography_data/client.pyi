"""
Type annotations for payment-cryptography-data service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_payment_cryptography_data.client import PaymentCryptographyDataPlaneClient

    session = Session()
    client: PaymentCryptographyDataPlaneClient = session.client("payment-cryptography-data")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    DecryptDataInputTypeDef,
    DecryptDataOutputTypeDef,
    EncryptDataInputTypeDef,
    EncryptDataOutputTypeDef,
    GenerateCardValidationDataInputTypeDef,
    GenerateCardValidationDataOutputTypeDef,
    GenerateMacEmvPinChangeInputTypeDef,
    GenerateMacEmvPinChangeOutputTypeDef,
    GenerateMacInputTypeDef,
    GenerateMacOutputTypeDef,
    GeneratePinDataInputTypeDef,
    GeneratePinDataOutputTypeDef,
    ReEncryptDataInputTypeDef,
    ReEncryptDataOutputTypeDef,
    TranslatePinDataInputTypeDef,
    TranslatePinDataOutputTypeDef,
    VerifyAuthRequestCryptogramInputTypeDef,
    VerifyAuthRequestCryptogramOutputTypeDef,
    VerifyCardValidationDataInputTypeDef,
    VerifyCardValidationDataOutputTypeDef,
    VerifyMacInputTypeDef,
    VerifyMacOutputTypeDef,
    VerifyPinDataInputTypeDef,
    VerifyPinDataOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("PaymentCryptographyDataPlaneClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]
    VerificationFailedException: Type[BotocoreClientError]

class PaymentCryptographyDataPlaneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PaymentCryptographyDataPlaneClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data.html#PaymentCryptographyDataPlane.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#generate_presigned_url)
        """

    def decrypt_data(self, **kwargs: Unpack[DecryptDataInputTypeDef]) -> DecryptDataOutputTypeDef:
        """
        Decrypts ciphertext data to plaintext using a symmetric (TDES, AES), asymmetric
        (RSA), or derived (DUKPT or EMV) encryption key scheme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/decrypt_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#decrypt_data)
        """

    def encrypt_data(self, **kwargs: Unpack[EncryptDataInputTypeDef]) -> EncryptDataOutputTypeDef:
        """
        Encrypts plaintext data to ciphertext using a symmetric (TDES, AES), asymmetric
        (RSA), or derived (DUKPT or EMV) encryption key scheme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/encrypt_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#encrypt_data)
        """

    def generate_card_validation_data(
        self, **kwargs: Unpack[GenerateCardValidationDataInputTypeDef]
    ) -> GenerateCardValidationDataOutputTypeDef:
        """
        Generates card-related validation data using algorithms such as Card
        Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2),
        or Card Security Codes (CSC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/generate_card_validation_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#generate_card_validation_data)
        """

    def generate_mac(self, **kwargs: Unpack[GenerateMacInputTypeDef]) -> GenerateMacOutputTypeDef:
        """
        Generates a Message Authentication Code (MAC) cryptogram within Amazon Web
        Services Payment Cryptography.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/generate_mac.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#generate_mac)
        """

    def generate_mac_emv_pin_change(
        self, **kwargs: Unpack[GenerateMacEmvPinChangeInputTypeDef]
    ) -> GenerateMacEmvPinChangeOutputTypeDef:
        """
        Generates an issuer script mac for EMV payment cards that use offline PINs as
        the cardholder verification method (CVM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/generate_mac_emv_pin_change.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#generate_mac_emv_pin_change)
        """

    def generate_pin_data(
        self, **kwargs: Unpack[GeneratePinDataInputTypeDef]
    ) -> GeneratePinDataOutputTypeDef:
        """
        Generates pin-related data such as PIN, PIN Verification Value (PVV), PIN
        Block, and PIN Offset during new card issuance or reissuance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/generate_pin_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#generate_pin_data)
        """

    def re_encrypt_data(
        self, **kwargs: Unpack[ReEncryptDataInputTypeDef]
    ) -> ReEncryptDataOutputTypeDef:
        """
        Re-encrypt ciphertext using DUKPT or Symmetric data encryption keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/re_encrypt_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#re_encrypt_data)
        """

    def translate_pin_data(
        self, **kwargs: Unpack[TranslatePinDataInputTypeDef]
    ) -> TranslatePinDataOutputTypeDef:
        """
        Translates encrypted PIN block from and to ISO 9564 formats 0,1,3,4.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/translate_pin_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#translate_pin_data)
        """

    def verify_auth_request_cryptogram(
        self, **kwargs: Unpack[VerifyAuthRequestCryptogramInputTypeDef]
    ) -> VerifyAuthRequestCryptogramOutputTypeDef:
        """
        Verifies Authorization Request Cryptogram (ARQC) for a EMV chip payment card
        authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/verify_auth_request_cryptogram.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#verify_auth_request_cryptogram)
        """

    def verify_card_validation_data(
        self, **kwargs: Unpack[VerifyCardValidationDataInputTypeDef]
    ) -> VerifyCardValidationDataOutputTypeDef:
        """
        Verifies card-related validation data using algorithms such as Card
        Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2)
        and Card Security Codes (CSC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/verify_card_validation_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#verify_card_validation_data)
        """

    def verify_mac(self, **kwargs: Unpack[VerifyMacInputTypeDef]) -> VerifyMacOutputTypeDef:
        """
        Verifies a Message Authentication Code (MAC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/verify_mac.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#verify_mac)
        """

    def verify_pin_data(
        self, **kwargs: Unpack[VerifyPinDataInputTypeDef]
    ) -> VerifyPinDataOutputTypeDef:
        """
        Verifies pin-related data such as PIN and PIN Offset using algorithms including
        VISA PVV and IBM3624.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography-data/client/verify_pin_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/client/#verify_pin_data)
        """
