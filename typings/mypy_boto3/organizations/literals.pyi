"""
Type annotations for organizations service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/literals.html)

Usage::

    ```python
    from mypy_boto3_organizations.literals import AccountJoinedMethodType

    data: AccountJoinedMethodType = "CREATED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountJoinedMethodType",
    "AccountStatusType",
    "ActionTypeType",
    "ChildTypeType",
    "CreateAccountFailureReasonType",
    "CreateAccountStateType",
    "EffectivePolicyTypeType",
    "HandshakePartyTypeType",
    "HandshakeResourceTypeType",
    "HandshakeStateType",
    "IAMUserAccessToBillingType",
    "ListAWSServiceAccessForOrganizationPaginatorName",
    "ListAccountsForParentPaginatorName",
    "ListAccountsPaginatorName",
    "ListChildrenPaginatorName",
    "ListCreateAccountStatusPaginatorName",
    "ListDelegatedAdministratorsPaginatorName",
    "ListDelegatedServicesForAccountPaginatorName",
    "ListHandshakesForAccountPaginatorName",
    "ListHandshakesForOrganizationPaginatorName",
    "ListOrganizationalUnitsForParentPaginatorName",
    "ListParentsPaginatorName",
    "ListPoliciesForTargetPaginatorName",
    "ListPoliciesPaginatorName",
    "ListRootsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTargetsForPolicyPaginatorName",
    "OrganizationFeatureSetType",
    "ParentTypeType",
    "PolicyTypeStatusType",
    "PolicyTypeType",
    "TargetTypeType",
)

AccountJoinedMethodType = Literal["CREATED", "INVITED"]
AccountStatusType = Literal["ACTIVE", "SUSPENDED"]
ActionTypeType = Literal[
    "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE", "APPROVE_ALL_FEATURES", "ENABLE_ALL_FEATURES", "INVITE"
]
ChildTypeType = Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]
CreateAccountFailureReasonType = Literal[
    "ACCOUNT_LIMIT_EXCEEDED",
    "CONCURRENT_ACCOUNT_MODIFICATION",
    "EMAIL_ALREADY_EXISTS",
    "FAILED_BUSINESS_VALIDATION",
    "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
    "INTERNAL_FAILURE",
    "INVALID_ADDRESS",
    "INVALID_EMAIL",
    "INVALID_IDENTITY_FOR_BUSINESS_VALIDATION",
    "MISSING_BUSINESS_VALIDATION",
    "MISSING_PAYMENT_INSTRUMENT",
    "PENDING_BUSINESS_VALIDATION",
    "UNKNOWN_BUSINESS_VALIDATION",
]
CreateAccountStateType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
EffectivePolicyTypeType = Literal["AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "TAG_POLICY"]
HandshakePartyTypeType = Literal["ACCOUNT", "EMAIL", "ORGANIZATION"]
HandshakeResourceTypeType = Literal[
    "ACCOUNT",
    "EMAIL",
    "MASTER_EMAIL",
    "MASTER_NAME",
    "NOTES",
    "ORGANIZATION",
    "ORGANIZATION_FEATURE_SET",
    "PARENT_HANDSHAKE",
]
HandshakeStateType = Literal["ACCEPTED", "CANCELED", "DECLINED", "EXPIRED", "OPEN", "REQUESTED"]
IAMUserAccessToBillingType = Literal["ALLOW", "DENY"]
ListAWSServiceAccessForOrganizationPaginatorName = Literal[
    "list_aws_service_access_for_organization"
]
ListAccountsForParentPaginatorName = Literal["list_accounts_for_parent"]
ListAccountsPaginatorName = Literal["list_accounts"]
ListChildrenPaginatorName = Literal["list_children"]
ListCreateAccountStatusPaginatorName = Literal["list_create_account_status"]
ListDelegatedAdministratorsPaginatorName = Literal["list_delegated_administrators"]
ListDelegatedServicesForAccountPaginatorName = Literal["list_delegated_services_for_account"]
ListHandshakesForAccountPaginatorName = Literal["list_handshakes_for_account"]
ListHandshakesForOrganizationPaginatorName = Literal["list_handshakes_for_organization"]
ListOrganizationalUnitsForParentPaginatorName = Literal["list_organizational_units_for_parent"]
ListParentsPaginatorName = Literal["list_parents"]
ListPoliciesForTargetPaginatorName = Literal["list_policies_for_target"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListRootsPaginatorName = Literal["list_roots"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTargetsForPolicyPaginatorName = Literal["list_targets_for_policy"]
OrganizationFeatureSetType = Literal["ALL", "CONSOLIDATED_BILLING"]
ParentTypeType = Literal["ORGANIZATIONAL_UNIT", "ROOT"]
PolicyTypeStatusType = Literal["ENABLED", "PENDING_DISABLE", "PENDING_ENABLE"]
PolicyTypeType = Literal[
    "AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "SERVICE_CONTROL_POLICY", "TAG_POLICY"
]
TargetTypeType = Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"]
