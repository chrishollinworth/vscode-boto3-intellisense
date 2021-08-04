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
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    TemplateVersionStatusType,
)
from .paginator import (
    ListEnvironmentAccountConnectionsPaginator,
    ListEnvironmentsPaginator,
    ListEnvironmentTemplatesPaginator,
    ListEnvironmentTemplateVersionsPaginator,
    ListServiceInstancesPaginator,
    ListServicesPaginator,
    ListServiceTemplatesPaginator,
    ListServiceTemplateVersionsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AcceptEnvironmentAccountConnectionOutputTypeDef,
    CancelEnvironmentDeploymentOutputTypeDef,
    CancelServiceInstanceDeploymentOutputTypeDef,
    CancelServicePipelineDeploymentOutputTypeDef,
    CompatibleEnvironmentTemplateInputTypeDef,
    CreateEnvironmentAccountConnectionOutputTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateEnvironmentTemplateOutputTypeDef,
    CreateEnvironmentTemplateVersionOutputTypeDef,
    CreateServiceOutputTypeDef,
    CreateServiceTemplateOutputTypeDef,
    CreateServiceTemplateVersionOutputTypeDef,
    DeleteEnvironmentAccountConnectionOutputTypeDef,
    DeleteEnvironmentOutputTypeDef,
    DeleteEnvironmentTemplateOutputTypeDef,
    DeleteEnvironmentTemplateVersionOutputTypeDef,
    DeleteServiceOutputTypeDef,
    DeleteServiceTemplateOutputTypeDef,
    DeleteServiceTemplateVersionOutputTypeDef,
    EnvironmentTemplateFilterTypeDef,
    GetAccountSettingsOutputTypeDef,
    GetEnvironmentAccountConnectionOutputTypeDef,
    GetEnvironmentOutputTypeDef,
    GetEnvironmentTemplateOutputTypeDef,
    GetEnvironmentTemplateVersionOutputTypeDef,
    GetServiceInstanceOutputTypeDef,
    GetServiceOutputTypeDef,
    GetServiceTemplateOutputTypeDef,
    GetServiceTemplateVersionOutputTypeDef,
    ListEnvironmentAccountConnectionsOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListEnvironmentTemplatesOutputTypeDef,
    ListEnvironmentTemplateVersionsOutputTypeDef,
    ListServiceInstancesOutputTypeDef,
    ListServicesOutputTypeDef,
    ListServiceTemplatesOutputTypeDef,
    ListServiceTemplateVersionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    RejectEnvironmentAccountConnectionOutputTypeDef,
    TagTypeDef,
    TemplateVersionSourceInputTypeDef,
    UpdateAccountSettingsOutputTypeDef,
    UpdateEnvironmentAccountConnectionOutputTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateEnvironmentTemplateOutputTypeDef,
    UpdateEnvironmentTemplateVersionOutputTypeDef,
    UpdateServiceInstanceOutputTypeDef,
    UpdateServiceOutputTypeDef,
    UpdateServicePipelineOutputTypeDef,
    UpdateServiceTemplateOutputTypeDef,
    UpdateServiceTemplateVersionOutputTypeDef,
)
from .waiter import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.accept_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#accept_environment_account_connection)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#can_paginate)
        """
    def cancel_environment_deployment(
        self, *, environmentName: str
    ) -> CancelEnvironmentDeploymentOutputTypeDef:
        """
        Attempts to cancel an environment deployment on an  UpdateEnvironment action, if
        the deployment is `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.cancel_environment_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#cancel_environment_deployment)
        """
    def cancel_service_instance_deployment(
        self, *, serviceInstanceName: str, serviceName: str
    ) -> CancelServiceInstanceDeploymentOutputTypeDef:
        """
        Attempts to cancel a service instance deployment on an  UpdateServiceInstance
        action, if the deployment is `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.cancel_service_instance_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#cancel_service_instance_deployment)
        """
    def cancel_service_pipeline_deployment(
        self, *, serviceName: str
    ) -> CancelServicePipelineDeploymentOutputTypeDef:
        """
        Attempts to cancel a service pipeline deployment on an  UpdateServicePipeline
        action, if the deployment is `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.cancel_service_pipeline_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#cancel_service_pipeline_deployment)
        """
    def create_environment(
        self,
        *,
        name: str,
        spec: str,
        templateMajorVersion: str,
        templateName: str,
        description: str = None,
        environmentAccountConnectionId: str = None,
        protonServiceRoleArn: str = None,
        tags: List["TagTypeDef"] = None,
        templateMinorVersion: str = None
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Deploy a new environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_environment)
        """
    def create_environment_account_connection(
        self,
        *,
        environmentName: str,
        managementAccountId: str,
        roleArn: str,
        clientToken: str = None
    ) -> CreateEnvironmentAccountConnectionOutputTypeDef:
        """
        Create an environment account connection in an environment account so that
        environment infrastructure resources can be provisioned in the environment
        account from a management account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.create_environment_account_connection)
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
        Create an environment template for AWS Proton.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.create_environment_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.create_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_environment_template_version)
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
        Create an AWS Proton service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_service)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.create_service_template)
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
        tags: List["TagTypeDef"] = None
    ) -> CreateServiceTemplateVersionOutputTypeDef:
        """
        Create a new major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.create_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#create_service_template_version)
        """
    def delete_environment(self, *, name: str) -> DeleteEnvironmentOutputTypeDef:
        """
        Delete an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment)
        """
    def delete_environment_account_connection(
        self, *, id: str
    ) -> DeleteEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, delete an environment account connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.delete_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment_account_connection)
        """
    def delete_environment_template(self, *, name: str) -> DeleteEnvironmentTemplateOutputTypeDef:
        """
        If no other major or minor versions of an environment template exist, delete the
        environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.delete_environment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment_template)
        """
    def delete_environment_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> DeleteEnvironmentTemplateVersionOutputTypeDef:
        """
        If no other minor versions of an environment template exist, delete a major
        version of the environment template if it's not the `Recommended` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.delete_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_environment_template_version)
        """
    def delete_service(self, *, name: str) -> DeleteServiceOutputTypeDef:
        """
        Delete a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_service)
        """
    def delete_service_template(self, *, name: str) -> DeleteServiceTemplateOutputTypeDef:
        """
        If no other major or minor versions of the service template exist, delete the
        service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.delete_service_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_service_template)
        """
    def delete_service_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> DeleteServiceTemplateVersionOutputTypeDef:
        """
        If no other minor versions of a service template exist, delete a major version
        of the service template if it's not the `Recommended` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.delete_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#delete_service_template_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#generate_presigned_url)
        """
    def get_account_settings(self) -> GetAccountSettingsOutputTypeDef:
        """
        Get detail data for the AWS Proton pipeline service role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_account_settings)
        """
    def get_environment(self, *, name: str) -> GetEnvironmentOutputTypeDef:
        """
        Get detail data for an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment)
        """
    def get_environment_account_connection(
        self, *, id: str
    ) -> GetEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, view the detail data for an environment account
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment_account_connection)
        """
    def get_environment_template(self, *, name: str) -> GetEnvironmentTemplateOutputTypeDef:
        """
        Get detail data for an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_environment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment_template)
        """
    def get_environment_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> GetEnvironmentTemplateVersionOutputTypeDef:
        """
        View detail data for a major or minor version of an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_environment_template_version)
        """
    def get_service(self, *, name: str) -> GetServiceOutputTypeDef:
        """
        Get detail data for a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service)
        """
    def get_service_instance(
        self, *, name: str, serviceName: str
    ) -> GetServiceInstanceOutputTypeDef:
        """
        Get detail data for a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_service_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_instance)
        """
    def get_service_template(self, *, name: str) -> GetServiceTemplateOutputTypeDef:
        """
        Get detail data for a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_service_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_template)
        """
    def get_service_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> GetServiceTemplateVersionOutputTypeDef:
        """
        View detail data for a major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.get_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#get_service_template_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_environment_account_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environment_account_connections)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_environment_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environment_template_versions)
        """
    def list_environment_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListEnvironmentTemplatesOutputTypeDef:
        """
        List environment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_environment_templates)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_environments)
        """
    def list_service_instances(
        self, *, maxResults: int = None, nextToken: str = None, serviceName: str = None
    ) -> ListServiceInstancesOutputTypeDef:
        """
        List service instances with summaries of detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_service_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_instances)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_service_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_template_versions)
        """
    def list_service_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListServiceTemplatesOutputTypeDef:
        """
        List service templates with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_service_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_service_templates)
        """
    def list_services(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListServicesOutputTypeDef:
        """
        List services with summaries of detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_services)
        """
    def list_tags_for_resource(
        self, *, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#list_tags_for_resource)
        """
    def reject_environment_account_connection(
        self, *, id: str
    ) -> RejectEnvironmentAccountConnectionOutputTypeDef:
        """
        In a management account, reject an environment account connection from another
        environment account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.reject_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#reject_environment_account_connection)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tag a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#untag_resource)
        """
    def update_account_settings(
        self, *, pipelineServiceRoleArn: str = None
    ) -> UpdateAccountSettingsOutputTypeDef:
        """
        Update the AWS Proton pipeline service account settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_account_settings)
        """
    def update_environment(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        name: str,
        description: str = None,
        environmentAccountConnectionId: str = None,
        protonServiceRoleArn: str = None,
        spec: str = None,
        templateMajorVersion: str = None,
        templateMinorVersion: str = None
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Update an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_environment)
        """
    def update_environment_account_connection(
        self, *, id: str, roleArn: str
    ) -> UpdateEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, update an environment account connection to use a new
        IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_environment_account_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_environment_account_connection)
        """
    def update_environment_template(
        self, *, name: str, description: str = None, displayName: str = None
    ) -> UpdateEnvironmentTemplateOutputTypeDef:
        """
        Update an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_environment_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_environment_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_environment_template_version)
        """
    def update_service(
        self, *, name: str, description: str = None, spec: str = None
    ) -> UpdateServiceOutputTypeDef:
        """
        Edit a service description or use a spec to add and delete service instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service)
        """
    def update_service_instance(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        name: str,
        serviceName: str,
        spec: str = None,
        templateMajorVersion: str = None,
        templateMinorVersion: str = None
    ) -> UpdateServiceInstanceOutputTypeDef:
        """
        Update a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_service_instance)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_service_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_pipeline)
        """
    def update_service_template(
        self, *, name: str, description: str = None, displayName: str = None
    ) -> UpdateServiceTemplateOutputTypeDef:
        """
        Update a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_service_template)
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
        status: TemplateVersionStatusType = None
    ) -> UpdateServiceTemplateVersionOutputTypeDef:
        """
        Update a major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Client.update_service_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/client.html#update_service_template_version)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_account_connections"]
    ) -> ListEnvironmentAccountConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListEnvironmentAccountConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentaccountconnectionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_template_versions"]
    ) -> ListEnvironmentTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplateversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_templates"]
    ) -> ListEnvironmentTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_instances"]
    ) -> ListServiceInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListServiceInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_template_versions"]
    ) -> ListServiceTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListServiceTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplateversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_templates"]
    ) -> ListServiceTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListServiceTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["environment_deployed"]) -> EnvironmentDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.EnvironmentDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#environmentdeployedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["environment_template_version_registered"]
    ) -> EnvironmentTemplateVersionRegisteredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.EnvironmentTemplateVersionRegistered)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#environmenttemplateversionregisteredwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["service_created"]) -> ServiceCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.ServiceCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicecreatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["service_deleted"]) -> ServiceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.ServiceDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicedeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["service_instance_deployed"]
    ) -> ServiceInstanceDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.ServiceInstanceDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#serviceinstancedeployedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["service_pipeline_deployed"]
    ) -> ServicePipelineDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.ServicePipelineDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicepipelinedeployedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["service_template_version_registered"]
    ) -> ServiceTemplateVersionRegisteredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.ServiceTemplateVersionRegistered)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#servicetemplateversionregisteredwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["service_updated"]) -> ServiceUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/proton.html#Proton.Waiter.ServiceUpdated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/waiters.html#serviceupdatedwaiter)
        """
