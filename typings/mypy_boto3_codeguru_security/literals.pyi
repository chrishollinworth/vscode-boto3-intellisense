"""
Type annotations for codeguru-security service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/literals.html)

Usage::

    ```python
    from mypy_boto3_codeguru_security.literals import AnalysisTypeType

    data: AnalysisTypeType = "All"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnalysisTypeType",
    "ErrorCodeType",
    "GetFindingsPaginatorName",
    "ListFindingsMetricsPaginatorName",
    "ListScansPaginatorName",
    "ScanStateType",
    "ScanTypeType",
    "SeverityType",
    "StatusType",
)

AnalysisTypeType = Literal["All", "Security"]
ErrorCodeType = Literal[
    "DUPLICATE_IDENTIFIER",
    "INTERNAL_ERROR",
    "INVALID_FINDING_ID",
    "INVALID_SCAN_NAME",
    "ITEM_DOES_NOT_EXIST",
]
GetFindingsPaginatorName = Literal["get_findings"]
ListFindingsMetricsPaginatorName = Literal["list_findings_metrics"]
ListScansPaginatorName = Literal["list_scans"]
ScanStateType = Literal["Failed", "InProgress", "Successful"]
ScanTypeType = Literal["Express", "Standard"]
SeverityType = Literal["Critical", "High", "Info", "Low", "Medium"]
StatusType = Literal["All", "Closed", "Open"]
