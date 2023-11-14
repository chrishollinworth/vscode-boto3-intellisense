"""
Type annotations for cloudsearch service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudsearch.literals import AlgorithmicStemmingType

    data: AlgorithmicStemmingType = "full"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlgorithmicStemmingType",
    "AnalysisSchemeLanguageType",
    "IndexFieldTypeType",
    "OptionStateType",
    "PartitionInstanceTypeType",
    "SuggesterFuzzyMatchingType",
    "TLSSecurityPolicyType",
)

AlgorithmicStemmingType = Literal["full", "light", "minimal", "none"]
AnalysisSchemeLanguageType = Literal[
    "ar",
    "bg",
    "ca",
    "cs",
    "da",
    "de",
    "el",
    "en",
    "es",
    "eu",
    "fa",
    "fi",
    "fr",
    "ga",
    "gl",
    "he",
    "hi",
    "hu",
    "hy",
    "id",
    "it",
    "ja",
    "ko",
    "lv",
    "mul",
    "nl",
    "no",
    "pt",
    "ro",
    "ru",
    "sv",
    "th",
    "tr",
    "zh-Hans",
    "zh-Hant",
]
IndexFieldTypeType = Literal[
    "date",
    "date-array",
    "double",
    "double-array",
    "int",
    "int-array",
    "latlon",
    "literal",
    "literal-array",
    "text",
    "text-array",
]
OptionStateType = Literal["Active", "FailedToValidate", "Processing", "RequiresIndexDocuments"]
PartitionInstanceTypeType = Literal[
    "search.2xlarge",
    "search.large",
    "search.m1.large",
    "search.m1.small",
    "search.m2.2xlarge",
    "search.m2.xlarge",
    "search.m3.2xlarge",
    "search.m3.large",
    "search.m3.medium",
    "search.m3.xlarge",
    "search.medium",
    "search.previousgeneration.2xlarge",
    "search.previousgeneration.large",
    "search.previousgeneration.small",
    "search.previousgeneration.xlarge",
    "search.small",
    "search.xlarge",
]
SuggesterFuzzyMatchingType = Literal["high", "low", "none"]
TLSSecurityPolicyType = Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"]
