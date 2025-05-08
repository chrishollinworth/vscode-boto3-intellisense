"""
Type annotations for iotthingsgraph service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotthingsgraph.client import IoTThingsGraphClient

    session = Session()
    client: IoTThingsGraphClient = session.client("iotthingsgraph")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetFlowTemplateRevisionsPaginator,
    GetSystemTemplateRevisionsPaginator,
    ListFlowExecutionMessagesPaginator,
    ListTagsForResourcePaginator,
    SearchEntitiesPaginator,
    SearchFlowExecutionsPaginator,
    SearchFlowTemplatesPaginator,
    SearchSystemInstancesPaginator,
    SearchSystemTemplatesPaginator,
    SearchThingsPaginator,
)
from .type_defs import (
    AssociateEntityToThingRequestTypeDef,
    CreateFlowTemplateRequestTypeDef,
    CreateFlowTemplateResponseTypeDef,
    CreateSystemInstanceRequestTypeDef,
    CreateSystemInstanceResponseTypeDef,
    CreateSystemTemplateRequestTypeDef,
    CreateSystemTemplateResponseTypeDef,
    DeleteFlowTemplateRequestTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeleteSystemInstanceRequestTypeDef,
    DeleteSystemTemplateRequestTypeDef,
    DeploySystemInstanceRequestTypeDef,
    DeploySystemInstanceResponseTypeDef,
    DeprecateFlowTemplateRequestTypeDef,
    DeprecateSystemTemplateRequestTypeDef,
    DescribeNamespaceRequestTypeDef,
    DescribeNamespaceResponseTypeDef,
    DissociateEntityFromThingRequestTypeDef,
    GetEntitiesRequestTypeDef,
    GetEntitiesResponseTypeDef,
    GetFlowTemplateRequestTypeDef,
    GetFlowTemplateResponseTypeDef,
    GetFlowTemplateRevisionsRequestTypeDef,
    GetFlowTemplateRevisionsResponseTypeDef,
    GetNamespaceDeletionStatusResponseTypeDef,
    GetSystemInstanceRequestTypeDef,
    GetSystemInstanceResponseTypeDef,
    GetSystemTemplateRequestTypeDef,
    GetSystemTemplateResponseTypeDef,
    GetSystemTemplateRevisionsRequestTypeDef,
    GetSystemTemplateRevisionsResponseTypeDef,
    GetUploadStatusRequestTypeDef,
    GetUploadStatusResponseTypeDef,
    ListFlowExecutionMessagesRequestTypeDef,
    ListFlowExecutionMessagesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    SearchEntitiesRequestTypeDef,
    SearchEntitiesResponseTypeDef,
    SearchFlowExecutionsRequestTypeDef,
    SearchFlowExecutionsResponseTypeDef,
    SearchFlowTemplatesRequestTypeDef,
    SearchFlowTemplatesResponseTypeDef,
    SearchSystemInstancesRequestTypeDef,
    SearchSystemInstancesResponseTypeDef,
    SearchSystemTemplatesRequestTypeDef,
    SearchSystemTemplatesResponseTypeDef,
    SearchThingsRequestTypeDef,
    SearchThingsResponseTypeDef,
    TagResourceRequestTypeDef,
    UndeploySystemInstanceRequestTypeDef,
    UndeploySystemInstanceResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateFlowTemplateRequestTypeDef,
    UpdateFlowTemplateResponseTypeDef,
    UpdateSystemTemplateRequestTypeDef,
    UpdateSystemTemplateResponseTypeDef,
    UploadEntityDefinitionsRequestTypeDef,
    UploadEntityDefinitionsResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("IoTThingsGraphClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class IoTThingsGraphClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTThingsGraphClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#generate_presigned_url)
        """

    def associate_entity_to_thing(
        self, **kwargs: Unpack[AssociateEntityToThingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a device with a concrete thing that is in the user's registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/associate_entity_to_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#associate_entity_to_thing)
        """

    def create_flow_template(
        self, **kwargs: Unpack[CreateFlowTemplateRequestTypeDef]
    ) -> CreateFlowTemplateResponseTypeDef:
        """
        Creates a workflow template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/create_flow_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#create_flow_template)
        """

    def create_system_instance(
        self, **kwargs: Unpack[CreateSystemInstanceRequestTypeDef]
    ) -> CreateSystemInstanceResponseTypeDef:
        """
        Creates a system instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/create_system_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#create_system_instance)
        """

    def create_system_template(
        self, **kwargs: Unpack[CreateSystemTemplateRequestTypeDef]
    ) -> CreateSystemTemplateResponseTypeDef:
        """
        Creates a system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/create_system_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#create_system_template)
        """

    def delete_flow_template(
        self, **kwargs: Unpack[DeleteFlowTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/delete_flow_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#delete_flow_template)
        """

    def delete_namespace(self) -> DeleteNamespaceResponseTypeDef:
        """
        Deletes the specified namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/delete_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#delete_namespace)
        """

    def delete_system_instance(
        self, **kwargs: Unpack[DeleteSystemInstanceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a system instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/delete_system_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#delete_system_instance)
        """

    def delete_system_template(
        self, **kwargs: Unpack[DeleteSystemTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/delete_system_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#delete_system_template)
        """

    def deploy_system_instance(
        self, **kwargs: Unpack[DeploySystemInstanceRequestTypeDef]
    ) -> DeploySystemInstanceResponseTypeDef:
        """
        <b>Greengrass and Cloud Deployments</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/deploy_system_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#deploy_system_instance)
        """

    def deprecate_flow_template(
        self, **kwargs: Unpack[DeprecateFlowTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deprecates the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/deprecate_flow_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#deprecate_flow_template)
        """

    def deprecate_system_template(
        self, **kwargs: Unpack[DeprecateSystemTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deprecates the specified system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/deprecate_system_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#deprecate_system_template)
        """

    def describe_namespace(
        self, **kwargs: Unpack[DescribeNamespaceRequestTypeDef]
    ) -> DescribeNamespaceResponseTypeDef:
        """
        Gets the latest version of the user's namespace and the public version that it
        is tracking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/describe_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#describe_namespace)
        """

    def dissociate_entity_from_thing(
        self, **kwargs: Unpack[DissociateEntityFromThingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Dissociates a device entity from a concrete thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/dissociate_entity_from_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#dissociate_entity_from_thing)
        """

    def get_entities(
        self, **kwargs: Unpack[GetEntitiesRequestTypeDef]
    ) -> GetEntitiesResponseTypeDef:
        """
        Gets definitions of the specified entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_entities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_entities)
        """

    def get_flow_template(
        self, **kwargs: Unpack[GetFlowTemplateRequestTypeDef]
    ) -> GetFlowTemplateResponseTypeDef:
        """
        Gets the latest version of the <code>DefinitionDocument</code> and
        <code>FlowTemplateSummary</code> for the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_flow_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_flow_template)
        """

    def get_flow_template_revisions(
        self, **kwargs: Unpack[GetFlowTemplateRevisionsRequestTypeDef]
    ) -> GetFlowTemplateRevisionsResponseTypeDef:
        """
        Gets revisions of the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_flow_template_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_flow_template_revisions)
        """

    def get_namespace_deletion_status(self) -> GetNamespaceDeletionStatusResponseTypeDef:
        """
        Gets the status of a namespace deletion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_namespace_deletion_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_namespace_deletion_status)
        """

    def get_system_instance(
        self, **kwargs: Unpack[GetSystemInstanceRequestTypeDef]
    ) -> GetSystemInstanceResponseTypeDef:
        """
        Gets a system instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_system_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_system_instance)
        """

    def get_system_template(
        self, **kwargs: Unpack[GetSystemTemplateRequestTypeDef]
    ) -> GetSystemTemplateResponseTypeDef:
        """
        Gets a system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_system_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_system_template)
        """

    def get_system_template_revisions(
        self, **kwargs: Unpack[GetSystemTemplateRevisionsRequestTypeDef]
    ) -> GetSystemTemplateRevisionsResponseTypeDef:
        """
        Gets revisions made to the specified system template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_system_template_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_system_template_revisions)
        """

    def get_upload_status(
        self, **kwargs: Unpack[GetUploadStatusRequestTypeDef]
    ) -> GetUploadStatusResponseTypeDef:
        """
        Gets the status of the specified upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_upload_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_upload_status)
        """

    def list_flow_execution_messages(
        self, **kwargs: Unpack[ListFlowExecutionMessagesRequestTypeDef]
    ) -> ListFlowExecutionMessagesResponseTypeDef:
        """
        Returns a list of objects that contain information about events in a flow
        execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/list_flow_execution_messages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#list_flow_execution_messages)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags on an AWS IoT Things Graph resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#list_tags_for_resource)
        """

    def search_entities(
        self, **kwargs: Unpack[SearchEntitiesRequestTypeDef]
    ) -> SearchEntitiesResponseTypeDef:
        """
        Searches for entities of the specified type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/search_entities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#search_entities)
        """

    def search_flow_executions(
        self, **kwargs: Unpack[SearchFlowExecutionsRequestTypeDef]
    ) -> SearchFlowExecutionsResponseTypeDef:
        """
        Searches for AWS IoT Things Graph workflow execution instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/search_flow_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#search_flow_executions)
        """

    def search_flow_templates(
        self, **kwargs: Unpack[SearchFlowTemplatesRequestTypeDef]
    ) -> SearchFlowTemplatesResponseTypeDef:
        """
        Searches for summary information about workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/search_flow_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#search_flow_templates)
        """

    def search_system_instances(
        self, **kwargs: Unpack[SearchSystemInstancesRequestTypeDef]
    ) -> SearchSystemInstancesResponseTypeDef:
        """
        Searches for system instances in the user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/search_system_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#search_system_instances)
        """

    def search_system_templates(
        self, **kwargs: Unpack[SearchSystemTemplatesRequestTypeDef]
    ) -> SearchSystemTemplatesResponseTypeDef:
        """
        Searches for summary information about systems in the user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/search_system_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#search_system_templates)
        """

    def search_things(
        self, **kwargs: Unpack[SearchThingsRequestTypeDef]
    ) -> SearchThingsResponseTypeDef:
        """
        Searches for things associated with the specified entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/search_things.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#search_things)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a tag for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#tag_resource)
        """

    def undeploy_system_instance(
        self, **kwargs: Unpack[UndeploySystemInstanceRequestTypeDef]
    ) -> UndeploySystemInstanceResponseTypeDef:
        """
        Removes a system instance from its target (Cloud or Greengrass).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/undeploy_system_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#undeploy_system_instance)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#untag_resource)
        """

    def update_flow_template(
        self, **kwargs: Unpack[UpdateFlowTemplateRequestTypeDef]
    ) -> UpdateFlowTemplateResponseTypeDef:
        """
        Updates the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/update_flow_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#update_flow_template)
        """

    def update_system_template(
        self, **kwargs: Unpack[UpdateSystemTemplateRequestTypeDef]
    ) -> UpdateSystemTemplateResponseTypeDef:
        """
        Updates the specified system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/update_system_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#update_system_template)
        """

    def upload_entity_definitions(
        self, **kwargs: Unpack[UploadEntityDefinitionsRequestTypeDef]
    ) -> UploadEntityDefinitionsResponseTypeDef:
        """
        Asynchronously uploads one or more entity definitions to the user's namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/upload_entity_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#upload_entity_definitions)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_flow_template_revisions"]
    ) -> GetFlowTemplateRevisionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_system_template_revisions"]
    ) -> GetSystemTemplateRevisionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flow_execution_messages"]
    ) -> ListFlowExecutionMessagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_entities"]
    ) -> SearchEntitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_flow_executions"]
    ) -> SearchFlowExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_flow_templates"]
    ) -> SearchFlowTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_system_instances"]
    ) -> SearchSystemInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_system_templates"]
    ) -> SearchSystemTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_things"]
    ) -> SearchThingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client/#get_paginator)
        """
