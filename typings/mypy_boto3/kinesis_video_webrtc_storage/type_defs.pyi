"""
Type annotations for kinesis-video-webrtc-storage service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_webrtc_storage.type_defs import JoinStorageSessionInputRequestTypeDef

    data: JoinStorageSessionInputRequestTypeDef = {...}
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = ("JoinStorageSessionInputRequestTypeDef",)

JoinStorageSessionInputRequestTypeDef = TypedDict(
    "JoinStorageSessionInputRequestTypeDef",
    {
        "channelArn": str,
    },
)
