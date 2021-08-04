"""
Type annotations for comprehend service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/literals.html)

Usage::

    ```python
    from mypy_boto3_comprehend.literals import DocumentClassifierDataFormatType

    data: DocumentClassifierDataFormatType = "AUGMENTED_MANIFEST"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DocumentClassifierDataFormatType",
    "DocumentClassifierModeType",
    "EndpointStatusType",
    "EntityRecognizerDataFormatType",
    "EntityTypeType",
    "InputFormatType",
    "JobStatusType",
    "LanguageCodeType",
    "ListDocumentClassificationJobsPaginatorName",
    "ListDocumentClassifiersPaginatorName",
    "ListDominantLanguageDetectionJobsPaginatorName",
    "ListEntitiesDetectionJobsPaginatorName",
    "ListEntityRecognizersPaginatorName",
    "ListKeyPhrasesDetectionJobsPaginatorName",
    "ListSentimentDetectionJobsPaginatorName",
    "ListTopicsDetectionJobsPaginatorName",
    "ModelStatusType",
    "PartOfSpeechTagTypeType",
    "PiiEntitiesDetectionMaskModeType",
    "PiiEntitiesDetectionModeType",
    "PiiEntityTypeType",
    "SentimentTypeType",
    "SyntaxLanguageCodeType",
)

DocumentClassifierDataFormatType = Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]
DocumentClassifierModeType = Literal["MULTI_CLASS", "MULTI_LABEL"]
EndpointStatusType = Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"]
EntityRecognizerDataFormatType = Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]
EntityTypeType = Literal[
    "COMMERCIAL_ITEM",
    "DATE",
    "EVENT",
    "LOCATION",
    "ORGANIZATION",
    "OTHER",
    "PERSON",
    "QUANTITY",
    "TITLE",
]
InputFormatType = Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]
JobStatusType = Literal[
    "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
]
LanguageCodeType = Literal[
    "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
]
ListDocumentClassificationJobsPaginatorName = Literal["list_document_classification_jobs"]
ListDocumentClassifiersPaginatorName = Literal["list_document_classifiers"]
ListDominantLanguageDetectionJobsPaginatorName = Literal["list_dominant_language_detection_jobs"]
ListEntitiesDetectionJobsPaginatorName = Literal["list_entities_detection_jobs"]
ListEntityRecognizersPaginatorName = Literal["list_entity_recognizers"]
ListKeyPhrasesDetectionJobsPaginatorName = Literal["list_key_phrases_detection_jobs"]
ListSentimentDetectionJobsPaginatorName = Literal["list_sentiment_detection_jobs"]
ListTopicsDetectionJobsPaginatorName = Literal["list_topics_detection_jobs"]
ModelStatusType = Literal[
    "DELETING", "IN_ERROR", "STOPPED", "STOP_REQUESTED", "SUBMITTED", "TRAINED", "TRAINING"
]
PartOfSpeechTagTypeType = Literal[
    "ADJ",
    "ADP",
    "ADV",
    "AUX",
    "CCONJ",
    "CONJ",
    "DET",
    "INTJ",
    "NOUN",
    "NUM",
    "O",
    "PART",
    "PRON",
    "PROPN",
    "PUNCT",
    "SCONJ",
    "SYM",
    "VERB",
]
PiiEntitiesDetectionMaskModeType = Literal["MASK", "REPLACE_WITH_PII_ENTITY_TYPE"]
PiiEntitiesDetectionModeType = Literal["ONLY_OFFSETS", "ONLY_REDACTION"]
PiiEntityTypeType = Literal[
    "ADDRESS",
    "AGE",
    "ALL",
    "AWS_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "BANK_ACCOUNT_NUMBER",
    "BANK_ROUTING",
    "CREDIT_DEBIT_CVV",
    "CREDIT_DEBIT_EXPIRY",
    "CREDIT_DEBIT_NUMBER",
    "DATE_TIME",
    "DRIVER_ID",
    "EMAIL",
    "IP_ADDRESS",
    "MAC_ADDRESS",
    "NAME",
    "PASSPORT_NUMBER",
    "PASSWORD",
    "PHONE",
    "PIN",
    "SSN",
    "URL",
    "USERNAME",
]
SentimentTypeType = Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]
SyntaxLanguageCodeType = Literal["de", "en", "es", "fr", "it", "pt"]
