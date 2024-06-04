"""
Type annotations for transcribe service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/literals.html)

Usage::

    ```python
    from mypy_boto3_transcribe.literals import BaseModelNameType

    data: BaseModelNameType = "NarrowBand"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BaseModelNameType",
    "CLMLanguageCodeType",
    "CallAnalyticsFeatureType",
    "CallAnalyticsJobStatusType",
    "CallAnalyticsSkippedReasonCodeType",
    "InputTypeType",
    "LanguageCodeType",
    "MediaFormatType",
    "MedicalContentIdentificationTypeType",
    "MedicalScribeJobStatusType",
    "MedicalScribeLanguageCodeType",
    "MedicalScribeParticipantRoleType",
    "ModelStatusType",
    "OutputLocationTypeType",
    "ParticipantRoleType",
    "PiiEntityTypeType",
    "RedactionOutputType",
    "RedactionTypeType",
    "SentimentValueType",
    "SpecialtyType",
    "SubtitleFormatType",
    "ToxicityCategoryType",
    "TranscriptFilterTypeType",
    "TranscriptionJobStatusType",
    "TypeType",
    "VocabularyFilterMethodType",
    "VocabularyStateType",
)

BaseModelNameType = Literal["NarrowBand", "WideBand"]
CLMLanguageCodeType = Literal["de-DE", "en-AU", "en-GB", "en-US", "es-US", "hi-IN", "ja-JP"]
CallAnalyticsFeatureType = Literal["GENERATIVE_SUMMARIZATION"]
CallAnalyticsJobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
CallAnalyticsSkippedReasonCodeType = Literal[
    "FAILED_SAFETY_GUIDELINES", "INSUFFICIENT_CONVERSATION_CONTENT"
]
InputTypeType = Literal["POST_CALL", "REAL_TIME"]
LanguageCodeType = Literal[
    "ab-GE",
    "af-ZA",
    "ar-AE",
    "ar-SA",
    "ast-ES",
    "az-AZ",
    "ba-RU",
    "be-BY",
    "bg-BG",
    "bn-IN",
    "bs-BA",
    "ca-ES",
    "ckb-IQ",
    "ckb-IR",
    "cs-CZ",
    "cy-WL",
    "da-DK",
    "de-CH",
    "de-DE",
    "el-GR",
    "en-AB",
    "en-AU",
    "en-GB",
    "en-IE",
    "en-IN",
    "en-NZ",
    "en-US",
    "en-WL",
    "en-ZA",
    "es-ES",
    "es-US",
    "et-ET",
    "eu-ES",
    "fa-IR",
    "fi-FI",
    "fr-CA",
    "fr-FR",
    "gl-ES",
    "gu-IN",
    "ha-NG",
    "he-IL",
    "hi-IN",
    "hr-HR",
    "hu-HU",
    "hy-AM",
    "id-ID",
    "is-IS",
    "it-IT",
    "ja-JP",
    "ka-GE",
    "kab-DZ",
    "kk-KZ",
    "kn-IN",
    "ko-KR",
    "ky-KG",
    "lg-IN",
    "lt-LT",
    "lv-LV",
    "mhr-RU",
    "mi-NZ",
    "mk-MK",
    "ml-IN",
    "mn-MN",
    "mr-IN",
    "ms-MY",
    "mt-MT",
    "nl-NL",
    "no-NO",
    "or-IN",
    "pa-IN",
    "pl-PL",
    "ps-AF",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "rw-RW",
    "si-LK",
    "sk-SK",
    "sl-SI",
    "so-SO",
    "sr-RS",
    "su-ID",
    "sv-SE",
    "sw-BI",
    "sw-KE",
    "sw-RW",
    "sw-TZ",
    "sw-UG",
    "ta-IN",
    "te-IN",
    "th-TH",
    "tl-PH",
    "tr-TR",
    "tt-RU",
    "ug-CN",
    "uk-UA",
    "uz-UZ",
    "vi-VN",
    "wo-SN",
    "zh-CN",
    "zh-TW",
    "zu-ZA",
]
MediaFormatType = Literal["amr", "flac", "m4a", "mp3", "mp4", "ogg", "wav", "webm"]
MedicalContentIdentificationTypeType = Literal["PHI"]
MedicalScribeJobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
MedicalScribeLanguageCodeType = Literal["en-US"]
MedicalScribeParticipantRoleType = Literal["CLINICIAN", "PATIENT"]
ModelStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
OutputLocationTypeType = Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"]
ParticipantRoleType = Literal["AGENT", "CUSTOMER"]
PiiEntityTypeType = Literal[
    "ADDRESS",
    "ALL",
    "BANK_ACCOUNT_NUMBER",
    "BANK_ROUTING",
    "CREDIT_DEBIT_CVV",
    "CREDIT_DEBIT_EXPIRY",
    "CREDIT_DEBIT_NUMBER",
    "EMAIL",
    "NAME",
    "PHONE",
    "PIN",
    "SSN",
]
RedactionOutputType = Literal["redacted", "redacted_and_unredacted"]
RedactionTypeType = Literal["PII"]
SentimentValueType = Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]
SpecialtyType = Literal["PRIMARYCARE"]
SubtitleFormatType = Literal["srt", "vtt"]
ToxicityCategoryType = Literal["ALL"]
TranscriptFilterTypeType = Literal["EXACT"]
TranscriptionJobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
TypeType = Literal["CONVERSATION", "DICTATION"]
VocabularyFilterMethodType = Literal["mask", "remove", "tag"]
VocabularyStateType = Literal["FAILED", "PENDING", "READY"]
