"""
Type annotations for apprunner service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_apprunner.client import AppRunnerClient

    session = Session()
    client: AppRunnerClient = session.client("apprunner")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AssociateCustomDomainRequestTypeDef,
    AssociateCustomDomainResponseTypeDef,
    CreateAutoScalingConfigurationRequestTypeDef,
    CreateAutoScalingConfigurationResponseTypeDef,
    CreateConnectionRequestTypeDef,
    CreateConnectionResponseTypeDef,
    CreateObservabilityConfigurationRequestTypeDef,
    CreateObservabilityConfigurationResponseTypeDef,
    CreateServiceRequestTypeDef,
    CreateServiceResponseTypeDef,
    CreateVpcConnectorRequestTypeDef,
    CreateVpcConnectorResponseTypeDef,
    CreateVpcIngressConnectionRequestTypeDef,
    CreateVpcIngressConnectionResponseTypeDef,
    DeleteAutoScalingConfigurationRequestTypeDef,
    DeleteAutoScalingConfigurationResponseTypeDef,
    DeleteConnectionRequestTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteObservabilityConfigurationRequestTypeDef,
    DeleteObservabilityConfigurationResponseTypeDef,
    DeleteServiceRequestTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteVpcConnectorRequestTypeDef,
    DeleteVpcConnectorResponseTypeDef,
    DeleteVpcIngressConnectionRequestTypeDef,
    DeleteVpcIngressConnectionResponseTypeDef,
    DescribeAutoScalingConfigurationRequestTypeDef,
    DescribeAutoScalingConfigurationResponseTypeDef,
    DescribeCustomDomainsRequestTypeDef,
    DescribeCustomDomainsResponseTypeDef,
    DescribeObservabilityConfigurationRequestTypeDef,
    DescribeObservabilityConfigurationResponseTypeDef,
    DescribeServiceRequestTypeDef,
    DescribeServiceResponseTypeDef,
    DescribeVpcConnectorRequestTypeDef,
    DescribeVpcConnectorResponseTypeDef,
    DescribeVpcIngressConnectionRequestTypeDef,
    DescribeVpcIngressConnectionResponseTypeDef,
    DisassociateCustomDomainRequestTypeDef,
    DisassociateCustomDomainResponseTypeDef,
    ListAutoScalingConfigurationsRequestTypeDef,
    ListAutoScalingConfigurationsResponseTypeDef,
    ListConnectionsRequestTypeDef,
    ListConnectionsResponseTypeDef,
    ListObservabilityConfigurationsRequestTypeDef,
    ListObservabilityConfigurationsResponseTypeDef,
    ListOperationsRequestTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesForAutoScalingConfigurationRequestTypeDef,
    ListServicesForAutoScalingConfigurationResponseTypeDef,
    ListServicesRequestTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVpcConnectorsRequestTypeDef,
    ListVpcConnectorsResponseTypeDef,
    ListVpcIngressConnectionsRequestTypeDef,
    ListVpcIngressConnectionsResponseTypeDef,
    PauseServiceRequestTypeDef,
    PauseServiceResponseTypeDef,
    ResumeServiceRequestTypeDef,
    ResumeServiceResponseTypeDef,
    StartDeploymentRequestTypeDef,
    StartDeploymentResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDefaultAutoScalingConfigurationRequestTypeDef,
    UpdateDefaultAutoScalingConfigurationResponseTypeDef,
    UpdateServiceRequestTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateVpcIngressConnectionRequestTypeDef,
    UpdateVpcIngressConnectionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("AppRunnerClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]

class AppRunnerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppRunnerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#generate_presigned_url)
        """

    def associate_custom_domain(
        self, **kwargs: Unpack[AssociateCustomDomainRequestTypeDef]
    ) -> AssociateCustomDomainResponseTypeDef:
        """
        Associate your own domain name with the App Runner subdomain URL of your App
        Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/associate_custom_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#associate_custom_domain)
        """

    def create_auto_scaling_configuration(
        self, **kwargs: Unpack[CreateAutoScalingConfigurationRequestTypeDef]
    ) -> CreateAutoScalingConfigurationResponseTypeDef:
        """
        Create an App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/create_auto_scaling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#create_auto_scaling_configuration)
        """

    def create_connection(
        self, **kwargs: Unpack[CreateConnectionRequestTypeDef]
    ) -> CreateConnectionResponseTypeDef:
        """
        Create an App Runner connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/create_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#create_connection)
        """

    def create_observability_configuration(
        self, **kwargs: Unpack[CreateObservabilityConfigurationRequestTypeDef]
    ) -> CreateObservabilityConfigurationResponseTypeDef:
        """
        Create an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/create_observability_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#create_observability_configuration)
        """

    def create_service(
        self, **kwargs: Unpack[CreateServiceRequestTypeDef]
    ) -> CreateServiceResponseTypeDef:
        """
        Create an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/create_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#create_service)
        """

    def create_vpc_connector(
        self, **kwargs: Unpack[CreateVpcConnectorRequestTypeDef]
    ) -> CreateVpcConnectorResponseTypeDef:
        """
        Create an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/create_vpc_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#create_vpc_connector)
        """

    def create_vpc_ingress_connection(
        self, **kwargs: Unpack[CreateVpcIngressConnectionRequestTypeDef]
    ) -> CreateVpcIngressConnectionResponseTypeDef:
        """
        Create an App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/create_vpc_ingress_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#create_vpc_ingress_connection)
        """

    def delete_auto_scaling_configuration(
        self, **kwargs: Unpack[DeleteAutoScalingConfigurationRequestTypeDef]
    ) -> DeleteAutoScalingConfigurationResponseTypeDef:
        """
        Delete an App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/delete_auto_scaling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#delete_auto_scaling_configuration)
        """

    def delete_connection(
        self, **kwargs: Unpack[DeleteConnectionRequestTypeDef]
    ) -> DeleteConnectionResponseTypeDef:
        """
        Delete an App Runner connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/delete_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#delete_connection)
        """

    def delete_observability_configuration(
        self, **kwargs: Unpack[DeleteObservabilityConfigurationRequestTypeDef]
    ) -> DeleteObservabilityConfigurationResponseTypeDef:
        """
        Delete an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/delete_observability_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#delete_observability_configuration)
        """

    def delete_service(
        self, **kwargs: Unpack[DeleteServiceRequestTypeDef]
    ) -> DeleteServiceResponseTypeDef:
        """
        Delete an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/delete_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#delete_service)
        """

    def delete_vpc_connector(
        self, **kwargs: Unpack[DeleteVpcConnectorRequestTypeDef]
    ) -> DeleteVpcConnectorResponseTypeDef:
        """
        Delete an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/delete_vpc_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#delete_vpc_connector)
        """

    def delete_vpc_ingress_connection(
        self, **kwargs: Unpack[DeleteVpcIngressConnectionRequestTypeDef]
    ) -> DeleteVpcIngressConnectionResponseTypeDef:
        """
        Delete an App Runner VPC Ingress Connection resource that's associated with an
        App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/delete_vpc_ingress_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#delete_vpc_ingress_connection)
        """

    def describe_auto_scaling_configuration(
        self, **kwargs: Unpack[DescribeAutoScalingConfigurationRequestTypeDef]
    ) -> DescribeAutoScalingConfigurationResponseTypeDef:
        """
        Return a full description of an App Runner automatic scaling configuration
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/describe_auto_scaling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#describe_auto_scaling_configuration)
        """

    def describe_custom_domains(
        self, **kwargs: Unpack[DescribeCustomDomainsRequestTypeDef]
    ) -> DescribeCustomDomainsResponseTypeDef:
        """
        Return a description of custom domain names that are associated with an App
        Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/describe_custom_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#describe_custom_domains)
        """

    def describe_observability_configuration(
        self, **kwargs: Unpack[DescribeObservabilityConfigurationRequestTypeDef]
    ) -> DescribeObservabilityConfigurationResponseTypeDef:
        """
        Return a full description of an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/describe_observability_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#describe_observability_configuration)
        """

    def describe_service(
        self, **kwargs: Unpack[DescribeServiceRequestTypeDef]
    ) -> DescribeServiceResponseTypeDef:
        """
        Return a full description of an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/describe_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#describe_service)
        """

    def describe_vpc_connector(
        self, **kwargs: Unpack[DescribeVpcConnectorRequestTypeDef]
    ) -> DescribeVpcConnectorResponseTypeDef:
        """
        Return a description of an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/describe_vpc_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#describe_vpc_connector)
        """

    def describe_vpc_ingress_connection(
        self, **kwargs: Unpack[DescribeVpcIngressConnectionRequestTypeDef]
    ) -> DescribeVpcIngressConnectionResponseTypeDef:
        """
        Return a full description of an App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/describe_vpc_ingress_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#describe_vpc_ingress_connection)
        """

    def disassociate_custom_domain(
        self, **kwargs: Unpack[DisassociateCustomDomainRequestTypeDef]
    ) -> DisassociateCustomDomainResponseTypeDef:
        """
        Disassociate a custom domain name from an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/disassociate_custom_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#disassociate_custom_domain)
        """

    def list_auto_scaling_configurations(
        self, **kwargs: Unpack[ListAutoScalingConfigurationsRequestTypeDef]
    ) -> ListAutoScalingConfigurationsResponseTypeDef:
        """
        Returns a list of active App Runner automatic scaling configurations in your
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_auto_scaling_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_auto_scaling_configurations)
        """

    def list_connections(
        self, **kwargs: Unpack[ListConnectionsRequestTypeDef]
    ) -> ListConnectionsResponseTypeDef:
        """
        Returns a list of App Runner connections that are associated with your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_connections)
        """

    def list_observability_configurations(
        self, **kwargs: Unpack[ListObservabilityConfigurationsRequestTypeDef]
    ) -> ListObservabilityConfigurationsResponseTypeDef:
        """
        Returns a list of active App Runner observability configurations in your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_observability_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_observability_configurations)
        """

    def list_operations(
        self, **kwargs: Unpack[ListOperationsRequestTypeDef]
    ) -> ListOperationsResponseTypeDef:
        """
        Return a list of operations that occurred on an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_operations)
        """

    def list_services(
        self, **kwargs: Unpack[ListServicesRequestTypeDef]
    ) -> ListServicesResponseTypeDef:
        """
        Returns a list of running App Runner services in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_services)
        """

    def list_services_for_auto_scaling_configuration(
        self, **kwargs: Unpack[ListServicesForAutoScalingConfigurationRequestTypeDef]
    ) -> ListServicesForAutoScalingConfigurationResponseTypeDef:
        """
        Returns a list of the associated App Runner services using an auto scaling
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_services_for_auto_scaling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_services_for_auto_scaling_configuration)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List tags that are associated with for an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_tags_for_resource)
        """

    def list_vpc_connectors(
        self, **kwargs: Unpack[ListVpcConnectorsRequestTypeDef]
    ) -> ListVpcConnectorsResponseTypeDef:
        """
        Returns a list of App Runner VPC connectors in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_vpc_connectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_vpc_connectors)
        """

    def list_vpc_ingress_connections(
        self, **kwargs: Unpack[ListVpcIngressConnectionsRequestTypeDef]
    ) -> ListVpcIngressConnectionsResponseTypeDef:
        """
        Return a list of App Runner VPC Ingress Connections in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/list_vpc_ingress_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#list_vpc_ingress_connections)
        """

    def pause_service(
        self, **kwargs: Unpack[PauseServiceRequestTypeDef]
    ) -> PauseServiceResponseTypeDef:
        """
        Pause an active App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/pause_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#pause_service)
        """

    def resume_service(
        self, **kwargs: Unpack[ResumeServiceRequestTypeDef]
    ) -> ResumeServiceResponseTypeDef:
        """
        Resume an active App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/resume_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#resume_service)
        """

    def start_deployment(
        self, **kwargs: Unpack[StartDeploymentRequestTypeDef]
    ) -> StartDeploymentResponseTypeDef:
        """
        Initiate a manual deployment of the latest commit in a source code repository
        or the latest image in a source image repository to an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/start_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#start_deployment)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Add tags to, or update the tag values of, an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove tags from an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#untag_resource)
        """

    def update_default_auto_scaling_configuration(
        self, **kwargs: Unpack[UpdateDefaultAutoScalingConfigurationRequestTypeDef]
    ) -> UpdateDefaultAutoScalingConfigurationResponseTypeDef:
        """
        Update an auto scaling configuration to be the default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/update_default_auto_scaling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#update_default_auto_scaling_configuration)
        """

    def update_service(
        self, **kwargs: Unpack[UpdateServiceRequestTypeDef]
    ) -> UpdateServiceResponseTypeDef:
        """
        Update an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/update_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#update_service)
        """

    def update_vpc_ingress_connection(
        self, **kwargs: Unpack[UpdateVpcIngressConnectionRequestTypeDef]
    ) -> UpdateVpcIngressConnectionResponseTypeDef:
        """
        Update an existing App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner/client/update_vpc_ingress_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/client/#update_vpc_ingress_connection)
        """
