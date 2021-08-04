"""
Type annotations for sns service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/literals.html)

Usage::

    ```python
    from mypy_boto3_sns.literals import LanguageCodeStringType

    data: LanguageCodeStringType = "de-DE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "LanguageCodeStringType",
    "ListEndpointsByPlatformApplicationPaginatorName",
    "ListOriginationNumbersPaginatorName",
    "ListPhoneNumbersOptedOutPaginatorName",
    "ListPlatformApplicationsPaginatorName",
    "ListSMSSandboxPhoneNumbersPaginatorName",
    "ListSubscriptionsByTopicPaginatorName",
    "ListSubscriptionsPaginatorName",
    "ListTopicsPaginatorName",
    "NumberCapabilityType",
    "RouteTypeType",
    "SMSSandboxPhoneNumberVerificationStatusType",
)

LanguageCodeStringType = Literal[
    "de-DE",
    "en-GB",
    "en-US",
    "es-419",
    "es-ES",
    "fr-CA",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "kr-KR",
    "pt-BR",
    "zh-CN",
    "zh-TW",
]
ListEndpointsByPlatformApplicationPaginatorName = Literal["list_endpoints_by_platform_application"]
ListOriginationNumbersPaginatorName = Literal["list_origination_numbers"]
ListPhoneNumbersOptedOutPaginatorName = Literal["list_phone_numbers_opted_out"]
ListPlatformApplicationsPaginatorName = Literal["list_platform_applications"]
ListSMSSandboxPhoneNumbersPaginatorName = Literal["list_sms_sandbox_phone_numbers"]
ListSubscriptionsByTopicPaginatorName = Literal["list_subscriptions_by_topic"]
ListSubscriptionsPaginatorName = Literal["list_subscriptions"]
ListTopicsPaginatorName = Literal["list_topics"]
NumberCapabilityType = Literal["MMS", "SMS", "VOICE"]
RouteTypeType = Literal["Premium", "Promotional", "Transactional"]
SMSSandboxPhoneNumberVerificationStatusType = Literal["Pending", "Verified"]
