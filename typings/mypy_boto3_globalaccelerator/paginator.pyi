"""
Type annotations for globalaccelerator service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_globalaccelerator.client import GlobalAcceleratorClient
    from mypy_boto3_globalaccelerator.paginator import (
        ListAcceleratorsPaginator,
        ListByoipCidrsPaginator,
        ListCrossAccountAttachmentsPaginator,
        ListCrossAccountResourcesPaginator,
        ListCustomRoutingAcceleratorsPaginator,
        ListCustomRoutingEndpointGroupsPaginator,
        ListCustomRoutingListenersPaginator,
        ListCustomRoutingPortMappingsByDestinationPaginator,
        ListCustomRoutingPortMappingsPaginator,
        ListEndpointGroupsPaginator,
        ListListenersPaginator,
    )

    session = Session()
    client: GlobalAcceleratorClient = session.client("globalaccelerator")

    list_accelerators_paginator: ListAcceleratorsPaginator = client.get_paginator("list_accelerators")
    list_byoip_cidrs_paginator: ListByoipCidrsPaginator = client.get_paginator("list_byoip_cidrs")
    list_cross_account_attachments_paginator: ListCrossAccountAttachmentsPaginator = client.get_paginator("list_cross_account_attachments")
    list_cross_account_resources_paginator: ListCrossAccountResourcesPaginator = client.get_paginator("list_cross_account_resources")
    list_custom_routing_accelerators_paginator: ListCustomRoutingAcceleratorsPaginator = client.get_paginator("list_custom_routing_accelerators")
    list_custom_routing_endpoint_groups_paginator: ListCustomRoutingEndpointGroupsPaginator = client.get_paginator("list_custom_routing_endpoint_groups")
    list_custom_routing_listeners_paginator: ListCustomRoutingListenersPaginator = client.get_paginator("list_custom_routing_listeners")
    list_custom_routing_port_mappings_by_destination_paginator: ListCustomRoutingPortMappingsByDestinationPaginator = client.get_paginator("list_custom_routing_port_mappings_by_destination")
    list_custom_routing_port_mappings_paginator: ListCustomRoutingPortMappingsPaginator = client.get_paginator("list_custom_routing_port_mappings")
    list_endpoint_groups_paginator: ListEndpointGroupsPaginator = client.get_paginator("list_endpoint_groups")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAcceleratorsRequestPaginateTypeDef,
    ListAcceleratorsResponseTypeDef,
    ListByoipCidrsRequestPaginateTypeDef,
    ListByoipCidrsResponseTypeDef,
    ListCrossAccountAttachmentsRequestPaginateTypeDef,
    ListCrossAccountAttachmentsResponseTypeDef,
    ListCrossAccountResourcesRequestPaginateTypeDef,
    ListCrossAccountResourcesResponseTypeDef,
    ListCustomRoutingAcceleratorsRequestPaginateTypeDef,
    ListCustomRoutingAcceleratorsResponseTypeDef,
    ListCustomRoutingEndpointGroupsRequestPaginateTypeDef,
    ListCustomRoutingEndpointGroupsResponseTypeDef,
    ListCustomRoutingListenersRequestPaginateTypeDef,
    ListCustomRoutingListenersResponseTypeDef,
    ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef,
    ListCustomRoutingPortMappingsByDestinationResponseTypeDef,
    ListCustomRoutingPortMappingsRequestPaginateTypeDef,
    ListCustomRoutingPortMappingsResponseTypeDef,
    ListEndpointGroupsRequestPaginateTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersRequestPaginateTypeDef,
    ListListenersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAcceleratorsPaginator",
    "ListByoipCidrsPaginator",
    "ListCrossAccountAttachmentsPaginator",
    "ListCrossAccountResourcesPaginator",
    "ListCustomRoutingAcceleratorsPaginator",
    "ListCustomRoutingEndpointGroupsPaginator",
    "ListCustomRoutingListenersPaginator",
    "ListCustomRoutingPortMappingsByDestinationPaginator",
    "ListCustomRoutingPortMappingsPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)

if TYPE_CHECKING:
    _ListAcceleratorsPaginatorBase = Paginator[ListAcceleratorsResponseTypeDef]
else:
    _ListAcceleratorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAcceleratorsPaginator(_ListAcceleratorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListAccelerators.html#GlobalAccelerator.Paginator.ListAccelerators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listacceleratorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAcceleratorsRequestPaginateTypeDef]
    ) -> PageIterator[ListAcceleratorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListAccelerators.html#GlobalAccelerator.Paginator.ListAccelerators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listacceleratorspaginator)
        """

if TYPE_CHECKING:
    _ListByoipCidrsPaginatorBase = Paginator[ListByoipCidrsResponseTypeDef]
else:
    _ListByoipCidrsPaginatorBase = Paginator  # type: ignore[assignment]

