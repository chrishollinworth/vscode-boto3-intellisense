"""
Type annotations for backup-gateway service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_backup_gateway.client import BackupGatewayClient

    session = Session()
    client: BackupGatewayClient = session.client("backup-gateway")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListGatewaysPaginator, ListHypervisorsPaginator, ListVirtualMachinesPaginator
from .type_defs import (
    AssociateGatewayToServerInputTypeDef,
    AssociateGatewayToServerOutputTypeDef,
    CreateGatewayInputTypeDef,
    CreateGatewayOutputTypeDef,
    DeleteGatewayInputTypeDef,
    DeleteGatewayOutputTypeDef,
    DeleteHypervisorInputTypeDef,
    DeleteHypervisorOutputTypeDef,
    DisassociateGatewayFromServerInputTypeDef,
    DisassociateGatewayFromServerOutputTypeDef,
    GetBandwidthRateLimitScheduleInputTypeDef,
    GetBandwidthRateLimitScheduleOutputTypeDef,
    GetGatewayInputTypeDef,
    GetGatewayOutputTypeDef,
    GetHypervisorInputTypeDef,
    GetHypervisorOutputTypeDef,
    GetHypervisorPropertyMappingsInputTypeDef,
    GetHypervisorPropertyMappingsOutputTypeDef,
    GetVirtualMachineInputTypeDef,
    GetVirtualMachineOutputTypeDef,
    ImportHypervisorConfigurationInputTypeDef,
    ImportHypervisorConfigurationOutputTypeDef,
    ListGatewaysInputTypeDef,
    ListGatewaysOutputTypeDef,
    ListHypervisorsInputTypeDef,
    ListHypervisorsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListVirtualMachinesInputTypeDef,
    ListVirtualMachinesOutputTypeDef,
    PutBandwidthRateLimitScheduleInputTypeDef,
    PutBandwidthRateLimitScheduleOutputTypeDef,
    PutHypervisorPropertyMappingsInputTypeDef,
    PutHypervisorPropertyMappingsOutputTypeDef,
    PutMaintenanceStartTimeInputTypeDef,
    PutMaintenanceStartTimeOutputTypeDef,
    StartVirtualMachinesMetadataSyncInputTypeDef,
    StartVirtualMachinesMetadataSyncOutputTypeDef,
    TagResourceInputTypeDef,
    TagResourceOutputTypeDef,
    TestHypervisorConfigurationInputTypeDef,
    UntagResourceInputTypeDef,
    UntagResourceOutputTypeDef,
    UpdateGatewayInformationInputTypeDef,
    UpdateGatewayInformationOutputTypeDef,
    UpdateGatewaySoftwareNowInputTypeDef,
    UpdateGatewaySoftwareNowOutputTypeDef,
    UpdateHypervisorInputTypeDef,
    UpdateHypervisorOutputTypeDef,
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

__all__ = ("BackupGatewayClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BackupGatewayClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway.html#BackupGateway.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BackupGatewayClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway.html#BackupGateway.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#generate_presigned_url)
        """

    def associate_gateway_to_server(
        self, **kwargs: Unpack[AssociateGatewayToServerInputTypeDef]
    ) -> AssociateGatewayToServerOutputTypeDef:
        """
        Associates a backup gateway with your server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/associate_gateway_to_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#associate_gateway_to_server)
        """

    def create_gateway(
        self, **kwargs: Unpack[CreateGatewayInputTypeDef]
    ) -> CreateGatewayOutputTypeDef:
        """
        Creates a backup gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/create_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#create_gateway)
        """

    def delete_gateway(
        self, **kwargs: Unpack[DeleteGatewayInputTypeDef]
    ) -> DeleteGatewayOutputTypeDef:
        """
        Deletes a backup gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/delete_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#delete_gateway)
        """

    def delete_hypervisor(
        self, **kwargs: Unpack[DeleteHypervisorInputTypeDef]
    ) -> DeleteHypervisorOutputTypeDef:
        """
        Deletes a hypervisor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/delete_hypervisor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#delete_hypervisor)
        """

    def disassociate_gateway_from_server(
        self, **kwargs: Unpack[DisassociateGatewayFromServerInputTypeDef]
    ) -> DisassociateGatewayFromServerOutputTypeDef:
        """
        Disassociates a backup gateway from the specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/disassociate_gateway_from_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#disassociate_gateway_from_server)
        """

    def get_bandwidth_rate_limit_schedule(
        self, **kwargs: Unpack[GetBandwidthRateLimitScheduleInputTypeDef]
    ) -> GetBandwidthRateLimitScheduleOutputTypeDef:
        """
        Retrieves the bandwidth rate limit schedule for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_bandwidth_rate_limit_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_bandwidth_rate_limit_schedule)
        """

    def get_gateway(self, **kwargs: Unpack[GetGatewayInputTypeDef]) -> GetGatewayOutputTypeDef:
        """
        By providing the ARN (Amazon Resource Name), this API returns the gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_gateway)
        """

    def get_hypervisor(
        self, **kwargs: Unpack[GetHypervisorInputTypeDef]
    ) -> GetHypervisorOutputTypeDef:
        """
        This action requests information about the specified hypervisor to which the
        gateway will connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_hypervisor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_hypervisor)
        """

    def get_hypervisor_property_mappings(
        self, **kwargs: Unpack[GetHypervisorPropertyMappingsInputTypeDef]
    ) -> GetHypervisorPropertyMappingsOutputTypeDef:
        """
        This action retrieves the property mappings for the specified hypervisor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_hypervisor_property_mappings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_hypervisor_property_mappings)
        """

    def get_virtual_machine(
        self, **kwargs: Unpack[GetVirtualMachineInputTypeDef]
    ) -> GetVirtualMachineOutputTypeDef:
        """
        By providing the ARN (Amazon Resource Name), this API returns the virtual
        machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_virtual_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_virtual_machine)
        """

    def import_hypervisor_configuration(
        self, **kwargs: Unpack[ImportHypervisorConfigurationInputTypeDef]
    ) -> ImportHypervisorConfigurationOutputTypeDef:
        """
        Connect to a hypervisor by importing its configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/import_hypervisor_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#import_hypervisor_configuration)
        """

    def list_gateways(
        self, **kwargs: Unpack[ListGatewaysInputTypeDef]
    ) -> ListGatewaysOutputTypeDef:
        """
        Lists backup gateways owned by an Amazon Web Services account in an Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/list_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#list_gateways)
        """

    def list_hypervisors(
        self, **kwargs: Unpack[ListHypervisorsInputTypeDef]
    ) -> ListHypervisorsOutputTypeDef:
        """
        Lists your hypervisors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/list_hypervisors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#list_hypervisors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags applied to the resource identified by its Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#list_tags_for_resource)
        """

    def list_virtual_machines(
        self, **kwargs: Unpack[ListVirtualMachinesInputTypeDef]
    ) -> ListVirtualMachinesOutputTypeDef:
        """
        Lists your virtual machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/list_virtual_machines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#list_virtual_machines)
        """

    def put_bandwidth_rate_limit_schedule(
        self, **kwargs: Unpack[PutBandwidthRateLimitScheduleInputTypeDef]
    ) -> PutBandwidthRateLimitScheduleOutputTypeDef:
        """
        This action sets the bandwidth rate limit schedule for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/put_bandwidth_rate_limit_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#put_bandwidth_rate_limit_schedule)
        """

    def put_hypervisor_property_mappings(
        self, **kwargs: Unpack[PutHypervisorPropertyMappingsInputTypeDef]
    ) -> PutHypervisorPropertyMappingsOutputTypeDef:
        """
        This action sets the property mappings for the specified hypervisor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/put_hypervisor_property_mappings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#put_hypervisor_property_mappings)
        """

    def put_maintenance_start_time(
        self, **kwargs: Unpack[PutMaintenanceStartTimeInputTypeDef]
    ) -> PutMaintenanceStartTimeOutputTypeDef:
        """
        Set the maintenance start time for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/put_maintenance_start_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#put_maintenance_start_time)
        """

    def start_virtual_machines_metadata_sync(
        self, **kwargs: Unpack[StartVirtualMachinesMetadataSyncInputTypeDef]
    ) -> StartVirtualMachinesMetadataSyncOutputTypeDef:
        """
        This action sends a request to sync metadata across the specified virtual
        machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/start_virtual_machines_metadata_sync.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#start_virtual_machines_metadata_sync)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> TagResourceOutputTypeDef:
        """
        Tag the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#tag_resource)
        """

    def test_hypervisor_configuration(
        self, **kwargs: Unpack[TestHypervisorConfigurationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Tests your hypervisor configuration to validate that backup gateway can connect
        with the hypervisor and its resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/test_hypervisor_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#test_hypervisor_configuration)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> UntagResourceOutputTypeDef:
        """
        Removes tags from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#untag_resource)
        """

    def update_gateway_information(
        self, **kwargs: Unpack[UpdateGatewayInformationInputTypeDef]
    ) -> UpdateGatewayInformationOutputTypeDef:
        """
        Updates a gateway's name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/update_gateway_information.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#update_gateway_information)
        """

    def update_gateway_software_now(
        self, **kwargs: Unpack[UpdateGatewaySoftwareNowInputTypeDef]
    ) -> UpdateGatewaySoftwareNowOutputTypeDef:
        """
        Updates the gateway virtual machine (VM) software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/update_gateway_software_now.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#update_gateway_software_now)
        """

    def update_hypervisor(
        self, **kwargs: Unpack[UpdateHypervisorInputTypeDef]
    ) -> UpdateHypervisorOutputTypeDef:
        """
        Updates a hypervisor metadata, including its host, username, and password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/update_hypervisor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#update_hypervisor)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gateways"]
    ) -> ListGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_hypervisors"]
    ) -> ListHypervisorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_virtual_machines"]
    ) -> ListVirtualMachinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client/#get_paginator)
        """
