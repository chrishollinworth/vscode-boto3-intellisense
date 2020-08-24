"""
Main interface for support service.

Usage::

    ```python
    import boto3
    from mypy_boto3_support import (
        Client,
        DescribeCasesPaginator,
        DescribeCommunicationsPaginator,
        SupportClient,
    )

    session = boto3.Session()

    client: SupportClient = boto3.client("support")
    session_client: SupportClient = session.client("support")

    describe_cases_paginator: DescribeCasesPaginator = client.get_paginator("describe_cases")
    describe_communications_paginator: DescribeCommunicationsPaginator = client.get_paginator("describe_communications")
    ```
"""
from mypy_boto3_support.client import SupportClient
from mypy_boto3_support.paginator import DescribeCasesPaginator, DescribeCommunicationsPaginator

Client = SupportClient


__all__ = ("Client", "DescribeCasesPaginator", "DescribeCommunicationsPaginator", "SupportClient")
