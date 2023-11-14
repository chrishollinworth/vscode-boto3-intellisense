"""
Type annotations for tnb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/literals.html)

Usage::

    ```python
    from mypy_boto3_tnb.literals import DescriptorContentTypeType

    data: DescriptorContentTypeType = "text/plain"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescriptorContentTypeType",
    "LcmOperationTypeType",
    "ListSolFunctionInstancesPaginatorName",
    "ListSolFunctionPackagesPaginatorName",
    "ListSolNetworkInstancesPaginatorName",
    "ListSolNetworkOperationsPaginatorName",
    "ListSolNetworkPackagesPaginatorName",
    "NsLcmOperationStateType",
    "NsStateType",
    "NsdOnboardingStateType",
    "NsdOperationalStateType",
    "NsdUsageStateType",
    "OnboardingStateType",
    "OperationalStateType",
    "PackageContentTypeType",
    "TaskStatusType",
    "UpdateSolNetworkTypeType",
    "UsageStateType",
    "VnfInstantiationStateType",
    "VnfOperationalStateType",
)

DescriptorContentTypeType = Literal["text/plain"]
LcmOperationTypeType = Literal["INSTANTIATE", "TERMINATE", "UPDATE"]
ListSolFunctionInstancesPaginatorName = Literal["list_sol_function_instances"]
ListSolFunctionPackagesPaginatorName = Literal["list_sol_function_packages"]
ListSolNetworkInstancesPaginatorName = Literal["list_sol_network_instances"]
ListSolNetworkOperationsPaginatorName = Literal["list_sol_network_operations"]
ListSolNetworkPackagesPaginatorName = Literal["list_sol_network_packages"]
NsLcmOperationStateType = Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "PROCESSING"]
NsStateType = Literal[
    "DELETED",
    "IMPAIRED",
    "INSTANTIATED",
    "INSTANTIATE_IN_PROGRESS",
    "NOT_INSTANTIATED",
    "STOPPED",
    "TERMINATE_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
]
NsdOnboardingStateType = Literal["CREATED", "ERROR", "ONBOARDED"]
NsdOperationalStateType = Literal["DISABLED", "ENABLED"]
NsdUsageStateType = Literal["IN_USE", "NOT_IN_USE"]
OnboardingStateType = Literal["CREATED", "ERROR", "ONBOARDED"]
OperationalStateType = Literal["DISABLED", "ENABLED"]
PackageContentTypeType = Literal["application/zip"]
TaskStatusType = Literal[
    "CANCELLED", "COMPLETED", "ERROR", "IN_PROGRESS", "SCHEDULED", "SKIPPED", "STARTED"
]
UpdateSolNetworkTypeType = Literal["MODIFY_VNF_INFORMATION"]
UsageStateType = Literal["IN_USE", "NOT_IN_USE"]
VnfInstantiationStateType = Literal["INSTANTIATED", "NOT_INSTANTIATED"]
VnfOperationalStateType = Literal["STARTED", "STOPPED"]
