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
    "ConfigurationStatusType",
    "DescribeMappedResourceConfigurationPaginatorName",
    "FormatConfigKeyType",
    "FormatType",
    "ImageSelectorTypeType",
    "ListSignalingChannelsPaginatorName",
    "ListStreamsPaginatorName",
    "MediaStorageConfigurationStatusType",
    "MediaUriTypeType",
    "StatusType",
    "StrategyOnFullSizeType",
    "SyncStatusType",
    "UpdateDataRetentionOperationType",
)

APINameType = Literal[
    "GET_CLIP",
    "GET_DASH_STREAMING_SESSION_URL",
    "GET_HLS_STREAMING_SESSION_URL",
    "GET_IMAGES",
    "GET_MEDIA",
    "GET_MEDIA_FOR_FRAGMENT_LIST",
    "LIST_FRAGMENTS",
    "PUT_MEDIA",
]
ChannelProtocolType = Literal["HTTPS", "WEBRTC", "WSS"]
ChannelRoleType = Literal["MASTER", "VIEWER"]
ChannelTypeType = Literal["FULL_MESH", "SINGLE_MASTER"]
ComparisonOperatorType = Literal["BEGINS_WITH"]
ConfigurationStatusType = Literal["DISABLED", "ENABLED"]
DescribeMappedResourceConfigurationPaginatorName = Literal["describe_mapped_resource_configuration"]
FormatConfigKeyType = Literal["JPEGQuality"]
FormatType = Literal["JPEG", "PNG"]
ImageSelectorTypeType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
ListSignalingChannelsPaginatorName = Literal["list_signaling_channels"]
ListStreamsPaginatorName = Literal["list_streams"]
MediaStorageConfigurationStatusType = Literal["DISABLED", "ENABLED"]
MediaUriTypeType = Literal["FILE_URI", "RTSP_URI"]
StatusType = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
StrategyOnFullSizeType = Literal["DELETE_OLDEST_MEDIA", "DENY_NEW_MEDIA"]
SyncStatusType = Literal[
    "ACKNOWLEDGED", "DELETE_FAILED", "DELETING", "IN_SYNC", "SYNCING", "SYNC_FAILED"
]
UpdateDataRetentionOperationType = Literal["DECREASE_DATA_RETENTION", "INCREASE_DATA_RETENTION"]
