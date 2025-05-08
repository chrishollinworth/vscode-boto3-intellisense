"""
Main interface for mediapackagev2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackagev2 import (
        Client,
        HarvestJobFinishedWaiter,
        ListChannelGroupsPaginator,
        ListChannelsPaginator,
        ListHarvestJobsPaginator,
        ListOriginEndpointsPaginator,
        Mediapackagev2Client,
    )

    session = Session()
    client: Mediapackagev2Client = session.client("mediapackagev2")

    harvest_job_finished_waiter: HarvestJobFinishedWaiter = client.get_waiter("harvest_job_finished")

    list_channel_groups_paginator: ListChannelGroupsPaginator = client.get_paginator("list_channel_groups")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_harvest_jobs_paginator: ListHarvestJobsPaginator = client.get_paginator("list_harvest_jobs")
    list_origin_endpoints_paginator: ListOriginEndpointsPaginator = client.get_paginator("list_origin_endpoints")
    ```
"""

from .client import Mediapackagev2Client
from .paginator import (
    ListChannelGroupsPaginator,
    ListChannelsPaginator,
    ListHarvestJobsPaginator,
    ListOriginEndpointsPaginator,
)
from .waiter import HarvestJobFinishedWaiter

Client = Mediapackagev2Client

__all__ = (
    "Client",
    "HarvestJobFinishedWaiter",
    "ListChannelGroupsPaginator",
    "ListChannelsPaginator",
    "ListHarvestJobsPaginator",
    "ListOriginEndpointsPaginator",
    "Mediapackagev2Client",
)
