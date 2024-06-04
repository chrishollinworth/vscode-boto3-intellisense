"""
Type annotations for pca-connector-ad service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pca_connector_ad.type_defs import AccessControlEntrySummaryTypeDef

    data: AccessControlEntrySummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessRightType,
    ApplicationPolicyTypeType,
    ClientCompatibilityV2Type,
    ClientCompatibilityV3Type,
    ClientCompatibilityV4Type,
    ConnectorStatusReasonType,
    ConnectorStatusType,
    DirectoryRegistrationStatusReasonType,
    DirectoryRegistrationStatusType,
    HashAlgorithmType,
    KeySpecType,
    PrivateKeyAlgorithmType,
    ServicePrincipalNameStatusReasonType,
    ServicePrincipalNameStatusType,
    TemplateStatusType,
    ValidityPeriodTypeType,
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
    "AccessControlEntrySummaryTypeDef",
    "AccessControlEntryTypeDef",
    "AccessRightsTypeDef",
    "ApplicationPoliciesTypeDef",
    "ApplicationPolicyTypeDef",
    "CertificateValidityTypeDef",
    "ConnectorSummaryTypeDef",
    "ConnectorTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateDirectoryRegistrationRequestRequestTypeDef",
    "CreateDirectoryRegistrationResponseTypeDef",
    "CreateServicePrincipalNameRequestRequestTypeDef",
    "CreateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "CreateTemplateResponseTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "DeleteDirectoryRegistrationRequestRequestTypeDef",
    "DeleteServicePrincipalNameRequestRequestTypeDef",
    "DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DirectoryRegistrationSummaryTypeDef",
    "DirectoryRegistrationTypeDef",
    "EnrollmentFlagsV2TypeDef",
    "EnrollmentFlagsV3TypeDef",
    "EnrollmentFlagsV4TypeDef",
    "ExtensionsV2TypeDef",
    "ExtensionsV3TypeDef",
    "ExtensionsV4TypeDef",
    "GeneralFlagsV2TypeDef",
    "GeneralFlagsV3TypeDef",
    "GeneralFlagsV4TypeDef",
    "GetConnectorRequestRequestTypeDef",
    "GetConnectorResponseTypeDef",
    "GetDirectoryRegistrationRequestRequestTypeDef",
    "GetDirectoryRegistrationResponseTypeDef",
    "GetServicePrincipalNameRequestRequestTypeDef",
    "GetServicePrincipalNameResponseTypeDef",
    "GetTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "GetTemplateGroupAccessControlEntryResponseTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "KeyUsageFlagsTypeDef",
    "KeyUsagePropertyFlagsTypeDef",
    "KeyUsagePropertyTypeDef",
    "KeyUsageTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListDirectoryRegistrationsRequestRequestTypeDef",
    "ListDirectoryRegistrationsResponseTypeDef",
    "ListServicePrincipalNamesRequestRequestTypeDef",
    "ListServicePrincipalNamesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateGroupAccessControlEntriesRequestRequestTypeDef",
    "ListTemplateGroupAccessControlEntriesResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateKeyAttributesV2TypeDef",
    "PrivateKeyAttributesV3TypeDef",
    "PrivateKeyAttributesV4TypeDef",
    "PrivateKeyFlagsV2TypeDef",
    "PrivateKeyFlagsV3TypeDef",
    "PrivateKeyFlagsV4TypeDef",
    "ResponseMetadataTypeDef",
    "ServicePrincipalNameSummaryTypeDef",
    "ServicePrincipalNameTypeDef",
    "SubjectNameFlagsV2TypeDef",
    "SubjectNameFlagsV3TypeDef",
    "SubjectNameFlagsV4TypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemplateDefinitionTypeDef",
    "TemplateRevisionTypeDef",
    "TemplateSummaryTypeDef",
    "TemplateTypeDef",
    "TemplateV2TypeDef",
    "TemplateV3TypeDef",
    "TemplateV4TypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "ValidityPeriodTypeDef",
    "VpcInformationTypeDef",
)

AccessControlEntrySummaryTypeDef = TypedDict(
    "AccessControlEntrySummaryTypeDef",
    {
        "AccessRights": "AccessRightsTypeDef",
        "CreatedAt": datetime,
        "GroupDisplayName": str,
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

AccessControlEntryTypeDef = TypedDict(
    "AccessControlEntryTypeDef",
    {
        "AccessRights": "AccessRightsTypeDef",
        "CreatedAt": datetime,
        "GroupDisplayName": str,
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

AccessRightsTypeDef = TypedDict(
    "AccessRightsTypeDef",
    {
        "AutoEnroll": AccessRightType,
        "Enroll": AccessRightType,
    },
    total=False,
)

_RequiredApplicationPoliciesTypeDef = TypedDict(
    "_RequiredApplicationPoliciesTypeDef",
    {
        "Policies": List["ApplicationPolicyTypeDef"],
    },
)
_OptionalApplicationPoliciesTypeDef = TypedDict(
    "_OptionalApplicationPoliciesTypeDef",
    {
        "Critical": bool,
    },
    total=False,
)

class ApplicationPoliciesTypeDef(
    _RequiredApplicationPoliciesTypeDef, _OptionalApplicationPoliciesTypeDef
):
    pass

ApplicationPolicyTypeDef = TypedDict(
    "ApplicationPolicyTypeDef",
    {
        "PolicyObjectIdentifier": str,
        "PolicyType": ApplicationPolicyTypeType,
    },
    total=False,
)

CertificateValidityTypeDef = TypedDict(
    "CertificateValidityTypeDef",
    {
        "RenewalPeriod": "ValidityPeriodTypeDef",
        "ValidityPeriod": "ValidityPeriodTypeDef",
    },
)

ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "Arn": str,
        "CertificateAuthorityArn": str,
        "CertificateEnrollmentPolicyServerEndpoint": str,
        "CreatedAt": datetime,
        "DirectoryId": str,
        "Status": ConnectorStatusType,
        "StatusReason": ConnectorStatusReasonType,
        "UpdatedAt": datetime,
        "VpcInformation": "VpcInformationTypeDef",
    },
    total=False,
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "Arn": str,
        "CertificateAuthorityArn": str,
        "CertificateEnrollmentPolicyServerEndpoint": str,
        "CreatedAt": datetime,
        "DirectoryId": str,
        "Status": ConnectorStatusType,
        "StatusReason": ConnectorStatusReasonType,
        "UpdatedAt": datetime,
        "VpcInformation": "VpcInformationTypeDef",
    },
    total=False,
)

_RequiredCreateConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "DirectoryId": str,
        "VpcInformation": "VpcInformationTypeDef",
    },
)
_OptionalCreateConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateConnectorRequestRequestTypeDef(
    _RequiredCreateConnectorRequestRequestTypeDef, _OptionalCreateConnectorRequestRequestTypeDef
):
    pass

CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "ConnectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDirectoryRegistrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDirectoryRegistrationRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalCreateDirectoryRegistrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDirectoryRegistrationRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDirectoryRegistrationRequestRequestTypeDef(
    _RequiredCreateDirectoryRegistrationRequestRequestTypeDef,
    _OptionalCreateDirectoryRegistrationRequestRequestTypeDef,
):
    pass

CreateDirectoryRegistrationResponseTypeDef = TypedDict(
    "CreateDirectoryRegistrationResponseTypeDef",
    {
        "DirectoryRegistrationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServicePrincipalNameRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServicePrincipalNameRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "DirectoryRegistrationArn": str,
    },
)
_OptionalCreateServicePrincipalNameRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServicePrincipalNameRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreateServicePrincipalNameRequestRequestTypeDef(
    _RequiredCreateServicePrincipalNameRequestRequestTypeDef,
    _OptionalCreateServicePrincipalNameRequestRequestTypeDef,
):
    pass

_RequiredCreateTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "AccessRights": "AccessRightsTypeDef",
        "GroupDisplayName": str,
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
    },
)
_OptionalCreateTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreateTemplateGroupAccessControlEntryRequestRequestTypeDef(
    _RequiredCreateTemplateGroupAccessControlEntryRequestRequestTypeDef,
    _OptionalCreateTemplateGroupAccessControlEntryRequestRequestTypeDef,
):
    pass

_RequiredCreateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTemplateRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "Definition": "TemplateDefinitionTypeDef",
        "Name": str,
    },
)
_OptionalCreateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTemplateRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateTemplateRequestRequestTypeDef(
    _RequiredCreateTemplateRequestRequestTypeDef, _OptionalCreateTemplateRequestRequestTypeDef
):
    pass

CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "TemplateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)

DeleteDirectoryRegistrationRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRegistrationRequestRequestTypeDef",
    {
        "DirectoryRegistrationArn": str,
    },
)

DeleteServicePrincipalNameRequestRequestTypeDef = TypedDict(
    "DeleteServicePrincipalNameRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "DirectoryRegistrationArn": str,
    },
)

DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
    },
)

DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "TemplateArn": str,
    },
)

DirectoryRegistrationSummaryTypeDef = TypedDict(
    "DirectoryRegistrationSummaryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "DirectoryId": str,
        "Status": DirectoryRegistrationStatusType,
        "StatusReason": DirectoryRegistrationStatusReasonType,
        "UpdatedAt": datetime,
    },
    total=False,
)

DirectoryRegistrationTypeDef = TypedDict(
    "DirectoryRegistrationTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "DirectoryId": str,
        "Status": DirectoryRegistrationStatusType,
        "StatusReason": DirectoryRegistrationStatusReasonType,
        "UpdatedAt": datetime,
    },
    total=False,
)

EnrollmentFlagsV2TypeDef = TypedDict(
    "EnrollmentFlagsV2TypeDef",
    {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": bool,
        "IncludeSymmetricAlgorithms": bool,
        "NoSecurityExtension": bool,
        "RemoveInvalidCertificateFromPersonalStore": bool,
        "UserInteractionRequired": bool,
    },
    total=False,
)

EnrollmentFlagsV3TypeDef = TypedDict(
    "EnrollmentFlagsV3TypeDef",
    {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": bool,
        "IncludeSymmetricAlgorithms": bool,
        "NoSecurityExtension": bool,
        "RemoveInvalidCertificateFromPersonalStore": bool,
        "UserInteractionRequired": bool,
    },
    total=False,
)

EnrollmentFlagsV4TypeDef = TypedDict(
    "EnrollmentFlagsV4TypeDef",
    {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": bool,
        "IncludeSymmetricAlgorithms": bool,
        "NoSecurityExtension": bool,
        "RemoveInvalidCertificateFromPersonalStore": bool,
        "UserInteractionRequired": bool,
    },
    total=False,
)

_RequiredExtensionsV2TypeDef = TypedDict(
    "_RequiredExtensionsV2TypeDef",
    {
        "KeyUsage": "KeyUsageTypeDef",
    },
)
_OptionalExtensionsV2TypeDef = TypedDict(
    "_OptionalExtensionsV2TypeDef",
    {
        "ApplicationPolicies": "ApplicationPoliciesTypeDef",
    },
    total=False,
)

class ExtensionsV2TypeDef(_RequiredExtensionsV2TypeDef, _OptionalExtensionsV2TypeDef):
    pass

_RequiredExtensionsV3TypeDef = TypedDict(
    "_RequiredExtensionsV3TypeDef",
    {
        "KeyUsage": "KeyUsageTypeDef",
    },
)
_OptionalExtensionsV3TypeDef = TypedDict(
    "_OptionalExtensionsV3TypeDef",
    {
        "ApplicationPolicies": "ApplicationPoliciesTypeDef",
    },
    total=False,
)

class ExtensionsV3TypeDef(_RequiredExtensionsV3TypeDef, _OptionalExtensionsV3TypeDef):
    pass

_RequiredExtensionsV4TypeDef = TypedDict(
    "_RequiredExtensionsV4TypeDef",
    {
        "KeyUsage": "KeyUsageTypeDef",
    },
)
_OptionalExtensionsV4TypeDef = TypedDict(
    "_OptionalExtensionsV4TypeDef",
    {
        "ApplicationPolicies": "ApplicationPoliciesTypeDef",
    },
    total=False,
)

class ExtensionsV4TypeDef(_RequiredExtensionsV4TypeDef, _OptionalExtensionsV4TypeDef):
    pass

GeneralFlagsV2TypeDef = TypedDict(
    "GeneralFlagsV2TypeDef",
    {
        "AutoEnrollment": bool,
        "MachineType": bool,
    },
    total=False,
)

GeneralFlagsV3TypeDef = TypedDict(
    "GeneralFlagsV3TypeDef",
    {
        "AutoEnrollment": bool,
        "MachineType": bool,
    },
    total=False,
)

GeneralFlagsV4TypeDef = TypedDict(
    "GeneralFlagsV4TypeDef",
    {
        "AutoEnrollment": bool,
        "MachineType": bool,
    },
    total=False,
)

GetConnectorRequestRequestTypeDef = TypedDict(
    "GetConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)

GetConnectorResponseTypeDef = TypedDict(
    "GetConnectorResponseTypeDef",
    {
        "Connector": "ConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDirectoryRegistrationRequestRequestTypeDef = TypedDict(
    "GetDirectoryRegistrationRequestRequestTypeDef",
    {
        "DirectoryRegistrationArn": str,
    },
)

GetDirectoryRegistrationResponseTypeDef = TypedDict(
    "GetDirectoryRegistrationResponseTypeDef",
    {
        "DirectoryRegistration": "DirectoryRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServicePrincipalNameRequestRequestTypeDef = TypedDict(
    "GetServicePrincipalNameRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "DirectoryRegistrationArn": str,
    },
)

GetServicePrincipalNameResponseTypeDef = TypedDict(
    "GetServicePrincipalNameResponseTypeDef",
    {
        "ServicePrincipalName": "ServicePrincipalNameTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "GetTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
    },
)

GetTemplateGroupAccessControlEntryResponseTypeDef = TypedDict(
    "GetTemplateGroupAccessControlEntryResponseTypeDef",
    {
        "AccessControlEntry": "AccessControlEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "TemplateArn": str,
    },
)

GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyUsageFlagsTypeDef = TypedDict(
    "KeyUsageFlagsTypeDef",
    {
        "DataEncipherment": bool,
        "DigitalSignature": bool,
        "KeyAgreement": bool,
        "KeyEncipherment": bool,
        "NonRepudiation": bool,
    },
    total=False,
)

KeyUsagePropertyFlagsTypeDef = TypedDict(
    "KeyUsagePropertyFlagsTypeDef",
    {
        "Decrypt": bool,
        "KeyAgreement": bool,
        "Sign": bool,
    },
    total=False,
)

KeyUsagePropertyTypeDef = TypedDict(
    "KeyUsagePropertyTypeDef",
    {
        "PropertyFlags": "KeyUsagePropertyFlagsTypeDef",
        "PropertyType": Literal["ALL"],
    },
    total=False,
)

_RequiredKeyUsageTypeDef = TypedDict(
    "_RequiredKeyUsageTypeDef",
    {
        "UsageFlags": "KeyUsageFlagsTypeDef",
    },
)
_OptionalKeyUsageTypeDef = TypedDict(
    "_OptionalKeyUsageTypeDef",
    {
        "Critical": bool,
    },
    total=False,
)

class KeyUsageTypeDef(_RequiredKeyUsageTypeDef, _OptionalKeyUsageTypeDef):
    pass

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "Connectors": List["ConnectorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDirectoryRegistrationsRequestRequestTypeDef = TypedDict(
    "ListDirectoryRegistrationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDirectoryRegistrationsResponseTypeDef = TypedDict(
    "ListDirectoryRegistrationsResponseTypeDef",
    {
        "DirectoryRegistrations": List["DirectoryRegistrationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServicePrincipalNamesRequestRequestTypeDef = TypedDict(
    "_RequiredListServicePrincipalNamesRequestRequestTypeDef",
    {
        "DirectoryRegistrationArn": str,
    },
)
_OptionalListServicePrincipalNamesRequestRequestTypeDef = TypedDict(
    "_OptionalListServicePrincipalNamesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServicePrincipalNamesRequestRequestTypeDef(
    _RequiredListServicePrincipalNamesRequestRequestTypeDef,
    _OptionalListServicePrincipalNamesRequestRequestTypeDef,
):
    pass

ListServicePrincipalNamesResponseTypeDef = TypedDict(
    "ListServicePrincipalNamesResponseTypeDef",
    {
        "NextToken": str,
        "ServicePrincipalNames": List["ServicePrincipalNameSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplateGroupAccessControlEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplateGroupAccessControlEntriesRequestRequestTypeDef",
    {
        "TemplateArn": str,
    },
)
_OptionalListTemplateGroupAccessControlEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplateGroupAccessControlEntriesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTemplateGroupAccessControlEntriesRequestRequestTypeDef(
    _RequiredListTemplateGroupAccessControlEntriesRequestRequestTypeDef,
    _OptionalListTemplateGroupAccessControlEntriesRequestRequestTypeDef,
):
    pass

ListTemplateGroupAccessControlEntriesResponseTypeDef = TypedDict(
    "ListTemplateGroupAccessControlEntriesResponseTypeDef",
    {
        "AccessControlEntries": List["AccessControlEntrySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplatesRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)
_OptionalListTemplatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplatesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTemplatesRequestRequestTypeDef(
    _RequiredListTemplatesRequestRequestTypeDef, _OptionalListTemplatesRequestRequestTypeDef
):
    pass

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "NextToken": str,
        "Templates": List["TemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPrivateKeyAttributesV2TypeDef = TypedDict(
    "_RequiredPrivateKeyAttributesV2TypeDef",
    {
        "KeySpec": KeySpecType,
        "MinimalKeyLength": int,
    },
)
_OptionalPrivateKeyAttributesV2TypeDef = TypedDict(
    "_OptionalPrivateKeyAttributesV2TypeDef",
    {
        "CryptoProviders": List[str],
    },
    total=False,
)

class PrivateKeyAttributesV2TypeDef(
    _RequiredPrivateKeyAttributesV2TypeDef, _OptionalPrivateKeyAttributesV2TypeDef
):
    pass

_RequiredPrivateKeyAttributesV3TypeDef = TypedDict(
    "_RequiredPrivateKeyAttributesV3TypeDef",
    {
        "Algorithm": PrivateKeyAlgorithmType,
        "KeySpec": KeySpecType,
        "KeyUsageProperty": "KeyUsagePropertyTypeDef",
        "MinimalKeyLength": int,
    },
)
_OptionalPrivateKeyAttributesV3TypeDef = TypedDict(
    "_OptionalPrivateKeyAttributesV3TypeDef",
    {
        "CryptoProviders": List[str],
    },
    total=False,
)

class PrivateKeyAttributesV3TypeDef(
    _RequiredPrivateKeyAttributesV3TypeDef, _OptionalPrivateKeyAttributesV3TypeDef
):
    pass

_RequiredPrivateKeyAttributesV4TypeDef = TypedDict(
    "_RequiredPrivateKeyAttributesV4TypeDef",
    {
        "KeySpec": KeySpecType,
        "MinimalKeyLength": int,
    },
)
_OptionalPrivateKeyAttributesV4TypeDef = TypedDict(
    "_OptionalPrivateKeyAttributesV4TypeDef",
    {
        "Algorithm": PrivateKeyAlgorithmType,
        "CryptoProviders": List[str],
        "KeyUsageProperty": "KeyUsagePropertyTypeDef",
    },
    total=False,
)

class PrivateKeyAttributesV4TypeDef(
    _RequiredPrivateKeyAttributesV4TypeDef, _OptionalPrivateKeyAttributesV4TypeDef
):
    pass

_RequiredPrivateKeyFlagsV2TypeDef = TypedDict(
    "_RequiredPrivateKeyFlagsV2TypeDef",
    {
        "ClientVersion": ClientCompatibilityV2Type,
    },
)
_OptionalPrivateKeyFlagsV2TypeDef = TypedDict(
    "_OptionalPrivateKeyFlagsV2TypeDef",
    {
        "ExportableKey": bool,
        "StrongKeyProtectionRequired": bool,
    },
    total=False,
)

class PrivateKeyFlagsV2TypeDef(
    _RequiredPrivateKeyFlagsV2TypeDef, _OptionalPrivateKeyFlagsV2TypeDef
):
    pass

_RequiredPrivateKeyFlagsV3TypeDef = TypedDict(
    "_RequiredPrivateKeyFlagsV3TypeDef",
    {
        "ClientVersion": ClientCompatibilityV3Type,
    },
)
_OptionalPrivateKeyFlagsV3TypeDef = TypedDict(
    "_OptionalPrivateKeyFlagsV3TypeDef",
    {
        "ExportableKey": bool,
        "RequireAlternateSignatureAlgorithm": bool,
        "StrongKeyProtectionRequired": bool,
    },
    total=False,
)

class PrivateKeyFlagsV3TypeDef(
    _RequiredPrivateKeyFlagsV3TypeDef, _OptionalPrivateKeyFlagsV3TypeDef
):
    pass

_RequiredPrivateKeyFlagsV4TypeDef = TypedDict(
    "_RequiredPrivateKeyFlagsV4TypeDef",
    {
        "ClientVersion": ClientCompatibilityV4Type,
    },
)
_OptionalPrivateKeyFlagsV4TypeDef = TypedDict(
    "_OptionalPrivateKeyFlagsV4TypeDef",
    {
        "ExportableKey": bool,
        "RequireAlternateSignatureAlgorithm": bool,
        "RequireSameKeyRenewal": bool,
        "StrongKeyProtectionRequired": bool,
        "UseLegacyProvider": bool,
    },
    total=False,
)

class PrivateKeyFlagsV4TypeDef(
    _RequiredPrivateKeyFlagsV4TypeDef, _OptionalPrivateKeyFlagsV4TypeDef
):
    pass

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

ServicePrincipalNameSummaryTypeDef = TypedDict(
    "ServicePrincipalNameSummaryTypeDef",
    {
        "ConnectorArn": str,
        "CreatedAt": datetime,
        "DirectoryRegistrationArn": str,
        "Status": ServicePrincipalNameStatusType,
        "StatusReason": ServicePrincipalNameStatusReasonType,
        "UpdatedAt": datetime,
    },
    total=False,
)

ServicePrincipalNameTypeDef = TypedDict(
    "ServicePrincipalNameTypeDef",
    {
        "ConnectorArn": str,
        "CreatedAt": datetime,
        "DirectoryRegistrationArn": str,
        "Status": ServicePrincipalNameStatusType,
        "StatusReason": ServicePrincipalNameStatusReasonType,
        "UpdatedAt": datetime,
    },
    total=False,
)

SubjectNameFlagsV2TypeDef = TypedDict(
    "SubjectNameFlagsV2TypeDef",
    {
        "RequireCommonName": bool,
        "RequireDirectoryPath": bool,
        "RequireDnsAsCn": bool,
        "RequireEmail": bool,
        "SanRequireDirectoryGuid": bool,
        "SanRequireDns": bool,
        "SanRequireDomainDns": bool,
        "SanRequireEmail": bool,
        "SanRequireSpn": bool,
        "SanRequireUpn": bool,
    },
    total=False,
)

SubjectNameFlagsV3TypeDef = TypedDict(
    "SubjectNameFlagsV3TypeDef",
    {
        "RequireCommonName": bool,
        "RequireDirectoryPath": bool,
        "RequireDnsAsCn": bool,
        "RequireEmail": bool,
        "SanRequireDirectoryGuid": bool,
        "SanRequireDns": bool,
        "SanRequireDomainDns": bool,
        "SanRequireEmail": bool,
        "SanRequireSpn": bool,
        "SanRequireUpn": bool,
    },
    total=False,
)

SubjectNameFlagsV4TypeDef = TypedDict(
    "SubjectNameFlagsV4TypeDef",
    {
        "RequireCommonName": bool,
        "RequireDirectoryPath": bool,
        "RequireDnsAsCn": bool,
        "RequireEmail": bool,
        "SanRequireDirectoryGuid": bool,
        "SanRequireDns": bool,
        "SanRequireDomainDns": bool,
        "SanRequireEmail": bool,
        "SanRequireSpn": bool,
        "SanRequireUpn": bool,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TemplateDefinitionTypeDef = TypedDict(
    "TemplateDefinitionTypeDef",
    {
        "TemplateV2": "TemplateV2TypeDef",
        "TemplateV3": "TemplateV3TypeDef",
        "TemplateV4": "TemplateV4TypeDef",
    },
    total=False,
)

TemplateRevisionTypeDef = TypedDict(
    "TemplateRevisionTypeDef",
    {
        "MajorRevision": int,
        "MinorRevision": int,
    },
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "Arn": str,
        "ConnectorArn": str,
        "CreatedAt": datetime,
        "Definition": "TemplateDefinitionTypeDef",
        "Name": str,
        "ObjectIdentifier": str,
        "PolicySchema": int,
        "Revision": "TemplateRevisionTypeDef",
        "Status": TemplateStatusType,
        "UpdatedAt": datetime,
    },
    total=False,
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Arn": str,
        "ConnectorArn": str,
        "CreatedAt": datetime,
        "Definition": "TemplateDefinitionTypeDef",
        "Name": str,
        "ObjectIdentifier": str,
        "PolicySchema": int,
        "Revision": "TemplateRevisionTypeDef",
        "Status": TemplateStatusType,
        "UpdatedAt": datetime,
    },
    total=False,
)

_RequiredTemplateV2TypeDef = TypedDict(
    "_RequiredTemplateV2TypeDef",
    {
        "CertificateValidity": "CertificateValidityTypeDef",
        "EnrollmentFlags": "EnrollmentFlagsV2TypeDef",
        "Extensions": "ExtensionsV2TypeDef",
        "GeneralFlags": "GeneralFlagsV2TypeDef",
        "PrivateKeyAttributes": "PrivateKeyAttributesV2TypeDef",
        "PrivateKeyFlags": "PrivateKeyFlagsV2TypeDef",
        "SubjectNameFlags": "SubjectNameFlagsV2TypeDef",
    },
)
_OptionalTemplateV2TypeDef = TypedDict(
    "_OptionalTemplateV2TypeDef",
    {
        "SupersededTemplates": List[str],
    },
    total=False,
)

class TemplateV2TypeDef(_RequiredTemplateV2TypeDef, _OptionalTemplateV2TypeDef):
    pass

_RequiredTemplateV3TypeDef = TypedDict(
    "_RequiredTemplateV3TypeDef",
    {
        "CertificateValidity": "CertificateValidityTypeDef",
        "EnrollmentFlags": "EnrollmentFlagsV3TypeDef",
        "Extensions": "ExtensionsV3TypeDef",
        "GeneralFlags": "GeneralFlagsV3TypeDef",
        "HashAlgorithm": HashAlgorithmType,
        "PrivateKeyAttributes": "PrivateKeyAttributesV3TypeDef",
        "PrivateKeyFlags": "PrivateKeyFlagsV3TypeDef",
        "SubjectNameFlags": "SubjectNameFlagsV3TypeDef",
    },
)
_OptionalTemplateV3TypeDef = TypedDict(
    "_OptionalTemplateV3TypeDef",
    {
        "SupersededTemplates": List[str],
    },
    total=False,
)

class TemplateV3TypeDef(_RequiredTemplateV3TypeDef, _OptionalTemplateV3TypeDef):
    pass

_RequiredTemplateV4TypeDef = TypedDict(
    "_RequiredTemplateV4TypeDef",
    {
        "CertificateValidity": "CertificateValidityTypeDef",
        "EnrollmentFlags": "EnrollmentFlagsV4TypeDef",
        "Extensions": "ExtensionsV4TypeDef",
        "GeneralFlags": "GeneralFlagsV4TypeDef",
        "PrivateKeyAttributes": "PrivateKeyAttributesV4TypeDef",
        "PrivateKeyFlags": "PrivateKeyFlagsV4TypeDef",
        "SubjectNameFlags": "SubjectNameFlagsV4TypeDef",
    },
)
_OptionalTemplateV4TypeDef = TypedDict(
    "_OptionalTemplateV4TypeDef",
    {
        "HashAlgorithm": HashAlgorithmType,
        "SupersededTemplates": List[str],
    },
    total=False,
)

class TemplateV4TypeDef(_RequiredTemplateV4TypeDef, _OptionalTemplateV4TypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
    },
)
_OptionalUpdateTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "AccessRights": "AccessRightsTypeDef",
        "GroupDisplayName": str,
    },
    total=False,
)

class UpdateTemplateGroupAccessControlEntryRequestRequestTypeDef(
    _RequiredUpdateTemplateGroupAccessControlEntryRequestRequestTypeDef,
    _OptionalUpdateTemplateGroupAccessControlEntryRequestRequestTypeDef,
):
    pass

_RequiredUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplateRequestRequestTypeDef",
    {
        "TemplateArn": str,
    },
)
_OptionalUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplateRequestRequestTypeDef",
    {
        "Definition": "TemplateDefinitionTypeDef",
        "ReenrollAllCertificateHolders": bool,
    },
    total=False,
)

class UpdateTemplateRequestRequestTypeDef(
    _RequiredUpdateTemplateRequestRequestTypeDef, _OptionalUpdateTemplateRequestRequestTypeDef
):
    pass

ValidityPeriodTypeDef = TypedDict(
    "ValidityPeriodTypeDef",
    {
        "Period": int,
        "PeriodType": ValidityPeriodTypeType,
    },
)

VpcInformationTypeDef = TypedDict(
    "VpcInformationTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
)
