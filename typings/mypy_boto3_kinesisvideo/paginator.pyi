"""
Type annotations for kinesisvideo service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesisvideo import KinesisVideoClient
    from mypy_boto3_kinesisvideo.paginator import (
        DescribeMappedResourceConfigurationPaginator,
        ListEdgeAgentConfigurationsPaginator,
        ListSignalingChannelsPaginator,
        ListStreamsPaginator,
    )

    client: KinesisVideoClient = boto3.client("kinesisvideo")

    describe_mapped_resource_configuration_paginator: DescribeMappedResourceConfigurationPaginator = client.get_paginator("describe_mapped_resource_configuration")
    list_edge_agent_configurations_paginator: ListEdgeAgentConfigurationsPaginator = client.get_paginator("list_edge_agent_configurations")
    list_signaling_channels_paginator: ListSignalingChannelsPaginator = client.get_paginator("list_signaling_channels")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ChannelNameConditionTypeDef,
    DescribeMappedResourceConfigurationOutputTypeDef,
    ListEdgeAgentConfigurationsOutputTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    PaginatorConfigTypeDef,
    StreamNameConditionTypeDef,
)

__all__ = (
    "DescribeMappedResourceConfigurationPaginator",
    "ListEdgeAgentConfigurationsPaginator",
    "ListSignalingChannelsPaginator",
    "ListStreamsPaginator",
)

class DescribeMappedResourceConfigurationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.DescribeMappedResourceConfiguration)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#describemappedresourceconfigurationpaginator)
    """

    def paginate(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMappedResourceConfigurationOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.DescribeMappedResourceConfiguration.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#describemappedresourceconfigurationpaginator)
        """

class ListEdgeAgentConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListEdgeAgentConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#listedgeagentconfigurationspaginator)
    """

    def paginate(
        self, *, HubDeviceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEdgeAgentConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListEdgeAgentConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#listedgeagentconfigurationspaginator)
        """

class ListSignalingChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#listsignalingchannelspaginator)
    """

    def paginate(
        self,
        *,
        ChannelNameCondition: "ChannelNameConditionTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSignalingChannelsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#listsignalingchannelspaginator)
        """

class ListStreamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#liststreamspaginator)
    """

    def paginate(
        self,
        *,
        StreamNameCondition: "StreamNameConditionTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#liststreamspaginator)
        """
