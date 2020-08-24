"""
Main interface for cloudsearchdomain service type definitions.

Usage::

    ```python
    from mypy_boto3_cloudsearchdomain.type_defs import BucketInfoTypeDef

    data: BucketInfoTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BucketInfoTypeDef",
    "BucketTypeDef",
    "DocumentServiceWarningTypeDef",
    "FieldStatsTypeDef",
    "HitTypeDef",
    "HitsTypeDef",
    "SearchStatusTypeDef",
    "SuggestModelTypeDef",
    "SuggestStatusTypeDef",
    "SuggestionMatchTypeDef",
    "SearchResponseTypeDef",
    "SuggestResponseTypeDef",
    "UploadDocumentsResponseTypeDef",
)

BucketInfoTypeDef = TypedDict("BucketInfoTypeDef", {"buckets": List["BucketTypeDef"]}, total=False)

BucketTypeDef = TypedDict("BucketTypeDef", {"value": str, "count": int}, total=False)

DocumentServiceWarningTypeDef = TypedDict(
    "DocumentServiceWarningTypeDef", {"message": str}, total=False
)

FieldStatsTypeDef = TypedDict(
    "FieldStatsTypeDef",
    {
        "min": str,
        "max": str,
        "count": int,
        "missing": int,
        "sum": float,
        "sumOfSquares": float,
        "mean": str,
        "stddev": float,
    },
    total=False,
)

HitTypeDef = TypedDict(
    "HitTypeDef",
    {
        "id": str,
        "fields": Dict[str, List[str]],
        "exprs": Dict[str, str],
        "highlights": Dict[str, str],
    },
    total=False,
)

HitsTypeDef = TypedDict(
    "HitsTypeDef",
    {"found": int, "start": int, "cursor": str, "hit": List["HitTypeDef"]},
    total=False,
)

SearchStatusTypeDef = TypedDict("SearchStatusTypeDef", {"timems": int, "rid": str}, total=False)

SuggestModelTypeDef = TypedDict(
    "SuggestModelTypeDef",
    {"query": str, "found": int, "suggestions": List["SuggestionMatchTypeDef"]},
    total=False,
)

SuggestStatusTypeDef = TypedDict("SuggestStatusTypeDef", {"timems": int, "rid": str}, total=False)

SuggestionMatchTypeDef = TypedDict(
    "SuggestionMatchTypeDef", {"suggestion": str, "score": int, "id": str}, total=False
)

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef",
    {
        "status": "SearchStatusTypeDef",
        "hits": "HitsTypeDef",
        "facets": Dict[str, "BucketInfoTypeDef"],
        "stats": Dict[str, "FieldStatsTypeDef"],
    },
    total=False,
)

SuggestResponseTypeDef = TypedDict(
    "SuggestResponseTypeDef",
    {"status": "SuggestStatusTypeDef", "suggest": "SuggestModelTypeDef"},
    total=False,
)

UploadDocumentsResponseTypeDef = TypedDict(
    "UploadDocumentsResponseTypeDef",
    {"status": str, "adds": int, "deletes": int, "warnings": List["DocumentServiceWarningTypeDef"]},
    total=False,
)
