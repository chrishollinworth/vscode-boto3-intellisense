"""
Type annotations for sagemaker-edge service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_edge.literals import ChecksumTypeType

    data: ChecksumTypeType = "SHA1"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChecksumTypeType",
    "DeploymentStatusType",
    "DeploymentTypeType",
    "FailureHandlingPolicyType",
    "ModelStateType",
)

ChecksumTypeType = Literal["SHA1"]
DeploymentStatusType = Literal["FAIL", "SUCCESS"]
DeploymentTypeType = Literal["Model"]
FailureHandlingPolicyType = Literal["DO_NOTHING", "ROLLBACK_ON_FAILURE"]
ModelStateType = Literal["DEPLOY", "UNDEPLOY"]
