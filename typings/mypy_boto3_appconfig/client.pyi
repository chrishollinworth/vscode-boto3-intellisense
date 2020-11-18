# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for appconfig service client

Usage::

    ```python
    import boto3
    from mypy_boto3_appconfig import AppConfigClient

    client: AppConfigClient = boto3.client("appconfig")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_appconfig.type_defs import (
    ApplicationsTypeDef,
    ApplicationTypeDef,
    ConfigurationProfilesTypeDef,
    ConfigurationProfileTypeDef,
    ConfigurationTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentStrategyTypeDef,
    DeploymentsTypeDef,
    DeploymentTypeDef,
    EnvironmentsTypeDef,
    EnvironmentTypeDef,
    HostedConfigurationVersionsTypeDef,
    HostedConfigurationVersionTypeDef,
    MonitorTypeDef,
    ResourceTagsTypeDef,
    ValidatorTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppConfigClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]


class AppConfigClient:
    """
    [AppConfig.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.can_paginate)
        """

    def create_application(
        self, Name: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> "ApplicationTypeDef":
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.create_application)
        """

    def create_configuration_profile(
        self,
        ApplicationId: str,
        Name: str,
        LocationUri: str,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List["ValidatorTypeDef"] = None,
        Tags: Dict[str, str] = None,
    ) -> ConfigurationProfileTypeDef:
        """
        [Client.create_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.create_configuration_profile)
        """

    def create_deployment_strategy(
        self,
        Name: str,
        DeploymentDurationInMinutes: int,
        GrowthFactor: float,
        ReplicateTo: Literal["NONE", "SSM_DOCUMENT"],
        Description: str = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthType: Literal["LINEAR", "EXPONENTIAL"] = None,
        Tags: Dict[str, str] = None,
    ) -> "DeploymentStrategyTypeDef":
        """
        [Client.create_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.create_deployment_strategy)
        """

    def create_environment(
        self,
        ApplicationId: str,
        Name: str,
        Description: str = None,
        Monitors: List["MonitorTypeDef"] = None,
        Tags: Dict[str, str] = None,
    ) -> "EnvironmentTypeDef":
        """
        [Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.create_environment)
        """

    def create_hosted_configuration_version(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Content: Union[bytes, IO[bytes]],
        ContentType: str,
        Description: str = None,
        LatestVersionNumber: int = None,
    ) -> HostedConfigurationVersionTypeDef:
        """
        [Client.create_hosted_configuration_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.create_hosted_configuration_version)
        """

    def delete_application(self, ApplicationId: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.delete_application)
        """

    def delete_configuration_profile(self, ApplicationId: str, ConfigurationProfileId: str) -> None:
        """
        [Client.delete_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.delete_configuration_profile)
        """

    def delete_deployment_strategy(self, DeploymentStrategyId: str) -> None:
        """
        [Client.delete_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.delete_deployment_strategy)
        """

    def delete_environment(self, ApplicationId: str, EnvironmentId: str) -> None:
        """
        [Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.delete_environment)
        """

    def delete_hosted_configuration_version(
        self, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> None:
        """
        [Client.delete_hosted_configuration_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.delete_hosted_configuration_version)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.generate_presigned_url)
        """

    def get_application(self, ApplicationId: str) -> "ApplicationTypeDef":
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.get_application)
        """

    def get_configuration(
        self,
        Application: str,
        Environment: str,
        Configuration: str,
        ClientId: str,
        ClientConfigurationVersion: str = None,
    ) -> ConfigurationTypeDef:
        """
        [Client.get_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.get_configuration)
        """

    def get_configuration_profile(
        self, ApplicationId: str, ConfigurationProfileId: str
    ) -> ConfigurationProfileTypeDef:
        """
        [Client.get_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.get_configuration_profile)
        """

    def get_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.get_deployment)
        """

    def get_deployment_strategy(self, DeploymentStrategyId: str) -> "DeploymentStrategyTypeDef":
        """
        [Client.get_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.get_deployment_strategy)
        """

    def get_environment(self, ApplicationId: str, EnvironmentId: str) -> "EnvironmentTypeDef":
        """
        [Client.get_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.get_environment)
        """

    def get_hosted_configuration_version(
        self, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> HostedConfigurationVersionTypeDef:
        """
        [Client.get_hosted_configuration_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.get_hosted_configuration_version)
        """

    def list_applications(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ApplicationsTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.list_applications)
        """

    def list_configuration_profiles(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ConfigurationProfilesTypeDef:
        """
        [Client.list_configuration_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.list_configuration_profiles)
        """

    def list_deployment_strategies(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DeploymentStrategiesTypeDef:
        """
        [Client.list_deployment_strategies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.list_deployment_strategies)
        """

    def list_deployments(
        self, ApplicationId: str, EnvironmentId: str, MaxResults: int = None, NextToken: str = None
    ) -> DeploymentsTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.list_deployments)
        """

    def list_environments(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> EnvironmentsTypeDef:
        """
        [Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.list_environments)
        """

    def list_hosted_configuration_versions(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> HostedConfigurationVersionsTypeDef:
        """
        [Client.list_hosted_configuration_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.list_hosted_configuration_versions)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ResourceTagsTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.list_tags_for_resource)
        """

    def start_deployment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        DeploymentStrategyId: str,
        ConfigurationProfileId: str,
        ConfigurationVersion: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> DeploymentTypeDef:
        """
        [Client.start_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.start_deployment)
        """

    def stop_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        [Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.stop_deployment)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.untag_resource)
        """

    def update_application(
        self, ApplicationId: str, Name: str = None, Description: str = None
    ) -> "ApplicationTypeDef":
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.update_application)
        """

    def update_configuration_profile(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Name: str = None,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List["ValidatorTypeDef"] = None,
    ) -> ConfigurationProfileTypeDef:
        """
        [Client.update_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.update_configuration_profile)
        """

    def update_deployment_strategy(
        self,
        DeploymentStrategyId: str,
        Description: str = None,
        DeploymentDurationInMinutes: int = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthFactor: float = None,
        GrowthType: Literal["LINEAR", "EXPONENTIAL"] = None,
    ) -> "DeploymentStrategyTypeDef":
        """
        [Client.update_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.update_deployment_strategy)
        """

    def update_environment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        Name: str = None,
        Description: str = None,
        Monitors: List["MonitorTypeDef"] = None,
    ) -> "EnvironmentTypeDef":
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.update_environment)
        """

    def validate_configuration(
        self, ApplicationId: str, ConfigurationProfileId: str, ConfigurationVersion: str
    ) -> None:
        """
        [Client.validate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appconfig.html#AppConfig.Client.validate_configuration)
        """
