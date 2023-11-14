"""
Type annotations for route53domains service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_route53domains import Route53DomainsClient

    client: Route53DomainsClient = boto3.client("route53domains")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import OperationStatusType, OperationTypeType, SortOrderType
from .paginator import (
    ListDomainsPaginator,
    ListOperationsPaginator,
    ListPricesPaginator,
    ViewBillingPaginator,
)
from .type_defs import (
    AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef,
    AssociateDelegationSignerToDomainResponseTypeDef,
    CancelDomainTransferToAnotherAwsAccountResponseTypeDef,
    CheckDomainAvailabilityResponseTypeDef,
    CheckDomainTransferabilityResponseTypeDef,
    ConsentTypeDef,
    ContactDetailTypeDef,
    DeleteDomainResponseTypeDef,
    DisableDomainTransferLockResponseTypeDef,
    DisassociateDelegationSignerFromDomainResponseTypeDef,
    DnssecSigningAttributesTypeDef,
    EnableDomainTransferLockResponseTypeDef,
    FilterConditionTypeDef,
    GetContactReachabilityStatusResponseTypeDef,
    GetDomainDetailResponseTypeDef,
    GetDomainSuggestionsResponseTypeDef,
    GetOperationDetailResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListPricesResponseTypeDef,
    ListTagsForDomainResponseTypeDef,
    NameserverTypeDef,
    RegisterDomainResponseTypeDef,
    RejectDomainTransferFromAnotherAwsAccountResponseTypeDef,
    RenewDomainResponseTypeDef,
    ResendContactReachabilityEmailResponseTypeDef,
    RetrieveDomainAuthCodeResponseTypeDef,
    SortConditionTypeDef,
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
    DnssecLimitExceeded: Type[BotocoreClientError]
    DomainLimitExceeded: Type[BotocoreClientError]
    DuplicateRequest: Type[BotocoreClientError]
    InvalidInput: Type[BotocoreClientError]
    OperationLimitExceeded: Type[BotocoreClientError]
    TLDRulesViolation: Type[BotocoreClientError]
    UnsupportedTLD: Type[BotocoreClientError]

class Route53DomainsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53DomainsClient exceptions.
        """
    def accept_domain_transfer_from_another_aws_account(
        self, *, DomainName: str, Password: str
    ) -> AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef:
        """
        Accepts the transfer of a domain from another Amazon Web Services account to the
        currentAmazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.accept_domain_transfer_from_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#accept_domain_transfer_from_another_aws_account)
        """
    def associate_delegation_signer_to_domain(
        self, *, DomainName: str, SigningAttributes: "DnssecSigningAttributesTypeDef"
    ) -> AssociateDelegationSignerToDomainResponseTypeDef:
        """
        Creates a delegation signer (DS) record in the registry zone for this domain
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.associate_delegation_signer_to_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#associate_delegation_signer_to_domain)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#can_paginate)
        """
    def cancel_domain_transfer_to_another_aws_account(
        self, *, DomainName: str
    ) -> CancelDomainTransferToAnotherAwsAccountResponseTypeDef:
        """
        Cancels the transfer of a domain from the current Amazon Web Services account to
        another Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.cancel_domain_transfer_to_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#cancel_domain_transfer_to_another_aws_account)
        """
    def check_domain_availability(
        self, *, DomainName: str, IdnLangCode: str = None
    ) -> CheckDomainAvailabilityResponseTypeDef:
        """
        This operation checks the availability of one domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.check_domain_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#check_domain_availability)
        """
    def check_domain_transferability(
        self, *, DomainName: str, AuthCode: str = None
    ) -> CheckDomainTransferabilityResponseTypeDef:
        """
        Checks whether a domain name can be transferred to Amazon Route 53.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.check_domain_transferability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#check_domain_transferability)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#close)
        """
    def delete_domain(self, *, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        This operation deletes the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#delete_domain)
        """
    def delete_tags_for_domain(self, *, DomainName: str, TagsToDelete: List[str]) -> Dict[str, Any]:
        """
        This operation deletes the specified tags for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.delete_tags_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#delete_tags_for_domain)
        """
    def disable_domain_auto_renew(self, *, DomainName: str) -> Dict[str, Any]:
        """
        This operation disables automatic renewal of domain registration for the
        specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.disable_domain_auto_renew)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#disable_domain_auto_renew)
        """
    def disable_domain_transfer_lock(
        self, *, DomainName: str
    ) -> DisableDomainTransferLockResponseTypeDef:
        """
        This operation removes the transfer lock on the domain (specifically the
        `clientTransferProhibited` status) to allow domain transfers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.disable_domain_transfer_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#disable_domain_transfer_lock)
        """
    def disassociate_delegation_signer_from_domain(
        self, *, DomainName: str, Id: str
    ) -> DisassociateDelegationSignerFromDomainResponseTypeDef:
        """
        Deletes a delegation signer (DS) record in the registry zone for this domain
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.disassociate_delegation_signer_from_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#disassociate_delegation_signer_from_domain)
        """
    def enable_domain_auto_renew(self, *, DomainName: str) -> Dict[str, Any]:
        """
        This operation configures Amazon Route 53 to automatically renew the specified
        domain before the domain registration expires.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.enable_domain_auto_renew)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#enable_domain_auto_renew)
        """
    def enable_domain_transfer_lock(
        self, *, DomainName: str
    ) -> EnableDomainTransferLockResponseTypeDef:
        """
        This operation sets the transfer lock on the domain (specifically the
        `clientTransferProhibited` status) to prevent domain transfers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.enable_domain_transfer_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#enable_domain_transfer_lock)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#generate_presigned_url)
        """
    def get_contact_reachability_status(
        self, *, domainName: str = None
    ) -> GetContactReachabilityStatusResponseTypeDef:
        """
        For operations that require confirmation that the email address for the
        registrant contact is valid, such as registering a new domain, this operation
        returns information about whether the registrant contact has responded.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.get_contact_reachability_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_contact_reachability_status)
        """
    def get_domain_detail(self, *, DomainName: str) -> GetDomainDetailResponseTypeDef:
        """
        This operation returns detailed information about a specified domain that is
        associated with the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.get_domain_detail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_domain_detail)
        """
    def get_domain_suggestions(
        self, *, DomainName: str, SuggestionCount: int, OnlyAvailable: bool
    ) -> GetDomainSuggestionsResponseTypeDef:
        """
        The GetDomainSuggestions operation returns a list of suggested domain names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.get_domain_suggestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_domain_suggestions)
        """
    def get_operation_detail(self, *, OperationId: str) -> GetOperationDetailResponseTypeDef:
        """
        This operation returns the current status of an operation that is not completed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.get_operation_detail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_operation_detail)
        """
    def list_domains(
        self,
        *,
        FilterConditions: List["FilterConditionTypeDef"] = None,
        SortCondition: "SortConditionTypeDef" = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        This operation returns all the domain names registered with Amazon Route 53 for
        the current Amazon Web Services account if no filtering conditions are used.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#list_domains)
        """
    def list_operations(
        self,
        *,
        SubmittedSince: Union[datetime, str] = None,
        Marker: str = None,
        MaxItems: int = None,
        Status: List[OperationStatusType] = None,
        Type: List[OperationTypeType] = None,
        SortBy: Literal["SubmittedDate"] = None,
        SortOrder: SortOrderType = None
    ) -> ListOperationsResponseTypeDef:
        """
        Returns information about all of the operations that return an operation ID and
        that have ever been performed on domains that were registered by the current
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.list_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#list_operations)
        """
    def list_prices(
        self, *, Tld: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListPricesResponseTypeDef:
        """
        Lists the following prices for either all the TLDs supported by Route 53, or the
        specified TLD * Registration * Transfer * Owner change * Domain renewal * Domain
        restoration See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ListP...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.list_prices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#list_prices)
        """
    def list_tags_for_domain(self, *, DomainName: str) -> ListTagsForDomainResponseTypeDef:
        """
        This operation returns all of the tags that are associated with the specified
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.list_tags_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#list_tags_for_domain)
        """
    def push_domain(self, *, DomainName: str, Target: str) -> None:
        """
        Moves a domain from Amazon Web Services to another registrar.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.push_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#push_domain)
        """
    def register_domain(
        self,
        *,
        DomainName: str,
        DurationInYears: int,
        AdminContact: "ContactDetailTypeDef",
        RegistrantContact: "ContactDetailTypeDef",
        TechContact: "ContactDetailTypeDef",
        IdnLangCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None
    ) -> RegisterDomainResponseTypeDef:
        """
        This operation registers a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.register_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#register_domain)
        """
    def reject_domain_transfer_from_another_aws_account(
        self, *, DomainName: str
    ) -> RejectDomainTransferFromAnotherAwsAccountResponseTypeDef:
        """
        Rejects the transfer of a domain from another Amazon Web Services account to the
        current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.reject_domain_transfer_from_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#reject_domain_transfer_from_another_aws_account)
        """
    def renew_domain(
        self, *, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None
    ) -> RenewDomainResponseTypeDef:
        """
        This operation renews a domain for the specified number of years.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.renew_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#renew_domain)
        """
    def resend_contact_reachability_email(
        self, *, domainName: str = None
    ) -> ResendContactReachabilityEmailResponseTypeDef:
        """
        For operations that require confirmation that the email address for the
        registrant contact is valid, such as registering a new domain, this operation
        resends the confirmation email to the current email address for the registrant
        contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.resend_contact_reachability_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#resend_contact_reachability_email)
        """
    def resend_operation_authorization(self, *, OperationId: str) -> None:
        """
        Resend the form of authorization email for this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.resend_operation_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#resend_operation_authorization)
        """
    def retrieve_domain_auth_code(
        self, *, DomainName: str
    ) -> RetrieveDomainAuthCodeResponseTypeDef:
        """
        This operation returns the authorization code for the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.retrieve_domain_auth_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#retrieve_domain_auth_code)
        """
    def transfer_domain(
        self,
        *,
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
        PrivacyProtectTechContact: bool = None
    ) -> TransferDomainResponseTypeDef:
        """
        Transfers a domain from another registrar to Amazon Route 53.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.transfer_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#transfer_domain)
        """
    def transfer_domain_to_another_aws_account(
        self, *, DomainName: str, AccountId: str
    ) -> TransferDomainToAnotherAwsAccountResponseTypeDef:
        """
        Transfers a domain from the current Amazon Web Services account to another
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.transfer_domain_to_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#transfer_domain_to_another_aws_account)
        """
    def update_domain_contact(
        self,
        *,
        DomainName: str,
        AdminContact: "ContactDetailTypeDef" = None,
        RegistrantContact: "ContactDetailTypeDef" = None,
        TechContact: "ContactDetailTypeDef" = None,
        Consent: "ConsentTypeDef" = None
    ) -> UpdateDomainContactResponseTypeDef:
        """
        This operation updates the contact information for a particular domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_domain_contact)
        """
    def update_domain_contact_privacy(
        self,
        *,
        DomainName: str,
        AdminPrivacy: bool = None,
        RegistrantPrivacy: bool = None,
        TechPrivacy: bool = None
    ) -> UpdateDomainContactPrivacyResponseTypeDef:
        """
        This operation updates the specified domain contact's privacy setting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact_privacy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_domain_contact_privacy)
        """
    def update_domain_nameservers(
        self, *, DomainName: str, Nameservers: List["NameserverTypeDef"], FIAuthKey: str = None
    ) -> UpdateDomainNameserversResponseTypeDef:
        """
        This operation replaces the current set of name servers for the domain with the
        specified set of name servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.update_domain_nameservers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_domain_nameservers)
        """
    def update_tags_for_domain(
        self, *, DomainName: str, TagsToUpdate: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        This operation adds or updates tags for a specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.update_tags_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_tags_for_domain)
        """
    def view_billing(
        self,
        *,
        Start: Union[datetime, str] = None,
        End: Union[datetime, str] = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ViewBillingResponseTypeDef:
        """
        Returns all the domain-related billing records for the current Amazon Web
        Services account for a specified period See also: `AWS API Documentation <https:
        //docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ViewBilling>`_
        **Request Syntax** response = client.view_billing( ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Client.view_billing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#view_billing)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listdomainspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_operations"]) -> ListOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listoperationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_prices"]) -> ListPricesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Paginator.ListPrices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listpricespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["view_billing"]) -> ViewBillingPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#viewbillingpaginator)
        """
