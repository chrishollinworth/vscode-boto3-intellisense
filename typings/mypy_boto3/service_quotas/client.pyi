"""
Type annotations for service-quotas service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_service_quotas.client import ServiceQuotasClient

    session = Session()
    client: ServiceQuotasClient = session.client("service-quotas")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAWSDefaultServiceQuotasPaginator,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
    ListRequestedServiceQuotaChangeHistoryPaginator,
    ListServiceQuotaIncreaseRequestsInTemplatePaginator,
    ListServiceQuotasPaginator,
    ListServicesPaginator,
)
from .type_defs import (
    DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef,
    GetAssociationForServiceQuotaTemplateResponseTypeDef,
    GetAWSDefaultServiceQuotaRequestTypeDef,
    GetAWSDefaultServiceQuotaResponseTypeDef,
    GetRequestedServiceQuotaChangeRequestTypeDef,
    GetRequestedServiceQuotaChangeResponseTypeDef,
    GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef,
    GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef,
    GetServiceQuotaRequestTypeDef,
    GetServiceQuotaResponseTypeDef,
    ListAWSDefaultServiceQuotasRequestTypeDef,
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryRequestTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasRequestTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesRequestTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef,
    PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef,
    RequestServiceQuotaIncreaseRequestTypeDef,
    RequestServiceQuotaIncreaseResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("ServiceQuotasClient",)

class Exceptions(BaseClientExceptions):
    AWSServiceAccessNotEnabledException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DependencyAccessDeniedException: Type[BotocoreClientError]
    IllegalArgumentException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    NoAvailableOrganizationException: Type[BotocoreClientError]
    NoSuchResourceException: Type[BotocoreClientError]
    OrganizationNotInAllFeaturesModeException: Type[BotocoreClientError]
    QuotaExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ServiceQuotaTemplateNotInUseException: Type[BotocoreClientError]
    TagPolicyViolationException: Type[BotocoreClientError]
    TemplatesNotAvailableInRegionException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class ServiceQuotasClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ServiceQuotasClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#generate_presigned_url)
        """

    def associate_service_quota_template(self) -> Dict[str, Any]:
        """
        Associates your quota request template with your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/associate_service_quota_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#associate_service_quota_template)
        """

    def delete_service_quota_increase_request_from_template(
        self, **kwargs: Unpack[DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the quota increase request for the specified quota from your quota
        request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/delete_service_quota_increase_request_from_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#delete_service_quota_increase_request_from_template)
        """

    def disassociate_service_quota_template(self) -> Dict[str, Any]:
        """
        Disables your quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/disassociate_service_quota_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#disassociate_service_quota_template)
        """

    def get_aws_default_service_quota(
        self, **kwargs: Unpack[GetAWSDefaultServiceQuotaRequestTypeDef]
    ) -> GetAWSDefaultServiceQuotaResponseTypeDef:
        """
        Retrieves the default value for the specified quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_aws_default_service_quota.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_aws_default_service_quota)
        """

    def get_association_for_service_quota_template(
        self,
    ) -> GetAssociationForServiceQuotaTemplateResponseTypeDef:
        """
        Retrieves the status of the association for the quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_association_for_service_quota_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_association_for_service_quota_template)
        """

    def get_requested_service_quota_change(
        self, **kwargs: Unpack[GetRequestedServiceQuotaChangeRequestTypeDef]
    ) -> GetRequestedServiceQuotaChangeResponseTypeDef:
        """
        Retrieves information about the specified quota increase request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_requested_service_quota_change.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_requested_service_quota_change)
        """

    def get_service_quota(
        self, **kwargs: Unpack[GetServiceQuotaRequestTypeDef]
    ) -> GetServiceQuotaResponseTypeDef:
        """
        Retrieves the applied quota value for the specified account-level or
        resource-level quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_service_quota.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_service_quota)
        """

    def get_service_quota_increase_request_from_template(
        self, **kwargs: Unpack[GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef]
    ) -> GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef:
        """
        Retrieves information about the specified quota increase request in your quota
        request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_service_quota_increase_request_from_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_service_quota_increase_request_from_template)
        """

    def list_aws_default_service_quotas(
        self, **kwargs: Unpack[ListAWSDefaultServiceQuotasRequestTypeDef]
    ) -> ListAWSDefaultServiceQuotasResponseTypeDef:
        """
        Lists the default values for the quotas for the specified Amazon Web Services
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_aws_default_service_quotas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_aws_default_service_quotas)
        """

    def list_requested_service_quota_change_history(
        self, **kwargs: Unpack[ListRequestedServiceQuotaChangeHistoryRequestTypeDef]
    ) -> ListRequestedServiceQuotaChangeHistoryResponseTypeDef:
        """
        Retrieves the quota increase requests for the specified Amazon Web Services
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_requested_service_quota_change_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_requested_service_quota_change_history)
        """

    def list_requested_service_quota_change_history_by_quota(
        self, **kwargs: Unpack[ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef]
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef:
        """
        Retrieves the quota increase requests for the specified quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_requested_service_quota_change_history_by_quota.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_requested_service_quota_change_history_by_quota)
        """

    def list_service_quota_increase_requests_in_template(
        self, **kwargs: Unpack[ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef]
    ) -> ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef:
        """
        Lists the quota increase requests in the specified quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_service_quota_increase_requests_in_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_service_quota_increase_requests_in_template)
        """

    def list_service_quotas(
        self, **kwargs: Unpack[ListServiceQuotasRequestTypeDef]
    ) -> ListServiceQuotasResponseTypeDef:
        """
        Lists the applied quota values for the specified Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_service_quotas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_service_quotas)
        """

    def list_services(
        self, **kwargs: Unpack[ListServicesRequestTypeDef]
    ) -> ListServicesResponseTypeDef:
        """
        Lists the names and codes for the Amazon Web Services services integrated with
        Service Quotas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_services)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified applied quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_tags_for_resource)
        """

    def put_service_quota_increase_request_into_template(
        self, **kwargs: Unpack[PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef]
    ) -> PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef:
        """
        Adds a quota increase request to your quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/put_service_quota_increase_request_into_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#put_service_quota_increase_request_into_template)
        """

    def request_service_quota_increase(
        self, **kwargs: Unpack[RequestServiceQuotaIncreaseRequestTypeDef]
    ) -> RequestServiceQuotaIncreaseResponseTypeDef:
        """
        Submits a quota increase request for the specified quota at the account or
        resource level.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/request_service_quota_increase.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#request_service_quota_increase)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to the specified applied quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified applied quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_aws_default_service_quotas"]
    ) -> ListAWSDefaultServiceQuotasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_requested_service_quota_change_history_by_quota"]
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_requested_service_quota_change_history"]
    ) -> ListRequestedServiceQuotaChangeHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_quota_increase_requests_in_template"]
    ) -> ListServiceQuotaIncreaseRequestsInTemplatePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_quotas"]
    ) -> ListServiceQuotasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_services"]
    ) -> ListServicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """
