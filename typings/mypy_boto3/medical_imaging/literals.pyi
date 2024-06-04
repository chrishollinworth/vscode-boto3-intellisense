"""
Type annotations for medical-imaging service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/literals.html)

Usage::

    ```python
    from mypy_boto3_medical_imaging.literals import DatastoreStatusType

    data: DatastoreStatusType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DatastoreStatusType",
    "ImageSetStateType",
    "ImageSetWorkflowStatusType",
    "JobStatusType",
    "ListDICOMImportJobsPaginatorName",
    "ListDatastoresPaginatorName",
    "ListImageSetVersionsPaginatorName",
    "OperatorType",
    "SearchImageSetsPaginatorName",
    "SortFieldType",
    "SortOrderType",
)

DatastoreStatusType = Literal["ACTIVE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING"]
ImageSetStateType = Literal["ACTIVE", "DELETED", "LOCKED"]
ImageSetWorkflowStatusType = Literal[
    "COPIED",
    "COPYING",
    "COPYING_WITH_READ_ONLY_ACCESS",
    "COPY_FAILED",
    "CREATED",
    "DELETED",
    "DELETING",
    "UPDATED",
    "UPDATE_FAILED",
    "UPDATING",
]
JobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "SUBMITTED"]
ListDICOMImportJobsPaginatorName = Literal["list_dicom_import_jobs"]
ListDatastoresPaginatorName = Literal["list_datastores"]
ListImageSetVersionsPaginatorName = Literal["list_image_set_versions"]
OperatorType = Literal["BETWEEN", "EQUAL"]
SearchImageSetsPaginatorName = Literal["search_image_sets"]
SortFieldType = Literal["DICOMStudyDateAndTime", "createdAt", "updatedAt"]
SortOrderType = Literal["ASC", "DESC"]
