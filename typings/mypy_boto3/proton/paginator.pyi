"""
Type annotations for proton service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_proton.client import ProtonClient
    from mypy_boto3_proton.paginator import (
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
    )

    session = Session()
    client: ProtonClient = session.client("proton")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListComponentOutputsInputPaginateTypeDef,
    ListComponentOutputsOutputTypeDef,
    ListComponentProvisionedResourcesInputPaginateTypeDef,
    ListComponentProvisionedResourcesOutputTypeDef,
    ListComponentsInputPaginateTypeDef,
    ListComponentsOutputTypeDef,
    ListDeploymentsInputPaginateTypeDef,
    ListDeploymentsOutputTypeDef,
    ListEnvironmentAccountConnectionsInputPaginateTypeDef,
    ListEnvironmentAccountConnectionsOutputTypeDef,
    ListEnvironmentOutputsInputPaginateTypeDef,
    ListEnvironmentOutputsOutputTypeDef,
    ListEnvironmentProvisionedResourcesInputPaginateTypeDef,
    ListEnvironmentProvisionedResourcesOutputTypeDef,
    ListEnvironmentsInputPaginateTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListEnvironmentTemplatesInputPaginateTypeDef,
    ListEnvironmentTemplatesOutputTypeDef,
    ListEnvironmentTemplateVersionsInputPaginateTypeDef,
    ListEnvironmentTemplateVersionsOutputTypeDef,
    ListRepositoriesInputPaginateTypeDef,
    ListRepositoriesOutputTypeDef,
    ListRepositorySyncDefinitionsInputPaginateTypeDef,
    ListRepositorySyncDefinitionsOutputTypeDef,
    ListServiceInstanceOutputsInputPaginateTypeDef,
    ListServiceInstanceOutputsOutputTypeDef,
    ListServiceInstanceProvisionedResourcesInputPaginateTypeDef,
    ListServiceInstanceProvisionedResourcesOutputTypeDef,
    ListServiceInstancesInputPaginateTypeDef,
    ListServiceInstancesOutputTypeDef,
    ListServicePipelineOutputsInputPaginateTypeDef,
    ListServicePipelineOutputsOutputTypeDef,
    ListServicePipelineProvisionedResourcesInputPaginateTypeDef,
    ListServicePipelineProvisionedResourcesOutputTypeDef,
    ListServicesInputPaginateTypeDef,
    ListServicesOutputTypeDef,
    ListServiceTemplatesInputPaginateTypeDef,
    ListServiceTemplatesOutputTypeDef,
    ListServiceTemplateVersionsInputPaginateTypeDef,
    ListServiceTemplateVersionsOutputTypeDef,
    ListTagsForResourceInputPaginateTypeDef,
    ListTagsForResourceOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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
)

if TYPE_CHECKING:
    _ListComponentOutputsPaginatorBase = Paginator[ListComponentOutputsOutputTypeDef]
else:
    _ListComponentOutputsPaginatorBase = Paginator  # type: ignore[assignment]

class ListComponentOutputsPaginator(_ListComponentOutputsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListComponentOutputs.html#Proton.Paginator.ListComponentOutputs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listcomponentoutputspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComponentOutputsInputPaginateTypeDef]
    ) -> PageIterator[ListComponentOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListComponentOutputs.html#Proton.Paginator.ListComponentOutputs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listcomponentoutputspaginator)
        """

if TYPE_CHECKING:
    _ListComponentProvisionedResourcesPaginatorBase = Paginator[
        ListComponentProvisionedResourcesOutputTypeDef
    ]
