"""
Type annotations for greengrass service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_greengrass.client import GreengrassClient

    session = Session()
    client: GreengrassClient = session.client("greengrass")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListBulkDeploymentDetailedReportsPaginator,
    ListBulkDeploymentsPaginator,
    ListConnectorDefinitionsPaginator,
    ListConnectorDefinitionVersionsPaginator,
    ListCoreDefinitionsPaginator,
    ListCoreDefinitionVersionsPaginator,
    ListDeploymentsPaginator,
    ListDeviceDefinitionsPaginator,
    ListDeviceDefinitionVersionsPaginator,
    ListFunctionDefinitionsPaginator,
    ListFunctionDefinitionVersionsPaginator,
    ListGroupsPaginator,
    ListGroupVersionsPaginator,
    ListLoggerDefinitionsPaginator,
    ListLoggerDefinitionVersionsPaginator,
    ListResourceDefinitionsPaginator,
    ListResourceDefinitionVersionsPaginator,
    ListSubscriptionDefinitionsPaginator,
    ListSubscriptionDefinitionVersionsPaginator,
)
from .type_defs import (
    AssociateRoleToGroupRequestTypeDef,
    AssociateRoleToGroupResponseTypeDef,
    AssociateServiceRoleToAccountRequestTypeDef,
    AssociateServiceRoleToAccountResponseTypeDef,
    CreateConnectorDefinitionRequestTypeDef,
    CreateConnectorDefinitionResponseTypeDef,
    CreateConnectorDefinitionVersionRequestTypeDef,
    CreateConnectorDefinitionVersionResponseTypeDef,
    CreateCoreDefinitionRequestTypeDef,
    CreateCoreDefinitionResponseTypeDef,
    CreateCoreDefinitionVersionRequestTypeDef,
    CreateCoreDefinitionVersionResponseTypeDef,
    CreateDeploymentRequestTypeDef,
    CreateDeploymentResponseTypeDef,
    CreateDeviceDefinitionRequestTypeDef,
    CreateDeviceDefinitionResponseTypeDef,
    CreateDeviceDefinitionVersionRequestTypeDef,
    CreateDeviceDefinitionVersionResponseTypeDef,
    CreateFunctionDefinitionRequestTypeDef,
    CreateFunctionDefinitionResponseTypeDef,
    CreateFunctionDefinitionVersionRequestTypeDef,
    CreateFunctionDefinitionVersionResponseTypeDef,
    CreateGroupCertificateAuthorityRequestTypeDef,
    CreateGroupCertificateAuthorityResponseTypeDef,
    CreateGroupRequestTypeDef,
    CreateGroupResponseTypeDef,
    CreateGroupVersionRequestTypeDef,
    CreateGroupVersionResponseTypeDef,
    CreateLoggerDefinitionRequestTypeDef,
    CreateLoggerDefinitionResponseTypeDef,
    CreateLoggerDefinitionVersionRequestTypeDef,
    CreateLoggerDefinitionVersionResponseTypeDef,
    CreateResourceDefinitionRequestTypeDef,
    CreateResourceDefinitionResponseTypeDef,
    CreateResourceDefinitionVersionRequestTypeDef,
    CreateResourceDefinitionVersionResponseTypeDef,
    CreateSoftwareUpdateJobRequestTypeDef,
    CreateSoftwareUpdateJobResponseTypeDef,
    CreateSubscriptionDefinitionRequestTypeDef,
    CreateSubscriptionDefinitionResponseTypeDef,
    CreateSubscriptionDefinitionVersionRequestTypeDef,
    CreateSubscriptionDefinitionVersionResponseTypeDef,
    DeleteConnectorDefinitionRequestTypeDef,
    DeleteCoreDefinitionRequestTypeDef,
    DeleteDeviceDefinitionRequestTypeDef,
    DeleteFunctionDefinitionRequestTypeDef,
    DeleteGroupRequestTypeDef,
    DeleteLoggerDefinitionRequestTypeDef,
    DeleteResourceDefinitionRequestTypeDef,
    DeleteSubscriptionDefinitionRequestTypeDef,
    DisassociateRoleFromGroupRequestTypeDef,
    DisassociateRoleFromGroupResponseTypeDef,
    DisassociateServiceRoleFromAccountResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAssociatedRoleRequestTypeDef,
    GetAssociatedRoleResponseTypeDef,
    GetBulkDeploymentStatusRequestTypeDef,
    GetBulkDeploymentStatusResponseTypeDef,
    GetConnectivityInfoRequestTypeDef,
    GetConnectivityInfoResponseTypeDef,
    GetConnectorDefinitionRequestTypeDef,
    GetConnectorDefinitionResponseTypeDef,
    GetConnectorDefinitionVersionRequestTypeDef,
    GetConnectorDefinitionVersionResponseTypeDef,
    GetCoreDefinitionRequestTypeDef,
    GetCoreDefinitionResponseTypeDef,
    GetCoreDefinitionVersionRequestTypeDef,
    GetCoreDefinitionVersionResponseTypeDef,
    GetDeploymentStatusRequestTypeDef,
    GetDeploymentStatusResponseTypeDef,
    GetDeviceDefinitionRequestTypeDef,
    GetDeviceDefinitionResponseTypeDef,
    GetDeviceDefinitionVersionRequestTypeDef,
    GetDeviceDefinitionVersionResponseTypeDef,
    GetFunctionDefinitionRequestTypeDef,
    GetFunctionDefinitionResponseTypeDef,
    GetFunctionDefinitionVersionRequestTypeDef,
    GetFunctionDefinitionVersionResponseTypeDef,
    GetGroupCertificateAuthorityRequestTypeDef,
    GetGroupCertificateAuthorityResponseTypeDef,
    GetGroupCertificateConfigurationRequestTypeDef,
    GetGroupCertificateConfigurationResponseTypeDef,
    GetGroupRequestTypeDef,
    GetGroupResponseTypeDef,
    GetGroupVersionRequestTypeDef,
    GetGroupVersionResponseTypeDef,
    GetLoggerDefinitionRequestTypeDef,
    GetLoggerDefinitionResponseTypeDef,
    GetLoggerDefinitionVersionRequestTypeDef,
    GetLoggerDefinitionVersionResponseTypeDef,
    GetResourceDefinitionRequestTypeDef,
    GetResourceDefinitionResponseTypeDef,
    GetResourceDefinitionVersionRequestTypeDef,
    GetResourceDefinitionVersionResponseTypeDef,
    GetServiceRoleForAccountResponseTypeDef,
    GetSubscriptionDefinitionRequestTypeDef,
    GetSubscriptionDefinitionResponseTypeDef,
    GetSubscriptionDefinitionVersionRequestTypeDef,
    GetSubscriptionDefinitionVersionResponseTypeDef,
    GetThingRuntimeConfigurationRequestTypeDef,
    GetThingRuntimeConfigurationResponseTypeDef,
    ListBulkDeploymentDetailedReportsRequestTypeDef,
    ListBulkDeploymentDetailedReportsResponseTypeDef,
    ListBulkDeploymentsRequestTypeDef,
    ListBulkDeploymentsResponseTypeDef,
    ListConnectorDefinitionsRequestTypeDef,
    ListConnectorDefinitionsResponseTypeDef,
    ListConnectorDefinitionVersionsRequestTypeDef,
    ListConnectorDefinitionVersionsResponseTypeDef,
    ListCoreDefinitionsRequestTypeDef,
    ListCoreDefinitionsResponseTypeDef,
    ListCoreDefinitionVersionsRequestTypeDef,
    ListCoreDefinitionVersionsResponseTypeDef,
    ListDeploymentsRequestTypeDef,
    ListDeploymentsResponseTypeDef,
    ListDeviceDefinitionsRequestTypeDef,
    ListDeviceDefinitionsResponseTypeDef,
    ListDeviceDefinitionVersionsRequestTypeDef,
    ListDeviceDefinitionVersionsResponseTypeDef,
    ListFunctionDefinitionsRequestTypeDef,
    ListFunctionDefinitionsResponseTypeDef,
    ListFunctionDefinitionVersionsRequestTypeDef,
    ListFunctionDefinitionVersionsResponseTypeDef,
    ListGroupCertificateAuthoritiesRequestTypeDef,
    ListGroupCertificateAuthoritiesResponseTypeDef,
    ListGroupsRequestTypeDef,
    ListGroupsResponseTypeDef,
    ListGroupVersionsRequestTypeDef,
    ListGroupVersionsResponseTypeDef,
    ListLoggerDefinitionsRequestTypeDef,
    ListLoggerDefinitionsResponseTypeDef,
    ListLoggerDefinitionVersionsRequestTypeDef,
    ListLoggerDefinitionVersionsResponseTypeDef,
    ListResourceDefinitionsRequestTypeDef,
    ListResourceDefinitionsResponseTypeDef,
    ListResourceDefinitionVersionsRequestTypeDef,
    ListResourceDefinitionVersionsResponseTypeDef,
    ListSubscriptionDefinitionsRequestTypeDef,
    ListSubscriptionDefinitionsResponseTypeDef,
    ListSubscriptionDefinitionVersionsRequestTypeDef,
    ListSubscriptionDefinitionVersionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ResetDeploymentsRequestTypeDef,
    ResetDeploymentsResponseTypeDef,
    StartBulkDeploymentRequestTypeDef,
    StartBulkDeploymentResponseTypeDef,
    StopBulkDeploymentRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateConnectivityInfoRequestTypeDef,
    UpdateConnectivityInfoResponseTypeDef,
    UpdateConnectorDefinitionRequestTypeDef,
    UpdateCoreDefinitionRequestTypeDef,
    UpdateDeviceDefinitionRequestTypeDef,
    UpdateFunctionDefinitionRequestTypeDef,
    UpdateGroupCertificateConfigurationRequestTypeDef,
    UpdateGroupCertificateConfigurationResponseTypeDef,
    UpdateGroupRequestTypeDef,
    UpdateLoggerDefinitionRequestTypeDef,
    UpdateResourceDefinitionRequestTypeDef,
    UpdateSubscriptionDefinitionRequestTypeDef,
    UpdateThingRuntimeConfigurationRequestTypeDef,
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

__all__ = ("GreengrassClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]

class GreengrassClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GreengrassClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#generate_presigned_url)
        """

    def associate_role_to_group(
        self, **kwargs: Unpack[AssociateRoleToGroupRequestTypeDef]
    ) -> AssociateRoleToGroupResponseTypeDef:
        """
        Associates a role with a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/associate_role_to_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#associate_role_to_group)
        """

    def associate_service_role_to_account(
        self, **kwargs: Unpack[AssociateServiceRoleToAccountRequestTypeDef]
    ) -> AssociateServiceRoleToAccountResponseTypeDef:
        """
        Associates a role with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/associate_service_role_to_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#associate_service_role_to_account)
        """

    def create_connector_definition(
        self, **kwargs: Unpack[CreateConnectorDefinitionRequestTypeDef]
    ) -> CreateConnectorDefinitionResponseTypeDef:
        """
        Creates a connector definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_connector_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_connector_definition)
        """

    def create_connector_definition_version(
        self, **kwargs: Unpack[CreateConnectorDefinitionVersionRequestTypeDef]
    ) -> CreateConnectorDefinitionVersionResponseTypeDef:
        """
        Creates a version of a connector definition which has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_connector_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_connector_definition_version)
        """

    def create_core_definition(
        self, **kwargs: Unpack[CreateCoreDefinitionRequestTypeDef]
    ) -> CreateCoreDefinitionResponseTypeDef:
        """
        Creates a core definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_core_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_core_definition)
        """

    def create_core_definition_version(
        self, **kwargs: Unpack[CreateCoreDefinitionVersionRequestTypeDef]
    ) -> CreateCoreDefinitionVersionResponseTypeDef:
        """
        Creates a version of a core definition that has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_core_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_core_definition_version)
        """

    def create_deployment(
        self, **kwargs: Unpack[CreateDeploymentRequestTypeDef]
    ) -> CreateDeploymentResponseTypeDef:
        """
        Creates a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_deployment)
        """

    def create_device_definition(
        self, **kwargs: Unpack[CreateDeviceDefinitionRequestTypeDef]
    ) -> CreateDeviceDefinitionResponseTypeDef:
        """
        Creates a device definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_device_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_device_definition)
        """

    def create_device_definition_version(
        self, **kwargs: Unpack[CreateDeviceDefinitionVersionRequestTypeDef]
    ) -> CreateDeviceDefinitionVersionResponseTypeDef:
        """
        Creates a version of a device definition that has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_device_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_device_definition_version)
        """

    def create_function_definition(
        self, **kwargs: Unpack[CreateFunctionDefinitionRequestTypeDef]
    ) -> CreateFunctionDefinitionResponseTypeDef:
        """
        Creates a Lambda function definition which contains a list of Lambda functions
        and their configurations to be used in a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_function_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_function_definition)
        """

    def create_function_definition_version(
        self, **kwargs: Unpack[CreateFunctionDefinitionVersionRequestTypeDef]
    ) -> CreateFunctionDefinitionVersionResponseTypeDef:
        """
        Creates a version of a Lambda function definition that has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_function_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_function_definition_version)
        """

    def create_group(
        self, **kwargs: Unpack[CreateGroupRequestTypeDef]
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_group)
        """

    def create_group_certificate_authority(
        self, **kwargs: Unpack[CreateGroupCertificateAuthorityRequestTypeDef]
    ) -> CreateGroupCertificateAuthorityResponseTypeDef:
        """
        Creates a CA for the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_group_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_group_certificate_authority)
        """

    def create_group_version(
        self, **kwargs: Unpack[CreateGroupVersionRequestTypeDef]
    ) -> CreateGroupVersionResponseTypeDef:
        """
        Creates a version of a group which has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_group_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_group_version)
        """

    def create_logger_definition(
        self, **kwargs: Unpack[CreateLoggerDefinitionRequestTypeDef]
    ) -> CreateLoggerDefinitionResponseTypeDef:
        """
        Creates a logger definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_logger_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_logger_definition)
        """

    def create_logger_definition_version(
        self, **kwargs: Unpack[CreateLoggerDefinitionVersionRequestTypeDef]
    ) -> CreateLoggerDefinitionVersionResponseTypeDef:
        """
        Creates a version of a logger definition that has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_logger_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_logger_definition_version)
        """

    def create_resource_definition(
        self, **kwargs: Unpack[CreateResourceDefinitionRequestTypeDef]
    ) -> CreateResourceDefinitionResponseTypeDef:
        """
        Creates a resource definition which contains a list of resources to be used in
        a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_resource_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_resource_definition)
        """

    def create_resource_definition_version(
        self, **kwargs: Unpack[CreateResourceDefinitionVersionRequestTypeDef]
    ) -> CreateResourceDefinitionVersionResponseTypeDef:
        """
        Creates a version of a resource definition that has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_resource_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_resource_definition_version)
        """

    def create_software_update_job(
        self, **kwargs: Unpack[CreateSoftwareUpdateJobRequestTypeDef]
    ) -> CreateSoftwareUpdateJobResponseTypeDef:
        """
        Creates a software update for a core or group of cores (specified as an IoT
        thing group.) Use this to update the OTA Agent as well as the Greengrass core
        software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_software_update_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_software_update_job)
        """

    def create_subscription_definition(
        self, **kwargs: Unpack[CreateSubscriptionDefinitionRequestTypeDef]
    ) -> CreateSubscriptionDefinitionResponseTypeDef:
        """
        Creates a subscription definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_subscription_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_subscription_definition)
        """

    def create_subscription_definition_version(
        self, **kwargs: Unpack[CreateSubscriptionDefinitionVersionRequestTypeDef]
    ) -> CreateSubscriptionDefinitionVersionResponseTypeDef:
        """
        Creates a version of a subscription definition which has already been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/create_subscription_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#create_subscription_definition_version)
        """

    def delete_connector_definition(
        self, **kwargs: Unpack[DeleteConnectorDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a connector definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_connector_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_connector_definition)
        """

    def delete_core_definition(
        self, **kwargs: Unpack[DeleteCoreDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a core definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_core_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_core_definition)
        """

    def delete_device_definition(
        self, **kwargs: Unpack[DeleteDeviceDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a device definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_device_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_device_definition)
        """

    def delete_function_definition(
        self, **kwargs: Unpack[DeleteFunctionDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Lambda function definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_function_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_function_definition)
        """

    def delete_group(self, **kwargs: Unpack[DeleteGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_group)
        """

    def delete_logger_definition(
        self, **kwargs: Unpack[DeleteLoggerDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a logger definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_logger_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_logger_definition)
        """

    def delete_resource_definition(
        self, **kwargs: Unpack[DeleteResourceDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_resource_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_resource_definition)
        """

    def delete_subscription_definition(
        self, **kwargs: Unpack[DeleteSubscriptionDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a subscription definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/delete_subscription_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#delete_subscription_definition)
        """

    def disassociate_role_from_group(
        self, **kwargs: Unpack[DisassociateRoleFromGroupRequestTypeDef]
    ) -> DisassociateRoleFromGroupResponseTypeDef:
        """
        Disassociates the role from a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/disassociate_role_from_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#disassociate_role_from_group)
        """

    def disassociate_service_role_from_account(
        self,
    ) -> DisassociateServiceRoleFromAccountResponseTypeDef:
        """
        Disassociates the service role from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/disassociate_service_role_from_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#disassociate_service_role_from_account)
        """

    def get_associated_role(
        self, **kwargs: Unpack[GetAssociatedRoleRequestTypeDef]
    ) -> GetAssociatedRoleResponseTypeDef:
        """
        Retrieves the role associated with a particular group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_associated_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_associated_role)
        """

    def get_bulk_deployment_status(
        self, **kwargs: Unpack[GetBulkDeploymentStatusRequestTypeDef]
    ) -> GetBulkDeploymentStatusResponseTypeDef:
        """
        Returns the status of a bulk deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_bulk_deployment_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_bulk_deployment_status)
        """

    def get_connectivity_info(
        self, **kwargs: Unpack[GetConnectivityInfoRequestTypeDef]
    ) -> GetConnectivityInfoResponseTypeDef:
        """
        Retrieves the connectivity information for a core.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_connectivity_info.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_connectivity_info)
        """

    def get_connector_definition(
        self, **kwargs: Unpack[GetConnectorDefinitionRequestTypeDef]
    ) -> GetConnectorDefinitionResponseTypeDef:
        """
        Retrieves information about a connector definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_connector_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_connector_definition)
        """

    def get_connector_definition_version(
        self, **kwargs: Unpack[GetConnectorDefinitionVersionRequestTypeDef]
    ) -> GetConnectorDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a connector definition version, including the
        connectors that the version contains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_connector_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_connector_definition_version)
        """

    def get_core_definition(
        self, **kwargs: Unpack[GetCoreDefinitionRequestTypeDef]
    ) -> GetCoreDefinitionResponseTypeDef:
        """
        Retrieves information about a core definition version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_core_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_core_definition)
        """

    def get_core_definition_version(
        self, **kwargs: Unpack[GetCoreDefinitionVersionRequestTypeDef]
    ) -> GetCoreDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a core definition version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_core_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_core_definition_version)
        """

    def get_deployment_status(
        self, **kwargs: Unpack[GetDeploymentStatusRequestTypeDef]
    ) -> GetDeploymentStatusResponseTypeDef:
        """
        Returns the status of a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_deployment_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_deployment_status)
        """

    def get_device_definition(
        self, **kwargs: Unpack[GetDeviceDefinitionRequestTypeDef]
    ) -> GetDeviceDefinitionResponseTypeDef:
        """
        Retrieves information about a device definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_device_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_device_definition)
        """

    def get_device_definition_version(
        self, **kwargs: Unpack[GetDeviceDefinitionVersionRequestTypeDef]
    ) -> GetDeviceDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a device definition version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_device_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_device_definition_version)
        """

    def get_function_definition(
        self, **kwargs: Unpack[GetFunctionDefinitionRequestTypeDef]
    ) -> GetFunctionDefinitionResponseTypeDef:
        """
        Retrieves information about a Lambda function definition, including its
        creation time and latest version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_function_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_function_definition)
        """

    def get_function_definition_version(
        self, **kwargs: Unpack[GetFunctionDefinitionVersionRequestTypeDef]
    ) -> GetFunctionDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a Lambda function definition version, including
        which Lambda functions are included in the version and their configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_function_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_function_definition_version)
        """

    def get_group(self, **kwargs: Unpack[GetGroupRequestTypeDef]) -> GetGroupResponseTypeDef:
        """
        Retrieves information about a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_group)
        """

    def get_group_certificate_authority(
        self, **kwargs: Unpack[GetGroupCertificateAuthorityRequestTypeDef]
    ) -> GetGroupCertificateAuthorityResponseTypeDef:
        """
        Retreives the CA associated with a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_group_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_group_certificate_authority)
        """

    def get_group_certificate_configuration(
        self, **kwargs: Unpack[GetGroupCertificateConfigurationRequestTypeDef]
    ) -> GetGroupCertificateConfigurationResponseTypeDef:
        """
        Retrieves the current configuration for the CA used by the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_group_certificate_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_group_certificate_configuration)
        """

    def get_group_version(
        self, **kwargs: Unpack[GetGroupVersionRequestTypeDef]
    ) -> GetGroupVersionResponseTypeDef:
        """
        Retrieves information about a group version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_group_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_group_version)
        """

    def get_logger_definition(
        self, **kwargs: Unpack[GetLoggerDefinitionRequestTypeDef]
    ) -> GetLoggerDefinitionResponseTypeDef:
        """
        Retrieves information about a logger definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_logger_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_logger_definition)
        """

    def get_logger_definition_version(
        self, **kwargs: Unpack[GetLoggerDefinitionVersionRequestTypeDef]
    ) -> GetLoggerDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a logger definition version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_logger_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_logger_definition_version)
        """

    def get_resource_definition(
        self, **kwargs: Unpack[GetResourceDefinitionRequestTypeDef]
    ) -> GetResourceDefinitionResponseTypeDef:
        """
        Retrieves information about a resource definition, including its creation time
        and latest version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_resource_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_resource_definition)
        """

    def get_resource_definition_version(
        self, **kwargs: Unpack[GetResourceDefinitionVersionRequestTypeDef]
    ) -> GetResourceDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a resource definition version, including which
        resources are included in the version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_resource_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_resource_definition_version)
        """

    def get_service_role_for_account(self) -> GetServiceRoleForAccountResponseTypeDef:
        """
        Retrieves the service role that is attached to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_service_role_for_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_service_role_for_account)
        """

    def get_subscription_definition(
        self, **kwargs: Unpack[GetSubscriptionDefinitionRequestTypeDef]
    ) -> GetSubscriptionDefinitionResponseTypeDef:
        """
        Retrieves information about a subscription definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_subscription_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_subscription_definition)
        """

    def get_subscription_definition_version(
        self, **kwargs: Unpack[GetSubscriptionDefinitionVersionRequestTypeDef]
    ) -> GetSubscriptionDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a subscription definition version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_subscription_definition_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_subscription_definition_version)
        """

    def get_thing_runtime_configuration(
        self, **kwargs: Unpack[GetThingRuntimeConfigurationRequestTypeDef]
    ) -> GetThingRuntimeConfigurationResponseTypeDef:
        """
        Get the runtime configuration of a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_thing_runtime_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_thing_runtime_configuration)
        """

    def list_bulk_deployment_detailed_reports(
        self, **kwargs: Unpack[ListBulkDeploymentDetailedReportsRequestTypeDef]
    ) -> ListBulkDeploymentDetailedReportsResponseTypeDef:
        """
        Gets a paginated list of the deployments that have been started in a bulk
        deployment operation, and their current deployment status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_bulk_deployment_detailed_reports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_bulk_deployment_detailed_reports)
        """

    def list_bulk_deployments(
        self, **kwargs: Unpack[ListBulkDeploymentsRequestTypeDef]
    ) -> ListBulkDeploymentsResponseTypeDef:
        """
        Returns a list of bulk deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_bulk_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_bulk_deployments)
        """

    def list_connector_definition_versions(
        self, **kwargs: Unpack[ListConnectorDefinitionVersionsRequestTypeDef]
    ) -> ListConnectorDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a connector definition, which are containers for
        connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_connector_definition_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_connector_definition_versions)
        """

    def list_connector_definitions(
        self, **kwargs: Unpack[ListConnectorDefinitionsRequestTypeDef]
    ) -> ListConnectorDefinitionsResponseTypeDef:
        """
        Retrieves a list of connector definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_connector_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_connector_definitions)
        """

    def list_core_definition_versions(
        self, **kwargs: Unpack[ListCoreDefinitionVersionsRequestTypeDef]
    ) -> ListCoreDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a core definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_core_definition_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_core_definition_versions)
        """

    def list_core_definitions(
        self, **kwargs: Unpack[ListCoreDefinitionsRequestTypeDef]
    ) -> ListCoreDefinitionsResponseTypeDef:
        """
        Retrieves a list of core definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_core_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_core_definitions)
        """

    def list_deployments(
        self, **kwargs: Unpack[ListDeploymentsRequestTypeDef]
    ) -> ListDeploymentsResponseTypeDef:
        """
        Returns a history of deployments for the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_deployments)
        """

    def list_device_definition_versions(
        self, **kwargs: Unpack[ListDeviceDefinitionVersionsRequestTypeDef]
    ) -> ListDeviceDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a device definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_device_definition_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_device_definition_versions)
        """

    def list_device_definitions(
        self, **kwargs: Unpack[ListDeviceDefinitionsRequestTypeDef]
    ) -> ListDeviceDefinitionsResponseTypeDef:
        """
        Retrieves a list of device definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_device_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_device_definitions)
        """

    def list_function_definition_versions(
        self, **kwargs: Unpack[ListFunctionDefinitionVersionsRequestTypeDef]
    ) -> ListFunctionDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a Lambda function definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_function_definition_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_function_definition_versions)
        """

    def list_function_definitions(
        self, **kwargs: Unpack[ListFunctionDefinitionsRequestTypeDef]
    ) -> ListFunctionDefinitionsResponseTypeDef:
        """
        Retrieves a list of Lambda function definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_function_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_function_definitions)
        """

    def list_group_certificate_authorities(
        self, **kwargs: Unpack[ListGroupCertificateAuthoritiesRequestTypeDef]
    ) -> ListGroupCertificateAuthoritiesResponseTypeDef:
        """
        Retrieves the current CAs for a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_group_certificate_authorities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_group_certificate_authorities)
        """

    def list_group_versions(
        self, **kwargs: Unpack[ListGroupVersionsRequestTypeDef]
    ) -> ListGroupVersionsResponseTypeDef:
        """
        Lists the versions of a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_group_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_group_versions)
        """

    def list_groups(self, **kwargs: Unpack[ListGroupsRequestTypeDef]) -> ListGroupsResponseTypeDef:
        """
        Retrieves a list of groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_groups)
        """

    def list_logger_definition_versions(
        self, **kwargs: Unpack[ListLoggerDefinitionVersionsRequestTypeDef]
    ) -> ListLoggerDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a logger definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_logger_definition_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_logger_definition_versions)
        """

    def list_logger_definitions(
        self, **kwargs: Unpack[ListLoggerDefinitionsRequestTypeDef]
    ) -> ListLoggerDefinitionsResponseTypeDef:
        """
        Retrieves a list of logger definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_logger_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_logger_definitions)
        """

    def list_resource_definition_versions(
        self, **kwargs: Unpack[ListResourceDefinitionVersionsRequestTypeDef]
    ) -> ListResourceDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a resource definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_resource_definition_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_resource_definition_versions)
        """

    def list_resource_definitions(
        self, **kwargs: Unpack[ListResourceDefinitionsRequestTypeDef]
    ) -> ListResourceDefinitionsResponseTypeDef:
        """
        Retrieves a list of resource definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_resource_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_resource_definitions)
        """

    def list_subscription_definition_versions(
        self, **kwargs: Unpack[ListSubscriptionDefinitionVersionsRequestTypeDef]
    ) -> ListSubscriptionDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a subscription definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_subscription_definition_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_subscription_definition_versions)
        """

    def list_subscription_definitions(
        self, **kwargs: Unpack[ListSubscriptionDefinitionsRequestTypeDef]
    ) -> ListSubscriptionDefinitionsResponseTypeDef:
        """
        Retrieves a list of subscription definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_subscription_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_subscription_definitions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of resource tags for a resource arn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#list_tags_for_resource)
        """

    def reset_deployments(
        self, **kwargs: Unpack[ResetDeploymentsRequestTypeDef]
    ) -> ResetDeploymentsResponseTypeDef:
        """
        Resets a group's deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/reset_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#reset_deployments)
        """

    def start_bulk_deployment(
        self, **kwargs: Unpack[StartBulkDeploymentRequestTypeDef]
    ) -> StartBulkDeploymentResponseTypeDef:
        """
        Deploys multiple groups in one operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/start_bulk_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#start_bulk_deployment)
        """

    def stop_bulk_deployment(
        self, **kwargs: Unpack[StopBulkDeploymentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops the execution of a bulk deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/stop_bulk_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#stop_bulk_deployment)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to a Greengrass resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove resource tags from a Greengrass Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#untag_resource)
        """

    def update_connectivity_info(
        self, **kwargs: Unpack[UpdateConnectivityInfoRequestTypeDef]
    ) -> UpdateConnectivityInfoResponseTypeDef:
        """
        Updates the connectivity information for the core.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_connectivity_info.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_connectivity_info)
        """

    def update_connector_definition(
        self, **kwargs: Unpack[UpdateConnectorDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a connector definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_connector_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_connector_definition)
        """

    def update_core_definition(
        self, **kwargs: Unpack[UpdateCoreDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a core definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_core_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_core_definition)
        """

    def update_device_definition(
        self, **kwargs: Unpack[UpdateDeviceDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a device definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_device_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_device_definition)
        """

    def update_function_definition(
        self, **kwargs: Unpack[UpdateFunctionDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a Lambda function definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_function_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_function_definition)
        """

    def update_group(self, **kwargs: Unpack[UpdateGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_group)
        """

    def update_group_certificate_configuration(
        self, **kwargs: Unpack[UpdateGroupCertificateConfigurationRequestTypeDef]
    ) -> UpdateGroupCertificateConfigurationResponseTypeDef:
        """
        Updates the Certificate expiry time for a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_group_certificate_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_group_certificate_configuration)
        """

    def update_logger_definition(
        self, **kwargs: Unpack[UpdateLoggerDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a logger definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_logger_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_logger_definition)
        """

    def update_resource_definition(
        self, **kwargs: Unpack[UpdateResourceDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a resource definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_resource_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_resource_definition)
        """

    def update_subscription_definition(
        self, **kwargs: Unpack[UpdateSubscriptionDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a subscription definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_subscription_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_subscription_definition)
        """

    def update_thing_runtime_configuration(
        self, **kwargs: Unpack[UpdateThingRuntimeConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the runtime configuration of a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/update_thing_runtime_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#update_thing_runtime_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bulk_deployment_detailed_reports"]
    ) -> ListBulkDeploymentDetailedReportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bulk_deployments"]
    ) -> ListBulkDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connector_definition_versions"]
    ) -> ListConnectorDefinitionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connector_definitions"]
    ) -> ListConnectorDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_core_definition_versions"]
    ) -> ListCoreDefinitionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_core_definitions"]
    ) -> ListCoreDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_definition_versions"]
    ) -> ListDeviceDefinitionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_definitions"]
    ) -> ListDeviceDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_function_definition_versions"]
    ) -> ListFunctionDefinitionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_function_definitions"]
    ) -> ListFunctionDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_group_versions"]
    ) -> ListGroupVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups"]
    ) -> ListGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_logger_definition_versions"]
    ) -> ListLoggerDefinitionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_logger_definitions"]
    ) -> ListLoggerDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_definition_versions"]
    ) -> ListResourceDefinitionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_definitions"]
    ) -> ListResourceDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscription_definition_versions"]
    ) -> ListSubscriptionDefinitionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscription_definitions"]
    ) -> ListSubscriptionDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client/#get_paginator)
        """
