"""
Type annotations for iotfleetwise service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotfleetwise import IoTFleetWiseClient

    client: IoTFleetWiseClient = boto3.client("iotfleetwise")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    CompressionType,
    DiagnosticsModeType,
    ManifestStatusType,
    SpoolingModeType,
    UpdateCampaignActionType,
    UpdateModeType,
    VehicleAssociationBehaviorType,
)
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
from .type_defs import (
    BatchCreateVehicleResponseTypeDef,
    BatchUpdateVehicleResponseTypeDef,
    CloudWatchLogDeliveryOptionsTypeDef,
    CollectionSchemeTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDecoderManifestResponseTypeDef,
    CreateFleetResponseTypeDef,
    CreateModelManifestResponseTypeDef,
    CreateSignalCatalogResponseTypeDef,
    CreateVehicleRequestItemTypeDef,
    CreateVehicleResponseTypeDef,
    DeleteCampaignResponseTypeDef,
    DeleteDecoderManifestResponseTypeDef,
    DeleteFleetResponseTypeDef,
    DeleteModelManifestResponseTypeDef,
    DeleteSignalCatalogResponseTypeDef,
    DeleteVehicleResponseTypeDef,
    FormattedVssTypeDef,
    GetCampaignResponseTypeDef,
    GetDecoderManifestResponseTypeDef,
    GetFleetResponseTypeDef,
    GetLoggingOptionsResponseTypeDef,
    GetModelManifestResponseTypeDef,
    GetRegisterAccountStatusResponseTypeDef,
    GetSignalCatalogResponseTypeDef,
    GetVehicleResponseTypeDef,
    GetVehicleStatusResponseTypeDef,
    IamResourcesTypeDef,
    ImportDecoderManifestResponseTypeDef,
    ImportSignalCatalogResponseTypeDef,
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
    ListTagsForResourceResponseTypeDef,
    ListVehiclesInFleetResponseTypeDef,
    ListVehiclesResponseTypeDef,
    NetworkFileDefinitionTypeDef,
    NetworkInterfaceTypeDef,
    NodeTypeDef,
    RegisterAccountResponseTypeDef,
    SignalDecoderTypeDef,
    SignalInformationTypeDef,
    TagTypeDef,
    TimestreamResourcesTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateDecoderManifestResponseTypeDef,
    UpdateFleetResponseTypeDef,
    UpdateModelManifestResponseTypeDef,
    UpdateSignalCatalogResponseTypeDef,
    UpdateVehicleRequestItemTypeDef,
    UpdateVehicleResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IoTFleetWiseClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DecoderManifestValidationException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidNodeException: Type[BotocoreClientError]
    InvalidSignalsException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IoTFleetWiseClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTFleetWiseClient exceptions.
        """
    def associate_vehicle_fleet(self, *, vehicleName: str, fleetId: str) -> Dict[str, Any]:
        """
        Adds, or associates, a vehicle with a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.associate_vehicle_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#associate_vehicle_fleet)
        """
    def batch_create_vehicle(
        self, *, vehicles: List["CreateVehicleRequestItemTypeDef"]
    ) -> BatchCreateVehicleResponseTypeDef:
        """
        Creates a group, or batch, of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.batch_create_vehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#batch_create_vehicle)
        """
    def batch_update_vehicle(
        self, *, vehicles: List["UpdateVehicleRequestItemTypeDef"]
    ) -> BatchUpdateVehicleResponseTypeDef:
        """
        Updates a group, or batch, of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.batch_update_vehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#batch_update_vehicle)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#close)
        """
    def create_campaign(
        self,
        *,
        name: str,
        signalCatalogArn: str,
        targetArn: str,
        collectionScheme: "CollectionSchemeTypeDef",
        description: str = None,
        startTime: Union[datetime, str] = None,
        expiryTime: Union[datetime, str] = None,
        postTriggerCollectionDuration: int = None,
        diagnosticsMode: DiagnosticsModeType = None,
        spoolingMode: SpoolingModeType = None,
        compression: CompressionType = None,
        priority: int = None,
        signalsToCollect: List["SignalInformationTypeDef"] = None,
        dataExtraDimensions: List[str] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateCampaignResponseTypeDef:
        """
        Creates an orchestration of data collection rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#create_campaign)
        """
    def create_decoder_manifest(
        self,
        *,
        name: str,
        modelManifestArn: str,
        description: str = None,
        signalDecoders: List["SignalDecoderTypeDef"] = None,
        networkInterfaces: List["NetworkInterfaceTypeDef"] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDecoderManifestResponseTypeDef:
        """
        Creates the decoder manifest associated with a model manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_decoder_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#create_decoder_manifest)
        """
    def create_fleet(
        self,
        *,
        fleetId: str,
        signalCatalogArn: str,
        description: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateFleetResponseTypeDef:
        """
        Creates a fleet that represents a group of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#create_fleet)
        """
    def create_model_manifest(
        self,
        *,
        name: str,
        nodes: List[str],
        signalCatalogArn: str,
        description: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateModelManifestResponseTypeDef:
        """
        Creates a vehicle model (model manifest) that specifies signals (attributes,
        branches, sensors, and actuators).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_model_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#create_model_manifest)
        """
    def create_signal_catalog(
        self,
        *,
        name: str,
        description: str = None,
        nodes: List["NodeTypeDef"] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateSignalCatalogResponseTypeDef:
        """
        Creates a collection of standardized signals that can be reused to create
        vehicle models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_signal_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#create_signal_catalog)
        """
    def create_vehicle(
        self,
        *,
        vehicleName: str,
        modelManifestArn: str,
        decoderManifestArn: str,
        attributes: Dict[str, str] = None,
        associationBehavior: VehicleAssociationBehaviorType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateVehicleResponseTypeDef:
        """
        Creates a vehicle, which is an instance of a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_vehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#create_vehicle)
        """
    def delete_campaign(self, *, name: str) -> DeleteCampaignResponseTypeDef:
        """
        Deletes a data collection campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#delete_campaign)
        """
    def delete_decoder_manifest(self, *, name: str) -> DeleteDecoderManifestResponseTypeDef:
        """
        Deletes a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_decoder_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#delete_decoder_manifest)
        """
    def delete_fleet(self, *, fleetId: str) -> DeleteFleetResponseTypeDef:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#delete_fleet)
        """
    def delete_model_manifest(self, *, name: str) -> DeleteModelManifestResponseTypeDef:
        """
        Deletes a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_model_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#delete_model_manifest)
        """
    def delete_signal_catalog(self, *, name: str) -> DeleteSignalCatalogResponseTypeDef:
        """
        Deletes a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_signal_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#delete_signal_catalog)
        """
    def delete_vehicle(self, *, vehicleName: str) -> DeleteVehicleResponseTypeDef:
        """
        Deletes a vehicle and removes it from any campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_vehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#delete_vehicle)
        """
    def disassociate_vehicle_fleet(self, *, vehicleName: str, fleetId: str) -> Dict[str, Any]:
        """
        Removes, or disassociates, a vehicle from a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.disassociate_vehicle_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#disassociate_vehicle_fleet)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#generate_presigned_url)
        """
    def get_campaign(self, *, name: str) -> GetCampaignResponseTypeDef:
        """
        Retrieves information about a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_campaign)
        """
    def get_decoder_manifest(self, *, name: str) -> GetDecoderManifestResponseTypeDef:
        """
        Retrieves information about a created decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_decoder_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_decoder_manifest)
        """
    def get_fleet(self, *, fleetId: str) -> GetFleetResponseTypeDef:
        """
        Retrieves information about a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_fleet)
        """
    def get_logging_options(self) -> GetLoggingOptionsResponseTypeDef:
        """
        Retrieves the logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_logging_options)
        """
    def get_model_manifest(self, *, name: str) -> GetModelManifestResponseTypeDef:
        """
        Retrieves information about a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_model_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_model_manifest)
        """
    def get_register_account_status(self) -> GetRegisterAccountStatusResponseTypeDef:
        """
        Retrieves information about the status of registering your Amazon Web Services
        account, IAM, and Amazon Timestream resources so that Amazon Web Services IoT
        FleetWise can transfer your vehicle data to the Amazon Web Services Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_register_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_register_account_status)
        """
    def get_signal_catalog(self, *, name: str) -> GetSignalCatalogResponseTypeDef:
        """
        Retrieves information about a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_signal_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_signal_catalog)
        """
    def get_vehicle(self, *, vehicleName: str) -> GetVehicleResponseTypeDef:
        """
        Retrieves information about a vehicle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_vehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_vehicle)
        """
    def get_vehicle_status(
        self, *, vehicleName: str, nextToken: str = None, maxResults: int = None
    ) -> GetVehicleStatusResponseTypeDef:
        """
        Retrieves information about the status of a vehicle with any associated
        campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_vehicle_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#get_vehicle_status)
        """
    def import_decoder_manifest(
        self, *, name: str, networkFileDefinitions: List["NetworkFileDefinitionTypeDef"]
    ) -> ImportDecoderManifestResponseTypeDef:
        """
        Creates a decoder manifest using your existing CAN DBC file from your local
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.import_decoder_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#import_decoder_manifest)
        """
    def import_signal_catalog(
        self,
        *,
        name: str,
        description: str = None,
        vss: "FormattedVssTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> ImportSignalCatalogResponseTypeDef:
        """
        Creates a signal catalog using your existing VSS formatted content from your
        local device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.import_signal_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#import_signal_catalog)
        """
    def list_campaigns(
        self, *, nextToken: str = None, maxResults: int = None, status: str = None
    ) -> ListCampaignsResponseTypeDef:
        """
        Lists information about created campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_campaigns)
        """
    def list_decoder_manifest_network_interfaces(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> ListDecoderManifestNetworkInterfacesResponseTypeDef:
        """
        Lists the network interfaces specified in a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_decoder_manifest_network_interfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_decoder_manifest_network_interfaces)
        """
    def list_decoder_manifest_signals(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> ListDecoderManifestSignalsResponseTypeDef:
        """
        A list of information about signal decoders specified in a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_decoder_manifest_signals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_decoder_manifest_signals)
        """
    def list_decoder_manifests(
        self, *, modelManifestArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDecoderManifestsResponseTypeDef:
        """
        Lists decoder manifests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_decoder_manifests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_decoder_manifests)
        """
    def list_fleets(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListFleetsResponseTypeDef:
        """
        Retrieves information for each created fleet in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_fleets)
        """
    def list_fleets_for_vehicle(
        self, *, vehicleName: str, nextToken: str = None, maxResults: int = None
    ) -> ListFleetsForVehicleResponseTypeDef:
        """
        Retrieves a list of IDs for all fleets that the vehicle is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_fleets_for_vehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_fleets_for_vehicle)
        """
    def list_model_manifest_nodes(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> ListModelManifestNodesResponseTypeDef:
        """
        Lists information about nodes specified in a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_model_manifest_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_model_manifest_nodes)
        """
    def list_model_manifests(
        self, *, signalCatalogArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListModelManifestsResponseTypeDef:
        """
        Retrieves a list of vehicle models (model manifests).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_model_manifests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_model_manifests)
        """
    def list_signal_catalog_nodes(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> ListSignalCatalogNodesResponseTypeDef:
        """
        Lists of information about the signals (nodes) specified in a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_signal_catalog_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_signal_catalog_nodes)
        """
    def list_signal_catalogs(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListSignalCatalogsResponseTypeDef:
        """
        Lists all the created signal catalogs in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_signal_catalogs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_signal_catalogs)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_tags_for_resource)
        """
    def list_vehicles(
        self, *, modelManifestArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListVehiclesResponseTypeDef:
        """
        Retrieves a list of summaries of created vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_vehicles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_vehicles)
        """
    def list_vehicles_in_fleet(
        self, *, fleetId: str, nextToken: str = None, maxResults: int = None
    ) -> ListVehiclesInFleetResponseTypeDef:
        """
        Retrieves a list of summaries of all vehicles associated with a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_vehicles_in_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#list_vehicles_in_fleet)
        """
    def put_logging_options(
        self, *, cloudWatchLogDelivery: "CloudWatchLogDeliveryOptionsTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates or updates the logging option.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.put_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#put_logging_options)
        """
    def register_account(
        self,
        *,
        timestreamResources: "TimestreamResourcesTypeDef",
        iamResources: "IamResourcesTypeDef" = None
    ) -> RegisterAccountResponseTypeDef:
        """
        Registers your Amazon Web Services account, IAM, and Amazon Timestream resources
        so Amazon Web Services IoT FleetWise can transfer your vehicle data to the
        Amazon Web Services Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.register_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#register_account)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#untag_resource)
        """
    def update_campaign(
        self,
        *,
        name: str,
        action: UpdateCampaignActionType,
        description: str = None,
        dataExtraDimensions: List[str] = None
    ) -> UpdateCampaignResponseTypeDef:
        """
        Updates a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#update_campaign)
        """
    def update_decoder_manifest(
        self,
        *,
        name: str,
        description: str = None,
        signalDecodersToAdd: List["SignalDecoderTypeDef"] = None,
        signalDecodersToUpdate: List["SignalDecoderTypeDef"] = None,
        signalDecodersToRemove: List[str] = None,
        networkInterfacesToAdd: List["NetworkInterfaceTypeDef"] = None,
        networkInterfacesToUpdate: List["NetworkInterfaceTypeDef"] = None,
        networkInterfacesToRemove: List[str] = None,
        status: ManifestStatusType = None
    ) -> UpdateDecoderManifestResponseTypeDef:
        """
        Updates a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_decoder_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#update_decoder_manifest)
        """
    def update_fleet(self, *, fleetId: str, description: str = None) -> UpdateFleetResponseTypeDef:
        """
        Updates the description of an existing fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#update_fleet)
        """
    def update_model_manifest(
        self,
        *,
        name: str,
        description: str = None,
        nodesToAdd: List[str] = None,
        nodesToRemove: List[str] = None,
        status: ManifestStatusType = None
    ) -> UpdateModelManifestResponseTypeDef:
        """
        Updates a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_model_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#update_model_manifest)
        """
    def update_signal_catalog(
        self,
        *,
        name: str,
        description: str = None,
        nodesToAdd: List["NodeTypeDef"] = None,
        nodesToUpdate: List["NodeTypeDef"] = None,
        nodesToRemove: List[str] = None
    ) -> UpdateSignalCatalogResponseTypeDef:
        """
        Updates a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_signal_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#update_signal_catalog)
        """
    def update_vehicle(
        self,
        *,
        vehicleName: str,
        modelManifestArn: str = None,
        decoderManifestArn: str = None,
        attributes: Dict[str, str] = None,
        attributeUpdateMode: UpdateModeType = None
    ) -> UpdateVehicleResponseTypeDef:
        """
        Updates a vehicle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_vehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client.html#update_vehicle)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_vehicle_status"]
    ) -> GetVehicleStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.GetVehicleStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#getvehiclestatuspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_campaigns"]) -> ListCampaignsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListCampaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listcampaignspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_decoder_manifest_network_interfaces"]
    ) -> ListDecoderManifestNetworkInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestNetworkInterfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestnetworkinterfacespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_decoder_manifest_signals"]
    ) -> ListDecoderManifestSignalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestSignals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestsignalspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_decoder_manifests"]
    ) -> ListDecoderManifestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listdecodermanifestspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listfleetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_fleets_for_vehicle"]
    ) -> ListFleetsForVehiclePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleetsForVehicle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listfleetsforvehiclepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_manifest_nodes"]
    ) -> ListModelManifestNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifestNodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listmodelmanifestnodespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_manifests"]
    ) -> ListModelManifestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listmodelmanifestspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_signal_catalog_nodes"]
    ) -> ListSignalCatalogNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogNodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listsignalcatalognodespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_signal_catalogs"]
    ) -> ListSignalCatalogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listsignalcatalogspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_vehicles"]) -> ListVehiclesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehicles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listvehiclespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_vehicles_in_fleet"]
    ) -> ListVehiclesInFleetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehiclesInFleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators.html#listvehiclesinfleetpaginator)
        """
