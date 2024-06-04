"""
Type annotations for sso-admin service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_admin.type_defs import AccessControlAttributeTypeDef

    data: AccessControlAttributeTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ApplicationStatusType,
    ApplicationVisibilityType,
    FederationProtocolType,
    GrantTypeType,
    InstanceAccessControlAttributeConfigurationStatusType,
    InstanceStatusType,
    PrincipalTypeType,
    ProvisioningStatusType,
    ProvisionTargetTypeType,
    SignInOriginType,
    StatusValuesType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessControlAttributeTypeDef",
    "AccessControlAttributeValueTypeDef",
    "AccountAssignmentForPrincipalTypeDef",
    "AccountAssignmentOperationStatusMetadataTypeDef",
    "AccountAssignmentOperationStatusTypeDef",
    "AccountAssignmentTypeDef",
    "ApplicationAssignmentForPrincipalTypeDef",
    "ApplicationAssignmentTypeDef",
    "ApplicationProviderTypeDef",
    "ApplicationTypeDef",
    "AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef",
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    "AttachedManagedPolicyTypeDef",
    "AuthenticationMethodItemTypeDef",
    "AuthenticationMethodTypeDef",
    "AuthorizationCodeGrantTypeDef",
    "AuthorizedTokenIssuerTypeDef",
    "CreateAccountAssignmentRequestRequestTypeDef",
    "CreateAccountAssignmentResponseTypeDef",
    "CreateApplicationAssignmentRequestRequestTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreatePermissionSetRequestRequestTypeDef",
    "CreatePermissionSetResponseTypeDef",
    "CreateTrustedTokenIssuerRequestRequestTypeDef",
    "CreateTrustedTokenIssuerResponseTypeDef",
    "CustomerManagedPolicyReferenceTypeDef",
    "DeleteAccountAssignmentRequestRequestTypeDef",
    "DeleteAccountAssignmentResponseTypeDef",
    "DeleteApplicationAccessScopeRequestRequestTypeDef",
    "DeleteApplicationAssignmentRequestRequestTypeDef",
    "DeleteApplicationAuthenticationMethodRequestRequestTypeDef",
    "DeleteApplicationGrantRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeletePermissionSetRequestRequestTypeDef",
    "DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef",
    "DeleteTrustedTokenIssuerRequestRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    "DescribeApplicationAssignmentRequestRequestTypeDef",
    "DescribeApplicationAssignmentResponseTypeDef",
    "DescribeApplicationProviderRequestRequestTypeDef",
    "DescribeApplicationProviderResponseTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    "DescribeInstanceRequestRequestTypeDef",
    "DescribeInstanceResponseTypeDef",
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    "DescribePermissionSetRequestRequestTypeDef",
    "DescribePermissionSetResponseTypeDef",
    "DescribeTrustedTokenIssuerRequestRequestTypeDef",
    "DescribeTrustedTokenIssuerResponseTypeDef",
    "DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef",
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    "DisplayDataTypeDef",
    "GetApplicationAccessScopeRequestRequestTypeDef",
    "GetApplicationAccessScopeResponseTypeDef",
    "GetApplicationAssignmentConfigurationRequestRequestTypeDef",
    "GetApplicationAssignmentConfigurationResponseTypeDef",
    "GetApplicationAuthenticationMethodRequestRequestTypeDef",
    "GetApplicationAuthenticationMethodResponseTypeDef",
    "GetApplicationGrantRequestRequestTypeDef",
    "GetApplicationGrantResponseTypeDef",
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    "GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef",
    "GetPermissionsBoundaryForPermissionSetResponseTypeDef",
    "GrantItemTypeDef",
    "GrantTypeDef",
    "IamAuthenticationMethodTypeDef",
    "InstanceAccessControlAttributeConfigurationTypeDef",
    "InstanceMetadataTypeDef",
    "JwtBearerGrantTypeDef",
    "ListAccountAssignmentCreationStatusRequestRequestTypeDef",
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    "ListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    "ListAccountAssignmentsFilterTypeDef",
    "ListAccountAssignmentsForPrincipalRequestRequestTypeDef",
    "ListAccountAssignmentsForPrincipalResponseTypeDef",
    "ListAccountAssignmentsRequestRequestTypeDef",
    "ListAccountAssignmentsResponseTypeDef",
    "ListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    "ListApplicationAccessScopesRequestRequestTypeDef",
    "ListApplicationAccessScopesResponseTypeDef",
    "ListApplicationAssignmentsFilterTypeDef",
    "ListApplicationAssignmentsForPrincipalRequestRequestTypeDef",
    "ListApplicationAssignmentsForPrincipalResponseTypeDef",
    "ListApplicationAssignmentsRequestRequestTypeDef",
    "ListApplicationAssignmentsResponseTypeDef",
    "ListApplicationAuthenticationMethodsRequestRequestTypeDef",
    "ListApplicationAuthenticationMethodsResponseTypeDef",
    "ListApplicationGrantsRequestRequestTypeDef",
    "ListApplicationGrantsResponseTypeDef",
    "ListApplicationProvidersRequestRequestTypeDef",
    "ListApplicationProvidersResponseTypeDef",
    "ListApplicationsFilterTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    "ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    "ListPermissionSetProvisioningStatusRequestRequestTypeDef",
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    "ListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    "ListPermissionSetsRequestRequestTypeDef",
    "ListPermissionSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustedTokenIssuersRequestRequestTypeDef",
    "ListTrustedTokenIssuersResponseTypeDef",
    "OidcJwtConfigurationTypeDef",
    "OidcJwtUpdateConfigurationTypeDef",
    "OperationStatusFilterTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionSetProvisioningStatusMetadataTypeDef",
    "PermissionSetProvisioningStatusTypeDef",
    "PermissionSetTypeDef",
    "PermissionsBoundaryTypeDef",
    "PortalOptionsTypeDef",
    "ProvisionPermissionSetRequestRequestTypeDef",
    "ProvisionPermissionSetResponseTypeDef",
    "PutApplicationAccessScopeRequestRequestTypeDef",
    "PutApplicationAssignmentConfigurationRequestRequestTypeDef",
    "PutApplicationAuthenticationMethodRequestRequestTypeDef",
    "PutApplicationGrantRequestRequestTypeDef",
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    "PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef",
    "ResourceServerConfigTypeDef",
    "ResourceServerScopeDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "ScopeDetailsTypeDef",
    "SignInOptionsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrustedTokenIssuerConfigurationTypeDef",
    "TrustedTokenIssuerMetadataTypeDef",
    "TrustedTokenIssuerUpdateConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationPortalOptionsTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "UpdateInstanceRequestRequestTypeDef",
    "UpdatePermissionSetRequestRequestTypeDef",
    "UpdateTrustedTokenIssuerRequestRequestTypeDef",
)

AccessControlAttributeTypeDef = TypedDict(
    "AccessControlAttributeTypeDef",
    {
        "Key": str,
        "Value": "AccessControlAttributeValueTypeDef",
    },
)

AccessControlAttributeValueTypeDef = TypedDict(
    "AccessControlAttributeValueTypeDef",
    {
        "Source": List[str],
    },
)

AccountAssignmentForPrincipalTypeDef = TypedDict(
    "AccountAssignmentForPrincipalTypeDef",
    {
        "AccountId": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
    total=False,
)

AccountAssignmentOperationStatusMetadataTypeDef = TypedDict(
    "AccountAssignmentOperationStatusMetadataTypeDef",
    {
        "CreatedDate": datetime,
        "RequestId": str,
        "Status": StatusValuesType,
    },
    total=False,
)

AccountAssignmentOperationStatusTypeDef = TypedDict(
    "AccountAssignmentOperationStatusTypeDef",
    {
        "CreatedDate": datetime,
        "FailureReason": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "RequestId": str,
        "Status": StatusValuesType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
    },
    total=False,
)

AccountAssignmentTypeDef = TypedDict(
    "AccountAssignmentTypeDef",
    {
        "AccountId": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
    total=False,
)

ApplicationAssignmentForPrincipalTypeDef = TypedDict(
    "ApplicationAssignmentForPrincipalTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
    total=False,
)

ApplicationAssignmentTypeDef = TypedDict(
    "ApplicationAssignmentTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)

_RequiredApplicationProviderTypeDef = TypedDict(
    "_RequiredApplicationProviderTypeDef",
    {
        "ApplicationProviderArn": str,
    },
)
_OptionalApplicationProviderTypeDef = TypedDict(
    "_OptionalApplicationProviderTypeDef",
    {
        "DisplayData": "DisplayDataTypeDef",
        "FederationProtocol": FederationProtocolType,
        "ResourceServerConfig": "ResourceServerConfigTypeDef",
    },
    total=False,
)

class ApplicationProviderTypeDef(
    _RequiredApplicationProviderTypeDef, _OptionalApplicationProviderTypeDef
):
    pass

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "ApplicationAccount": str,
        "ApplicationArn": str,
        "ApplicationProviderArn": str,
        "CreatedDate": datetime,
        "Description": str,
        "InstanceArn": str,
        "Name": str,
        "PortalOptions": "PortalOptionsTypeDef",
        "Status": ApplicationStatusType,
    },
    total=False,
)

AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef",
    {
        "CustomerManagedPolicyReference": "CustomerManagedPolicyReferenceTypeDef",
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

AttachManagedPolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ManagedPolicyArn": str,
        "PermissionSetArn": str,
    },
)

AttachedManagedPolicyTypeDef = TypedDict(
    "AttachedManagedPolicyTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

AuthenticationMethodItemTypeDef = TypedDict(
    "AuthenticationMethodItemTypeDef",
    {
        "AuthenticationMethod": "AuthenticationMethodTypeDef",
        "AuthenticationMethodType": Literal["IAM"],
    },
    total=False,
)

AuthenticationMethodTypeDef = TypedDict(
    "AuthenticationMethodTypeDef",
    {
        "Iam": "IamAuthenticationMethodTypeDef",
    },
    total=False,
)

AuthorizationCodeGrantTypeDef = TypedDict(
    "AuthorizationCodeGrantTypeDef",
    {
        "RedirectUris": List[str],
    },
    total=False,
)

AuthorizedTokenIssuerTypeDef = TypedDict(
    "AuthorizedTokenIssuerTypeDef",
    {
        "AuthorizedAudiences": List[str],
        "TrustedTokenIssuerArn": str,
    },
    total=False,
)

CreateAccountAssignmentRequestRequestTypeDef = TypedDict(
    "CreateAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
    },
)

CreateAccountAssignmentResponseTypeDef = TypedDict(
    "CreateAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApplicationAssignmentRequestRequestTypeDef = TypedDict(
    "CreateApplicationAssignmentRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "ApplicationProviderArn": str,
        "InstanceArn": str,
        "Name": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "PortalOptions": "PortalOptionsTypeDef",
        "Status": ApplicationStatusType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
        "InstanceArn": str,
    },
)

CreateInstanceRequestRequestTypeDef = TypedDict(
    "CreateInstanceRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateInstanceResponseTypeDef = TypedDict(
    "CreateInstanceResponseTypeDef",
    {
        "InstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Name": str,
    },
)
_OptionalCreatePermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionSetRequestRequestTypeDef",
    {
        "Description": str,
        "RelayState": str,
        "SessionDuration": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePermissionSetRequestRequestTypeDef(
    _RequiredCreatePermissionSetRequestRequestTypeDef,
    _OptionalCreatePermissionSetRequestRequestTypeDef,
):
    pass

CreatePermissionSetResponseTypeDef = TypedDict(
    "CreatePermissionSetResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrustedTokenIssuerRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Name": str,
        "TrustedTokenIssuerConfiguration": "TrustedTokenIssuerConfigurationTypeDef",
        "TrustedTokenIssuerType": Literal["OIDC_JWT"],
    },
)
_OptionalCreateTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrustedTokenIssuerRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrustedTokenIssuerRequestRequestTypeDef(
    _RequiredCreateTrustedTokenIssuerRequestRequestTypeDef,
    _OptionalCreateTrustedTokenIssuerRequestRequestTypeDef,
):
    pass

CreateTrustedTokenIssuerResponseTypeDef = TypedDict(
    "CreateTrustedTokenIssuerResponseTypeDef",
    {
        "TrustedTokenIssuerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomerManagedPolicyReferenceTypeDef = TypedDict(
    "_RequiredCustomerManagedPolicyReferenceTypeDef",
    {
        "Name": str,
    },
)
_OptionalCustomerManagedPolicyReferenceTypeDef = TypedDict(
    "_OptionalCustomerManagedPolicyReferenceTypeDef",
    {
        "Path": str,
    },
    total=False,
)

class CustomerManagedPolicyReferenceTypeDef(
    _RequiredCustomerManagedPolicyReferenceTypeDef, _OptionalCustomerManagedPolicyReferenceTypeDef
):
    pass

DeleteAccountAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
    },
)

DeleteAccountAssignmentResponseTypeDef = TypedDict(
    "DeleteAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationAccessScopeRequestRequestTypeDef = TypedDict(
    "DeleteApplicationAccessScopeRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Scope": str,
    },
)

DeleteApplicationAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteApplicationAssignmentRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)

DeleteApplicationAuthenticationMethodRequestRequestTypeDef = TypedDict(
    "DeleteApplicationAuthenticationMethodRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AuthenticationMethodType": Literal["IAM"],
    },
)

DeleteApplicationGrantRequestRequestTypeDef = TypedDict(
    "DeleteApplicationGrantRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "GrantType": GrantTypeType,
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)

DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DeletePermissionSetRequestRequestTypeDef = TypedDict(
    "DeletePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DeleteTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "DeleteTrustedTokenIssuerRequestRequestTypeDef",
    {
        "TrustedTokenIssuerArn": str,
    },
)

DescribeAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "AccountAssignmentCreationRequestId": str,
        "InstanceArn": str,
    },
)

DescribeAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "AccountAssignmentDeletionRequestId": str,
        "InstanceArn": str,
    },
)

DescribeAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationAssignmentRequestRequestTypeDef = TypedDict(
    "DescribeApplicationAssignmentRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)

DescribeApplicationAssignmentResponseTypeDef = TypedDict(
    "DescribeApplicationAssignmentResponseTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationProviderRequestRequestTypeDef = TypedDict(
    "DescribeApplicationProviderRequestRequestTypeDef",
    {
        "ApplicationProviderArn": str,
    },
)

DescribeApplicationProviderResponseTypeDef = TypedDict(
    "DescribeApplicationProviderResponseTypeDef",
    {
        "ApplicationProviderArn": str,
        "DisplayData": "DisplayDataTypeDef",
        "FederationProtocol": FederationProtocolType,
        "ResourceServerConfig": "ResourceServerConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationAccount": str,
        "ApplicationArn": str,
        "ApplicationProviderArn": str,
        "CreatedDate": datetime,
        "Description": str,
        "InstanceArn": str,
        "Name": str,
        "PortalOptions": "PortalOptionsTypeDef",
        "Status": ApplicationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
        "Status": InstanceAccessControlAttributeConfigurationStatusType,
        "StatusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRequestRequestTypeDef = TypedDict(
    "DescribeInstanceRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DescribeInstanceResponseTypeDef = TypedDict(
    "DescribeInstanceResponseTypeDef",
    {
        "CreatedDate": datetime,
        "IdentityStoreId": str,
        "InstanceArn": str,
        "Name": str,
        "OwnerAccountId": str,
        "Status": InstanceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ProvisionPermissionSetRequestId": str,
    },
)

DescribePermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DescribePermissionSetResponseTypeDef = TypedDict(
    "DescribePermissionSetResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "DescribeTrustedTokenIssuerRequestRequestTypeDef",
    {
        "TrustedTokenIssuerArn": str,
    },
)

DescribeTrustedTokenIssuerResponseTypeDef = TypedDict(
    "DescribeTrustedTokenIssuerResponseTypeDef",
    {
        "Name": str,
        "TrustedTokenIssuerArn": str,
        "TrustedTokenIssuerConfiguration": "TrustedTokenIssuerConfigurationTypeDef",
        "TrustedTokenIssuerType": Literal["OIDC_JWT"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef",
    {
        "CustomerManagedPolicyReference": "CustomerManagedPolicyReferenceTypeDef",
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DetachManagedPolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ManagedPolicyArn": str,
        "PermissionSetArn": str,
    },
)

DisplayDataTypeDef = TypedDict(
    "DisplayDataTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "IconUrl": str,
    },
    total=False,
)

GetApplicationAccessScopeRequestRequestTypeDef = TypedDict(
    "GetApplicationAccessScopeRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Scope": str,
    },
)

GetApplicationAccessScopeResponseTypeDef = TypedDict(
    "GetApplicationAccessScopeResponseTypeDef",
    {
        "AuthorizedTargets": List[str],
        "Scope": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationAssignmentConfigurationRequestRequestTypeDef = TypedDict(
    "GetApplicationAssignmentConfigurationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)

GetApplicationAssignmentConfigurationResponseTypeDef = TypedDict(
    "GetApplicationAssignmentConfigurationResponseTypeDef",
    {
        "AssignmentRequired": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationAuthenticationMethodRequestRequestTypeDef = TypedDict(
    "GetApplicationAuthenticationMethodRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AuthenticationMethodType": Literal["IAM"],
    },
)

GetApplicationAuthenticationMethodResponseTypeDef = TypedDict(
    "GetApplicationAuthenticationMethodResponseTypeDef",
    {
        "AuthenticationMethod": "AuthenticationMethodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationGrantRequestRequestTypeDef = TypedDict(
    "GetApplicationGrantRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "GrantType": GrantTypeType,
    },
)

GetApplicationGrantResponseTypeDef = TypedDict(
    "GetApplicationGrantResponseTypeDef",
    {
        "Grant": "GrantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInlinePolicyForPermissionSetRequestRequestTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

GetInlinePolicyForPermissionSetResponseTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    {
        "InlinePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef = TypedDict(
    "GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

GetPermissionsBoundaryForPermissionSetResponseTypeDef = TypedDict(
    "GetPermissionsBoundaryForPermissionSetResponseTypeDef",
    {
        "PermissionsBoundary": "PermissionsBoundaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantItemTypeDef = TypedDict(
    "GrantItemTypeDef",
    {
        "Grant": "GrantTypeDef",
        "GrantType": GrantTypeType,
    },
)

GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "AuthorizationCode": "AuthorizationCodeGrantTypeDef",
        "JwtBearer": "JwtBearerGrantTypeDef",
        "RefreshToken": Dict[str, Any],
        "TokenExchange": Dict[str, Any],
    },
    total=False,
)

IamAuthenticationMethodTypeDef = TypedDict(
    "IamAuthenticationMethodTypeDef",
    {
        "ActorPolicy": Dict[str, Any],
    },
)

InstanceAccessControlAttributeConfigurationTypeDef = TypedDict(
    "InstanceAccessControlAttributeConfigurationTypeDef",
    {
        "AccessControlAttributes": List["AccessControlAttributeTypeDef"],
    },
)

InstanceMetadataTypeDef = TypedDict(
    "InstanceMetadataTypeDef",
    {
        "CreatedDate": datetime,
        "IdentityStoreId": str,
        "InstanceArn": str,
        "Name": str,
        "OwnerAccountId": str,
        "Status": InstanceStatusType,
    },
    total=False,
)

JwtBearerGrantTypeDef = TypedDict(
    "JwtBearerGrantTypeDef",
    {
        "AuthorizedTokenIssuers": List["AuthorizedTokenIssuerTypeDef"],
    },
    total=False,
)

_RequiredListAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "Filter": "OperationStatusFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccountAssignmentCreationStatusRequestRequestTypeDef(
    _RequiredListAccountAssignmentCreationStatusRequestRequestTypeDef,
    _OptionalListAccountAssignmentCreationStatusRequestRequestTypeDef,
):
    pass

ListAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentsCreationStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "Filter": "OperationStatusFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccountAssignmentDeletionStatusRequestRequestTypeDef(
    _RequiredListAccountAssignmentDeletionStatusRequestRequestTypeDef,
    _OptionalListAccountAssignmentDeletionStatusRequestRequestTypeDef,
):
    pass

ListAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentsDeletionStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountAssignmentsFilterTypeDef = TypedDict(
    "ListAccountAssignmentsFilterTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

_RequiredListAccountAssignmentsForPrincipalRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentsForPrincipalRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)
_OptionalListAccountAssignmentsForPrincipalRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentsForPrincipalRequestRequestTypeDef",
    {
        "Filter": "ListAccountAssignmentsFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccountAssignmentsForPrincipalRequestRequestTypeDef(
    _RequiredListAccountAssignmentsForPrincipalRequestRequestTypeDef,
    _OptionalListAccountAssignmentsForPrincipalRequestRequestTypeDef,
):
    pass

ListAccountAssignmentsForPrincipalResponseTypeDef = TypedDict(
    "ListAccountAssignmentsForPrincipalResponseTypeDef",
    {
        "AccountAssignments": List["AccountAssignmentForPrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountAssignmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentsRequestRequestTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListAccountAssignmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccountAssignmentsRequestRequestTypeDef(
    _RequiredListAccountAssignmentsRequestRequestTypeDef,
    _OptionalListAccountAssignmentsRequestRequestTypeDef,
):
    pass

ListAccountAssignmentsResponseTypeDef = TypedDict(
    "ListAccountAssignmentsResponseTypeDef",
    {
        "AccountAssignments": List["AccountAssignmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountsForProvisionedPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListAccountsForProvisionedPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ProvisioningStatus": ProvisioningStatusType,
    },
    total=False,
)

class ListAccountsForProvisionedPermissionSetRequestRequestTypeDef(
    _RequiredListAccountsForProvisionedPermissionSetRequestRequestTypeDef,
    _OptionalListAccountsForProvisionedPermissionSetRequestRequestTypeDef,
):
    pass

ListAccountsForProvisionedPermissionSetResponseTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    {
        "AccountIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationAccessScopesRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationAccessScopesRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
_OptionalListApplicationAccessScopesRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationAccessScopesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationAccessScopesRequestRequestTypeDef(
    _RequiredListApplicationAccessScopesRequestRequestTypeDef,
    _OptionalListApplicationAccessScopesRequestRequestTypeDef,
):
    pass

ListApplicationAccessScopesResponseTypeDef = TypedDict(
    "ListApplicationAccessScopesResponseTypeDef",
    {
        "NextToken": str,
        "Scopes": List["ScopeDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationAssignmentsFilterTypeDef = TypedDict(
    "ListApplicationAssignmentsFilterTypeDef",
    {
        "ApplicationArn": str,
    },
    total=False,
)

_RequiredListApplicationAssignmentsForPrincipalRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationAssignmentsForPrincipalRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)
_OptionalListApplicationAssignmentsForPrincipalRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationAssignmentsForPrincipalRequestRequestTypeDef",
    {
        "Filter": "ListApplicationAssignmentsFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationAssignmentsForPrincipalRequestRequestTypeDef(
    _RequiredListApplicationAssignmentsForPrincipalRequestRequestTypeDef,
    _OptionalListApplicationAssignmentsForPrincipalRequestRequestTypeDef,
):
    pass

ListApplicationAssignmentsForPrincipalResponseTypeDef = TypedDict(
    "ListApplicationAssignmentsForPrincipalResponseTypeDef",
    {
        "ApplicationAssignments": List["ApplicationAssignmentForPrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationAssignmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationAssignmentsRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
_OptionalListApplicationAssignmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationAssignmentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationAssignmentsRequestRequestTypeDef(
    _RequiredListApplicationAssignmentsRequestRequestTypeDef,
    _OptionalListApplicationAssignmentsRequestRequestTypeDef,
):
    pass

ListApplicationAssignmentsResponseTypeDef = TypedDict(
    "ListApplicationAssignmentsResponseTypeDef",
    {
        "ApplicationAssignments": List["ApplicationAssignmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationAuthenticationMethodsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationAuthenticationMethodsRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
_OptionalListApplicationAuthenticationMethodsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationAuthenticationMethodsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListApplicationAuthenticationMethodsRequestRequestTypeDef(
    _RequiredListApplicationAuthenticationMethodsRequestRequestTypeDef,
    _OptionalListApplicationAuthenticationMethodsRequestRequestTypeDef,
):
    pass

ListApplicationAuthenticationMethodsResponseTypeDef = TypedDict(
    "ListApplicationAuthenticationMethodsResponseTypeDef",
    {
        "AuthenticationMethods": List["AuthenticationMethodItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationGrantsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationGrantsRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
_OptionalListApplicationGrantsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationGrantsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListApplicationGrantsRequestRequestTypeDef(
    _RequiredListApplicationGrantsRequestRequestTypeDef,
    _OptionalListApplicationGrantsRequestRequestTypeDef,
):
    pass

ListApplicationGrantsResponseTypeDef = TypedDict(
    "ListApplicationGrantsResponseTypeDef",
    {
        "Grants": List["GrantItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationProvidersRequestRequestTypeDef = TypedDict(
    "ListApplicationProvidersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListApplicationProvidersResponseTypeDef = TypedDict(
    "ListApplicationProvidersResponseTypeDef",
    {
        "ApplicationProviders": List["ApplicationProviderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsFilterTypeDef = TypedDict(
    "ListApplicationsFilterTypeDef",
    {
        "ApplicationAccount": str,
        "ApplicationProvider": str,
    },
    total=False,
)

_RequiredListApplicationsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationsRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListApplicationsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationsRequestRequestTypeDef",
    {
        "Filter": "ListApplicationsFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationsRequestRequestTypeDef(
    _RequiredListApplicationsRequestRequestTypeDef, _OptionalListApplicationsRequestRequestTypeDef
):
    pass

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "Applications": List["ApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef(
    _RequiredListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef,
    _OptionalListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef,
):
    pass

ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef = TypedDict(
    "ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef",
    {
        "CustomerManagedPolicyReferences": List["CustomerManagedPolicyReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List["InstanceMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagedPoliciesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListManagedPoliciesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListManagedPoliciesInPermissionSetRequestRequestTypeDef(
    _RequiredListManagedPoliciesInPermissionSetRequestRequestTypeDef,
    _OptionalListManagedPoliciesInPermissionSetRequestRequestTypeDef,
):
    pass

ListManagedPoliciesInPermissionSetResponseTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    {
        "AttachedManagedPolicies": List["AttachedManagedPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "Filter": "OperationStatusFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPermissionSetProvisioningStatusRequestRequestTypeDef(
    _RequiredListPermissionSetProvisioningStatusRequestRequestTypeDef,
    _OptionalListPermissionSetProvisioningStatusRequestRequestTypeDef,
):
    pass

ListPermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSetsProvisioningStatus": List["PermissionSetProvisioningStatusMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ProvisioningStatus": ProvisioningStatusType,
    },
    total=False,
)

class ListPermissionSetsProvisionedToAccountRequestRequestTypeDef(
    _RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef,
    _OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef,
):
    pass

ListPermissionSetsProvisionedToAccountResponseTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetsRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPermissionSetsRequestRequestTypeDef(
    _RequiredListPermissionSetsRequestRequestTypeDef,
    _OptionalListPermissionSetsRequestRequestTypeDef,
):
    pass

ListPermissionSetsResponseTypeDef = TypedDict(
    "ListPermissionSetsResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrustedTokenIssuersRequestRequestTypeDef = TypedDict(
    "_RequiredListTrustedTokenIssuersRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListTrustedTokenIssuersRequestRequestTypeDef = TypedDict(
    "_OptionalListTrustedTokenIssuersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTrustedTokenIssuersRequestRequestTypeDef(
    _RequiredListTrustedTokenIssuersRequestRequestTypeDef,
    _OptionalListTrustedTokenIssuersRequestRequestTypeDef,
):
    pass

ListTrustedTokenIssuersResponseTypeDef = TypedDict(
    "ListTrustedTokenIssuersResponseTypeDef",
    {
        "NextToken": str,
        "TrustedTokenIssuers": List["TrustedTokenIssuerMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OidcJwtConfigurationTypeDef = TypedDict(
    "OidcJwtConfigurationTypeDef",
    {
        "ClaimAttributePath": str,
        "IdentityStoreAttributePath": str,
        "IssuerUrl": str,
        "JwksRetrievalOption": Literal["OPEN_ID_DISCOVERY"],
    },
)

OidcJwtUpdateConfigurationTypeDef = TypedDict(
    "OidcJwtUpdateConfigurationTypeDef",
    {
        "ClaimAttributePath": str,
        "IdentityStoreAttributePath": str,
        "JwksRetrievalOption": Literal["OPEN_ID_DISCOVERY"],
    },
    total=False,
)

OperationStatusFilterTypeDef = TypedDict(
    "OperationStatusFilterTypeDef",
    {
        "Status": StatusValuesType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PermissionSetProvisioningStatusMetadataTypeDef = TypedDict(
    "PermissionSetProvisioningStatusMetadataTypeDef",
    {
        "CreatedDate": datetime,
        "RequestId": str,
        "Status": StatusValuesType,
    },
    total=False,
)

PermissionSetProvisioningStatusTypeDef = TypedDict(
    "PermissionSetProvisioningStatusTypeDef",
    {
        "AccountId": str,
        "CreatedDate": datetime,
        "FailureReason": str,
        "PermissionSetArn": str,
        "RequestId": str,
        "Status": StatusValuesType,
    },
    total=False,
)

PermissionSetTypeDef = TypedDict(
    "PermissionSetTypeDef",
    {
        "CreatedDate": datetime,
        "Description": str,
        "Name": str,
        "PermissionSetArn": str,
        "RelayState": str,
        "SessionDuration": str,
    },
    total=False,
)

PermissionsBoundaryTypeDef = TypedDict(
    "PermissionsBoundaryTypeDef",
    {
        "CustomerManagedPolicyReference": "CustomerManagedPolicyReferenceTypeDef",
        "ManagedPolicyArn": str,
    },
    total=False,
)

PortalOptionsTypeDef = TypedDict(
    "PortalOptionsTypeDef",
    {
        "SignInOptions": "SignInOptionsTypeDef",
        "Visibility": ApplicationVisibilityType,
    },
    total=False,
)

_RequiredProvisionPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredProvisionPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "TargetType": ProvisionTargetTypeType,
    },
)
_OptionalProvisionPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalProvisionPermissionSetRequestRequestTypeDef",
    {
        "TargetId": str,
    },
    total=False,
)

class ProvisionPermissionSetRequestRequestTypeDef(
    _RequiredProvisionPermissionSetRequestRequestTypeDef,
    _OptionalProvisionPermissionSetRequestRequestTypeDef,
):
    pass

ProvisionPermissionSetResponseTypeDef = TypedDict(
    "ProvisionPermissionSetResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutApplicationAccessScopeRequestRequestTypeDef = TypedDict(
    "_RequiredPutApplicationAccessScopeRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Scope": str,
    },
)
_OptionalPutApplicationAccessScopeRequestRequestTypeDef = TypedDict(
    "_OptionalPutApplicationAccessScopeRequestRequestTypeDef",
    {
        "AuthorizedTargets": List[str],
    },
    total=False,
)

class PutApplicationAccessScopeRequestRequestTypeDef(
    _RequiredPutApplicationAccessScopeRequestRequestTypeDef,
    _OptionalPutApplicationAccessScopeRequestRequestTypeDef,
):
    pass

PutApplicationAssignmentConfigurationRequestRequestTypeDef = TypedDict(
    "PutApplicationAssignmentConfigurationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AssignmentRequired": bool,
    },
)

PutApplicationAuthenticationMethodRequestRequestTypeDef = TypedDict(
    "PutApplicationAuthenticationMethodRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AuthenticationMethod": "AuthenticationMethodTypeDef",
        "AuthenticationMethodType": Literal["IAM"],
    },
)

PutApplicationGrantRequestRequestTypeDef = TypedDict(
    "PutApplicationGrantRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Grant": "GrantTypeDef",
        "GrantType": GrantTypeType,
    },
)

PutInlinePolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    {
        "InlinePolicy": str,
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef = TypedDict(
    "PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PermissionsBoundary": "PermissionsBoundaryTypeDef",
    },
)

ResourceServerConfigTypeDef = TypedDict(
    "ResourceServerConfigTypeDef",
    {
        "Scopes": Dict[str, "ResourceServerScopeDetailsTypeDef"],
    },
    total=False,
)

ResourceServerScopeDetailsTypeDef = TypedDict(
    "ResourceServerScopeDetailsTypeDef",
    {
        "DetailedTitle": str,
        "LongDescription": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredScopeDetailsTypeDef = TypedDict(
    "_RequiredScopeDetailsTypeDef",
    {
        "Scope": str,
    },
)
_OptionalScopeDetailsTypeDef = TypedDict(
    "_OptionalScopeDetailsTypeDef",
    {
        "AuthorizedTargets": List[str],
    },
    total=False,
)

class ScopeDetailsTypeDef(_RequiredScopeDetailsTypeDef, _OptionalScopeDetailsTypeDef):
    pass

_RequiredSignInOptionsTypeDef = TypedDict(
    "_RequiredSignInOptionsTypeDef",
    {
        "Origin": SignInOriginType,
    },
)
_OptionalSignInOptionsTypeDef = TypedDict(
    "_OptionalSignInOptionsTypeDef",
    {
        "ApplicationUrl": str,
    },
    total=False,
)

class SignInOptionsTypeDef(_RequiredSignInOptionsTypeDef, _OptionalSignInOptionsTypeDef):
    pass

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TrustedTokenIssuerConfigurationTypeDef = TypedDict(
    "TrustedTokenIssuerConfigurationTypeDef",
    {
        "OidcJwtConfiguration": "OidcJwtConfigurationTypeDef",
    },
    total=False,
)

TrustedTokenIssuerMetadataTypeDef = TypedDict(
    "TrustedTokenIssuerMetadataTypeDef",
    {
        "Name": str,
        "TrustedTokenIssuerArn": str,
        "TrustedTokenIssuerType": Literal["OIDC_JWT"],
    },
    total=False,
)

TrustedTokenIssuerUpdateConfigurationTypeDef = TypedDict(
    "TrustedTokenIssuerUpdateConfigurationTypeDef",
    {
        "OidcJwtConfiguration": "OidcJwtUpdateConfigurationTypeDef",
    },
    total=False,
)

_RequiredUntagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
_OptionalUntagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUntagResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
    total=False,
)

class UntagResourceRequestRequestTypeDef(
    _RequiredUntagResourceRequestRequestTypeDef, _OptionalUntagResourceRequestRequestTypeDef
):
    pass

UpdateApplicationPortalOptionsTypeDef = TypedDict(
    "UpdateApplicationPortalOptionsTypeDef",
    {
        "SignInOptions": "SignInOptionsTypeDef",
    },
    total=False,
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "Description": str,
        "Name": str,
        "PortalOptions": "UpdateApplicationPortalOptionsTypeDef",
        "Status": ApplicationStatusType,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
        "InstanceArn": str,
    },
)

UpdateInstanceRequestRequestTypeDef = TypedDict(
    "UpdateInstanceRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Name": str,
    },
)

_RequiredUpdatePermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalUpdatePermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePermissionSetRequestRequestTypeDef",
    {
        "Description": str,
        "RelayState": str,
        "SessionDuration": str,
    },
    total=False,
)

class UpdatePermissionSetRequestRequestTypeDef(
    _RequiredUpdatePermissionSetRequestRequestTypeDef,
    _OptionalUpdatePermissionSetRequestRequestTypeDef,
):
    pass

_RequiredUpdateTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustedTokenIssuerRequestRequestTypeDef",
    {
        "TrustedTokenIssuerArn": str,
    },
)
_OptionalUpdateTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustedTokenIssuerRequestRequestTypeDef",
    {
        "Name": str,
        "TrustedTokenIssuerConfiguration": "TrustedTokenIssuerUpdateConfigurationTypeDef",
    },
    total=False,
)

class UpdateTrustedTokenIssuerRequestRequestTypeDef(
    _RequiredUpdateTrustedTokenIssuerRequestRequestTypeDef,
    _OptionalUpdateTrustedTokenIssuerRequestRequestTypeDef,
):
    pass
