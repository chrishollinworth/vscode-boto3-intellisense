"""
Type annotations for rolesanywhere service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_rolesanywhere import IAMRolesAnywhereClient
    from mypy_boto3_rolesanywhere.paginator import (
        ListCrlsPaginator,
        ListProfilesPaginator,
        ListSubjectsPaginator,
        ListTrustAnchorsPaginator,
    )

    client: IAMRolesAnywhereClient = boto3.client("rolesanywhere")

    list_crls_paginator: ListCrlsPaginator = client.get_paginator("list_crls")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_subjects_paginator: ListSubjectsPaginator = client.get_paginator("list_subjects")
    list_trust_anchors_paginator: ListTrustAnchorsPaginator = client.get_paginator("list_trust_anchors")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListCrlsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListSubjectsResponseTypeDef,
    ListTrustAnchorsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListCrlsPaginator",
    "ListProfilesPaginator",
    "ListSubjectsPaginator",
    "ListTrustAnchorsPaginator",
)

class ListCrlsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListCrls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listcrlspaginator)
    """

    def paginate(
        self, *, pageSize: int = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCrlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListCrls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listcrlspaginator)
        """

class ListProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listprofilespaginator)
    """

    def paginate(
        self, *, pageSize: int = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listprofilespaginator)
        """

class ListSubjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListSubjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listsubjectspaginator)
    """

    def paginate(
        self, *, pageSize: int = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListSubjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listsubjectspaginator)
        """

class ListTrustAnchorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListTrustAnchors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listtrustanchorspaginator)
    """

    def paginate(
        self, *, pageSize: int = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrustAnchorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListTrustAnchors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listtrustanchorspaginator)
        """
