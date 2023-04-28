"""
Type annotations for appconfig service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appconfig import AppConfigClient

    client: AppConfigClient = boto3.client("appconfig")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import ActionPointType, GrowthTypeType, ReplicateToType
from .type_defs import (
    ActionTypeDef,
    ApplicationResponseMetadataTypeDef,
    ApplicationsTypeDef,
    ConfigurationProfilesTypeDef,
    ConfigurationProfileTypeDef,
    ConfigurationTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentStrategyResponseMetadataTypeDef,
    DeploymentsTypeDef,
    DeploymentTypeDef,
    EnvironmentResponseMetadataTypeDef,
    EnvironmentsTypeDef,
    ExtensionAssociationsTypeDef,
    ExtensionAssociationTypeDef,
    ExtensionsTypeDef,
    ExtensionTypeDef,
    HostedConfigurationVersionsTypeDef,
    HostedConfigurationVersionTypeDef,
    MonitorTypeDef,
    ParameterTypeDef,
    ResourceTagsTypeDef,
    ValidatorTypeDef,
)

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

class AppConfigClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppConfigClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#close)
        """
    def create_application(
        self, *, Name: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> ApplicationResponseMetadataTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create_application)
        """
    def create_configuration_profile(
        self,
        *,
        ApplicationId: str,
        Name: str,
        LocationUri: str,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List["ValidatorTypeDef"] = None,
        Tags: Dict[str, str] = None,
        Type: str = None
    ) -> ConfigurationProfileTypeDef:
        """
        Creates a configuration profile, which is information that enables AppConfig to
        access the configuration source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.create_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create_configuration_profile)
        """
    def create_deployment_strategy(
        self,
        *,
        Name: str,
        DeploymentDurationInMinutes: int,
        GrowthFactor: float,
        Description: str = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthType: GrowthTypeType = None,
        ReplicateTo: ReplicateToType = None,
        Tags: Dict[str, str] = None
    ) -> DeploymentStrategyResponseMetadataTypeDef:
        """
        Creates a deployment strategy that defines important criteria for rolling out
        your configuration to the designated targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.create_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create_deployment_strategy)
        """
    def create_environment(
        self,
        *,
        ApplicationId: str,
        Name: str,
        Description: str = None,
        Monitors: List["MonitorTypeDef"] = None,
        Tags: Dict[str, str] = None
    ) -> EnvironmentResponseMetadataTypeDef:
        """
        Creates an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create_environment)
        """
    def create_extension(
        self,
        *,
        Name: str,
        Actions: Dict[ActionPointType, List["ActionTypeDef"]],
        Description: str = None,
        Parameters: Dict[str, "ParameterTypeDef"] = None,
        Tags: Dict[str, str] = None,
        LatestVersionNumber: int = None
    ) -> ExtensionTypeDef:
        """
        Creates an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.create_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create_extension)
        """
    def create_extension_association(
        self,
        *,
        ExtensionIdentifier: str,
        ResourceIdentifier: str,
        ExtensionVersionNumber: int = None,
        Parameters: Dict[str, str] = None,
        Tags: Dict[str, str] = None
    ) -> ExtensionAssociationTypeDef:
        """
        When you create an extension or configure an Amazon Web Services authored
        extension, you associate the extension with an AppConfig application,
        environment, or configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.create_extension_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create_extension_association)
        """
    def create_hosted_configuration_version(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Content: Union[bytes, IO[bytes], StreamingBody],
        ContentType: str,
        Description: str = None,
        LatestVersionNumber: int = None,
        VersionLabel: str = None
    ) -> HostedConfigurationVersionTypeDef:
        """
        Creates a new configuration in the AppConfig hosted configuration store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.create_hosted_configuration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create_hosted_configuration_version)
        """
    def delete_application(self, *, ApplicationId: str) -> None:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete_application)
        """
    def delete_configuration_profile(
        self, *, ApplicationId: str, ConfigurationProfileId: str
    ) -> None:
        """
        Deletes a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.delete_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete_configuration_profile)
        """
    def delete_deployment_strategy(self, *, DeploymentStrategyId: str) -> None:
        """
        Deletes a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.delete_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete_deployment_strategy)
        """
    def delete_environment(self, *, ApplicationId: str, EnvironmentId: str) -> None:
        """
        Deletes an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete_environment)
        """
    def delete_extension(self, *, ExtensionIdentifier: str, VersionNumber: int = None) -> None:
        """
        Deletes an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.delete_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete_extension)
        """
    def delete_extension_association(self, *, ExtensionAssociationId: str) -> None:
        """
        Deletes an extension association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.delete_extension_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete_extension_association)
        """
    def delete_hosted_configuration_version(
        self, *, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> None:
        """
        Deletes a version of a configuration from the AppConfig hosted configuration
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.delete_hosted_configuration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete_hosted_configuration_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#generate_presigned_url)
        """
    def get_application(self, *, ApplicationId: str) -> ApplicationResponseMetadataTypeDef:
        """
        Retrieves information about an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_application)
        """
    def get_configuration(
        self,
        *,
        Application: str,
        Environment: str,
        Configuration: str,
        ClientId: str,
        ClientConfigurationVersion: str = None
    ) -> ConfigurationTypeDef:
        """
        (Deprecated) Retrieves the latest deployed configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_configuration)
        """
    def get_configuration_profile(
        self, *, ApplicationId: str, ConfigurationProfileId: str
    ) -> ConfigurationProfileTypeDef:
        """
        Retrieves information about a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_configuration_profile)
        """
    def get_deployment(
        self, *, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        Retrieves information about a configuration deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_deployment)
        """
    def get_deployment_strategy(
        self, *, DeploymentStrategyId: str
    ) -> DeploymentStrategyResponseMetadataTypeDef:
        """
        Retrieves information about a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_deployment_strategy)
        """
    def get_environment(
        self, *, ApplicationId: str, EnvironmentId: str
    ) -> EnvironmentResponseMetadataTypeDef:
        """
        Retrieves information about an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_environment)
        """
    def get_extension(
        self, *, ExtensionIdentifier: str, VersionNumber: int = None
    ) -> ExtensionTypeDef:
        """
        Returns information about an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_extension)
        """
    def get_extension_association(
        self, *, ExtensionAssociationId: str
    ) -> ExtensionAssociationTypeDef:
        """
        Returns information about an AppConfig extension association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_extension_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_extension_association)
        """
    def get_hosted_configuration_version(
        self, *, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> HostedConfigurationVersionTypeDef:
        """
        Retrieves information about a specific configuration version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.get_hosted_configuration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get_hosted_configuration_version)
        """
    def list_applications(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ApplicationsTypeDef:
        """
        Lists all applications in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_applications)
        """
    def list_configuration_profiles(
        self, *, ApplicationId: str, MaxResults: int = None, NextToken: str = None, Type: str = None
    ) -> ConfigurationProfilesTypeDef:
        """
        Lists the configuration profiles for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_configuration_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_configuration_profiles)
        """
    def list_deployment_strategies(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DeploymentStrategiesTypeDef:
        """
        Lists deployment strategies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_deployment_strategies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_deployment_strategies)
        """
    def list_deployments(
        self,
        *,
        ApplicationId: str,
        EnvironmentId: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DeploymentsTypeDef:
        """
        Lists the deployments for an environment in descending deployment number order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_deployments)
        """
    def list_environments(
        self, *, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> EnvironmentsTypeDef:
        """
        Lists the environments for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_environments)
        """
    def list_extension_associations(
        self,
        *,
        ResourceIdentifier: str = None,
        ExtensionIdentifier: str = None,
        ExtensionVersionNumber: int = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ExtensionAssociationsTypeDef:
        """
        Lists all AppConfig extension associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_extension_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_extension_associations)
        """
    def list_extensions(
        self, *, MaxResults: int = None, NextToken: str = None, Name: str = None
    ) -> ExtensionsTypeDef:
        """
        Lists all custom and Amazon Web Services authored AppConfig extensions in the
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_extensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_extensions)
        """
    def list_hosted_configuration_versions(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        MaxResults: int = None,
        NextToken: str = None,
        VersionLabel: str = None
    ) -> HostedConfigurationVersionsTypeDef:
        """
        Lists configurations stored in the AppConfig hosted configuration store by
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_hosted_configuration_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_hosted_configuration_versions)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ResourceTagsTypeDef:
        """
        Retrieves the list of key-value tags assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list_tags_for_resource)
        """
    def start_deployment(
        self,
        *,
        ApplicationId: str,
        EnvironmentId: str,
        DeploymentStrategyId: str,
        ConfigurationProfileId: str,
        ConfigurationVersion: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
        KmsKeyIdentifier: str = None
    ) -> DeploymentTypeDef:
        """
        Starts a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.start_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#start_deployment)
        """
    def stop_deployment(
        self, *, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        Stops a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.stop_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#stop_deployment)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Assigns metadata to an AppConfig resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Deletes a tag key and value from an AppConfig resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#untag_resource)
        """
    def update_application(
        self, *, ApplicationId: str, Name: str = None, Description: str = None
    ) -> ApplicationResponseMetadataTypeDef:
        """
        Updates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update_application)
        """
    def update_configuration_profile(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Name: str = None,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List["ValidatorTypeDef"] = None
    ) -> ConfigurationProfileTypeDef:
        """
        Updates a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.update_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update_configuration_profile)
        """
    def update_deployment_strategy(
        self,
        *,
        DeploymentStrategyId: str,
        Description: str = None,
        DeploymentDurationInMinutes: int = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthFactor: float = None,
        GrowthType: GrowthTypeType = None
    ) -> DeploymentStrategyResponseMetadataTypeDef:
        """
        Updates a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.update_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update_deployment_strategy)
        """
    def update_environment(
        self,
        *,
        ApplicationId: str,
        EnvironmentId: str,
        Name: str = None,
        Description: str = None,
        Monitors: List["MonitorTypeDef"] = None
    ) -> EnvironmentResponseMetadataTypeDef:
        """
        Updates an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update_environment)
        """
    def update_extension(
        self,
        *,
        ExtensionIdentifier: str,
        Description: str = None,
        Actions: Dict[ActionPointType, List["ActionTypeDef"]] = None,
        Parameters: Dict[str, "ParameterTypeDef"] = None,
        VersionNumber: int = None
    ) -> ExtensionTypeDef:
        """
        Updates an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.update_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update_extension)
        """
    def update_extension_association(
        self, *, ExtensionAssociationId: str, Parameters: Dict[str, str] = None
    ) -> ExtensionAssociationTypeDef:
        """
        Updates an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.update_extension_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update_extension_association)
        """
    def validate_configuration(
        self, *, ApplicationId: str, ConfigurationProfileId: str, ConfigurationVersion: str
    ) -> None:
        """
        Uses the validators in a configuration profile to validate a configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/appconfig.html#AppConfig.Client.validate_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#validate_configuration)
        """
