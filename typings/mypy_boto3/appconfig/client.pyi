"""
Type annotations for appconfig service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appconfig.client import AppConfigClient

    session = Session()
    client: AppConfigClient = session.client("appconfig")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationsPaginator,
    ListConfigurationProfilesPaginator,
    ListDeploymentsPaginator,
    ListDeploymentStrategiesPaginator,
    ListEnvironmentsPaginator,
    ListExtensionAssociationsPaginator,
    ListExtensionsPaginator,
    ListHostedConfigurationVersionsPaginator,
)
from .type_defs import (
    AccountSettingsTypeDef,
    ApplicationResponseTypeDef,
    ApplicationsTypeDef,
    ConfigurationProfilesTypeDef,
    ConfigurationProfileTypeDef,
    ConfigurationTypeDef,
    CreateApplicationRequestTypeDef,
    CreateConfigurationProfileRequestTypeDef,
    CreateDeploymentStrategyRequestTypeDef,
    CreateEnvironmentRequestTypeDef,
    CreateExtensionAssociationRequestTypeDef,
    CreateExtensionRequestTypeDef,
    CreateHostedConfigurationVersionRequestTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteConfigurationProfileRequestTypeDef,
    DeleteDeploymentStrategyRequestTypeDef,
    DeleteEnvironmentRequestTypeDef,
    DeleteExtensionAssociationRequestTypeDef,
    DeleteExtensionRequestTypeDef,
    DeleteHostedConfigurationVersionRequestTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentStrategyResponseTypeDef,
    DeploymentsTypeDef,
    DeploymentTypeDef,
    EmptyResponseMetadataTypeDef,
    EnvironmentResponseTypeDef,
    EnvironmentsTypeDef,
    ExtensionAssociationsTypeDef,
    ExtensionAssociationTypeDef,
    ExtensionsTypeDef,
    ExtensionTypeDef,
    GetApplicationRequestTypeDef,
    GetConfigurationProfileRequestTypeDef,
    GetConfigurationRequestTypeDef,
    GetDeploymentRequestTypeDef,
    GetDeploymentStrategyRequestTypeDef,
    GetEnvironmentRequestTypeDef,
    GetExtensionAssociationRequestTypeDef,
    GetExtensionRequestTypeDef,
    GetHostedConfigurationVersionRequestTypeDef,
    HostedConfigurationVersionsTypeDef,
    HostedConfigurationVersionTypeDef,
    ListApplicationsRequestTypeDef,
    ListConfigurationProfilesRequestTypeDef,
    ListDeploymentsRequestTypeDef,
    ListDeploymentStrategiesRequestTypeDef,
    ListEnvironmentsRequestTypeDef,
    ListExtensionAssociationsRequestTypeDef,
    ListExtensionsRequestTypeDef,
    ListHostedConfigurationVersionsRequestTypeDef,
    ListTagsForResourceRequestTypeDef,
    ResourceTagsTypeDef,
    StartDeploymentRequestTypeDef,
    StopDeploymentRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccountSettingsRequestTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateConfigurationProfileRequestTypeDef,
    UpdateDeploymentStrategyRequestTypeDef,
    UpdateEnvironmentRequestTypeDef,
    UpdateExtensionAssociationRequestTypeDef,
    UpdateExtensionRequestTypeDef,
    ValidateConfigurationRequestTypeDef,
)
from .waiter import DeploymentCompleteWaiter, EnvironmentReadyForDeploymentWaiter

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("AppConfigClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]

class AppConfigClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppConfigClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#generate_presigned_url)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> ApplicationResponseTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#create_application)
        """

    def create_configuration_profile(
        self, **kwargs: Unpack[CreateConfigurationProfileRequestTypeDef]
    ) -> ConfigurationProfileTypeDef:
        """
        Creates a configuration profile, which is information that enables AppConfig to
        access the configuration source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/create_configuration_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#create_configuration_profile)
        """

    def create_deployment_strategy(
        self, **kwargs: Unpack[CreateDeploymentStrategyRequestTypeDef]
    ) -> DeploymentStrategyResponseTypeDef:
        """
        Creates a deployment strategy that defines important criteria for rolling out
        your configuration to the designated targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/create_deployment_strategy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#create_deployment_strategy)
        """

    def create_environment(
        self, **kwargs: Unpack[CreateEnvironmentRequestTypeDef]
    ) -> EnvironmentResponseTypeDef:
        """
        Creates an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/create_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#create_environment)
        """

    def create_extension(self, **kwargs: Unpack[CreateExtensionRequestTypeDef]) -> ExtensionTypeDef:
        """
        Creates an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/create_extension.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#create_extension)
        """

    def create_extension_association(
        self, **kwargs: Unpack[CreateExtensionAssociationRequestTypeDef]
    ) -> ExtensionAssociationTypeDef:
        """
        When you create an extension or configure an Amazon Web Services authored
        extension, you associate the extension with an AppConfig application,
        environment, or configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/create_extension_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#create_extension_association)
        """

    def create_hosted_configuration_version(
        self, **kwargs: Unpack[CreateHostedConfigurationVersionRequestTypeDef]
    ) -> HostedConfigurationVersionTypeDef:
        """
        Creates a new configuration in the AppConfig hosted configuration store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/create_hosted_configuration_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#create_hosted_configuration_version)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#delete_application)
        """

    def delete_configuration_profile(
        self, **kwargs: Unpack[DeleteConfigurationProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/delete_configuration_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#delete_configuration_profile)
        """

    def delete_deployment_strategy(
        self, **kwargs: Unpack[DeleteDeploymentStrategyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/delete_deployment_strategy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#delete_deployment_strategy)
        """

    def delete_environment(
        self, **kwargs: Unpack[DeleteEnvironmentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/delete_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#delete_environment)
        """

    def delete_extension(
        self, **kwargs: Unpack[DeleteExtensionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/delete_extension.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#delete_extension)
        """

    def delete_extension_association(
        self, **kwargs: Unpack[DeleteExtensionAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an extension association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/delete_extension_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#delete_extension_association)
        """

    def delete_hosted_configuration_version(
        self, **kwargs: Unpack[DeleteHostedConfigurationVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a version of a configuration from the AppConfig hosted configuration
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/delete_hosted_configuration_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#delete_hosted_configuration_version)
        """

    def get_account_settings(self) -> AccountSettingsTypeDef:
        """
        Returns information about the status of the <code>DeletionProtection</code>
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_account_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_account_settings)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> ApplicationResponseTypeDef:
        """
        Retrieves information about an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_application)
        """

    def get_configuration(
        self, **kwargs: Unpack[GetConfigurationRequestTypeDef]
    ) -> ConfigurationTypeDef:
        """
        (Deprecated) Retrieves the latest deployed configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_configuration)
        """

    def get_configuration_profile(
        self, **kwargs: Unpack[GetConfigurationProfileRequestTypeDef]
    ) -> ConfigurationProfileTypeDef:
        """
        Retrieves information about a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_configuration_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_configuration_profile)
        """

    def get_deployment(self, **kwargs: Unpack[GetDeploymentRequestTypeDef]) -> DeploymentTypeDef:
        """
        Retrieves information about a configuration deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_deployment)
        """

    def get_deployment_strategy(
        self, **kwargs: Unpack[GetDeploymentStrategyRequestTypeDef]
    ) -> DeploymentStrategyResponseTypeDef:
        """
        Retrieves information about a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_deployment_strategy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_deployment_strategy)
        """

    def get_environment(
        self, **kwargs: Unpack[GetEnvironmentRequestTypeDef]
    ) -> EnvironmentResponseTypeDef:
        """
        Retrieves information about an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_environment)
        """

    def get_extension(self, **kwargs: Unpack[GetExtensionRequestTypeDef]) -> ExtensionTypeDef:
        """
        Returns information about an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_extension.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_extension)
        """

    def get_extension_association(
        self, **kwargs: Unpack[GetExtensionAssociationRequestTypeDef]
    ) -> ExtensionAssociationTypeDef:
        """
        Returns information about an AppConfig extension association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_extension_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_extension_association)
        """

    def get_hosted_configuration_version(
        self, **kwargs: Unpack[GetHostedConfigurationVersionRequestTypeDef]
    ) -> HostedConfigurationVersionTypeDef:
        """
        Retrieves information about a specific configuration version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_hosted_configuration_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_hosted_configuration_version)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ApplicationsTypeDef:
        """
        Lists all applications in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_applications)
        """

    def list_configuration_profiles(
        self, **kwargs: Unpack[ListConfigurationProfilesRequestTypeDef]
    ) -> ConfigurationProfilesTypeDef:
        """
        Lists the configuration profiles for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_configuration_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_configuration_profiles)
        """

    def list_deployment_strategies(
        self, **kwargs: Unpack[ListDeploymentStrategiesRequestTypeDef]
    ) -> DeploymentStrategiesTypeDef:
        """
        Lists deployment strategies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_deployment_strategies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_deployment_strategies)
        """

    def list_deployments(
        self, **kwargs: Unpack[ListDeploymentsRequestTypeDef]
    ) -> DeploymentsTypeDef:
        """
        Lists the deployments for an environment in descending deployment number order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_deployments)
        """

    def list_environments(
        self, **kwargs: Unpack[ListEnvironmentsRequestTypeDef]
    ) -> EnvironmentsTypeDef:
        """
        Lists the environments for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_environments)
        """

    def list_extension_associations(
        self, **kwargs: Unpack[ListExtensionAssociationsRequestTypeDef]
    ) -> ExtensionAssociationsTypeDef:
        """
        Lists all AppConfig extension associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_extension_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_extension_associations)
        """

    def list_extensions(self, **kwargs: Unpack[ListExtensionsRequestTypeDef]) -> ExtensionsTypeDef:
        """
        Lists all custom and Amazon Web Services authored AppConfig extensions in the
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_extensions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_extensions)
        """

    def list_hosted_configuration_versions(
        self, **kwargs: Unpack[ListHostedConfigurationVersionsRequestTypeDef]
    ) -> HostedConfigurationVersionsTypeDef:
        """
        Lists configurations stored in the AppConfig hosted configuration store by
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_hosted_configuration_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_hosted_configuration_versions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ResourceTagsTypeDef:
        """
        Retrieves the list of key-value tags assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#list_tags_for_resource)
        """

    def start_deployment(
        self, **kwargs: Unpack[StartDeploymentRequestTypeDef]
    ) -> DeploymentTypeDef:
        """
        Starts a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/start_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#start_deployment)
        """

    def stop_deployment(self, **kwargs: Unpack[StopDeploymentRequestTypeDef]) -> DeploymentTypeDef:
        """
        Stops a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/stop_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#stop_deployment)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns metadata to an AppConfig resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a tag key and value from an AppConfig resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#untag_resource)
        """

    def update_account_settings(
        self, **kwargs: Unpack[UpdateAccountSettingsRequestTypeDef]
    ) -> AccountSettingsTypeDef:
        """
        Updates the value of the <code>DeletionProtection</code> parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/update_account_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#update_account_settings)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> ApplicationResponseTypeDef:
        """
        Updates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#update_application)
        """

    def update_configuration_profile(
        self, **kwargs: Unpack[UpdateConfigurationProfileRequestTypeDef]
    ) -> ConfigurationProfileTypeDef:
        """
        Updates a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/update_configuration_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#update_configuration_profile)
        """

    def update_deployment_strategy(
        self, **kwargs: Unpack[UpdateDeploymentStrategyRequestTypeDef]
    ) -> DeploymentStrategyResponseTypeDef:
        """
        Updates a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/update_deployment_strategy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#update_deployment_strategy)
        """

    def update_environment(
        self, **kwargs: Unpack[UpdateEnvironmentRequestTypeDef]
    ) -> EnvironmentResponseTypeDef:
        """
        Updates an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/update_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#update_environment)
        """

    def update_extension(self, **kwargs: Unpack[UpdateExtensionRequestTypeDef]) -> ExtensionTypeDef:
        """
        Updates an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/update_extension.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#update_extension)
        """

    def update_extension_association(
        self, **kwargs: Unpack[UpdateExtensionAssociationRequestTypeDef]
    ) -> ExtensionAssociationTypeDef:
        """
        Updates an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/update_extension_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#update_extension_association)
        """

    def validate_configuration(
        self, **kwargs: Unpack[ValidateConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Uses the validators in a configuration profile to validate a configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/validate_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#validate_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configuration_profiles"]
    ) -> ListConfigurationProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployment_strategies"]
    ) -> ListDeploymentStrategiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_extension_associations"]
    ) -> ListExtensionAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_extensions"]
    ) -> ListExtensionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_hosted_configuration_versions"]
    ) -> ListHostedConfigurationVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["deployment_complete"]
    ) -> DeploymentCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["environment_ready_for_deployment"]
    ) -> EnvironmentReadyForDeploymentWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client/#get_waiter)
        """
