"""
Type annotations for proton service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/literals.html)

Usage::

    ```python
    from mypy_boto3_proton.literals import BlockerStatusType

    data: BlockerStatusType = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BlockerStatusType",
    "BlockerTypeType",
    "ComponentDeletedWaiterName",
    "ComponentDeployedWaiterName",
    "ComponentDeploymentUpdateTypeType",
    "DeploymentStatusType",
    "DeploymentUpdateTypeType",
    "EnvironmentAccountConnectionRequesterAccountTypeType",
    "EnvironmentAccountConnectionStatusType",
    "EnvironmentDeployedWaiterName",
    "EnvironmentTemplateVersionRegisteredWaiterName",
    "ListComponentOutputsPaginatorName",
    "ListComponentProvisionedResourcesPaginatorName",
    "ListComponentsPaginatorName",
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
    "ListServiceInstancesFilterByType",
    "ListServiceInstancesPaginatorName",
    "ListServiceInstancesSortByType",
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
    "ServiceTemplateSupportedComponentSourceTypeType",
    "ServiceTemplateVersionRegisteredWaiterName",
    "ServiceUpdatedWaiterName",
    "SortOrderType",
    "SyncTypeType",
    "TemplateTypeType",
    "TemplateVersionStatusType",
)

BlockerStatusType = Literal["ACTIVE", "RESOLVED"]
BlockerTypeType = Literal["AUTOMATED"]
ComponentDeletedWaiterName = Literal["component_deleted"]
ComponentDeployedWaiterName = Literal["component_deployed"]
ComponentDeploymentUpdateTypeType = Literal["CURRENT_VERSION", "NONE"]
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
ListComponentOutputsPaginatorName = Literal["list_component_outputs"]
ListComponentProvisionedResourcesPaginatorName = Literal["list_component_provisioned_resources"]
ListComponentsPaginatorName = Literal["list_components"]
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
ListServiceInstancesFilterByType = Literal[
    "createdAtAfter",
    "createdAtBefore",
    "deployedTemplateVersionStatus",
    "deploymentStatus",
    "environmentName",
    "lastDeploymentAttemptedAtAfter",
    "lastDeploymentAttemptedAtBefore",
    "name",
    "serviceName",
    "templateName",
]
ListServiceInstancesPaginatorName = Literal["list_service_instances"]
ListServiceInstancesSortByType = Literal[
    "createdAt",
    "deploymentStatus",
    "environmentName",
    "lastDeploymentAttemptedAt",
    "name",
    "serviceName",
    "templateName",
]
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
ServiceTemplateSupportedComponentSourceTypeType = Literal["DIRECTLY_DEFINED"]
ServiceTemplateVersionRegisteredWaiterName = Literal["service_template_version_registered"]
ServiceUpdatedWaiterName = Literal["service_updated"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SyncTypeType = Literal["SERVICE_SYNC", "TEMPLATE_SYNC"]
TemplateTypeType = Literal["ENVIRONMENT", "SERVICE"]
TemplateVersionStatusType = Literal[
    "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
]
