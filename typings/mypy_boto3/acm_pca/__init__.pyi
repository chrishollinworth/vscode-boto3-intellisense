"""
Main interface for acm-pca service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_acm_pca import (
        ACMPCAClient,
        AuditReportCreatedWaiter,
        CertificateAuthorityCSRCreatedWaiter,
        CertificateIssuedWaiter,
        Client,
        ListCertificateAuthoritiesPaginator,
        ListPermissionsPaginator,
        ListTagsPaginator,
    )

    session = Session()
    client: ACMPCAClient = session.client("acm-pca")

    audit_report_created_waiter: AuditReportCreatedWaiter = client.get_waiter("audit_report_created")
    certificate_authority_csr_created_waiter: CertificateAuthorityCSRCreatedWaiter = client.get_waiter("certificate_authority_csr_created")
    certificate_issued_waiter: CertificateIssuedWaiter = client.get_waiter("certificate_issued")

    list_certificate_authorities_paginator: ListCertificateAuthoritiesPaginator = client.get_paginator("list_certificate_authorities")
    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""

from .client import ACMPCAClient
from .paginator import (
    ListCertificateAuthoritiesPaginator,
    ListPermissionsPaginator,
    ListTagsPaginator,
)
from .waiter import (
    AuditReportCreatedWaiter,
    CertificateAuthorityCSRCreatedWaiter,
    CertificateIssuedWaiter,
)

Client = ACMPCAClient

__all__ = (
    "ACMPCAClient",
    "AuditReportCreatedWaiter",
    "CertificateAuthorityCSRCreatedWaiter",
    "CertificateIssuedWaiter",
    "Client",
    "ListCertificateAuthoritiesPaginator",
    "ListPermissionsPaginator",
    "ListTagsPaginator",
)
