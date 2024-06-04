"""
Type annotations for pca-connector-ad service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/literals.html)

Usage::

    ```python
    from mypy_boto3_pca_connector_ad.literals import AccessRightType

    data: AccessRightType = "ALLOW"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessRightType",
    "ApplicationPolicyTypeType",
    "ClientCompatibilityV2Type",
    "ClientCompatibilityV3Type",
    "ClientCompatibilityV4Type",
    "ConnectorStatusReasonType",
    "ConnectorStatusType",
    "DirectoryRegistrationStatusReasonType",
    "DirectoryRegistrationStatusType",
    "HashAlgorithmType",
    "KeySpecType",
    "KeyUsagePropertyTypeType",
    "ListConnectorsPaginatorName",
    "ListDirectoryRegistrationsPaginatorName",
    "ListServicePrincipalNamesPaginatorName",
    "ListTemplateGroupAccessControlEntriesPaginatorName",
    "ListTemplatesPaginatorName",
    "PrivateKeyAlgorithmType",
    "ServicePrincipalNameStatusReasonType",
    "ServicePrincipalNameStatusType",
    "TemplateStatusType",
    "ValidityPeriodTypeType",
)

AccessRightType = Literal["ALLOW", "DENY"]
ApplicationPolicyTypeType = Literal[
    "ALL_APPLICATION_POLICIES",
    "ANY_PURPOSE",
    "ATTESTATION_IDENTITY_KEY_CERTIFICATE",
    "CERTIFICATE_REQUEST_AGENT",
    "CLIENT_AUTHENTICATION",
    "CODE_SIGNING",
    "CTL_USAGE",
    "DIGITAL_RIGHTS",
    "DIRECTORY_SERVICE_EMAIL_REPLICATION",
    "DISALLOWED_LIST",
    "DNS_SERVER_TRUST",
    "DOCUMENT_ENCRYPTION",
    "DOCUMENT_SIGNING",
    "DYNAMIC_CODE_GENERATOR",
    "EARLY_LAUNCH_ANTIMALWARE_DRIVER",
    "EMBEDDED_WINDOWS_SYSTEM_COMPONENT_VERIFICATION",
    "ENCLAVE",
    "ENCRYPTING_FILE_SYSTEM",
    "ENDORSEMENT_KEY_CERTIFICATE",
    "FILE_RECOVERY",
    "HAL_EXTENSION",
    "IP_SECURITY_END_SYSTEM",
    "IP_SECURITY_IKE_INTERMEDIATE",
    "IP_SECURITY_TUNNEL_TERMINATION",
    "IP_SECURITY_USER",
    "ISOLATED_USER_MODE",
    "KDC_AUTHENTICATION",
    "KERNEL_MODE_CODE_SIGNING",
    "KEY_PACK_LICENSES",
    "KEY_RECOVERY",
    "KEY_RECOVERY_AGENT",
    "LICENSE_SERVER_VERIFICATION",
    "LIFETIME_SIGNING",
    "MICROSOFT_PUBLISHER",
    "MICROSOFT_TIME_STAMPING",
    "MICROSOFT_TRUST_LIST_SIGNING",
    "OCSP_SIGNING",
    "OEM_WINDOWS_SYSTEM_COMPONENT_VERIFICATION",
    "PLATFORM_CERTIFICATE",
    "PREVIEW_BUILD_SIGNING",
    "PRIVATE_KEY_ARCHIVAL",
    "PROTECTED_PROCESS_LIGHT_VERIFICATION",
    "PROTECTED_PROCESS_VERIFICATION",
    "QUALIFIED_SUBORDINATION",
    "REVOKED_LIST_SIGNER",
    "ROOT_LIST_SIGNER",
    "ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION",
    "ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION",
    "ROOT_PROGRAM_NO_OSCP_FAILOVER_TO_CRL",
    "SECURE_EMAIL",
    "SERVER_AUTHENTICATION",
    "SMART_CARD_LOGIN",
    "SPC_ENCRYPTED_DIGEST_RETRY_COUNT",
    "SPC_RELAXED_PE_MARKER_CHECK",
    "TIME_STAMPING",
    "WINDOWS_HARDWARE_DRIVER_ATTESTED_VERIFICATION",
    "WINDOWS_HARDWARE_DRIVER_EXTENDED_VERIFICATION",
    "WINDOWS_HARDWARE_DRIVER_VERIFICATION",
    "WINDOWS_HELLO_RECOVERY_KEY_ENCRYPTION",
    "WINDOWS_KITS_COMPONENT",
    "WINDOWS_RT_VERIFICATION",
    "WINDOWS_SOFTWARE_EXTENSION_VERIFICATION",
    "WINDOWS_STORE",
    "WINDOWS_SYSTEM_COMPONENT_VERIFICATION",
    "WINDOWS_TCB_COMPONENT",
    "WINDOWS_THIRD_PARTY_APPLICATION_COMPONENT",
    "WINDOWS_UPDATE",
]
ClientCompatibilityV2Type = Literal[
    "WINDOWS_SERVER_2003",
    "WINDOWS_SERVER_2008",
    "WINDOWS_SERVER_2008_R2",
    "WINDOWS_SERVER_2012",
    "WINDOWS_SERVER_2012_R2",
    "WINDOWS_SERVER_2016",
]
ClientCompatibilityV3Type = Literal[
    "WINDOWS_SERVER_2008",
    "WINDOWS_SERVER_2008_R2",
    "WINDOWS_SERVER_2012",
    "WINDOWS_SERVER_2012_R2",
    "WINDOWS_SERVER_2016",
]
ClientCompatibilityV4Type = Literal[
    "WINDOWS_SERVER_2012", "WINDOWS_SERVER_2012_R2", "WINDOWS_SERVER_2016"
]
ConnectorStatusReasonType = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "INTERNAL_FAILURE",
    "PRIVATECA_ACCESS_DENIED",
    "PRIVATECA_RESOURCE_NOT_FOUND",
    "SECURITY_GROUP_NOT_IN_VPC",
    "VPC_ACCESS_DENIED",
    "VPC_ENDPOINT_LIMIT_EXCEEDED",
    "VPC_RESOURCE_NOT_FOUND",
]
ConnectorStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
DirectoryRegistrationStatusReasonType = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_NOT_ACTIVE",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "DIRECTORY_TYPE_NOT_SUPPORTED",
    "INTERNAL_FAILURE",
]
DirectoryRegistrationStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
HashAlgorithmType = Literal["SHA256", "SHA384", "SHA512"]
KeySpecType = Literal["KEY_EXCHANGE", "SIGNATURE"]
KeyUsagePropertyTypeType = Literal["ALL"]
ListConnectorsPaginatorName = Literal["list_connectors"]
ListDirectoryRegistrationsPaginatorName = Literal["list_directory_registrations"]
ListServicePrincipalNamesPaginatorName = Literal["list_service_principal_names"]
ListTemplateGroupAccessControlEntriesPaginatorName = Literal[
    "list_template_group_access_control_entries"
]
ListTemplatesPaginatorName = Literal["list_templates"]
PrivateKeyAlgorithmType = Literal["ECDH_P256", "ECDH_P384", "ECDH_P521", "RSA"]
ServicePrincipalNameStatusReasonType = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "INTERNAL_FAILURE",
    "SPN_EXISTS_ON_DIFFERENT_AD_OBJECT",
]
ServicePrincipalNameStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
TemplateStatusType = Literal["ACTIVE", "DELETING"]
ValidityPeriodTypeType = Literal["DAYS", "HOURS", "MONTHS", "WEEKS", "YEARS"]
