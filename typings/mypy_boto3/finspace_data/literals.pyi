"""
Type annotations for finspace-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/literals.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.literals import ChangeTypeType

    data: ChangeTypeType = "APPEND"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChangeTypeType",
    "ChangesetStatusType",
    "ErrorCategoryType",
    "FormatTypeType",
    "SourceTypeType",
    "locationTypeType",
)

ChangeTypeType = Literal["APPEND", "MODIFY", "REPLACE"]
ChangesetStatusType = Literal["FAILED", "PENDING", "RUNNING", "STOP_REQUESTED", "SUCCESS"]
ErrorCategoryType = Literal[
    "A_user_recoverable_error_has_occurred",
    "An_internal_error_has_occurred",
    "Cancelled",
    "Missing_required_permission_to_perform_this_request",
    "One_or_more_inputs_to_this_request_were_not_found",
    "Service_limits_have_been_exceeded",
    "The_inputs_to_this_request_are_invalid",
    "The_system_temporarily_lacks_sufficient_resources_to_process_the_request",
]
FormatTypeType = Literal["CSV", "JSON", "PARQUET", "XML"]
SourceTypeType = Literal["S3"]
locationTypeType = Literal["INGESTION", "SAGEMAKER"]
