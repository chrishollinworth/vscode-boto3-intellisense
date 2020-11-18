# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sms service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sms import SMSClient

    client: SMSClient = boto3.client("sms")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_sms.paginator import (
    GetConnectorsPaginator,
    GetReplicationJobsPaginator,
    GetReplicationRunsPaginator,
    GetServersPaginator,
    ListAppsPaginator,
)
from mypy_boto3_sms.type_defs import (
    AppValidationConfigurationTypeDef,
    CreateAppResponseTypeDef,
    CreateReplicationJobResponseTypeDef,
    GenerateChangeSetResponseTypeDef,
    GenerateTemplateResponseTypeDef,
    GetAppLaunchConfigurationResponseTypeDef,
    GetAppReplicationConfigurationResponseTypeDef,
    GetAppResponseTypeDef,
    GetAppValidationConfigurationResponseTypeDef,
    GetAppValidationOutputResponseTypeDef,
    GetConnectorsResponseTypeDef,
    GetReplicationJobsResponseTypeDef,
    GetReplicationRunsResponseTypeDef,
    GetServersResponseTypeDef,
    ListAppsResponseTypeDef,
    NotificationContextTypeDef,
    ServerGroupLaunchConfigurationTypeDef,
    ServerGroupReplicationConfigurationTypeDef,
    ServerGroupTypeDef,
    ServerGroupValidationConfigurationTypeDef,
    StartOnDemandReplicationRunResponseTypeDef,
    TagTypeDef,
    UpdateAppResponseTypeDef,
    VmServerAddressTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SMSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DryRunOperationException: Type[BotocoreClientError]
    InternalError: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    NoConnectorsAvailableException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    ReplicationJobAlreadyExistsException: Type[BotocoreClientError]
    ReplicationJobNotFoundException: Type[BotocoreClientError]
    ReplicationRunLimitExceededException: Type[BotocoreClientError]
    ServerCannotBeReplicatedException: Type[BotocoreClientError]
    TemporarilyUnavailableException: Type[BotocoreClientError]
    UnauthorizedOperationException: Type[BotocoreClientError]


class SMSClient:
    """
    [SMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.can_paginate)
        """

    def create_app(
        self,
        name: str = None,
        description: str = None,
        roleName: str = None,
        clientToken: str = None,
        serverGroups: List["ServerGroupTypeDef"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.create_app)
        """

    def create_replication_job(
        self,
        serverId: str,
        seedReplicationTime: datetime,
        frequency: int = None,
        runOnce: bool = None,
        licenseType: Literal["AWS", "BYOL"] = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None,
    ) -> CreateReplicationJobResponseTypeDef:
        """
        [Client.create_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.create_replication_job)
        """

    def delete_app(
        self,
        appId: str = None,
        forceStopAppReplication: bool = None,
        forceTerminateApp: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.delete_app)
        """

    def delete_app_launch_configuration(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.delete_app_launch_configuration)
        """

    def delete_app_replication_configuration(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.delete_app_replication_configuration)
        """

    def delete_app_validation_configuration(self, appId: str) -> Dict[str, Any]:
        """
        [Client.delete_app_validation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.delete_app_validation_configuration)
        """

    def delete_replication_job(self, replicationJobId: str) -> Dict[str, Any]:
        """
        [Client.delete_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.delete_replication_job)
        """

    def delete_server_catalog(self) -> Dict[str, Any]:
        """
        [Client.delete_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.delete_server_catalog)
        """

    def disassociate_connector(self, connectorId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.disassociate_connector)
        """

    def generate_change_set(
        self, appId: str = None, changesetFormat: Literal["JSON", "YAML"] = None
    ) -> GenerateChangeSetResponseTypeDef:
        """
        [Client.generate_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.generate_change_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.generate_presigned_url)
        """

    def generate_template(
        self, appId: str = None, templateFormat: Literal["JSON", "YAML"] = None
    ) -> GenerateTemplateResponseTypeDef:
        """
        [Client.generate_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.generate_template)
        """

    def get_app(self, appId: str = None) -> GetAppResponseTypeDef:
        """
        [Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_app)
        """

    def get_app_launch_configuration(
        self, appId: str = None
    ) -> GetAppLaunchConfigurationResponseTypeDef:
        """
        [Client.get_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_app_launch_configuration)
        """

    def get_app_replication_configuration(
        self, appId: str = None
    ) -> GetAppReplicationConfigurationResponseTypeDef:
        """
        [Client.get_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_app_replication_configuration)
        """

    def get_app_validation_configuration(
        self, appId: str
    ) -> GetAppValidationConfigurationResponseTypeDef:
        """
        [Client.get_app_validation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_app_validation_configuration)
        """

    def get_app_validation_output(self, appId: str) -> GetAppValidationOutputResponseTypeDef:
        """
        [Client.get_app_validation_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_app_validation_output)
        """

    def get_connectors(
        self, nextToken: str = None, maxResults: int = None
    ) -> GetConnectorsResponseTypeDef:
        """
        [Client.get_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_connectors)
        """

    def get_replication_jobs(
        self, replicationJobId: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetReplicationJobsResponseTypeDef:
        """
        [Client.get_replication_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_replication_jobs)
        """

    def get_replication_runs(
        self, replicationJobId: str, nextToken: str = None, maxResults: int = None
    ) -> GetReplicationRunsResponseTypeDef:
        """
        [Client.get_replication_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_replication_runs)
        """

    def get_servers(
        self,
        nextToken: str = None,
        maxResults: int = None,
        vmServerAddressList: List["VmServerAddressTypeDef"] = None,
    ) -> GetServersResponseTypeDef:
        """
        [Client.get_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.get_servers)
        """

    def import_app_catalog(self, roleName: str = None) -> Dict[str, Any]:
        """
        [Client.import_app_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.import_app_catalog)
        """

    def import_server_catalog(self) -> Dict[str, Any]:
        """
        [Client.import_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.import_server_catalog)
        """

    def launch_app(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.launch_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.launch_app)
        """

    def list_apps(
        self, appIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> ListAppsResponseTypeDef:
        """
        [Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.list_apps)
        """

    def notify_app_validation_output(
        self, appId: str, notificationContext: NotificationContextTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Client.notify_app_validation_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.notify_app_validation_output)
        """

    def put_app_launch_configuration(
        self,
        appId: str = None,
        roleName: str = None,
        autoLaunch: bool = None,
        serverGroupLaunchConfigurations: List["ServerGroupLaunchConfigurationTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.put_app_launch_configuration)
        """

    def put_app_replication_configuration(
        self,
        appId: str = None,
        serverGroupReplicationConfigurations: List[
            "ServerGroupReplicationConfigurationTypeDef"
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.put_app_replication_configuration)
        """

    def put_app_validation_configuration(
        self,
        appId: str,
        appValidationConfigurations: List["AppValidationConfigurationTypeDef"] = None,
        serverGroupValidationConfigurations: List[
            "ServerGroupValidationConfigurationTypeDef"
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_app_validation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.put_app_validation_configuration)
        """

    def start_app_replication(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.start_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.start_app_replication)
        """

    def start_on_demand_app_replication(
        self, appId: str, description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.start_on_demand_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.start_on_demand_app_replication)
        """

    def start_on_demand_replication_run(
        self, replicationJobId: str, description: str = None
    ) -> StartOnDemandReplicationRunResponseTypeDef:
        """
        [Client.start_on_demand_replication_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.start_on_demand_replication_run)
        """

    def stop_app_replication(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.stop_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.stop_app_replication)
        """

    def terminate_app(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.terminate_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.terminate_app)
        """

    def update_app(
        self,
        appId: str = None,
        name: str = None,
        description: str = None,
        roleName: str = None,
        serverGroups: List["ServerGroupTypeDef"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> UpdateAppResponseTypeDef:
        """
        [Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.update_app)
        """

    def update_replication_job(
        self,
        replicationJobId: str,
        frequency: int = None,
        nextReplicationRunStartTime: datetime = None,
        licenseType: Literal["AWS", "BYOL"] = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Client.update_replication_job)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_connectors"]) -> GetConnectorsPaginator:
        """
        [Paginator.GetConnectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetConnectors)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_replication_jobs"]
    ) -> GetReplicationJobsPaginator:
        """
        [Paginator.GetReplicationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetReplicationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_replication_runs"]
    ) -> GetReplicationRunsPaginator:
        """
        [Paginator.GetReplicationRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetReplicationRuns)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_servers"]) -> GetServersPaginator:
        """
        [Paginator.GetServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetServers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.ListApps)
        """
