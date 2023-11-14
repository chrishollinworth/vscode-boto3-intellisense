"""
Type annotations for resourcegroupstaggingapi service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/literals.html)

Usage::

    ```python
    from mypy_boto3_resourcegroupstaggingapi.literals import ErrorCodeType

    data: ErrorCodeType = "InternalServiceException"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ErrorCodeType",
    "GetComplianceSummaryPaginatorName",
    "GetResourcesPaginatorName",
    "GetTagKeysPaginatorName",
    "GetTagValuesPaginatorName",
    "GroupByAttributeType",
    "TargetIdTypeType",
)

ErrorCodeType = Literal["InternalServiceException", "InvalidParameterException"]
GetComplianceSummaryPaginatorName = Literal["get_compliance_summary"]
GetResourcesPaginatorName = Literal["get_resources"]
GetTagKeysPaginatorName = Literal["get_tag_keys"]
GetTagValuesPaginatorName = Literal["get_tag_values"]
GroupByAttributeType = Literal["REGION", "RESOURCE_TYPE", "TARGET_ID"]
TargetIdTypeType = Literal["ACCOUNT", "OU", "ROOT"]
