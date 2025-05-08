"""
Type annotations for amplify service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_amplify.client import AmplifyClient

    session = Session()
    client: AmplifyClient = session.client("amplify")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAppsPaginator,
    ListBranchesPaginator,
    ListDomainAssociationsPaginator,
    ListJobsPaginator,
)
from .type_defs import (
    CreateAppRequestTypeDef,
    CreateAppResultTypeDef,
    CreateBackendEnvironmentRequestTypeDef,
    CreateBackendEnvironmentResultTypeDef,
    CreateBranchRequestTypeDef,
    CreateBranchResultTypeDef,
    CreateDeploymentRequestTypeDef,
    CreateDeploymentResultTypeDef,
    CreateDomainAssociationRequestTypeDef,
    CreateDomainAssociationResultTypeDef,
    CreateWebhookRequestTypeDef,
    CreateWebhookResultTypeDef,
    DeleteAppRequestTypeDef,
    DeleteAppResultTypeDef,
    DeleteBackendEnvironmentRequestTypeDef,
    DeleteBackendEnvironmentResultTypeDef,
    DeleteBranchRequestTypeDef,
    DeleteBranchResultTypeDef,
    DeleteDomainAssociationRequestTypeDef,
    DeleteDomainAssociationResultTypeDef,
    DeleteJobRequestTypeDef,
    DeleteJobResultTypeDef,
    DeleteWebhookRequestTypeDef,
    DeleteWebhookResultTypeDef,
    GenerateAccessLogsRequestTypeDef,
    GenerateAccessLogsResultTypeDef,
    GetAppRequestTypeDef,
    GetAppResultTypeDef,
    GetArtifactUrlRequestTypeDef,
    GetArtifactUrlResultTypeDef,
    GetBackendEnvironmentRequestTypeDef,
    GetBackendEnvironmentResultTypeDef,
    GetBranchRequestTypeDef,
    GetBranchResultTypeDef,
    GetDomainAssociationRequestTypeDef,
    GetDomainAssociationResultTypeDef,
    GetJobRequestTypeDef,
    GetJobResultTypeDef,
    GetWebhookRequestTypeDef,
    GetWebhookResultTypeDef,
    ListAppsRequestTypeDef,
    ListAppsResultTypeDef,
    ListArtifactsRequestTypeDef,
    ListArtifactsResultTypeDef,
    ListBackendEnvironmentsRequestTypeDef,
    ListBackendEnvironmentsResultTypeDef,
    ListBranchesRequestTypeDef,
    ListBranchesResultTypeDef,
    ListDomainAssociationsRequestTypeDef,
    ListDomainAssociationsResultTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebhooksRequestTypeDef,
    ListWebhooksResultTypeDef,
    StartDeploymentRequestTypeDef,
    StartDeploymentResultTypeDef,
    StartJobRequestTypeDef,
    StartJobResultTypeDef,
    StopJobRequestTypeDef,
    StopJobResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAppRequestTypeDef,
    UpdateAppResultTypeDef,
    UpdateBranchRequestTypeDef,
    UpdateBranchResultTypeDef,
    UpdateDomainAssociationRequestTypeDef,
    UpdateDomainAssociationResultTypeDef,
    UpdateWebhookRequestTypeDef,
    UpdateWebhookResultTypeDef,
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

__all__ = ("AmplifyClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DependentServiceFailureException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class AmplifyClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AmplifyClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#generate_presigned_url)
        """

    def create_app(self, **kwargs: Unpack[CreateAppRequestTypeDef]) -> CreateAppResultTypeDef:
        """
        Creates a new Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/create_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#create_app)
        """

    def create_backend_environment(
        self, **kwargs: Unpack[CreateBackendEnvironmentRequestTypeDef]
    ) -> CreateBackendEnvironmentResultTypeDef:
        """
        Creates a new backend environment for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/create_backend_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#create_backend_environment)
        """

    def create_branch(
        self, **kwargs: Unpack[CreateBranchRequestTypeDef]
    ) -> CreateBranchResultTypeDef:
        """
        Creates a new branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/create_branch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#create_branch)
        """

    def create_deployment(
        self, **kwargs: Unpack[CreateDeploymentRequestTypeDef]
    ) -> CreateDeploymentResultTypeDef:
        """
        Creates a deployment for a manually deployed Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/create_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#create_deployment)
        """

    def create_domain_association(
        self, **kwargs: Unpack[CreateDomainAssociationRequestTypeDef]
    ) -> CreateDomainAssociationResultTypeDef:
        """
        Creates a new domain association for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/create_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#create_domain_association)
        """

    def create_webhook(
        self, **kwargs: Unpack[CreateWebhookRequestTypeDef]
    ) -> CreateWebhookResultTypeDef:
        """
        Creates a new webhook on an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/create_webhook.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#create_webhook)
        """

    def delete_app(self, **kwargs: Unpack[DeleteAppRequestTypeDef]) -> DeleteAppResultTypeDef:
        """
        Deletes an existing Amplify app specified by an app ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/delete_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#delete_app)
        """

    def delete_backend_environment(
        self, **kwargs: Unpack[DeleteBackendEnvironmentRequestTypeDef]
    ) -> DeleteBackendEnvironmentResultTypeDef:
        """
        Deletes a backend environment for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/delete_backend_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#delete_backend_environment)
        """

    def delete_branch(
        self, **kwargs: Unpack[DeleteBranchRequestTypeDef]
    ) -> DeleteBranchResultTypeDef:
        """
        Deletes a branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/delete_branch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#delete_branch)
        """

    def delete_domain_association(
        self, **kwargs: Unpack[DeleteDomainAssociationRequestTypeDef]
    ) -> DeleteDomainAssociationResultTypeDef:
        """
        Deletes a domain association for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/delete_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#delete_domain_association)
        """

    def delete_job(self, **kwargs: Unpack[DeleteJobRequestTypeDef]) -> DeleteJobResultTypeDef:
        """
        Deletes a job for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/delete_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#delete_job)
        """

    def delete_webhook(
        self, **kwargs: Unpack[DeleteWebhookRequestTypeDef]
    ) -> DeleteWebhookResultTypeDef:
        """
        Deletes a webhook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/delete_webhook.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#delete_webhook)
        """

    def generate_access_logs(
        self, **kwargs: Unpack[GenerateAccessLogsRequestTypeDef]
    ) -> GenerateAccessLogsResultTypeDef:
        """
        Returns the website access logs for a specific time range using a presigned URL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/generate_access_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#generate_access_logs)
        """

    def get_app(self, **kwargs: Unpack[GetAppRequestTypeDef]) -> GetAppResultTypeDef:
        """
        Returns an existing Amplify app specified by an app ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_app)
        """

    def get_artifact_url(
        self, **kwargs: Unpack[GetArtifactUrlRequestTypeDef]
    ) -> GetArtifactUrlResultTypeDef:
        """
        Returns the artifact info that corresponds to an artifact id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_artifact_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_artifact_url)
        """

    def get_backend_environment(
        self, **kwargs: Unpack[GetBackendEnvironmentRequestTypeDef]
    ) -> GetBackendEnvironmentResultTypeDef:
        """
        Returns a backend environment for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_backend_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_backend_environment)
        """

    def get_branch(self, **kwargs: Unpack[GetBranchRequestTypeDef]) -> GetBranchResultTypeDef:
        """
        Returns a branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_branch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_branch)
        """

    def get_domain_association(
        self, **kwargs: Unpack[GetDomainAssociationRequestTypeDef]
    ) -> GetDomainAssociationResultTypeDef:
        """
        Returns the domain information for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_domain_association)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestTypeDef]) -> GetJobResultTypeDef:
        """
        Returns a job for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_job)
        """

    def get_webhook(self, **kwargs: Unpack[GetWebhookRequestTypeDef]) -> GetWebhookResultTypeDef:
        """
        Returns the webhook information that corresponds to a specified webhook ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_webhook.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_webhook)
        """

    def list_apps(self, **kwargs: Unpack[ListAppsRequestTypeDef]) -> ListAppsResultTypeDef:
        """
        Returns a list of the existing Amplify apps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_apps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_apps)
        """

    def list_artifacts(
        self, **kwargs: Unpack[ListArtifactsRequestTypeDef]
    ) -> ListArtifactsResultTypeDef:
        """
        Returns a list of end-to-end testing artifacts for a specified app, branch, and
        job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_artifacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_artifacts)
        """

    def list_backend_environments(
        self, **kwargs: Unpack[ListBackendEnvironmentsRequestTypeDef]
    ) -> ListBackendEnvironmentsResultTypeDef:
        """
        Lists the backend environments for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_backend_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_backend_environments)
        """

    def list_branches(
        self, **kwargs: Unpack[ListBranchesRequestTypeDef]
    ) -> ListBranchesResultTypeDef:
        """
        Lists the branches of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_branches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_branches)
        """

    def list_domain_associations(
        self, **kwargs: Unpack[ListDomainAssociationsRequestTypeDef]
    ) -> ListDomainAssociationsResultTypeDef:
        """
        Returns the domain associations for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_domain_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_domain_associations)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResultTypeDef:
        """
        Lists the jobs for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_jobs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a specified Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_tags_for_resource)
        """

    def list_webhooks(
        self, **kwargs: Unpack[ListWebhooksRequestTypeDef]
    ) -> ListWebhooksResultTypeDef:
        """
        Returns a list of webhooks for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/list_webhooks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#list_webhooks)
        """

    def start_deployment(
        self, **kwargs: Unpack[StartDeploymentRequestTypeDef]
    ) -> StartDeploymentResultTypeDef:
        """
        Starts a deployment for a manually deployed app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/start_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#start_deployment)
        """

    def start_job(self, **kwargs: Unpack[StartJobRequestTypeDef]) -> StartJobResultTypeDef:
        """
        Starts a new job for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/start_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#start_job)
        """

    def stop_job(self, **kwargs: Unpack[StopJobRequestTypeDef]) -> StopJobResultTypeDef:
        """
        Stops a job that is in progress for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/stop_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#stop_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags the resource with a tag key and value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Untags a resource with a specified Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#untag_resource)
        """

    def update_app(self, **kwargs: Unpack[UpdateAppRequestTypeDef]) -> UpdateAppResultTypeDef:
        """
        Updates an existing Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/update_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#update_app)
        """

    def update_branch(
        self, **kwargs: Unpack[UpdateBranchRequestTypeDef]
    ) -> UpdateBranchResultTypeDef:
        """
        Updates a branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/update_branch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#update_branch)
        """

    def update_domain_association(
        self, **kwargs: Unpack[UpdateDomainAssociationRequestTypeDef]
    ) -> UpdateDomainAssociationResultTypeDef:
        """
        Creates a new domain association for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/update_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#update_domain_association)
        """

    def update_webhook(
        self, **kwargs: Unpack[UpdateWebhookRequestTypeDef]
    ) -> UpdateWebhookResultTypeDef:
        """
        Updates a webhook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/update_webhook.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#update_webhook)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_apps"]
    ) -> ListAppsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_branches"]
    ) -> ListBranchesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domain_associations"]
    ) -> ListDomainAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/client/#get_paginator)
        """
