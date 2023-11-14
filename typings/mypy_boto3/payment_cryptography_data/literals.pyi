"""
Type annotations for payment-cryptography-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography_data/literals.html)

Usage::

    ```python
    from mypy_boto3_payment_cryptography_data.literals import DukptDerivationTypeType

    data: DukptDerivationTypeType = "AES_128"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DukptDerivationTypeType",
    "DukptEncryptionModeType",
    "DukptKeyVariantType",
    "EncryptionModeType",
    "MacAlgorithmType",
    "MajorKeyDerivationModeType",
    "PaddingTypeType",
    "PinBlockFormatForPinDataType",
    "SessionKeyDerivationModeType",
)

DukptDerivationTypeType = Literal["AES_128", "AES_192", "AES_256", "TDES_2KEY", "TDES_3KEY"]
DukptEncryptionModeType = Literal["CBC", "ECB"]
DukptKeyVariantType = Literal["BIDIRECTIONAL", "REQUEST", "RESPONSE"]
EncryptionModeType = Literal["CBC", "CFB", "CFB1", "CFB128", "CFB64", "CFB8", "ECB", "OFB"]
MacAlgorithmType = Literal[
    "CMAC",
    "HMAC_SHA224",
    "HMAC_SHA256",
    "HMAC_SHA384",
    "HMAC_SHA512",
    "ISO9797_ALGORITHM1",
    "ISO9797_ALGORITHM3",
]
MajorKeyDerivationModeType = Literal["EMV_OPTION_A", "EMV_OPTION_B"]
PaddingTypeType = Literal["OAEP_SHA1", "OAEP_SHA256", "OAEP_SHA512", "PKCS1"]
PinBlockFormatForPinDataType = Literal["ISO_FORMAT_0", "ISO_FORMAT_3"]
SessionKeyDerivationModeType = Literal[
    "AMEX", "EMV2000", "EMV_COMMON_SESSION_KEY", "MASTERCARD_SESSION_KEY", "VISA"
]
