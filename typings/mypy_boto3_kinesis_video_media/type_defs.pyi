"""
Main interface for kinesis-video-media service type definitions.

Usage::

    ```python
    from mypy_boto3_kinesis_video_media.type_defs import ResponseMetadata

    data: ResponseMetadata = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ResponseMetadata", "GetMediaOutputTypeDef", "StartSelectorTypeDef")

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

GetMediaOutputTypeDef = TypedDict(
    "GetMediaOutputTypeDef",
    {"ContentType": str, "Payload": IO[bytes], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredStartSelectorTypeDef = TypedDict(
    "_RequiredStartSelectorTypeDef",
    {
        "StartSelectorType": Literal[
            "FRAGMENT_NUMBER",
            "SERVER_TIMESTAMP",
            "PRODUCER_TIMESTAMP",
            "NOW",
            "EARLIEST",
            "CONTINUATION_TOKEN",
        ]
    },
)
_OptionalStartSelectorTypeDef = TypedDict(
    "_OptionalStartSelectorTypeDef",
    {"AfterFragmentNumber": str, "StartTimestamp": datetime, "ContinuationToken": str},
    total=False,
)


class StartSelectorTypeDef(_RequiredStartSelectorTypeDef, _OptionalStartSelectorTypeDef):
    pass
