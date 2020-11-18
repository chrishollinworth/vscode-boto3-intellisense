# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for route53domains service client

Usage::

    ```python
    import boto3
    from mypy_boto3_route53domains import Route53DomainsClient

    client: Route53DomainsClient = boto3.client("route53domains")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_route53domains.paginator import (
    ListDomainsPaginator,
    ListOperationsPaginator,
    ViewBillingPaginator,
)
from mypy_boto3_route53domains.type_defs import (
    AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef,
    CancelDomainTransferToAnotherAwsAccountResponseTypeDef,
    CheckDomainAvailabilityResponseTypeDef,
    CheckDomainTransferabilityResponseTypeDef,
    ContactDetailTypeDef,
    DisableDomainTransferLockResponseTypeDef,
    EnableDomainTransferLockResponseTypeDef,
    GetContactReachabilityStatusResponseTypeDef,
    GetDomainDetailResponseTypeDef,
    GetDomainSuggestionsResponseTypeDef,
    GetOperationDetailResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListTagsForDomainResponseTypeDef,
    NameserverTypeDef,
    RegisterDomainResponseTypeDef,
    RejectDomainTransferFromAnotherAwsAccountResponseTypeDef,
    RenewDomainResponseTypeDef,
    ResendContactReachabilityEmailResponseTypeDef,
    RetrieveDomainAuthCodeResponseTypeDef,
    TagTypeDef,
    TransferDomainResponseTypeDef,
    TransferDomainToAnotherAwsAccountResponseTypeDef,
    UpdateDomainContactPrivacyResponseTypeDef,
    UpdateDomainContactResponseTypeDef,
    UpdateDomainNameserversResponseTypeDef,
    ViewBillingResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53DomainsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DomainLimitExceeded: Type[BotocoreClientError]
    DuplicateRequest: Type[BotocoreClientError]
    InvalidInput: Type[BotocoreClientError]
    OperationLimitExceeded: Type[BotocoreClientError]
    TLDRulesViolation: Type[BotocoreClientError]
    UnsupportedTLD: Type[BotocoreClientError]


class Route53DomainsClient:
    """
    [Route53Domains.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_domain_transfer_from_another_aws_account(
        self, DomainName: str, Password: str
    ) -> AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef:
        """
        [Client.accept_domain_transfer_from_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.accept_domain_transfer_from_another_aws_account)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.can_paginate)
        """

    def cancel_domain_transfer_to_another_aws_account(
        self, DomainName: str
    ) -> CancelDomainTransferToAnotherAwsAccountResponseTypeDef:
        """
        [Client.cancel_domain_transfer_to_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.cancel_domain_transfer_to_another_aws_account)
        """

    def check_domain_availability(
        self, DomainName: str, IdnLangCode: str = None
    ) -> CheckDomainAvailabilityResponseTypeDef:
        """
        [Client.check_domain_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.check_domain_availability)
        """

    def check_domain_transferability(
        self, DomainName: str, AuthCode: str = None
    ) -> CheckDomainTransferabilityResponseTypeDef:
        """
        [Client.check_domain_transferability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.check_domain_transferability)
        """

    def delete_tags_for_domain(self, DomainName: str, TagsToDelete: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.delete_tags_for_domain)
        """

    def disable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        """
        [Client.disable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.disable_domain_auto_renew)
        """

    def disable_domain_transfer_lock(
        self, DomainName: str
    ) -> DisableDomainTransferLockResponseTypeDef:
        """
        [Client.disable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.disable_domain_transfer_lock)
        """

    def enable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        """
        [Client.enable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.enable_domain_auto_renew)
        """

    def enable_domain_transfer_lock(
        self, DomainName: str
    ) -> EnableDomainTransferLockResponseTypeDef:
        """
        [Client.enable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.enable_domain_transfer_lock)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.generate_presigned_url)
        """

    def get_contact_reachability_status(
        self, domainName: str = None
    ) -> GetContactReachabilityStatusResponseTypeDef:
        """
        [Client.get_contact_reachability_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.get_contact_reachability_status)
        """

    def get_domain_detail(self, DomainName: str) -> GetDomainDetailResponseTypeDef:
        """
        [Client.get_domain_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.get_domain_detail)
        """

    def get_domain_suggestions(
        self, DomainName: str, SuggestionCount: int, OnlyAvailable: bool
    ) -> GetDomainSuggestionsResponseTypeDef:
        """
        [Client.get_domain_suggestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.get_domain_suggestions)
        """

    def get_operation_detail(self, OperationId: str) -> GetOperationDetailResponseTypeDef:
        """
        [Client.get_operation_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.get_operation_detail)
        """

    def list_domains(self, Marker: str = None, MaxItems: int = None) -> ListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.list_domains)
        """

    def list_operations(
        self, SubmittedSince: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> ListOperationsResponseTypeDef:
        """
        [Client.list_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.list_operations)
        """

    def list_tags_for_domain(self, DomainName: str) -> ListTagsForDomainResponseTypeDef:
        """
        [Client.list_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.list_tags_for_domain)
        """

    def register_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: "ContactDetailTypeDef",
        RegistrantContact: "ContactDetailTypeDef",
        TechContact: "ContactDetailTypeDef",
        IdnLangCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> RegisterDomainResponseTypeDef:
        """
        [Client.register_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.register_domain)
        """

    def reject_domain_transfer_from_another_aws_account(
        self, DomainName: str
    ) -> RejectDomainTransferFromAnotherAwsAccountResponseTypeDef:
        """
        [Client.reject_domain_transfer_from_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.reject_domain_transfer_from_another_aws_account)
        """

    def renew_domain(
        self, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None
    ) -> RenewDomainResponseTypeDef:
        """
        [Client.renew_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.renew_domain)
        """

    def resend_contact_reachability_email(
        self, domainName: str = None
    ) -> ResendContactReachabilityEmailResponseTypeDef:
        """
        [Client.resend_contact_reachability_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.resend_contact_reachability_email)
        """

    def retrieve_domain_auth_code(self, DomainName: str) -> RetrieveDomainAuthCodeResponseTypeDef:
        """
        [Client.retrieve_domain_auth_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.retrieve_domain_auth_code)
        """

    def transfer_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: "ContactDetailTypeDef",
        RegistrantContact: "ContactDetailTypeDef",
        TechContact: "ContactDetailTypeDef",
        IdnLangCode: str = None,
        Nameservers: List["NameserverTypeDef"] = None,
        AuthCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> TransferDomainResponseTypeDef:
        """
        [Client.transfer_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.transfer_domain)
        """

    def transfer_domain_to_another_aws_account(
        self, DomainName: str, AccountId: str
    ) -> TransferDomainToAnotherAwsAccountResponseTypeDef:
        """
        [Client.transfer_domain_to_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.transfer_domain_to_another_aws_account)
        """

    def update_domain_contact(
        self,
        DomainName: str,
        AdminContact: "ContactDetailTypeDef" = None,
        RegistrantContact: "ContactDetailTypeDef" = None,
        TechContact: "ContactDetailTypeDef" = None,
    ) -> UpdateDomainContactResponseTypeDef:
        """
        [Client.update_domain_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact)
        """

    def update_domain_contact_privacy(
        self,
        DomainName: str,
        AdminPrivacy: bool = None,
        RegistrantPrivacy: bool = None,
        TechPrivacy: bool = None,
    ) -> UpdateDomainContactPrivacyResponseTypeDef:
        """
        [Client.update_domain_contact_privacy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact_privacy)
        """

    def update_domain_nameservers(
        self, DomainName: str, Nameservers: List["NameserverTypeDef"], FIAuthKey: str = None
    ) -> UpdateDomainNameserversResponseTypeDef:
        """
        [Client.update_domain_nameservers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.update_domain_nameservers)
        """

    def update_tags_for_domain(
        self, DomainName: str, TagsToUpdate: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Client.update_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.update_tags_for_domain)
        """

    def view_billing(
        self, Start: datetime = None, End: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> ViewBillingResponseTypeDef:
        """
        [Client.view_billing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Client.view_billing)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_operations"]) -> ListOperationsPaginator:
        """
        [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["view_billing"]) -> ViewBillingPaginator:
        """
        [Paginator.ViewBilling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)
        """
