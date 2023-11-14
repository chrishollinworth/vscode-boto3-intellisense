"""
Type annotations for route53-recovery-readiness service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/literals.html)

Usage::

    ```python
    from mypy_boto3_route53_recovery_readiness.literals import GetCellReadinessSummaryPaginatorName

    data: GetCellReadinessSummaryPaginatorName = "get_cell_readiness_summary"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "GetCellReadinessSummaryPaginatorName",
    "GetReadinessCheckResourceStatusPaginatorName",
    "GetReadinessCheckStatusPaginatorName",
    "GetRecoveryGroupReadinessSummaryPaginatorName",
    "ListCellsPaginatorName",
    "ListCrossAccountAuthorizationsPaginatorName",
    "ListReadinessChecksPaginatorName",
    "ListRecoveryGroupsPaginatorName",
    "ListResourceSetsPaginatorName",
    "ListRulesPaginatorName",
    "ReadinessType",
)

GetCellReadinessSummaryPaginatorName = Literal["get_cell_readiness_summary"]
GetReadinessCheckResourceStatusPaginatorName = Literal["get_readiness_check_resource_status"]
GetReadinessCheckStatusPaginatorName = Literal["get_readiness_check_status"]
GetRecoveryGroupReadinessSummaryPaginatorName = Literal["get_recovery_group_readiness_summary"]
ListCellsPaginatorName = Literal["list_cells"]
ListCrossAccountAuthorizationsPaginatorName = Literal["list_cross_account_authorizations"]
ListReadinessChecksPaginatorName = Literal["list_readiness_checks"]
ListRecoveryGroupsPaginatorName = Literal["list_recovery_groups"]
ListResourceSetsPaginatorName = Literal["list_resource_sets"]
ListRulesPaginatorName = Literal["list_rules"]
ReadinessType = Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"]
