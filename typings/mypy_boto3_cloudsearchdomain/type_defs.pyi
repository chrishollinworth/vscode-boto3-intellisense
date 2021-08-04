"""
Type annotations for cloudsearchdomain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearchdomain.type_defs import BucketInfoTypeDef

    data: BucketInfoTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import ContentTypeType, QueryParserType

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
    "ResponseMetadataTypeDef",
    "SearchRequestRequestTypeDef",
    "SearchResponseTypeDef",
    "SearchStatusTypeDef",
    "SuggestModelTypeDef",
    "SuggestRequestRequestTypeDef",
    "SuggestResponseTypeDef",
    "SuggestStatusTypeDef",
    "SuggestionMatchTypeDef",
    "UploadDocumentsRequestRequestTypeDef",
    "UploadDocumentsResponseTypeDef",
)

BucketInfoTypeDef = TypedDict(
    "BucketInfoTypeDef",
    {
        "buckets": List["BucketTypeDef"],
    },
    total=False,
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "value": str,
        "count": int,
    },
    total=False,
)

DocumentServiceWarningTypeDef = TypedDict(
    "DocumentServiceWarningTypeDef",
    {
        "message": str,
    },
    total=False,
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
    {
        "found": int,
        "start": int,
        "cursor": str,
        "hit": List["HitTypeDef"],
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSearchRequestRequestTypeDef = TypedDict(
    "_RequiredSearchRequestRequestTypeDef",
    {
        "query": str,
    },
)
_OptionalSearchRequestRequestTypeDef = TypedDict(
    "_OptionalSearchRequestRequestTypeDef",
    {
        "cursor": str,
        "expr": str,
        "facet": str,
        "filterQuery": str,
        "highlight": str,
        "partial": bool,
        "queryOptions": str,
        "queryParser": QueryParserType,
        "returnFields": str,
        "size": int,
        "sort": str,
        "start": int,
        "stats": str,
    },
    total=False,
)

class SearchRequestRequestTypeDef(
    _RequiredSearchRequestRequestTypeDef, _OptionalSearchRequestRequestTypeDef
):
    pass

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef",
    {
        "status": "SearchStatusTypeDef",
        "hits": "HitsTypeDef",
        "facets": Dict[str, "BucketInfoTypeDef"],
        "stats": Dict[str, "FieldStatsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchStatusTypeDef = TypedDict(
    "SearchStatusTypeDef",
    {
        "timems": int,
        "rid": str,
    },
    total=False,
)

SuggestModelTypeDef = TypedDict(
    "SuggestModelTypeDef",
    {
        "query": str,
        "found": int,
        "suggestions": List["SuggestionMatchTypeDef"],
    },
    total=False,
)

_RequiredSuggestRequestRequestTypeDef = TypedDict(
    "_RequiredSuggestRequestRequestTypeDef",
    {
        "query": str,
        "suggester": str,
    },
)
_OptionalSuggestRequestRequestTypeDef = TypedDict(
    "_OptionalSuggestRequestRequestTypeDef",
    {
        "size": int,
    },
    total=False,
)

class SuggestRequestRequestTypeDef(
    _RequiredSuggestRequestRequestTypeDef, _OptionalSuggestRequestRequestTypeDef
):
    pass

SuggestResponseTypeDef = TypedDict(
    "SuggestResponseTypeDef",
    {
        "status": "SuggestStatusTypeDef",
        "suggest": "SuggestModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuggestStatusTypeDef = TypedDict(
    "SuggestStatusTypeDef",
    {
        "timems": int,
        "rid": str,
    },
    total=False,
)

SuggestionMatchTypeDef = TypedDict(
    "SuggestionMatchTypeDef",
    {
        "suggestion": str,
        "score": int,
        "id": str,
    },
    total=False,
)

UploadDocumentsRequestRequestTypeDef = TypedDict(
    "UploadDocumentsRequestRequestTypeDef",
    {
        "documents": Union[bytes, IO[bytes], StreamingBody],
        "contentType": ContentTypeType,
    },
)

UploadDocumentsResponseTypeDef = TypedDict(
    "UploadDocumentsResponseTypeDef",
    {
        "status": str,
        "adds": int,
        "deletes": int,
        "warnings": List["DocumentServiceWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
