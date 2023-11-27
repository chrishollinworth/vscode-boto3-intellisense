"""
Type annotations for pca-connector-ad service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pca_connector_ad import PcaConnectorAdClient

    client: PcaConnectorAdClient = boto3.client("pca-connector-ad")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListConnectorsPaginator,
    ListDirectoryRegistrationsPaginator,
    ListServicePrincipalNamesPaginator,
    ListTemplateGroupAccessControlEntriesPaginator,
    ListTemplatesPaginator,
)
from .type_defs import (
    AccessRightsTypeDef,
    CreateConnectorResponseTypeDef,
    CreateDirectoryRegistrationResponseTypeDef,
    CreateTemplateResponseTypeDef,
    GetConnectorResponseTypeDef,
    GetDirectoryRegistrationResponseTypeDef,
    GetServicePrincipalNameResponseTypeDef,
    GetTemplateGroupAccessControlEntryResponseTypeDef,
    GetTemplateResponseTypeDef,
    ListConnectorsResponseTypeDef,
    ListDirectoryRegistrationsResponseTypeDef,
    ListServicePrincipalNamesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateGroupAccessControlEntriesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    TemplateDefinitionTypeDef,
    VpcInformationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PcaConnectorAdClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PcaConnectorAdClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PcaConnectorAdClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#close)
        """
    def create_connector(
        self,
        *,
        CertificateAuthorityArn: str,
        DirectoryId: str,
        VpcInformation: "VpcInformationTypeDef",
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a connector between Amazon Web Services Private CA and an Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#create_connector)
        """
    def create_directory_registration(
        self, *, DirectoryId: str, ClientToken: str = None, Tags: Dict[str, str] = None
    ) -> CreateDirectoryRegistrationResponseTypeDef:
        """
        Creates a directory registration that authorizes communication between Amazon
        Web Services Private CA and an Active Directory See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pca-connector-
        ad-2018-05-10/CreateDirectoryRegistration>`_ **Request Syntax** response...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_directory_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#create_directory_registration)
        """
    def create_service_principal_name(
        self, *, ConnectorArn: str, DirectoryRegistrationArn: str, ClientToken: str = None
    ) -> None:
        """
        Creates a service principal name (SPN) for the service account in Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_service_principal_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#create_service_principal_name)
        """
    def create_template(
        self,
        *,
        ConnectorArn: str,
        Definition: "TemplateDefinitionTypeDef",
        Name: str,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates an Active Directory compatible certificate template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#create_template)
        """
    def create_template_group_access_control_entry(
        self,
        *,
        AccessRights: "AccessRightsTypeDef",
        GroupDisplayName: str,
        GroupSecurityIdentifier: str,
        TemplateArn: str,
        ClientToken: str = None
    ) -> None:
        """
        Create a group access control entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_template_group_access_control_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#create_template_group_access_control_entry)
        """
    def delete_connector(self, *, ConnectorArn: str) -> None:
        """
        Deletes a connector for Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#delete_connector)
        """
    def delete_directory_registration(self, *, DirectoryRegistrationArn: str) -> None:
        """
        Deletes a directory registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_directory_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#delete_directory_registration)
        """
    def delete_service_principal_name(
        self, *, ConnectorArn: str, DirectoryRegistrationArn: str
    ) -> None:
        """
        Deletes the service principal name (SPN) used by a connector to authenticate
        with your Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_service_principal_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#delete_service_principal_name)
        """
    def delete_template(self, *, TemplateArn: str) -> None:
        """
        Deletes a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#delete_template)
        """
    def delete_template_group_access_control_entry(
        self, *, GroupSecurityIdentifier: str, TemplateArn: str
    ) -> None:
        """
        Deletes a group access control entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_template_group_access_control_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#delete_template_group_access_control_entry)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#generate_presigned_url)
        """
    def get_connector(self, *, ConnectorArn: str) -> GetConnectorResponseTypeDef:
        """
        Lists information about your connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#get_connector)
        """
    def get_directory_registration(
        self, *, DirectoryRegistrationArn: str
    ) -> GetDirectoryRegistrationResponseTypeDef:
        """
        A structure that contains information about your directory registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_directory_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#get_directory_registration)
        """
    def get_service_principal_name(
        self, *, ConnectorArn: str, DirectoryRegistrationArn: str
    ) -> GetServicePrincipalNameResponseTypeDef:
        """
        Lists the service principal name that the connector uses to authenticate with
        Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_service_principal_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#get_service_principal_name)
        """
    def get_template(self, *, TemplateArn: str) -> GetTemplateResponseTypeDef:
        """
        Retrieves a certificate template that the connector uses to issue certificates
        from a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#get_template)
        """
    def get_template_group_access_control_entry(
        self, *, GroupSecurityIdentifier: str, TemplateArn: str
    ) -> GetTemplateGroupAccessControlEntryResponseTypeDef:
        """
        Retrieves the group access control entries for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_template_group_access_control_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#get_template_group_access_control_entry)
        """
    def list_connectors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors that you created by using the
        `https\://docs.aws.amazon.com/pca-connector-
        ad/latest/APIReference/API_CreateConnector <https://docs.aws.amazon.com/pca-
        connector-ad/latest/APIReference/API_CreateConnector>`__ action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#list_connectors)
        """
    def list_directory_registrations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDirectoryRegistrationsResponseTypeDef:
        """
        Lists the directory registrations that you created by using the
        `https\://docs.aws.amazon.com/pca-connector-
        ad/latest/APIReference/API_CreateDirectoryRegistration
        <https://docs.aws.amazon.com/pca-connector-
        ad/latest/APIReference/API_CreateDirectoryRegistration>`__ action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_directory_registrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#list_directory_registrations)
        """
    def list_service_principal_names(
        self, *, DirectoryRegistrationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListServicePrincipalNamesResponseTypeDef:
        """
        Lists the service principal names that the connector uses to authenticate with
        Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_service_principal_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#list_service_principal_names)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags, if any, that are associated with your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#list_tags_for_resource)
        """
    def list_template_group_access_control_entries(
        self, *, TemplateArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTemplateGroupAccessControlEntriesResponseTypeDef:
        """
        Lists group access control entries you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_template_group_access_control_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#list_template_group_access_control_entries)
        """
    def list_templates(
        self, *, ConnectorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists the templates, if any, that are associated with a connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#list_templates)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Adds one or more tags to your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes one or more tags from your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#untag_resource)
        """
    def update_template(
        self,
        *,
        TemplateArn: str,
        Definition: "TemplateDefinitionTypeDef" = None,
        ReenrollAllCertificateHolders: bool = None
    ) -> None:
        """
        Update template configuration to define the information included in
        certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.update_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#update_template)
        """
    def update_template_group_access_control_entry(
        self,
        *,
        GroupSecurityIdentifier: str,
        TemplateArn: str,
        AccessRights: "AccessRightsTypeDef" = None,
        GroupDisplayName: str = None
    ) -> None:
        """
        Update a group access control entry you created using
        `CreateTemplateGroupAccessControlEntry <https://docs.aws.amazon.com/pca-
        connector-
        ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.update_template_group_access_control_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/client.html#update_template_group_access_control_entry)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListConnectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listconnectorspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_directory_registrations"]
    ) -> ListDirectoryRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListDirectoryRegistrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listdirectoryregistrationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_principal_names"]
    ) -> ListServicePrincipalNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListServicePrincipalNames)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listserviceprincipalnamespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_group_access_control_entries"]
    ) -> ListTemplateGroupAccessControlEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListTemplateGroupAccessControlEntries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listtemplategroupaccesscontrolentriespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listtemplatespaginator)
        """
