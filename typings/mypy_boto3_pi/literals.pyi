"""
Type annotations for pi service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/literals.html)

Usage::

    ```python
    from mypy_boto3_pi.literals import AcceptLanguageType

    data: AcceptLanguageType = "EN_US"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceptLanguageType",
    "AnalysisStatusType",
    "ContextTypeType",
    "DetailStatusType",
    "FeatureStatusType",
    "FineGrainedActionType",
    "PeriodAlignmentType",
    "ServiceTypeType",
    "SeverityType",
    "TextFormatType",
)

AcceptLanguageType = Literal["EN_US"]
AnalysisStatusType = Literal["FAILED", "RUNNING", "SUCCEEDED"]
ContextTypeType = Literal["CAUSAL", "CONTEXTUAL"]
DetailStatusType = Literal["AVAILABLE", "PROCESSING", "UNAVAILABLE"]
FeatureStatusType = Literal[
    "DISABLED",
    "DISABLED_PENDING_REBOOT",
    "ENABLED",
    "ENABLED_PENDING_REBOOT",
    "UNKNOWN",
    "UNSUPPORTED",
]
FineGrainedActionType = Literal[
    "DescribeDimensionKeys", "GetDimensionKeyDetails", "GetResourceMetrics"
]
PeriodAlignmentType = Literal["END_TIME", "START_TIME"]
ServiceTypeType = Literal["DOCDB", "RDS"]
SeverityType = Literal["HIGH", "LOW", "MEDIUM"]
TextFormatType = Literal["MARKDOWN", "PLAIN_TEXT"]
