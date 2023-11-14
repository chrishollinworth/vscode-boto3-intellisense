"""
Main interface for medical-imaging service.

Usage::

    ```python
    import boto3
    from mypy_boto3_medical_imaging import (
        Client,
        HealthImagingClient,
        ListDICOMImportJobsPaginator,
        ListDatastoresPaginator,
        ListImageSetVersionsPaginator,
        SearchImageSetsPaginator,
    )

    session = boto3.Session()

    client: HealthImagingClient = boto3.client("medical-imaging")
    session_client: HealthImagingClient = session.client("medical-imaging")

    list_dicom_import_jobs_paginator: ListDICOMImportJobsPaginator = client.get_paginator("list_dicom_import_jobs")
    list_datastores_paginator: ListDatastoresPaginator = client.get_paginator("list_datastores")
    list_image_set_versions_paginator: ListImageSetVersionsPaginator = client.get_paginator("list_image_set_versions")
    search_image_sets_paginator: SearchImageSetsPaginator = client.get_paginator("search_image_sets")
    ```
"""
from .client import HealthImagingClient
from .paginator import (
    ListDatastoresPaginator,
    ListDICOMImportJobsPaginator,
    ListImageSetVersionsPaginator,
    SearchImageSetsPaginator,
)

Client = HealthImagingClient

__all__ = (
    "Client",
    "HealthImagingClient",
    "ListDICOMImportJobsPaginator",
    "ListDatastoresPaginator",
    "ListImageSetVersionsPaginator",
    "SearchImageSetsPaginator",
)
