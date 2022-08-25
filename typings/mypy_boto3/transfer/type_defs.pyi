"""
Type annotations for transfer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_transfer.type_defs import As2ConnectorConfigTypeDef

    data: As2ConnectorConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgreementStatusTypeType,
    CertificateStatusTypeType,
    CertificateTypeType,
    CertificateUsageTypeType,
    CompressionEnumType,
    CustomStepStatusType,
    DomainType,
    EncryptionAlgType,
    EndpointTypeType,
    ExecutionErrorTypeType,
    ExecutionStatusType,
    HomeDirectoryTypeType,
    IdentityProviderTypeType,
    MdnResponseType,
    MdnSigningAlgType,
    OverwriteExistingType,
    ProfileTypeType,
    ProtocolType,
    SetStatOptionType,
    SigningAlgType,
    StateType,
    TlsSessionResumptionModeType,
    WorkflowStepTypeType,
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
    "As2ConnectorConfigTypeDef",
    "CopyStepDetailsTypeDef",
    "CreateAccessRequestRequestTypeDef",
    "CreateAccessResponseTypeDef",
    "CreateAgreementRequestRequestTypeDef",
    "CreateAgreementResponseTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateServerRequestRequestTypeDef",
    "CreateServerResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CustomStepDetailsTypeDef",
    "DeleteAccessRequestRequestTypeDef",
    "DeleteAgreementRequestRequestTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteServerRequestRequestTypeDef",
    "DeleteSshPublicKeyRequestRequestTypeDef",
    "DeleteStepDetailsTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DescribeAccessRequestRequestTypeDef",
    "DescribeAccessResponseTypeDef",
    "DescribeAgreementRequestRequestTypeDef",
    "DescribeAgreementResponseTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeExecutionRequestRequestTypeDef",
    "DescribeExecutionResponseTypeDef",
    "DescribeProfileRequestRequestTypeDef",
    "DescribeProfileResponseTypeDef",
    "DescribeSecurityPolicyRequestRequestTypeDef",
    "DescribeSecurityPolicyResponseTypeDef",
    "DescribeServerRequestRequestTypeDef",
    "DescribeServerResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribeWorkflowRequestRequestTypeDef",
    "DescribeWorkflowResponseTypeDef",
    "DescribedAccessTypeDef",
    "DescribedAgreementTypeDef",
    "DescribedCertificateTypeDef",
    "DescribedConnectorTypeDef",
    "DescribedExecutionTypeDef",
    "DescribedProfileTypeDef",
    "DescribedSecurityPolicyTypeDef",
    "DescribedServerTypeDef",
    "DescribedUserTypeDef",
    "DescribedWorkflowTypeDef",
    "EfsFileLocationTypeDef",
    "EndpointDetailsTypeDef",
    "ExecutionErrorTypeDef",
    "ExecutionResultsTypeDef",
    "ExecutionStepResultTypeDef",
    "FileLocationTypeDef",
    "HomeDirectoryMapEntryTypeDef",
    "IdentityProviderDetailsTypeDef",
    "ImportCertificateRequestRequestTypeDef",
    "ImportCertificateResponseTypeDef",
    "ImportSshPublicKeyRequestRequestTypeDef",
    "ImportSshPublicKeyResponseTypeDef",
    "InputFileLocationTypeDef",
    "ListAccessesRequestRequestTypeDef",
    "ListAccessesResponseTypeDef",
    "ListAgreementsRequestRequestTypeDef",
    "ListAgreementsResponseTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListExecutionsRequestRequestTypeDef",
    "ListExecutionsResponseTypeDef",
    "ListProfilesRequestRequestTypeDef",
    "ListProfilesResponseTypeDef",
    "ListSecurityPoliciesRequestRequestTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "ListServersRequestRequestTypeDef",
    "ListServersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "ListedAccessTypeDef",
    "ListedAgreementTypeDef",
    "ListedCertificateTypeDef",
    "ListedConnectorTypeDef",
    "ListedExecutionTypeDef",
    "ListedProfileTypeDef",
    "ListedServerTypeDef",
    "ListedUserTypeDef",
    "ListedWorkflowTypeDef",
    "LoggingConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PosixProfileTypeDef",
    "ProtocolDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "S3FileLocationTypeDef",
    "S3InputFileLocationTypeDef",
    "S3TagTypeDef",
    "SendWorkflowStepStateRequestRequestTypeDef",
    "ServiceMetadataTypeDef",
    "SshPublicKeyTypeDef",
    "StartFileTransferRequestRequestTypeDef",
    "StartFileTransferResponseTypeDef",
    "StartServerRequestRequestTypeDef",
    "StopServerRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagStepDetailsTypeDef",
    "TagTypeDef",
    "TestIdentityProviderRequestRequestTypeDef",
    "TestIdentityProviderResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessRequestRequestTypeDef",
    "UpdateAccessResponseTypeDef",
    "UpdateAgreementRequestRequestTypeDef",
    "UpdateAgreementResponseTypeDef",
    "UpdateCertificateRequestRequestTypeDef",
    "UpdateCertificateResponseTypeDef",
    "UpdateConnectorRequestRequestTypeDef",
    "UpdateConnectorResponseTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "UpdateProfileResponseTypeDef",
    "UpdateServerRequestRequestTypeDef",
    "UpdateServerResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UserDetailsTypeDef",
    "WaiterConfigTypeDef",
    "WorkflowDetailTypeDef",
    "WorkflowDetailsTypeDef",
    "WorkflowStepTypeDef",
)

As2ConnectorConfigTypeDef = TypedDict(
    "As2ConnectorConfigTypeDef",
    {
        "LocalProfileId": str,
        "PartnerProfileId": str,
        "MessageSubject": str,
        "Compression": CompressionEnumType,
        "EncryptionAlgorithm": EncryptionAlgType,
        "SigningAlgorithm": SigningAlgType,
        "MdnSigningAlgorithm": MdnSigningAlgType,
        "MdnResponse": MdnResponseType,
    },
    total=False,
)

CopyStepDetailsTypeDef = TypedDict(
    "CopyStepDetailsTypeDef",
    {
        "Name": str,
        "DestinationFileLocation": "InputFileLocationTypeDef",
        "OverwriteExisting": OverwriteExistingType,
        "SourceFileLocation": str,
    },
    total=False,
)

_RequiredCreateAccessRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "ExternalId": str,
    },
)
_OptionalCreateAccessRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
    },
    total=False,
)

class CreateAccessRequestRequestTypeDef(
    _RequiredCreateAccessRequestRequestTypeDef, _OptionalCreateAccessRequestRequestTypeDef
):
    pass

CreateAccessResponseTypeDef = TypedDict(
    "CreateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAgreementRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgreementRequestRequestTypeDef",
    {
        "ServerId": str,
        "LocalProfileId": str,
        "PartnerProfileId": str,
        "BaseDirectory": str,
        "AccessRole": str,
    },
)
_OptionalCreateAgreementRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgreementRequestRequestTypeDef",
    {
        "Description": str,
        "Status": AgreementStatusTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAgreementRequestRequestTypeDef(
    _RequiredCreateAgreementRequestRequestTypeDef, _OptionalCreateAgreementRequestRequestTypeDef
):
    pass

CreateAgreementResponseTypeDef = TypedDict(
    "CreateAgreementResponseTypeDef",
    {
        "AgreementId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorRequestRequestTypeDef",
    {
        "Url": str,
        "As2Config": "As2ConnectorConfigTypeDef",
        "AccessRole": str,
    },
)
_OptionalCreateConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorRequestRequestTypeDef",
    {
        "LoggingRole": str,
        "Tags": List["TagTypeDef"],
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
        "ConnectorId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestRequestTypeDef",
    {
        "As2Id": str,
        "ProfileType": ProfileTypeType,
    },
)
_OptionalCreateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestRequestTypeDef",
    {
        "CertificateIds": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProfileRequestRequestTypeDef(
    _RequiredCreateProfileRequestRequestTypeDef, _OptionalCreateProfileRequestRequestTypeDef
):
    pass

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServerRequestRequestTypeDef = TypedDict(
    "CreateServerRequestRequestTypeDef",
    {
        "Certificate": str,
        "Domain": DomainType,
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKey": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "IdentityProviderType": IdentityProviderTypeType,
        "LoggingRole": str,
        "PostAuthenticationLoginBanner": str,
        "PreAuthenticationLoginBanner": str,
        "Protocols": List[ProtocolType],
        "ProtocolDetails": "ProtocolDetailsTypeDef",
        "SecurityPolicyName": str,
        "Tags": List["TagTypeDef"],
        "WorkflowDetails": "WorkflowDetailsTypeDef",
    },
    total=False,
)

CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "SshPublicKeyBody": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkflowRequestRequestTypeDef",
    {
        "Steps": List["WorkflowStepTypeDef"],
    },
)
_OptionalCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkflowRequestRequestTypeDef",
    {
        "Description": str,
        "OnExceptionSteps": List["WorkflowStepTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWorkflowRequestRequestTypeDef(
    _RequiredCreateWorkflowRequestRequestTypeDef, _OptionalCreateWorkflowRequestRequestTypeDef
):
    pass

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomStepDetailsTypeDef = TypedDict(
    "CustomStepDetailsTypeDef",
    {
        "Name": str,
        "Target": str,
        "TimeoutSeconds": int,
        "SourceFileLocation": str,
    },
    total=False,
)

DeleteAccessRequestRequestTypeDef = TypedDict(
    "DeleteAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DeleteAgreementRequestRequestTypeDef = TypedDict(
    "DeleteAgreementRequestRequestTypeDef",
    {
        "AgreementId": str,
        "ServerId": str,
    },
)

DeleteCertificateRequestRequestTypeDef = TypedDict(
    "DeleteCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
    },
)

DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "ConnectorId": str,
    },
)

DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)

DeleteServerRequestRequestTypeDef = TypedDict(
    "DeleteServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

DeleteSshPublicKeyRequestRequestTypeDef = TypedDict(
    "DeleteSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
    },
)

DeleteStepDetailsTypeDef = TypedDict(
    "DeleteStepDetailsTypeDef",
    {
        "Name": str,
        "SourceFileLocation": str,
    },
    total=False,
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "WorkflowId": str,
    },
)

DescribeAccessRequestRequestTypeDef = TypedDict(
    "DescribeAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DescribeAccessResponseTypeDef = TypedDict(
    "DescribeAccessResponseTypeDef",
    {
        "ServerId": str,
        "Access": "DescribedAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAgreementRequestRequestTypeDef = TypedDict(
    "DescribeAgreementRequestRequestTypeDef",
    {
        "AgreementId": str,
        "ServerId": str,
    },
)

DescribeAgreementResponseTypeDef = TypedDict(
    "DescribeAgreementResponseTypeDef",
    {
        "Agreement": "DescribedAgreementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
    },
)

DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef",
    {
        "Certificate": "DescribedCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorRequestRequestTypeDef = TypedDict(
    "DescribeConnectorRequestRequestTypeDef",
    {
        "ConnectorId": str,
    },
)

DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "Connector": "DescribedConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExecutionRequestRequestTypeDef = TypedDict(
    "DescribeExecutionRequestRequestTypeDef",
    {
        "ExecutionId": str,
        "WorkflowId": str,
    },
)

DescribeExecutionResponseTypeDef = TypedDict(
    "DescribeExecutionResponseTypeDef",
    {
        "WorkflowId": str,
        "Execution": "DescribedExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProfileRequestRequestTypeDef = TypedDict(
    "DescribeProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)

DescribeProfileResponseTypeDef = TypedDict(
    "DescribeProfileResponseTypeDef",
    {
        "Profile": "DescribedProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityPolicyRequestRequestTypeDef = TypedDict(
    "DescribeSecurityPolicyRequestRequestTypeDef",
    {
        "SecurityPolicyName": str,
    },
)

DescribeSecurityPolicyResponseTypeDef = TypedDict(
    "DescribeSecurityPolicyResponseTypeDef",
    {
        "SecurityPolicy": "DescribedSecurityPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServerRequestRequestTypeDef = TypedDict(
    "DescribeServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

DescribeServerResponseTypeDef = TypedDict(
    "DescribeServerResponseTypeDef",
    {
        "Server": "DescribedServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "ServerId": str,
        "User": "DescribedUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkflowRequestRequestTypeDef = TypedDict(
    "DescribeWorkflowRequestRequestTypeDef",
    {
        "WorkflowId": str,
    },
)

DescribeWorkflowResponseTypeDef = TypedDict(
    "DescribeWorkflowResponseTypeDef",
    {
        "Workflow": "DescribedWorkflowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribedAccessTypeDef = TypedDict(
    "DescribedAccessTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
        "ExternalId": str,
    },
    total=False,
)

_RequiredDescribedAgreementTypeDef = TypedDict(
    "_RequiredDescribedAgreementTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedAgreementTypeDef = TypedDict(
    "_OptionalDescribedAgreementTypeDef",
    {
        "AgreementId": str,
        "Description": str,
        "Status": AgreementStatusTypeType,
        "ServerId": str,
        "LocalProfileId": str,
        "PartnerProfileId": str,
        "BaseDirectory": str,
        "AccessRole": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class DescribedAgreementTypeDef(
    _RequiredDescribedAgreementTypeDef, _OptionalDescribedAgreementTypeDef
):
    pass

_RequiredDescribedCertificateTypeDef = TypedDict(
    "_RequiredDescribedCertificateTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedCertificateTypeDef = TypedDict(
    "_OptionalDescribedCertificateTypeDef",
    {
        "CertificateId": str,
        "Usage": CertificateUsageTypeType,
        "Status": CertificateStatusTypeType,
        "Certificate": str,
        "CertificateChain": str,
        "ActiveDate": datetime,
        "InactiveDate": datetime,
        "Serial": str,
        "NotBeforeDate": datetime,
        "NotAfterDate": datetime,
        "Type": CertificateTypeType,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class DescribedCertificateTypeDef(
    _RequiredDescribedCertificateTypeDef, _OptionalDescribedCertificateTypeDef
):
    pass

_RequiredDescribedConnectorTypeDef = TypedDict(
    "_RequiredDescribedConnectorTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedConnectorTypeDef = TypedDict(
    "_OptionalDescribedConnectorTypeDef",
    {
        "ConnectorId": str,
        "Url": str,
        "As2Config": "As2ConnectorConfigTypeDef",
        "AccessRole": str,
        "LoggingRole": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class DescribedConnectorTypeDef(
    _RequiredDescribedConnectorTypeDef, _OptionalDescribedConnectorTypeDef
):
    pass

DescribedExecutionTypeDef = TypedDict(
    "DescribedExecutionTypeDef",
    {
        "ExecutionId": str,
        "InitialFileLocation": "FileLocationTypeDef",
        "ServiceMetadata": "ServiceMetadataTypeDef",
        "ExecutionRole": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "PosixProfile": "PosixProfileTypeDef",
        "Status": ExecutionStatusType,
        "Results": "ExecutionResultsTypeDef",
    },
    total=False,
)

_RequiredDescribedProfileTypeDef = TypedDict(
    "_RequiredDescribedProfileTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedProfileTypeDef = TypedDict(
    "_OptionalDescribedProfileTypeDef",
    {
        "ProfileId": str,
        "ProfileType": ProfileTypeType,
        "As2Id": str,
        "CertificateIds": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class DescribedProfileTypeDef(_RequiredDescribedProfileTypeDef, _OptionalDescribedProfileTypeDef):
    pass

_RequiredDescribedSecurityPolicyTypeDef = TypedDict(
    "_RequiredDescribedSecurityPolicyTypeDef",
    {
        "SecurityPolicyName": str,
    },
)
_OptionalDescribedSecurityPolicyTypeDef = TypedDict(
    "_OptionalDescribedSecurityPolicyTypeDef",
    {
        "Fips": bool,
        "SshCiphers": List[str],
        "SshKexs": List[str],
        "SshMacs": List[str],
        "TlsCiphers": List[str],
    },
    total=False,
)

class DescribedSecurityPolicyTypeDef(
    _RequiredDescribedSecurityPolicyTypeDef, _OptionalDescribedSecurityPolicyTypeDef
):
    pass

_RequiredDescribedServerTypeDef = TypedDict(
    "_RequiredDescribedServerTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedServerTypeDef = TypedDict(
    "_OptionalDescribedServerTypeDef",
    {
        "Certificate": str,
        "ProtocolDetails": "ProtocolDetailsTypeDef",
        "Domain": DomainType,
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKeyFingerprint": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "IdentityProviderType": IdentityProviderTypeType,
        "LoggingRole": str,
        "PostAuthenticationLoginBanner": str,
        "PreAuthenticationLoginBanner": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
        "ServerId": str,
        "State": StateType,
        "Tags": List["TagTypeDef"],
        "UserCount": int,
        "WorkflowDetails": "WorkflowDetailsTypeDef",
    },
    total=False,
)

class DescribedServerTypeDef(_RequiredDescribedServerTypeDef, _OptionalDescribedServerTypeDef):
    pass

_RequiredDescribedUserTypeDef = TypedDict(
    "_RequiredDescribedUserTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedUserTypeDef = TypedDict(
    "_OptionalDescribedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
        "SshPublicKeys": List["SshPublicKeyTypeDef"],
        "Tags": List["TagTypeDef"],
        "UserName": str,
    },
    total=False,
)

class DescribedUserTypeDef(_RequiredDescribedUserTypeDef, _OptionalDescribedUserTypeDef):
    pass

_RequiredDescribedWorkflowTypeDef = TypedDict(
    "_RequiredDescribedWorkflowTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedWorkflowTypeDef = TypedDict(
    "_OptionalDescribedWorkflowTypeDef",
    {
        "Description": str,
        "Steps": List["WorkflowStepTypeDef"],
        "OnExceptionSteps": List["WorkflowStepTypeDef"],
        "WorkflowId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class DescribedWorkflowTypeDef(
    _RequiredDescribedWorkflowTypeDef, _OptionalDescribedWorkflowTypeDef
):
    pass

EfsFileLocationTypeDef = TypedDict(
    "EfsFileLocationTypeDef",
    {
        "FileSystemId": str,
        "Path": str,
    },
    total=False,
)

EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "AddressAllocationIds": List[str],
        "SubnetIds": List[str],
        "VpcEndpointId": str,
        "VpcId": str,
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ExecutionErrorTypeDef = TypedDict(
    "ExecutionErrorTypeDef",
    {
        "Type": ExecutionErrorTypeType,
        "Message": str,
    },
)

ExecutionResultsTypeDef = TypedDict(
    "ExecutionResultsTypeDef",
    {
        "Steps": List["ExecutionStepResultTypeDef"],
        "OnExceptionSteps": List["ExecutionStepResultTypeDef"],
    },
    total=False,
)

ExecutionStepResultTypeDef = TypedDict(
    "ExecutionStepResultTypeDef",
    {
        "StepType": WorkflowStepTypeType,
        "Outputs": str,
        "Error": "ExecutionErrorTypeDef",
    },
    total=False,
)

FileLocationTypeDef = TypedDict(
    "FileLocationTypeDef",
    {
        "S3FileLocation": "S3FileLocationTypeDef",
        "EfsFileLocation": "EfsFileLocationTypeDef",
    },
    total=False,
)

HomeDirectoryMapEntryTypeDef = TypedDict(
    "HomeDirectoryMapEntryTypeDef",
    {
        "Entry": str,
        "Target": str,
    },
)

IdentityProviderDetailsTypeDef = TypedDict(
    "IdentityProviderDetailsTypeDef",
    {
        "Url": str,
        "InvocationRole": str,
        "DirectoryId": str,
        "Function": str,
    },
    total=False,
)

_RequiredImportCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredImportCertificateRequestRequestTypeDef",
    {
        "Usage": CertificateUsageTypeType,
        "Certificate": str,
    },
)
_OptionalImportCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalImportCertificateRequestRequestTypeDef",
    {
        "CertificateChain": str,
        "PrivateKey": str,
        "ActiveDate": Union[datetime, str],
        "InactiveDate": Union[datetime, str],
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportCertificateRequestRequestTypeDef(
    _RequiredImportCertificateRequestRequestTypeDef, _OptionalImportCertificateRequestRequestTypeDef
):
    pass

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSshPublicKeyRequestRequestTypeDef = TypedDict(
    "ImportSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyBody": str,
        "UserName": str,
    },
)

ImportSshPublicKeyResponseTypeDef = TypedDict(
    "ImportSshPublicKeyResponseTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputFileLocationTypeDef = TypedDict(
    "InputFileLocationTypeDef",
    {
        "S3FileLocation": "S3InputFileLocationTypeDef",
        "EfsFileLocation": "EfsFileLocationTypeDef",
    },
    total=False,
)

_RequiredListAccessesRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessesRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalListAccessesRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccessesRequestRequestTypeDef(
    _RequiredListAccessesRequestRequestTypeDef, _OptionalListAccessesRequestRequestTypeDef
):
    pass

ListAccessesResponseTypeDef = TypedDict(
    "ListAccessesResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Accesses": List["ListedAccessTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAgreementsRequestRequestTypeDef = TypedDict(
    "_RequiredListAgreementsRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalListAgreementsRequestRequestTypeDef = TypedDict(
    "_OptionalListAgreementsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAgreementsRequestRequestTypeDef(
    _RequiredListAgreementsRequestRequestTypeDef, _OptionalListAgreementsRequestRequestTypeDef
):
    pass

ListAgreementsResponseTypeDef = TypedDict(
    "ListAgreementsResponseTypeDef",
    {
        "NextToken": str,
        "Agreements": List["ListedAgreementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "Certificates": List["ListedCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
        "NextToken": str,
        "Connectors": List["ListedConnectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListExecutionsRequestRequestTypeDef",
    {
        "WorkflowId": str,
    },
)
_OptionalListExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListExecutionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListExecutionsRequestRequestTypeDef(
    _RequiredListExecutionsRequestRequestTypeDef, _OptionalListExecutionsRequestRequestTypeDef
):
    pass

ListExecutionsResponseTypeDef = TypedDict(
    "ListExecutionsResponseTypeDef",
    {
        "NextToken": str,
        "WorkflowId": str,
        "Executions": List["ListedExecutionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilesRequestRequestTypeDef = TypedDict(
    "ListProfilesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ProfileType": ProfileTypeType,
    },
    total=False,
)

ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "NextToken": str,
        "Profiles": List["ListedProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityPoliciesRequestRequestTypeDef = TypedDict(
    "ListSecurityPoliciesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSecurityPoliciesResponseTypeDef = TypedDict(
    "ListSecurityPoliciesResponseTypeDef",
    {
        "NextToken": str,
        "SecurityPolicyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "NextToken": str,
        "Servers": List["ListedServerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
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
        "Arn": str,
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Users": List["ListedUserTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "NextToken": str,
        "Workflows": List["ListedWorkflowTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListedAccessTypeDef = TypedDict(
    "ListedAccessTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Role": str,
        "ExternalId": str,
    },
    total=False,
)

ListedAgreementTypeDef = TypedDict(
    "ListedAgreementTypeDef",
    {
        "Arn": str,
        "AgreementId": str,
        "Description": str,
        "Status": AgreementStatusTypeType,
        "ServerId": str,
        "LocalProfileId": str,
        "PartnerProfileId": str,
    },
    total=False,
)

ListedCertificateTypeDef = TypedDict(
    "ListedCertificateTypeDef",
    {
        "Arn": str,
        "CertificateId": str,
        "Usage": CertificateUsageTypeType,
        "Status": CertificateStatusTypeType,
        "ActiveDate": datetime,
        "InactiveDate": datetime,
        "Type": CertificateTypeType,
        "Description": str,
    },
    total=False,
)

ListedConnectorTypeDef = TypedDict(
    "ListedConnectorTypeDef",
    {
        "Arn": str,
        "ConnectorId": str,
        "Url": str,
    },
    total=False,
)

ListedExecutionTypeDef = TypedDict(
    "ListedExecutionTypeDef",
    {
        "ExecutionId": str,
        "InitialFileLocation": "FileLocationTypeDef",
        "ServiceMetadata": "ServiceMetadataTypeDef",
        "Status": ExecutionStatusType,
    },
    total=False,
)

ListedProfileTypeDef = TypedDict(
    "ListedProfileTypeDef",
    {
        "Arn": str,
        "ProfileId": str,
        "As2Id": str,
        "ProfileType": ProfileTypeType,
    },
    total=False,
)

_RequiredListedServerTypeDef = TypedDict(
    "_RequiredListedServerTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListedServerTypeDef = TypedDict(
    "_OptionalListedServerTypeDef",
    {
        "Domain": DomainType,
        "IdentityProviderType": IdentityProviderTypeType,
        "EndpointType": EndpointTypeType,
        "LoggingRole": str,
        "ServerId": str,
        "State": StateType,
        "UserCount": int,
    },
    total=False,
)

class ListedServerTypeDef(_RequiredListedServerTypeDef, _OptionalListedServerTypeDef):
    pass

_RequiredListedUserTypeDef = TypedDict(
    "_RequiredListedUserTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListedUserTypeDef = TypedDict(
    "_OptionalListedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Role": str,
        "SshPublicKeyCount": int,
        "UserName": str,
    },
    total=False,
)

class ListedUserTypeDef(_RequiredListedUserTypeDef, _OptionalListedUserTypeDef):
    pass

ListedWorkflowTypeDef = TypedDict(
    "ListedWorkflowTypeDef",
    {
        "WorkflowId": str,
        "Description": str,
        "Arn": str,
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "LoggingRole": str,
        "LogGroupName": str,
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

_RequiredPosixProfileTypeDef = TypedDict(
    "_RequiredPosixProfileTypeDef",
    {
        "Uid": int,
        "Gid": int,
    },
)
_OptionalPosixProfileTypeDef = TypedDict(
    "_OptionalPosixProfileTypeDef",
    {
        "SecondaryGids": List[int],
    },
    total=False,
)

class PosixProfileTypeDef(_RequiredPosixProfileTypeDef, _OptionalPosixProfileTypeDef):
    pass

ProtocolDetailsTypeDef = TypedDict(
    "ProtocolDetailsTypeDef",
    {
        "PassiveIp": str,
        "TlsSessionResumptionMode": TlsSessionResumptionModeType,
        "SetStatOption": SetStatOptionType,
        "As2Transports": List[Literal["HTTP"]],
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

S3FileLocationTypeDef = TypedDict(
    "S3FileLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": str,
        "Etag": str,
    },
    total=False,
)

S3InputFileLocationTypeDef = TypedDict(
    "S3InputFileLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
    total=False,
)

S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SendWorkflowStepStateRequestRequestTypeDef = TypedDict(
    "SendWorkflowStepStateRequestRequestTypeDef",
    {
        "WorkflowId": str,
        "ExecutionId": str,
        "Token": str,
        "Status": CustomStepStatusType,
    },
)

ServiceMetadataTypeDef = TypedDict(
    "ServiceMetadataTypeDef",
    {
        "UserDetails": "UserDetailsTypeDef",
    },
)

SshPublicKeyTypeDef = TypedDict(
    "SshPublicKeyTypeDef",
    {
        "DateImported": datetime,
        "SshPublicKeyBody": str,
        "SshPublicKeyId": str,
    },
)

StartFileTransferRequestRequestTypeDef = TypedDict(
    "StartFileTransferRequestRequestTypeDef",
    {
        "ConnectorId": str,
        "SendFilePaths": List[str],
    },
)

StartFileTransferResponseTypeDef = TypedDict(
    "StartFileTransferResponseTypeDef",
    {
        "TransferId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartServerRequestRequestTypeDef = TypedDict(
    "StartServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

StopServerRequestRequestTypeDef = TypedDict(
    "StopServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagStepDetailsTypeDef = TypedDict(
    "TagStepDetailsTypeDef",
    {
        "Name": str,
        "Tags": List["S3TagTypeDef"],
        "SourceFileLocation": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTestIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredTestIdentityProviderRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalTestIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalTestIdentityProviderRequestRequestTypeDef",
    {
        "ServerProtocol": ProtocolType,
        "SourceIp": str,
        "UserPassword": str,
    },
    total=False,
)

class TestIdentityProviderRequestRequestTypeDef(
    _RequiredTestIdentityProviderRequestRequestTypeDef,
    _OptionalTestIdentityProviderRequestRequestTypeDef,
):
    pass

TestIdentityProviderResponseTypeDef = TypedDict(
    "TestIdentityProviderResponseTypeDef",
    {
        "Response": str,
        "StatusCode": int,
        "Message": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAccessRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)
_OptionalUpdateAccessRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
    },
    total=False,
)

class UpdateAccessRequestRequestTypeDef(
    _RequiredUpdateAccessRequestRequestTypeDef, _OptionalUpdateAccessRequestRequestTypeDef
):
    pass

UpdateAccessResponseTypeDef = TypedDict(
    "UpdateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAgreementRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgreementRequestRequestTypeDef",
    {
        "AgreementId": str,
        "ServerId": str,
    },
)
_OptionalUpdateAgreementRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgreementRequestRequestTypeDef",
    {
        "Description": str,
        "Status": AgreementStatusTypeType,
        "LocalProfileId": str,
        "PartnerProfileId": str,
        "BaseDirectory": str,
        "AccessRole": str,
    },
    total=False,
)

class UpdateAgreementRequestRequestTypeDef(
    _RequiredUpdateAgreementRequestRequestTypeDef, _OptionalUpdateAgreementRequestRequestTypeDef
):
    pass

UpdateAgreementResponseTypeDef = TypedDict(
    "UpdateAgreementResponseTypeDef",
    {
        "AgreementId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
    },
)
_OptionalUpdateCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCertificateRequestRequestTypeDef",
    {
        "ActiveDate": Union[datetime, str],
        "InactiveDate": Union[datetime, str],
        "Description": str,
    },
    total=False,
)

class UpdateCertificateRequestRequestTypeDef(
    _RequiredUpdateCertificateRequestRequestTypeDef, _OptionalUpdateCertificateRequestRequestTypeDef
):
    pass

UpdateCertificateResponseTypeDef = TypedDict(
    "UpdateCertificateResponseTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectorRequestRequestTypeDef",
    {
        "ConnectorId": str,
    },
)
_OptionalUpdateConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectorRequestRequestTypeDef",
    {
        "Url": str,
        "As2Config": "As2ConnectorConfigTypeDef",
        "AccessRole": str,
        "LoggingRole": str,
    },
    total=False,
)

class UpdateConnectorRequestRequestTypeDef(
    _RequiredUpdateConnectorRequestRequestTypeDef, _OptionalUpdateConnectorRequestRequestTypeDef
):
    pass

UpdateConnectorResponseTypeDef = TypedDict(
    "UpdateConnectorResponseTypeDef",
    {
        "ConnectorId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)
_OptionalUpdateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileRequestRequestTypeDef",
    {
        "CertificateIds": List[str],
    },
    total=False,
)

class UpdateProfileRequestRequestTypeDef(
    _RequiredUpdateProfileRequestRequestTypeDef, _OptionalUpdateProfileRequestRequestTypeDef
):
    pass

UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalUpdateServerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServerRequestRequestTypeDef",
    {
        "Certificate": str,
        "ProtocolDetails": "ProtocolDetailsTypeDef",
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKey": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "LoggingRole": str,
        "PostAuthenticationLoginBanner": str,
        "PreAuthenticationLoginBanner": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
        "WorkflowDetails": "WorkflowDetailsTypeDef",
    },
    total=False,
)

class UpdateServerRequestRequestTypeDef(
    _RequiredUpdateServerRequestRequestTypeDef, _OptionalUpdateServerRequestRequestTypeDef
):
    pass

UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUserDetailsTypeDef = TypedDict(
    "_RequiredUserDetailsTypeDef",
    {
        "UserName": str,
        "ServerId": str,
    },
)
_OptionalUserDetailsTypeDef = TypedDict(
    "_OptionalUserDetailsTypeDef",
    {
        "SessionId": str,
    },
    total=False,
)

class UserDetailsTypeDef(_RequiredUserDetailsTypeDef, _OptionalUserDetailsTypeDef):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WorkflowDetailTypeDef = TypedDict(
    "WorkflowDetailTypeDef",
    {
        "WorkflowId": str,
        "ExecutionRole": str,
    },
)

WorkflowDetailsTypeDef = TypedDict(
    "WorkflowDetailsTypeDef",
    {
        "OnUpload": List["WorkflowDetailTypeDef"],
    },
)

WorkflowStepTypeDef = TypedDict(
    "WorkflowStepTypeDef",
    {
        "Type": WorkflowStepTypeType,
        "CopyStepDetails": "CopyStepDetailsTypeDef",
        "CustomStepDetails": "CustomStepDetailsTypeDef",
        "DeleteStepDetails": "DeleteStepDetailsTypeDef",
        "TagStepDetails": "TagStepDetailsTypeDef",
    },
    total=False,
)
