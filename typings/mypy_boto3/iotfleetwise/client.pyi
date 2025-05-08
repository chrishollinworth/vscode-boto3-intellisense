"""
Type annotations for iotfleetwise service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotfleetwise.client import IoTFleetWiseClient

    session = Session()
    client: IoTFleetWiseClient = session.client("iotfleetwise")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    ListStateTemplatesPaginator,
    ListVehiclesInFleetPaginator,
    ListVehiclesPaginator,
)
from .type_defs import (
    AssociateVehicleFleetRequestTypeDef,
    BatchCreateVehicleRequestTypeDef,
    BatchCreateVehicleResponseTypeDef,
    BatchUpdateVehicleRequestTypeDef,
    BatchUpdateVehicleResponseTypeDef,
    CreateCampaignRequestTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDecoderManifestRequestTypeDef,
    CreateDecoderManifestResponseTypeDef,
    CreateFleetRequestTypeDef,
    CreateFleetResponseTypeDef,
    CreateModelManifestRequestTypeDef,
    CreateModelManifestResponseTypeDef,
    CreateSignalCatalogRequestTypeDef,
    CreateSignalCatalogResponseTypeDef,
    CreateStateTemplateRequestTypeDef,
    CreateStateTemplateResponseTypeDef,
    CreateVehicleRequestTypeDef,
    CreateVehicleResponseTypeDef,
    DeleteCampaignRequestTypeDef,
    DeleteCampaignResponseTypeDef,
    DeleteDecoderManifestRequestTypeDef,
    DeleteDecoderManifestResponseTypeDef,
    DeleteFleetRequestTypeDef,
    DeleteFleetResponseTypeDef,
    DeleteModelManifestRequestTypeDef,
    DeleteModelManifestResponseTypeDef,
    DeleteSignalCatalogRequestTypeDef,
    DeleteSignalCatalogResponseTypeDef,
    DeleteStateTemplateRequestTypeDef,
    DeleteStateTemplateResponseTypeDef,
    DeleteVehicleRequestTypeDef,
    DeleteVehicleResponseTypeDef,
    DisassociateVehicleFleetRequestTypeDef,
    GetCampaignRequestTypeDef,
    GetCampaignResponseTypeDef,
    GetDecoderManifestRequestTypeDef,
    GetDecoderManifestResponseTypeDef,
    GetEncryptionConfigurationResponseTypeDef,
    GetFleetRequestTypeDef,
    GetFleetResponseTypeDef,
    GetLoggingOptionsResponseTypeDef,
    GetModelManifestRequestTypeDef,
    GetModelManifestResponseTypeDef,
    GetRegisterAccountStatusResponseTypeDef,
    GetSignalCatalogRequestTypeDef,
    GetSignalCatalogResponseTypeDef,
    GetStateTemplateRequestTypeDef,
    GetStateTemplateResponseTypeDef,
    GetVehicleRequestTypeDef,
    GetVehicleResponseTypeDef,
    GetVehicleStatusRequestTypeDef,
    GetVehicleStatusResponseTypeDef,
    ImportDecoderManifestRequestTypeDef,
    ImportDecoderManifestResponseTypeDef,
    ImportSignalCatalogRequestTypeDef,
    ImportSignalCatalogResponseTypeDef,
    ListCampaignsRequestTypeDef,
    ListCampaignsResponseTypeDef,
    ListDecoderManifestNetworkInterfacesRequestTypeDef,
    ListDecoderManifestNetworkInterfacesResponseTypeDef,
    ListDecoderManifestSignalsRequestTypeDef,
    ListDecoderManifestSignalsResponseTypeDef,
    ListDecoderManifestsRequestTypeDef,
    ListDecoderManifestsResponseTypeDef,
    ListFleetsForVehicleRequestTypeDef,
    ListFleetsForVehicleResponseTypeDef,
    ListFleetsRequestTypeDef,
    ListFleetsResponseTypeDef,
    ListModelManifestNodesRequestTypeDef,
    ListModelManifestNodesResponseTypeDef,
    ListModelManifestsRequestTypeDef,
    ListModelManifestsResponseTypeDef,
    ListSignalCatalogNodesRequestTypeDef,
    ListSignalCatalogNodesResponseTypeDef,
    ListSignalCatalogsRequestTypeDef,
    ListSignalCatalogsResponseTypeDef,
    ListStateTemplatesRequestTypeDef,
    ListStateTemplatesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVehiclesInFleetRequestTypeDef,
    ListVehiclesInFleetResponseTypeDef,
    ListVehiclesRequestTypeDef,
    ListVehiclesResponseTypeDef,
    PutEncryptionConfigurationRequestTypeDef,
    PutEncryptionConfigurationResponseTypeDef,
    PutLoggingOptionsRequestTypeDef,
    RegisterAccountRequestTypeDef,
    RegisterAccountResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCampaignRequestTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateDecoderManifestRequestTypeDef,
    UpdateDecoderManifestResponseTypeDef,
    UpdateFleetRequestTypeDef,
    UpdateFleetResponseTypeDef,
    UpdateModelManifestRequestTypeDef,
    UpdateModelManifestResponseTypeDef,
    UpdateSignalCatalogRequestTypeDef,
    UpdateSignalCatalogResponseTypeDef,
    UpdateStateTemplateRequestTypeDef,
    UpdateStateTemplateResponseTypeDef,
    UpdateVehicleRequestTypeDef,
    UpdateVehicleResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("IoTFleetWiseClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTFleetWiseClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#generate_presigned_url)
        """

    def associate_vehicle_fleet(
        self, **kwargs: Unpack[AssociateVehicleFleetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds, or associates, a vehicle with a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/associate_vehicle_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#associate_vehicle_fleet)
        """

    def batch_create_vehicle(
        self, **kwargs: Unpack[BatchCreateVehicleRequestTypeDef]
    ) -> BatchCreateVehicleResponseTypeDef:
        """
        Creates a group, or batch, of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/batch_create_vehicle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#batch_create_vehicle)
        """

    def batch_update_vehicle(
        self, **kwargs: Unpack[BatchUpdateVehicleRequestTypeDef]
    ) -> BatchUpdateVehicleResponseTypeDef:
        """
        Updates a group, or batch, of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/batch_update_vehicle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#batch_update_vehicle)
        """

    def create_campaign(
        self, **kwargs: Unpack[CreateCampaignRequestTypeDef]
    ) -> CreateCampaignResponseTypeDef:
        """
        Creates an orchestration of data collection rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/create_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#create_campaign)
        """

    def create_decoder_manifest(
        self, **kwargs: Unpack[CreateDecoderManifestRequestTypeDef]
    ) -> CreateDecoderManifestResponseTypeDef:
        """
        Creates the decoder manifest associated with a model manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/create_decoder_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#create_decoder_manifest)
        """

    def create_fleet(
        self, **kwargs: Unpack[CreateFleetRequestTypeDef]
    ) -> CreateFleetResponseTypeDef:
        """
        Creates a fleet that represents a group of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/create_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#create_fleet)
        """

    def create_model_manifest(
        self, **kwargs: Unpack[CreateModelManifestRequestTypeDef]
    ) -> CreateModelManifestResponseTypeDef:
        """
        Creates a vehicle model (model manifest) that specifies signals (attributes,
        branches, sensors, and actuators).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/create_model_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#create_model_manifest)
        """

    def create_signal_catalog(
        self, **kwargs: Unpack[CreateSignalCatalogRequestTypeDef]
    ) -> CreateSignalCatalogResponseTypeDef:
        """
        Creates a collection of standardized signals that can be reused to create
        vehicle models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/create_signal_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#create_signal_catalog)
        """

    def create_state_template(
        self, **kwargs: Unpack[CreateStateTemplateRequestTypeDef]
    ) -> CreateStateTemplateResponseTypeDef:
        """
        Creates a state template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/create_state_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#create_state_template)
        """

    def create_vehicle(
        self, **kwargs: Unpack[CreateVehicleRequestTypeDef]
    ) -> CreateVehicleResponseTypeDef:
        """
        Creates a vehicle, which is an instance of a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/create_vehicle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#create_vehicle)
        """

    def delete_campaign(
        self, **kwargs: Unpack[DeleteCampaignRequestTypeDef]
    ) -> DeleteCampaignResponseTypeDef:
        """
        Deletes a data collection campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/delete_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#delete_campaign)
        """

    def delete_decoder_manifest(
        self, **kwargs: Unpack[DeleteDecoderManifestRequestTypeDef]
    ) -> DeleteDecoderManifestResponseTypeDef:
        """
        Deletes a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/delete_decoder_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#delete_decoder_manifest)
        """

    def delete_fleet(
        self, **kwargs: Unpack[DeleteFleetRequestTypeDef]
    ) -> DeleteFleetResponseTypeDef:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/delete_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#delete_fleet)
        """

    def delete_model_manifest(
        self, **kwargs: Unpack[DeleteModelManifestRequestTypeDef]
    ) -> DeleteModelManifestResponseTypeDef:
        """
        Deletes a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/delete_model_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#delete_model_manifest)
        """

    def delete_signal_catalog(
        self, **kwargs: Unpack[DeleteSignalCatalogRequestTypeDef]
    ) -> DeleteSignalCatalogResponseTypeDef:
        """
        Deletes a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/delete_signal_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#delete_signal_catalog)
        """

    def delete_state_template(
        self, **kwargs: Unpack[DeleteStateTemplateRequestTypeDef]
    ) -> DeleteStateTemplateResponseTypeDef:
        """
        Deletes a state template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/delete_state_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#delete_state_template)
        """

    def delete_vehicle(
        self, **kwargs: Unpack[DeleteVehicleRequestTypeDef]
    ) -> DeleteVehicleResponseTypeDef:
        """
        Deletes a vehicle and removes it from any campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/delete_vehicle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#delete_vehicle)
        """

    def disassociate_vehicle_fleet(
        self, **kwargs: Unpack[DisassociateVehicleFleetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes, or disassociates, a vehicle from a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/disassociate_vehicle_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#disassociate_vehicle_fleet)
        """

    def get_campaign(
        self, **kwargs: Unpack[GetCampaignRequestTypeDef]
    ) -> GetCampaignResponseTypeDef:
        """
        Retrieves information about a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_campaign)
        """

    def get_decoder_manifest(
        self, **kwargs: Unpack[GetDecoderManifestRequestTypeDef]
    ) -> GetDecoderManifestResponseTypeDef:
        """
        Retrieves information about a created decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_decoder_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_decoder_manifest)
        """

    def get_encryption_configuration(self) -> GetEncryptionConfigurationResponseTypeDef:
        """
        Retrieves the encryption configuration for resources and data in Amazon Web
        Services IoT FleetWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_encryption_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_encryption_configuration)
        """

    def get_fleet(self, **kwargs: Unpack[GetFleetRequestTypeDef]) -> GetFleetResponseTypeDef:
        """
        Retrieves information about a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_fleet)
        """

    def get_logging_options(self) -> GetLoggingOptionsResponseTypeDef:
        """
        Retrieves the logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_logging_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_logging_options)
        """

    def get_model_manifest(
        self, **kwargs: Unpack[GetModelManifestRequestTypeDef]
    ) -> GetModelManifestResponseTypeDef:
        """
        Retrieves information about a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_model_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_model_manifest)
        """

    def get_register_account_status(self) -> GetRegisterAccountStatusResponseTypeDef:
        """
        Retrieves information about the status of registering your Amazon Web Services
        account, IAM, and Amazon Timestream resources so that Amazon Web Services IoT
        FleetWise can transfer your vehicle data to the Amazon Web Services Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_register_account_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_register_account_status)
        """

    def get_signal_catalog(
        self, **kwargs: Unpack[GetSignalCatalogRequestTypeDef]
    ) -> GetSignalCatalogResponseTypeDef:
        """
        Retrieves information about a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_signal_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_signal_catalog)
        """

    def get_state_template(
        self, **kwargs: Unpack[GetStateTemplateRequestTypeDef]
    ) -> GetStateTemplateResponseTypeDef:
        """
        Retrieves information about a state template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_state_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_state_template)
        """

    def get_vehicle(self, **kwargs: Unpack[GetVehicleRequestTypeDef]) -> GetVehicleResponseTypeDef:
        """
        Retrieves information about a vehicle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_vehicle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_vehicle)
        """

    def get_vehicle_status(
        self, **kwargs: Unpack[GetVehicleStatusRequestTypeDef]
    ) -> GetVehicleStatusResponseTypeDef:
        """
        Retrieves information about the status of campaigns, decoder manifests, or
        state templates associated with a vehicle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_vehicle_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_vehicle_status)
        """

    def import_decoder_manifest(
        self, **kwargs: Unpack[ImportDecoderManifestRequestTypeDef]
    ) -> ImportDecoderManifestResponseTypeDef:
        """
        Creates a decoder manifest using your existing CAN DBC file from your local
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/import_decoder_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#import_decoder_manifest)
        """

    def import_signal_catalog(
        self, **kwargs: Unpack[ImportSignalCatalogRequestTypeDef]
    ) -> ImportSignalCatalogResponseTypeDef:
        """
        Creates a signal catalog using your existing VSS formatted content from your
        local device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/import_signal_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#import_signal_catalog)
        """

    def list_campaigns(
        self, **kwargs: Unpack[ListCampaignsRequestTypeDef]
    ) -> ListCampaignsResponseTypeDef:
        """
        Lists information about created campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_campaigns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_campaigns)
        """

    def list_decoder_manifest_network_interfaces(
        self, **kwargs: Unpack[ListDecoderManifestNetworkInterfacesRequestTypeDef]
    ) -> ListDecoderManifestNetworkInterfacesResponseTypeDef:
        """
        Lists the network interfaces specified in a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_decoder_manifest_network_interfaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_decoder_manifest_network_interfaces)
        """

    def list_decoder_manifest_signals(
        self, **kwargs: Unpack[ListDecoderManifestSignalsRequestTypeDef]
    ) -> ListDecoderManifestSignalsResponseTypeDef:
        """
        A list of information about signal decoders specified in a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_decoder_manifest_signals.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_decoder_manifest_signals)
        """

    def list_decoder_manifests(
        self, **kwargs: Unpack[ListDecoderManifestsRequestTypeDef]
    ) -> ListDecoderManifestsResponseTypeDef:
        """
        Lists decoder manifests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_decoder_manifests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_decoder_manifests)
        """

    def list_fleets(self, **kwargs: Unpack[ListFleetsRequestTypeDef]) -> ListFleetsResponseTypeDef:
        """
        Retrieves information for each created fleet in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_fleets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_fleets)
        """

    def list_fleets_for_vehicle(
        self, **kwargs: Unpack[ListFleetsForVehicleRequestTypeDef]
    ) -> ListFleetsForVehicleResponseTypeDef:
        """
        Retrieves a list of IDs for all fleets that the vehicle is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_fleets_for_vehicle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_fleets_for_vehicle)
        """

    def list_model_manifest_nodes(
        self, **kwargs: Unpack[ListModelManifestNodesRequestTypeDef]
    ) -> ListModelManifestNodesResponseTypeDef:
        """
        Lists information about nodes specified in a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_model_manifest_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_model_manifest_nodes)
        """

    def list_model_manifests(
        self, **kwargs: Unpack[ListModelManifestsRequestTypeDef]
    ) -> ListModelManifestsResponseTypeDef:
        """
        Retrieves a list of vehicle models (model manifests).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_model_manifests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_model_manifests)
        """

    def list_signal_catalog_nodes(
        self, **kwargs: Unpack[ListSignalCatalogNodesRequestTypeDef]
    ) -> ListSignalCatalogNodesResponseTypeDef:
        """
        Lists of information about the signals (nodes) specified in a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_signal_catalog_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_signal_catalog_nodes)
        """

    def list_signal_catalogs(
        self, **kwargs: Unpack[ListSignalCatalogsRequestTypeDef]
    ) -> ListSignalCatalogsResponseTypeDef:
        """
        Lists all the created signal catalogs in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_signal_catalogs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_signal_catalogs)
        """

    def list_state_templates(
        self, **kwargs: Unpack[ListStateTemplatesRequestTypeDef]
    ) -> ListStateTemplatesResponseTypeDef:
        """
        Lists information about created state templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_state_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_state_templates)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_tags_for_resource)
        """

    def list_vehicles(
        self, **kwargs: Unpack[ListVehiclesRequestTypeDef]
    ) -> ListVehiclesResponseTypeDef:
        """
        Retrieves a list of summaries of created vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_vehicles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_vehicles)
        """

    def list_vehicles_in_fleet(
        self, **kwargs: Unpack[ListVehiclesInFleetRequestTypeDef]
    ) -> ListVehiclesInFleetResponseTypeDef:
        """
        Retrieves a list of summaries of all vehicles associated with a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/list_vehicles_in_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#list_vehicles_in_fleet)
        """

    def put_encryption_configuration(
        self, **kwargs: Unpack[PutEncryptionConfigurationRequestTypeDef]
    ) -> PutEncryptionConfigurationResponseTypeDef:
        """
        Creates or updates the encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/put_encryption_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#put_encryption_configuration)
        """

    def put_logging_options(
        self, **kwargs: Unpack[PutLoggingOptionsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates or updates the logging option.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/put_logging_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#put_logging_options)
        """

    def register_account(
        self, **kwargs: Unpack[RegisterAccountRequestTypeDef]
    ) -> RegisterAccountResponseTypeDef:
        """
        This API operation contains deprecated parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/register_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#register_account)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#untag_resource)
        """

    def update_campaign(
        self, **kwargs: Unpack[UpdateCampaignRequestTypeDef]
    ) -> UpdateCampaignResponseTypeDef:
        """
        Updates a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/update_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#update_campaign)
        """

    def update_decoder_manifest(
        self, **kwargs: Unpack[UpdateDecoderManifestRequestTypeDef]
    ) -> UpdateDecoderManifestResponseTypeDef:
        """
        Updates a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/update_decoder_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#update_decoder_manifest)
        """

    def update_fleet(
        self, **kwargs: Unpack[UpdateFleetRequestTypeDef]
    ) -> UpdateFleetResponseTypeDef:
        """
        Updates the description of an existing fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/update_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#update_fleet)
        """

    def update_model_manifest(
        self, **kwargs: Unpack[UpdateModelManifestRequestTypeDef]
    ) -> UpdateModelManifestResponseTypeDef:
        """
        Updates a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/update_model_manifest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#update_model_manifest)
        """

    def update_signal_catalog(
        self, **kwargs: Unpack[UpdateSignalCatalogRequestTypeDef]
    ) -> UpdateSignalCatalogResponseTypeDef:
        """
        Updates a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/update_signal_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#update_signal_catalog)
        """

    def update_state_template(
        self, **kwargs: Unpack[UpdateStateTemplateRequestTypeDef]
    ) -> UpdateStateTemplateResponseTypeDef:
        """
        Updates a state template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/update_state_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#update_state_template)
        """

    def update_vehicle(
        self, **kwargs: Unpack[UpdateVehicleRequestTypeDef]
    ) -> UpdateVehicleResponseTypeDef:
        """
        Updates a vehicle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/update_vehicle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#update_vehicle)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_vehicle_status"]
    ) -> GetVehicleStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_campaigns"]
    ) -> ListCampaignsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_decoder_manifest_network_interfaces"]
    ) -> ListDecoderManifestNetworkInterfacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_decoder_manifest_signals"]
    ) -> ListDecoderManifestSignalsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_decoder_manifests"]
    ) -> ListDecoderManifestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_fleets_for_vehicle"]
    ) -> ListFleetsForVehiclePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_fleets"]
    ) -> ListFleetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_model_manifest_nodes"]
    ) -> ListModelManifestNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_model_manifests"]
    ) -> ListModelManifestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signal_catalog_nodes"]
    ) -> ListSignalCatalogNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signal_catalogs"]
    ) -> ListSignalCatalogsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_state_templates"]
    ) -> ListStateTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_vehicles_in_fleet"]
    ) -> ListVehiclesInFleetPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_vehicles"]
    ) -> ListVehiclesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/client/#get_paginator)
        """
