"""
Type annotations for payment-cryptography service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/literals.html)

Usage::

    ```python
    from mypy_boto3_payment_cryptography.literals import KeyAlgorithmType

    data: KeyAlgorithmType = "AES_128"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "KeyAlgorithmType",
    "KeyCheckValueAlgorithmType",
    "KeyClassType",
    "KeyMaterialTypeType",
    "KeyOriginType",
    "KeyStateType",
    "KeyUsageType",
    "ListAliasesPaginatorName",
    "ListKeysPaginatorName",
    "ListTagsForResourcePaginatorName",
    "Tr34KeyBlockFormatType",
    "WrappedKeyMaterialFormatType",
)

KeyAlgorithmType = Literal[
    "AES_128", "AES_192", "AES_256", "RSA_2048", "RSA_3072", "RSA_4096", "TDES_2KEY", "TDES_3KEY"
]
KeyCheckValueAlgorithmType = Literal["ANSI_X9_24", "CMAC"]
KeyClassType = Literal["ASYMMETRIC_KEY_PAIR", "PRIVATE_KEY", "PUBLIC_KEY", "SYMMETRIC_KEY"]
KeyMaterialTypeType = Literal[
    "ROOT_PUBLIC_KEY_CERTIFICATE",
    "TR31_KEY_BLOCK",
    "TR34_KEY_BLOCK",
    "TRUSTED_PUBLIC_KEY_CERTIFICATE",
]
KeyOriginType = Literal["AWS_PAYMENT_CRYPTOGRAPHY", "EXTERNAL"]
KeyStateType = Literal["CREATE_COMPLETE", "CREATE_IN_PROGRESS", "DELETE_COMPLETE", "DELETE_PENDING"]
KeyUsageType = Literal[
    "TR31_B0_BASE_DERIVATION_KEY",
    "TR31_C0_CARD_VERIFICATION_KEY",
    "TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY",
    "TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION",
    "TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS",
    "TR31_E1_EMV_MKEY_CONFIDENTIALITY",
    "TR31_E2_EMV_MKEY_INTEGRITY",
    "TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS",
    "TR31_E5_EMV_MKEY_CARD_PERSONALIZATION",
    "TR31_E6_EMV_MKEY_OTHER",
    "TR31_K0_KEY_ENCRYPTION_KEY",
    "TR31_K1_KEY_BLOCK_PROTECTION_KEY",
    "TR31_K2_TR34_ASYMMETRIC_KEY",
    "TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT",
    "TR31_M3_ISO_9797_3_MAC_KEY",
    "TR31_M6_ISO_9797_5_CMAC_KEY",
    "TR31_M7_HMAC_KEY",
    "TR31_P0_PIN_ENCRYPTION_KEY",
    "TR31_P1_PIN_GENERATION_KEY",
    "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
    "TR31_V1_IBM3624_PIN_VERIFICATION_KEY",
    "TR31_V2_VISA_PIN_VERIFICATION_KEY",
]
ListAliasesPaginatorName = Literal["list_aliases"]
ListKeysPaginatorName = Literal["list_keys"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
Tr34KeyBlockFormatType = Literal["X9_TR34_2012"]
WrappedKeyMaterialFormatType = Literal["KEY_CRYPTOGRAM", "TR31_KEY_BLOCK", "TR34_KEY_BLOCK"]
