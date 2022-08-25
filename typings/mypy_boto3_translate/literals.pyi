"""
Type annotations for translate service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/literals.html)

Usage::

    ```python
    from mypy_boto3_translate.literals import DirectionalityType

    data: DirectionalityType = "MULTI"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DirectionalityType",
    "DisplayLanguageCodeType",
    "EncryptionKeyTypeType",
    "FormalityType",
    "JobStatusType",
    "ListTerminologiesPaginatorName",
    "MergeStrategyType",
    "ParallelDataFormatType",
    "ParallelDataStatusType",
    "ProfanityType",
    "TerminologyDataFormatType",
)

DirectionalityType = Literal["MULTI", "UNI"]
DisplayLanguageCodeType = Literal["de", "en", "es", "fr", "it", "ja", "ko", "pt", "zh", "zh-TW"]
EncryptionKeyTypeType = Literal["KMS"]
FormalityType = Literal["FORMAL", "INFORMAL"]
JobStatusType = Literal[
    "COMPLETED",
    "COMPLETED_WITH_ERROR",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
    "STOP_REQUESTED",
    "SUBMITTED",
]
ListTerminologiesPaginatorName = Literal["list_terminologies"]
MergeStrategyType = Literal["OVERWRITE"]
ParallelDataFormatType = Literal["CSV", "TMX", "TSV"]
ParallelDataStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
ProfanityType = Literal["MASK"]
TerminologyDataFormatType = Literal["CSV", "TMX", "TSV"]
