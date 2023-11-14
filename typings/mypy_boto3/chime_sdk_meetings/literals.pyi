"""
Type annotations for chime-sdk-meetings service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/literals.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_meetings.literals import MediaCapabilitiesType

    data: MediaCapabilitiesType = "None"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "MediaCapabilitiesType",
    "MeetingFeatureStatusType",
    "TranscribeContentIdentificationTypeType",
    "TranscribeContentRedactionTypeType",
    "TranscribeLanguageCodeType",
    "TranscribeMedicalContentIdentificationTypeType",
    "TranscribeMedicalLanguageCodeType",
    "TranscribeMedicalRegionType",
    "TranscribeMedicalSpecialtyType",
    "TranscribeMedicalTypeType",
    "TranscribePartialResultsStabilityType",
    "TranscribeRegionType",
    "TranscribeVocabularyFilterMethodType",
)

MediaCapabilitiesType = Literal["None", "Receive", "Send", "SendReceive"]
MeetingFeatureStatusType = Literal["AVAILABLE", "UNAVAILABLE"]
TranscribeContentIdentificationTypeType = Literal["PII"]
TranscribeContentRedactionTypeType = Literal["PII"]
TranscribeLanguageCodeType = Literal[
    "de-DE",
    "en-AU",
    "en-GB",
    "en-US",
    "es-US",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "pt-BR",
    "th-TH",
    "zh-CN",
]
TranscribeMedicalContentIdentificationTypeType = Literal["PHI"]
TranscribeMedicalLanguageCodeType = Literal["en-US"]
TranscribeMedicalRegionType = Literal[
    "ap-southeast-2", "auto", "ca-central-1", "eu-west-1", "us-east-1", "us-east-2", "us-west-2"
]
TranscribeMedicalSpecialtyType = Literal[
    "CARDIOLOGY", "NEUROLOGY", "ONCOLOGY", "PRIMARYCARE", "RADIOLOGY", "UROLOGY"
]
TranscribeMedicalTypeType = Literal["CONVERSATION", "DICTATION"]
TranscribePartialResultsStabilityType = Literal["high", "low", "medium"]
TranscribeRegionType = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-2",
    "auto",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-gov-west-1",
    "us-west-2",
]
TranscribeVocabularyFilterMethodType = Literal["mask", "remove", "tag"]
