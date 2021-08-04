"""
Type annotations for amplify service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_amplify import AmplifyClient

    client: AmplifyClient = boto3.client("amplify")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import JobTypeType, StageType
from .paginator import (
    ListAppsPaginator,
    ListBranchesPaginator,
    ListDomainAssociationsPaginator,
    ListJobsPaginator,
)
from .type_defs import (
    AutoBranchCreationConfigTypeDef,
    CreateAppResultTypeDef,
    CreateBackendEnvironmentResultTypeDef,
    CreateBranchResultTypeDef,
    CreateDeploymentResultTypeDef,
    CreateDomainAssociationResultTypeDef,
    CreateWebhookResultTypeDef,
    CustomRuleTypeDef,
    DeleteAppResultTypeDef,
    DeleteBackendEnvironmentResultTypeDef,
    DeleteBranchResultTypeDef,
    DeleteDomainAssociationResultTypeDef,
    DeleteJobResultTypeDef,
    DeleteWebhookResultTypeDef,
    GenerateAccessLogsResultTypeDef,
    GetAppResultTypeDef,
    GetArtifactUrlResultTypeDef,
    GetBackendEnvironmentResultTypeDef,
    GetBranchResultTypeDef,
    GetDomainAssociationResultTypeDef,
    GetJobResultTypeDef,
    GetWebhookResultTypeDef,
    ListAppsResultTypeDef,
    ListArtifactsResultTypeDef,
    ListBackendEnvironmentsResultTypeDef,
    ListBranchesResultTypeDef,
    ListDomainAssociationsResultTypeDef,
    ListJobsResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebhooksResultTypeDef,
    StartDeploymentResultTypeDef,
    StartJobResultTypeDef,
    StopJobResultTypeDef,
    SubDomainSettingTypeDef,
    UpdateAppResultTypeDef,
    UpdateBranchResultTypeDef,
    UpdateDomainAssociationResultTypeDef,
    UpdateWebhookResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AmplifyClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        AmplifyClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#can_paginate)
        """
    def create_app(
        self,
        *,
        name: str,
        description: str = None,
        repository: str = None,
        platform: Literal["WEB"] = None,
        iamServiceRoleArn: str = None,
        oauthToken: str = None,
        accessToken: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBranchAutoDeletion: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List["CustomRuleTypeDef"] = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        customHeaders: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: "AutoBranchCreationConfigTypeDef" = None
    ) -> CreateAppResultTypeDef:
        """
        Creates a new Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#create_app)
        """
    def create_backend_environment(
        self,
        *,
        appId: str,
        environmentName: str,
        stackName: str = None,
        deploymentArtifacts: str = None
    ) -> CreateBackendEnvironmentResultTypeDef:
        """
        Creates a new backend environment for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.create_backend_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#create_backend_environment)
        """
    def create_branch(
        self,
        *,
        appId: str,
        branchName: str,
        description: str = None,
        stage: StageType = None,
        framework: str = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        enablePerformanceMode: bool = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None
    ) -> CreateBranchResultTypeDef:
        """
        Creates a new branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.create_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#create_branch)
        """
    def create_deployment(
        self, *, appId: str, branchName: str, fileMap: Dict[str, str] = None
    ) -> CreateDeploymentResultTypeDef:
        """
        Creates a deployment for a manually deployed Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#create_deployment)
        """
    def create_domain_association(
        self,
        *,
        appId: str,
        domainName: str,
        subDomainSettings: List["SubDomainSettingTypeDef"],
        enableAutoSubDomain: bool = None,
        autoSubDomainCreationPatterns: List[str] = None,
        autoSubDomainIAMRole: str = None
    ) -> CreateDomainAssociationResultTypeDef:
        """
        Creates a new domain association for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.create_domain_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#create_domain_association)
        """
    def create_webhook(
        self, *, appId: str, branchName: str, description: str = None
    ) -> CreateWebhookResultTypeDef:
        """
        Creates a new webhook on an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.create_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#create_webhook)
        """
    def delete_app(self, *, appId: str) -> DeleteAppResultTypeDef:
        """
        Deletes an existing Amplify app specified by an app ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#delete_app)
        """
    def delete_backend_environment(
        self, *, appId: str, environmentName: str
    ) -> DeleteBackendEnvironmentResultTypeDef:
        """
        Deletes a backend environment for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.delete_backend_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#delete_backend_environment)
        """
    def delete_branch(self, *, appId: str, branchName: str) -> DeleteBranchResultTypeDef:
        """
        Deletes a branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.delete_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#delete_branch)
        """
    def delete_domain_association(
        self, *, appId: str, domainName: str
    ) -> DeleteDomainAssociationResultTypeDef:
        """
        Deletes a domain association for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.delete_domain_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#delete_domain_association)
        """
    def delete_job(self, *, appId: str, branchName: str, jobId: str) -> DeleteJobResultTypeDef:
        """
        Deletes a job for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#delete_job)
        """
    def delete_webhook(self, *, webhookId: str) -> DeleteWebhookResultTypeDef:
        """
        Deletes a webhook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.delete_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#delete_webhook)
        """
    def generate_access_logs(
        self,
        *,
        domainName: str,
        appId: str,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None
    ) -> GenerateAccessLogsResultTypeDef:
        """
        Returns the website access logs for a specific time range using a presigned URL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.generate_access_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#generate_access_logs)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#generate_presigned_url)
        """
    def get_app(self, *, appId: str) -> GetAppResultTypeDef:
        """
        Returns an existing Amplify app by appID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.get_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#get_app)
        """
    def get_artifact_url(self, *, artifactId: str) -> GetArtifactUrlResultTypeDef:
        """
        Returns the artifact info that corresponds to an artifact id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.get_artifact_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#get_artifact_url)
        """
    def get_backend_environment(
        self, *, appId: str, environmentName: str
    ) -> GetBackendEnvironmentResultTypeDef:
        """
        Returns a backend environment for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.get_backend_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#get_backend_environment)
        """
    def get_branch(self, *, appId: str, branchName: str) -> GetBranchResultTypeDef:
        """
        Returns a branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.get_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#get_branch)
        """
    def get_domain_association(
        self, *, appId: str, domainName: str
    ) -> GetDomainAssociationResultTypeDef:
        """
        Returns the domain information for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.get_domain_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#get_domain_association)
        """
    def get_job(self, *, appId: str, branchName: str, jobId: str) -> GetJobResultTypeDef:
        """
        Returns a job for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.get_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#get_job)
        """
    def get_webhook(self, *, webhookId: str) -> GetWebhookResultTypeDef:
        """
        Returns the webhook information that corresponds to a specified webhook ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.get_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#get_webhook)
        """
    def list_apps(self, *, nextToken: str = None, maxResults: int = None) -> ListAppsResultTypeDef:
        """
        Returns a list of the existing Amplify apps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_apps)
        """
    def list_artifacts(
        self,
        *,
        appId: str,
        branchName: str,
        jobId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListArtifactsResultTypeDef:
        """
        Returns a list of artifacts for a specified app, branch, and job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_artifacts)
        """
    def list_backend_environments(
        self,
        *,
        appId: str,
        environmentName: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListBackendEnvironmentsResultTypeDef:
        """
        Lists the backend environments for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_backend_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_backend_environments)
        """
    def list_branches(
        self, *, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ListBranchesResultTypeDef:
        """
        Lists the branches of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_branches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_branches)
        """
    def list_domain_associations(
        self, *, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDomainAssociationsResultTypeDef:
        """
        Returns the domain associations for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_domain_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_domain_associations)
        """
    def list_jobs(
        self, *, appId: str, branchName: str, nextToken: str = None, maxResults: int = None
    ) -> ListJobsResultTypeDef:
        """
        Lists the jobs for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_jobs)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a specified Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_tags_for_resource)
        """
    def list_webhooks(
        self, *, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ListWebhooksResultTypeDef:
        """
        Returns a list of webhooks for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.list_webhooks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#list_webhooks)
        """
    def start_deployment(
        self, *, appId: str, branchName: str, jobId: str = None, sourceUrl: str = None
    ) -> StartDeploymentResultTypeDef:
        """
        Starts a deployment for a manually deployed app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.start_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#start_deployment)
        """
    def start_job(
        self,
        *,
        appId: str,
        branchName: str,
        jobType: JobTypeType,
        jobId: str = None,
        jobReason: str = None,
        commitId: str = None,
        commitMessage: str = None,
        commitTime: Union[datetime, str] = None
    ) -> StartJobResultTypeDef:
        """
        Starts a new job for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.start_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#start_job)
        """
    def stop_job(self, *, appId: str, branchName: str, jobId: str) -> StopJobResultTypeDef:
        """
        Stops a job that is in progress for a branch of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.stop_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#stop_job)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags the resource with a tag key and value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Untags a resource with a specified Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#untag_resource)
        """
    def update_app(
        self,
        *,
        appId: str,
        name: str = None,
        description: str = None,
        platform: Literal["WEB"] = None,
        iamServiceRoleArn: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBranchAutoDeletion: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List["CustomRuleTypeDef"] = None,
        buildSpec: str = None,
        customHeaders: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: "AutoBranchCreationConfigTypeDef" = None,
        repository: str = None,
        oauthToken: str = None,
        accessToken: str = None
    ) -> UpdateAppResultTypeDef:
        """
        Updates an existing Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.update_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#update_app)
        """
    def update_branch(
        self,
        *,
        appId: str,
        branchName: str,
        description: str = None,
        framework: str = None,
        stage: StageType = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        enablePerformanceMode: bool = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None
    ) -> UpdateBranchResultTypeDef:
        """
        Updates a branch for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.update_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#update_branch)
        """
    def update_domain_association(
        self,
        *,
        appId: str,
        domainName: str,
        subDomainSettings: List["SubDomainSettingTypeDef"],
        enableAutoSubDomain: bool = None,
        autoSubDomainCreationPatterns: List[str] = None,
        autoSubDomainIAMRole: str = None
    ) -> UpdateDomainAssociationResultTypeDef:
        """
        Creates a new domain association for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.update_domain_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#update_domain_association)
        """
    def update_webhook(
        self, *, webhookId: str, branchName: str = None, description: str = None
    ) -> UpdateWebhookResultTypeDef:
        """
        Updates a webhook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Client.update_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/client.html#update_webhook)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListApps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listappspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_branches"]) -> ListBranchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListBranches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listbranchespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_domain_associations"]
    ) -> ListDomainAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listdomainassociationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listjobspaginator)
        """
