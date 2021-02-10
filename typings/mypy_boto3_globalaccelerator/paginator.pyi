"""
Main interface for globalaccelerator service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_globalaccelerator import GlobalAcceleratorClient
    from mypy_boto3_globalaccelerator.paginator import (
        ListAcceleratorsPaginator,
        ListByoipCidrsPaginator,
        ListCustomRoutingAcceleratorsPaginator,
        ListCustomRoutingListenersPaginator,
        ListCustomRoutingPortMappingsPaginator,
        ListCustomRoutingPortMappingsByDestinationPaginator,
        ListEndpointGroupsPaginator,
        ListListenersPaginator,
    )

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")

    list_accelerators_paginator: ListAcceleratorsPaginator = client.get_paginator("list_accelerators")
    list_byoip_cidrs_paginator: ListByoipCidrsPaginator = client.get_paginator("list_byoip_cidrs")
    list_custom_routing_accelerators_paginator: ListCustomRoutingAcceleratorsPaginator = client.get_paginator("list_custom_routing_accelerators")
    list_custom_routing_listeners_paginator: ListCustomRoutingListenersPaginator = client.get_paginator("list_custom_routing_listeners")
    list_custom_routing_port_mappings_paginator: ListCustomRoutingPortMappingsPaginator = client.get_paginator("list_custom_routing_port_mappings")
    list_custom_routing_port_mappings_by_destination_paginator: ListCustomRoutingPortMappingsByDestinationPaginator = client.get_paginator("list_custom_routing_port_mappings_by_destination")
    list_endpoint_groups_paginator: ListEndpointGroupsPaginator = client.get_paginator("list_endpoint_groups")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_globalaccelerator.type_defs import (
    ListAcceleratorsResponseTypeDef,
    ListByoipCidrsResponseTypeDef,
    ListCustomRoutingAcceleratorsResponseTypeDef,
    ListCustomRoutingListenersResponseTypeDef,
    ListCustomRoutingPortMappingsByDestinationResponseTypeDef,
    ListCustomRoutingPortMappingsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAcceleratorsPaginator",
    "ListByoipCidrsPaginator",
    "ListCustomRoutingAcceleratorsPaginator",
    "ListCustomRoutingListenersPaginator",
    "ListCustomRoutingPortMappingsPaginator",
    "ListCustomRoutingPortMappingsByDestinationPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)


class ListAcceleratorsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAcceleratorsResponseTypeDef]:
        """
        [ListAccelerators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators.paginate)
        """


class ListByoipCidrsPaginator(Boto3Paginator):
    """
    [Paginator.ListByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListByoipCidrs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListByoipCidrsResponseTypeDef]:
        """
        [ListByoipCidrs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListByoipCidrs.paginate)
        """


class ListCustomRoutingAcceleratorsPaginator(Boto3Paginator):
    """
    [Paginator.ListCustomRoutingAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomRoutingAcceleratorsResponseTypeDef]:
        """
        [ListCustomRoutingAccelerators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators.paginate)
        """


class ListCustomRoutingListenersPaginator(Boto3Paginator):
    """
    [Paginator.ListCustomRoutingListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners)
    """

    def paginate(
        self, AcceleratorArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomRoutingListenersResponseTypeDef]:
        """
        [ListCustomRoutingListeners.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners.paginate)
        """


class ListCustomRoutingPortMappingsPaginator(Boto3Paginator):
    """
    [Paginator.ListCustomRoutingPortMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings)
    """

    def paginate(
        self,
        AcceleratorArn: str,
        EndpointGroupArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCustomRoutingPortMappingsResponseTypeDef]:
        """
        [ListCustomRoutingPortMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings.paginate)
        """


class ListCustomRoutingPortMappingsByDestinationPaginator(Boto3Paginator):
    """
    [Paginator.ListCustomRoutingPortMappingsByDestination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination)
    """

    def paginate(
        self,
        EndpointId: str,
        DestinationAddress: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCustomRoutingPortMappingsByDestinationResponseTypeDef]:
        """
        [ListCustomRoutingPortMappingsByDestination.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination.paginate)
        """


class ListEndpointGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
    """

    def paginate(
        self, ListenerArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointGroupsResponseTypeDef]:
        """
        [ListEndpointGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups.paginate)
        """


class ListListenersPaginator(Boto3Paginator):
    """
    [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
    """

    def paginate(
        self, AcceleratorArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListListenersResponseTypeDef]:
        """
        [ListListeners.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners.paginate)
        """
