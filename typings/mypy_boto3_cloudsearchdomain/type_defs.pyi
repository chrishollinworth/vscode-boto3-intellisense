"""
Type annotations for cloudsearchdomain service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudsearchdomain.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import ContentTypeType, QueryParserType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "BucketInfoTypeDef",
    "BucketTypeDef",
    "DocumentServiceWarningTypeDef",
    "FieldStatsTypeDef",
    "HitTypeDef",
    "HitsTypeDef",
    "ResponseMetadataTypeDef",
    "SearchRequestTypeDef",
    "SearchResponseTypeDef",
    "SearchStatusTypeDef",
    "SuggestModelTypeDef",
    "SuggestRequestTypeDef",
    "SuggestResponseTypeDef",
    "SuggestStatusTypeDef",
    "SuggestionMatchTypeDef",
    "UploadDocumentsRequestTypeDef",
    "UploadDocumentsResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BucketTypeDef(TypedDict):
    value: NotRequired[str]
    count: NotRequired[int]

class DocumentServiceWarningTypeDef(TypedDict):
    message: NotRequired[str]

FieldStatsTypeDef = TypedDict(
    "FieldStatsTypeDef",
    {
        "min": NotRequired[str],
        "max": NotRequired[str],
        "count": NotRequired[int],
        "missing": NotRequired[int],
        "sum": NotRequired[float],
        "sumOfSquares": NotRequired[float],
        "mean": NotRequired[str],
        "stddev": NotRequired[float],
    },
)
HitTypeDef = TypedDict(
    "HitTypeDef",
    {
        "id": NotRequired[str],
        "fields": NotRequired[Dict[str, List[str]]],
        "exprs": NotRequired[Dict[str, str]],
        "highlights": NotRequired[Dict[str, str]],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SearchRequestTypeDef(TypedDict):
    query: str
    cursor: NotRequired[str]
    expr: NotRequired[str]
    facet: NotRequired[str]
    filterQuery: NotRequired[str]
    highlight: NotRequired[str]
    partial: NotRequired[bool]
    queryOptions: NotRequired[str]
    queryParser: NotRequired[QueryParserType]
    returnFields: NotRequired[str]
    size: NotRequired[int]
    sort: NotRequired[str]
    start: NotRequired[int]
    stats: NotRequired[str]

class SearchStatusTypeDef(TypedDict):
    timems: NotRequired[int]
    rid: NotRequired[str]

SuggestionMatchTypeDef = TypedDict(
    "SuggestionMatchTypeDef",
    {
        "suggestion": NotRequired[str],
        "score": NotRequired[int],
        "id": NotRequired[str],
    },
)

class SuggestRequestTypeDef(TypedDict):
    query: str
    suggester: str
    size: NotRequired[int]

class SuggestStatusTypeDef(TypedDict):
    timems: NotRequired[int]
    rid: NotRequired[str]

class UploadDocumentsRequestTypeDef(TypedDict):
    documents: BlobTypeDef
    contentType: ContentTypeType

class BucketInfoTypeDef(TypedDict):
    buckets: NotRequired[List[BucketTypeDef]]

class HitsTypeDef(TypedDict):
    found: NotRequired[int]
    start: NotRequired[int]
    cursor: NotRequired[str]
    hit: NotRequired[List[HitTypeDef]]

class UploadDocumentsResponseTypeDef(TypedDict):
    status: str
    adds: int
    deletes: int
    warnings: List[DocumentServiceWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SuggestModelTypeDef(TypedDict):
    query: NotRequired[str]
    found: NotRequired[int]
    suggestions: NotRequired[List[SuggestionMatchTypeDef]]

class SearchResponseTypeDef(TypedDict):
    status: SearchStatusTypeDef
    hits: HitsTypeDef
    facets: Dict[str, BucketInfoTypeDef]
    stats: Dict[str, FieldStatsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SuggestResponseTypeDef(TypedDict):
    status: SuggestStatusTypeDef
    suggest: SuggestModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
