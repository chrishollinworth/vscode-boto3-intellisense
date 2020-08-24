# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for iam service ServiceResource

Usage::

    ```python
    import boto3

    from mypy_boto3_iam import IAMServiceResource
    import mypy_boto3_iam.service_resource as iam_resources

    resource: IAMServiceResource = boto3.resource("iam")

    my_access_key: iam_resources.AccessKey = resource.AccessKey(...)
    my_access_key_pair: iam_resources.AccessKeyPair = resource.AccessKeyPair(...)
    my_account_password_policy: iam_resources.AccountPasswordPolicy = resource.AccountPasswordPolicy(...)
    my_account_summary: iam_resources.AccountSummary = resource.AccountSummary(...)
    my_assume_role_policy: iam_resources.AssumeRolePolicy = resource.AssumeRolePolicy(...)
    my_current_user: iam_resources.CurrentUser = resource.CurrentUser(...)
    my_group: iam_resources.Group = resource.Group(...)
    my_group_policy: iam_resources.GroupPolicy = resource.GroupPolicy(...)
    my_instance_profile: iam_resources.InstanceProfile = resource.InstanceProfile(...)
    my_login_profile: iam_resources.LoginProfile = resource.LoginProfile(...)
    my_mfa_device: iam_resources.MfaDevice = resource.MfaDevice(...)
    my_policy: iam_resources.Policy = resource.Policy(...)
    my_policy_version: iam_resources.PolicyVersion = resource.PolicyVersion(...)
    my_role: iam_resources.Role = resource.Role(...)
    my_role_policy: iam_resources.RolePolicy = resource.RolePolicy(...)
    my_saml_provider: iam_resources.SamlProvider = resource.SamlProvider(...)
    my_server_certificate: iam_resources.ServerCertificate = resource.ServerCertificate(...)
    my_signing_certificate: iam_resources.SigningCertificate = resource.SigningCertificate(...)
    my_user: iam_resources.User = resource.User(...)
    my_user_policy: iam_resources.UserPolicy = resource.UserPolicy(...)
    my_virtual_mfa_device: iam_resources.VirtualMfaDevice = resource.VirtualMfaDevice(...)
```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_iam.type_defs import TagTypeDef, UpdateSAMLProviderResponseTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "IAMServiceResource",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupUsersCollection",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersionsCollection",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserSigningCertificatesCollection",
)


class ServiceResourceGroupsCollection(ResourceCollection):
    """
    [ServiceResource.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.groups)
    """

    def all(self) -> "ServiceResourceGroupsCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceGroupsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceGroupsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    [ServiceResource.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
    """

    def all(self) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(self) -> Iterator["InstanceProfile"]:
        pass


class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    [ServiceResource.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.policies)
    """

    def all(self) -> "ServiceResourcePoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "ServiceResourcePoliciesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourcePoliciesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourcePoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class ServiceResourceRolesCollection(ResourceCollection):
    """
    [ServiceResource.roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.roles)
    """

    def all(self) -> "ServiceResourceRolesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceRolesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceRolesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceRolesCollection":
        pass

    def pages(self) -> Iterator[List["Role"]]:
        pass

    def __iter__(self) -> Iterator["Role"]:
        pass


class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    [ServiceResource.saml_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.saml_providers)
    """

    def all(self) -> "ServiceResourceSamlProvidersCollection":
        pass

    def filter(  # type: ignore
        self,
    ) -> "ServiceResourceSamlProvidersCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        pass

    def pages(self) -> Iterator[List["SamlProvider"]]:
        pass

    def __iter__(self) -> Iterator["SamlProvider"]:
        pass


class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    [ServiceResource.server_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.server_certificates)
    """

    def all(self) -> "ServiceResourceServerCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceServerCertificatesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["ServerCertificate"]]:
        pass

    def __iter__(self) -> Iterator["ServerCertificate"]:
        pass


