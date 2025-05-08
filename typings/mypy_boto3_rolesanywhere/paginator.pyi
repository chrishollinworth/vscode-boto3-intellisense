"""
Type annotations for rolesanywhere service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rolesanywhere.client import IAMRolesAnywhereClient
    from mypy_boto3_rolesanywhere.paginator import (
        ListCrlsPaginator,
        ListProfilesPaginator,
        ListSubjectsPaginator,
        ListTrustAnchorsPaginator,
    )

    session = Session()
    client: IAMRolesAnywhereClient = session.client("rolesanywhere")

    list_crls_paginator: ListCrlsPaginator = client.get_paginator("list_crls")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_subjects_paginator: ListSubjectsPaginator = client.get_paginator("list_subjects")
    list_trust_anchors_paginator: ListTrustAnchorsPaginator = client.get_paginator("list_trust_anchors")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCrlsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListRequestPaginateExtraExtraExtraTypeDef,
    ListRequestPaginateExtraExtraTypeDef,
    ListRequestPaginateExtraTypeDef,
    ListRequestPaginateTypeDef,
    ListSubjectsResponseTypeDef,
    ListTrustAnchorsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCrlsPaginator",
    "ListProfilesPaginator",
    "ListSubjectsPaginator",
    "ListTrustAnchorsPaginator",
)

if TYPE_CHECKING:
    _ListCrlsPaginatorBase = Paginator[ListCrlsResponseTypeDef]
else:
    _ListCrlsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCrlsPaginator(_ListCrlsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListCrls.html#IAMRolesAnywhere.Paginator.ListCrls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listcrlspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRequestPaginateTypeDef]
    ) -> PageIterator[ListCrlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListCrls.html#IAMRolesAnywhere.Paginator.ListCrls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listcrlspaginator)
        """

if TYPE_CHECKING:
    _ListProfilesPaginatorBase = Paginator[ListProfilesResponseTypeDef]
else:
    _ListProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProfilesPaginator(_ListProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListProfiles.html#IAMRolesAnywhere.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRequestPaginateExtraTypeDef]
    ) -> PageIterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListProfiles.html#IAMRolesAnywhere.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listprofilespaginator)
        """

if TYPE_CHECKING:
    _ListSubjectsPaginatorBase = Paginator[ListSubjectsResponseTypeDef]
else:
    _ListSubjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubjectsPaginator(_ListSubjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListSubjects.html#IAMRolesAnywhere.Paginator.ListSubjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listsubjectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRequestPaginateExtraExtraTypeDef]
    ) -> PageIterator[ListSubjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListSubjects.html#IAMRolesAnywhere.Paginator.ListSubjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listsubjectspaginator)
        """

if TYPE_CHECKING:
    _ListTrustAnchorsPaginatorBase = Paginator[ListTrustAnchorsResponseTypeDef]
else:
    _ListTrustAnchorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrustAnchorsPaginator(_ListTrustAnchorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListTrustAnchors.html#IAMRolesAnywhere.Paginator.ListTrustAnchors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listtrustanchorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRequestPaginateExtraExtraExtraTypeDef]
    ) -> PageIterator[ListTrustAnchorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/paginator/ListTrustAnchors.html#IAMRolesAnywhere.Paginator.ListTrustAnchors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators/#listtrustanchorspaginator)
        """
