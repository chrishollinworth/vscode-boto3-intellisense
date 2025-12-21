"""
Main interface for healthlake service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_healthlake import (
        Client,
        FHIRDatastoreActiveWaiter,
        FHIRDatastoreDeletedWaiter,
        FHIRExportJobCompletedWaiter,
        FHIRImportJobCompletedWaiter,
        HealthLakeClient,
    )

    session = Session()
    client: HealthLakeClient = session.client("healthlake")

    fhir_datastore_active_waiter: FHIRDatastoreActiveWaiter = client.get_waiter("fhir_datastore_active")
    fhir_datastore_deleted_waiter: FHIRDatastoreDeletedWaiter = client.get_waiter("fhir_datastore_deleted")
    fhir_export_job_completed_waiter: FHIRExportJobCompletedWaiter = client.get_waiter("fhir_export_job_completed")
    fhir_import_job_completed_waiter: FHIRImportJobCompletedWaiter = client.get_waiter("fhir_import_job_completed")
    ```
"""

from .client import HealthLakeClient
from .waiter import (
    FHIRDatastoreActiveWaiter,
    FHIRDatastoreDeletedWaiter,
    FHIRExportJobCompletedWaiter,
    FHIRImportJobCompletedWaiter,
)

Client = HealthLakeClient

__all__ = (
    "Client",
    "FHIRDatastoreActiveWaiter",
    "FHIRDatastoreDeletedWaiter",
    "FHIRExportJobCompletedWaiter",
    "FHIRImportJobCompletedWaiter",
    "HealthLakeClient",
)
