"""
Type annotations for proton service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_proton import ProtonClient

    client: ProtonClient = boto3.client("proton")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ComponentDeploymentUpdateTypeType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ListServiceInstancesSortByType,
    RepositoryProviderType,
    ResourceDeploymentStatusType,
    SortOrderType,
    SyncTypeType,
    TemplateTypeType,
    TemplateVersionStatusType,
)
from .paginator import (
    ListComponentOutputsPaginator,
    ListComponentProvisionedResourcesPaginator,
    ListComponentsPaginator,
    ListEnvironmentAccountConnectionsPaginator,
    ListEnvironmentOutputsPaginator,
    ListEnvironmentProvisionedResourcesPaginator,
    ListEnvironmentsPaginator,
    ListEnvironmentTemplatesPaginator,
    ListEnvironmentTemplateVersionsPaginator,
    ListRepositoriesPaginator,
    ListRepositorySyncDefinitionsPaginator,
    ListServiceInstanceOutputsPaginator,
    ListServiceInstanceProvisionedResourcesPaginator,
    ListServiceInstancesPaginator,
    ListServicePipelineOutputsPaginator,
    ListServicePipelineProvisionedResourcesPaginator,
    ListServicesPaginator,
    ListServiceTemplatesPaginator,
    ListServiceTemplateVersionsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AcceptEnvironmentAccountConnectionOutputTypeDef,
    CancelComponentDeploymentOutputTypeDef,
    CancelEnvironmentDeploymentOutputTypeDef,
    CancelServiceInstanceDeploymentOutputTypeDef,
    CancelServicePipelineDeploymentOutputTypeDef,
    CompatibleEnvironmentTemplateInputTypeDef,
    CreateComponentOutputTypeDef,
    CreateEnvironmentAccountConnectionOutputTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateEnvironmentTemplateOutputTypeDef,
    CreateEnvironmentTemplateVersionOutputTypeDef,
    CreateRepositoryOutputTypeDef,
    CreateServiceInstanceOutputTypeDef,
    CreateServiceOutputTypeDef,
    CreateServiceSyncConfigOutputTypeDef,
    CreateServiceTemplateOutputTypeDef,
    CreateServiceTemplateVersionOutputTypeDef,
    CreateTemplateSyncConfigOutputTypeDef,
    DeleteComponentOutputTypeDef,
    DeleteEnvironmentAccountConnectionOutputTypeDef,
    DeleteEnvironmentOutputTypeDef,
    DeleteEnvironmentTemplateOutputTypeDef,
    DeleteEnvironmentTemplateVersionOutputTypeDef,
    DeleteRepositoryOutputTypeDef,
    DeleteServiceOutputTypeDef,
    DeleteServiceSyncConfigOutputTypeDef,
    DeleteServiceTemplateOutputTypeDef,
    DeleteServiceTemplateVersionOutputTypeDef,
    DeleteTemplateSyncConfigOutputTypeDef,
    EnvironmentTemplateFilterTypeDef,
    GetAccountSettingsOutputTypeDef,
    GetComponentOutputTypeDef,
    GetEnvironmentAccountConnectionOutputTypeDef,
    GetEnvironmentOutputTypeDef,
    GetEnvironmentTemplateOutputTypeDef,
    GetEnvironmentTemplateVersionOutputTypeDef,
    GetRepositoryOutputTypeDef,
    GetRepositorySyncStatusOutputTypeDef,
    GetResourcesSummaryOutputTypeDef,
    GetServiceInstanceOutputTypeDef,
    GetServiceInstanceSyncStatusOutputTypeDef,
    GetServiceOutputTypeDef,
    GetServiceSyncBlockerSummaryOutputTypeDef,
    GetServiceSyncConfigOutputTypeDef,
    GetServiceTemplateOutputTypeDef,
    GetServiceTemplateVersionOutputTypeDef,
    GetTemplateSyncConfigOutputTypeDef,
    GetTemplateSyncStatusOutputTypeDef,
    ListComponentOutputsOutputTypeDef,
    ListComponentProvisionedResourcesOutputTypeDef,
    ListComponentsOutputTypeDef,
    ListEnvironmentAccountConnectionsOutputTypeDef,
    ListEnvironmentOutputsOutputTypeDef,
    ListEnvironmentProvisionedResourcesOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListEnvironmentTemplatesOutputTypeDef,
    ListEnvironmentTemplateVersionsOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    ListRepositorySyncDefinitionsOutputTypeDef,
    ListServiceInstanceOutputsOutputTypeDef,
    ListServiceInstanceProvisionedResourcesOutputTypeDef,
    ListServiceInstancesFilterTypeDef,
    ListServiceInstancesOutputTypeDef,
    ListServicePipelineOutputsOutputTypeDef,
    ListServicePipelineProvisionedResourcesOutputTypeDef,
    ListServicesOutputTypeDef,
    ListServiceTemplatesOutputTypeDef,
    ListServiceTemplateVersionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    OutputTypeDef,
    RejectEnvironmentAccountConnectionOutputTypeDef,
    RepositoryBranchInputTypeDef,
    TagTypeDef,
    TemplateVersionSourceInputTypeDef,
    UpdateAccountSettingsOutputTypeDef,
    UpdateComponentOutputTypeDef,
    UpdateEnvironmentAccountConnectionOutputTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateEnvironmentTemplateOutputTypeDef,
    UpdateEnvironmentTemplateVersionOutputTypeDef,
    UpdateServiceInstanceOutputTypeDef,
    UpdateServiceOutputTypeDef,
    UpdateServicePipelineOutputTypeDef,
    UpdateServiceSyncBlockerOutputTypeDef,
    UpdateServiceSyncConfigOutputTypeDef,
    UpdateServiceTemplateOutputTypeDef,
    UpdateServiceTemplateVersionOutputTypeDef,
    UpdateTemplateSyncConfigOutputTypeDef,
)
from .waiter import (
    ComponentDeletedWaiter,
    ComponentDeployedWaiter,
    EnvironmentDeployedWaiter,
    EnvironmentTemplateVersionRegisteredWaiter,
    ServiceCreatedWaiter,
    ServiceDeletedWaiter,
    ServiceInstanceDeployedWaiter,
    ServicePipelineDeployedWaiter,
    ServiceTemplateVersionRegisteredWaiter,
    ServiceUpdatedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ProtonClient",)

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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ProtonClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ProtonClient exceptions.
        """
    def accept_environment_account_connection(
        self, *, id: str
    ) -> AcceptEnvironmentAccountConnectionOutputTypeDef:
        """
        In a management account, an environment account connection request is accepted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.accept_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#accept_environment_account_connection)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#can_paginate)
        """
    def cancel_component_deployment(
        self, *, componentName: str
    ) -> CancelComponentDeploymentOutputTypeDef:
        """
        Attempts to cancel a component deployment (for a component that is in the
        `IN_PROGRESS` deployment status).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.cancel_component_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#cancel_component_deployment)
        """
    def cancel_environment_deployment(
        self, *, environmentName: str
    ) -> CancelEnvironmentDeploymentOutputTypeDef:
        """
        Attempts to cancel an environment deployment on an  UpdateEnvironment action, if
        the deployment is `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.cancel_environment_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#cancel_environment_deployment)
        """
    def cancel_service_instance_deployment(
        self, *, serviceInstanceName: str, serviceName: str
    ) -> CancelServiceInstanceDeploymentOutputTypeDef:
        """
        Attempts to cancel a service instance deployment on an  UpdateServiceInstance
        action, if the deployment is `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.cancel_service_instance_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#cancel_service_instance_deployment)
        """
    def cancel_service_pipeline_deployment(
        self, *, serviceName: str
    ) -> CancelServicePipelineDeploymentOutputTypeDef:
        """
        Attempts to cancel a service pipeline deployment on an  UpdateServicePipeline
        action, if the deployment is `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.cancel_service_pipeline_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#cancel_service_pipeline_deployment)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#close)
        """
    def create_component(
        self,
        *,
        manifest: str,
        name: str,
        templateFile: str,
        clientToken: str = None,
        description: str = None,
        environmentName: str = None,
        serviceInstanceName: str = None,
        serviceName: str = None,
        serviceSpec: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateComponentOutputTypeDef:
        """
        Create an Proton component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_component)
        """
    def create_environment(
        self,
        *,
        name: str,
        spec: str,
        templateMajorVersion: str,
        templateName: str,
        codebuildRoleArn: str = None,
        componentRoleArn: str = None,
        description: str = None,
        environmentAccountConnectionId: str = None,
        protonServiceRoleArn: str = None,
        provisioningRepository: "RepositoryBranchInputTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        templateMinorVersion: str = None
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Deploy a new environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_environment)
        """
    def create_environment_account_connection(
        self,
        *,
        environmentName: str,
        managementAccountId: str,
        clientToken: str = None,
        codebuildRoleArn: str = None,
        componentRoleArn: str = None,
        roleArn: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateEnvironmentAccountConnectionOutputTypeDef:
        """
        Create an environment account connection in an environment account so that
        environment infrastructure resources can be provisioned in the environment
        account from a management account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_environment_account_connection)
        """
    def create_environment_template(
        self,
        *,
        name: str,
        description: str = None,
        displayName: str = None,
        encryptionKey: str = None,
        provisioning: Literal["CUSTOMER_MANAGED"] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateEnvironmentTemplateOutputTypeDef:
        """
        Create an environment template for Proton.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_environment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_environment_template)
        """
    def create_environment_template_version(
        self,
        *,
        source: "TemplateVersionSourceInputTypeDef",
        templateName: str,
        clientToken: str = None,
        description: str = None,
        majorVersion: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateEnvironmentTemplateVersionOutputTypeDef:
        """
        Create a new major or minor version of an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_environment_template_version)
        """
    def create_repository(
        self,
        *,
        connectionArn: str,
        name: str,
        provider: RepositoryProviderType,
        encryptionKey: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRepositoryOutputTypeDef:
        """
        Create and register a link to a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_repository)
        """
    def create_service(
        self,
        *,
        name: str,
        spec: str,
        templateMajorVersion: str,
        templateName: str,
        branchName: str = None,
        description: str = None,
        repositoryConnectionArn: str = None,
        repositoryId: str = None,
        tags: List["TagTypeDef"] = None,
        templateMinorVersion: str = None
    ) -> CreateServiceOutputTypeDef:
        """
        Create an Proton service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_service)
        """
    def create_service_instance(
        self,
        *,
        name: str,
        serviceName: str,
        spec: str,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None,
        templateMajorVersion: str = None,
        templateMinorVersion: str = None
    ) -> CreateServiceInstanceOutputTypeDef:
        """
        Create a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_service_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_service_instance)
        """
    def create_service_sync_config(
        self,
        *,
        branch: str,
        filePath: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        serviceName: str
    ) -> CreateServiceSyncConfigOutputTypeDef:
        """
        Create the Proton Ops configuration file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_service_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_service_sync_config)
        """
    def create_service_template(
        self,
        *,
        name: str,
        description: str = None,
        displayName: str = None,
        encryptionKey: str = None,
        pipelineProvisioning: Literal["CUSTOMER_MANAGED"] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateServiceTemplateOutputTypeDef:
        """
        Create a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_service_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_service_template)
        """
    def create_service_template_version(
        self,
        *,
        compatibleEnvironmentTemplates: List["CompatibleEnvironmentTemplateInputTypeDef"],
        source: "TemplateVersionSourceInputTypeDef",
        templateName: str,
        clientToken: str = None,
        description: str = None,
        majorVersion: str = None,
        supportedComponentSources: List[Literal["DIRECTLY_DEFINED"]] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateServiceTemplateVersionOutputTypeDef:
        """
        Create a new major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_service_template_version)
        """
    def create_template_sync_config(
        self,
        *,
        branch: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        templateName: str,
        templateType: TemplateTypeType,
        subdirectory: str = None
    ) -> CreateTemplateSyncConfigOutputTypeDef:
        """
        Set up a template to create new template versions automatically by tracking a
        linked repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.create_template_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_template_sync_config)
        """
    def delete_component(self, *, name: str) -> DeleteComponentOutputTypeDef:
        """
        Delete an Proton component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_component)
        """
    def delete_environment(self, *, name: str) -> DeleteEnvironmentOutputTypeDef:
        """
        Delete an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment)
        """
    def delete_environment_account_connection(
        self, *, id: str
    ) -> DeleteEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, delete an environment account connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment_account_connection)
        """
    def delete_environment_template(self, *, name: str) -> DeleteEnvironmentTemplateOutputTypeDef:
        """
        If no other major or minor versions of an environment template exist, delete the
        environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_environment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment_template)
        """
    def delete_environment_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> DeleteEnvironmentTemplateVersionOutputTypeDef:
        """
        If no other minor versions of an environment template exist, delete a major
        version of the environment template if it's not the `Recommended` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment_template_version)
        """
    def delete_repository(
        self, *, name: str, provider: RepositoryProviderType
    ) -> DeleteRepositoryOutputTypeDef:
        """
        De-register and unlink your repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_repository)
        """
    def delete_service(self, *, name: str) -> DeleteServiceOutputTypeDef:
        """
        Delete a service, with its instances and pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_service)
        """
    def delete_service_sync_config(
        self, *, serviceName: str
    ) -> DeleteServiceSyncConfigOutputTypeDef:
        """
        Delete the Proton Ops file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_service_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_service_sync_config)
        """
    def delete_service_template(self, *, name: str) -> DeleteServiceTemplateOutputTypeDef:
        """
        If no other major or minor versions of the service template exist, delete the
        service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_service_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_service_template)
        """
    def delete_service_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> DeleteServiceTemplateVersionOutputTypeDef:
        """
        If no other minor versions of a service template exist, delete a major version
        of the service template if it's not the `Recommended` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_service_template_version)
        """
    def delete_template_sync_config(
        self, *, templateName: str, templateType: TemplateTypeType
    ) -> DeleteTemplateSyncConfigOutputTypeDef:
        """
        Delete a template sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.delete_template_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_template_sync_config)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#generate_presigned_url)
        """
    def get_account_settings(self) -> GetAccountSettingsOutputTypeDef:
        """
        Get detail data for Proton account-wide settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_account_settings)
        """
    def get_component(self, *, name: str) -> GetComponentOutputTypeDef:
        """
        Get detailed data for a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_component)
        """
    def get_environment(self, *, name: str) -> GetEnvironmentOutputTypeDef:
        """
        Get detailed data for an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment)
        """
    def get_environment_account_connection(
        self, *, id: str
    ) -> GetEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, get the detailed data for an environment account
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment_account_connection)
        """
    def get_environment_template(self, *, name: str) -> GetEnvironmentTemplateOutputTypeDef:
        """
        Get detailed data for an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_environment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment_template)
        """
    def get_environment_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> GetEnvironmentTemplateVersionOutputTypeDef:
        """
        Get detailed data for a major or minor version of an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment_template_version)
        """
    def get_repository(
        self, *, name: str, provider: RepositoryProviderType
    ) -> GetRepositoryOutputTypeDef:
        """
        Get detail data for a linked repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_repository)
        """
    def get_repository_sync_status(
        self,
        *,
        branch: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        syncType: SyncTypeType
    ) -> GetRepositorySyncStatusOutputTypeDef:
        """
        Get the sync status of a repository used for Proton template sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_repository_sync_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_repository_sync_status)
        """
    def get_resources_summary(self) -> GetResourcesSummaryOutputTypeDef:
        """
        Get counts of Proton resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_resources_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_resources_summary)
        """
    def get_service(self, *, name: str) -> GetServiceOutputTypeDef:
        """
        Get detailed data for a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service)
        """
    def get_service_instance(
        self, *, name: str, serviceName: str
    ) -> GetServiceInstanceOutputTypeDef:
        """
        Get detailed data for a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_service_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_instance)
        """
    def get_service_instance_sync_status(
        self, *, serviceInstanceName: str, serviceName: str
    ) -> GetServiceInstanceSyncStatusOutputTypeDef:
        """
        Get the status of the synced service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_service_instance_sync_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_instance_sync_status)
        """
    def get_service_sync_blocker_summary(
        self, *, serviceName: str, serviceInstanceName: str = None
    ) -> GetServiceSyncBlockerSummaryOutputTypeDef:
        """
        Get detailed data for the service sync blocker summary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_service_sync_blocker_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_sync_blocker_summary)
        """
    def get_service_sync_config(self, *, serviceName: str) -> GetServiceSyncConfigOutputTypeDef:
        """
        Get detailed information for the service sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_service_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_sync_config)
        """
    def get_service_template(self, *, name: str) -> GetServiceTemplateOutputTypeDef:
        """
        Get detailed data for a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_service_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_template)
        """
    def get_service_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> GetServiceTemplateVersionOutputTypeDef:
        """
        Get detailed data for a major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_template_version)
        """
    def get_template_sync_config(
        self, *, templateName: str, templateType: TemplateTypeType
    ) -> GetTemplateSyncConfigOutputTypeDef:
        """
        Get detail data for a template sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_template_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_template_sync_config)
        """
    def get_template_sync_status(
        self, *, templateName: str, templateType: TemplateTypeType, templateVersion: str
    ) -> GetTemplateSyncStatusOutputTypeDef:
        """
        Get the status of a template sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.get_template_sync_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_template_sync_status)
        """
    def list_component_outputs(
        self, *, componentName: str, nextToken: str = None
    ) -> ListComponentOutputsOutputTypeDef:
        """
        Get a list of component Infrastructure as Code (IaC) outputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_component_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_component_outputs)
        """
    def list_component_provisioned_resources(
        self, *, componentName: str, nextToken: str = None
    ) -> ListComponentProvisionedResourcesOutputTypeDef:
        """
        List provisioned resources for a component with details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_component_provisioned_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_component_provisioned_resources)
        """
    def list_components(
        self,
        *,
        environmentName: str = None,
        maxResults: int = None,
        nextToken: str = None,
        serviceInstanceName: str = None,
        serviceName: str = None
    ) -> ListComponentsOutputTypeDef:
        """
        List components with summary data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_components)
        """
    def list_environment_account_connections(
        self,
        *,
        requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType,
        environmentName: str = None,
        maxResults: int = None,
        nextToken: str = None,
        statuses: List[EnvironmentAccountConnectionStatusType] = None
    ) -> ListEnvironmentAccountConnectionsOutputTypeDef:
        """
        View a list of environment account connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_environment_account_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environment_account_connections)
        """
    def list_environment_outputs(
        self, *, environmentName: str, nextToken: str = None
    ) -> ListEnvironmentOutputsOutputTypeDef:
        """
        List the infrastructure as code outputs for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_environment_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environment_outputs)
        """
    def list_environment_provisioned_resources(
        self, *, environmentName: str, nextToken: str = None
    ) -> ListEnvironmentProvisionedResourcesOutputTypeDef:
        """
        List the provisioned resources for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_environment_provisioned_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environment_provisioned_resources)
        """
    def list_environment_template_versions(
        self,
        *,
        templateName: str,
        majorVersion: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListEnvironmentTemplateVersionsOutputTypeDef:
        """
        List major or minor versions of an environment template with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_environment_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environment_template_versions)
        """
    def list_environment_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListEnvironmentTemplatesOutputTypeDef:
        """
        List environment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_environment_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environment_templates)
        """
    def list_environments(
        self,
        *,
        environmentTemplates: List["EnvironmentTemplateFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListEnvironmentsOutputTypeDef:
        """
        List environments with detail data summaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environments)
        """
    def list_repositories(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListRepositoriesOutputTypeDef:
        """
        List linked repositories with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_repositories)
        """
    def list_repository_sync_definitions(
        self,
        *,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        syncType: SyncTypeType,
        nextToken: str = None
    ) -> ListRepositorySyncDefinitionsOutputTypeDef:
        """
        List repository sync definitions with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_repository_sync_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_repository_sync_definitions)
        """
    def list_service_instance_outputs(
        self, *, serviceInstanceName: str, serviceName: str, nextToken: str = None
    ) -> ListServiceInstanceOutputsOutputTypeDef:
        """
        Get a list service of instance Infrastructure as Code (IaC) outputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_service_instance_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_instance_outputs)
        """
    def list_service_instance_provisioned_resources(
        self, *, serviceInstanceName: str, serviceName: str, nextToken: str = None
    ) -> ListServiceInstanceProvisionedResourcesOutputTypeDef:
        """
        List provisioned resources for a service instance with details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_service_instance_provisioned_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_instance_provisioned_resources)
        """
    def list_service_instances(
        self,
        *,
        filters: List["ListServiceInstancesFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        serviceName: str = None,
        sortBy: ListServiceInstancesSortByType = None,
        sortOrder: SortOrderType = None
    ) -> ListServiceInstancesOutputTypeDef:
        """
        List service instances with summary data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_service_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_instances)
        """
    def list_service_pipeline_outputs(
        self, *, serviceName: str, nextToken: str = None
    ) -> ListServicePipelineOutputsOutputTypeDef:
        """
        Get a list of service pipeline Infrastructure as Code (IaC) outputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_service_pipeline_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_pipeline_outputs)
        """
    def list_service_pipeline_provisioned_resources(
        self, *, serviceName: str, nextToken: str = None
    ) -> ListServicePipelineProvisionedResourcesOutputTypeDef:
        """
        List provisioned resources for a service and pipeline with details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_service_pipeline_provisioned_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_pipeline_provisioned_resources)
        """
    def list_service_template_versions(
        self,
        *,
        templateName: str,
        majorVersion: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListServiceTemplateVersionsOutputTypeDef:
        """
        List major or minor versions of a service template with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_service_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_template_versions)
        """
    def list_service_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListServiceTemplatesOutputTypeDef:
        """
        List service templates with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_service_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_templates)
        """
    def list_services(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListServicesOutputTypeDef:
        """
        List services with summaries of detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_services)
        """
    def list_tags_for_resource(
        self, *, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_tags_for_resource)
        """
    def notify_resource_deployment_status_change(
        self,
        *,
        resourceArn: str,
        deploymentId: str = None,
        outputs: List["OutputTypeDef"] = None,
        status: ResourceDeploymentStatusType = None,
        statusMessage: str = None
    ) -> Dict[str, Any]:
        """
        Notify Proton of status changes to a provisioned resource when you use self-
        managed provisioning.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.notify_resource_deployment_status_change)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#notify_resource_deployment_status_change)
        """
    def reject_environment_account_connection(
        self, *, id: str
    ) -> RejectEnvironmentAccountConnectionOutputTypeDef:
        """
        In a management account, reject an environment account connection from another
        environment account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.reject_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#reject_environment_account_connection)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tag a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove a customer tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#untag_resource)
        """
    def update_account_settings(
        self,
        *,
        deletePipelineProvisioningRepository: bool = None,
        pipelineCodebuildRoleArn: str = None,
        pipelineProvisioningRepository: "RepositoryBranchInputTypeDef" = None,
        pipelineServiceRoleArn: str = None
    ) -> UpdateAccountSettingsOutputTypeDef:
        """
        Update Proton settings that are used for multiple services in the Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_account_settings)
        """
    def update_component(
        self,
        *,
        deploymentType: ComponentDeploymentUpdateTypeType,
        name: str,
        clientToken: str = None,
        description: str = None,
        serviceInstanceName: str = None,
        serviceName: str = None,
        serviceSpec: str = None,
        templateFile: str = None
    ) -> UpdateComponentOutputTypeDef:
        """
        Update a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_component)
        """
    def update_environment(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        name: str,
        codebuildRoleArn: str = None,
        componentRoleArn: str = None,
        description: str = None,
        environmentAccountConnectionId: str = None,
        protonServiceRoleArn: str = None,
        provisioningRepository: "RepositoryBranchInputTypeDef" = None,
        spec: str = None,
        templateMajorVersion: str = None,
        templateMinorVersion: str = None
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Update an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_environment)
        """
    def update_environment_account_connection(
        self,
        *,
        id: str,
        codebuildRoleArn: str = None,
        componentRoleArn: str = None,
        roleArn: str = None
    ) -> UpdateEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, update an environment account connection to use a new
        IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_environment_account_connection)
        """
    def update_environment_template(
        self, *, name: str, description: str = None, displayName: str = None
    ) -> UpdateEnvironmentTemplateOutputTypeDef:
        """
        Update an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_environment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_environment_template)
        """
    def update_environment_template_version(
        self,
        *,
        majorVersion: str,
        minorVersion: str,
        templateName: str,
        description: str = None,
        status: TemplateVersionStatusType = None
    ) -> UpdateEnvironmentTemplateVersionOutputTypeDef:
        """
        Update a major or minor version of an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_environment_template_version)
        """
    def update_service(
        self, *, name: str, description: str = None, spec: str = None
    ) -> UpdateServiceOutputTypeDef:
        """
        Edit a service description or use a spec to add and delete service instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service)
        """
    def update_service_instance(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        name: str,
        serviceName: str,
        clientToken: str = None,
        spec: str = None,
        templateMajorVersion: str = None,
        templateMinorVersion: str = None
    ) -> UpdateServiceInstanceOutputTypeDef:
        """
        Update a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_service_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_instance)
        """
    def update_service_pipeline(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        serviceName: str,
        spec: str,
        templateMajorVersion: str = None,
        templateMinorVersion: str = None
    ) -> UpdateServicePipelineOutputTypeDef:
        """
        Update the service pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_service_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_pipeline)
        """
    def update_service_sync_blocker(
        self, *, id: str, resolvedReason: str
    ) -> UpdateServiceSyncBlockerOutputTypeDef:
        """
        Update the service sync blocker by resolving it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_service_sync_blocker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_sync_blocker)
        """
    def update_service_sync_config(
        self,
        *,
        branch: str,
        filePath: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        serviceName: str
    ) -> UpdateServiceSyncConfigOutputTypeDef:
        """
        Update the Proton Ops config file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_service_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_sync_config)
        """
    def update_service_template(
        self, *, name: str, description: str = None, displayName: str = None
    ) -> UpdateServiceTemplateOutputTypeDef:
        """
        Update a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_service_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_template)
        """
    def update_service_template_version(
        self,
        *,
        majorVersion: str,
        minorVersion: str,
        templateName: str,
        compatibleEnvironmentTemplates: List["CompatibleEnvironmentTemplateInputTypeDef"] = None,
        description: str = None,
        status: TemplateVersionStatusType = None,
        supportedComponentSources: List[Literal["DIRECTLY_DEFINED"]] = None
    ) -> UpdateServiceTemplateVersionOutputTypeDef:
        """
        Update a major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_template_version)
        """
    def update_template_sync_config(
        self,
        *,
        branch: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        templateName: str,
        templateType: TemplateTypeType,
        subdirectory: str = None
    ) -> UpdateTemplateSyncConfigOutputTypeDef:
        """
        Update template sync configuration parameters, except for the `templateName` and
        `templateType`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Client.update_template_sync_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_template_sync_config)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_component_outputs"]
    ) -> ListComponentOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListComponentOutputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentoutputspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_component_provisioned_resources"]
    ) -> ListComponentProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListComponentProvisionedResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentprovisionedresourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_components"]) -> ListComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListComponents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_account_connections"]
    ) -> ListEnvironmentAccountConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListEnvironmentAccountConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentaccountconnectionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_outputs"]
    ) -> ListEnvironmentOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListEnvironmentOutputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentoutputspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_provisioned_resources"]
    ) -> ListEnvironmentProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListEnvironmentProvisionedResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentprovisionedresourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_template_versions"]
    ) -> ListEnvironmentTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplateversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_templates"]
    ) -> ListEnvironmentTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListRepositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listrepositoriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_repository_sync_definitions"]
    ) -> ListRepositorySyncDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListRepositorySyncDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listrepositorysyncdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_instance_outputs"]
    ) -> ListServiceInstanceOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServiceInstanceOutputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstanceoutputspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_instance_provisioned_resources"]
    ) -> ListServiceInstanceProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServiceInstanceProvisionedResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstanceprovisionedresourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_instances"]
    ) -> ListServiceInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServiceInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_pipeline_outputs"]
    ) -> ListServicePipelineOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServicePipelineOutputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicepipelineoutputspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_pipeline_provisioned_resources"]
    ) -> ListServicePipelineProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServicePipelineProvisionedResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicepipelineprovisionedresourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_template_versions"]
    ) -> ListServiceTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServiceTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplateversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_templates"]
    ) -> ListServiceTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServiceTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["component_deleted"]) -> ComponentDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ComponentDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#componentdeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["component_deployed"]) -> ComponentDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ComponentDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#componentdeployedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["environment_deployed"]) -> EnvironmentDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.EnvironmentDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#environmentdeployedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["environment_template_version_registered"]
    ) -> EnvironmentTemplateVersionRegisteredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.EnvironmentTemplateVersionRegistered)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#environmenttemplateversionregisteredwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["service_created"]) -> ServiceCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ServiceCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicecreatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["service_deleted"]) -> ServiceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ServiceDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicedeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["service_instance_deployed"]
    ) -> ServiceInstanceDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ServiceInstanceDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#serviceinstancedeployedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["service_pipeline_deployed"]
    ) -> ServicePipelineDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ServicePipelineDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicepipelinedeployedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["service_template_version_registered"]
    ) -> ServiceTemplateVersionRegisteredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ServiceTemplateVersionRegistered)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicetemplateversionregisteredwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["service_updated"]) -> ServiceUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/proton.html#Proton.Waiter.ServiceUpdated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#serviceupdatedwaiter)
        """
