"""
Type annotations for proton service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/literals.html)

Usage::

    ```python
    from mypy_boto3_proton.literals import DeploymentStatusType

    data: DeploymentStatusType = "CANCELLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DeploymentStatusType",
    "DeploymentUpdateTypeType",
    "EnvironmentAccountConnectionRequesterAccountTypeType",
    "EnvironmentAccountConnectionStatusType",
    "EnvironmentDeployedWaiterName",
    "EnvironmentTemplateVersionRegisteredWaiterName",
    "ListEnvironmentAccountConnectionsPaginatorName",
    "ListEnvironmentOutputsPaginatorName",
    "ListEnvironmentProvisionedResourcesPaginatorName",
    "ListEnvironmentTemplateVersionsPaginatorName",
    "ListEnvironmentTemplatesPaginatorName",
    "ListEnvironmentsPaginatorName",
    "ListRepositoriesPaginatorName",
    "ListRepositorySyncDefinitionsPaginatorName",
    "ListServiceInstanceOutputsPaginatorName",
    "ListServiceInstanceProvisionedResourcesPaginatorName",
    "ListServiceInstancesPaginatorName",
    "ListServicePipelineOutputsPaginatorName",
    "ListServicePipelineProvisionedResourcesPaginatorName",
    "ListServiceTemplateVersionsPaginatorName",
    "ListServiceTemplatesPaginatorName",
    "ListServicesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ProvisionedResourceEngineType",
    "ProvisioningType",
    "RepositoryProviderType",
    "RepositorySyncStatusType",
    "ResourceDeploymentStatusType",
    "ResourceSyncStatusType",
    "ServiceCreatedWaiterName",
    "ServiceDeletedWaiterName",
    "ServiceInstanceDeployedWaiterName",
    "ServicePipelineDeployedWaiterName",
    "ServiceStatusType",
    "ServiceTemplateVersionRegisteredWaiterName",
    "ServiceUpdatedWaiterName",
    "SyncTypeType",
    "TemplateTypeType",
    "TemplateVersionStatusType",
)

DeploymentStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "FAILED",
    "IN_PROGRESS",
    "SUCCEEDED",
]
DeploymentUpdateTypeType = Literal["CURRENT_VERSION", "MAJOR_VERSION", "MINOR_VERSION", "NONE"]
EnvironmentAccountConnectionRequesterAccountTypeType = Literal[
    "ENVIRONMENT_ACCOUNT", "MANAGEMENT_ACCOUNT"
]
EnvironmentAccountConnectionStatusType = Literal["CONNECTED", "PENDING", "REJECTED"]
EnvironmentDeployedWaiterName = Literal["environment_deployed"]
EnvironmentTemplateVersionRegisteredWaiterName = Literal["environment_template_version_registered"]
ListEnvironmentAccountConnectionsPaginatorName = Literal["list_environment_account_connections"]
ListEnvironmentOutputsPaginatorName = Literal["list_environment_outputs"]
ListEnvironmentProvisionedResourcesPaginatorName = Literal["list_environment_provisioned_resources"]
ListEnvironmentTemplateVersionsPaginatorName = Literal["list_environment_template_versions"]
ListEnvironmentTemplatesPaginatorName = Literal["list_environment_templates"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ListRepositoriesPaginatorName = Literal["list_repositories"]
ListRepositorySyncDefinitionsPaginatorName = Literal["list_repository_sync_definitions"]
ListServiceInstanceOutputsPaginatorName = Literal["list_service_instance_outputs"]
ListServiceInstanceProvisionedResourcesPaginatorName = Literal[
    "list_service_instance_provisioned_resources"
]
ListServiceInstancesPaginatorName = Literal["list_service_instances"]
ListServicePipelineOutputsPaginatorName = Literal["list_service_pipeline_outputs"]
ListServicePipelineProvisionedResourcesPaginatorName = Literal[
    "list_service_pipeline_provisioned_resources"
]
ListServiceTemplateVersionsPaginatorName = Literal["list_service_template_versions"]
ListServiceTemplatesPaginatorName = Literal["list_service_templates"]
ListServicesPaginatorName = Literal["list_services"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ProvisionedResourceEngineType = Literal["CLOUDFORMATION", "TERRAFORM"]
ProvisioningType = Literal["CUSTOMER_MANAGED"]
RepositoryProviderType = Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"]
RepositorySyncStatusType = Literal["FAILED", "INITIATED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
ResourceDeploymentStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ResourceSyncStatusType = Literal["FAILED", "INITIATED", "IN_PROGRESS", "SUCCEEDED"]
ServiceCreatedWaiterName = Literal["service_created"]
ServiceDeletedWaiterName = Literal["service_deleted"]
ServiceInstanceDeployedWaiterName = Literal["service_instance_deployed"]
ServicePipelineDeployedWaiterName = Literal["service_pipeline_deployed"]
ServiceStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_FAILED_CLEANUP_COMPLETE",
    "CREATE_FAILED_CLEANUP_FAILED",
    "CREATE_FAILED_CLEANUP_IN_PROGRESS",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE_CLEANUP_FAILED",
    "UPDATE_FAILED",
    "UPDATE_FAILED_CLEANUP_COMPLETE",
    "UPDATE_FAILED_CLEANUP_FAILED",
    "UPDATE_FAILED_CLEANUP_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
]
ServiceTemplateVersionRegisteredWaiterName = Literal["service_template_version_registered"]
ServiceUpdatedWaiterName = Literal["service_updated"]
SyncTypeType = Literal["TEMPLATE_SYNC"]
TemplateTypeType = Literal["ENVIRONMENT", "SERVICE"]
TemplateVersionStatusType = Literal[
    "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
]
