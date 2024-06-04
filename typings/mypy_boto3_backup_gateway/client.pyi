"""
Type annotations for backup-gateway service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_backup_gateway import BackupGatewayClient

    client: BackupGatewayClient = boto3.client("backup-gateway")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListGatewaysPaginator, ListHypervisorsPaginator, ListVirtualMachinesPaginator
from .type_defs import (
    AssociateGatewayToServerOutputTypeDef,
    BandwidthRateLimitIntervalTypeDef,
    CreateGatewayOutputTypeDef,
    DeleteGatewayOutputTypeDef,
    DeleteHypervisorOutputTypeDef,
    DisassociateGatewayFromServerOutputTypeDef,
    GetBandwidthRateLimitScheduleOutputTypeDef,
    GetGatewayOutputTypeDef,
    GetHypervisorOutputTypeDef,
    GetHypervisorPropertyMappingsOutputTypeDef,
    GetVirtualMachineOutputTypeDef,
    ImportHypervisorConfigurationOutputTypeDef,
    ListGatewaysOutputTypeDef,
    ListHypervisorsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListVirtualMachinesOutputTypeDef,
    PutBandwidthRateLimitScheduleOutputTypeDef,
    PutHypervisorPropertyMappingsOutputTypeDef,
    PutMaintenanceStartTimeOutputTypeDef,
    StartVirtualMachinesMetadataSyncOutputTypeDef,
    TagResourceOutputTypeDef,
    TagTypeDef,
    UntagResourceOutputTypeDef,
    UpdateGatewayInformationOutputTypeDef,
    UpdateGatewaySoftwareNowOutputTypeDef,
    UpdateHypervisorOutputTypeDef,
    VmwareToAwsTagMappingTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BackupGatewayClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BackupGatewayClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BackupGatewayClient exceptions.
        """

    def associate_gateway_to_server(
        self, *, GatewayArn: str, ServerArn: str
    ) -> AssociateGatewayToServerOutputTypeDef:
        """
        Associates a backup gateway with your server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.associate_gateway_to_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#associate_gateway_to_server)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#close)
        """

    def create_gateway(
        self,
        *,
        ActivationKey: str,
        GatewayDisplayName: str,
        GatewayType: Literal["BACKUP_VM"],
        Tags: List["TagTypeDef"] = None
    ) -> CreateGatewayOutputTypeDef:
        """
        Creates a backup gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.create_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#create_gateway)
        """

    def delete_gateway(self, *, GatewayArn: str) -> DeleteGatewayOutputTypeDef:
        """
        Deletes a backup gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.delete_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#delete_gateway)
        """

    def delete_hypervisor(self, *, HypervisorArn: str) -> DeleteHypervisorOutputTypeDef:
        """
        Deletes a hypervisor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.delete_hypervisor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#delete_hypervisor)
        """

    def disassociate_gateway_from_server(
        self, *, GatewayArn: str
    ) -> DisassociateGatewayFromServerOutputTypeDef:
        """
        Disassociates a backup gateway from the specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.disassociate_gateway_from_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#disassociate_gateway_from_server)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#generate_presigned_url)
        """

    def get_bandwidth_rate_limit_schedule(
        self, *, GatewayArn: str
    ) -> GetBandwidthRateLimitScheduleOutputTypeDef:
        """
        Retrieves the bandwidth rate limit schedule for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.get_bandwidth_rate_limit_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#get_bandwidth_rate_limit_schedule)
        """

    def get_gateway(self, *, GatewayArn: str) -> GetGatewayOutputTypeDef:
        """
        By providing the ARN (Amazon Resource Name), this API returns the gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.get_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#get_gateway)
        """

    def get_hypervisor(self, *, HypervisorArn: str) -> GetHypervisorOutputTypeDef:
        """
        This action requests information about the specified hypervisor to which the
        gateway will connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.get_hypervisor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#get_hypervisor)
        """

    def get_hypervisor_property_mappings(
        self, *, HypervisorArn: str
    ) -> GetHypervisorPropertyMappingsOutputTypeDef:
        """
        This action retrieves the property mappings for the specified hypervisor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.get_hypervisor_property_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#get_hypervisor_property_mappings)
        """

    def get_virtual_machine(self, *, ResourceArn: str) -> GetVirtualMachineOutputTypeDef:
        """
        By providing the ARN (Amazon Resource Name), this API returns the virtual
        machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.get_virtual_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#get_virtual_machine)
        """

    def import_hypervisor_configuration(
        self,
        *,
        Host: str,
        Name: str,
        KmsKeyArn: str = None,
        Password: str = None,
        Tags: List["TagTypeDef"] = None,
        Username: str = None
    ) -> ImportHypervisorConfigurationOutputTypeDef:
        """
        Connect to a hypervisor by importing its configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.import_hypervisor_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#import_hypervisor_configuration)
        """

    def list_gateways(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListGatewaysOutputTypeDef:
        """
        Lists backup gateways owned by an Amazon Web Services account in an Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.list_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#list_gateways)
        """

    def list_hypervisors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListHypervisorsOutputTypeDef:
        """
        Lists your hypervisors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.list_hypervisors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#list_hypervisors)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags applied to the resource identified by its Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#list_tags_for_resource)
        """

    def list_virtual_machines(
        self, *, HypervisorArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListVirtualMachinesOutputTypeDef:
        """
        Lists your virtual machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.list_virtual_machines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#list_virtual_machines)
        """

    def put_bandwidth_rate_limit_schedule(
        self,
        *,
        BandwidthRateLimitIntervals: List["BandwidthRateLimitIntervalTypeDef"],
        GatewayArn: str
    ) -> PutBandwidthRateLimitScheduleOutputTypeDef:
        """
        This action sets the bandwidth rate limit schedule for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.put_bandwidth_rate_limit_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#put_bandwidth_rate_limit_schedule)
        """

    def put_hypervisor_property_mappings(
        self,
        *,
        HypervisorArn: str,
        IamRoleArn: str,
        VmwareToAwsTagMappings: List["VmwareToAwsTagMappingTypeDef"]
    ) -> PutHypervisorPropertyMappingsOutputTypeDef:
        """
        This action sets the property mappings for the specified hypervisor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.put_hypervisor_property_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#put_hypervisor_property_mappings)
        """

    def put_maintenance_start_time(
        self,
        *,
        GatewayArn: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfMonth: int = None,
        DayOfWeek: int = None
    ) -> PutMaintenanceStartTimeOutputTypeDef:
        """
        Set the maintenance start time for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.put_maintenance_start_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#put_maintenance_start_time)
        """

    def start_virtual_machines_metadata_sync(
        self, *, HypervisorArn: str
    ) -> StartVirtualMachinesMetadataSyncOutputTypeDef:
        """
        This action sends a request to sync metadata across the specified virtual
        machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.start_virtual_machines_metadata_sync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#start_virtual_machines_metadata_sync)
        """

    def tag_resource(
        self, *, ResourceARN: str, Tags: List["TagTypeDef"]
    ) -> TagResourceOutputTypeDef:
        """
        Tag the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#tag_resource)
        """

    def test_hypervisor_configuration(
        self, *, GatewayArn: str, Host: str, Password: str = None, Username: str = None
    ) -> Dict[str, Any]:
        """
        Tests your hypervisor configuration to validate that backup gateway can connect
        with the hypervisor and its resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.test_hypervisor_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#test_hypervisor_configuration)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> UntagResourceOutputTypeDef:
        """
        Removes tags from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#untag_resource)
        """

    def update_gateway_information(
        self, *, GatewayArn: str, GatewayDisplayName: str = None
    ) -> UpdateGatewayInformationOutputTypeDef:
        """
        Updates a gateway's name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.update_gateway_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#update_gateway_information)
        """

    def update_gateway_software_now(
        self, *, GatewayArn: str
    ) -> UpdateGatewaySoftwareNowOutputTypeDef:
        """
        Updates the gateway virtual machine (VM) software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.update_gateway_software_now)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#update_gateway_software_now)
        """

    def update_hypervisor(
        self,
        *,
        HypervisorArn: str,
        Host: str = None,
        LogGroupArn: str = None,
        Name: str = None,
        Password: str = None,
        Username: str = None
    ) -> UpdateHypervisorOutputTypeDef:
        """
        Updates a hypervisor metadata, including its host, username, and password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Client.update_hypervisor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/client.html#update_hypervisor)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Paginator.ListGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hypervisors"]
    ) -> ListHypervisorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Paginator.ListHypervisors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listhypervisorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_machines"]
    ) -> ListVirtualMachinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/backup-gateway.html#BackupGateway.Paginator.ListVirtualMachines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listvirtualmachinespaginator)
        """
