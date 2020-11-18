"""
Main interface for ivs service type definitions.

Usage::

    ```python
    from mypy_boto3_ivs.type_defs import BatchErrorTypeDef

    data: BatchErrorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
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
    "BatchErrorTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "PlaybackKeyPairSummaryTypeDef",
    "PlaybackKeyPairTypeDef",
    "StreamKeySummaryTypeDef",
    "StreamKeyTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "BatchGetChannelResponseTypeDef",
    "BatchGetStreamKeyResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateStreamKeyResponseTypeDef",
    "GetChannelResponseTypeDef",
    "GetPlaybackKeyPairResponseTypeDef",
    "GetStreamKeyResponseTypeDef",
    "GetStreamResponseTypeDef",
    "ImportPlaybackKeyPairResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "ListPlaybackKeyPairsResponseTypeDef",
    "ListStreamKeysResponseTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateChannelResponseTypeDef",
)

BatchErrorTypeDef = TypedDict(
    "BatchErrorTypeDef", {"arn": str, "code": str, "message": str}, total=False
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "latencyMode": Literal["NORMAL", "LOW"],
        "authorized": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "arn": str,
        "name": str,
        "latencyMode": Literal["NORMAL", "LOW"],
        "type": Literal["BASIC", "STANDARD"],
        "ingestEndpoint": str,
        "playbackUrl": str,
        "authorized": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

PlaybackKeyPairSummaryTypeDef = TypedDict(
    "PlaybackKeyPairSummaryTypeDef", {"arn": str, "name": str, "tags": Dict[str, str]}, total=False
)

PlaybackKeyPairTypeDef = TypedDict(
    "PlaybackKeyPairTypeDef",
    {"arn": str, "name": str, "fingerprint": str, "tags": Dict[str, str]},
    total=False,
)

StreamKeySummaryTypeDef = TypedDict(
    "StreamKeySummaryTypeDef", {"arn": str, "channelArn": str, "tags": Dict[str, str]}, total=False
)

StreamKeyTypeDef = TypedDict(
    "StreamKeyTypeDef",
    {"arn": str, "value": str, "channelArn": str, "tags": Dict[str, str]},
    total=False,
)

StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "channelArn": str,
        "state": Literal["LIVE", "OFFLINE"],
        "health": Literal["HEALTHY", "STARVING", "UNKNOWN"],
        "viewerCount": int,
        "startTime": datetime,
    },
    total=False,
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "channelArn": str,
        "playbackUrl": str,
        "startTime": datetime,
        "state": Literal["LIVE", "OFFLINE"],
        "health": Literal["HEALTHY", "STARVING", "UNKNOWN"],
        "viewerCount": int,
    },
    total=False,
)

BatchGetChannelResponseTypeDef = TypedDict(
    "BatchGetChannelResponseTypeDef",
    {"channels": List["ChannelTypeDef"], "errors": List["BatchErrorTypeDef"]},
    total=False,
)

BatchGetStreamKeyResponseTypeDef = TypedDict(
    "BatchGetStreamKeyResponseTypeDef",
    {"streamKeys": List["StreamKeyTypeDef"], "errors": List["BatchErrorTypeDef"]},
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {"channel": "ChannelTypeDef", "streamKey": "StreamKeyTypeDef"},
    total=False,
)

CreateStreamKeyResponseTypeDef = TypedDict(
    "CreateStreamKeyResponseTypeDef", {"streamKey": "StreamKeyTypeDef"}, total=False
)

GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef", {"channel": "ChannelTypeDef"}, total=False
)

GetPlaybackKeyPairResponseTypeDef = TypedDict(
    "GetPlaybackKeyPairResponseTypeDef", {"keyPair": "PlaybackKeyPairTypeDef"}, total=False
)

GetStreamKeyResponseTypeDef = TypedDict(
    "GetStreamKeyResponseTypeDef", {"streamKey": "StreamKeyTypeDef"}, total=False
)

GetStreamResponseTypeDef = TypedDict(
    "GetStreamResponseTypeDef", {"stream": "StreamTypeDef"}, total=False
)

ImportPlaybackKeyPairResponseTypeDef = TypedDict(
    "ImportPlaybackKeyPairResponseTypeDef", {"keyPair": "PlaybackKeyPairTypeDef"}, total=False
)

_RequiredListChannelsResponseTypeDef = TypedDict(
    "_RequiredListChannelsResponseTypeDef", {"channels": List["ChannelSummaryTypeDef"]}
)
_OptionalListChannelsResponseTypeDef = TypedDict(
    "_OptionalListChannelsResponseTypeDef", {"nextToken": str}, total=False
)


class ListChannelsResponseTypeDef(
    _RequiredListChannelsResponseTypeDef, _OptionalListChannelsResponseTypeDef
):
    pass


_RequiredListPlaybackKeyPairsResponseTypeDef = TypedDict(
    "_RequiredListPlaybackKeyPairsResponseTypeDef",
    {"keyPairs": List["PlaybackKeyPairSummaryTypeDef"]},
)
_OptionalListPlaybackKeyPairsResponseTypeDef = TypedDict(
    "_OptionalListPlaybackKeyPairsResponseTypeDef", {"nextToken": str}, total=False
)


class ListPlaybackKeyPairsResponseTypeDef(
    _RequiredListPlaybackKeyPairsResponseTypeDef, _OptionalListPlaybackKeyPairsResponseTypeDef
):
    pass


_RequiredListStreamKeysResponseTypeDef = TypedDict(
    "_RequiredListStreamKeysResponseTypeDef", {"streamKeys": List["StreamKeySummaryTypeDef"]}
)
_OptionalListStreamKeysResponseTypeDef = TypedDict(
    "_OptionalListStreamKeysResponseTypeDef", {"nextToken": str}, total=False
)


class ListStreamKeysResponseTypeDef(
    _RequiredListStreamKeysResponseTypeDef, _OptionalListStreamKeysResponseTypeDef
):
    pass


_RequiredListStreamsResponseTypeDef = TypedDict(
    "_RequiredListStreamsResponseTypeDef", {"streams": List["StreamSummaryTypeDef"]}
)
_OptionalListStreamsResponseTypeDef = TypedDict(
    "_OptionalListStreamsResponseTypeDef", {"nextToken": str}, total=False
)


class ListStreamsResponseTypeDef(
    _RequiredListStreamsResponseTypeDef, _OptionalListStreamsResponseTypeDef
):
    pass


_RequiredListTagsForResourceResponseTypeDef = TypedDict(
    "_RequiredListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}
)
_OptionalListTagsForResourceResponseTypeDef = TypedDict(
    "_OptionalListTagsForResourceResponseTypeDef", {"nextToken": str}, total=False
)


class ListTagsForResourceResponseTypeDef(
    _RequiredListTagsForResourceResponseTypeDef, _OptionalListTagsForResourceResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef", {"channel": "ChannelTypeDef"}, total=False
)
