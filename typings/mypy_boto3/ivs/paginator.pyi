"""
Type annotations for ivs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ivs.client import IVSClient
    from mypy_boto3_ivs.paginator import (
        ListChannelsPaginator,
        ListPlaybackKeyPairsPaginator,
        ListRecordingConfigurationsPaginator,
        ListStreamKeysPaginator,
        ListStreamsPaginator,
    )

    session = Session()
    client: IVSClient = session.client("ivs")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_playback_key_pairs_paginator: ListPlaybackKeyPairsPaginator = client.get_paginator("list_playback_key_pairs")
    list_recording_configurations_paginator: ListRecordingConfigurationsPaginator = client.get_paginator("list_recording_configurations")
    list_stream_keys_paginator: ListStreamKeysPaginator = client.get_paginator("list_stream_keys")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChannelsRequestPaginateTypeDef,
    ListChannelsResponseTypeDef,
    ListPlaybackKeyPairsRequestPaginateTypeDef,
    ListPlaybackKeyPairsResponseTypeDef,
    ListRecordingConfigurationsRequestPaginateTypeDef,
    ListRecordingConfigurationsResponseTypeDef,
    ListStreamKeysRequestPaginateTypeDef,
    ListStreamKeysResponseTypeDef,
    ListStreamsRequestPaginateTypeDef,
    ListStreamsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListChannelsPaginator",
    "ListPlaybackKeyPairsPaginator",
    "ListRecordingConfigurationsPaginator",
    "ListStreamKeysPaginator",
    "ListStreamsPaginator",
)

if TYPE_CHECKING:
    _ListChannelsPaginatorBase = Paginator[ListChannelsResponseTypeDef]
else:
    _ListChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChannelsPaginator(_ListChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListChannels.html#IVS.Paginator.ListChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#listchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListChannels.html#IVS.Paginator.ListChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#listchannelspaginator)
        """

if TYPE_CHECKING:
    _ListPlaybackKeyPairsPaginatorBase = Paginator[ListPlaybackKeyPairsResponseTypeDef]
else:
    _ListPlaybackKeyPairsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlaybackKeyPairsPaginator(_ListPlaybackKeyPairsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListPlaybackKeyPairs.html#IVS.Paginator.ListPlaybackKeyPairs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#listplaybackkeypairspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlaybackKeyPairsRequestPaginateTypeDef]
    ) -> PageIterator[ListPlaybackKeyPairsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListPlaybackKeyPairs.html#IVS.Paginator.ListPlaybackKeyPairs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#listplaybackkeypairspaginator)
        """

if TYPE_CHECKING:
    _ListRecordingConfigurationsPaginatorBase = Paginator[
        ListRecordingConfigurationsResponseTypeDef
    ]
else:
    _ListRecordingConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecordingConfigurationsPaginator(_ListRecordingConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListRecordingConfigurations.html#IVS.Paginator.ListRecordingConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#listrecordingconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecordingConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecordingConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListRecordingConfigurations.html#IVS.Paginator.ListRecordingConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#listrecordingconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListStreamKeysPaginatorBase = Paginator[ListStreamKeysResponseTypeDef]
else:
    _ListStreamKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamKeysPaginator(_ListStreamKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListStreamKeys.html#IVS.Paginator.ListStreamKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#liststreamkeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListStreamKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListStreamKeys.html#IVS.Paginator.ListStreamKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#liststreamkeyspaginator)
        """

if TYPE_CHECKING:
    _ListStreamsPaginatorBase = Paginator[ListStreamsResponseTypeDef]
else:
    _ListStreamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamsPaginator(_ListStreamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListStreams.html#IVS.Paginator.ListStreams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#liststreamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamsRequestPaginateTypeDef]
    ) -> PageIterator[ListStreamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/paginator/ListStreams.html#IVS.Paginator.ListStreams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators/#liststreamspaginator)
        """
