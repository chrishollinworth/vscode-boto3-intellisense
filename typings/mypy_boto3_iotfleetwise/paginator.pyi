"""
Type annotations for iotfleetwise service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iotfleetwise import IoTFleetWiseClient
    from mypy_boto3_iotfleetwise.paginator import (
        GetVehicleStatusPaginator,
        ListCampaignsPaginator,
        ListDecoderManifestNetworkInterfacesPaginator,
        ListDecoderManifestSignalsPaginator,
        ListDecoderManifestsPaginator,
        ListFleetsPaginator,
        ListFleetsForVehiclePaginator,
        ListModelManifestNodesPaginator,
        ListModelManifestsPaginator,
        ListSignalCatalogNodesPaginator,
        ListSignalCatalogsPaginator,
        ListVehiclesPaginator,
        ListVehiclesInFleetPaginator,
    )

    client: IoTFleetWiseClient = boto3.client("iotfleetwise")

    get_vehicle_status_paginator: GetVehicleStatusPaginator = client.get_paginator("get_vehicle_status")
    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_decoder_manifest_network_interfaces_paginator: ListDecoderManifestNetworkInterfacesPaginator = client.get_paginator("list_decoder_manifest_network_interfaces")
    list_decoder_manifest_signals_paginator: ListDecoderManifestSignalsPaginator = client.get_paginator("list_decoder_manifest_signals")
    list_decoder_manifests_paginator: ListDecoderManifestsPaginator = client.get_paginator("list_decoder_manifests")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_fleets_for_vehicle_paginator: ListFleetsForVehiclePaginator = client.get_paginator("list_fleets_for_vehicle")
    list_model_manifest_nodes_paginator: ListModelManifestNodesPaginator = client.get_paginator("list_model_manifest_nodes")
    list_model_manifests_paginator: ListModelManifestsPaginator = client.get_paginator("list_model_manifests")
    list_signal_catalog_nodes_paginator: ListSignalCatalogNodesPaginator = client.get_paginator("list_signal_catalog_nodes")
    list_signal_catalogs_paginator: ListSignalCatalogsPaginator = client.get_paginator("list_signal_catalogs")
    list_vehicles_paginator: ListVehiclesPaginator = client.get_paginator("list_vehicles")
    list_vehicles_in_fleet_paginator: ListVehiclesInFleetPaginator = client.get_paginator("list_vehicles_in_fleet")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import SignalNodeTypeType
from .type_defs import (
    GetVehicleStatusResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDecoderManifestNetworkInterfacesResponseTypeDef,
    ListDecoderManifestSignalsResponseTypeDef,
    ListDecoderManifestsResponseTypeDef,
    ListFleetsForVehicleResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListModelManifestNodesResponseTypeDef,
    ListModelManifestsResponseTypeDef,
    ListSignalCatalogNodesResponseTypeDef,
    ListSignalCatalogsResponseTypeDef,
    ListVehiclesInFleetResponseTypeDef,
    ListVehiclesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetVehicleStatusPaginator",
    "ListCampaignsPaginator",
    "ListDecoderManifestNetworkInterfacesPaginator",
    "ListDecoderManifestSignalsPaginator",
    "ListDecoderManifestsPaginator",
    "ListFleetsPaginator",
    "ListFleetsForVehiclePaginator",
    "ListModelManifestNodesPaginator",
    "ListModelManifestsPaginator",
    "ListSignalCatalogNodesPaginator",
    "ListSignalCatalogsPaginator",
    "ListVehiclesPaginator",
    "ListVehiclesInFleetPaginator",
)

class GetVehicleStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.GetVehicleStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#getvehiclestatuspaginator)
    """

    def paginate(
        self, *, vehicleName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetVehicleStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.GetVehicleStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#getvehiclestatuspaginator)
        """

class ListCampaignsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListCampaigns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listcampaignspaginator)
    """

    def paginate(
        self, *, status: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCampaignsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListCampaigns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listcampaignspaginator)
        """

class ListDecoderManifestNetworkInterfacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestNetworkInterfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestnetworkinterfacespaginator)
    """

    def paginate(
        self, *, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDecoderManifestNetworkInterfacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestNetworkInterfaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestnetworkinterfacespaginator)
        """

class ListDecoderManifestSignalsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestSignals)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestsignalspaginator)
    """

    def paginate(
        self, *, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDecoderManifestSignalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestSignals.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestsignalspaginator)
        """

class ListDecoderManifestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestspaginator)
    """

    def paginate(
        self, *, modelManifestArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDecoderManifestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestspaginator)
        """

class ListFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listfleetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listfleetspaginator)
        """

class ListFleetsForVehiclePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleetsForVehicle)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listfleetsforvehiclepaginator)
    """

    def paginate(
        self, *, vehicleName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFleetsForVehicleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleetsForVehicle.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listfleetsforvehiclepaginator)
        """

class ListModelManifestNodesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifestNodes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listmodelmanifestnodespaginator)
    """

    def paginate(
        self, *, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelManifestNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifestNodes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listmodelmanifestnodespaginator)
        """

class ListModelManifestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listmodelmanifestspaginator)
    """

    def paginate(
        self, *, signalCatalogArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelManifestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listmodelmanifestspaginator)
        """

class ListSignalCatalogNodesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogNodes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listsignalcatalognodespaginator)
    """

    def paginate(
        self,
        *,
        name: str,
        signalNodeType: SignalNodeTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSignalCatalogNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogNodes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listsignalcatalognodespaginator)
        """

class ListSignalCatalogsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listsignalcatalogspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSignalCatalogsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listsignalcatalogspaginator)
        """

class ListVehiclesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehicles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listvehiclespaginator)
    """

    def paginate(
        self,
        *,
        modelManifestArn: str = None,
        attributeNames: List[str] = None,
        attributeValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVehiclesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehicles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listvehiclespaginator)
        """

class ListVehiclesInFleetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehiclesInFleet)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listvehiclesinfleetpaginator)
    """

    def paginate(
        self, *, fleetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVehiclesInFleetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehiclesInFleet.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listvehiclesinfleetpaginator)
        """
