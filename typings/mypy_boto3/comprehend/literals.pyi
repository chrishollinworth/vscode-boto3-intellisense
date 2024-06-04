"""
Type annotations for comprehend service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/literals.html)

Usage::

    ```python
    from mypy_boto3_comprehend.literals import AugmentedManifestsDocumentTypeFormatType

    data: AugmentedManifestsDocumentTypeFormatType = "PLAIN_TEXT_DOCUMENT"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AugmentedManifestsDocumentTypeFormatType",
    "BlockTypeType",
    "DatasetDataFormatType",
    "DatasetStatusType",
    "DatasetTypeType",
    "DocumentClassifierDataFormatType",
    "DocumentClassifierDocumentTypeFormatType",
    "DocumentClassifierModeType",
    "DocumentReadActionType",
    "DocumentReadFeatureTypesType",
    "DocumentReadModeType",
    "DocumentTypeType",
    "EndpointStatusType",
    "EntityRecognizerDataFormatType",
    "EntityTypeType",
    "FlywheelIterationStatusType",
    "FlywheelStatusType",
    "InputFormatType",
    "JobStatusType",
    "LanguageCodeType",
    "ListDocumentClassificationJobsPaginatorName",
    "ListDocumentClassifiersPaginatorName",
    "ListDominantLanguageDetectionJobsPaginatorName",
    "ListEndpointsPaginatorName",
    "ListEntitiesDetectionJobsPaginatorName",
    "ListEntityRecognizersPaginatorName",
    "ListKeyPhrasesDetectionJobsPaginatorName",
    "ListPiiEntitiesDetectionJobsPaginatorName",
    "ListSentimentDetectionJobsPaginatorName",
    "ListTopicsDetectionJobsPaginatorName",
    "ModelStatusType",
    "ModelTypeType",
    "PageBasedErrorCodeType",
    "PageBasedWarningCodeType",
    "PartOfSpeechTagTypeType",
    "PiiEntitiesDetectionMaskModeType",
    "PiiEntitiesDetectionModeType",
    "PiiEntityTypeType",
    "RelationshipTypeType",
    "SentimentTypeType",
    "SplitType",
    "SyntaxLanguageCodeType",
    "TargetedSentimentEntityTypeType",
    "ToxicContentTypeType",
)

AugmentedManifestsDocumentTypeFormatType = Literal[
    "PLAIN_TEXT_DOCUMENT", "SEMI_STRUCTURED_DOCUMENT"
]
BlockTypeType = Literal["LINE", "WORD"]
DatasetDataFormatType = Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]
DatasetStatusType = Literal["COMPLETED", "CREATING", "FAILED"]
DatasetTypeType = Literal["TEST", "TRAIN"]
DocumentClassifierDataFormatType = Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]
DocumentClassifierDocumentTypeFormatType = Literal[
    "PLAIN_TEXT_DOCUMENT", "SEMI_STRUCTURED_DOCUMENT"
]
DocumentClassifierModeType = Literal["MULTI_CLASS", "MULTI_LABEL"]
DocumentReadActionType = Literal["TEXTRACT_ANALYZE_DOCUMENT", "TEXTRACT_DETECT_DOCUMENT_TEXT"]
DocumentReadFeatureTypesType = Literal["FORMS", "TABLES"]
DocumentReadModeType = Literal["FORCE_DOCUMENT_READ_ACTION", "SERVICE_DEFAULT"]
DocumentTypeType = Literal[
    "IMAGE",
    "MS_WORD",
    "NATIVE_PDF",
    "PLAIN_TEXT",
    "SCANNED_PDF",
    "TEXTRACT_ANALYZE_DOCUMENT_JSON",
    "TEXTRACT_DETECT_DOCUMENT_TEXT_JSON",
]
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
FlywheelIterationStatusType = Literal[
    "COMPLETED", "EVALUATING", "FAILED", "STOPPED", "STOP_REQUESTED", "TRAINING"
]
FlywheelStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
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
ListEndpointsPaginatorName = Literal["list_endpoints"]
ListEntitiesDetectionJobsPaginatorName = Literal["list_entities_detection_jobs"]
ListEntityRecognizersPaginatorName = Literal["list_entity_recognizers"]
ListKeyPhrasesDetectionJobsPaginatorName = Literal["list_key_phrases_detection_jobs"]
ListPiiEntitiesDetectionJobsPaginatorName = Literal["list_pii_entities_detection_jobs"]
ListSentimentDetectionJobsPaginatorName = Literal["list_sentiment_detection_jobs"]
ListTopicsDetectionJobsPaginatorName = Literal["list_topics_detection_jobs"]
ModelStatusType = Literal[
    "DELETING",
    "IN_ERROR",
    "STOPPED",
    "STOP_REQUESTED",
    "SUBMITTED",
    "TRAINED",
    "TRAINED_WITH_WARNING",
    "TRAINING",
]
ModelTypeType = Literal["DOCUMENT_CLASSIFIER", "ENTITY_RECOGNIZER"]
PageBasedErrorCodeType = Literal[
    "INTERNAL_SERVER_ERROR",
    "PAGE_CHARACTERS_EXCEEDED",
    "PAGE_SIZE_EXCEEDED",
    "TEXTRACT_BAD_PAGE",
    "TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED",
]
PageBasedWarningCodeType = Literal[
    "INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL",
    "INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL",
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
    "CA_HEALTH_NUMBER",
    "CA_SOCIAL_INSURANCE_NUMBER",
    "CREDIT_DEBIT_CVV",
    "CREDIT_DEBIT_EXPIRY",
    "CREDIT_DEBIT_NUMBER",
    "DATE_TIME",
    "DRIVER_ID",
    "EMAIL",
    "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
    "IN_AADHAAR",
    "IN_NREGA",
    "IN_PERMANENT_ACCOUNT_NUMBER",
    "IN_VOTER_NUMBER",
    "IP_ADDRESS",
    "LICENSE_PLATE",
    "MAC_ADDRESS",
    "NAME",
    "PASSPORT_NUMBER",
    "PASSWORD",
    "PHONE",
    "PIN",
    "SSN",
    "SWIFT_CODE",
    "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
    "UK_NATIONAL_INSURANCE_NUMBER",
    "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
    "URL",
    "USERNAME",
    "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
    "VEHICLE_IDENTIFICATION_NUMBER",
]
RelationshipTypeType = Literal["CHILD"]
SentimentTypeType = Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]
SplitType = Literal["TEST", "TRAIN"]
SyntaxLanguageCodeType = Literal["de", "en", "es", "fr", "it", "pt"]
TargetedSentimentEntityTypeType = Literal[
    "ATTRIBUTE",
    "BOOK",
    "BRAND",
    "COMMERCIAL_ITEM",
    "DATE",
    "EVENT",
    "FACILITY",
    "GAME",
    "LOCATION",
    "MOVIE",
    "MUSIC",
    "ORGANIZATION",
    "OTHER",
    "PERSON",
    "PERSONAL_TITLE",
    "QUANTITY",
    "SOFTWARE",
]
ToxicContentTypeType = Literal[
    "GRAPHIC",
    "HARASSMENT_OR_ABUSE",
    "HATE_SPEECH",
    "INSULT",
    "PROFANITY",
    "SEXUAL",
    "VIOLENCE_OR_THREAT",
]
