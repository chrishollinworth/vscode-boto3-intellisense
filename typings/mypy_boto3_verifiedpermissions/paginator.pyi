"""
Type annotations for verifiedpermissions service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_verifiedpermissions import VerifiedPermissionsClient
    from mypy_boto3_verifiedpermissions.paginator import (
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyStoresPaginator,
        ListPolicyTemplatesPaginator,
    )

    client: VerifiedPermissionsClient = boto3.client("verifiedpermissions")

    list_identity_sources_paginator: ListIdentitySourcesPaginator = client.get_paginator("list_identity_sources")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_stores_paginator: ListPolicyStoresPaginator = client.get_paginator("list_policy_stores")
    list_policy_templates_paginator: ListPolicyTemplatesPaginator = client.get_paginator("list_policy_templates")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    IdentitySourceFilterTypeDef,
    ListIdentitySourcesOutputTypeDef,
    ListPoliciesOutputTypeDef,
    ListPolicyStoresOutputTypeDef,
    ListPolicyTemplatesOutputTypeDef,
    PaginatorConfigTypeDef,
    PolicyFilterTypeDef,
)

__all__ = (
    "ListIdentitySourcesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyStoresPaginator",
    "ListPolicyTemplatesPaginator",
)

class ListIdentitySourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListIdentitySources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listidentitysourcespaginator)
    """

    def paginate(
        self,
        *,
        policyStoreId: str,
        filters: List["IdentitySourceFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentitySourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListIdentitySources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listidentitysourcespaginator)
        """

class ListPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpoliciespaginator)
    """

    def paginate(
        self,
        *,
        policyStoreId: str,
        filter: "PolicyFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpoliciespaginator)
        """

class ListPolicyStoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyStores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpolicystorespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPolicyStoresOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyStores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpolicystorespaginator)
        """

class ListPolicyTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpolicytemplatespaginator)
    """

    def paginate(
        self, *, policyStoreId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPolicyTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpolicytemplatespaginator)
        """
