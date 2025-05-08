"""
Type annotations for migration-hub-refactor-spaces service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient

    session = Session()
    client: MigrationHubRefactorSpacesClient = session.client("migration-hub-refactor-spaces")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationsPaginator,
    ListEnvironmentsPaginator,
    ListEnvironmentVpcsPaginator,
    ListRoutesPaginator,
    ListServicesPaginator,
)
from .type_defs import (
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateEnvironmentRequestTypeDef,
    CreateEnvironmentResponseTypeDef,
    CreateRouteRequestTypeDef,
    CreateRouteResponseTypeDef,
    CreateServiceRequestTypeDef,
    CreateServiceResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteApplicationResponseTypeDef,
    DeleteEnvironmentRequestTypeDef,
    DeleteEnvironmentResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteRouteRequestTypeDef,
    DeleteRouteResponseTypeDef,
    DeleteServiceRequestTypeDef,
    DeleteServiceResponseTypeDef,
    GetApplicationRequestTypeDef,
    GetApplicationResponseTypeDef,
    GetEnvironmentRequestTypeDef,
    GetEnvironmentResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetRouteRequestTypeDef,
    GetRouteResponseTypeDef,
    GetServiceRequestTypeDef,
    GetServiceResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListEnvironmentsRequestTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListEnvironmentVpcsRequestTypeDef,
    ListEnvironmentVpcsResponseTypeDef,
    ListRoutesRequestTypeDef,
    ListRoutesResponseTypeDef,
    ListServicesRequestTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateRouteRequestTypeDef,
    UpdateRouteResponseTypeDef,
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

__all__ = ("MigrationHubRefactorSpacesClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidResourcePolicyException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MigrationHubRefactorSpacesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubRefactorSpacesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#generate_presigned_url)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an Amazon Web Services Migration Hub Refactor Spaces application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#create_application)
        """

    def create_environment(
        self, **kwargs: Unpack[CreateEnvironmentRequestTypeDef]
    ) -> CreateEnvironmentResponseTypeDef:
        """
        Creates an Amazon Web Services Migration Hub Refactor Spaces environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/create_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#create_environment)
        """

    def create_route(
        self, **kwargs: Unpack[CreateRouteRequestTypeDef]
    ) -> CreateRouteResponseTypeDef:
        """
        Creates an Amazon Web Services Migration Hub Refactor Spaces route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/create_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#create_route)
        """

    def create_service(
        self, **kwargs: Unpack[CreateServiceRequestTypeDef]
    ) -> CreateServiceResponseTypeDef:
        """
        Creates an Amazon Web Services Migration Hub Refactor Spaces service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/create_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#create_service)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> DeleteApplicationResponseTypeDef:
        """
        Deletes an Amazon Web Services Migration Hub Refactor Spaces application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#delete_application)
        """

    def delete_environment(
        self, **kwargs: Unpack[DeleteEnvironmentRequestTypeDef]
    ) -> DeleteEnvironmentResponseTypeDef:
        """
        Deletes an Amazon Web Services Migration Hub Refactor Spaces environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/delete_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#delete_environment)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the resource policy set for the environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#delete_resource_policy)
        """

    def delete_route(
        self, **kwargs: Unpack[DeleteRouteRequestTypeDef]
    ) -> DeleteRouteResponseTypeDef:
        """
        Deletes an Amazon Web Services Migration Hub Refactor Spaces route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/delete_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#delete_route)
        """

    def delete_service(
        self, **kwargs: Unpack[DeleteServiceRequestTypeDef]
    ) -> DeleteServiceResponseTypeDef:
        """
        Deletes an Amazon Web Services Migration Hub Refactor Spaces service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/delete_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#delete_service)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> GetApplicationResponseTypeDef:
        """
        Gets an Amazon Web Services Migration Hub Refactor Spaces application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_application)
        """

    def get_environment(
        self, **kwargs: Unpack[GetEnvironmentRequestTypeDef]
    ) -> GetEnvironmentResponseTypeDef:
        """
        Gets an Amazon Web Services Migration Hub Refactor Spaces environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_environment)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Gets the resource-based permission policy that is set for the given environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_resource_policy)
        """

    def get_route(self, **kwargs: Unpack[GetRouteRequestTypeDef]) -> GetRouteResponseTypeDef:
        """
        Gets an Amazon Web Services Migration Hub Refactor Spaces route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_route)
        """

    def get_service(self, **kwargs: Unpack[GetServiceRequestTypeDef]) -> GetServiceResponseTypeDef:
        """
        Gets an Amazon Web Services Migration Hub Refactor Spaces service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_service)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists all the Amazon Web Services Migration Hub Refactor Spaces applications
        within an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#list_applications)
        """

    def list_environment_vpcs(
        self, **kwargs: Unpack[ListEnvironmentVpcsRequestTypeDef]
    ) -> ListEnvironmentVpcsResponseTypeDef:
        """
        Lists all Amazon Web Services Migration Hub Refactor Spaces service virtual
        private clouds (VPCs) that are part of the environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/list_environment_vpcs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#list_environment_vpcs)
        """

    def list_environments(
        self, **kwargs: Unpack[ListEnvironmentsRequestTypeDef]
    ) -> ListEnvironmentsResponseTypeDef:
        """
        Lists Amazon Web Services Migration Hub Refactor Spaces environments owned by a
        caller account or shared with the caller account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/list_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#list_environments)
        """

    def list_routes(self, **kwargs: Unpack[ListRoutesRequestTypeDef]) -> ListRoutesResponseTypeDef:
        """
        Lists all the Amazon Web Services Migration Hub Refactor Spaces routes within
        an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/list_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#list_routes)
        """

    def list_services(
        self, **kwargs: Unpack[ListServicesRequestTypeDef]
    ) -> ListServicesResponseTypeDef:
        """
        Lists all the Amazon Web Services Migration Hub Refactor Spaces services within
        an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/list_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#list_services)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#list_tags_for_resource)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attaches a resource-based permission policy to the Amazon Web Services
        Migration Hub Refactor Spaces environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#put_resource_policy)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the tags of a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#untag_resource)
        """

    def update_route(
        self, **kwargs: Unpack[UpdateRouteRequestTypeDef]
    ) -> UpdateRouteResponseTypeDef:
        """
        Updates an Amazon Web Services Migration Hub Refactor Spaces route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/update_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#update_route)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environment_vpcs"]
    ) -> ListEnvironmentVpcsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_routes"]
    ) -> ListRoutesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_services"]
    ) -> ListServicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/client/#get_paginator)
        """
