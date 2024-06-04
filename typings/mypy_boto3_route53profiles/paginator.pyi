"""
Type annotations for route53profiles service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_route53profiles import Route53ProfilesClient
    from mypy_boto3_route53profiles.paginator import (
        ListProfileAssociationsPaginator,
        ListProfileResourceAssociationsPaginator,
        ListProfilesPaginator,
    )

    client: Route53ProfilesClient = boto3.client("route53profiles")

    list_profile_associations_paginator: ListProfileAssociationsPaginator = client.get_paginator("list_profile_associations")
    list_profile_resource_associations_paginator: ListProfileResourceAssociationsPaginator = client.get_paginator("list_profile_resource_associations")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListProfileAssociationsResponseTypeDef,
    ListProfileResourceAssociationsResponseTypeDef,
    ListProfilesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListProfileAssociationsPaginator",
    "ListProfileResourceAssociationsPaginator",
    "ListProfilesPaginator",
)

class ListProfileAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfileAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofileassociationspaginator)
    """

    def paginate(
        self,
        *,
        ProfileId: str = None,
        ResourceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProfileAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfileAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofileassociationspaginator)
        """

class ListProfileResourceAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfileResourceAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofileresourceassociationspaginator)
    """

    def paginate(
        self,
        *,
        ProfileId: str,
        ResourceType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProfileResourceAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfileResourceAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofileresourceassociationspaginator)
        """

class ListProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofilespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofilespaginator)
        """
