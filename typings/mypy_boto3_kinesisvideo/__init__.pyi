"""
Main interface for kinesisvideo service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisvideo import (
        Client,
        DescribeMappedResourceConfigurationPaginator,
        KinesisVideoClient,
        ListSignalingChannelsPaginator,
        ListStreamsPaginator,
    )

    session = boto3.Session()

    client: KinesisVideoClient = boto3.client("kinesisvideo")
    session_client: KinesisVideoClient = session.client("kinesisvideo")

    describe_mapped_resource_configuration_paginator: DescribeMappedResourceConfigurationPaginator = client.get_paginator("describe_mapped_resource_configuration")
    list_signaling_channels_paginator: ListSignalingChannelsPaginator = client.get_paginator("list_signaling_channels")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""
from .client import KinesisVideoClient
from .paginator import (
    DescribeMappedResourceConfigurationPaginator,
    ListSignalingChannelsPaginator,
    ListStreamsPaginator,
)

Client = KinesisVideoClient

__all__ = (
    "Client",
    "DescribeMappedResourceConfigurationPaginator",
    "KinesisVideoClient",
    "ListSignalingChannelsPaginator",
    "ListStreamsPaginator",
)
