"""
Type annotations for kinesisvideo service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_kinesisvideo.client import KinesisVideoClient
    from mypy_boto3_kinesisvideo.paginator import (
        DescribeMappedResourceConfigurationPaginator,
        ListEdgeAgentConfigurationsPaginator,
        ListSignalingChannelsPaginator,
        ListStreamsPaginator,
    )

    session = Session()
    client: KinesisVideoClient = session.client("kinesisvideo")

    describe_mapped_resource_configuration_paginator: DescribeMappedResourceConfigurationPaginator = client.get_paginator("describe_mapped_resource_configuration")
    list_edge_agent_configurations_paginator: ListEdgeAgentConfigurationsPaginator = client.get_paginator("list_edge_agent_configurations")
    list_signaling_channels_paginator: ListSignalingChannelsPaginator = client.get_paginator("list_signaling_channels")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeMappedResourceConfigurationInputPaginateTypeDef,
    DescribeMappedResourceConfigurationOutputTypeDef,
    ListEdgeAgentConfigurationsInputPaginateTypeDef,
    ListEdgeAgentConfigurationsOutputTypeDef,
    ListSignalingChannelsInputPaginateTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsInputPaginateTypeDef,
    ListStreamsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeMappedResourceConfigurationPaginator",
    "ListEdgeAgentConfigurationsPaginator",
    "ListSignalingChannelsPaginator",
    "ListStreamsPaginator",
)

if TYPE_CHECKING:
    _DescribeMappedResourceConfigurationPaginatorBase = Paginator[
        DescribeMappedResourceConfigurationOutputTypeDef
    ]
else:
    _DescribeMappedResourceConfigurationPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMappedResourceConfigurationPaginator(
    _DescribeMappedResourceConfigurationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/DescribeMappedResourceConfiguration.html#KinesisVideo.Paginator.DescribeMappedResourceConfiguration)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#describemappedresourceconfigurationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMappedResourceConfigurationInputPaginateTypeDef]
    ) -> PageIterator[DescribeMappedResourceConfigurationOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/DescribeMappedResourceConfiguration.html#KinesisVideo.Paginator.DescribeMappedResourceConfiguration.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#describemappedresourceconfigurationpaginator)
        """

if TYPE_CHECKING:
    _ListEdgeAgentConfigurationsPaginatorBase = Paginator[ListEdgeAgentConfigurationsOutputTypeDef]
else:
    _ListEdgeAgentConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEdgeAgentConfigurationsPaginator(_ListEdgeAgentConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/ListEdgeAgentConfigurations.html#KinesisVideo.Paginator.ListEdgeAgentConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#listedgeagentconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEdgeAgentConfigurationsInputPaginateTypeDef]
    ) -> PageIterator[ListEdgeAgentConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/ListEdgeAgentConfigurations.html#KinesisVideo.Paginator.ListEdgeAgentConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#listedgeagentconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListSignalingChannelsPaginatorBase = Paginator[ListSignalingChannelsOutputTypeDef]
else:
    _ListSignalingChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSignalingChannelsPaginator(_ListSignalingChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/ListSignalingChannels.html#KinesisVideo.Paginator.ListSignalingChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#listsignalingchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSignalingChannelsInputPaginateTypeDef]
    ) -> PageIterator[ListSignalingChannelsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/ListSignalingChannels.html#KinesisVideo.Paginator.ListSignalingChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#listsignalingchannelspaginator)
        """

if TYPE_CHECKING:
    _ListStreamsPaginatorBase = Paginator[ListStreamsOutputTypeDef]
else:
    _ListStreamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamsPaginator(_ListStreamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/ListStreams.html#KinesisVideo.Paginator.ListStreams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#liststreamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamsInputPaginateTypeDef]
    ) -> PageIterator[ListStreamsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/paginator/ListStreams.html#KinesisVideo.Paginator.ListStreams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators/#liststreamspaginator)
        """
