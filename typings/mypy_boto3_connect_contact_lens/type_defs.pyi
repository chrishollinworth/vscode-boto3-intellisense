"""
Main interface for connect-contact-lens service type definitions.

Usage::

    ```python
    from mypy_boto3_connect_contact_lens.type_defs import CategoriesTypeDef

    data: CategoriesTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CategoriesTypeDef",
    "CategoryDetailsTypeDef",
    "CharacterOffsetsTypeDef",
    "IssueDetectedTypeDef",
    "PointOfInterestTypeDef",
    "RealtimeContactAnalysisSegmentTypeDef",
    "TranscriptTypeDef",
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
)

CategoriesTypeDef = TypedDict(
    "CategoriesTypeDef",
    {"MatchedCategories": List[str], "MatchedDetails": Dict[str, "CategoryDetailsTypeDef"]},
)

CategoryDetailsTypeDef = TypedDict(
    "CategoryDetailsTypeDef", {"PointsOfInterest": List["PointOfInterestTypeDef"]}
)

CharacterOffsetsTypeDef = TypedDict(
    "CharacterOffsetsTypeDef", {"BeginOffsetChar": int, "EndOffsetChar": int}
)

IssueDetectedTypeDef = TypedDict(
    "IssueDetectedTypeDef", {"CharacterOffsets": "CharacterOffsetsTypeDef"}
)

PointOfInterestTypeDef = TypedDict(
    "PointOfInterestTypeDef", {"BeginOffsetMillis": int, "EndOffsetMillis": int}
)

RealtimeContactAnalysisSegmentTypeDef = TypedDict(
    "RealtimeContactAnalysisSegmentTypeDef",
    {"Transcript": "TranscriptTypeDef", "Categories": "CategoriesTypeDef"},
    total=False,
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
        "Sentiment": Literal["POSITIVE", "NEUTRAL", "NEGATIVE"],
    },
)
_OptionalTranscriptTypeDef = TypedDict(
    "_OptionalTranscriptTypeDef", {"IssuesDetected": List["IssueDetectedTypeDef"]}, total=False
)


class TranscriptTypeDef(_RequiredTranscriptTypeDef, _OptionalTranscriptTypeDef):
    pass


_RequiredListRealtimeContactAnalysisSegmentsResponseTypeDef = TypedDict(
    "_RequiredListRealtimeContactAnalysisSegmentsResponseTypeDef",
    {"Segments": List["RealtimeContactAnalysisSegmentTypeDef"]},
)
_OptionalListRealtimeContactAnalysisSegmentsResponseTypeDef = TypedDict(
    "_OptionalListRealtimeContactAnalysisSegmentsResponseTypeDef", {"NextToken": str}, total=False
)


class ListRealtimeContactAnalysisSegmentsResponseTypeDef(
    _RequiredListRealtimeContactAnalysisSegmentsResponseTypeDef,
    _OptionalListRealtimeContactAnalysisSegmentsResponseTypeDef,
):
    pass
