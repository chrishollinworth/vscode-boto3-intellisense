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
    "ContinuousDeploymentPolicyTypeType",
    "DistributionDeployedWaiterName",
    "EventTypeType",
    "FormatType",
    "FrameOptionsListType",
    "FunctionRuntimeType",
    "FunctionStageType",
    "GeoRestrictionTypeType",
    "HttpVersionType",
    "ICPRecordalStatusType",
    "ImportSourceTypeType",
    "InvalidationCompletedWaiterName",
    "ItemSelectionType",
    "ListCloudFrontOriginAccessIdentitiesPaginatorName",
    "ListDistributionsPaginatorName",
    "ListInvalidationsPaginatorName",
    "ListKeyValueStoresPaginatorName",
    "ListStreamingDistributionsPaginatorName",
    "MethodType",
    "MinimumProtocolVersionType",
    "OriginAccessControlOriginTypesType",
    "OriginAccessControlSigningBehaviorsType",
    "OriginAccessControlSigningProtocolsType",
    "OriginProtocolPolicyType",
    "OriginRequestPolicyCookieBehaviorType",
    "OriginRequestPolicyHeaderBehaviorType",
    "OriginRequestPolicyQueryStringBehaviorType",
    "OriginRequestPolicyTypeType",
    "PriceClassType",
    "RealtimeMetricsSubscriptionStatusType",
    "ReferrerPolicyListType",
    "ResponseHeadersPolicyAccessControlAllowMethodsValuesType",
    "ResponseHeadersPolicyTypeType",
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
ContinuousDeploymentPolicyTypeType = Literal["SingleHeader", "SingleWeight"]
DistributionDeployedWaiterName = Literal["distribution_deployed"]
EventTypeType = Literal["origin-request", "origin-response", "viewer-request", "viewer-response"]
FormatType = Literal["URLEncoded"]
FrameOptionsListType = Literal["DENY", "SAMEORIGIN"]
FunctionRuntimeType = Literal["cloudfront-js-1.0", "cloudfront-js-2.0"]
FunctionStageType = Literal["DEVELOPMENT", "LIVE"]
GeoRestrictionTypeType = Literal["blacklist", "none", "whitelist"]
HttpVersionType = Literal["http1.1", "http2", "http2and3", "http3"]
ICPRecordalStatusType = Literal["APPROVED", "PENDING", "SUSPENDED"]
ImportSourceTypeType = Literal["S3"]
InvalidationCompletedWaiterName = Literal["invalidation_completed"]
ItemSelectionType = Literal["all", "none", "whitelist"]
ListCloudFrontOriginAccessIdentitiesPaginatorName = Literal[
    "list_cloud_front_origin_access_identities"
]
ListDistributionsPaginatorName = Literal["list_distributions"]
ListInvalidationsPaginatorName = Literal["list_invalidations"]
ListKeyValueStoresPaginatorName = Literal["list_key_value_stores"]
ListStreamingDistributionsPaginatorName = Literal["list_streaming_distributions"]
MethodType = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
MinimumProtocolVersionType = Literal[
    "SSLv3", "TLSv1", "TLSv1.1_2016", "TLSv1.2_2018", "TLSv1.2_2019", "TLSv1.2_2021", "TLSv1_2016"
]
OriginAccessControlOriginTypesType = Literal["lambda", "mediapackagev2", "mediastore", "s3"]
OriginAccessControlSigningBehaviorsType = Literal["always", "never", "no-override"]
OriginAccessControlSigningProtocolsType = Literal["sigv4"]
OriginProtocolPolicyType = Literal["http-only", "https-only", "match-viewer"]
OriginRequestPolicyCookieBehaviorType = Literal["all", "allExcept", "none", "whitelist"]
OriginRequestPolicyHeaderBehaviorType = Literal[
    "allExcept", "allViewer", "allViewerAndWhitelistCloudFront", "none", "whitelist"
]
OriginRequestPolicyQueryStringBehaviorType = Literal["all", "allExcept", "none", "whitelist"]
OriginRequestPolicyTypeType = Literal["custom", "managed"]
PriceClassType = Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"]
RealtimeMetricsSubscriptionStatusType = Literal["Disabled", "Enabled"]
ReferrerPolicyListType = Literal[
    "no-referrer",
    "no-referrer-when-downgrade",
    "origin",
    "origin-when-cross-origin",
    "same-origin",
    "strict-origin",
    "strict-origin-when-cross-origin",
    "unsafe-url",
]
ResponseHeadersPolicyAccessControlAllowMethodsValuesType = Literal[
    "ALL", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
]
ResponseHeadersPolicyTypeType = Literal["custom", "managed"]
SSLSupportMethodType = Literal["sni-only", "static-ip", "vip"]
SslProtocolType = Literal["SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2"]
StreamingDistributionDeployedWaiterName = Literal["streaming_distribution_deployed"]
ViewerProtocolPolicyType = Literal["allow-all", "https-only", "redirect-to-https"]
