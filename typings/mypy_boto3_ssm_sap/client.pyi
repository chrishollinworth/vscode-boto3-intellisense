"""
Type annotations for ssm-sap service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm_sap import SsmSapClient

    client: SsmSapClient = boto3.client("ssm-sap")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListApplicationsPaginator, ListComponentsPaginator, ListDatabasesPaginator
from .type_defs import (
    ApplicationCredentialTypeDef,
    DeleteResourcePermissionOutputTypeDef,
    GetApplicationOutputTypeDef,
    GetComponentOutputTypeDef,
    GetDatabaseOutputTypeDef,
    GetOperationOutputTypeDef,
    GetResourcePermissionOutputTypeDef,
    ListApplicationsOutputTypeDef,
    ListComponentsOutputTypeDef,
    ListDatabasesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutResourcePermissionOutputTypeDef,
    RegisterApplicationOutputTypeDef,
    UpdateApplicationSettingsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SsmSapClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SsmSapClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SsmSapClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#close)
        """
    def delete_resource_permission(
        self,
        *,
        ResourceArn: str,
        ActionType: Literal["RESTORE"] = None,
        SourceResourceArn: str = None
    ) -> DeleteResourcePermissionOutputTypeDef:
        """
        Removes permissions associated with the target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.delete_resource_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#delete_resource_permission)
        """
    def deregister_application(self, *, ApplicationId: str) -> Dict[str, Any]:
        """
        Deregister an SAP application with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.deregister_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#deregister_application)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#generate_presigned_url)
        """
    def get_application(
        self, *, ApplicationId: str = None, ApplicationArn: str = None
    ) -> GetApplicationOutputTypeDef:
        """
        Gets an application registered with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#get_application)
        """
    def get_component(self, *, ApplicationId: str, ComponentId: str) -> GetComponentOutputTypeDef:
        """
        Gets the component of an application registered with AWS Systems Manager for
        SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.get_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#get_component)
        """
    def get_database(
        self,
        *,
        ApplicationId: str = None,
        ComponentId: str = None,
        DatabaseId: str = None,
        DatabaseArn: str = None
    ) -> GetDatabaseOutputTypeDef:
        """
        Gets the SAP HANA database of an application registered with AWS Systems Manager
        for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.get_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#get_database)
        """
    def get_operation(self, *, OperationId: str) -> GetOperationOutputTypeDef:
        """
        Gets the details of an operation by specifying the operation ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.get_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#get_operation)
        """
    def get_resource_permission(
        self, *, ResourceArn: str, ActionType: Literal["RESTORE"] = None
    ) -> GetResourcePermissionOutputTypeDef:
        """
        Gets permissions associated with the target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.get_resource_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#get_resource_permission)
        """
    def list_applications(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListApplicationsOutputTypeDef:
        """
        Lists all the applications registered with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#list_applications)
        """
    def list_components(
        self, *, ApplicationId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListComponentsOutputTypeDef:
        """
        Lists all the components registered with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#list_components)
        """
    def list_databases(
        self,
        *,
        ApplicationId: str = None,
        ComponentId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDatabasesOutputTypeDef:
        """
        Lists the SAP HANA databases of an application registered with AWS Systems
        Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.list_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#list_databases)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags on an SAP HANA application and/or database registered with AWS
        Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#list_tags_for_resource)
        """
    def put_resource_permission(
        self, *, ActionType: Literal["RESTORE"], SourceResourceArn: str, ResourceArn: str
    ) -> PutResourcePermissionOutputTypeDef:
        """
        Adds permissions to the target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.put_resource_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#put_resource_permission)
        """
    def register_application(
        self,
        *,
        ApplicationId: str,
        ApplicationType: Literal["HANA"],
        Instances: List[str],
        Credentials: List["ApplicationCredentialTypeDef"],
        SapInstanceNumber: str = None,
        Sid: str = None,
        Tags: Dict[str, str] = None
    ) -> RegisterApplicationOutputTypeDef:
        """
        Register an SAP application with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.register_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#register_application)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Creates tag for a resource by specifying the ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Delete the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#untag_resource)
        """
    def update_application_settings(
        self,
        *,
        ApplicationId: str,
        CredentialsToAddOrUpdate: List["ApplicationCredentialTypeDef"] = None,
        CredentialsToRemove: List["ApplicationCredentialTypeDef"] = None
    ) -> UpdateApplicationSettingsOutputTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-
        sap-2018-05-10/UpdateApplicationSettings>`_ **Request Syntax** response =
        client.update_application_settings( ApplicationId='string',
        CredentialsToAddOrUpdate=[ { 'DatabaseNa...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Client.update_application_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/client.html#update_application_settings)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listapplicationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_components"]) -> ListComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Paginator.ListComponents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listcomponentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/ssm-sap.html#SsmSap.Paginator.ListDatabases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listdatabasespaginator)
        """
