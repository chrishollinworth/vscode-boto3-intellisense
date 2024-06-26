"""
Type annotations for transfer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/literals.html)

Usage::

    ```python
    from mypy_boto3_transfer.literals import AgreementStatusTypeType

    data: AgreementStatusTypeType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AgreementStatusTypeType",
    "As2TransportType",
    "CertificateStatusTypeType",
    "CertificateTypeType",
    "CertificateUsageTypeType",
    "CompressionEnumType",
    "CustomStepStatusType",
    "DirectoryListingOptimizationType",
    "DomainType",
    "EncryptionAlgType",
    "EncryptionTypeType",
    "EndpointTypeType",
    "ExecutionErrorTypeType",
    "ExecutionStatusType",
    "HomeDirectoryTypeType",
    "IdentityProviderTypeType",
    "ListAccessesPaginatorName",
    "ListAgreementsPaginatorName",
    "ListCertificatesPaginatorName",
    "ListConnectorsPaginatorName",
    "ListExecutionsPaginatorName",
    "ListProfilesPaginatorName",
    "ListSecurityPoliciesPaginatorName",
    "ListServersPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListUsersPaginatorName",
    "ListWorkflowsPaginatorName",
    "MapTypeType",
    "MdnResponseType",
    "MdnSigningAlgType",
    "OverwriteExistingType",
    "ProfileTypeType",
    "ProtocolType",
    "SecurityPolicyProtocolType",
    "SecurityPolicyResourceTypeType",
    "ServerOfflineWaiterName",
    "ServerOnlineWaiterName",
    "SetStatOptionType",
    "SftpAuthenticationMethodsType",
    "SigningAlgType",
    "StateType",
    "TlsSessionResumptionModeType",
    "WorkflowStepTypeType",
)

AgreementStatusTypeType = Literal["ACTIVE", "INACTIVE"]
As2TransportType = Literal["HTTP"]
CertificateStatusTypeType = Literal["ACTIVE", "INACTIVE", "PENDING_ROTATION"]
CertificateTypeType = Literal["CERTIFICATE", "CERTIFICATE_WITH_PRIVATE_KEY"]
CertificateUsageTypeType = Literal["ENCRYPTION", "SIGNING", "TLS"]
CompressionEnumType = Literal["DISABLED", "ZLIB"]
CustomStepStatusType = Literal["FAILURE", "SUCCESS"]
DirectoryListingOptimizationType = Literal["DISABLED", "ENABLED"]
DomainType = Literal["EFS", "S3"]
EncryptionAlgType = Literal["AES128_CBC", "AES192_CBC", "AES256_CBC", "DES_EDE3_CBC", "NONE"]
EncryptionTypeType = Literal["PGP"]
EndpointTypeType = Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]
ExecutionErrorTypeType = Literal[
    "ALREADY_EXISTS",
    "BAD_REQUEST",
    "CUSTOM_STEP_FAILED",
    "INTERNAL_SERVER_ERROR",
    "NOT_FOUND",
    "PERMISSION_DENIED",
    "THROTTLED",
    "TIMEOUT",
]
ExecutionStatusType = Literal["COMPLETED", "EXCEPTION", "HANDLING_EXCEPTION", "IN_PROGRESS"]
HomeDirectoryTypeType = Literal["LOGICAL", "PATH"]
IdentityProviderTypeType = Literal[
    "API_GATEWAY", "AWS_DIRECTORY_SERVICE", "AWS_LAMBDA", "SERVICE_MANAGED"
]
ListAccessesPaginatorName = Literal["list_accesses"]
ListAgreementsPaginatorName = Literal["list_agreements"]
ListCertificatesPaginatorName = Literal["list_certificates"]
ListConnectorsPaginatorName = Literal["list_connectors"]
ListExecutionsPaginatorName = Literal["list_executions"]
ListProfilesPaginatorName = Literal["list_profiles"]
ListSecurityPoliciesPaginatorName = Literal["list_security_policies"]
ListServersPaginatorName = Literal["list_servers"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListUsersPaginatorName = Literal["list_users"]
ListWorkflowsPaginatorName = Literal["list_workflows"]
MapTypeType = Literal["DIRECTORY", "FILE"]
MdnResponseType = Literal["NONE", "SYNC"]
MdnSigningAlgType = Literal["DEFAULT", "NONE", "SHA1", "SHA256", "SHA384", "SHA512"]
OverwriteExistingType = Literal["FALSE", "TRUE"]
ProfileTypeType = Literal["LOCAL", "PARTNER"]
ProtocolType = Literal["AS2", "FTP", "FTPS", "SFTP"]
SecurityPolicyProtocolType = Literal["FTPS", "SFTP"]
SecurityPolicyResourceTypeType = Literal["CONNECTOR", "SERVER"]
ServerOfflineWaiterName = Literal["server_offline"]
ServerOnlineWaiterName = Literal["server_online"]
SetStatOptionType = Literal["DEFAULT", "ENABLE_NO_OP"]
SftpAuthenticationMethodsType = Literal[
    "PASSWORD", "PUBLIC_KEY", "PUBLIC_KEY_AND_PASSWORD", "PUBLIC_KEY_OR_PASSWORD"
]
SigningAlgType = Literal["NONE", "SHA1", "SHA256", "SHA384", "SHA512"]
StateType = Literal["OFFLINE", "ONLINE", "STARTING", "START_FAILED", "STOPPING", "STOP_FAILED"]
TlsSessionResumptionModeType = Literal["DISABLED", "ENABLED", "ENFORCED"]
WorkflowStepTypeType = Literal["COPY", "CUSTOM", "DECRYPT", "DELETE", "TAG"]