class ServiceResourceUsersCollection(ResourceCollection):
    """
    [ServiceResource.users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.users)
    """

    def all(self) -> "ServiceResourceUsersCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceUsersCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceUsersCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    [ServiceResource.virtual_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
    """

    def all(self) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["VirtualMfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["VirtualMfaDevice"]:
        pass


class CurrentUserAccessKeysCollection(ResourceCollection):
    """
    [CurrentUser.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.CurrentUser.access_keys)
    """

    def all(self) -> "CurrentUserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserAccessKeysCollection":
        pass

    def limit(self, count: int) -> "CurrentUserAccessKeysCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserAccessKeysCollection":
        pass

    def pages(self) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(self) -> Iterator["AccessKey"]:
        pass


class CurrentUserMfaDevicesCollection(ResourceCollection):
    """
    [CurrentUser.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.CurrentUser.mfa_devices)
    """

    def all(self) -> "CurrentUserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "CurrentUserMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["MfaDevice"]:
        pass


class CurrentUserSigningCertificatesCollection(ResourceCollection):
    """
    [CurrentUser.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.CurrentUser.signing_certificates)
    """

    def all(self) -> "CurrentUserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserSigningCertificatesCollection":
        pass

    def limit(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(self) -> Iterator["SigningCertificate"]:
        pass


class GroupAttachedPoliciesCollection(ResourceCollection):
    """
    [Group.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.attached_policies)
    """

    def all(self) -> "GroupAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "GroupAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "GroupAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "GroupAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class GroupPoliciesCollection(ResourceCollection):
    """
    [Group.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.policies)
    """

    def all(self) -> "GroupPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "GroupPoliciesCollection":
        pass

    def limit(self, count: int) -> "GroupPoliciesCollection":
        pass

    def page_size(self, count: int) -> "GroupPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["GroupPolicy"]]:
        pass

    def __iter__(self) -> Iterator["GroupPolicy"]:
        pass


class GroupUsersCollection(ResourceCollection):
    """
    [Group.users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.users)
    """

    def all(self) -> "GroupUsersCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "GroupUsersCollection":
        pass

    def limit(self, count: int) -> "GroupUsersCollection":
        pass

    def page_size(self, count: int) -> "GroupUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class PolicyAttachedGroupsCollection(ResourceCollection):
    """
    [Policy.attached_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.attached_groups)
    """

    def all(self) -> "PolicyAttachedGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedGroupsCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedGroupsCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class PolicyAttachedRolesCollection(ResourceCollection):
    """
    [Policy.attached_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.attached_roles)
    """

    def all(self) -> "PolicyAttachedRolesCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedRolesCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedRolesCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedRolesCollection":
        pass

    def pages(self) -> Iterator[List["Role"]]:
        pass

    def __iter__(self) -> Iterator["Role"]:
        pass


class PolicyAttachedUsersCollection(ResourceCollection):
    """
    [Policy.attached_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.attached_users)
    """

    def all(self) -> "PolicyAttachedUsersCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedUsersCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedUsersCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class PolicyVersionsCollection(ResourceCollection):
    """
    [Policy.versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.versions)
    """

    def all(self) -> "PolicyVersionsCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "PolicyVersionsCollection":
        pass

    def limit(self, count: int) -> "PolicyVersionsCollection":
        pass

    def page_size(self, count: int) -> "PolicyVersionsCollection":
        pass

    def pages(self) -> Iterator[List["PolicyVersion"]]:
        pass

    def __iter__(self) -> Iterator["PolicyVersion"]:
        pass


class RoleAttachedPoliciesCollection(ResourceCollection):
    """
    [Role.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.attached_policies)
    """

    def all(self) -> "RoleAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "RoleAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "RoleAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "RoleAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class RoleInstanceProfilesCollection(ResourceCollection):
    """
    [Role.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.instance_profiles)
    """

    def all(self) -> "RoleInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "RoleInstanceProfilesCollection":
        pass

    def limit(self, count: int) -> "RoleInstanceProfilesCollection":
        pass

    def page_size(self, count: int) -> "RoleInstanceProfilesCollection":
        pass

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(self) -> Iterator["InstanceProfile"]:
        pass


class RolePoliciesCollection(ResourceCollection):
    """
    [Role.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.policies)
    """

    def all(self) -> "RolePoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "RolePoliciesCollection":
        pass

    def limit(self, count: int) -> "RolePoliciesCollection":
        pass

    def page_size(self, count: int) -> "RolePoliciesCollection":
        pass

    def pages(self) -> Iterator[List["RolePolicy"]]:
        pass

    def __iter__(self) -> Iterator["RolePolicy"]:
        pass


class UserAccessKeysCollection(ResourceCollection):
    """
    [User.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.access_keys)
    """

    def all(self) -> "UserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserAccessKeysCollection":
        pass

    def limit(self, count: int) -> "UserAccessKeysCollection":
        pass

    def page_size(self, count: int) -> "UserAccessKeysCollection":
        pass

    def pages(self) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(self) -> Iterator["AccessKey"]:
        pass


class UserAttachedPoliciesCollection(ResourceCollection):
    """
    [User.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.attached_policies)
    """

    def all(self) -> "UserAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "UserAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "UserAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class UserGroupsCollection(ResourceCollection):
    """
    [User.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.groups)
    """

    def all(self) -> "UserGroupsCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "UserGroupsCollection":
        pass

    def limit(self, count: int) -> "UserGroupsCollection":
        pass

    def page_size(self, count: int) -> "UserGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class UserMfaDevicesCollection(ResourceCollection):
    """
    [User.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.mfa_devices)
    """

    def all(self) -> "UserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "UserMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "UserMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["MfaDevice"]:
        pass


class UserPoliciesCollection(ResourceCollection):
    """
    [User.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.policies)
    """

    def all(self) -> "UserPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "UserPoliciesCollection":
        pass

    def limit(self, count: int) -> "UserPoliciesCollection":
        pass

    def page_size(self, count: int) -> "UserPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["UserPolicy"]]:
        pass

    def __iter__(self) -> Iterator["UserPolicy"]:
        pass


class UserSigningCertificatesCollection(ResourceCollection):
    """
    [User.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.signing_certificates)
    """

    def all(self) -> "UserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserSigningCertificatesCollection":
        pass

    def limit(self, count: int) -> "UserSigningCertificatesCollection":
        pass

    def page_size(self, count: int) -> "UserSigningCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(self) -> Iterator["SigningCertificate"]:
        pass


class AccessKeyPair(Boto3ServiceResource):
    """
    [AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
    """

    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    def activate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKeyPair.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKeyPair.activate)
        """

    def deactivate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKeyPair.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKeyPair.deactivate)
        """

    def delete(self) -> None:
        """
        [AccessKeyPair.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKeyPair.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [AccessKeyPair.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKeyPair.get_available_subresources)
        """


_AccessKeyPair = AccessKeyPair


class AccountPasswordPolicy(Boto3ServiceResource):
    """
    [AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
    """

    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    def delete(self) -> None:
        """
        [AccountPasswordPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountPasswordPolicy.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [AccountPasswordPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountPasswordPolicy.get_available_subresources)
        """

    def load(self) -> None:
        """
        [AccountPasswordPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountPasswordPolicy.load)
        """

    def reload(self) -> None:
        """
        [AccountPasswordPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountPasswordPolicy.reload)
        """

    def update(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        """
        [AccountPasswordPolicy.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountPasswordPolicy.update)
        """


_AccountPasswordPolicy = AccountPasswordPolicy


class AccountSummary(Boto3ServiceResource):
    """
    [AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
    """

    summary_map: Dict[str, Any]

    def get_available_subresources(self) -> List[str]:
        """
        [AccountSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountSummary.get_available_subresources)
        """

    def load(self) -> None:
        """
        [AccountSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountSummary.load)
        """

    def reload(self) -> None:
        """
        [AccountSummary.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccountSummary.reload)
        """


_AccountSummary = AccountSummary


class CurrentUser(Boto3ServiceResource):
    """
    [CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    user: "User"
    access_keys: CurrentUserAccessKeysCollection
    mfa_devices: CurrentUserMfaDevicesCollection
    signing_certificates: CurrentUserSigningCertificatesCollection

    def get_available_subresources(self) -> List[str]:
        """
        [CurrentUser.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.CurrentUser.get_available_subresources)
        """

    def load(self) -> None:
        """
        [CurrentUser.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.CurrentUser.load)
        """

    def reload(self) -> None:
        """
        [CurrentUser.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.CurrentUser.reload)
        """


_CurrentUser = CurrentUser


class InstanceProfile(Boto3ServiceResource):
    """
    [InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
    """

    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[Any]
    name: str
    roles: "Role"

    def add_role(self, RoleName: str) -> None:
        """
        [InstanceProfile.add_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.InstanceProfile.add_role)
        """

    def delete(self) -> None:
        """
        [InstanceProfile.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.InstanceProfile.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [InstanceProfile.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.InstanceProfile.get_available_subresources)
        """

    def load(self) -> None:
        """
        [InstanceProfile.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.InstanceProfile.load)
        """

    def reload(self) -> None:
        """
        [InstanceProfile.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.InstanceProfile.reload)
        """

    def remove_role(self, RoleName: str) -> None:
        """
        [InstanceProfile.remove_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.InstanceProfile.remove_role)
        """


_InstanceProfile = InstanceProfile


class PolicyVersion(Boto3ServiceResource):
    """
    [PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
    """

    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    def delete(self) -> None:
        """
        [PolicyVersion.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.PolicyVersion.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [PolicyVersion.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.PolicyVersion.get_available_subresources)
        """

    def load(self) -> None:
        """
        [PolicyVersion.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.PolicyVersion.load)
        """

    def reload(self) -> None:
        """
        [PolicyVersion.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.PolicyVersion.reload)
        """

    def set_as_default(self) -> None:
        """
        [PolicyVersion.set_as_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.PolicyVersion.set_as_default)
        """


_PolicyVersion = PolicyVersion


class SamlProvider(Boto3ServiceResource):
    """
    [SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
    """

    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    arn: str

    def delete(self) -> None:
        """
        [SamlProvider.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SamlProvider.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [SamlProvider.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SamlProvider.get_available_subresources)
        """

    def load(self) -> None:
        """
        [SamlProvider.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SamlProvider.load)
        """

    def reload(self) -> None:
        """
        [SamlProvider.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SamlProvider.reload)
        """

    def update(self, SAMLMetadataDocument: str) -> UpdateSAMLProviderResponseTypeDef:
        """
        [SamlProvider.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SamlProvider.update)
        """


_SamlProvider = SamlProvider


class VirtualMfaDevice(Boto3ServiceResource):
    """
    [VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
    """

    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict[str, Any]
    enable_date: datetime
    serial_number: str
    user: "User"

    def delete(self) -> None:
        """
        [VirtualMfaDevice.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.VirtualMfaDevice.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [VirtualMfaDevice.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.VirtualMfaDevice.get_available_subresources)
        """


_VirtualMfaDevice = VirtualMfaDevice


class AccessKey(Boto3ServiceResource):
    """
    [AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccessKey)
    """

    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    def User(self) -> "_User":
        """
        [AccessKey.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKey.User)
        """

    def activate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKey.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKey.activate)
        """

    def deactivate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKey.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKey.deactivate)
        """

    def delete(self) -> None:
        """
        [AccessKey.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKey.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [AccessKey.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AccessKey.get_available_subresources)
        """


_AccessKey = AccessKey


class AssumeRolePolicy(Boto3ServiceResource):
    """
    [AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
    """

    role_name: str

    def Role(self) -> "_Role":
        """
        [AssumeRolePolicy.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AssumeRolePolicy.Role)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [AssumeRolePolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AssumeRolePolicy.get_available_subresources)
        """

    def update(self, PolicyDocument: str) -> None:
        """
        [AssumeRolePolicy.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.AssumeRolePolicy.update)
        """


_AssumeRolePolicy = AssumeRolePolicy


class GroupPolicy(Boto3ServiceResource):
    """
    [GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
    """

    policy_name: str
    policy_document: str
    group_name: str
    name: str

    def Group(self) -> "_Group":
        """
        [GroupPolicy.Group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.GroupPolicy.Group)
        """

    def delete(self) -> None:
        """
        [GroupPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.GroupPolicy.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [GroupPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.GroupPolicy.get_available_subresources)
        """

    def load(self) -> None:
        """
        [GroupPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.GroupPolicy.load)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [GroupPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.GroupPolicy.put)
        """

    def reload(self) -> None:
        """
        [GroupPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.GroupPolicy.reload)
        """


_GroupPolicy = GroupPolicy


class MfaDevice(Boto3ServiceResource):
    """
    [MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
    """

    enable_date: datetime
    user_name: str
    serial_number: str

    def User(self) -> "_User":
        """
        [MfaDevice.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.MfaDevice.User)
        """

    def associate(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [MfaDevice.associate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.MfaDevice.associate)
        """

    def disassociate(self) -> None:
        """
        [MfaDevice.disassociate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.MfaDevice.disassociate)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MfaDevice.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.MfaDevice.get_available_subresources)
        """

    def resync(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [MfaDevice.resync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.MfaDevice.resync)
        """


_MfaDevice = MfaDevice


class Policy(Boto3ServiceResource):
    """
    [Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.Policy)
    """

    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    arn: str
    default_version: "PolicyVersion"
    attached_groups: PolicyAttachedGroupsCollection
    attached_roles: PolicyAttachedRolesCollection
    attached_users: PolicyAttachedUsersCollection
    versions: PolicyVersionsCollection

    def attach_group(self, GroupName: str) -> None:
        """
        [Policy.attach_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.attach_group)
        """

    def attach_role(self, RoleName: str) -> None:
        """
        [Policy.attach_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.attach_role)
        """

    def attach_user(self, UserName: str) -> None:
        """
        [Policy.attach_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.attach_user)
        """

    def create_version(self, PolicyDocument: str, SetAsDefault: bool = None) -> _PolicyVersion:
        """
        [Policy.create_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.create_version)
        """

    def delete(self) -> None:
        """
        [Policy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.delete)
        """

    def detach_group(self, GroupName: str) -> None:
        """
        [Policy.detach_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.detach_group)
        """

    def detach_role(self, RoleName: str) -> None:
        """
        [Policy.detach_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.detach_role)
        """

    def detach_user(self, UserName: str) -> None:
        """
        [Policy.detach_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.detach_user)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Policy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Policy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.load)
        """

    def reload(self) -> None:
        """
        [Policy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Policy.reload)
        """


_Policy = Policy


class RolePolicy(Boto3ServiceResource):
    """
    [RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
    """

    policy_name: str
    policy_document: str
    role_name: str
    name: str

    def Role(self) -> "_Role":
        """
        [RolePolicy.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.RolePolicy.Role)
        """

    def delete(self) -> None:
        """
        [RolePolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.RolePolicy.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [RolePolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.RolePolicy.get_available_subresources)
        """

    def load(self) -> None:
        """
        [RolePolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.RolePolicy.load)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [RolePolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.RolePolicy.put)
        """

    def reload(self) -> None:
        """
        [RolePolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.RolePolicy.reload)
        """


_RolePolicy = RolePolicy


class ServerCertificate(Boto3ServiceResource):
    """
    [ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
    """

    server_certificate_metadata: Dict[str, Any]
    certificate_body: str
    certificate_chain: str
    name: str

    def delete(self) -> None:
        """
        [ServerCertificate.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServerCertificate.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServerCertificate.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServerCertificate.get_available_subresources)
        """

    def load(self) -> None:
        """
        [ServerCertificate.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServerCertificate.load)
        """

    def reload(self) -> None:
        """
        [ServerCertificate.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServerCertificate.reload)
        """

    def update(
        self, NewPath: str = None, NewServerCertificateName: str = None
    ) -> "_ServerCertificate":
        """
        [ServerCertificate.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServerCertificate.update)
        """


_ServerCertificate = ServerCertificate


class SigningCertificate(Boto3ServiceResource):
    """
    [SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
    """

    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    def User(self) -> "_User":
        """
        [SigningCertificate.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SigningCertificate.User)
        """

    def activate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [SigningCertificate.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SigningCertificate.activate)
        """

    def deactivate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [SigningCertificate.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SigningCertificate.deactivate)
        """

    def delete(self) -> None:
        """
        [SigningCertificate.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SigningCertificate.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [SigningCertificate.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.SigningCertificate.get_available_subresources)
        """


_SigningCertificate = SigningCertificate


class UserPolicy(Boto3ServiceResource):
    """
    [UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
    """

    policy_name: str
    policy_document: str
    user_name: str
    name: str

    def User(self) -> "_User":
        """
        [UserPolicy.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.UserPolicy.User)
        """

    def delete(self) -> None:
        """
        [UserPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.UserPolicy.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [UserPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.UserPolicy.get_available_subresources)
        """

    def load(self) -> None:
        """
        [UserPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.UserPolicy.load)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [UserPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.UserPolicy.put)
        """

    def reload(self) -> None:
        """
        [UserPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.UserPolicy.reload)
        """


_UserPolicy = UserPolicy


class LoginProfile(Boto3ServiceResource):
    """
    [LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
    """

    create_date: datetime
    password_reset_required: bool
    user_name: str

    def User(self) -> "_User":
        """
        [LoginProfile.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.LoginProfile.User)
        """

    def create(self, Password: str, PasswordResetRequired: bool = None) -> "_LoginProfile":
        """
        [LoginProfile.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.LoginProfile.create)
        """

    def delete(self) -> None:
        """
        [LoginProfile.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.LoginProfile.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [LoginProfile.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.LoginProfile.get_available_subresources)
        """

    def load(self) -> None:
        """
        [LoginProfile.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.LoginProfile.load)
        """

    def reload(self) -> None:
        """
        [LoginProfile.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.LoginProfile.reload)
        """

    def update(self, Password: str = None, PasswordResetRequired: bool = None) -> None:
        """
        [LoginProfile.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.LoginProfile.update)
        """


_LoginProfile = LoginProfile


class Role(Boto3ServiceResource):
    """
    [Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.Role)
    """

    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    role_last_used: Dict[str, Any]
    name: str
    attached_policies: RoleAttachedPoliciesCollection
    instance_profiles: RoleInstanceProfilesCollection
    policies: RolePoliciesCollection

    def AssumeRolePolicy(self) -> _AssumeRolePolicy:
        """
        [Role.AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.AssumeRolePolicy)
        """

    def Policy(self, name: str) -> _RolePolicy:
        """
        [Role.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.Policy)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Role.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.attach_policy)
        """

    def delete(self) -> None:
        """
        [Role.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.delete)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Role.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.detach_policy)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Role.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Role.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.load)
        """

    def reload(self) -> None:
        """
        [Role.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Role.reload)
        """


_Role = Role


class Group(Boto3ServiceResource):
    """
    [Group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.Group)
    """

    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: GroupAttachedPoliciesCollection
    policies: GroupPoliciesCollection
    users: GroupUsersCollection

    def Policy(self, name: str) -> _GroupPolicy:
        """
        [Group.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.Policy)
        """

    def add_user(self, UserName: str) -> None:
        """
        [Group.add_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.add_user)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Group.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.attach_policy)
        """

    def create(self, Path: str = None) -> "_Group":
        """
        [Group.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.create)
        """

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> _GroupPolicy:
        """
        [Group.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.create_policy)
        """

    def delete(self) -> None:
        """
        [Group.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.delete)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Group.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.detach_policy)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Group.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Group.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.load)
        """

    def reload(self) -> None:
        """
        [Group.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.reload)
        """

    def remove_user(self, UserName: str) -> None:
        """
        [Group.remove_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.remove_user)
        """

    def update(self, NewPath: str = None, NewGroupName: str = None) -> "_Group":
        """
        [Group.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Group.update)
        """


_Group = Group


class User(Boto3ServiceResource):
    """
    [User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.User)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    name: str
    access_keys: UserAccessKeysCollection
    attached_policies: UserAttachedPoliciesCollection
    groups: UserGroupsCollection
    mfa_devices: UserMfaDevicesCollection
    policies: UserPoliciesCollection
    signing_certificates: UserSigningCertificatesCollection

    def AccessKey(self, id: str) -> _AccessKey:
        """
        [User.AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.AccessKey)
        """

    def LoginProfile(self) -> _LoginProfile:
        """
        [User.LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.LoginProfile)
        """

    def MfaDevice(self, serial_number: str) -> _MfaDevice:
        """
        [User.MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.MfaDevice)
        """

    def Policy(self, name: str) -> _UserPolicy:
        """
        [User.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.Policy)
        """

    def SigningCertificate(self, id: str) -> _SigningCertificate:
        """
        [User.SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.SigningCertificate)
        """

    def add_group(self, GroupName: str) -> None:
        """
        [User.add_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.add_group)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [User.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.attach_policy)
        """

    def create(
        self, Path: str = None, PermissionsBoundary: str = None, Tags: List["TagTypeDef"] = None
    ) -> "_User":
        """
        [User.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.create)
        """

    def create_access_key_pair(self) -> _AccessKeyPair:
        """
        [User.create_access_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.create_access_key_pair)
        """

    def create_login_profile(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> _LoginProfile:
        """
        [User.create_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.create_login_profile)
        """

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> _UserPolicy:
        """
        [User.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.create_policy)
        """

    def delete(self) -> None:
        """
        [User.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.delete)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [User.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.detach_policy)
        """

    def enable_mfa(
        self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> _MfaDevice:
        """
        [User.enable_mfa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.enable_mfa)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [User.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.get_available_subresources)
        """

    def load(self) -> None:
        """
        [User.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.load)
        """

    def reload(self) -> None:
        """
        [User.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.reload)
        """

    def remove_group(self, GroupName: str) -> None:
        """
        [User.remove_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.remove_group)
        """

    def update(self, NewPath: str = None, NewUserName: str = None) -> "_User":
        """
        [User.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.User.update)
        """


_User = User


class IAMServiceResource(Boto3ServiceResource):
    """
    [IAM.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource)
    """

    groups: ServiceResourceGroupsCollection
    instance_profiles: ServiceResourceInstanceProfilesCollection
    policies: ServiceResourcePoliciesCollection
    roles: ServiceResourceRolesCollection
    saml_providers: ServiceResourceSamlProvidersCollection
    server_certificates: ServiceResourceServerCertificatesCollection
    users: ServiceResourceUsersCollection
    virtual_mfa_devices: ServiceResourceVirtualMfaDevicesCollection

    def AccessKey(self, user_name: str, id: str) -> _AccessKey:
        """
        [ServiceResource.AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccessKey)
        """

    def AccessKeyPair(self, user_name: str, id: str, secret: str) -> _AccessKeyPair:
        """
        [ServiceResource.AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
        """

    def AccountPasswordPolicy(self) -> _AccountPasswordPolicy:
        """
        [ServiceResource.AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
        """

    def AccountSummary(self) -> _AccountSummary:
        """
        [ServiceResource.AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
        """

    def AssumeRolePolicy(self, role_name: str) -> _AssumeRolePolicy:
        """
        [ServiceResource.AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
        """

    def CurrentUser(self) -> _CurrentUser:
        """
        [ServiceResource.CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
        """

    def Group(self, name: str) -> _Group:
        """
        [ServiceResource.Group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.Group)
        """

    def GroupPolicy(self, group_name: str, name: str) -> _GroupPolicy:
        """
        [ServiceResource.GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
        """

    def InstanceProfile(self, name: str) -> _InstanceProfile:
        """
        [ServiceResource.InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
        """

    def LoginProfile(self, user_name: str) -> _LoginProfile:
        """
        [ServiceResource.LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
        """

    def MfaDevice(self, user_name: str, serial_number: str) -> _MfaDevice:
        """
        [ServiceResource.MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
        """

    def Policy(self, policy_arn: str) -> _Policy:
        """
        [ServiceResource.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.Policy)
        """

    def PolicyVersion(self, arn: str, version_id: str) -> _PolicyVersion:
        """
        [ServiceResource.PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
        """

    def Role(self, name: str) -> _Role:
        """
        [ServiceResource.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.Role)
        """

    def RolePolicy(self, role_name: str, name: str) -> _RolePolicy:
        """
        [ServiceResource.RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
        """

    def SamlProvider(self, arn: str) -> _SamlProvider:
        """
        [ServiceResource.SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
        """

    def ServerCertificate(self, name: str) -> _ServerCertificate:
        """
        [ServiceResource.ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
        """

    def SigningCertificate(self, user_name: str, id: str) -> _SigningCertificate:
        """
        [ServiceResource.SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
        """

    def User(self, name: str) -> _User:
        """
        [ServiceResource.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.User)
        """

    def UserPolicy(self, user_name: str, name: str) -> _UserPolicy:
        """
        [ServiceResource.UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
        """

    def VirtualMfaDevice(self, serial_number: str) -> _VirtualMfaDevice:
        """
        [ServiceResource.VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
        """

    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        [ServiceResource.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.change_password)
        """

    def create_account_alias(self, AccountAlias: str) -> None:
        """
        [ServiceResource.create_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_account_alias)
        """

    def create_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> _AccountPasswordPolicy:
        """
        [ServiceResource.create_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_account_password_policy)
        """

    def create_group(self, GroupName: str, Path: str = None) -> _Group:
        """
        [ServiceResource.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_group)
        """

    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None
    ) -> _InstanceProfile:
        """
        [ServiceResource.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_instance_profile)
        """

    def create_policy(
        self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None
    ) -> _Policy:
        """
        [ServiceResource.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_policy)
        """

    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _Role:
        """
        [ServiceResource.create_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_role)
        """

    def create_saml_provider(self, SAMLMetadataDocument: str, Name: str) -> _SamlProvider:
        """
        [ServiceResource.create_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_saml_provider)
        """

    def create_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
    ) -> _ServerCertificate:
        """
        [ServiceResource.create_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_server_certificate)
        """

    def create_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> _SigningCertificate:
        """
        [ServiceResource.create_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_signing_certificate)
        """

    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _User:
        """
        [ServiceResource.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_user)
        """

    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None
    ) -> _VirtualMfaDevice:
        """
        [ServiceResource.create_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.create_virtual_mfa_device)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.ServiceResource.get_available_subresources)
        """
