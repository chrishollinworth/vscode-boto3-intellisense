"""
Type annotations for elastictranscoder service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/literals.html)

Usage::

    ```python
    from mypy_boto3_elastictranscoder.literals import JobCompleteWaiterName

    data: JobCompleteWaiterName = "job_complete"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "JobCompleteWaiterName",
    "ListJobsByPipelinePaginatorName",
    "ListJobsByStatusPaginatorName",
    "ListPipelinesPaginatorName",
    "ListPresetsPaginatorName",
)

JobCompleteWaiterName = Literal["job_complete"]
ListJobsByPipelinePaginatorName = Literal["list_jobs_by_pipeline"]
ListJobsByStatusPaginatorName = Literal["list_jobs_by_status"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
ListPresetsPaginatorName = Literal["list_presets"]
