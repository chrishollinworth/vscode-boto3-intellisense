"""
Type annotations for apprunner service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/literals.html)

Usage::

    ```python
    from mypy_boto3_apprunner.literals import AutoScalingConfigurationStatusType

    data: AutoScalingConfigurationStatusType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AutoScalingConfigurationStatusType",
    "CertificateValidationRecordStatusType",
    "ConfigurationSourceType",
    "ConnectionStatusType",
    "CustomDomainAssociationStatusType",
    "EgressTypeType",
    "HealthCheckProtocolType",
    "ImageRepositoryTypeType",
    "IpAddressTypeType",
    "ObservabilityConfigurationStatusType",
    "OperationStatusType",
    "OperationTypeType",
    "ProviderTypeType",
    "RuntimeType",
    "ServiceStatusType",
    "SourceCodeVersionTypeType",
    "TracingVendorType",
    "VpcConnectorStatusType",
    "VpcIngressConnectionStatusType",
)

AutoScalingConfigurationStatusType = Literal["ACTIVE", "INACTIVE"]
CertificateValidationRecordStatusType = Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
ConfigurationSourceType = Literal["API", "REPOSITORY"]
ConnectionStatusType = Literal["AVAILABLE", "DELETED", "ERROR", "PENDING_HANDSHAKE"]
CustomDomainAssociationStatusType = Literal[
    "ACTIVE",
    "BINDING_CERTIFICATE",
    "CREATE_FAILED",
    "CREATING",
    "DELETE_FAILED",
    "DELETING",
    "PENDING_CERTIFICATE_DNS_VALIDATION",
]
EgressTypeType = Literal["DEFAULT", "VPC"]
HealthCheckProtocolType = Literal["HTTP", "TCP"]
ImageRepositoryTypeType = Literal["ECR", "ECR_PUBLIC"]
IpAddressTypeType = Literal["DUAL_STACK", "IPV4"]
ObservabilityConfigurationStatusType = Literal["ACTIVE", "INACTIVE"]
OperationStatusType = Literal[
    "FAILED",
    "IN_PROGRESS",
    "PENDING",
    "ROLLBACK_FAILED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_SUCCEEDED",
    "SUCCEEDED",
]
OperationTypeType = Literal[
    "CREATE_SERVICE",
    "DELETE_SERVICE",
    "PAUSE_SERVICE",
    "RESUME_SERVICE",
    "START_DEPLOYMENT",
    "UPDATE_SERVICE",
]
ProviderTypeType = Literal["BITBUCKET", "GITHUB"]
RuntimeType = Literal[
    "CORRETTO_11",
    "CORRETTO_8",
    "DOTNET_6",
    "GO_1",
    "NODEJS_12",
    "NODEJS_14",
    "NODEJS_16",
    "NODEJS_18",
    "PHP_81",
    "PYTHON_3",
    "PYTHON_311",
    "RUBY_31",
]
ServiceStatusType = Literal[
    "CREATE_FAILED", "DELETED", "DELETE_FAILED", "OPERATION_IN_PROGRESS", "PAUSED", "RUNNING"
]
SourceCodeVersionTypeType = Literal["BRANCH"]
TracingVendorType = Literal["AWSXRAY"]
VpcConnectorStatusType = Literal["ACTIVE", "INACTIVE"]
VpcIngressConnectionStatusType = Literal[
    "AVAILABLE",
    "DELETED",
    "FAILED_CREATION",
    "FAILED_DELETION",
    "FAILED_UPDATE",
    "PENDING_CREATION",
    "PENDING_DELETION",
    "PENDING_UPDATE",
]
