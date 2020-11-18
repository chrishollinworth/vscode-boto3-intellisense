# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for greengrass service client

Usage::

    ```python
    import boto3
    from mypy_boto3_greengrass import GreengrassClient

    client: GreengrassClient = boto3.client("greengrass")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_greengrass.paginator import (
    ListBulkDeploymentDetailedReportsPaginator,
    ListBulkDeploymentsPaginator,
    ListConnectorDefinitionsPaginator,
    ListConnectorDefinitionVersionsPaginator,
    ListCoreDefinitionsPaginator,
    ListCoreDefinitionVersionsPaginator,
    ListDeploymentsPaginator,
    ListDeviceDefinitionsPaginator,
    ListDeviceDefinitionVersionsPaginator,
    ListFunctionDefinitionsPaginator,
    ListFunctionDefinitionVersionsPaginator,
    ListGroupsPaginator,
    ListGroupVersionsPaginator,
    ListLoggerDefinitionsPaginator,
    ListLoggerDefinitionVersionsPaginator,
    ListResourceDefinitionsPaginator,
    ListResourceDefinitionVersionsPaginator,
    ListSubscriptionDefinitionsPaginator,
    ListSubscriptionDefinitionVersionsPaginator,
)
from mypy_boto3_greengrass.type_defs import (
    AssociateRoleToGroupResponseTypeDef,
    AssociateServiceRoleToAccountResponseTypeDef,
    ConnectivityInfoTypeDef,
    ConnectorDefinitionVersionTypeDef,
    ConnectorTypeDef,
    CoreDefinitionVersionTypeDef,
    CoreTypeDef,
    CreateConnectorDefinitionResponseTypeDef,
    CreateConnectorDefinitionVersionResponseTypeDef,
    CreateCoreDefinitionResponseTypeDef,
    CreateCoreDefinitionVersionResponseTypeDef,
    CreateDeploymentResponseTypeDef,
    CreateDeviceDefinitionResponseTypeDef,
    CreateDeviceDefinitionVersionResponseTypeDef,
    CreateFunctionDefinitionResponseTypeDef,
    CreateFunctionDefinitionVersionResponseTypeDef,
    CreateGroupCertificateAuthorityResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateGroupVersionResponseTypeDef,
    CreateLoggerDefinitionResponseTypeDef,
    CreateLoggerDefinitionVersionResponseTypeDef,
    CreateResourceDefinitionResponseTypeDef,
    CreateResourceDefinitionVersionResponseTypeDef,
    CreateSoftwareUpdateJobResponseTypeDef,
    CreateSubscriptionDefinitionResponseTypeDef,
    CreateSubscriptionDefinitionVersionResponseTypeDef,
    DeviceDefinitionVersionTypeDef,
    DeviceTypeDef,
    DisassociateRoleFromGroupResponseTypeDef,
    DisassociateServiceRoleFromAccountResponseTypeDef,
    FunctionDefaultConfigTypeDef,
    FunctionDefinitionVersionTypeDef,
    FunctionTypeDef,
    GetAssociatedRoleResponseTypeDef,
    GetBulkDeploymentStatusResponseTypeDef,
    GetConnectivityInfoResponseTypeDef,
    GetConnectorDefinitionResponseTypeDef,
    GetConnectorDefinitionVersionResponseTypeDef,
    GetCoreDefinitionResponseTypeDef,
    GetCoreDefinitionVersionResponseTypeDef,
    GetDeploymentStatusResponseTypeDef,
    GetDeviceDefinitionResponseTypeDef,
    GetDeviceDefinitionVersionResponseTypeDef,
    GetFunctionDefinitionResponseTypeDef,
    GetFunctionDefinitionVersionResponseTypeDef,
    GetGroupCertificateAuthorityResponseTypeDef,
    GetGroupCertificateConfigurationResponseTypeDef,
    GetGroupResponseTypeDef,
    GetGroupVersionResponseTypeDef,
    GetLoggerDefinitionResponseTypeDef,
    GetLoggerDefinitionVersionResponseTypeDef,
    GetResourceDefinitionResponseTypeDef,
    GetResourceDefinitionVersionResponseTypeDef,
    GetServiceRoleForAccountResponseTypeDef,
    GetSubscriptionDefinitionResponseTypeDef,
    GetSubscriptionDefinitionVersionResponseTypeDef,
    GetThingRuntimeConfigurationResponseTypeDef,
    GroupVersionTypeDef,
    ListBulkDeploymentDetailedReportsResponseTypeDef,
    ListBulkDeploymentsResponseTypeDef,
    ListConnectorDefinitionsResponseTypeDef,
    ListConnectorDefinitionVersionsResponseTypeDef,
    ListCoreDefinitionsResponseTypeDef,
    ListCoreDefinitionVersionsResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListDeviceDefinitionsResponseTypeDef,
    ListDeviceDefinitionVersionsResponseTypeDef,
    ListFunctionDefinitionsResponseTypeDef,
    ListFunctionDefinitionVersionsResponseTypeDef,
    ListGroupCertificateAuthoritiesResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListGroupVersionsResponseTypeDef,
    ListLoggerDefinitionsResponseTypeDef,
    ListLoggerDefinitionVersionsResponseTypeDef,
    ListResourceDefinitionsResponseTypeDef,
    ListResourceDefinitionVersionsResponseTypeDef,
    ListSubscriptionDefinitionsResponseTypeDef,
    ListSubscriptionDefinitionVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggerDefinitionVersionTypeDef,
    LoggerTypeDef,
    ResetDeploymentsResponseTypeDef,
    ResourceDefinitionVersionTypeDef,
    ResourceTypeDef,
    StartBulkDeploymentResponseTypeDef,
    SubscriptionDefinitionVersionTypeDef,
    SubscriptionTypeDef,
    TelemetryConfigurationUpdateTypeDef,
    UpdateConnectivityInfoResponseTypeDef,
    UpdateGroupCertificateConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GreengrassClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]


class GreengrassClient:
    """
    [Greengrass.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_role_to_group(
        self, GroupId: str, RoleArn: str
    ) -> AssociateRoleToGroupResponseTypeDef:
        """
        [Client.associate_role_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.associate_role_to_group)
        """

    def associate_service_role_to_account(
        self, RoleArn: str
    ) -> AssociateServiceRoleToAccountResponseTypeDef:
        """
        [Client.associate_service_role_to_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.associate_service_role_to_account)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.can_paginate)
        """

    def create_connector_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "ConnectorDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateConnectorDefinitionResponseTypeDef:
        """
        [Client.create_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_connector_definition)
        """

    def create_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        AmznClientToken: str = None,
        Connectors: List["ConnectorTypeDef"] = None,
    ) -> CreateConnectorDefinitionVersionResponseTypeDef:
        """
        [Client.create_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_connector_definition_version)
        """

    def create_core_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "CoreDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateCoreDefinitionResponseTypeDef:
        """
        [Client.create_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_core_definition)
        """

    def create_core_definition_version(
        self, CoreDefinitionId: str, AmznClientToken: str = None, Cores: List["CoreTypeDef"] = None
    ) -> CreateCoreDefinitionVersionResponseTypeDef:
        """
        [Client.create_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_core_definition_version)
        """

    def create_deployment(
        self,
        DeploymentType: Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        GroupId: str,
        AmznClientToken: str = None,
        DeploymentId: str = None,
        GroupVersionId: str = None,
    ) -> CreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_deployment)
        """

    def create_device_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "DeviceDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateDeviceDefinitionResponseTypeDef:
        """
        [Client.create_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_device_definition)
        """

    def create_device_definition_version(
        self,
        DeviceDefinitionId: str,
        AmznClientToken: str = None,
        Devices: List["DeviceTypeDef"] = None,
    ) -> CreateDeviceDefinitionVersionResponseTypeDef:
        """
        [Client.create_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_device_definition_version)
        """

    def create_function_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "FunctionDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateFunctionDefinitionResponseTypeDef:
        """
        [Client.create_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_function_definition)
        """

    def create_function_definition_version(
        self,
        FunctionDefinitionId: str,
        AmznClientToken: str = None,
        DefaultConfig: "FunctionDefaultConfigTypeDef" = None,
        Functions: List["FunctionTypeDef"] = None,
    ) -> CreateFunctionDefinitionVersionResponseTypeDef:
        """
        [Client.create_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_function_definition_version)
        """

    def create_group(
        self,
        AmznClientToken: str = None,
        InitialVersion: "GroupVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_group)
        """

    def create_group_certificate_authority(
        self, GroupId: str, AmznClientToken: str = None
    ) -> CreateGroupCertificateAuthorityResponseTypeDef:
        """
        [Client.create_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_group_certificate_authority)
        """

    def create_group_version(
        self,
        GroupId: str,
        AmznClientToken: str = None,
        ConnectorDefinitionVersionArn: str = None,
        CoreDefinitionVersionArn: str = None,
        DeviceDefinitionVersionArn: str = None,
        FunctionDefinitionVersionArn: str = None,
        LoggerDefinitionVersionArn: str = None,
        ResourceDefinitionVersionArn: str = None,
        SubscriptionDefinitionVersionArn: str = None,
    ) -> CreateGroupVersionResponseTypeDef:
        """
        [Client.create_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_group_version)
        """

    def create_logger_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "LoggerDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateLoggerDefinitionResponseTypeDef:
        """
        [Client.create_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_logger_definition)
        """

    def create_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        AmznClientToken: str = None,
        Loggers: List["LoggerTypeDef"] = None,
    ) -> CreateLoggerDefinitionVersionResponseTypeDef:
        """
        [Client.create_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_logger_definition_version)
        """

    def create_resource_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "ResourceDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateResourceDefinitionResponseTypeDef:
        """
        [Client.create_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_resource_definition)
        """

    def create_resource_definition_version(
        self,
        ResourceDefinitionId: str,
        AmznClientToken: str = None,
        Resources: List["ResourceTypeDef"] = None,
    ) -> CreateResourceDefinitionVersionResponseTypeDef:
        """
        [Client.create_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_resource_definition_version)
        """

    def create_software_update_job(
        self,
        S3UrlSignerRole: str,
        SoftwareToUpdate: Literal["core", "ota_agent"],
        UpdateTargets: List[str],
        UpdateTargetsArchitecture: Literal["armv6l", "armv7l", "x86_64", "aarch64"],
        UpdateTargetsOperatingSystem: Literal["ubuntu", "raspbian", "amazon_linux", "openwrt"],
        AmznClientToken: str = None,
        UpdateAgentLogLevel: Literal[
            "NONE", "TRACE", "DEBUG", "VERBOSE", "INFO", "WARN", "ERROR", "FATAL"
        ] = None,
    ) -> CreateSoftwareUpdateJobResponseTypeDef:
        """
        [Client.create_software_update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_software_update_job)
        """

    def create_subscription_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "SubscriptionDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateSubscriptionDefinitionResponseTypeDef:
        """
        [Client.create_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition)
        """

    def create_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        AmznClientToken: str = None,
        Subscriptions: List["SubscriptionTypeDef"] = None,
    ) -> CreateSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Client.create_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition_version)
        """

    def delete_connector_definition(self, ConnectorDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_connector_definition)
        """

    def delete_core_definition(self, CoreDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_core_definition)
        """

    def delete_device_definition(self, DeviceDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_device_definition)
        """

    def delete_function_definition(self, FunctionDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_function_definition)
        """

    def delete_group(self, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_group)
        """

    def delete_logger_definition(self, LoggerDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_logger_definition)
        """

    def delete_resource_definition(self, ResourceDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_resource_definition)
        """

    def delete_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.delete_subscription_definition)
        """

    def disassociate_role_from_group(
        self, GroupId: str
    ) -> DisassociateRoleFromGroupResponseTypeDef:
        """
        [Client.disassociate_role_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.disassociate_role_from_group)
        """

    def disassociate_service_role_from_account(
        self,
    ) -> DisassociateServiceRoleFromAccountResponseTypeDef:
        """
        [Client.disassociate_service_role_from_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.disassociate_service_role_from_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.generate_presigned_url)
        """

    def get_associated_role(self, GroupId: str) -> GetAssociatedRoleResponseTypeDef:
        """
        [Client.get_associated_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_associated_role)
        """

    def get_bulk_deployment_status(
        self, BulkDeploymentId: str
    ) -> GetBulkDeploymentStatusResponseTypeDef:
        """
        [Client.get_bulk_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_bulk_deployment_status)
        """

    def get_connectivity_info(self, ThingName: str) -> GetConnectivityInfoResponseTypeDef:
        """
        [Client.get_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_connectivity_info)
        """

    def get_connector_definition(
        self, ConnectorDefinitionId: str
    ) -> GetConnectorDefinitionResponseTypeDef:
        """
        [Client.get_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_connector_definition)
        """

    def get_connector_definition_version(
        self, ConnectorDefinitionId: str, ConnectorDefinitionVersionId: str, NextToken: str = None
    ) -> GetConnectorDefinitionVersionResponseTypeDef:
        """
        [Client.get_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_connector_definition_version)
        """

    def get_core_definition(self, CoreDefinitionId: str) -> GetCoreDefinitionResponseTypeDef:
        """
        [Client.get_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_core_definition)
        """

    def get_core_definition_version(
        self, CoreDefinitionId: str, CoreDefinitionVersionId: str
    ) -> GetCoreDefinitionVersionResponseTypeDef:
        """
        [Client.get_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_core_definition_version)
        """

    def get_deployment_status(
        self, DeploymentId: str, GroupId: str
    ) -> GetDeploymentStatusResponseTypeDef:
        """
        [Client.get_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_deployment_status)
        """

    def get_device_definition(self, DeviceDefinitionId: str) -> GetDeviceDefinitionResponseTypeDef:
        """
        [Client.get_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_device_definition)
        """

    def get_device_definition_version(
        self, DeviceDefinitionId: str, DeviceDefinitionVersionId: str, NextToken: str = None
    ) -> GetDeviceDefinitionVersionResponseTypeDef:
        """
        [Client.get_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_device_definition_version)
        """

    def get_function_definition(
        self, FunctionDefinitionId: str
    ) -> GetFunctionDefinitionResponseTypeDef:
        """
        [Client.get_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_function_definition)
        """

    def get_function_definition_version(
        self, FunctionDefinitionId: str, FunctionDefinitionVersionId: str, NextToken: str = None
    ) -> GetFunctionDefinitionVersionResponseTypeDef:
        """
        [Client.get_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_function_definition_version)
        """

    def get_group(self, GroupId: str) -> GetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_group)
        """

    def get_group_certificate_authority(
        self, CertificateAuthorityId: str, GroupId: str
    ) -> GetGroupCertificateAuthorityResponseTypeDef:
        """
        [Client.get_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_authority)
        """

    def get_group_certificate_configuration(
        self, GroupId: str
    ) -> GetGroupCertificateConfigurationResponseTypeDef:
        """
        [Client.get_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_configuration)
        """

    def get_group_version(
        self, GroupId: str, GroupVersionId: str
    ) -> GetGroupVersionResponseTypeDef:
        """
        [Client.get_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_group_version)
        """

    def get_logger_definition(self, LoggerDefinitionId: str) -> GetLoggerDefinitionResponseTypeDef:
        """
        [Client.get_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_logger_definition)
        """

    def get_logger_definition_version(
        self, LoggerDefinitionId: str, LoggerDefinitionVersionId: str, NextToken: str = None
    ) -> GetLoggerDefinitionVersionResponseTypeDef:
        """
        [Client.get_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_logger_definition_version)
        """

    def get_resource_definition(
        self, ResourceDefinitionId: str
    ) -> GetResourceDefinitionResponseTypeDef:
        """
        [Client.get_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_resource_definition)
        """

    def get_resource_definition_version(
        self, ResourceDefinitionId: str, ResourceDefinitionVersionId: str
    ) -> GetResourceDefinitionVersionResponseTypeDef:
        """
        [Client.get_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_resource_definition_version)
        """

    def get_service_role_for_account(self) -> GetServiceRoleForAccountResponseTypeDef:
        """
        [Client.get_service_role_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_service_role_for_account)
        """

    def get_subscription_definition(
        self, SubscriptionDefinitionId: str
    ) -> GetSubscriptionDefinitionResponseTypeDef:
        """
        [Client.get_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition)
        """

    def get_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        SubscriptionDefinitionVersionId: str,
        NextToken: str = None,
    ) -> GetSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Client.get_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition_version)
        """

    def get_thing_runtime_configuration(
        self, ThingName: str
    ) -> GetThingRuntimeConfigurationResponseTypeDef:
        """
        [Client.get_thing_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.get_thing_runtime_configuration)
        """

    def list_bulk_deployment_detailed_reports(
        self, BulkDeploymentId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListBulkDeploymentDetailedReportsResponseTypeDef:
        """
        [Client.list_bulk_deployment_detailed_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployment_detailed_reports)
        """

    def list_bulk_deployments(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListBulkDeploymentsResponseTypeDef:
        """
        [Client.list_bulk_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployments)
        """

    def list_connector_definition_versions(
        self, ConnectorDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListConnectorDefinitionVersionsResponseTypeDef:
        """
        [Client.list_connector_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_connector_definition_versions)
        """

    def list_connector_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListConnectorDefinitionsResponseTypeDef:
        """
        [Client.list_connector_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_connector_definitions)
        """

    def list_core_definition_versions(
        self, CoreDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListCoreDefinitionVersionsResponseTypeDef:
        """
        [Client.list_core_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_core_definition_versions)
        """

    def list_core_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListCoreDefinitionsResponseTypeDef:
        """
        [Client.list_core_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_core_definitions)
        """

    def list_deployments(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListDeploymentsResponseTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_deployments)
        """

    def list_device_definition_versions(
        self, DeviceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListDeviceDefinitionVersionsResponseTypeDef:
        """
        [Client.list_device_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_device_definition_versions)
        """

    def list_device_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListDeviceDefinitionsResponseTypeDef:
        """
        [Client.list_device_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_device_definitions)
        """

    def list_function_definition_versions(
        self, FunctionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListFunctionDefinitionVersionsResponseTypeDef:
        """
        [Client.list_function_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_function_definition_versions)
        """

    def list_function_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListFunctionDefinitionsResponseTypeDef:
        """
        [Client.list_function_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_function_definitions)
        """

    def list_group_certificate_authorities(
        self, GroupId: str
    ) -> ListGroupCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_group_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_group_certificate_authorities)
        """

    def list_group_versions(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListGroupVersionsResponseTypeDef:
        """
        [Client.list_group_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_group_versions)
        """

    def list_groups(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_groups)
        """

    def list_logger_definition_versions(
        self, LoggerDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListLoggerDefinitionVersionsResponseTypeDef:
        """
        [Client.list_logger_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_logger_definition_versions)
        """

    def list_logger_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListLoggerDefinitionsResponseTypeDef:
        """
        [Client.list_logger_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_logger_definitions)
        """

    def list_resource_definition_versions(
        self, ResourceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListResourceDefinitionVersionsResponseTypeDef:
        """
        [Client.list_resource_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_resource_definition_versions)
        """

    def list_resource_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListResourceDefinitionsResponseTypeDef:
        """
        [Client.list_resource_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_resource_definitions)
        """

    def list_subscription_definition_versions(
        self, SubscriptionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListSubscriptionDefinitionVersionsResponseTypeDef:
        """
        [Client.list_subscription_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_subscription_definition_versions)
        """

    def list_subscription_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListSubscriptionDefinitionsResponseTypeDef:
        """
        [Client.list_subscription_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_subscription_definitions)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.list_tags_for_resource)
        """

    def reset_deployments(
        self, GroupId: str, AmznClientToken: str = None, Force: bool = None
    ) -> ResetDeploymentsResponseTypeDef:
        """
        [Client.reset_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.reset_deployments)
        """

    def start_bulk_deployment(
        self,
        ExecutionRoleArn: str,
        InputFileUri: str,
        AmznClientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> StartBulkDeploymentResponseTypeDef:
        """
        [Client.start_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.start_bulk_deployment)
        """

    def stop_bulk_deployment(self, BulkDeploymentId: str) -> Dict[str, Any]:
        """
        [Client.stop_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.stop_bulk_deployment)
        """

    def tag_resource(self, ResourceArn: str, tags: Dict[str, str] = None) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.untag_resource)
        """

    def update_connectivity_info(
        self, ThingName: str, ConnectivityInfo: List["ConnectivityInfoTypeDef"] = None
    ) -> UpdateConnectivityInfoResponseTypeDef:
        """
        [Client.update_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_connectivity_info)
        """

    def update_connector_definition(
        self, ConnectorDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_connector_definition)
        """

    def update_core_definition(self, CoreDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_core_definition)
        """

    def update_device_definition(self, DeviceDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_device_definition)
        """

    def update_function_definition(
        self, FunctionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_function_definition)
        """

    def update_group(self, GroupId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_group)
        """

    def update_group_certificate_configuration(
        self, GroupId: str, CertificateExpiryInMilliseconds: str = None
    ) -> UpdateGroupCertificateConfigurationResponseTypeDef:
        """
        [Client.update_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_group_certificate_configuration)
        """

    def update_logger_definition(self, LoggerDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_logger_definition)
        """

    def update_resource_definition(
        self, ResourceDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_resource_definition)
        """

    def update_subscription_definition(
        self, SubscriptionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_subscription_definition)
        """

    def update_thing_runtime_configuration(
        self, ThingName: str, TelemetryConfiguration: TelemetryConfigurationUpdateTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Client.update_thing_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Client.update_thing_runtime_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployment_detailed_reports"]
    ) -> ListBulkDeploymentDetailedReportsPaginator:
        """
        [Paginator.ListBulkDeploymentDetailedReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployments"]
    ) -> ListBulkDeploymentsPaginator:
        """
        [Paginator.ListBulkDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_connector_definition_versions"]
    ) -> ListConnectorDefinitionVersionsPaginator:
        """
        [Paginator.ListConnectorDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_connector_definitions"]
    ) -> ListConnectorDefinitionsPaginator:
        """
        [Paginator.ListConnectorDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_definition_versions"]
    ) -> ListCoreDefinitionVersionsPaginator:
        """
        [Paginator.ListCoreDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_definitions"]
    ) -> ListCoreDefinitionsPaginator:
        """
        [Paginator.ListCoreDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_definition_versions"]
    ) -> ListDeviceDefinitionVersionsPaginator:
        """
        [Paginator.ListDeviceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_definitions"]
    ) -> ListDeviceDefinitionsPaginator:
        """
        [Paginator.ListDeviceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_function_definition_versions"]
    ) -> ListFunctionDefinitionVersionsPaginator:
        """
        [Paginator.ListFunctionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_function_definitions"]
    ) -> ListFunctionDefinitionsPaginator:
        """
        [Paginator.ListFunctionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_versions"]
    ) -> ListGroupVersionsPaginator:
        """
        [Paginator.ListGroupVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_logger_definition_versions"]
    ) -> ListLoggerDefinitionVersionsPaginator:
        """
        [Paginator.ListLoggerDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_logger_definitions"]
    ) -> ListLoggerDefinitionsPaginator:
        """
        [Paginator.ListLoggerDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_definition_versions"]
    ) -> ListResourceDefinitionVersionsPaginator:
        """
        [Paginator.ListResourceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_definitions"]
    ) -> ListResourceDefinitionsPaginator:
        """
        [Paginator.ListResourceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_definition_versions"]
    ) -> ListSubscriptionDefinitionVersionsPaginator:
        """
        [Paginator.ListSubscriptionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_definitions"]
    ) -> ListSubscriptionDefinitionsPaginator:
        """
        [Paginator.ListSubscriptionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions)
        """