else:
    _ListComponentProvisionedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListComponentProvisionedResourcesPaginator(_ListComponentProvisionedResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListComponentProvisionedResources.html#Proton.Paginator.ListComponentProvisionedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listcomponentprovisionedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComponentProvisionedResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListComponentProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListComponentProvisionedResources.html#Proton.Paginator.ListComponentProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listcomponentprovisionedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListComponentsPaginatorBase = Paginator[ListComponentsOutputTypeDef]
else:
    _ListComponentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListComponentsPaginator(_ListComponentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListComponents.html#Proton.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listcomponentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComponentsInputPaginateTypeDef]
    ) -> PageIterator[ListComponentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListComponents.html#Proton.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listcomponentspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentsPaginatorBase = Paginator[ListDeploymentsOutputTypeDef]
else:
    _ListDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentsPaginator(_ListDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListDeployments.html#Proton.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentsInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListDeployments.html#Proton.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentAccountConnectionsPaginatorBase = Paginator[
        ListEnvironmentAccountConnectionsOutputTypeDef
    ]
else:
    _ListEnvironmentAccountConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentAccountConnectionsPaginator(_ListEnvironmentAccountConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentAccountConnections.html#Proton.Paginator.ListEnvironmentAccountConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentaccountconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentAccountConnectionsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentAccountConnectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentAccountConnections.html#Proton.Paginator.ListEnvironmentAccountConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentaccountconnectionspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentOutputsPaginatorBase = Paginator[ListEnvironmentOutputsOutputTypeDef]
else:
    _ListEnvironmentOutputsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentOutputsPaginator(_ListEnvironmentOutputsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentOutputs.html#Proton.Paginator.ListEnvironmentOutputs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentoutputspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentOutputsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentOutputs.html#Proton.Paginator.ListEnvironmentOutputs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentoutputspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentProvisionedResourcesPaginatorBase = Paginator[
        ListEnvironmentProvisionedResourcesOutputTypeDef
    ]
else:
    _ListEnvironmentProvisionedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentProvisionedResourcesPaginator(
    _ListEnvironmentProvisionedResourcesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentProvisionedResources.html#Proton.Paginator.ListEnvironmentProvisionedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentprovisionedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentProvisionedResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentProvisionedResources.html#Proton.Paginator.ListEnvironmentProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentprovisionedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentTemplateVersionsPaginatorBase = Paginator[
        ListEnvironmentTemplateVersionsOutputTypeDef
    ]
else:
    _ListEnvironmentTemplateVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentTemplateVersionsPaginator(_ListEnvironmentTemplateVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentTemplateVersions.html#Proton.Paginator.ListEnvironmentTemplateVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmenttemplateversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentTemplateVersionsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentTemplateVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentTemplateVersions.html#Proton.Paginator.ListEnvironmentTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmenttemplateversionspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentTemplatesPaginatorBase = Paginator[ListEnvironmentTemplatesOutputTypeDef]
else:
    _ListEnvironmentTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentTemplatesPaginator(_ListEnvironmentTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentTemplates.html#Proton.Paginator.ListEnvironmentTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmenttemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironmentTemplates.html#Proton.Paginator.ListEnvironmentTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmenttemplatespaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsOutputTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironments.html#Proton.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListEnvironments.html#Proton.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListRepositoriesPaginatorBase = Paginator[ListRepositoriesOutputTypeDef]
else:
    _ListRepositoriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRepositoriesPaginator(_ListRepositoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListRepositories.html#Proton.Paginator.ListRepositories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listrepositoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRepositoriesInputPaginateTypeDef]
    ) -> PageIterator[ListRepositoriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListRepositories.html#Proton.Paginator.ListRepositories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listrepositoriespaginator)
        """

if TYPE_CHECKING:
    _ListRepositorySyncDefinitionsPaginatorBase = Paginator[
        ListRepositorySyncDefinitionsOutputTypeDef
    ]
else:
    _ListRepositorySyncDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRepositorySyncDefinitionsPaginator(_ListRepositorySyncDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListRepositorySyncDefinitions.html#Proton.Paginator.ListRepositorySyncDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listrepositorysyncdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRepositorySyncDefinitionsInputPaginateTypeDef]
    ) -> PageIterator[ListRepositorySyncDefinitionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListRepositorySyncDefinitions.html#Proton.Paginator.ListRepositorySyncDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listrepositorysyncdefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListServiceInstanceOutputsPaginatorBase = Paginator[ListServiceInstanceOutputsOutputTypeDef]
else:
    _ListServiceInstanceOutputsPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceInstanceOutputsPaginator(_ListServiceInstanceOutputsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceInstanceOutputs.html#Proton.Paginator.ListServiceInstanceOutputs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listserviceinstanceoutputspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceInstanceOutputsInputPaginateTypeDef]
    ) -> PageIterator[ListServiceInstanceOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceInstanceOutputs.html#Proton.Paginator.ListServiceInstanceOutputs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listserviceinstanceoutputspaginator)
        """

if TYPE_CHECKING:
    _ListServiceInstanceProvisionedResourcesPaginatorBase = Paginator[
        ListServiceInstanceProvisionedResourcesOutputTypeDef
    ]
else:
    _ListServiceInstanceProvisionedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceInstanceProvisionedResourcesPaginator(
    _ListServiceInstanceProvisionedResourcesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceInstanceProvisionedResources.html#Proton.Paginator.ListServiceInstanceProvisionedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listserviceinstanceprovisionedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceInstanceProvisionedResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListServiceInstanceProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceInstanceProvisionedResources.html#Proton.Paginator.ListServiceInstanceProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listserviceinstanceprovisionedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListServiceInstancesPaginatorBase = Paginator[ListServiceInstancesOutputTypeDef]
else:
    _ListServiceInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceInstancesPaginator(_ListServiceInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceInstances.html#Proton.Paginator.ListServiceInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listserviceinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListServiceInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceInstances.html#Proton.Paginator.ListServiceInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listserviceinstancespaginator)
        """

if TYPE_CHECKING:
    _ListServicePipelineOutputsPaginatorBase = Paginator[ListServicePipelineOutputsOutputTypeDef]
else:
    _ListServicePipelineOutputsPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicePipelineOutputsPaginator(_ListServicePipelineOutputsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServicePipelineOutputs.html#Proton.Paginator.ListServicePipelineOutputs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicepipelineoutputspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicePipelineOutputsInputPaginateTypeDef]
    ) -> PageIterator[ListServicePipelineOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServicePipelineOutputs.html#Proton.Paginator.ListServicePipelineOutputs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicepipelineoutputspaginator)
        """

if TYPE_CHECKING:
    _ListServicePipelineProvisionedResourcesPaginatorBase = Paginator[
        ListServicePipelineProvisionedResourcesOutputTypeDef
    ]
else:
    _ListServicePipelineProvisionedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicePipelineProvisionedResourcesPaginator(
    _ListServicePipelineProvisionedResourcesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServicePipelineProvisionedResources.html#Proton.Paginator.ListServicePipelineProvisionedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicepipelineprovisionedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicePipelineProvisionedResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListServicePipelineProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServicePipelineProvisionedResources.html#Proton.Paginator.ListServicePipelineProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicepipelineprovisionedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListServiceTemplateVersionsPaginatorBase = Paginator[ListServiceTemplateVersionsOutputTypeDef]
else:
    _ListServiceTemplateVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceTemplateVersionsPaginator(_ListServiceTemplateVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceTemplateVersions.html#Proton.Paginator.ListServiceTemplateVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicetemplateversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceTemplateVersionsInputPaginateTypeDef]
    ) -> PageIterator[ListServiceTemplateVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceTemplateVersions.html#Proton.Paginator.ListServiceTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicetemplateversionspaginator)
        """

if TYPE_CHECKING:
    _ListServiceTemplatesPaginatorBase = Paginator[ListServiceTemplatesOutputTypeDef]
else:
    _ListServiceTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceTemplatesPaginator(_ListServiceTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceTemplates.html#Proton.Paginator.ListServiceTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicetemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListServiceTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServiceTemplates.html#Proton.Paginator.ListServiceTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicetemplatespaginator)
        """

if TYPE_CHECKING:
    _ListServicesPaginatorBase = Paginator[ListServicesOutputTypeDef]
else:
    _ListServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicesPaginator(_ListServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServices.html#Proton.Paginator.ListServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicesInputPaginateTypeDef]
    ) -> PageIterator[ListServicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListServices.html#Proton.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listservicespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceOutputTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListTagsForResource.html#Proton.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceInputPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton/paginator/ListTagsForResource.html#Proton.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators/#listtagsforresourcepaginator)
        """
