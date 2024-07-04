"""
Type annotations for b2bi service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_b2bi import B2BIClient
    from mypy_boto3_b2bi.paginator import (
        ListCapabilitiesPaginator,
        ListPartnershipsPaginator,
        ListProfilesPaginator,
        ListTransformersPaginator,
    )

    client: B2BIClient = boto3.client("b2bi")

    list_capabilities_paginator: ListCapabilitiesPaginator = client.get_paginator("list_capabilities")
    list_partnerships_paginator: ListPartnershipsPaginator = client.get_paginator("list_partnerships")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_transformers_paginator: ListTransformersPaginator = client.get_paginator("list_transformers")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListCapabilitiesResponseTypeDef,
    ListPartnershipsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListTransformersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListCapabilitiesPaginator",
    "ListPartnershipsPaginator",
    "ListProfilesPaginator",
    "ListTransformersPaginator",
)

class ListCapabilitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListCapabilities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listcapabilitiespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCapabilitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListCapabilities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listcapabilitiespaginator)
        """

class ListPartnershipsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListPartnerships)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listpartnershipspaginator)
    """

    def paginate(
        self, *, profileId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPartnershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListPartnerships.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listpartnershipspaginator)
        """

class ListProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listprofilespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listprofilespaginator)
        """

class ListTransformersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListTransformers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listtransformerspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTransformersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/b2bi.html#B2BI.Paginator.ListTransformers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listtransformerspaginator)
        """
