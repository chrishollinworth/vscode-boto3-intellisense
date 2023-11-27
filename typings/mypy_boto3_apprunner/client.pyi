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
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ProviderTypeType
from .type_defs import (
    AssociateCustomDomainResponseTypeDef,
    CreateAutoScalingConfigurationResponseTypeDef,
    CreateConnectionResponseTypeDef,
    CreateObservabilityConfigurationResponseTypeDef,
    CreateServiceResponseTypeDef,
    CreateVpcConnectorResponseTypeDef,
    CreateVpcIngressConnectionResponseTypeDef,
    DeleteAutoScalingConfigurationResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteObservabilityConfigurationResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteVpcConnectorResponseTypeDef,
    DeleteVpcIngressConnectionResponseTypeDef,
    DescribeAutoScalingConfigurationResponseTypeDef,
    DescribeCustomDomainsResponseTypeDef,
    DescribeObservabilityConfigurationResponseTypeDef,
    DescribeServiceResponseTypeDef,
    DescribeVpcConnectorResponseTypeDef,
    DescribeVpcIngressConnectionResponseTypeDef,
    DisassociateCustomDomainResponseTypeDef,
    EncryptionConfigurationTypeDef,
    HealthCheckConfigurationTypeDef,
    IngressVpcConfigurationTypeDef,
    InstanceConfigurationTypeDef,
    ListAutoScalingConfigurationsResponseTypeDef,
    ListConnectionsResponseTypeDef,
    ListObservabilityConfigurationsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesForAutoScalingConfigurationResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVpcConnectorsResponseTypeDef,
    ListVpcIngressConnectionsFilterTypeDef,
    ListVpcIngressConnectionsResponseTypeDef,
    NetworkConfigurationTypeDef,
    PauseServiceResponseTypeDef,
    ResumeServiceResponseTypeDef,
    ServiceObservabilityConfigurationTypeDef,
    SourceConfigurationTypeDef,
    StartDeploymentResponseTypeDef,
    TagTypeDef,
    TraceConfigurationTypeDef,
    UpdateDefaultAutoScalingConfigurationResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateVpcIngressConnectionResponseTypeDef,
)

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client)
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
        Associate your own domain name with the App Runner subdomain URL of your App
        Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.associate_custom_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#associate_custom_domain)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#close)
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
        Create an App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.create_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_auto_scaling_configuration)
        """
    def create_connection(
        self,
        *,
        ConnectionName: str,
        ProviderType: ProviderTypeType,
        Tags: List["TagTypeDef"] = None
    ) -> CreateConnectionResponseTypeDef:
        """
        Create an App Runner connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_connection)
        """
    def create_observability_configuration(
        self,
        *,
        ObservabilityConfigurationName: str,
        TraceConfiguration: "TraceConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateObservabilityConfigurationResponseTypeDef:
        """
        Create an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.create_observability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_observability_configuration)
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
        AutoScalingConfigurationArn: str = None,
        NetworkConfiguration: "NetworkConfigurationTypeDef" = None,
        ObservabilityConfiguration: "ServiceObservabilityConfigurationTypeDef" = None
    ) -> CreateServiceResponseTypeDef:
        """
        Create an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_service)
        """
    def create_vpc_connector(
        self,
        *,
        VpcConnectorName: str,
        Subnets: List[str],
        SecurityGroups: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateVpcConnectorResponseTypeDef:
        """
        Create an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.create_vpc_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_vpc_connector)
        """
    def create_vpc_ingress_connection(
        self,
        *,
        ServiceArn: str,
        VpcIngressConnectionName: str,
        IngressVpcConfiguration: "IngressVpcConfigurationTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreateVpcIngressConnectionResponseTypeDef:
        """
        Create an App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.create_vpc_ingress_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#create_vpc_ingress_connection)
        """
    def delete_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str, DeleteAllRevisions: bool = None
    ) -> DeleteAutoScalingConfigurationResponseTypeDef:
        """
        Delete an App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.delete_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_auto_scaling_configuration)
        """
    def delete_connection(self, *, ConnectionArn: str) -> DeleteConnectionResponseTypeDef:
        """
        Delete an App Runner connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_connection)
        """
    def delete_observability_configuration(
        self, *, ObservabilityConfigurationArn: str
    ) -> DeleteObservabilityConfigurationResponseTypeDef:
        """
        Delete an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.delete_observability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_observability_configuration)
        """
    def delete_service(self, *, ServiceArn: str) -> DeleteServiceResponseTypeDef:
        """
        Delete an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_service)
        """
    def delete_vpc_connector(self, *, VpcConnectorArn: str) -> DeleteVpcConnectorResponseTypeDef:
        """
        Delete an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.delete_vpc_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_vpc_connector)
        """
    def delete_vpc_ingress_connection(
        self, *, VpcIngressConnectionArn: str
    ) -> DeleteVpcIngressConnectionResponseTypeDef:
        """
        Delete an App Runner VPC Ingress Connection resource that's associated with an
        App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.delete_vpc_ingress_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#delete_vpc_ingress_connection)
        """
    def describe_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str
    ) -> DescribeAutoScalingConfigurationResponseTypeDef:
        """
        Return a full description of an App Runner automatic scaling configuration
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.describe_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_auto_scaling_configuration)
        """
    def describe_custom_domains(
        self, *, ServiceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCustomDomainsResponseTypeDef:
        """
        Return a description of custom domain names that are associated with an App
        Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.describe_custom_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_custom_domains)
        """
    def describe_observability_configuration(
        self, *, ObservabilityConfigurationArn: str
    ) -> DescribeObservabilityConfigurationResponseTypeDef:
        """
        Return a full description of an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.describe_observability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_observability_configuration)
        """
    def describe_service(self, *, ServiceArn: str) -> DescribeServiceResponseTypeDef:
        """
        Return a full description of an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.describe_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_service)
        """
    def describe_vpc_connector(
        self, *, VpcConnectorArn: str
    ) -> DescribeVpcConnectorResponseTypeDef:
        """
        Return a description of an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.describe_vpc_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_vpc_connector)
        """
    def describe_vpc_ingress_connection(
        self, *, VpcIngressConnectionArn: str
    ) -> DescribeVpcIngressConnectionResponseTypeDef:
        """
        Return a full description of an App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.describe_vpc_ingress_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#describe_vpc_ingress_connection)
        """
    def disassociate_custom_domain(
        self, *, ServiceArn: str, DomainName: str
    ) -> DisassociateCustomDomainResponseTypeDef:
        """
        Disassociate a custom domain name from an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.disassociate_custom_domain)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.generate_presigned_url)
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
        Returns a list of active App Runner automatic scaling configurations in your
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_auto_scaling_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_auto_scaling_configurations)
        """
    def list_connections(
        self, *, ConnectionName: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListConnectionsResponseTypeDef:
        """
        Returns a list of App Runner connections that are associated with your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_connections)
        """
    def list_observability_configurations(
        self,
        *,
        ObservabilityConfigurationName: str = None,
        LatestOnly: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListObservabilityConfigurationsResponseTypeDef:
        """
        Returns a list of active App Runner observability configurations in your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_observability_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_observability_configurations)
        """
    def list_operations(
        self, *, ServiceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListOperationsResponseTypeDef:
        """
        Return a list of operations that occurred on an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_operations)
        """
    def list_services(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListServicesResponseTypeDef:
        """
        Returns a list of running App Runner services in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_services)
        """
    def list_services_for_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListServicesForAutoScalingConfigurationResponseTypeDef:
        """
        Returns a list of the associated App Runner services using an auto scaling
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_services_for_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_services_for_auto_scaling_configuration)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List tags that are associated with for an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_tags_for_resource)
        """
    def list_vpc_connectors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListVpcConnectorsResponseTypeDef:
        """
        Returns a list of App Runner VPC connectors in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_vpc_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_vpc_connectors)
        """
    def list_vpc_ingress_connections(
        self,
        *,
        Filter: "ListVpcIngressConnectionsFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListVpcIngressConnectionsResponseTypeDef:
        """
        Return a list of App Runner VPC Ingress Connections in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.list_vpc_ingress_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#list_vpc_ingress_connections)
        """
    def pause_service(self, *, ServiceArn: str) -> PauseServiceResponseTypeDef:
        """
        Pause an active App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.pause_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#pause_service)
        """
    def resume_service(self, *, ServiceArn: str) -> ResumeServiceResponseTypeDef:
        """
        Resume an active App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.resume_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#resume_service)
        """
    def start_deployment(self, *, ServiceArn: str) -> StartDeploymentResponseTypeDef:
        """
        Initiate a manual deployment of the latest commit in a source code repository or
        the latest image in a source image repository to an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.start_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#start_deployment)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add tags to, or update the tag values of, an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove tags from an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#untag_resource)
        """
    def update_default_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str
    ) -> UpdateDefaultAutoScalingConfigurationResponseTypeDef:
        """
        Update an auto scaling configuration to be the default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.update_default_auto_scaling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#update_default_auto_scaling_configuration)
        """
    def update_service(
        self,
        *,
        ServiceArn: str,
        SourceConfiguration: "SourceConfigurationTypeDef" = None,
        InstanceConfiguration: "InstanceConfigurationTypeDef" = None,
        AutoScalingConfigurationArn: str = None,
        HealthCheckConfiguration: "HealthCheckConfigurationTypeDef" = None,
        NetworkConfiguration: "NetworkConfigurationTypeDef" = None,
        ObservabilityConfiguration: "ServiceObservabilityConfigurationTypeDef" = None
    ) -> UpdateServiceResponseTypeDef:
        """
        Update an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#update_service)
        """
    def update_vpc_ingress_connection(
        self,
        *,
        VpcIngressConnectionArn: str,
        IngressVpcConfiguration: "IngressVpcConfigurationTypeDef"
    ) -> UpdateVpcIngressConnectionResponseTypeDef:
        """
        Update an existing App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/apprunner.html#AppRunner.Client.update_vpc_ingress_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client.html#update_vpc_ingress_connection)
        """
