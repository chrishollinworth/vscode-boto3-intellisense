"""
Type annotations for connectcases service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connectcases.client import ConnectCasesClient

    session = Session()
    client: ConnectCasesClient = session.client("connectcases")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListCaseRulesPaginator,
    SearchAllRelatedItemsPaginator,
    SearchCasesPaginator,
    SearchRelatedItemsPaginator,
)
from .type_defs import (
    BatchGetCaseRuleRequestTypeDef,
    BatchGetCaseRuleResponseTypeDef,
    BatchGetFieldRequestTypeDef,
    BatchGetFieldResponseTypeDef,
    BatchPutFieldOptionsRequestTypeDef,
    BatchPutFieldOptionsResponseTypeDef,
    CreateCaseRequestTypeDef,
    CreateCaseResponseTypeDef,
    CreateCaseRuleRequestTypeDef,
    CreateCaseRuleResponseTypeDef,
    CreateDomainRequestTypeDef,
    CreateDomainResponseTypeDef,
    CreateFieldRequestTypeDef,
    CreateFieldResponseTypeDef,
    CreateLayoutRequestTypeDef,
    CreateLayoutResponseTypeDef,
    CreateRelatedItemRequestTypeDef,
    CreateRelatedItemResponseTypeDef,
    CreateTemplateRequestTypeDef,
    CreateTemplateResponseTypeDef,
    DeleteCaseRequestTypeDef,
    DeleteCaseRuleRequestTypeDef,
    DeleteDomainRequestTypeDef,
    DeleteFieldRequestTypeDef,
    DeleteLayoutRequestTypeDef,
    DeleteRelatedItemRequestTypeDef,
    DeleteTemplateRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCaseAuditEventsRequestTypeDef,
    GetCaseAuditEventsResponseTypeDef,
    GetCaseEventConfigurationRequestTypeDef,
    GetCaseEventConfigurationResponseTypeDef,
    GetCaseRequestTypeDef,
    GetCaseResponseTypeDef,
    GetDomainRequestTypeDef,
    GetDomainResponseTypeDef,
    GetLayoutRequestTypeDef,
    GetLayoutResponseTypeDef,
    GetTemplateRequestTypeDef,
    GetTemplateResponseTypeDef,
    ListCaseRulesRequestTypeDef,
    ListCaseRulesResponseTypeDef,
    ListCasesForContactRequestTypeDef,
    ListCasesForContactResponseTypeDef,
    ListDomainsRequestTypeDef,
    ListDomainsResponseTypeDef,
    ListFieldOptionsRequestTypeDef,
    ListFieldOptionsResponseTypeDef,
    ListFieldsRequestTypeDef,
    ListFieldsResponseTypeDef,
    ListLayoutsRequestTypeDef,
    ListLayoutsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplatesRequestTypeDef,
    ListTemplatesResponseTypeDef,
    PutCaseEventConfigurationRequestTypeDef,
    SearchAllRelatedItemsRequestTypeDef,
    SearchAllRelatedItemsResponseTypeDef,
    SearchCasesRequestTypeDef,
    SearchCasesResponseTypeDef,
    SearchRelatedItemsRequestTypeDef,
    SearchRelatedItemsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCaseRequestTypeDef,
    UpdateCaseRuleRequestTypeDef,
    UpdateFieldRequestTypeDef,
    UpdateLayoutRequestTypeDef,
    UpdateTemplateRequestTypeDef,
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

__all__ = ("ConnectCasesClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectCasesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#generate_presigned_url)
        """

    def batch_get_case_rule(
        self, **kwargs: Unpack[BatchGetCaseRuleRequestTypeDef]
    ) -> BatchGetCaseRuleResponseTypeDef:
        """
        Gets a batch of case rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/batch_get_case_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#batch_get_case_rule)
        """

    def batch_get_field(
        self, **kwargs: Unpack[BatchGetFieldRequestTypeDef]
    ) -> BatchGetFieldResponseTypeDef:
        """
        Returns the description for the list of fields in the request parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/batch_get_field.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#batch_get_field)
        """

    def batch_put_field_options(
        self, **kwargs: Unpack[BatchPutFieldOptionsRequestTypeDef]
    ) -> BatchPutFieldOptionsResponseTypeDef:
        """
        Creates and updates a set of field options for a single select field in a Cases
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/batch_put_field_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#batch_put_field_options)
        """

    def create_case(self, **kwargs: Unpack[CreateCaseRequestTypeDef]) -> CreateCaseResponseTypeDef:
        """
        <note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must
        also have <a
        href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a>
        permission on the User ARN resource that you provide.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/create_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#create_case)
        """

    def create_case_rule(
        self, **kwargs: Unpack[CreateCaseRuleRequestTypeDef]
    ) -> CreateCaseRuleResponseTypeDef:
        """
        Creates a new case rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/create_case_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#create_case_rule)
        """

    def create_domain(
        self, **kwargs: Unpack[CreateDomainRequestTypeDef]
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a domain, which is a container for all case data, such as cases,
        fields, templates and layouts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/create_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#create_domain)
        """

    def create_field(
        self, **kwargs: Unpack[CreateFieldRequestTypeDef]
    ) -> CreateFieldResponseTypeDef:
        """
        Creates a field in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/create_field.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#create_field)
        """

    def create_layout(
        self, **kwargs: Unpack[CreateLayoutRequestTypeDef]
    ) -> CreateLayoutResponseTypeDef:
        """
        Creates a layout in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/create_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#create_layout)
        """

    def create_related_item(
        self, **kwargs: Unpack[CreateRelatedItemRequestTypeDef]
    ) -> CreateRelatedItemResponseTypeDef:
        """
        Creates a related item (comments, tasks, and contacts) and associates it with a
        case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/create_related_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#create_related_item)
        """

    def create_template(
        self, **kwargs: Unpack[CreateTemplateRequestTypeDef]
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates a template in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/create_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#create_template)
        """

    def delete_case(self, **kwargs: Unpack[DeleteCaseRequestTypeDef]) -> Dict[str, Any]:
        """
        The DeleteCase API permanently deletes a case and all its associated resources
        from the cases data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/delete_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#delete_case)
        """

    def delete_case_rule(self, **kwargs: Unpack[DeleteCaseRuleRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a case rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/delete_case_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#delete_case_rule)
        """

    def delete_domain(self, **kwargs: Unpack[DeleteDomainRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/delete_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#delete_domain)
        """

    def delete_field(self, **kwargs: Unpack[DeleteFieldRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a field from a cases template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/delete_field.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#delete_field)
        """

    def delete_layout(self, **kwargs: Unpack[DeleteLayoutRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a layout from a cases template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/delete_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#delete_layout)
        """

    def delete_related_item(
        self, **kwargs: Unpack[DeleteRelatedItemRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the related item resource under a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/delete_related_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#delete_related_item)
        """

    def delete_template(self, **kwargs: Unpack[DeleteTemplateRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a cases template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/delete_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#delete_template)
        """

    def get_case(self, **kwargs: Unpack[GetCaseRequestTypeDef]) -> GetCaseResponseTypeDef:
        """
        Returns information about a specific case if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_case)
        """

    def get_case_audit_events(
        self, **kwargs: Unpack[GetCaseAuditEventsRequestTypeDef]
    ) -> GetCaseAuditEventsResponseTypeDef:
        """
        Returns the audit history about a specific case if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_case_audit_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_case_audit_events)
        """

    def get_case_event_configuration(
        self, **kwargs: Unpack[GetCaseEventConfigurationRequestTypeDef]
    ) -> GetCaseEventConfigurationResponseTypeDef:
        """
        Returns the case event publishing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_case_event_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_case_event_configuration)
        """

    def get_domain(self, **kwargs: Unpack[GetDomainRequestTypeDef]) -> GetDomainResponseTypeDef:
        """
        Returns information about a specific domain if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_domain)
        """

    def get_layout(self, **kwargs: Unpack[GetLayoutRequestTypeDef]) -> GetLayoutResponseTypeDef:
        """
        Returns the details for the requested layout.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_layout)
        """

    def get_template(
        self, **kwargs: Unpack[GetTemplateRequestTypeDef]
    ) -> GetTemplateResponseTypeDef:
        """
        Returns the details for the requested template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_template)
        """

    def list_case_rules(
        self, **kwargs: Unpack[ListCaseRulesRequestTypeDef]
    ) -> ListCaseRulesResponseTypeDef:
        """
        Lists all case rules in a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_case_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_case_rules)
        """

    def list_cases_for_contact(
        self, **kwargs: Unpack[ListCasesForContactRequestTypeDef]
    ) -> ListCasesForContactResponseTypeDef:
        """
        Lists cases for a given contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_cases_for_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_cases_for_contact)
        """

    def list_domains(
        self, **kwargs: Unpack[ListDomainsRequestTypeDef]
    ) -> ListDomainsResponseTypeDef:
        """
        Lists all cases domains in the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_domains)
        """

    def list_field_options(
        self, **kwargs: Unpack[ListFieldOptionsRequestTypeDef]
    ) -> ListFieldOptionsResponseTypeDef:
        """
        Lists all of the field options for a field identifier in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_field_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_field_options)
        """

    def list_fields(self, **kwargs: Unpack[ListFieldsRequestTypeDef]) -> ListFieldsResponseTypeDef:
        """
        Lists all fields in a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_fields.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_fields)
        """

    def list_layouts(
        self, **kwargs: Unpack[ListLayoutsRequestTypeDef]
    ) -> ListLayoutsResponseTypeDef:
        """
        Lists all layouts in the given cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_layouts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_layouts)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_tags_for_resource)
        """

    def list_templates(
        self, **kwargs: Unpack[ListTemplatesRequestTypeDef]
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists all of the templates in a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/list_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#list_templates)
        """

    def put_case_event_configuration(
        self, **kwargs: Unpack[PutCaseEventConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds case event publishing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/put_case_event_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#put_case_event_configuration)
        """

    def search_all_related_items(
        self, **kwargs: Unpack[SearchAllRelatedItemsRequestTypeDef]
    ) -> SearchAllRelatedItemsResponseTypeDef:
        """
        Searches for related items across all cases within a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/search_all_related_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#search_all_related_items)
        """

    def search_cases(
        self, **kwargs: Unpack[SearchCasesRequestTypeDef]
    ) -> SearchCasesResponseTypeDef:
        """
        Searches for cases within their associated Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/search_cases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#search_cases)
        """

    def search_related_items(
        self, **kwargs: Unpack[SearchRelatedItemsRequestTypeDef]
    ) -> SearchRelatedItemsResponseTypeDef:
        """
        Searches for related items that are associated with a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/search_related_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#search_related_items)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#untag_resource)
        """

    def update_case(self, **kwargs: Unpack[UpdateCaseRequestTypeDef]) -> Dict[str, Any]:
        """
        <note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must
        also have <a
        href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a>
        permission on the User ARN resource that you provide.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/update_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#update_case)
        """

    def update_case_rule(self, **kwargs: Unpack[UpdateCaseRuleRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a case rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/update_case_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#update_case_rule)
        """

    def update_field(self, **kwargs: Unpack[UpdateFieldRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the properties of an existing field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/update_field.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#update_field)
        """

    def update_layout(self, **kwargs: Unpack[UpdateLayoutRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the attributes of an existing layout.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/update_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#update_layout)
        """

    def update_template(self, **kwargs: Unpack[UpdateTemplateRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the attributes of an existing template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/update_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#update_template)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_case_rules"]
    ) -> ListCaseRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_all_related_items"]
    ) -> SearchAllRelatedItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_cases"]
    ) -> SearchCasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_related_items"]
    ) -> SearchRelatedItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/client/#get_paginator)
        """
