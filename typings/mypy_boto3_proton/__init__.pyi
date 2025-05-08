"""
Main interface for proton service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_proton import (
        Client,
        ComponentDeletedWaiter,
        ComponentDeployedWaiter,
        EnvironmentDeployedWaiter,
        EnvironmentTemplateVersionRegisteredWaiter,
        ListComponentOutputsPaginator,
        ListComponentProvisionedResourcesPaginator,
        ListComponentsPaginator,
        ListDeploymentsPaginator,
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

    session = Session()
    client: ProtonClient = session.client("proton")

    component_deleted_waiter: ComponentDeletedWaiter = client.get_waiter("component_deleted")
    component_deployed_waiter: ComponentDeployedWaiter = client.get_waiter("component_deployed")
    environment_deployed_waiter: EnvironmentDeployedWaiter = client.get_waiter("environment_deployed")
    environment_template_version_registered_waiter: EnvironmentTemplateVersionRegisteredWaiter = client.get_waiter("environment_template_version_registered")
    service_created_waiter: ServiceCreatedWaiter = client.get_waiter("service_created")
    service_deleted_waiter: ServiceDeletedWaiter = client.get_waiter("service_deleted")
    service_instance_deployed_waiter: ServiceInstanceDeployedWaiter = client.get_waiter("service_instance_deployed")
    service_pipeline_deployed_waiter: ServicePipelineDeployedWaiter = client.get_waiter("service_pipeline_deployed")
    service_template_version_registered_waiter: ServiceTemplateVersionRegisteredWaiter = client.get_waiter("service_template_version_registered")
    service_updated_waiter: ServiceUpdatedWaiter = client.get_waiter("service_updated")

    list_component_outputs_paginator: ListComponentOutputsPaginator = client.get_paginator("list_component_outputs")
    list_component_provisioned_resources_paginator: ListComponentProvisionedResourcesPaginator = client.get_paginator("list_component_provisioned_resources")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
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
    ListComponentOutputsPaginator,
    ListComponentProvisionedResourcesPaginator,
    ListComponentsPaginator,
    ListDeploymentsPaginator,
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

Client = ProtonClient

__all__ = (
    "Client",
    "ComponentDeletedWaiter",
    "ComponentDeployedWaiter",
    "EnvironmentDeployedWaiter",
    "EnvironmentTemplateVersionRegisteredWaiter",
    "ListComponentOutputsPaginator",
    "ListComponentProvisionedResourcesPaginator",
    "ListComponentsPaginator",
    "ListDeploymentsPaginator",
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
