"""
Type annotations for connectcases service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_connectcases import ConnectCasesClient

    client: ConnectCasesClient = boto3.client("connectcases")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import FieldTypeType, RelatedItemTypeType, TemplateStatusType
from .paginator import SearchCasesPaginator, SearchRelatedItemsPaginator
from .type_defs import (
    BatchGetFieldResponseTypeDef,
    BatchPutFieldOptionsResponseTypeDef,
    CaseFilterTypeDef,
    CreateCaseResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateFieldResponseTypeDef,
    CreateLayoutResponseTypeDef,
    CreateRelatedItemResponseTypeDef,
    CreateTemplateResponseTypeDef,
    EventBridgeConfigurationTypeDef,
    FieldIdentifierTypeDef,
    FieldOptionTypeDef,
    FieldValueTypeDef,
    GetCaseEventConfigurationResponseTypeDef,
    GetCaseResponseTypeDef,
    GetDomainResponseTypeDef,
    GetLayoutResponseTypeDef,
    GetTemplateResponseTypeDef,
    LayoutConfigurationTypeDef,
    LayoutContentTypeDef,
    ListCasesForContactResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListFieldOptionsResponseTypeDef,
    ListFieldsResponseTypeDef,
    ListLayoutsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplatesResponseTypeDef,
    RelatedItemInputContentTypeDef,
    RelatedItemTypeFilterTypeDef,
    RequiredFieldTypeDef,
    SearchCasesResponseTypeDef,
    SearchRelatedItemsResponseTypeDef,
    SortTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConnectCasesClient",)

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

class ConnectCasesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectCasesClient exceptions.
        """
    def batch_get_field(
        self, *, domainId: str, fields: List["FieldIdentifierTypeDef"]
    ) -> BatchGetFieldResponseTypeDef:
        """
        Returns the description for the list of fields in the request parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.batch_get_field)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#batch_get_field)
        """
    def batch_put_field_options(
        self, *, domainId: str, fieldId: str, options: List["FieldOptionTypeDef"]
    ) -> BatchPutFieldOptionsResponseTypeDef:
        """
        Creates and updates a set of field options for a single select field in a Cases
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.batch_put_field_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#batch_put_field_options)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#close)
        """
    def create_case(
        self,
        *,
        domainId: str,
        fields: List["FieldValueTypeDef"],
        templateId: str,
        clientToken: str = None
    ) -> CreateCaseResponseTypeDef:
        """
        Creates a case in the specified Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.create_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#create_case)
        """
    def create_domain(self, *, name: str) -> CreateDomainResponseTypeDef:
        """
        Creates a domain, which is a container for all case data, such as cases, fields,
        templates and layouts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#create_domain)
        """
    def create_field(
        self, *, domainId: str, name: str, type: FieldTypeType, description: str = None
    ) -> CreateFieldResponseTypeDef:
        """
        Creates a field in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.create_field)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#create_field)
        """
    def create_layout(
        self, *, content: "LayoutContentTypeDef", domainId: str, name: str
    ) -> CreateLayoutResponseTypeDef:
        """
        Creates a layout in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.create_layout)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#create_layout)
        """
    def create_related_item(
        self,
        *,
        caseId: str,
        content: "RelatedItemInputContentTypeDef",
        domainId: str,
        type: RelatedItemTypeType
    ) -> CreateRelatedItemResponseTypeDef:
        """
        Creates a related item (comments, tasks, and contacts) and associates it with a
        case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.create_related_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#create_related_item)
        """
    def create_template(
        self,
        *,
        domainId: str,
        name: str,
        description: str = None,
        layoutConfiguration: "LayoutConfigurationTypeDef" = None,
        requiredFields: List["RequiredFieldTypeDef"] = None,
        status: TemplateStatusType = None
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates a template in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.create_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#create_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#generate_presigned_url)
        """
    def get_case(
        self,
        *,
        caseId: str,
        domainId: str,
        fields: List["FieldIdentifierTypeDef"],
        nextToken: str = None
    ) -> GetCaseResponseTypeDef:
        """
        Returns information about a specific case if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.get_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#get_case)
        """
    def get_case_event_configuration(
        self, *, domainId: str
    ) -> GetCaseEventConfigurationResponseTypeDef:
        """
        Returns the case event publishing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.get_case_event_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#get_case_event_configuration)
        """
    def get_domain(self, *, domainId: str) -> GetDomainResponseTypeDef:
        """
        Returns information about a specific domain if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.get_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#get_domain)
        """
    def get_layout(self, *, domainId: str, layoutId: str) -> GetLayoutResponseTypeDef:
        """
        Returns the details for the requested layout.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.get_layout)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#get_layout)
        """
    def get_template(self, *, domainId: str, templateId: str) -> GetTemplateResponseTypeDef:
        """
        Returns the details for the requested template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.get_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#get_template)
        """
    def list_cases_for_contact(
        self, *, contactArn: str, domainId: str, maxResults: int = None, nextToken: str = None
    ) -> ListCasesForContactResponseTypeDef:
        """
        Lists cases for a given contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.list_cases_for_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#list_cases_for_contact)
        """
    def list_domains(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListDomainsResponseTypeDef:
        """
        Lists all cases domains in the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#list_domains)
        """
    def list_field_options(
        self,
        *,
        domainId: str,
        fieldId: str,
        maxResults: int = None,
        nextToken: str = None,
        values: List[str] = None
    ) -> ListFieldOptionsResponseTypeDef:
        """
        Lists all of the field options for a field identifier in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.list_field_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#list_field_options)
        """
    def list_fields(
        self, *, domainId: str, maxResults: int = None, nextToken: str = None
    ) -> ListFieldsResponseTypeDef:
        """
        Lists all fields in a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.list_fields)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#list_fields)
        """
    def list_layouts(
        self, *, domainId: str, maxResults: int = None, nextToken: str = None
    ) -> ListLayoutsResponseTypeDef:
        """
        Lists all layouts in the given cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.list_layouts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#list_layouts)
        """
    def list_tags_for_resource(self, *, arn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#list_tags_for_resource)
        """
    def list_templates(
        self,
        *,
        domainId: str,
        maxResults: int = None,
        nextToken: str = None,
        status: List[TemplateStatusType] = None
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists all of the templates in a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#list_templates)
        """
    def put_case_event_configuration(
        self, *, domainId: str, eventBridge: "EventBridgeConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        API for adding case event publishing configuration See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/connectcases-2022-10-
        03/PutCaseEventConfiguration>`_ **Request Syntax** response =
        client.put_case_event_configuration( domainId='string', eventBrid...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.put_case_event_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#put_case_event_configuration)
        """
    def search_cases(
        self,
        *,
        domainId: str,
        fields: List["FieldIdentifierTypeDef"] = None,
        filter: "CaseFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        searchTerm: str = None,
        sorts: List["SortTypeDef"] = None
    ) -> SearchCasesResponseTypeDef:
        """
        Searches for cases within their associated Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.search_cases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#search_cases)
        """
    def search_related_items(
        self,
        *,
        caseId: str,
        domainId: str,
        filters: List["RelatedItemTypeFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchRelatedItemsResponseTypeDef:
        """
        Searches for related items that are associated with a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.search_related_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#search_related_items)
        """
    def tag_resource(self, *, arn: str, tags: Dict[str, str]) -> None:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#tag_resource)
        """
    def untag_resource(self, *, arn: str, tagKeys: List[str]) -> None:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#untag_resource)
        """
    def update_case(
        self, *, caseId: str, domainId: str, fields: List["FieldValueTypeDef"]
    ) -> Dict[str, Any]:
        """
        Updates the values of fields on a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.update_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#update_case)
        """
    def update_field(
        self, *, domainId: str, fieldId: str, description: str = None, name: str = None
    ) -> Dict[str, Any]:
        """
        Updates the properties of an existing field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.update_field)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#update_field)
        """
    def update_layout(
        self,
        *,
        domainId: str,
        layoutId: str,
        content: "LayoutContentTypeDef" = None,
        name: str = None
    ) -> Dict[str, Any]:
        """
        Updates the attributes of an existing layout.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.update_layout)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#update_layout)
        """
    def update_template(
        self,
        *,
        domainId: str,
        templateId: str,
        description: str = None,
        layoutConfiguration: "LayoutConfigurationTypeDef" = None,
        name: str = None,
        requiredFields: List["RequiredFieldTypeDef"] = None,
        status: TemplateStatusType = None
    ) -> Dict[str, Any]:
        """
        Updates the attributes of an existing template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Client.update_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client.html#update_template)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_cases"]) -> SearchCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Paginator.SearchCases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators.html#searchcasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_related_items"]
    ) -> SearchRelatedItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/connectcases.html#ConnectCases.Paginator.SearchRelatedItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators.html#searchrelateditemspaginator)
        """
