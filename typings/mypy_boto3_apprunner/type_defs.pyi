"""
Type annotations for apprunner service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apprunner.type_defs import AssociateCustomDomainRequestRequestTypeDef

    data: AssociateCustomDomainRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AutoScalingConfigurationStatusType,
    CertificateValidationRecordStatusType,
    ConfigurationSourceType,
    ConnectionStatusType,
    CustomDomainAssociationStatusType,
    EgressTypeType,
    HealthCheckProtocolType,
    ImageRepositoryTypeType,
    IpAddressTypeType,
    ObservabilityConfigurationStatusType,
    OperationStatusType,
    OperationTypeType,
    ProviderTypeType,
    RuntimeType,
    ServiceStatusType,
    VpcConnectorStatusType,
    VpcIngressConnectionStatusType,
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
    "AssociateCustomDomainRequestRequestTypeDef",
    "AssociateCustomDomainResponseTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AutoScalingConfigurationSummaryTypeDef",
    "AutoScalingConfigurationTypeDef",
    "CertificateValidationRecordTypeDef",
    "CodeConfigurationTypeDef",
    "CodeConfigurationValuesTypeDef",
    "CodeRepositoryTypeDef",
    "ConnectionSummaryTypeDef",
    "ConnectionTypeDef",
    "CreateAutoScalingConfigurationRequestRequestTypeDef",
    "CreateAutoScalingConfigurationResponseTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateObservabilityConfigurationRequestRequestTypeDef",
    "CreateObservabilityConfigurationResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateVpcConnectorRequestRequestTypeDef",
    "CreateVpcConnectorResponseTypeDef",
    "CreateVpcIngressConnectionRequestRequestTypeDef",
    "CreateVpcIngressConnectionResponseTypeDef",
    "CustomDomainTypeDef",
    "DeleteAutoScalingConfigurationRequestRequestTypeDef",
    "DeleteAutoScalingConfigurationResponseTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteObservabilityConfigurationRequestRequestTypeDef",
    "DeleteObservabilityConfigurationResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteVpcConnectorRequestRequestTypeDef",
    "DeleteVpcConnectorResponseTypeDef",
    "DeleteVpcIngressConnectionRequestRequestTypeDef",
    "DeleteVpcIngressConnectionResponseTypeDef",
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    "DescribeAutoScalingConfigurationResponseTypeDef",
    "DescribeCustomDomainsRequestRequestTypeDef",
    "DescribeCustomDomainsResponseTypeDef",
    "DescribeObservabilityConfigurationRequestRequestTypeDef",
    "DescribeObservabilityConfigurationResponseTypeDef",
    "DescribeServiceRequestRequestTypeDef",
    "DescribeServiceResponseTypeDef",
    "DescribeVpcConnectorRequestRequestTypeDef",
    "DescribeVpcConnectorResponseTypeDef",
    "DescribeVpcIngressConnectionRequestRequestTypeDef",
    "DescribeVpcIngressConnectionResponseTypeDef",
    "DisassociateCustomDomainRequestRequestTypeDef",
    "DisassociateCustomDomainResponseTypeDef",
    "EgressConfigurationTypeDef",
    "EncryptionConfigurationTypeDef",
    "HealthCheckConfigurationTypeDef",
    "ImageConfigurationTypeDef",
    "ImageRepositoryTypeDef",
    "IngressConfigurationTypeDef",
    "IngressVpcConfigurationTypeDef",
    "InstanceConfigurationTypeDef",
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    "ListAutoScalingConfigurationsResponseTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListConnectionsResponseTypeDef",
    "ListObservabilityConfigurationsRequestRequestTypeDef",
    "ListObservabilityConfigurationsResponseTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesForAutoScalingConfigurationRequestRequestTypeDef",
    "ListServicesForAutoScalingConfigurationResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVpcConnectorsRequestRequestTypeDef",
    "ListVpcConnectorsResponseTypeDef",
    "ListVpcIngressConnectionsFilterTypeDef",
    "ListVpcIngressConnectionsRequestRequestTypeDef",
    "ListVpcIngressConnectionsResponseTypeDef",
    "NetworkConfigurationTypeDef",
    "ObservabilityConfigurationSummaryTypeDef",
    "ObservabilityConfigurationTypeDef",
    "OperationSummaryTypeDef",
    "PauseServiceRequestRequestTypeDef",
    "PauseServiceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeServiceRequestRequestTypeDef",
    "ResumeServiceResponseTypeDef",
    "ServiceObservabilityConfigurationTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "SourceCodeVersionTypeDef",
    "SourceConfigurationTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "StartDeploymentResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TraceConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef",
    "UpdateDefaultAutoScalingConfigurationResponseTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateVpcIngressConnectionRequestRequestTypeDef",
    "UpdateVpcIngressConnectionResponseTypeDef",
    "VpcConnectorTypeDef",
    "VpcDNSTargetTypeDef",
    "VpcIngressConnectionSummaryTypeDef",
    "VpcIngressConnectionTypeDef",
)

_RequiredAssociateCustomDomainRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)
_OptionalAssociateCustomDomainRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateCustomDomainRequestRequestTypeDef",
    {
        "EnableWWWSubdomain": bool,
    },
    total=False,
)

class AssociateCustomDomainRequestRequestTypeDef(
    _RequiredAssociateCustomDomainRequestRequestTypeDef,
    _OptionalAssociateCustomDomainRequestRequestTypeDef,
):
    pass

AssociateCustomDomainResponseTypeDef = TypedDict(
    "AssociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
        "VpcDNSTargets": List["VpcDNSTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "ConnectionArn": str,
        "AccessRoleArn": str,
    },
    total=False,
)

AutoScalingConfigurationSummaryTypeDef = TypedDict(
    "AutoScalingConfigurationSummaryTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "AutoScalingConfigurationName": str,
        "AutoScalingConfigurationRevision": int,
        "Status": AutoScalingConfigurationStatusType,
        "CreatedAt": datetime,
        "HasAssociatedService": bool,
        "IsDefault": bool,
    },
    total=False,
)

AutoScalingConfigurationTypeDef = TypedDict(
    "AutoScalingConfigurationTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "AutoScalingConfigurationName": str,
        "AutoScalingConfigurationRevision": int,
        "Latest": bool,
        "Status": AutoScalingConfigurationStatusType,
        "MaxConcurrency": int,
        "MinSize": int,
        "MaxSize": int,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
        "HasAssociatedService": bool,
        "IsDefault": bool,
    },
    total=False,
)

CertificateValidationRecordTypeDef = TypedDict(
    "CertificateValidationRecordTypeDef",
    {
        "Name": str,
        "Type": str,
        "Value": str,
        "Status": CertificateValidationRecordStatusType,
    },
    total=False,
)

_RequiredCodeConfigurationTypeDef = TypedDict(
    "_RequiredCodeConfigurationTypeDef",
    {
        "ConfigurationSource": ConfigurationSourceType,
    },
)
_OptionalCodeConfigurationTypeDef = TypedDict(
    "_OptionalCodeConfigurationTypeDef",
    {
        "CodeConfigurationValues": "CodeConfigurationValuesTypeDef",
    },
    total=False,
)

class CodeConfigurationTypeDef(
    _RequiredCodeConfigurationTypeDef, _OptionalCodeConfigurationTypeDef
):
    pass

_RequiredCodeConfigurationValuesTypeDef = TypedDict(
    "_RequiredCodeConfigurationValuesTypeDef",
    {
        "Runtime": RuntimeType,
    },
)
_OptionalCodeConfigurationValuesTypeDef = TypedDict(
    "_OptionalCodeConfigurationValuesTypeDef",
    {
        "BuildCommand": str,
        "StartCommand": str,
        "Port": str,
        "RuntimeEnvironmentVariables": Dict[str, str],
        "RuntimeEnvironmentSecrets": Dict[str, str],
    },
    total=False,
)

class CodeConfigurationValuesTypeDef(
    _RequiredCodeConfigurationValuesTypeDef, _OptionalCodeConfigurationValuesTypeDef
):
    pass

_RequiredCodeRepositoryTypeDef = TypedDict(
    "_RequiredCodeRepositoryTypeDef",
    {
        "RepositoryUrl": str,
        "SourceCodeVersion": "SourceCodeVersionTypeDef",
    },
)
_OptionalCodeRepositoryTypeDef = TypedDict(
    "_OptionalCodeRepositoryTypeDef",
    {
        "CodeConfiguration": "CodeConfigurationTypeDef",
        "SourceDirectory": str,
    },
    total=False,
)

class CodeRepositoryTypeDef(_RequiredCodeRepositoryTypeDef, _OptionalCodeRepositoryTypeDef):
    pass

ConnectionSummaryTypeDef = TypedDict(
    "ConnectionSummaryTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": ProviderTypeType,
        "Status": ConnectionStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": ProviderTypeType,
        "Status": ConnectionStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

_RequiredCreateAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
    },
)
_OptionalCreateAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutoScalingConfigurationRequestRequestTypeDef",
    {
        "MaxConcurrency": int,
        "MinSize": int,
        "MaxSize": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAutoScalingConfigurationRequestRequestTypeDef(
    _RequiredCreateAutoScalingConfigurationRequestRequestTypeDef,
    _OptionalCreateAutoScalingConfigurationRequestRequestTypeDef,
):
    pass

CreateAutoScalingConfigurationResponseTypeDef = TypedDict(
    "CreateAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "ProviderType": ProviderTypeType,
    },
)
_OptionalCreateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateConnectionRequestRequestTypeDef(
    _RequiredCreateConnectionRequestRequestTypeDef, _OptionalCreateConnectionRequestRequestTypeDef
):
    pass

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationName": str,
    },
)
_OptionalCreateObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateObservabilityConfigurationRequestRequestTypeDef",
    {
        "TraceConfiguration": "TraceConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateObservabilityConfigurationRequestRequestTypeDef(
    _RequiredCreateObservabilityConfigurationRequestRequestTypeDef,
    _OptionalCreateObservabilityConfigurationRequestRequestTypeDef,
):
    pass

CreateObservabilityConfigurationResponseTypeDef = TypedDict(
    "CreateObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": "ObservabilityConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestRequestTypeDef",
    {
        "ServiceName": str,
        "SourceConfiguration": "SourceConfigurationTypeDef",
    },
)
_OptionalCreateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestRequestTypeDef",
    {
        "InstanceConfiguration": "InstanceConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "HealthCheckConfiguration": "HealthCheckConfigurationTypeDef",
        "AutoScalingConfigurationArn": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "ObservabilityConfiguration": "ServiceObservabilityConfigurationTypeDef",
    },
    total=False,
)

class CreateServiceRequestRequestTypeDef(
    _RequiredCreateServiceRequestRequestTypeDef, _OptionalCreateServiceRequestRequestTypeDef
):
    pass

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorName": str,
        "Subnets": List[str],
    },
)
_OptionalCreateVpcConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcConnectorRequestRequestTypeDef",
    {
        "SecurityGroups": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVpcConnectorRequestRequestTypeDef(
    _RequiredCreateVpcConnectorRequestRequestTypeDef,
    _OptionalCreateVpcConnectorRequestRequestTypeDef,
):
    pass

CreateVpcConnectorResponseTypeDef = TypedDict(
    "CreateVpcConnectorResponseTypeDef",
    {
        "VpcConnector": "VpcConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcIngressConnectionRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "VpcIngressConnectionName": str,
        "IngressVpcConfiguration": "IngressVpcConfigurationTypeDef",
    },
)
_OptionalCreateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcIngressConnectionRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVpcIngressConnectionRequestRequestTypeDef(
    _RequiredCreateVpcIngressConnectionRequestRequestTypeDef,
    _OptionalCreateVpcIngressConnectionRequestRequestTypeDef,
):
    pass

CreateVpcIngressConnectionResponseTypeDef = TypedDict(
    "CreateVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": "VpcIngressConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomDomainTypeDef = TypedDict(
    "_RequiredCustomDomainTypeDef",
    {
        "DomainName": str,
        "EnableWWWSubdomain": bool,
        "Status": CustomDomainAssociationStatusType,
    },
)
_OptionalCustomDomainTypeDef = TypedDict(
    "_OptionalCustomDomainTypeDef",
    {
        "CertificateValidationRecords": List["CertificateValidationRecordTypeDef"],
    },
    total=False,
)

class CustomDomainTypeDef(_RequiredCustomDomainTypeDef, _OptionalCustomDomainTypeDef):
    pass

_RequiredDeleteAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)
_OptionalDeleteAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAutoScalingConfigurationRequestRequestTypeDef",
    {
        "DeleteAllRevisions": bool,
    },
    total=False,
)

class DeleteAutoScalingConfigurationRequestRequestTypeDef(
    _RequiredDeleteAutoScalingConfigurationRequestRequestTypeDef,
    _OptionalDeleteAutoScalingConfigurationRequestRequestTypeDef,
):
    pass

DeleteAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
)

DeleteObservabilityConfigurationResponseTypeDef = TypedDict(
    "DeleteObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": "ObservabilityConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)

DeleteVpcConnectorResponseTypeDef = TypedDict(
    "DeleteVpcConnectorResponseTypeDef",
    {
        "VpcConnector": "VpcConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
    },
)

DeleteVpcIngressConnectionResponseTypeDef = TypedDict(
    "DeleteVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": "VpcIngressConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

DescribeAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCustomDomainsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeCustomDomainsRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalDescribeCustomDomainsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeCustomDomainsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeCustomDomainsRequestRequestTypeDef(
    _RequiredDescribeCustomDomainsRequestRequestTypeDef,
    _OptionalDescribeCustomDomainsRequestRequestTypeDef,
):
    pass

DescribeCustomDomainsResponseTypeDef = TypedDict(
    "DescribeCustomDomainsResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomains": List["CustomDomainTypeDef"],
        "VpcDNSTargets": List["VpcDNSTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
)

DescribeObservabilityConfigurationResponseTypeDef = TypedDict(
    "DescribeObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": "ObservabilityConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceRequestRequestTypeDef = TypedDict(
    "DescribeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DescribeServiceResponseTypeDef = TypedDict(
    "DescribeServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcConnectorRequestRequestTypeDef = TypedDict(
    "DescribeVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)

DescribeVpcConnectorResponseTypeDef = TypedDict(
    "DescribeVpcConnectorResponseTypeDef",
    {
        "VpcConnector": "VpcConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "DescribeVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
    },
)

DescribeVpcIngressConnectionResponseTypeDef = TypedDict(
    "DescribeVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": "VpcIngressConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateCustomDomainRequestRequestTypeDef = TypedDict(
    "DisassociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)

DisassociateCustomDomainResponseTypeDef = TypedDict(
    "DisassociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
        "VpcDNSTargets": List["VpcDNSTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EgressConfigurationTypeDef = TypedDict(
    "EgressConfigurationTypeDef",
    {
        "EgressType": EgressTypeType,
        "VpcConnectorArn": str,
    },
    total=False,
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
)

HealthCheckConfigurationTypeDef = TypedDict(
    "HealthCheckConfigurationTypeDef",
    {
        "Protocol": HealthCheckProtocolType,
        "Path": str,
        "Interval": int,
        "Timeout": int,
        "HealthyThreshold": int,
        "UnhealthyThreshold": int,
    },
    total=False,
)

ImageConfigurationTypeDef = TypedDict(
    "ImageConfigurationTypeDef",
    {
        "RuntimeEnvironmentVariables": Dict[str, str],
        "StartCommand": str,
        "Port": str,
        "RuntimeEnvironmentSecrets": Dict[str, str],
    },
    total=False,
)

_RequiredImageRepositoryTypeDef = TypedDict(
    "_RequiredImageRepositoryTypeDef",
    {
        "ImageIdentifier": str,
        "ImageRepositoryType": ImageRepositoryTypeType,
    },
)
_OptionalImageRepositoryTypeDef = TypedDict(
    "_OptionalImageRepositoryTypeDef",
    {
        "ImageConfiguration": "ImageConfigurationTypeDef",
    },
    total=False,
)

class ImageRepositoryTypeDef(_RequiredImageRepositoryTypeDef, _OptionalImageRepositoryTypeDef):
    pass

IngressConfigurationTypeDef = TypedDict(
    "IngressConfigurationTypeDef",
    {
        "IsPubliclyAccessible": bool,
    },
    total=False,
)

IngressVpcConfigurationTypeDef = TypedDict(
    "IngressVpcConfigurationTypeDef",
    {
        "VpcId": str,
        "VpcEndpointId": str,
    },
    total=False,
)

InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "Cpu": str,
        "Memory": str,
        "InstanceRoleArn": str,
    },
    total=False,
)

ListAutoScalingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
        "LatestOnly": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAutoScalingConfigurationsResponseTypeDef = TypedDict(
    "ListAutoScalingConfigurationsResponseTypeDef",
    {
        "AutoScalingConfigurationSummaryList": List["AutoScalingConfigurationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "ConnectionSummaryList": List["ConnectionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObservabilityConfigurationsRequestRequestTypeDef = TypedDict(
    "ListObservabilityConfigurationsRequestRequestTypeDef",
    {
        "ObservabilityConfigurationName": str,
        "LatestOnly": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListObservabilityConfigurationsResponseTypeDef = TypedDict(
    "ListObservabilityConfigurationsResponseTypeDef",
    {
        "ObservabilityConfigurationSummaryList": List["ObservabilityConfigurationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListOperationsRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalListOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListOperationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListOperationsRequestRequestTypeDef(
    _RequiredListOperationsRequestRequestTypeDef, _OptionalListOperationsRequestRequestTypeDef
):
    pass

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "OperationSummaryList": List["OperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServicesForAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredListServicesForAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)
_OptionalListServicesForAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalListServicesForAutoScalingConfigurationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServicesForAutoScalingConfigurationRequestRequestTypeDef(
    _RequiredListServicesForAutoScalingConfigurationRequestRequestTypeDef,
    _OptionalListServicesForAutoScalingConfigurationRequestRequestTypeDef,
):
    pass

ListServicesForAutoScalingConfigurationResponseTypeDef = TypedDict(
    "ListServicesForAutoScalingConfigurationResponseTypeDef",
    {
        "ServiceArnList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "ServiceSummaryList": List["ServiceSummaryTypeDef"],
        "NextToken": str,
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVpcConnectorsRequestRequestTypeDef = TypedDict(
    "ListVpcConnectorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListVpcConnectorsResponseTypeDef = TypedDict(
    "ListVpcConnectorsResponseTypeDef",
    {
        "VpcConnectors": List["VpcConnectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVpcIngressConnectionsFilterTypeDef = TypedDict(
    "ListVpcIngressConnectionsFilterTypeDef",
    {
        "ServiceArn": str,
        "VpcEndpointId": str,
    },
    total=False,
)

ListVpcIngressConnectionsRequestRequestTypeDef = TypedDict(
    "ListVpcIngressConnectionsRequestRequestTypeDef",
    {
        "Filter": "ListVpcIngressConnectionsFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListVpcIngressConnectionsResponseTypeDef = TypedDict(
    "ListVpcIngressConnectionsResponseTypeDef",
    {
        "VpcIngressConnectionSummaryList": List["VpcIngressConnectionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "EgressConfiguration": "EgressConfigurationTypeDef",
        "IngressConfiguration": "IngressConfigurationTypeDef",
        "IpAddressType": IpAddressTypeType,
    },
    total=False,
)

ObservabilityConfigurationSummaryTypeDef = TypedDict(
    "ObservabilityConfigurationSummaryTypeDef",
    {
        "ObservabilityConfigurationArn": str,
        "ObservabilityConfigurationName": str,
        "ObservabilityConfigurationRevision": int,
    },
    total=False,
)

ObservabilityConfigurationTypeDef = TypedDict(
    "ObservabilityConfigurationTypeDef",
    {
        "ObservabilityConfigurationArn": str,
        "ObservabilityConfigurationName": str,
        "TraceConfiguration": "TraceConfigurationTypeDef",
        "ObservabilityConfigurationRevision": int,
        "Latest": bool,
        "Status": ObservabilityConfigurationStatusType,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)

OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": str,
        "Type": OperationTypeType,
        "Status": OperationStatusType,
        "TargetArn": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

PauseServiceRequestRequestTypeDef = TypedDict(
    "PauseServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

PauseServiceResponseTypeDef = TypedDict(
    "PauseServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ResumeServiceRequestRequestTypeDef = TypedDict(
    "ResumeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

ResumeServiceResponseTypeDef = TypedDict(
    "ResumeServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredServiceObservabilityConfigurationTypeDef = TypedDict(
    "_RequiredServiceObservabilityConfigurationTypeDef",
    {
        "ObservabilityEnabled": bool,
    },
)
_OptionalServiceObservabilityConfigurationTypeDef = TypedDict(
    "_OptionalServiceObservabilityConfigurationTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
    total=False,
)

class ServiceObservabilityConfigurationTypeDef(
    _RequiredServiceObservabilityConfigurationTypeDef,
    _OptionalServiceObservabilityConfigurationTypeDef,
):
    pass

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "ServiceUrl": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
    },
    total=False,
)

_RequiredServiceTypeDef = TypedDict(
    "_RequiredServiceTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "InstanceConfiguration": "InstanceConfigurationTypeDef",
        "AutoScalingConfigurationSummary": "AutoScalingConfigurationSummaryTypeDef",
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
    },
)
_OptionalServiceTypeDef = TypedDict(
    "_OptionalServiceTypeDef",
    {
        "ServiceUrl": str,
        "DeletedAt": datetime,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "HealthCheckConfiguration": "HealthCheckConfigurationTypeDef",
        "ObservabilityConfiguration": "ServiceObservabilityConfigurationTypeDef",
    },
    total=False,
)

class ServiceTypeDef(_RequiredServiceTypeDef, _OptionalServiceTypeDef):
    pass

SourceCodeVersionTypeDef = TypedDict(
    "SourceCodeVersionTypeDef",
    {
        "Type": Literal["BRANCH"],
        "Value": str,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "CodeRepository": "CodeRepositoryTypeDef",
        "ImageRepository": "ImageRepositoryTypeDef",
        "AutoDeploymentsEnabled": bool,
        "AuthenticationConfiguration": "AuthenticationConfigurationTypeDef",
    },
    total=False,
)

StartDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeploymentRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

StartDeploymentResponseTypeDef = TypedDict(
    "StartDeploymentResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TraceConfigurationTypeDef = TypedDict(
    "TraceConfigurationTypeDef",
    {
        "Vendor": Literal["AWSXRAY"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

UpdateDefaultAutoScalingConfigurationResponseTypeDef = TypedDict(
    "UpdateDefaultAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalUpdateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceRequestRequestTypeDef",
    {
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "InstanceConfiguration": "InstanceConfigurationTypeDef",
        "AutoScalingConfigurationArn": str,
        "HealthCheckConfiguration": "HealthCheckConfigurationTypeDef",
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "ObservabilityConfiguration": "ServiceObservabilityConfigurationTypeDef",
    },
    total=False,
)

class UpdateServiceRequestRequestTypeDef(
    _RequiredUpdateServiceRequestRequestTypeDef, _OptionalUpdateServiceRequestRequestTypeDef
):
    pass

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "UpdateVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "IngressVpcConfiguration": "IngressVpcConfigurationTypeDef",
    },
)

UpdateVpcIngressConnectionResponseTypeDef = TypedDict(
    "UpdateVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": "VpcIngressConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConnectorTypeDef = TypedDict(
    "VpcConnectorTypeDef",
    {
        "VpcConnectorName": str,
        "VpcConnectorArn": str,
        "VpcConnectorRevision": int,
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "Status": VpcConnectorStatusType,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)

VpcDNSTargetTypeDef = TypedDict(
    "VpcDNSTargetTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "VpcId": str,
        "DomainName": str,
    },
    total=False,
)

VpcIngressConnectionSummaryTypeDef = TypedDict(
    "VpcIngressConnectionSummaryTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "ServiceArn": str,
    },
    total=False,
)

VpcIngressConnectionTypeDef = TypedDict(
    "VpcIngressConnectionTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "VpcIngressConnectionName": str,
        "ServiceArn": str,
        "Status": VpcIngressConnectionStatusType,
        "AccountId": str,
        "DomainName": str,
        "IngressVpcConfiguration": "IngressVpcConfigurationTypeDef",
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)
