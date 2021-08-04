"""
Type annotations for cloudfront service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudfront.literals import CachePolicyCookieBehaviorType

    data: CachePolicyCookieBehaviorType = "all"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CachePolicyCookieBehaviorType",
    "CachePolicyHeaderBehaviorType",
    "CachePolicyQueryStringBehaviorType",
    "CachePolicyTypeType",
    "CertificateSourceType",
    "DistributionDeployedWaiterName",
    "EventTypeType",
    "FormatType",
    "FunctionRuntimeType",
    "FunctionStageType",
    "GeoRestrictionTypeType",
    "HttpVersionType",
    "ICPRecordalStatusType",
    "InvalidationCompletedWaiterName",
    "ItemSelectionType",
    "ListCloudFrontOriginAccessIdentitiesPaginatorName",
    "ListDistributionsPaginatorName",
    "ListInvalidationsPaginatorName",
    "ListStreamingDistributionsPaginatorName",
    "MethodType",
    "MinimumProtocolVersionType",
    "OriginProtocolPolicyType",
    "OriginRequestPolicyCookieBehaviorType",
    "OriginRequestPolicyHeaderBehaviorType",
    "OriginRequestPolicyQueryStringBehaviorType",
    "OriginRequestPolicyTypeType",
    "PriceClassType",
    "RealtimeMetricsSubscriptionStatusType",
    "SSLSupportMethodType",
    "SslProtocolType",
    "StreamingDistributionDeployedWaiterName",
    "ViewerProtocolPolicyType",
)

CachePolicyCookieBehaviorType = Literal["all", "allExcept", "none", "whitelist"]
CachePolicyHeaderBehaviorType = Literal["none", "whitelist"]
CachePolicyQueryStringBehaviorType = Literal["all", "allExcept", "none", "whitelist"]
CachePolicyTypeType = Literal["custom", "managed"]
CertificateSourceType = Literal["acm", "cloudfront", "iam"]
DistributionDeployedWaiterName = Literal["distribution_deployed"]
EventTypeType = Literal["origin-request", "origin-response", "viewer-request", "viewer-response"]
FormatType = Literal["URLEncoded"]
FunctionRuntimeType = Literal["cloudfront-js-1.0"]
FunctionStageType = Literal["DEVELOPMENT", "LIVE"]
GeoRestrictionTypeType = Literal["blacklist", "none", "whitelist"]
HttpVersionType = Literal["http1.1", "http2"]
ICPRecordalStatusType = Literal["APPROVED", "PENDING", "SUSPENDED"]
InvalidationCompletedWaiterName = Literal["invalidation_completed"]
ItemSelectionType = Literal["all", "none", "whitelist"]
ListCloudFrontOriginAccessIdentitiesPaginatorName = Literal[
    "list_cloud_front_origin_access_identities"
]
ListDistributionsPaginatorName = Literal["list_distributions"]
ListInvalidationsPaginatorName = Literal["list_invalidations"]
ListStreamingDistributionsPaginatorName = Literal["list_streaming_distributions"]
MethodType = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
MinimumProtocolVersionType = Literal[
    "SSLv3", "TLSv1", "TLSv1.1_2016", "TLSv1.2_2018", "TLSv1.2_2019", "TLSv1.2_2021", "TLSv1_2016"
]
OriginProtocolPolicyType = Literal["http-only", "https-only", "match-viewer"]
OriginRequestPolicyCookieBehaviorType = Literal["all", "none", "whitelist"]
OriginRequestPolicyHeaderBehaviorType = Literal[
    "allViewer", "allViewerAndWhitelistCloudFront", "none", "whitelist"
]
OriginRequestPolicyQueryStringBehaviorType = Literal["all", "none", "whitelist"]
OriginRequestPolicyTypeType = Literal["custom", "managed"]
PriceClassType = Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"]
RealtimeMetricsSubscriptionStatusType = Literal["Disabled", "Enabled"]
SSLSupportMethodType = Literal["sni-only", "static-ip", "vip"]
SslProtocolType = Literal["SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2"]
StreamingDistributionDeployedWaiterName = Literal["streaming_distribution_deployed"]
ViewerProtocolPolicyType = Literal["allow-all", "https-only", "redirect-to-https"]
