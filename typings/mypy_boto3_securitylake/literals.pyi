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
    "AwsLogSourceNameType",
    "DataLakeStatusType",
    "GetDataLakeSourcesPaginatorName",
    "HttpMethodType",
    "ListDataLakeExceptionsPaginatorName",
    "ListLogSourcesPaginatorName",
    "ListSubscribersPaginatorName",
    "SourceCollectionStatusType",
    "SubscriberStatusType",
)

AccessTypeType = Literal["LAKEFORMATION", "S3"]
AwsLogSourceNameType = Literal[
    "CLOUD_TRAIL_MGMT",
    "EKS_AUDIT",
    "LAMBDA_EXECUTION",
    "ROUTE53",
    "S3_DATA",
    "SH_FINDINGS",
    "VPC_FLOW",
    "WAF",
]
DataLakeStatusType = Literal["COMPLETED", "FAILED", "INITIALIZED", "PENDING"]
GetDataLakeSourcesPaginatorName = Literal["get_data_lake_sources"]
HttpMethodType = Literal["POST", "PUT"]
ListDataLakeExceptionsPaginatorName = Literal["list_data_lake_exceptions"]
ListLogSourcesPaginatorName = Literal["list_log_sources"]
ListSubscribersPaginatorName = Literal["list_subscribers"]
SourceCollectionStatusType = Literal["COLLECTING", "MISCONFIGURED", "NOT_COLLECTING"]
SubscriberStatusType = Literal["ACTIVE", "DEACTIVATED", "PENDING", "READY"]
