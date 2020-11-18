# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for serverlessrepo service client

Usage::

    ```python
    import boto3
    from mypy_boto3_serverlessrepo import ServerlessApplicationRepositoryClient

    client: ServerlessApplicationRepositoryClient = boto3.client("serverlessrepo")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_serverlessrepo.paginator import (
    ListApplicationDependenciesPaginator,
    ListApplicationsPaginator,
    ListApplicationVersionsPaginator,
)
from mypy_boto3_serverlessrepo.type_defs import (
    ApplicationPolicyStatementTypeDef,
    CreateApplicationResponseTypeDef,
    CreateApplicationVersionResponseTypeDef,
    CreateCloudFormationChangeSetResponseTypeDef,
    CreateCloudFormationTemplateResponseTypeDef,
    GetApplicationPolicyResponseTypeDef,
    GetApplicationResponseTypeDef,
    GetCloudFormationTemplateResponseTypeDef,
    ListApplicationDependenciesResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ParameterValueTypeDef,
    PutApplicationPolicyResponseTypeDef,
    RollbackConfigurationTypeDef,
    TagTypeDef,
    UpdateApplicationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServerlessApplicationRepositoryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class ServerlessApplicationRepositoryClient:
    """
    [ServerlessApplicationRepository.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.can_paginate)
        """

    def create_application(
        self,
        Author: str,
        Description: str,
        Name: str,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        LicenseBody: str = None,
        LicenseUrl: str = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
        SemanticVersion: str = None,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        SpdxLicenseId: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application)
        """

    def create_application_version(
        self,
        ApplicationId: str,
        SemanticVersion: str,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> CreateApplicationVersionResponseTypeDef:
        """
        [Client.create_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application_version)
        """

    def create_cloud_formation_change_set(
        self,
        ApplicationId: str,
        StackName: str,
        Capabilities: List[str] = None,
        ChangeSetName: str = None,
        ClientToken: str = None,
        Description: str = None,
        NotificationArns: List[str] = None,
        ParameterOverrides: List[ParameterValueTypeDef] = None,
        ResourceTypes: List[str] = None,
        RollbackConfiguration: RollbackConfigurationTypeDef = None,
        SemanticVersion: str = None,
        Tags: List[TagTypeDef] = None,
        TemplateId: str = None,
    ) -> CreateCloudFormationChangeSetResponseTypeDef:
        """
        [Client.create_cloud_formation_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_change_set)
        """

    def create_cloud_formation_template(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> CreateCloudFormationTemplateResponseTypeDef:
        """
        [Client.create_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_template)
        """

    def delete_application(self, ApplicationId: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.delete_application)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.generate_presigned_url)
        """

    def get_application(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> GetApplicationResponseTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application)
        """

    def get_application_policy(self, ApplicationId: str) -> GetApplicationPolicyResponseTypeDef:
        """
        [Client.get_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application_policy)
        """

    def get_cloud_formation_template(
        self, ApplicationId: str, TemplateId: str
    ) -> GetCloudFormationTemplateResponseTypeDef:
        """
        [Client.get_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_cloud_formation_template)
        """

    def list_application_dependencies(
        self,
        ApplicationId: str,
        MaxItems: int = None,
        NextToken: str = None,
        SemanticVersion: str = None,
    ) -> ListApplicationDependenciesResponseTypeDef:
        """
        [Client.list_application_dependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_dependencies)
        """

    def list_application_versions(
        self, ApplicationId: str, MaxItems: int = None, NextToken: str = None
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        [Client.list_application_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_versions)
        """

    def list_applications(
        self, MaxItems: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_applications)
        """

    def put_application_policy(
        self, ApplicationId: str, Statements: List["ApplicationPolicyStatementTypeDef"]
    ) -> PutApplicationPolicyResponseTypeDef:
        """
        [Client.put_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.put_application_policy)
        """

    def unshare_application(self, ApplicationId: str, OrganizationId: str) -> None:
        """
        [Client.unshare_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.unshare_application)
        """

    def update_application(
        self,
        ApplicationId: str,
        Author: str = None,
        Description: str = None,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.update_application)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_dependencies"]
    ) -> ListApplicationDependenciesPaginator:
        """
        [Paginator.ListApplicationDependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_versions"]
    ) -> ListApplicationVersionsPaginator:
        """
        [Paginator.ListApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications)
        """
