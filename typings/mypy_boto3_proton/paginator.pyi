"""
Type annotations for proton service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_proton import ProtonClient
    from mypy_boto3_proton.paginator import (
        ListComponentOutputsPaginator,
        ListComponentProvisionedResourcesPaginator,
        ListComponentsPaginator,
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

    client: ProtonClient = boto3.client("proton")

    list_component_outputs_paginator: ListComponentOutputsPaginator = client.get_paginator("list_component_outputs")
    list_component_provisioned_resources_paginator: ListComponentProvisionedResourcesPaginator = client.get_paginator("list_component_provisioned_resources")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
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
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    RepositoryProviderType,
)
from .type_defs import (
    EnvironmentTemplateFilterTypeDef,
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
    ListServiceInstancesOutputTypeDef,
    ListServicePipelineOutputsOutputTypeDef,
    ListServicePipelineProvisionedResourcesOutputTypeDef,
    ListServicesOutputTypeDef,
    ListServiceTemplatesOutputTypeDef,
    ListServiceTemplateVersionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListComponentOutputsPaginator",
    "ListComponentProvisionedResourcesPaginator",
    "ListComponentsPaginator",
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

class ListComponentOutputsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListComponentOutputs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentoutputspaginator)
    """

    def paginate(
        self, *, componentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListComponentOutputs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentoutputspaginator)
        """

class ListComponentProvisionedResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListComponentProvisionedResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentprovisionedresourcespaginator)
    """

    def paginate(
        self, *, componentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListComponentProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentprovisionedresourcespaginator)
        """

class ListComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentspaginator)
    """

    def paginate(
        self,
        *,
        environmentName: str = None,
        serviceInstanceName: str = None,
        serviceName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listcomponentspaginator)
        """

class ListEnvironmentAccountConnectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentAccountConnections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentaccountconnectionspaginator)
    """

    def paginate(
        self,
        *,
        requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType,
        environmentName: str = None,
        statuses: List[EnvironmentAccountConnectionStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentAccountConnectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentAccountConnections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentaccountconnectionspaginator)
        """

class ListEnvironmentOutputsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentOutputs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentoutputspaginator)
    """

    def paginate(
        self, *, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentOutputs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentoutputspaginator)
        """

class ListEnvironmentProvisionedResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentProvisionedResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentprovisionedresourcespaginator)
    """

    def paginate(
        self, *, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentprovisionedresourcespaginator)
        """

class ListEnvironmentTemplateVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplateVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplateversionspaginator)
    """

    def paginate(
        self,
        *,
        templateName: str,
        majorVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentTemplateVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplateversionspaginator)
        """

class ListEnvironmentTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironmentTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmenttemplatespaginator)
        """

class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        environmentTemplates: List["EnvironmentTemplateFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listenvironmentspaginator)
        """

class ListRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListRepositories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listrepositoriespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListRepositories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listrepositoriespaginator)
        """

class ListRepositorySyncDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListRepositorySyncDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listrepositorysyncdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        syncType: Literal["TEMPLATE_SYNC"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositorySyncDefinitionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListRepositorySyncDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listrepositorysyncdefinitionspaginator)
        """

class ListServiceInstanceOutputsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceInstanceOutputs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstanceoutputspaginator)
    """

    def paginate(
        self,
        *,
        serviceInstanceName: str,
        serviceName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceInstanceOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceInstanceOutputs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstanceoutputspaginator)
        """

class ListServiceInstanceProvisionedResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceInstanceProvisionedResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstanceprovisionedresourcespaginator)
    """

    def paginate(
        self,
        *,
        serviceInstanceName: str,
        serviceName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceInstanceProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceInstanceProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstanceprovisionedresourcespaginator)
        """

class ListServiceInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstancespaginator)
    """

    def paginate(
        self, *, serviceName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listserviceinstancespaginator)
        """

class ListServicePipelineOutputsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServicePipelineOutputs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicepipelineoutputspaginator)
    """

    def paginate(
        self, *, serviceName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicePipelineOutputsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServicePipelineOutputs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicepipelineoutputspaginator)
        """

class ListServicePipelineProvisionedResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServicePipelineProvisionedResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicepipelineprovisionedresourcespaginator)
    """

    def paginate(
        self, *, serviceName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicePipelineProvisionedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServicePipelineProvisionedResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicepipelineprovisionedresourcespaginator)
        """

class ListServiceTemplateVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceTemplateVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplateversionspaginator)
    """

    def paginate(
        self,
        *,
        templateName: str,
        majorVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceTemplateVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplateversionspaginator)
        """

class ListServiceTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServiceTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicetemplatespaginator)
        """

class ListServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listservicespaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/proton.html#Proton.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/paginators.html#listtagsforresourcepaginator)
        """
