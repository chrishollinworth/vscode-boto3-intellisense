"""
Main interface for marketplacecommerceanalytics service type definitions.

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.type_defs import GenerateDataSetResultTypeDef

    data: GenerateDataSetResultTypeDef = {...}
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("GenerateDataSetResultTypeDef", "StartSupportDataExportResultTypeDef")

GenerateDataSetResultTypeDef = TypedDict(
    "GenerateDataSetResultTypeDef", {"dataSetRequestId": str}, total=False
)

StartSupportDataExportResultTypeDef = TypedDict(
    "StartSupportDataExportResultTypeDef", {"dataSetRequestId": str}, total=False
)
