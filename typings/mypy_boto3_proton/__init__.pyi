"""
Main interface for proton service.

Usage::

    ```python
    import boto3
    from mypy_boto3_proton import (
        Client,
        EnvironmentDeployedWaiter,
        EnvironmentTemplateVersionRegisteredWaiter,
        ListEnvironmentAccountConnectionsPaginator,
        ListEnvironmentOutputsPaginator,
        ListEnvironmentProvisionedResourcesPaginator,
        ListEnvironmentTemplateVersionsPaginator,
        ListEnvironmentTemplatesPaginator,
        ListEnvironmentsPaginator,
        ListRepositoriesPaginator,
        ListRepositorySyncDefinitionsPaginator,
        ListServiceInstanceOutputsPaginator,
        ListServiceInstanceProvisionedResourcesPaginator,
        ListServiceInstancesPaginator,
        ListServicePipelineOutputsPaginator,
        ListServicePipelineProvisionedResourcesPaginator,
        ListServiceTemplateVersionsPaginator,
        ListServiceTemplatesPaginator,
        ListServicesPaginator,
        ListTagsForResourcePaginator,
        ProtonClient,
        ServiceCreatedWaiter,
        ServiceDeletedWaiter,
        ServiceInstanceDeployedWaiter,
        ServicePipelineDeployedWaiter,
        ServiceTemplateVersionRegisteredWaiter,
        ServiceUpdatedWaiter,
    )

    session = boto3.Session()

    client: ProtonClient = boto3.client("proton")
    session_client: ProtonClient = session.client("proton")

    environment_deployed_waiter: EnvironmentDeployedWaiter = client.get_waiter("environment_deployed")
    environment_template_version_registered_waiter: EnvironmentTemplateVersionRegisteredWaiter = client.get_waiter("environment_template_version_registered")
    service_created_waiter: ServiceCreatedWaiter = client.get_waiter("service_created")
    service_deleted_waiter: ServiceDeletedWaiter = client.get_waiter("service_deleted")
    service_instance_deployed_waiter: ServiceInstanceDeployedWaiter = client.get_waiter("service_instance_deployed")
    service_pipeline_deployed_waiter: ServicePipelineDeployedWaiter = client.get_waiter("service_pipeline_deployed")
    service_template_version_registered_waiter: ServiceTemplateVersionRegisteredWaiter = client.get_waiter("service_template_version_registered")
    service_updated_waiter: ServiceUpdatedWaiter = client.get_waiter("service_updated")

    list_environment_account_connections_paginator: ListEnvironmentAccountConnectionsPaginator = client.get_paginator("list_environment_account_connections")
    list_environment_outputs_paginator: ListEnvironmentOutputsPaginator = client.get_paginator("list_environment_outputs")
    list_environment_provisioned_resources_paginator: ListEnvironmentProvisionedResourcesPaginator = client.get_paginator("list_environment_provisioned_resources")
    list_environment_template_versions_paginator: ListEnvironmentTemplateVersionsPaginator = client.get_paginator("list_environment_template_versions")
    list_environment_templates_paginator: ListEnvironmentTemplatesPaginator = client.get_paginator("list_environment_templates")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_repositories_paginator: ListRepositoriesPaginator = client.get_paginator("list_repositories")
    list_repository_sync_definitions_paginator: ListRepositorySyncDefinitionsPaginator = client.get_paginator("list_repository_sync_definitions")
    list_service_instance_outputs_paginator: ListServiceInstanceOutputsPaginator = client.get_paginator("list_service_instance_outputs")
    list_service_instance_provisioned_resources_paginator: ListServiceInstanceProvisionedResourcesPaginator = client.get_paginator("list_service_instance_provisioned_resources")
    list_service_instances_paginator: ListServiceInstancesPaginator = client.get_paginator("list_service_instances")
    list_service_pipeline_outputs_paginator: ListServicePipelineOutputsPaginator = client.get_paginator("list_service_pipeline_outputs")
    list_service_pipeline_provisioned_resources_paginator: ListServicePipelineProvisionedResourcesPaginator = client.get_paginator("list_service_pipeline_provisioned_resources")
    list_service_template_versions_paginator: ListServiceTemplateVersionsPaginator = client.get_paginator("list_service_template_versions")
    list_service_templates_paginator: ListServiceTemplatesPaginator = client.get_paginator("list_service_templates")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from .client import ProtonClient
from .paginator import (
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

Client = ProtonClient

__all__ = (
    "Client",
    "EnvironmentDeployedWaiter",
    "EnvironmentTemplateVersionRegisteredWaiter",
    "ListEnvironmentAccountConnectionsPaginator",
    "ListEnvironmentOutputsPaginator",
    "ListEnvironmentProvisionedResourcesPaginator",
    "ListEnvironmentTemplateVersionsPaginator",
    "ListEnvironmentTemplatesPaginator",
    "ListEnvironmentsPaginator",
    "ListRepositoriesPaginator",
    "ListRepositorySyncDefinitionsPaginator",
    "ListServiceInstanceOutputsPaginator",
    "ListServiceInstanceProvisionedResourcesPaginator",
    "ListServiceInstancesPaginator",
    "ListServicePipelineOutputsPaginator",
    "ListServicePipelineProvisionedResourcesPaginator",
    "ListServiceTemplateVersionsPaginator",
    "ListServiceTemplatesPaginator",
    "ListServicesPaginator",
    "ListTagsForResourcePaginator",
    "ProtonClient",
    "ServiceCreatedWaiter",
    "ServiceDeletedWaiter",
    "ServiceInstanceDeployedWaiter",
    "ServicePipelineDeployedWaiter",
    "ServiceTemplateVersionRegisteredWaiter",
    "ServiceUpdatedWaiter",
)
