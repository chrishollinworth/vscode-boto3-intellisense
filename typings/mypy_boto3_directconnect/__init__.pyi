"""
Main interface for directconnect service.

Usage::

    ```python
    import boto3
    from mypy_boto3_directconnect import (
        Client,
        DescribeDirectConnectGatewayAssociationsPaginator,
        DescribeDirectConnectGatewayAttachmentsPaginator,
        DescribeDirectConnectGatewaysPaginator,
        DirectConnectClient,
    )

    session = boto3.Session()

    client: DirectConnectClient = boto3.client("directconnect")
    session_client: DirectConnectClient = session.client("directconnect")

    describe_direct_connect_gateway_associations_paginator: DescribeDirectConnectGatewayAssociationsPaginator = client.get_paginator("describe_direct_connect_gateway_associations")
    describe_direct_connect_gateway_attachments_paginator: DescribeDirectConnectGatewayAttachmentsPaginator = client.get_paginator("describe_direct_connect_gateway_attachments")
    describe_direct_connect_gateways_paginator: DescribeDirectConnectGatewaysPaginator = client.get_paginator("describe_direct_connect_gateways")
    ```
"""
from mypy_boto3_directconnect.client import DirectConnectClient
from mypy_boto3_directconnect.paginator import (
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
