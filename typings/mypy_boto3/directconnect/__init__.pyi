"""
Main interface for directconnect service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_directconnect import (
        Client,
        DescribeDirectConnectGatewayAssociationsPaginator,
        DescribeDirectConnectGatewayAttachmentsPaginator,
        DescribeDirectConnectGatewaysPaginator,
        DirectConnectClient,
    )

    session = Session()
    client: DirectConnectClient = session.client("directconnect")

    describe_direct_connect_gateway_associations_paginator: DescribeDirectConnectGatewayAssociationsPaginator = client.get_paginator("describe_direct_connect_gateway_associations")
    describe_direct_connect_gateway_attachments_paginator: DescribeDirectConnectGatewayAttachmentsPaginator = client.get_paginator("describe_direct_connect_gateway_attachments")
    describe_direct_connect_gateways_paginator: DescribeDirectConnectGatewaysPaginator = client.get_paginator("describe_direct_connect_gateways")
    ```
"""

from .client import DirectConnectClient
from .paginator import (
    DescribeDirectConnectGatewayAssociationsPaginator,
    DescribeDirectConnectGatewayAttachmentsPaginator,
    DescribeDirectConnectGatewaysPaginator,
)

Client = DirectConnectClient

__all__ = (
    "Client",
    "DescribeDirectConnectGatewayAssociationsPaginator",
    "DescribeDirectConnectGatewayAttachmentsPaginator",
    "DescribeDirectConnectGatewaysPaginator",
    "DirectConnectClient",
)
