"""
Type annotations for workspaces-instances service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workspaces_instances.client import WorkspacesInstancesClient

    session = Session()
    client: WorkspacesInstancesClient = session.client("workspaces-instances")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListInstanceTypesPaginator,
    ListRegionsPaginator,
    ListWorkspaceInstancesPaginator,
)
from .type_defs import (
    AssociateVolumeRequestTypeDef,
    CreateVolumeRequestTypeDef,
    CreateVolumeResponseTypeDef,
    CreateWorkspaceInstanceRequestTypeDef,
    CreateWorkspaceInstanceResponseTypeDef,
    DeleteVolumeRequestTypeDef,
    DeleteWorkspaceInstanceRequestTypeDef,
    DisassociateVolumeRequestTypeDef,
    GetWorkspaceInstanceRequestTypeDef,
    GetWorkspaceInstanceResponseTypeDef,
    ListInstanceTypesRequestTypeDef,
    ListInstanceTypesResponseTypeDef,
    ListRegionsRequestTypeDef,
    ListRegionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkspaceInstancesRequestTypeDef,
    ListWorkspaceInstancesResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("WorkspacesInstancesClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class WorkspacesInstancesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances.html#WorkspacesInstances.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkspacesInstancesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances.html#WorkspacesInstances.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#generate_presigned_url)
        """

    def associate_volume(self, **kwargs: Unpack[AssociateVolumeRequestTypeDef]) -> Dict[str, Any]:
        """
        Attaches a volume to a WorkSpace Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/associate_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#associate_volume)
        """

    def create_volume(
        self, **kwargs: Unpack[CreateVolumeRequestTypeDef]
    ) -> CreateVolumeResponseTypeDef:
        """
        Creates a new volume for WorkSpace Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/create_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#create_volume)
        """

    def create_workspace_instance(
        self, **kwargs: Unpack[CreateWorkspaceInstanceRequestTypeDef]
    ) -> CreateWorkspaceInstanceResponseTypeDef:
        """
        Launches a new WorkSpace Instance with specified configuration parameters,
        enabling programmatic workspace deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/create_workspace_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#create_workspace_instance)
        """

    def delete_volume(self, **kwargs: Unpack[DeleteVolumeRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a specified volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/delete_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#delete_volume)
        """

    def delete_workspace_instance(
        self, **kwargs: Unpack[DeleteWorkspaceInstanceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified WorkSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/delete_workspace_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#delete_workspace_instance)
        """

    def disassociate_volume(
        self, **kwargs: Unpack[DisassociateVolumeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Detaches a volume from a WorkSpace Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/disassociate_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#disassociate_volume)
        """

    def get_workspace_instance(
        self, **kwargs: Unpack[GetWorkspaceInstanceRequestTypeDef]
    ) -> GetWorkspaceInstanceResponseTypeDef:
        """
        Retrieves detailed information about a specific WorkSpace Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/get_workspace_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#get_workspace_instance)
        """

    def list_instance_types(
        self, **kwargs: Unpack[ListInstanceTypesRequestTypeDef]
    ) -> ListInstanceTypesResponseTypeDef:
        """
        Retrieves a list of instance types supported by Amazon WorkSpaces Instances,
        enabling precise workspace infrastructure configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/list_instance_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#list_instance_types)
        """

    def list_regions(
        self, **kwargs: Unpack[ListRegionsRequestTypeDef]
    ) -> ListRegionsResponseTypeDef:
        """
        Retrieves a list of AWS regions supported by Amazon WorkSpaces Instances,
        enabling region discovery for workspace deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/list_regions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#list_regions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves tags for a WorkSpace Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#list_tags_for_resource)
        """

    def list_workspace_instances(
        self, **kwargs: Unpack[ListWorkspaceInstancesRequestTypeDef]
    ) -> ListWorkspaceInstancesResponseTypeDef:
        """
        Retrieves a collection of WorkSpaces Instances based on specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/list_workspace_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#list_workspace_instances)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to a WorkSpace Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a WorkSpace Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instance_types"]
    ) -> ListInstanceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_regions"]
    ) -> ListRegionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workspace_instances"]
    ) -> ListWorkspaceInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/client/#get_paginator)
        """
