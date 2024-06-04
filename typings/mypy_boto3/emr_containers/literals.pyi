"""
Type annotations for emr-containers service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/literals.html)

Usage::

    ```python
    from mypy_boto3_emr_containers.literals import CertificateProviderTypeType

    data: CertificateProviderTypeType = "PEM"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CertificateProviderTypeType",
    "ContainerProviderTypeType",
    "EndpointStateType",
    "FailureReasonType",
    "JobRunStateType",
    "ListJobRunsPaginatorName",
    "ListJobTemplatesPaginatorName",
    "ListManagedEndpointsPaginatorName",
    "ListSecurityConfigurationsPaginatorName",
    "ListVirtualClustersPaginatorName",
    "PersistentAppUIType",
    "TemplateParameterDataTypeType",
    "VirtualClusterStateType",
)

CertificateProviderTypeType = Literal["PEM"]
ContainerProviderTypeType = Literal["EKS"]
EndpointStateType = Literal[
    "ACTIVE", "CREATING", "TERMINATED", "TERMINATED_WITH_ERRORS", "TERMINATING"
]
FailureReasonType = Literal[
    "CLUSTER_UNAVAILABLE", "INTERNAL_ERROR", "USER_ERROR", "VALIDATION_ERROR"
]
JobRunStateType = Literal[
    "CANCELLED", "CANCEL_PENDING", "COMPLETED", "FAILED", "PENDING", "RUNNING", "SUBMITTED"
]
ListJobRunsPaginatorName = Literal["list_job_runs"]
ListJobTemplatesPaginatorName = Literal["list_job_templates"]
ListManagedEndpointsPaginatorName = Literal["list_managed_endpoints"]
ListSecurityConfigurationsPaginatorName = Literal["list_security_configurations"]
ListVirtualClustersPaginatorName = Literal["list_virtual_clusters"]
PersistentAppUIType = Literal["DISABLED", "ENABLED"]
TemplateParameterDataTypeType = Literal["NUMBER", "STRING"]
VirtualClusterStateType = Literal["ARRESTED", "RUNNING", "TERMINATED", "TERMINATING"]
