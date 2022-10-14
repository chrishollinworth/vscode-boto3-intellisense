"""
Main interface for iotfleetwise service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotfleetwise import (
        Client,
        GetVehicleStatusPaginator,
        IoTFleetWiseClient,
        ListCampaignsPaginator,
        ListDecoderManifestNetworkInterfacesPaginator,
        ListDecoderManifestSignalsPaginator,
        ListDecoderManifestsPaginator,
        ListFleetsForVehiclePaginator,
        ListFleetsPaginator,
        ListModelManifestNodesPaginator,
        ListModelManifestsPaginator,
        ListSignalCatalogNodesPaginator,
        ListSignalCatalogsPaginator,
        ListVehiclesInFleetPaginator,
        ListVehiclesPaginator,
    )

    session = boto3.Session()

    client: IoTFleetWiseClient = boto3.client("iotfleetwise")
    session_client: IoTFleetWiseClient = session.client("iotfleetwise")

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
from .client import IoTFleetWiseClient
from .paginator import (
    GetVehicleStatusPaginator,
    ListCampaignsPaginator,
    ListDecoderManifestNetworkInterfacesPaginator,
    ListDecoderManifestSignalsPaginator,
    ListDecoderManifestsPaginator,
    ListFleetsForVehiclePaginator,
    ListFleetsPaginator,
    ListModelManifestNodesPaginator,
    ListModelManifestsPaginator,
    ListSignalCatalogNodesPaginator,
    ListSignalCatalogsPaginator,
    ListVehiclesInFleetPaginator,
    ListVehiclesPaginator,
)

Client = IoTFleetWiseClient

__all__ = (
    "Client",
    "GetVehicleStatusPaginator",
    "IoTFleetWiseClient",
    "ListCampaignsPaginator",
    "ListDecoderManifestNetworkInterfacesPaginator",
    "ListDecoderManifestSignalsPaginator",
    "ListDecoderManifestsPaginator",
    "ListFleetsForVehiclePaginator",
    "ListFleetsPaginator",
    "ListModelManifestNodesPaginator",
    "ListModelManifestsPaginator",
    "ListSignalCatalogNodesPaginator",
    "ListSignalCatalogsPaginator",
    "ListVehiclesInFleetPaginator",
    "ListVehiclesPaginator",
)