class ListByoipCidrsPaginator(_ListByoipCidrsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListByoipCidrs.html#GlobalAccelerator.Paginator.ListByoipCidrs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listbyoipcidrspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListByoipCidrsRequestPaginateTypeDef]
    ) -> PageIterator[ListByoipCidrsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListByoipCidrs.html#GlobalAccelerator.Paginator.ListByoipCidrs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listbyoipcidrspaginator)
        """

if TYPE_CHECKING:
    _ListCrossAccountAttachmentsPaginatorBase = Paginator[
        ListCrossAccountAttachmentsResponseTypeDef
    ]
else:
    _ListCrossAccountAttachmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCrossAccountAttachmentsPaginator(_ListCrossAccountAttachmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCrossAccountAttachments.html#GlobalAccelerator.Paginator.ListCrossAccountAttachments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcrossaccountattachmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCrossAccountAttachmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListCrossAccountAttachmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCrossAccountAttachments.html#GlobalAccelerator.Paginator.ListCrossAccountAttachments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcrossaccountattachmentspaginator)
        """

if TYPE_CHECKING:
    _ListCrossAccountResourcesPaginatorBase = Paginator[ListCrossAccountResourcesResponseTypeDef]
else:
    _ListCrossAccountResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCrossAccountResourcesPaginator(_ListCrossAccountResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCrossAccountResources.html#GlobalAccelerator.Paginator.ListCrossAccountResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcrossaccountresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCrossAccountResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListCrossAccountResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCrossAccountResources.html#GlobalAccelerator.Paginator.ListCrossAccountResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcrossaccountresourcespaginator)
        """

if TYPE_CHECKING:
    _ListCustomRoutingAcceleratorsPaginatorBase = Paginator[
        ListCustomRoutingAcceleratorsResponseTypeDef
    ]
else:
    _ListCustomRoutingAcceleratorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomRoutingAcceleratorsPaginator(_ListCustomRoutingAcceleratorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingAccelerators.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingacceleratorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomRoutingAcceleratorsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomRoutingAcceleratorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingAccelerators.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingacceleratorspaginator)
        """

if TYPE_CHECKING:
    _ListCustomRoutingEndpointGroupsPaginatorBase = Paginator[
        ListCustomRoutingEndpointGroupsResponseTypeDef
    ]
else:
    _ListCustomRoutingEndpointGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomRoutingEndpointGroupsPaginator(_ListCustomRoutingEndpointGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingEndpointGroups.html#GlobalAccelerator.Paginator.ListCustomRoutingEndpointGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingendpointgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomRoutingEndpointGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomRoutingEndpointGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingEndpointGroups.html#GlobalAccelerator.Paginator.ListCustomRoutingEndpointGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingendpointgroupspaginator)
        """

if TYPE_CHECKING:
    _ListCustomRoutingListenersPaginatorBase = Paginator[ListCustomRoutingListenersResponseTypeDef]
else:
    _ListCustomRoutingListenersPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomRoutingListenersPaginator(_ListCustomRoutingListenersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingListeners.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutinglistenerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomRoutingListenersRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomRoutingListenersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingListeners.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutinglistenerspaginator)
        """

if TYPE_CHECKING:
    _ListCustomRoutingPortMappingsByDestinationPaginatorBase = Paginator[
        ListCustomRoutingPortMappingsByDestinationResponseTypeDef
    ]
else:
    _ListCustomRoutingPortMappingsByDestinationPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomRoutingPortMappingsByDestinationPaginator(
    _ListCustomRoutingPortMappingsByDestinationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingPortMappingsByDestination.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingportmappingsbydestinationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomRoutingPortMappingsByDestinationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingPortMappingsByDestination.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingportmappingsbydestinationpaginator)
        """

if TYPE_CHECKING:
    _ListCustomRoutingPortMappingsPaginatorBase = Paginator[
        ListCustomRoutingPortMappingsResponseTypeDef
    ]
else:
    _ListCustomRoutingPortMappingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomRoutingPortMappingsPaginator(_ListCustomRoutingPortMappingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingPortMappings.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingportmappingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomRoutingPortMappingsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomRoutingPortMappingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListCustomRoutingPortMappings.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listcustomroutingportmappingspaginator)
        """

if TYPE_CHECKING:
    _ListEndpointGroupsPaginatorBase = Paginator[ListEndpointGroupsResponseTypeDef]
else:
    _ListEndpointGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEndpointGroupsPaginator(_ListEndpointGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListEndpointGroups.html#GlobalAccelerator.Paginator.ListEndpointGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listendpointgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEndpointGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListEndpointGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListEndpointGroups.html#GlobalAccelerator.Paginator.ListEndpointGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listendpointgroupspaginator)
        """

if TYPE_CHECKING:
    _ListListenersPaginatorBase = Paginator[ListListenersResponseTypeDef]
else:
    _ListListenersPaginatorBase = Paginator  # type: ignore[assignment]

class ListListenersPaginator(_ListListenersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListListeners.html#GlobalAccelerator.Paginator.ListListeners)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listlistenerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListListenersRequestPaginateTypeDef]
    ) -> PageIterator[ListListenersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator/paginator/ListListeners.html#GlobalAccelerator.Paginator.ListListeners.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators/#listlistenerspaginator)
        """
