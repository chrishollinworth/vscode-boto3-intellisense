"""
Type annotations for apprunner service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_apprunner import AppRunnerClient

    client: AppRunnerClient = boto3.client("apprunner")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    AssociateCustomDomainResponseTypeDef,
    CreateAutoScalingConfigurationResponseTypeDef,
    CreateConnectionResponseTypeDef,
    CreateServiceResponseTypeDef,
    DeleteAutoScalingConfigurationResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DescribeAutoScalingConfigurationResponseTypeDef,
    DescribeCustomDomainsResponseTypeDef,
    DescribeServiceResponseTypeDef,
    DisassociateCustomDomainResponseTypeDef,
    EncryptionConfigurationTypeDef,
    HealthCheckConfigurationTypeDef,
    InstanceConfigurationTypeDef,
    ListAutoScalingConfigurationsResponseTypeDef,
    ListConnectionsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PauseServiceResponseTypeDef,
    ResumeServiceResponseTypeDef,
    SourceConfigurationTypeDef,
    StartDeploymentResponseTypeDef,
    TagTypeDef,
    UpdateServiceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppRunnerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]

class AppRunnerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        AppRunnerClient exceptions.
        """
    def associate_custom_domain(
        self, *, ServiceArn: str, DomainName: str, EnableWWWSubdomain: bool = None
    ) -> AssociateCustomDomainResponseTypeDef:
        """
        Associate your own domain name with the AWS App Runner subdomain URL of your App
        Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.associate_custom_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#associate_custom_domain)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#can_paginate)
        """
    def create_auto_scaling_configuration(
        self,
        *,
        AutoScalingConfigurationName: str,
        MaxConcurrency: int = None,
        MinSize: int = None,
        MaxSize: int = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAutoScalingConfigurationResponseTypeDef:
        """
        Create an AWS App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.create_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_auto_scaling_configuration)
        """
    def create_connection(
        self,
        *,
        ConnectionName: str,
        ProviderType: Literal["GITHUB"],
        Tags: List["TagTypeDef"] = None
    ) -> CreateConnectionResponseTypeDef:
        """
        Create an AWS App Runner connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_connection)
        """
    def create_service(
        self,
        *,
        ServiceName: str,
        SourceConfiguration: "SourceConfigurationTypeDef",
        InstanceConfiguration: "InstanceConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        EncryptionConfiguration: "EncryptionConfigurationTypeDef" = None,
        HealthCheckConfiguration: "HealthCheckConfigurationTypeDef" = None,
        AutoScalingConfigurationArn: str = None
    ) -> CreateServiceResponseTypeDef:
        """
        Create an AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_service)
        """
    def delete_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str
    ) -> DeleteAutoScalingConfigurationResponseTypeDef:
        """
        Delete an AWS App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.delete_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_auto_scaling_configuration)
        """
    def delete_connection(self, *, ConnectionArn: str) -> DeleteConnectionResponseTypeDef:
        """
        Delete an AWS App Runner connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_connection)
        """
    def delete_service(self, *, ServiceArn: str) -> DeleteServiceResponseTypeDef:
        """
        Delete an AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_service)
        """
    def describe_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str
    ) -> DescribeAutoScalingConfigurationResponseTypeDef:
        """
        Return a full description of an AWS App Runner automatic scaling configuration
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.describe_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_auto_scaling_configuration)
        """
    def describe_custom_domains(
        self, *, ServiceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCustomDomainsResponseTypeDef:
        """
        Return a description of custom domain names that are associated with an AWS App
        Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.describe_custom_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_custom_domains)
        """
    def describe_service(self, *, ServiceArn: str) -> DescribeServiceResponseTypeDef:
        """
        Return a full description of an AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.describe_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_service)
        """
    def disassociate_custom_domain(
        self, *, ServiceArn: str, DomainName: str
    ) -> DisassociateCustomDomainResponseTypeDef:
        """
        Disassociate a custom domain name from an AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.disassociate_custom_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#disassociate_custom_domain)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#generate_presigned_url)
        """
    def list_auto_scaling_configurations(
        self,
        *,
        AutoScalingConfigurationName: str = None,
        LatestOnly: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAutoScalingConfigurationsResponseTypeDef:
        """
        Returns a list of AWS App Runner automatic scaling configurations in your AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.list_auto_scaling_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_auto_scaling_configurations)
        """
    def list_connections(
        self, *, ConnectionName: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListConnectionsResponseTypeDef:
        """
        Returns a list of AWS App Runner connections that are associated with your AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.list_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_connections)
        """
    def list_operations(
        self, *, ServiceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListOperationsResponseTypeDef:
        """
        Return a list of operations that occurred on an AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.list_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_operations)
        """
    def list_services(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListServicesResponseTypeDef:
        """
        Returns a list of running AWS App Runner services in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_services)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List tags that are associated with for an AWS App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_tags_for_resource)
        """
    def pause_service(self, *, ServiceArn: str) -> PauseServiceResponseTypeDef:
        """
        Pause an active AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.pause_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#pause_service)
        """
    def resume_service(self, *, ServiceArn: str) -> ResumeServiceResponseTypeDef:
        """
        Resume an active AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.resume_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#resume_service)
        """
    def start_deployment(self, *, ServiceArn: str) -> StartDeploymentResponseTypeDef:
        """
        Initiate a manual deployment of the latest commit in a source code repository or
        the latest image in a source image repository to an AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.start_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#start_deployment)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add tags to, or update the tag values of, an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove tags from an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#untag_resource)
        """
    def update_service(
        self,
        *,
        ServiceArn: str,
        SourceConfiguration: "SourceConfigurationTypeDef" = None,
        InstanceConfiguration: "InstanceConfigurationTypeDef" = None,
        AutoScalingConfigurationArn: str = None,
        HealthCheckConfiguration: "HealthCheckConfigurationTypeDef" = None
    ) -> UpdateServiceResponseTypeDef:
        """
        Update an AWS App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apprunner.html#AppRunner.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#update_service)
        """
