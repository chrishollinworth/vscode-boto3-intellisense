"""
Type annotations for connect-contact-lens service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connect_contact_lens.type_defs import CategoriesTypeDef

    data: CategoriesTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import SentimentValueType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CategoriesTypeDef",
    "CategoryDetailsTypeDef",
    "CharacterOffsetsTypeDef",
    "IssueDetectedTypeDef",
    "ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    "PointOfInterestTypeDef",
    "RealtimeContactAnalysisSegmentTypeDef",
    "ResponseMetadataTypeDef",
    "TranscriptTypeDef",
)

CategoriesTypeDef = TypedDict(
    "CategoriesTypeDef",
    {
        "MatchedCategories": List[str],
        "MatchedDetails": Dict[str, "CategoryDetailsTypeDef"],
    },
)

CategoryDetailsTypeDef = TypedDict(
    "CategoryDetailsTypeDef",
    {
        "PointsOfInterest": List["PointOfInterestTypeDef"],
    },
)

CharacterOffsetsTypeDef = TypedDict(
    "CharacterOffsetsTypeDef",
    {
        "BeginOffsetChar": int,
        "EndOffsetChar": int,
    },
)

IssueDetectedTypeDef = TypedDict(
    "IssueDetectedTypeDef",
    {
        "CharacterOffsets": "CharacterOffsetsTypeDef",
    },
)

_RequiredListRealtimeContactAnalysisSegmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)
_OptionalListRealtimeContactAnalysisSegmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef(
    _RequiredListRealtimeContactAnalysisSegmentsRequestRequestTypeDef,
    _OptionalListRealtimeContactAnalysisSegmentsRequestRequestTypeDef,
):
    pass

ListRealtimeContactAnalysisSegmentsResponseTypeDef = TypedDict(
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    {
        "Segments": List["RealtimeContactAnalysisSegmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PointOfInterestTypeDef = TypedDict(
    "PointOfInterestTypeDef",
    {
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
    },
)

RealtimeContactAnalysisSegmentTypeDef = TypedDict(
    "RealtimeContactAnalysisSegmentTypeDef",
    {
        "Transcript": "TranscriptTypeDef",
        "Categories": "CategoriesTypeDef",
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

_RequiredTranscriptTypeDef = TypedDict(
    "_RequiredTranscriptTypeDef",
    {
        "Id": str,
        "ParticipantId": str,
        "ParticipantRole": str,
        "Content": str,
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
        "Sentiment": SentimentValueType,
    },
)
_OptionalTranscriptTypeDef = TypedDict(
    "_OptionalTranscriptTypeDef",
    {
        "IssuesDetected": List["IssueDetectedTypeDef"],
    },
    total=False,
)

class TranscriptTypeDef(_RequiredTranscriptTypeDef, _OptionalTranscriptTypeDef):
    pass
