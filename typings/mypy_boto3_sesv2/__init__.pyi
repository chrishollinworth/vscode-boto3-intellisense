"""
Main interface for sesv2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sesv2 import (
        Client,
        ListMultiRegionEndpointsPaginator,
        SESV2Client,
    )

    session = Session()
    client: SESV2Client = session.client("sesv2")

    list_multi_region_endpoints_paginator: ListMultiRegionEndpointsPaginator = client.get_paginator("list_multi_region_endpoints")
    ```
"""

from .client import SESV2Client
from .paginator import ListMultiRegionEndpointsPaginator

Client = SESV2Client

__all__ = ("Client", "ListMultiRegionEndpointsPaginator", "SESV2Client")
