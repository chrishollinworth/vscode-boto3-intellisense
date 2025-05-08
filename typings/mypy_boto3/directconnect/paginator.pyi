"""
Type annotations for directconnect service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_directconnect.client import DirectConnectClient
    from mypy_boto3_directconnect.paginator import (
        DescribeDirectConnectGatewayAssociationsPaginator,
        DescribeDirectConnectGatewayAttachmentsPaginator,
        DescribeDirectConnectGatewaysPaginator,
    )

    session = Session()
    client: DirectConnectClient = session.client("directconnect")

    describe_direct_connect_gateway_associations_paginator: DescribeDirectConnectGatewayAssociationsPaginator = client.get_paginator("describe_direct_connect_gateway_associations")
    describe_direct_connect_gateway_attachments_paginator: DescribeDirectConnectGatewayAttachmentsPaginator = client.get_paginator("describe_direct_connect_gateway_attachments")
    describe_direct_connect_gateways_paginator: DescribeDirectConnectGatewaysPaginator = client.get_paginator("describe_direct_connect_gateways")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef,
    DescribeDirectConnectGatewayAssociationsResultTypeDef,
    DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef,
    DescribeDirectConnectGatewayAttachmentsResultTypeDef,
    DescribeDirectConnectGatewaysRequestPaginateTypeDef,
    DescribeDirectConnectGatewaysResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeDirectConnectGatewayAssociationsPaginator",
    "DescribeDirectConnectGatewayAttachmentsPaginator",
    "DescribeDirectConnectGatewaysPaginator",
)

if TYPE_CHECKING:
    _DescribeDirectConnectGatewayAssociationsPaginatorBase = Paginator[
        DescribeDirectConnectGatewayAssociationsResultTypeDef
    ]
else:
    _DescribeDirectConnectGatewayAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDirectConnectGatewayAssociationsPaginator(
    _DescribeDirectConnectGatewayAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/paginator/DescribeDirectConnectGatewayAssociations.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators/#describedirectconnectgatewayassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDirectConnectGatewayAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/paginator/DescribeDirectConnectGatewayAssociations.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators/#describedirectconnectgatewayassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeDirectConnectGatewayAttachmentsPaginatorBase = Paginator[
        DescribeDirectConnectGatewayAttachmentsResultTypeDef
    ]
else:
    _DescribeDirectConnectGatewayAttachmentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDirectConnectGatewayAttachmentsPaginator(
    _DescribeDirectConnectGatewayAttachmentsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/paginator/DescribeDirectConnectGatewayAttachments.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators/#describedirectconnectgatewayattachmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDirectConnectGatewayAttachmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/paginator/DescribeDirectConnectGatewayAttachments.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators/#describedirectconnectgatewayattachmentspaginator)
        """

if TYPE_CHECKING:
    _DescribeDirectConnectGatewaysPaginatorBase = Paginator[
        DescribeDirectConnectGatewaysResultTypeDef
    ]
else:
    _DescribeDirectConnectGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDirectConnectGatewaysPaginator(_DescribeDirectConnectGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/paginator/DescribeDirectConnectGateways.html#DirectConnect.Paginator.DescribeDirectConnectGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators/#describedirectconnectgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDirectConnectGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDirectConnectGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/paginator/DescribeDirectConnectGateways.html#DirectConnect.Paginator.DescribeDirectConnectGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators/#describedirectconnectgatewayspaginator)
        """
