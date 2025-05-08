"""
Type annotations for verifiedpermissions service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_verifiedpermissions.client import VerifiedPermissionsClient
    from mypy_boto3_verifiedpermissions.paginator import (
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyStoresPaginator,
        ListPolicyTemplatesPaginator,
    )

    session = Session()
    client: VerifiedPermissionsClient = session.client("verifiedpermissions")

    list_identity_sources_paginator: ListIdentitySourcesPaginator = client.get_paginator("list_identity_sources")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_stores_paginator: ListPolicyStoresPaginator = client.get_paginator("list_policy_stores")
    list_policy_templates_paginator: ListPolicyTemplatesPaginator = client.get_paginator("list_policy_templates")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListIdentitySourcesInputPaginateTypeDef,
    ListIdentitySourcesOutputTypeDef,
    ListPoliciesInputPaginateTypeDef,
    ListPoliciesOutputTypeDef,
    ListPolicyStoresInputPaginateTypeDef,
    ListPolicyStoresOutputTypeDef,
    ListPolicyTemplatesInputPaginateTypeDef,
    ListPolicyTemplatesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListIdentitySourcesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyStoresPaginator",
    "ListPolicyTemplatesPaginator",
)

if TYPE_CHECKING:
    _ListIdentitySourcesPaginatorBase = Paginator[ListIdentitySourcesOutputTypeDef]
else:
    _ListIdentitySourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdentitySourcesPaginator(_ListIdentitySourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListIdentitySources.html#VerifiedPermissions.Paginator.ListIdentitySources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listidentitysourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdentitySourcesInputPaginateTypeDef]
    ) -> PageIterator[ListIdentitySourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListIdentitySources.html#VerifiedPermissions.Paginator.ListIdentitySources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listidentitysourcespaginator)
        """

if TYPE_CHECKING:
    _ListPoliciesPaginatorBase = Paginator[ListPoliciesOutputTypeDef]
else:
    _ListPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPoliciesPaginator(_ListPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListPolicies.html#VerifiedPermissions.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPoliciesInputPaginateTypeDef]
    ) -> PageIterator[ListPoliciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListPolicies.html#VerifiedPermissions.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListPolicyStoresPaginatorBase = Paginator[ListPolicyStoresOutputTypeDef]
else:
    _ListPolicyStoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyStoresPaginator(_ListPolicyStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListPolicyStores.html#VerifiedPermissions.Paginator.ListPolicyStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listpolicystorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyStoresInputPaginateTypeDef]
    ) -> PageIterator[ListPolicyStoresOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListPolicyStores.html#VerifiedPermissions.Paginator.ListPolicyStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listpolicystorespaginator)
        """

if TYPE_CHECKING:
    _ListPolicyTemplatesPaginatorBase = Paginator[ListPolicyTemplatesOutputTypeDef]
else:
    _ListPolicyTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyTemplatesPaginator(_ListPolicyTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListPolicyTemplates.html#VerifiedPermissions.Paginator.ListPolicyTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listpolicytemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListPolicyTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/paginator/ListPolicyTemplates.html#VerifiedPermissions.Paginator.ListPolicyTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators/#listpolicytemplatespaginator)
        """
