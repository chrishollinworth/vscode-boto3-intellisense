"""
Type annotations for rolesanywhere service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/literals.html)

Usage::

    ```python
    from mypy_boto3_rolesanywhere.literals import CertificateFieldType

    data: CertificateFieldType = "x509Issuer"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CertificateFieldType",
    "ListCrlsPaginatorName",
    "ListProfilesPaginatorName",
    "ListSubjectsPaginatorName",
    "ListTrustAnchorsPaginatorName",
    "NotificationChannelType",
    "NotificationEventType",
    "TrustAnchorTypeType",
)

CertificateFieldType = Literal["x509Issuer", "x509SAN", "x509Subject"]
ListCrlsPaginatorName = Literal["list_crls"]
ListProfilesPaginatorName = Literal["list_profiles"]
ListSubjectsPaginatorName = Literal["list_subjects"]
ListTrustAnchorsPaginatorName = Literal["list_trust_anchors"]
NotificationChannelType = Literal["ALL"]
NotificationEventType = Literal["CA_CERTIFICATE_EXPIRY", "END_ENTITY_CERTIFICATE_EXPIRY"]
TrustAnchorTypeType = Literal["AWS_ACM_PCA", "CERTIFICATE_BUNDLE", "SELF_SIGNED_REPOSITORY"]
