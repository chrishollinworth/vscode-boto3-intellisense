"""
Type annotations for kinesisvideo service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/literals.html)

Usage::

    ```python
    from mypy_boto3_kinesisvideo.literals import APINameType

    data: APINameType = "GET_CLIP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "APINameType",
    "ChannelProtocolType",
    "ChannelRoleType",
    "ChannelTypeType",
    "ComparisonOperatorType",
    "ListSignalingChannelsPaginatorName",
    "ListStreamsPaginatorName",
    "StatusType",
    "UpdateDataRetentionOperationType",
)

APINameType = Literal[
    "GET_CLIP",
    "GET_DASH_STREAMING_SESSION_URL",
    "GET_HLS_STREAMING_SESSION_URL",
    "GET_MEDIA",
    "GET_MEDIA_FOR_FRAGMENT_LIST",
    "LIST_FRAGMENTS",
    "PUT_MEDIA",
]
ChannelProtocolType = Literal["HTTPS", "WSS"]
ChannelRoleType = Literal["MASTER", "VIEWER"]
ChannelTypeType = Literal["SINGLE_MASTER"]
ComparisonOperatorType = Literal["BEGINS_WITH"]
ListSignalingChannelsPaginatorName = Literal["list_signaling_channels"]
ListStreamsPaginatorName = Literal["list_streams"]
StatusType = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
UpdateDataRetentionOperationType = Literal["DECREASE_DATA_RETENTION", "INCREASE_DATA_RETENTION"]
