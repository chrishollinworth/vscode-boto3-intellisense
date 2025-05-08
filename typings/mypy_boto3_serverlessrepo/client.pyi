"""
Type annotations for serverlessrepo service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_serverlessrepo.client import ServerlessApplicationRepositoryClient

    session = Session()
    client: ServerlessApplicationRepositoryClient = session.client("serverlessrepo")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationDependenciesPaginator,
    ListApplicationsPaginator,
    ListApplicationVersionsPaginator,
)
from .type_defs import (
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateApplicationVersionRequestTypeDef,
    CreateApplicationVersionResponseTypeDef,
    CreateCloudFormationChangeSetRequestTypeDef,
    CreateCloudFormationChangeSetResponseTypeDef,
    CreateCloudFormationTemplateRequestTypeDef,
    CreateCloudFormationTemplateResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetApplicationPolicyRequestTypeDef,
    GetApplicationPolicyResponseTypeDef,
    GetApplicationRequestTypeDef,
    GetApplicationResponseTypeDef,
    GetCloudFormationTemplateRequestTypeDef,
    GetCloudFormationTemplateResponseTypeDef,
    ListApplicationDependenciesRequestTypeDef,
    ListApplicationDependenciesResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsRequestTypeDef,
    ListApplicationVersionsResponseTypeDef,
    PutApplicationPolicyRequestTypeDef,
    PutApplicationPolicyResponseTypeDef,
    UnshareApplicationRequestTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateApplicationResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ServerlessApplicationRepositoryClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class ServerlessApplicationRepositoryClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ServerlessApplicationRepositoryClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#generate_presigned_url)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an application, optionally including an AWS SAM file to create the
        first application version in the same call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#create_application)
        """

    def create_application_version(
        self, **kwargs: Unpack[CreateApplicationVersionRequestTypeDef]
    ) -> CreateApplicationVersionResponseTypeDef:
        """
        Creates an application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/create_application_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#create_application_version)
        """

    def create_cloud_formation_change_set(
        self, **kwargs: Unpack[CreateCloudFormationChangeSetRequestTypeDef]
    ) -> CreateCloudFormationChangeSetResponseTypeDef:
        """
        Creates an AWS CloudFormation change set for the given application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/create_cloud_formation_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#create_cloud_formation_change_set)
        """

    def create_cloud_formation_template(
        self, **kwargs: Unpack[CreateCloudFormationTemplateRequestTypeDef]
    ) -> CreateCloudFormationTemplateResponseTypeDef:
        """
        Creates an AWS CloudFormation template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/create_cloud_formation_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#create_cloud_formation_template)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#delete_application)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> GetApplicationResponseTypeDef:
        """
        Gets the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#get_application)
        """

    def get_application_policy(
        self, **kwargs: Unpack[GetApplicationPolicyRequestTypeDef]
    ) -> GetApplicationPolicyResponseTypeDef:
        """
        Retrieves the policy for the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/get_application_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#get_application_policy)
        """

    def get_cloud_formation_template(
        self, **kwargs: Unpack[GetCloudFormationTemplateRequestTypeDef]
    ) -> GetCloudFormationTemplateResponseTypeDef:
        """
        Gets the specified AWS CloudFormation template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/get_cloud_formation_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#get_cloud_formation_template)
        """

    def list_application_dependencies(
        self, **kwargs: Unpack[ListApplicationDependenciesRequestTypeDef]
    ) -> ListApplicationDependenciesResponseTypeDef:
        """
        Retrieves the list of applications nested in the containing application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/list_application_dependencies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#list_application_dependencies)
        """

    def list_application_versions(
        self, **kwargs: Unpack[ListApplicationVersionsRequestTypeDef]
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        Lists versions for the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/list_application_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#list_application_versions)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists applications owned by the requester.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#list_applications)
        """

    def put_application_policy(
        self, **kwargs: Unpack[PutApplicationPolicyRequestTypeDef]
    ) -> PutApplicationPolicyResponseTypeDef:
        """
        Sets the permission policy for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/put_application_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#put_application_policy)
        """

    def unshare_application(
        self, **kwargs: Unpack[UnshareApplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Unshares an application from an AWS Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/unshare_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#unshare_application)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#update_application)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_dependencies"]
    ) -> ListApplicationDependenciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_versions"]
    ) -> ListApplicationVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/client/#get_paginator)
        """
