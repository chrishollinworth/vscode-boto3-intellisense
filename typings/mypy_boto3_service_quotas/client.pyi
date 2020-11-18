# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for service-quotas service client

Usage::

    ```python
    import boto3
    from mypy_boto3_service_quotas import ServiceQuotasClient

    client: ServiceQuotasClient = boto3.client("service-quotas")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_service_quotas.paginator import (
    ListAWSDefaultServiceQuotasPaginator,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
    ListRequestedServiceQuotaChangeHistoryPaginator,
    ListServiceQuotaIncreaseRequestsInTemplatePaginator,
    ListServiceQuotasPaginator,
    ListServicesPaginator,
)
from mypy_boto3_service_quotas.type_defs import (
    GetAssociationForServiceQuotaTemplateResponseTypeDef,
    GetAWSDefaultServiceQuotaResponseTypeDef,
    GetRequestedServiceQuotaChangeResponseTypeDef,
    GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef,
    GetServiceQuotaResponseTypeDef,
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesResponseTypeDef,
    PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef,
    RequestServiceQuotaIncreaseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceQuotasClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
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
    TemplatesNotAvailableInRegionException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class ServiceQuotasClient:
    """
    [ServiceQuotas.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_service_quota_template(self) -> Dict[str, Any]:
        """
        [Client.associate_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.associate_service_quota_template)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.can_paginate)
        """

    def delete_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_service_quota_increase_request_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.delete_service_quota_increase_request_from_template)
        """

    def disassociate_service_quota_template(self) -> Dict[str, Any]:
        """
        [Client.disassociate_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.disassociate_service_quota_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.generate_presigned_url)
        """

    def get_association_for_service_quota_template(
        self,
    ) -> GetAssociationForServiceQuotaTemplateResponseTypeDef:
        """
        [Client.get_association_for_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.get_association_for_service_quota_template)
        """

    def get_aws_default_service_quota(
        self, ServiceCode: str, QuotaCode: str
    ) -> GetAWSDefaultServiceQuotaResponseTypeDef:
        """
        [Client.get_aws_default_service_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.get_aws_default_service_quota)
        """

    def get_requested_service_quota_change(
        self, RequestId: str
    ) -> GetRequestedServiceQuotaChangeResponseTypeDef:
        """
        [Client.get_requested_service_quota_change documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.get_requested_service_quota_change)
        """

    def get_service_quota(self, ServiceCode: str, QuotaCode: str) -> GetServiceQuotaResponseTypeDef:
        """
        [Client.get_service_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota)
        """

    def get_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef:
        """
        [Client.get_service_quota_increase_request_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota_increase_request_from_template)
        """

    def list_aws_default_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAWSDefaultServiceQuotasResponseTypeDef:
        """
        [Client.list_aws_default_service_quotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.list_aws_default_service_quotas)
        """

    def list_requested_service_quota_change_history(
        self,
        ServiceCode: str = None,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListRequestedServiceQuotaChangeHistoryResponseTypeDef:
        """
        [Client.list_requested_service_quota_change_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history)
        """

    def list_requested_service_quota_change_history_by_quota(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef:
        """
        [Client.list_requested_service_quota_change_history_by_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history_by_quota)
        """

    def list_service_quota_increase_requests_in_template(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef:
        """
        [Client.list_service_quota_increase_requests_in_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quota_increase_requests_in_template)
        """

    def list_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ListServiceQuotasResponseTypeDef:
        """
        [Client.list_service_quotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quotas)
        """

    def list_services(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListServicesResponseTypeDef:
        """
        [Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.list_services)
        """

    def put_service_quota_increase_request_into_template(
        self, QuotaCode: str, ServiceCode: str, AwsRegion: str, DesiredValue: float
    ) -> PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef:
        """
        [Client.put_service_quota_increase_request_into_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.put_service_quota_increase_request_into_template)
        """

    def request_service_quota_increase(
        self, ServiceCode: str, QuotaCode: str, DesiredValue: float
    ) -> RequestServiceQuotaIncreaseResponseTypeDef:
        """
        [Client.request_service_quota_increase documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Client.request_service_quota_increase)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aws_default_service_quotas"]
    ) -> ListAWSDefaultServiceQuotasPaginator:
        """
        [Paginator.ListAWSDefaultServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_requested_service_quota_change_history"]
    ) -> ListRequestedServiceQuotaChangeHistoryPaginator:
        """
        [Paginator.ListRequestedServiceQuotaChangeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_requested_service_quota_change_history_by_quota"]
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
        """
        [Paginator.ListRequestedServiceQuotaChangeHistoryByQuota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_quota_increase_requests_in_template"]
    ) -> ListServiceQuotaIncreaseRequestsInTemplatePaginator:
        """
        [Paginator.ListServiceQuotaIncreaseRequestsInTemplate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_quotas"]
    ) -> ListServiceQuotasPaginator:
        """
        [Paginator.ListServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices)
        """
