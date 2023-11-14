"""
Type annotations for license-manager-user-subscriptions service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/literals.html)

Usage::

    ```python
    from mypy_boto3_license_manager_user_subscriptions.literals import ListIdentityProvidersPaginatorName

    data: ListIdentityProvidersPaginatorName = "list_identity_providers"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListIdentityProvidersPaginatorName",
    "ListInstancesPaginatorName",
    "ListProductSubscriptionsPaginatorName",
    "ListUserAssociationsPaginatorName",
)

ListIdentityProvidersPaginatorName = Literal["list_identity_providers"]
ListInstancesPaginatorName = Literal["list_instances"]
ListProductSubscriptionsPaginatorName = Literal["list_product_subscriptions"]
ListUserAssociationsPaginatorName = Literal["list_user_associations"]
