"""
Type annotations for securitylake service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/literals.html)

Usage::

    ```python
    from mypy_boto3_securitylake.literals import AccessTypeType

    data: AccessTypeType = "LAKEFORMATION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessTypeType",
    "AwsLogSourceTypeType",
    "DimensionType",
    "EndpointProtocolType",
    "GetDatalakeStatusPaginatorName",
    "HttpsMethodType",
    "ListDatalakeExceptionsPaginatorName",
    "ListLogSourcesPaginatorName",
    "ListSubscribersPaginatorName",
    "OcsfEventClassType",
    "RegionType",
    "SourceStatusType",
    "StorageClassType",
    "SubscriptionProtocolTypeType",
    "SubscriptionStatusType",
    "settingsStatusType",
)

AccessTypeType = Literal["LAKEFORMATION", "S3"]
AwsLogSourceTypeType = Literal["CLOUD_TRAIL", "ROUTE53", "SH_FINDINGS", "VPC_FLOW"]
DimensionType = Literal["MEMBER", "REGION", "SOURCE_TYPE"]
EndpointProtocolType = Literal["HTTPS", "SQS"]
GetDatalakeStatusPaginatorName = Literal["get_datalake_status"]
HttpsMethodType = Literal["POST", "PUT"]
ListDatalakeExceptionsPaginatorName = Literal["list_datalake_exceptions"]
ListLogSourcesPaginatorName = Literal["list_log_sources"]
ListSubscribersPaginatorName = Literal["list_subscribers"]
OcsfEventClassType = Literal[
    "ACCESS_ACTIVITY",
    "ACCOUNT_CHANGE",
    "AUTHENTICATION",
    "AUTHORIZATION",
    "CLOUD_API",
    "CLOUD_STORAGE",
    "CONFIG_STATE",
    "CONTAINER_LIFECYCLE",
    "DATABASE_LIFECYCLE",
    "DHCP_ACTIVITY",
    "DNS_ACTIVITY",
    "ENTITY_MANAGEMENT_AUDIT",
    "FILE_ACTIVITY",
    "FTP_ACTIVITY",
    "HTTP_ACTIVITY",
    "INVENTORY_INFO",
    "KERNEL_ACTIVITY",
    "KERNEL_EXTENSION",
    "MEMORY_ACTIVITY",
    "MODULE_ACTIVITY",
    "NETWORK_ACTIVITY",
    "PROCESS_ACTIVITY",
    "RDP_ACTIVITY",
    "REGISTRY_KEY_ACTIVITY",
    "REGISTRY_VALUE_ACTIVITY",
    "RESOURCE_ACTIVITY",
    "RFB_ACTIVITY",
    "SCHEDULED_JOB_ACTIVITY",
    "SECURITY_FINDING",
    "SMB_ACTIVITY",
    "SMTP_ACTIVITY",
    "SSH_ACTIVITY",
    "VIRTUAL_MACHINE_ACTIVITY",
]
RegionType = Literal[
    "ap-northeast-1",
    "ap-southeast-2",
    "eu-central-1",
    "eu-west-1",
    "us-east-1",
    "us-east-2",
    "us-west-2",
]
SourceStatusType = Literal["ACTIVE", "DEACTIVATED", "PENDING"]
StorageClassType = Literal[
    "DEEP_ARCHIVE",
    "EXPIRE",
    "GLACIER",
    "GLACIER_IR",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "STANDARD_IA",
]
SubscriptionProtocolTypeType = Literal[
    "APP", "EMAIL", "EMAIL_JSON", "FIREHOSE", "HTTP", "HTTPS", "LAMBDA", "SMS", "SQS"
]
SubscriptionStatusType = Literal["ACTIVE", "DEACTIVATED", "PENDING", "READY"]
settingsStatusType = Literal["COMPLETED", "FAILED", "INITIALIZED", "PENDING"]
