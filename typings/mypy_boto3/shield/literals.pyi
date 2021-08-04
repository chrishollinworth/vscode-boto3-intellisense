"""
Type annotations for shield service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/literals.html)

Usage::

    ```python
    from mypy_boto3_shield.literals import AttackLayerType

    data: AttackLayerType = "APPLICATION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttackLayerType",
    "AttackPropertyIdentifierType",
    "AutoRenewType",
    "ListAttacksPaginatorName",
    "ListProtectionsPaginatorName",
    "ProactiveEngagementStatusType",
    "ProtectedResourceTypeType",
    "ProtectionGroupAggregationType",
    "ProtectionGroupPatternType",
    "SubResourceTypeType",
    "SubscriptionStateType",
    "UnitType",
)

AttackLayerType = Literal["APPLICATION", "NETWORK"]
AttackPropertyIdentifierType = Literal[
    "DESTINATION_URL",
    "REFERRER",
    "SOURCE_ASN",
    "SOURCE_COUNTRY",
    "SOURCE_IP_ADDRESS",
    "SOURCE_USER_AGENT",
    "WORDPRESS_PINGBACK_REFLECTOR",
    "WORDPRESS_PINGBACK_SOURCE",
]
AutoRenewType = Literal["DISABLED", "ENABLED"]
ListAttacksPaginatorName = Literal["list_attacks"]
ListProtectionsPaginatorName = Literal["list_protections"]
ProactiveEngagementStatusType = Literal["DISABLED", "ENABLED", "PENDING"]
ProtectedResourceTypeType = Literal[
    "APPLICATION_LOAD_BALANCER",
    "CLASSIC_LOAD_BALANCER",
    "CLOUDFRONT_DISTRIBUTION",
    "ELASTIC_IP_ALLOCATION",
    "GLOBAL_ACCELERATOR",
    "ROUTE_53_HOSTED_ZONE",
]
ProtectionGroupAggregationType = Literal["MAX", "MEAN", "SUM"]
ProtectionGroupPatternType = Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"]
SubResourceTypeType = Literal["IP", "URL"]
SubscriptionStateType = Literal["ACTIVE", "INACTIVE"]
UnitType = Literal["BITS", "BYTES", "PACKETS", "REQUESTS"]
