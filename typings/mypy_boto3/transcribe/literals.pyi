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
    "CallAnalyticsJobStatusType",
    "LanguageCodeType",
    "MediaFormatType",
    "MedicalContentIdentificationTypeType",
    "ModelStatusType",
    "OutputLocationTypeType",
    "ParticipantRoleType",
    "RedactionOutputType",
    "RedactionTypeType",
    "SentimentValueType",
    "SpecialtyType",
    "SubtitleFormatType",
    "TranscriptFilterTypeType",
    "TranscriptionJobStatusType",
    "TypeType",
    "VocabularyFilterMethodType",
    "VocabularyStateType",
)

BaseModelNameType = Literal["NarrowBand", "WideBand"]
CLMLanguageCodeType = Literal["en-AU", "en-GB", "en-US", "es-US", "hi-IN"]
CallAnalyticsJobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
LanguageCodeType = Literal[
    "af-ZA",
    "ar-AE",
    "ar-SA",
    "cy-GB",
    "da-DK",
    "de-CH",
    "de-DE",
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
    "fa-IR",
    "fr-CA",
    "fr-FR",
    "ga-IE",
    "gd-GB",
    "he-IL",
    "hi-IN",
    "id-ID",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "ms-MY",
    "nl-NL",
    "pt-BR",
    "pt-PT",
    "ru-RU",
    "ta-IN",
    "te-IN",
    "th-TH",
    "tr-TR",
    "zh-CN",
    "zh-TW",
]
MediaFormatType = Literal["amr", "flac", "mp3", "mp4", "ogg", "wav", "webm"]
MedicalContentIdentificationTypeType = Literal["PHI"]
ModelStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
OutputLocationTypeType = Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"]
ParticipantRoleType = Literal["AGENT", "CUSTOMER"]
RedactionOutputType = Literal["redacted", "redacted_and_unredacted"]
RedactionTypeType = Literal["PII"]
SentimentValueType = Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]
SpecialtyType = Literal["PRIMARYCARE"]
SubtitleFormatType = Literal["srt", "vtt"]
TranscriptFilterTypeType = Literal["EXACT"]
TranscriptionJobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
TypeType = Literal["CONVERSATION", "DICTATION"]
VocabularyFilterMethodType = Literal["mask", "remove", "tag"]
VocabularyStateType = Literal["FAILED", "PENDING", "READY"]
