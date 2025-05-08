"""
Type annotations for cloudfront service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudfront.type_defs import AliasICPRecordalTypeDef

    data: AliasICPRecordalTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    CachePolicyCookieBehaviorType,
    CachePolicyHeaderBehaviorType,
    CachePolicyQueryStringBehaviorType,
    CachePolicyTypeType,
    CertificateSourceType,
    CertificateTransparencyLoggingPreferenceType,
    ConnectionModeType,
    ContinuousDeploymentPolicyTypeType,
    CustomizationActionTypeType,
    DistributionResourceTypeType,
    DnsConfigurationStatusType,
    DomainStatusType,
    EventTypeType,
    FrameOptionsListType,
    FunctionRuntimeType,
    FunctionStageType,
    GeoRestrictionTypeType,
    HttpVersionType,
    ICPRecordalStatusType,
    ItemSelectionType,
    ManagedCertificateStatusType,
    MethodType,
    MinimumProtocolVersionType,
    OriginAccessControlOriginTypesType,
    OriginAccessControlSigningBehaviorsType,
    OriginGroupSelectionCriteriaType,
    OriginProtocolPolicyType,
    OriginRequestPolicyCookieBehaviorType,
    OriginRequestPolicyHeaderBehaviorType,
    OriginRequestPolicyQueryStringBehaviorType,
    OriginRequestPolicyTypeType,
    PriceClassType,
    RealtimeMetricsSubscriptionStatusType,
    ReferrerPolicyListType,
    ResponseHeadersPolicyAccessControlAllowMethodsValuesType,
    ResponseHeadersPolicyTypeType,
    SslProtocolType,
    SSLSupportMethodType,
    ValidationTokenHostType,
    ViewerProtocolPolicyType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActiveTrustedKeyGroupsTypeDef",
    "ActiveTrustedSignersTypeDef",
    "AliasICPRecordalTypeDef",
    "AliasesOutputTypeDef",
    "AliasesTypeDef",
    "AliasesUnionTypeDef",
    "AllowedMethodsOutputTypeDef",
    "AllowedMethodsTypeDef",
    "AllowedMethodsUnionTypeDef",
    "AnycastIpListCollectionTypeDef",
    "AnycastIpListSummaryTypeDef",
    "AnycastIpListTypeDef",
    "AssociateAliasRequestTypeDef",
    "AssociateDistributionTenantWebACLRequestTypeDef",
    "AssociateDistributionTenantWebACLResultTypeDef",
    "AssociateDistributionWebACLRequestTypeDef",
    "AssociateDistributionWebACLResultTypeDef",
    "BlobTypeDef",
    "CacheBehaviorOutputTypeDef",
    "CacheBehaviorTypeDef",
    "CacheBehaviorUnionTypeDef",
    "CacheBehaviorsOutputTypeDef",
    "CacheBehaviorsTypeDef",
    "CacheBehaviorsUnionTypeDef",
    "CachePolicyConfigOutputTypeDef",
    "CachePolicyConfigTypeDef",
    "CachePolicyConfigUnionTypeDef",
    "CachePolicyCookiesConfigOutputTypeDef",
    "CachePolicyCookiesConfigTypeDef",
    "CachePolicyHeadersConfigOutputTypeDef",
    "CachePolicyHeadersConfigTypeDef",
    "CachePolicyListTypeDef",
    "CachePolicyQueryStringsConfigOutputTypeDef",
    "CachePolicyQueryStringsConfigTypeDef",
    "CachePolicySummaryTypeDef",
    "CachePolicyTypeDef",
    "CachedMethodsOutputTypeDef",
    "CachedMethodsTypeDef",
    "CachedMethodsUnionTypeDef",
    "CertificateTypeDef",
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    "CloudFrontOriginAccessIdentityListTypeDef",
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    "CloudFrontOriginAccessIdentityTypeDef",
    "ConflictingAliasTypeDef",
    "ConflictingAliasesListTypeDef",
    "ConnectionGroupAssociationFilterTypeDef",
    "ConnectionGroupSummaryTypeDef",
    "ConnectionGroupTypeDef",
    "ContentTypeProfileConfigOutputTypeDef",
    "ContentTypeProfileConfigTypeDef",
    "ContentTypeProfileTypeDef",
    "ContentTypeProfilesOutputTypeDef",
    "ContentTypeProfilesTypeDef",
    "ContinuousDeploymentPolicyConfigOutputTypeDef",
    "ContinuousDeploymentPolicyConfigTypeDef",
    "ContinuousDeploymentPolicyConfigUnionTypeDef",
    "ContinuousDeploymentPolicyListTypeDef",
    "ContinuousDeploymentPolicySummaryTypeDef",
    "ContinuousDeploymentPolicyTypeDef",
    "ContinuousDeploymentSingleHeaderConfigTypeDef",
    "ContinuousDeploymentSingleWeightConfigTypeDef",
    "CookieNamesOutputTypeDef",
    "CookieNamesTypeDef",
    "CookieNamesUnionTypeDef",
    "CookiePreferenceOutputTypeDef",
    "CookiePreferenceTypeDef",
    "CookiePreferenceUnionTypeDef",
    "CopyDistributionRequestTypeDef",
    "CopyDistributionResultTypeDef",
    "CreateAnycastIpListRequestTypeDef",
    "CreateAnycastIpListResultTypeDef",
    "CreateCachePolicyRequestTypeDef",
    "CreateCachePolicyResultTypeDef",
    "CreateCloudFrontOriginAccessIdentityRequestTypeDef",
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    "CreateConnectionGroupRequestTypeDef",
    "CreateConnectionGroupResultTypeDef",
    "CreateContinuousDeploymentPolicyRequestTypeDef",
    "CreateContinuousDeploymentPolicyResultTypeDef",
    "CreateDistributionRequestTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDistributionTenantRequestTypeDef",
    "CreateDistributionTenantResultTypeDef",
    "CreateDistributionWithTagsRequestTypeDef",
    "CreateDistributionWithTagsResultTypeDef",
    "CreateFieldLevelEncryptionConfigRequestTypeDef",
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    "CreateFieldLevelEncryptionProfileRequestTypeDef",
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    "CreateFunctionRequestTypeDef",
    "CreateFunctionResultTypeDef",
    "CreateInvalidationForDistributionTenantRequestTypeDef",
    "CreateInvalidationForDistributionTenantResultTypeDef",
    "CreateInvalidationRequestTypeDef",
    "CreateInvalidationResultTypeDef",
    "CreateKeyGroupRequestTypeDef",
    "CreateKeyGroupResultTypeDef",
    "CreateKeyValueStoreRequestTypeDef",
    "CreateKeyValueStoreResultTypeDef",
    "CreateMonitoringSubscriptionRequestTypeDef",
    "CreateMonitoringSubscriptionResultTypeDef",
    "CreateOriginAccessControlRequestTypeDef",
    "CreateOriginAccessControlResultTypeDef",
    "CreateOriginRequestPolicyRequestTypeDef",
    "CreateOriginRequestPolicyResultTypeDef",
    "CreatePublicKeyRequestTypeDef",
    "CreatePublicKeyResultTypeDef",
    "CreateRealtimeLogConfigRequestTypeDef",
    "CreateRealtimeLogConfigResultTypeDef",
    "CreateResponseHeadersPolicyRequestTypeDef",
    "CreateResponseHeadersPolicyResultTypeDef",
    "CreateStreamingDistributionRequestTypeDef",
    "CreateStreamingDistributionResultTypeDef",
    "CreateStreamingDistributionWithTagsRequestTypeDef",
    "CreateStreamingDistributionWithTagsResultTypeDef",
    "CreateVpcOriginRequestTypeDef",
    "CreateVpcOriginResultTypeDef",
    "CustomErrorResponseTypeDef",
    "CustomErrorResponsesOutputTypeDef",
    "CustomErrorResponsesTypeDef",
    "CustomErrorResponsesUnionTypeDef",
    "CustomHeadersOutputTypeDef",
    "CustomHeadersTypeDef",
    "CustomHeadersUnionTypeDef",
    "CustomOriginConfigOutputTypeDef",
    "CustomOriginConfigTypeDef",
    "CustomOriginConfigUnionTypeDef",
    "CustomizationsOutputTypeDef",
    "CustomizationsTypeDef",
    "CustomizationsUnionTypeDef",
    "DefaultCacheBehaviorOutputTypeDef",
    "DefaultCacheBehaviorTypeDef",
    "DefaultCacheBehaviorUnionTypeDef",
    "DeleteAnycastIpListRequestTypeDef",
    "DeleteCachePolicyRequestTypeDef",
    "DeleteCloudFrontOriginAccessIdentityRequestTypeDef",
    "DeleteConnectionGroupRequestTypeDef",
    "DeleteContinuousDeploymentPolicyRequestTypeDef",
    "DeleteDistributionRequestTypeDef",
    "DeleteDistributionTenantRequestTypeDef",
    "DeleteFieldLevelEncryptionConfigRequestTypeDef",
    "DeleteFieldLevelEncryptionProfileRequestTypeDef",
    "DeleteFunctionRequestTypeDef",
    "DeleteKeyGroupRequestTypeDef",
    "DeleteKeyValueStoreRequestTypeDef",
    "DeleteMonitoringSubscriptionRequestTypeDef",
    "DeleteOriginAccessControlRequestTypeDef",
    "DeleteOriginRequestPolicyRequestTypeDef",
    "DeletePublicKeyRequestTypeDef",
    "DeleteRealtimeLogConfigRequestTypeDef",
    "DeleteResponseHeadersPolicyRequestTypeDef",
    "DeleteStreamingDistributionRequestTypeDef",
    "DeleteVpcOriginRequestTypeDef",
    "DeleteVpcOriginResultTypeDef",
    "DescribeFunctionRequestTypeDef",
    "DescribeFunctionResultTypeDef",
    "DescribeKeyValueStoreRequestTypeDef",
    "DescribeKeyValueStoreResultTypeDef",
    "DisassociateDistributionTenantWebACLRequestTypeDef",
    "DisassociateDistributionTenantWebACLResultTypeDef",
    "DisassociateDistributionWebACLRequestTypeDef",
    "DisassociateDistributionWebACLResultTypeDef",
    "DistributionConfigOutputTypeDef",
    "DistributionConfigTypeDef",
    "DistributionConfigUnionTypeDef",
    "DistributionConfigWithTagsTypeDef",
    "DistributionIdListTypeDef",
    "DistributionListTypeDef",
    "DistributionResourceIdTypeDef",
    "DistributionSummaryTypeDef",
    "DistributionTenantAssociationFilterTypeDef",
    "DistributionTenantSummaryTypeDef",
    "DistributionTenantTypeDef",
    "DistributionTypeDef",
    "DnsConfigurationTypeDef",
    "DomainConflictTypeDef",
    "DomainItemTypeDef",
    "DomainResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionEntitiesOutputTypeDef",
    "EncryptionEntitiesTypeDef",
    "EncryptionEntityOutputTypeDef",
    "EncryptionEntityTypeDef",
    "EndPointTypeDef",
    "FieldLevelEncryptionConfigOutputTypeDef",
    "FieldLevelEncryptionConfigTypeDef",
    "FieldLevelEncryptionConfigUnionTypeDef",
    "FieldLevelEncryptionListTypeDef",
    "FieldLevelEncryptionProfileConfigOutputTypeDef",
    "FieldLevelEncryptionProfileConfigTypeDef",
    "FieldLevelEncryptionProfileConfigUnionTypeDef",
    "FieldLevelEncryptionProfileListTypeDef",
    "FieldLevelEncryptionProfileSummaryTypeDef",
    "FieldLevelEncryptionProfileTypeDef",
    "FieldLevelEncryptionSummaryTypeDef",
    "FieldLevelEncryptionTypeDef",
    "FieldPatternsOutputTypeDef",
    "FieldPatternsTypeDef",
    "ForwardedValuesOutputTypeDef",
    "ForwardedValuesTypeDef",
    "ForwardedValuesUnionTypeDef",
    "FunctionAssociationTypeDef",
    "FunctionAssociationsOutputTypeDef",
    "FunctionAssociationsTypeDef",
    "FunctionAssociationsUnionTypeDef",
    "FunctionConfigOutputTypeDef",
    "FunctionConfigTypeDef",
    "FunctionConfigUnionTypeDef",
    "FunctionListTypeDef",
    "FunctionMetadataTypeDef",
    "FunctionSummaryTypeDef",
    "GeoRestrictionCustomizationOutputTypeDef",
    "GeoRestrictionCustomizationTypeDef",
    "GeoRestrictionOutputTypeDef",
    "GeoRestrictionTypeDef",
    "GeoRestrictionUnionTypeDef",
    "GetAnycastIpListRequestTypeDef",
    "GetAnycastIpListResultTypeDef",
    "GetCachePolicyConfigRequestTypeDef",
    "GetCachePolicyConfigResultTypeDef",
    "GetCachePolicyRequestTypeDef",
    "GetCachePolicyResultTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    "GetCloudFrontOriginAccessIdentityRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    "GetConnectionGroupByRoutingEndpointRequestTypeDef",
    "GetConnectionGroupByRoutingEndpointResultTypeDef",
    "GetConnectionGroupRequestTypeDef",
    "GetConnectionGroupResultTypeDef",
    "GetContinuousDeploymentPolicyConfigRequestTypeDef",
    "GetContinuousDeploymentPolicyConfigResultTypeDef",
    "GetContinuousDeploymentPolicyRequestTypeDef",
    "GetContinuousDeploymentPolicyResultTypeDef",
    "GetDistributionConfigRequestTypeDef",
    "GetDistributionConfigResultTypeDef",
    "GetDistributionRequestTypeDef",
    "GetDistributionRequestWaitTypeDef",
    "GetDistributionResultTypeDef",
    "GetDistributionTenantByDomainRequestTypeDef",
    "GetDistributionTenantByDomainResultTypeDef",
    "GetDistributionTenantRequestTypeDef",
    "GetDistributionTenantResultTypeDef",
    "GetFieldLevelEncryptionConfigRequestTypeDef",
    "GetFieldLevelEncryptionConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileConfigRequestTypeDef",
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileRequestTypeDef",
    "GetFieldLevelEncryptionProfileResultTypeDef",
    "GetFieldLevelEncryptionRequestTypeDef",
    "GetFieldLevelEncryptionResultTypeDef",
    "GetFunctionRequestTypeDef",
    "GetFunctionResultTypeDef",
    "GetInvalidationForDistributionTenantRequestTypeDef",
    "GetInvalidationForDistributionTenantRequestWaitTypeDef",
    "GetInvalidationForDistributionTenantResultTypeDef",
    "GetInvalidationRequestTypeDef",
    "GetInvalidationRequestWaitTypeDef",
    "GetInvalidationResultTypeDef",
    "GetKeyGroupConfigRequestTypeDef",
    "GetKeyGroupConfigResultTypeDef",
    "GetKeyGroupRequestTypeDef",
    "GetKeyGroupResultTypeDef",
    "GetManagedCertificateDetailsRequestTypeDef",
    "GetManagedCertificateDetailsResultTypeDef",
    "GetMonitoringSubscriptionRequestTypeDef",
    "GetMonitoringSubscriptionResultTypeDef",
    "GetOriginAccessControlConfigRequestTypeDef",
    "GetOriginAccessControlConfigResultTypeDef",
    "GetOriginAccessControlRequestTypeDef",
    "GetOriginAccessControlResultTypeDef",
    "GetOriginRequestPolicyConfigRequestTypeDef",
    "GetOriginRequestPolicyConfigResultTypeDef",
    "GetOriginRequestPolicyRequestTypeDef",
    "GetOriginRequestPolicyResultTypeDef",
    "GetPublicKeyConfigRequestTypeDef",
    "GetPublicKeyConfigResultTypeDef",
    "GetPublicKeyRequestTypeDef",
    "GetPublicKeyResultTypeDef",
    "GetRealtimeLogConfigRequestTypeDef",
    "GetRealtimeLogConfigResultTypeDef",
    "GetResponseHeadersPolicyConfigRequestTypeDef",
    "GetResponseHeadersPolicyConfigResultTypeDef",
    "GetResponseHeadersPolicyRequestTypeDef",
    "GetResponseHeadersPolicyResultTypeDef",
    "GetStreamingDistributionConfigRequestTypeDef",
    "GetStreamingDistributionConfigResultTypeDef",
    "GetStreamingDistributionRequestTypeDef",
    "GetStreamingDistributionRequestWaitTypeDef",
    "GetStreamingDistributionResultTypeDef",
    "GetVpcOriginRequestTypeDef",
    "GetVpcOriginResultTypeDef",
    "GrpcConfigTypeDef",
    "HeadersOutputTypeDef",
    "HeadersTypeDef",
    "HeadersUnionTypeDef",
    "ImportSourceTypeDef",
    "InvalidationBatchOutputTypeDef",
    "InvalidationBatchTypeDef",
    "InvalidationBatchUnionTypeDef",
    "InvalidationListTypeDef",
    "InvalidationSummaryTypeDef",
    "InvalidationTypeDef",
    "KGKeyPairIdsTypeDef",
    "KeyGroupConfigOutputTypeDef",
    "KeyGroupConfigTypeDef",
    "KeyGroupConfigUnionTypeDef",
    "KeyGroupListTypeDef",
    "KeyGroupSummaryTypeDef",
    "KeyGroupTypeDef",
    "KeyPairIdsTypeDef",
    "KeyValueStoreAssociationTypeDef",
    "KeyValueStoreAssociationsOutputTypeDef",
    "KeyValueStoreAssociationsTypeDef",
    "KeyValueStoreListTypeDef",
    "KeyValueStoreTypeDef",
    "KinesisStreamConfigTypeDef",
    "LambdaFunctionAssociationTypeDef",
    "LambdaFunctionAssociationsOutputTypeDef",
    "LambdaFunctionAssociationsTypeDef",
    "LambdaFunctionAssociationsUnionTypeDef",
    "ListAnycastIpListsRequestTypeDef",
    "ListAnycastIpListsResultTypeDef",
    "ListCachePoliciesRequestTypeDef",
    "ListCachePoliciesResultTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestTypeDef",
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    "ListConflictingAliasesRequestTypeDef",
    "ListConflictingAliasesResultTypeDef",
    "ListConnectionGroupsRequestPaginateTypeDef",
    "ListConnectionGroupsRequestTypeDef",
    "ListConnectionGroupsResultTypeDef",
    "ListContinuousDeploymentPoliciesRequestTypeDef",
    "ListContinuousDeploymentPoliciesResultTypeDef",
    "ListDistributionTenantsByCustomizationRequestPaginateTypeDef",
    "ListDistributionTenantsByCustomizationRequestTypeDef",
    "ListDistributionTenantsByCustomizationResultTypeDef",
    "ListDistributionTenantsRequestPaginateTypeDef",
    "ListDistributionTenantsRequestTypeDef",
    "ListDistributionTenantsResultTypeDef",
    "ListDistributionsByAnycastIpListIdRequestTypeDef",
    "ListDistributionsByAnycastIpListIdResultTypeDef",
    "ListDistributionsByCachePolicyIdRequestTypeDef",
    "ListDistributionsByCachePolicyIdResultTypeDef",
    "ListDistributionsByConnectionModeRequestPaginateTypeDef",
    "ListDistributionsByConnectionModeRequestTypeDef",
    "ListDistributionsByConnectionModeResultTypeDef",
    "ListDistributionsByKeyGroupRequestTypeDef",
    "ListDistributionsByKeyGroupResultTypeDef",
    "ListDistributionsByOriginRequestPolicyIdRequestTypeDef",
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    "ListDistributionsByRealtimeLogConfigRequestTypeDef",
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdRequestTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    "ListDistributionsByVpcOriginIdRequestTypeDef",
    "ListDistributionsByVpcOriginIdResultTypeDef",
    "ListDistributionsByWebACLIdRequestTypeDef",
    "ListDistributionsByWebACLIdResultTypeDef",
    "ListDistributionsRequestPaginateTypeDef",
    "ListDistributionsRequestTypeDef",
    "ListDistributionsResultTypeDef",
    "ListDomainConflictsRequestPaginateTypeDef",
    "ListDomainConflictsRequestTypeDef",
    "ListDomainConflictsResultTypeDef",
    "ListFieldLevelEncryptionConfigsRequestTypeDef",
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    "ListFieldLevelEncryptionProfilesRequestTypeDef",
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    "ListFunctionsRequestTypeDef",
    "ListFunctionsResultTypeDef",
    "ListInvalidationsForDistributionTenantRequestPaginateTypeDef",
    "ListInvalidationsForDistributionTenantRequestTypeDef",
    "ListInvalidationsForDistributionTenantResultTypeDef",
    "ListInvalidationsRequestPaginateTypeDef",
    "ListInvalidationsRequestTypeDef",
    "ListInvalidationsResultTypeDef",
    "ListKeyGroupsRequestTypeDef",
    "ListKeyGroupsResultTypeDef",
    "ListKeyValueStoresRequestPaginateTypeDef",
    "ListKeyValueStoresRequestTypeDef",
    "ListKeyValueStoresResultTypeDef",
    "ListOriginAccessControlsRequestTypeDef",
    "ListOriginAccessControlsResultTypeDef",
    "ListOriginRequestPoliciesRequestTypeDef",
    "ListOriginRequestPoliciesResultTypeDef",
    "ListPublicKeysRequestPaginateTypeDef",
    "ListPublicKeysRequestTypeDef",
    "ListPublicKeysResultTypeDef",
    "ListRealtimeLogConfigsRequestTypeDef",
    "ListRealtimeLogConfigsResultTypeDef",
    "ListResponseHeadersPoliciesRequestTypeDef",
    "ListResponseHeadersPoliciesResultTypeDef",
    "ListStreamingDistributionsRequestPaginateTypeDef",
    "ListStreamingDistributionsRequestTypeDef",
    "ListStreamingDistributionsResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "ListVpcOriginsRequestTypeDef",
    "ListVpcOriginsResultTypeDef",
    "LoggingConfigTypeDef",
    "ManagedCertificateDetailsTypeDef",
    "ManagedCertificateRequestTypeDef",
    "MonitoringSubscriptionTypeDef",
    "OriginAccessControlConfigTypeDef",
    "OriginAccessControlListTypeDef",
    "OriginAccessControlSummaryTypeDef",
    "OriginAccessControlTypeDef",
    "OriginCustomHeaderTypeDef",
    "OriginGroupFailoverCriteriaOutputTypeDef",
    "OriginGroupFailoverCriteriaTypeDef",
    "OriginGroupFailoverCriteriaUnionTypeDef",
    "OriginGroupMemberTypeDef",
    "OriginGroupMembersOutputTypeDef",
    "OriginGroupMembersTypeDef",
    "OriginGroupMembersUnionTypeDef",
    "OriginGroupOutputTypeDef",
    "OriginGroupTypeDef",
    "OriginGroupUnionTypeDef",
    "OriginGroupsOutputTypeDef",
    "OriginGroupsTypeDef",
    "OriginGroupsUnionTypeDef",
    "OriginOutputTypeDef",
    "OriginRequestPolicyConfigOutputTypeDef",
    "OriginRequestPolicyConfigTypeDef",
    "OriginRequestPolicyConfigUnionTypeDef",
    "OriginRequestPolicyCookiesConfigOutputTypeDef",
    "OriginRequestPolicyCookiesConfigTypeDef",
    "OriginRequestPolicyHeadersConfigOutputTypeDef",
    "OriginRequestPolicyHeadersConfigTypeDef",
    "OriginRequestPolicyListTypeDef",
    "OriginRequestPolicyQueryStringsConfigOutputTypeDef",
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    "OriginRequestPolicySummaryTypeDef",
    "OriginRequestPolicyTypeDef",
    "OriginShieldTypeDef",
    "OriginSslProtocolsOutputTypeDef",
    "OriginSslProtocolsTypeDef",
    "OriginSslProtocolsUnionTypeDef",
    "OriginTypeDef",
    "OriginUnionTypeDef",
    "OriginsOutputTypeDef",
    "OriginsTypeDef",
    "OriginsUnionTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterDefinitionSchemaTypeDef",
    "ParameterDefinitionTypeDef",
    "ParameterTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginOutputTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    "PathsOutputTypeDef",
    "PathsTypeDef",
    "PublicKeyConfigTypeDef",
    "PublicKeyListTypeDef",
    "PublicKeySummaryTypeDef",
    "PublicKeyTypeDef",
    "PublishFunctionRequestTypeDef",
    "PublishFunctionResultTypeDef",
    "QueryArgProfileConfigOutputTypeDef",
    "QueryArgProfileConfigTypeDef",
    "QueryArgProfileTypeDef",
    "QueryArgProfilesOutputTypeDef",
    "QueryArgProfilesTypeDef",
    "QueryStringCacheKeysOutputTypeDef",
    "QueryStringCacheKeysTypeDef",
    "QueryStringCacheKeysUnionTypeDef",
    "QueryStringNamesOutputTypeDef",
    "QueryStringNamesTypeDef",
    "RealtimeLogConfigTypeDef",
    "RealtimeLogConfigsTypeDef",
    "RealtimeMetricsSubscriptionConfigTypeDef",
    "ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef",
    "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
    "ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef",
    "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
    "ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef",
    "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
    "ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef",
    "ResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    "ResponseHeadersPolicyConfigOutputTypeDef",
    "ResponseHeadersPolicyConfigTypeDef",
    "ResponseHeadersPolicyConfigUnionTypeDef",
    "ResponseHeadersPolicyContentSecurityPolicyTypeDef",
    "ResponseHeadersPolicyContentTypeOptionsTypeDef",
    "ResponseHeadersPolicyCorsConfigOutputTypeDef",
    "ResponseHeadersPolicyCorsConfigTypeDef",
    "ResponseHeadersPolicyCustomHeaderTypeDef",
    "ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef",
    "ResponseHeadersPolicyCustomHeadersConfigTypeDef",
    "ResponseHeadersPolicyFrameOptionsTypeDef",
    "ResponseHeadersPolicyListTypeDef",
    "ResponseHeadersPolicyReferrerPolicyTypeDef",
    "ResponseHeadersPolicyRemoveHeaderTypeDef",
    "ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef",
    "ResponseHeadersPolicyRemoveHeadersConfigTypeDef",
    "ResponseHeadersPolicySecurityHeadersConfigTypeDef",
    "ResponseHeadersPolicyServerTimingHeadersConfigTypeDef",
    "ResponseHeadersPolicyStrictTransportSecurityTypeDef",
    "ResponseHeadersPolicySummaryTypeDef",
    "ResponseHeadersPolicyTypeDef",
    "ResponseHeadersPolicyXSSProtectionTypeDef",
    "ResponseMetadataTypeDef",
    "RestrictionsOutputTypeDef",
    "RestrictionsTypeDef",
    "RestrictionsUnionTypeDef",
    "S3OriginConfigTypeDef",
    "S3OriginTypeDef",
    "SessionStickinessConfigTypeDef",
    "SignerTypeDef",
    "StagingDistributionDnsNamesOutputTypeDef",
    "StagingDistributionDnsNamesTypeDef",
    "StatusCodesOutputTypeDef",
    "StatusCodesTypeDef",
    "StatusCodesUnionTypeDef",
    "StreamingDistributionConfigOutputTypeDef",
    "StreamingDistributionConfigTypeDef",
    "StreamingDistributionConfigUnionTypeDef",
    "StreamingDistributionConfigWithTagsTypeDef",
    "StreamingDistributionListTypeDef",
    "StreamingDistributionSummaryTypeDef",
    "StreamingDistributionTypeDef",
    "StreamingLoggingConfigTypeDef",
    "StringSchemaConfigTypeDef",
    "TagKeysTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TagsOutputTypeDef",
    "TagsTypeDef",
    "TagsUnionTypeDef",
    "TenantConfigOutputTypeDef",
    "TenantConfigTypeDef",
    "TenantConfigUnionTypeDef",
    "TestFunctionRequestTypeDef",
    "TestFunctionResultTypeDef",
    "TestResultTypeDef",
    "TrafficConfigTypeDef",
    "TrustedKeyGroupsOutputTypeDef",
    "TrustedKeyGroupsTypeDef",
    "TrustedKeyGroupsUnionTypeDef",
    "TrustedSignersOutputTypeDef",
    "TrustedSignersTypeDef",
    "TrustedSignersUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCachePolicyRequestTypeDef",
    "UpdateCachePolicyResultTypeDef",
    "UpdateCloudFrontOriginAccessIdentityRequestTypeDef",
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    "UpdateConnectionGroupRequestTypeDef",
    "UpdateConnectionGroupResultTypeDef",
    "UpdateContinuousDeploymentPolicyRequestTypeDef",
    "UpdateContinuousDeploymentPolicyResultTypeDef",
    "UpdateDistributionRequestTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateDistributionTenantRequestTypeDef",
    "UpdateDistributionTenantResultTypeDef",
    "UpdateDistributionWithStagingConfigRequestTypeDef",
    "UpdateDistributionWithStagingConfigResultTypeDef",
    "UpdateDomainAssociationRequestTypeDef",
    "UpdateDomainAssociationResultTypeDef",
    "UpdateFieldLevelEncryptionConfigRequestTypeDef",
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    "UpdateFieldLevelEncryptionProfileRequestTypeDef",
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    "UpdateFunctionRequestTypeDef",
    "UpdateFunctionResultTypeDef",
    "UpdateKeyGroupRequestTypeDef",
    "UpdateKeyGroupResultTypeDef",
    "UpdateKeyValueStoreRequestTypeDef",
    "UpdateKeyValueStoreResultTypeDef",
    "UpdateOriginAccessControlRequestTypeDef",
    "UpdateOriginAccessControlResultTypeDef",
    "UpdateOriginRequestPolicyRequestTypeDef",
    "UpdateOriginRequestPolicyResultTypeDef",
    "UpdatePublicKeyRequestTypeDef",
    "UpdatePublicKeyResultTypeDef",
    "UpdateRealtimeLogConfigRequestTypeDef",
    "UpdateRealtimeLogConfigResultTypeDef",
    "UpdateResponseHeadersPolicyRequestTypeDef",
    "UpdateResponseHeadersPolicyResultTypeDef",
    "UpdateStreamingDistributionRequestTypeDef",
    "UpdateStreamingDistributionResultTypeDef",
    "UpdateVpcOriginRequestTypeDef",
    "UpdateVpcOriginResultTypeDef",
    "ValidationTokenDetailTypeDef",
    "VerifyDnsConfigurationRequestTypeDef",
    "VerifyDnsConfigurationResultTypeDef",
    "ViewerCertificateTypeDef",
    "VpcOriginConfigTypeDef",
    "VpcOriginEndpointConfigOutputTypeDef",
    "VpcOriginEndpointConfigTypeDef",
    "VpcOriginEndpointConfigUnionTypeDef",
    "VpcOriginListTypeDef",
    "VpcOriginSummaryTypeDef",
    "VpcOriginTypeDef",
    "WaiterConfigTypeDef",
    "WebAclCustomizationTypeDef",
)

class AliasICPRecordalTypeDef(TypedDict):
    CNAME: NotRequired[str]
    ICPRecordalStatus: NotRequired[ICPRecordalStatusType]

class AliasesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class AliasesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class CachedMethodsOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[MethodType]

class AnycastIpListSummaryTypeDef(TypedDict):
    Id: str
    Name: str
    Status: str
    Arn: str
    IpCount: int
    LastModifiedTime: datetime

class AnycastIpListTypeDef(TypedDict):
    Id: str
    Name: str
    Status: str
    Arn: str
    AnycastIps: List[str]
    IpCount: int
    LastModifiedTime: datetime

class AssociateAliasRequestTypeDef(TypedDict):
    TargetDistributionId: str
    Alias: str

class AssociateDistributionTenantWebACLRequestTypeDef(TypedDict):
    Id: str
    WebACLArn: str
    IfMatch: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateDistributionWebACLRequestTypeDef(TypedDict):
    Id: str
    WebACLArn: str
    IfMatch: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class GrpcConfigTypeDef(TypedDict):
    Enabled: bool

class TrustedKeyGroupsOutputTypeDef(TypedDict):
    Enabled: bool
    Quantity: int
    Items: NotRequired[List[str]]

class TrustedSignersOutputTypeDef(TypedDict):
    Enabled: bool
    Quantity: int
    Items: NotRequired[List[str]]

class CookieNamesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class CookieNamesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class HeadersOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class HeadersTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class QueryStringNamesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class QueryStringNamesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class CachedMethodsTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[MethodType]

class CertificateTypeDef(TypedDict):
    Arn: str

class CloudFrontOriginAccessIdentityConfigTypeDef(TypedDict):
    CallerReference: str
    Comment: str

class CloudFrontOriginAccessIdentitySummaryTypeDef(TypedDict):
    Id: str
    S3CanonicalUserId: str
    Comment: str

class ConflictingAliasTypeDef(TypedDict):
    Alias: NotRequired[str]
    DistributionId: NotRequired[str]
    AccountId: NotRequired[str]

class ConnectionGroupAssociationFilterTypeDef(TypedDict):
    AnycastIpListId: NotRequired[str]

class ConnectionGroupSummaryTypeDef(TypedDict):
    Id: str
    Name: str
    Arn: str
    RoutingEndpoint: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    ETag: str
    AnycastIpListId: NotRequired[str]
    Enabled: NotRequired[bool]
    Status: NotRequired[str]
    IsDefault: NotRequired[bool]

class ContentTypeProfileTypeDef(TypedDict):
    Format: Literal["URLEncoded"]
    ContentType: str
    ProfileId: NotRequired[str]

class StagingDistributionDnsNamesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class StagingDistributionDnsNamesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class ContinuousDeploymentSingleHeaderConfigTypeDef(TypedDict):
    Header: str
    Value: str

class SessionStickinessConfigTypeDef(TypedDict):
    IdleTTL: int
    MaximumTTL: int

class CopyDistributionRequestTypeDef(TypedDict):
    PrimaryDistributionId: str
    CallerReference: str
    Staging: NotRequired[bool]
    IfMatch: NotRequired[str]
    Enabled: NotRequired[bool]

class DomainItemTypeDef(TypedDict):
    Domain: str

class ManagedCertificateRequestTypeDef(TypedDict):
    ValidationTokenHost: ValidationTokenHostType
    PrimaryDomainName: NotRequired[str]
    CertificateTransparencyLoggingPreference: NotRequired[
        CertificateTransparencyLoggingPreferenceType
    ]

class ParameterTypeDef(TypedDict):
    Name: str
    Value: str

class ImportSourceTypeDef(TypedDict):
    SourceType: Literal["S3"]
    SourceARN: str

class KeyValueStoreTypeDef(TypedDict):
    Name: str
    Id: str
    Comment: str
    ARN: str
    LastModifiedTime: datetime
    Status: NotRequired[str]

class OriginAccessControlConfigTypeDef(TypedDict):
    Name: str
    SigningProtocol: Literal["sigv4"]
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType
    Description: NotRequired[str]

class PublicKeyConfigTypeDef(TypedDict):
    CallerReference: str
    Name: str
    EncodedKey: str
    Comment: NotRequired[str]

class CustomErrorResponseTypeDef(TypedDict):
    ErrorCode: int
    ResponsePagePath: NotRequired[str]
    ResponseCode: NotRequired[str]
    ErrorCachingMinTTL: NotRequired[int]

class OriginCustomHeaderTypeDef(TypedDict):
    HeaderName: str
    HeaderValue: str

class OriginSslProtocolsOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[SslProtocolType]

class GeoRestrictionCustomizationOutputTypeDef(TypedDict):
    RestrictionType: GeoRestrictionTypeType
    Locations: NotRequired[List[str]]

class WebAclCustomizationTypeDef(TypedDict):
    Action: CustomizationActionTypeType
    Arn: NotRequired[str]

class GeoRestrictionCustomizationTypeDef(TypedDict):
    RestrictionType: GeoRestrictionTypeType
    Locations: NotRequired[Sequence[str]]

class DeleteAnycastIpListRequestTypeDef(TypedDict):
    Id: str
    IfMatch: str

class DeleteCachePolicyRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteCloudFrontOriginAccessIdentityRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteConnectionGroupRequestTypeDef(TypedDict):
    Id: str
    IfMatch: str

class DeleteContinuousDeploymentPolicyRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteDistributionRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteDistributionTenantRequestTypeDef(TypedDict):
    Id: str
    IfMatch: str

class DeleteFieldLevelEncryptionConfigRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteFieldLevelEncryptionProfileRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteFunctionRequestTypeDef(TypedDict):
    Name: str
    IfMatch: str

class DeleteKeyGroupRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteKeyValueStoreRequestTypeDef(TypedDict):
    Name: str
    IfMatch: str

class DeleteMonitoringSubscriptionRequestTypeDef(TypedDict):
    DistributionId: str

class DeleteOriginAccessControlRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteOriginRequestPolicyRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeletePublicKeyRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteRealtimeLogConfigRequestTypeDef(TypedDict):
    Name: NotRequired[str]
    ARN: NotRequired[str]

class DeleteResponseHeadersPolicyRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteStreamingDistributionRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DeleteVpcOriginRequestTypeDef(TypedDict):
    Id: str
    IfMatch: str

class DescribeFunctionRequestTypeDef(TypedDict):
    Name: str
    Stage: NotRequired[FunctionStageType]

class DescribeKeyValueStoreRequestTypeDef(TypedDict):
    Name: str

class DisassociateDistributionTenantWebACLRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class DisassociateDistributionWebACLRequestTypeDef(TypedDict):
    Id: str
    IfMatch: NotRequired[str]

class LoggingConfigTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    IncludeCookies: NotRequired[bool]
    Bucket: NotRequired[str]
    Prefix: NotRequired[str]

class ViewerCertificateTypeDef(TypedDict):
    CloudFrontDefaultCertificate: NotRequired[bool]
    IAMCertificateId: NotRequired[str]
    ACMCertificateArn: NotRequired[str]
    SSLSupportMethod: NotRequired[SSLSupportMethodType]
    MinimumProtocolVersion: NotRequired[MinimumProtocolVersionType]
    Certificate: NotRequired[str]
    CertificateSource: NotRequired[CertificateSourceType]

class DistributionIdListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[str]]

class DistributionResourceIdTypeDef(TypedDict):
    DistributionId: NotRequired[str]
    DistributionTenantId: NotRequired[str]

class DistributionTenantAssociationFilterTypeDef(TypedDict):
    DistributionId: NotRequired[str]
    ConnectionGroupId: NotRequired[str]

class DomainResultTypeDef(TypedDict):
    Domain: str
    Status: NotRequired[DomainStatusType]

class DnsConfigurationTypeDef(TypedDict):
    Domain: str
    Status: DnsConfigurationStatusType
    Reason: NotRequired[str]

class DomainConflictTypeDef(TypedDict):
    Domain: str
    ResourceType: DistributionResourceTypeType
    ResourceId: str
    AccountId: str

class FieldPatternsOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class FieldPatternsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class KinesisStreamConfigTypeDef(TypedDict):
    RoleARN: str
    StreamARN: str

class QueryStringCacheKeysOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class FunctionAssociationTypeDef(TypedDict):
    FunctionARN: str
    EventType: EventTypeType

class FunctionMetadataTypeDef(TypedDict):
    FunctionARN: str
    LastModifiedTime: datetime
    Stage: NotRequired[FunctionStageType]
    CreatedTime: NotRequired[datetime]

class GeoRestrictionOutputTypeDef(TypedDict):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: NotRequired[List[str]]

class GeoRestrictionTypeDef(TypedDict):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: NotRequired[Sequence[str]]

class GetAnycastIpListRequestTypeDef(TypedDict):
    Id: str

class GetCachePolicyConfigRequestTypeDef(TypedDict):
    Id: str

class GetCachePolicyRequestTypeDef(TypedDict):
    Id: str

class GetCloudFrontOriginAccessIdentityConfigRequestTypeDef(TypedDict):
    Id: str

class GetCloudFrontOriginAccessIdentityRequestTypeDef(TypedDict):
    Id: str

class GetConnectionGroupByRoutingEndpointRequestTypeDef(TypedDict):
    RoutingEndpoint: str

class GetConnectionGroupRequestTypeDef(TypedDict):
    Identifier: str

class GetContinuousDeploymentPolicyConfigRequestTypeDef(TypedDict):
    Id: str

class GetContinuousDeploymentPolicyRequestTypeDef(TypedDict):
    Id: str

class GetDistributionConfigRequestTypeDef(TypedDict):
    Id: str

class GetDistributionRequestTypeDef(TypedDict):
    Id: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetDistributionTenantByDomainRequestTypeDef(TypedDict):
    Domain: str

class GetDistributionTenantRequestTypeDef(TypedDict):
    Identifier: str

class GetFieldLevelEncryptionConfigRequestTypeDef(TypedDict):
    Id: str

class GetFieldLevelEncryptionProfileConfigRequestTypeDef(TypedDict):
    Id: str

class GetFieldLevelEncryptionProfileRequestTypeDef(TypedDict):
    Id: str

class GetFieldLevelEncryptionRequestTypeDef(TypedDict):
    Id: str

class GetFunctionRequestTypeDef(TypedDict):
    Name: str
    Stage: NotRequired[FunctionStageType]

class GetInvalidationForDistributionTenantRequestTypeDef(TypedDict):
    DistributionTenantId: str
    Id: str

class GetInvalidationRequestTypeDef(TypedDict):
    DistributionId: str
    Id: str

class GetKeyGroupConfigRequestTypeDef(TypedDict):
    Id: str

class KeyGroupConfigOutputTypeDef(TypedDict):
    Name: str
    Items: List[str]
    Comment: NotRequired[str]

class GetKeyGroupRequestTypeDef(TypedDict):
    Id: str

class GetManagedCertificateDetailsRequestTypeDef(TypedDict):
    Identifier: str

class GetMonitoringSubscriptionRequestTypeDef(TypedDict):
    DistributionId: str

class GetOriginAccessControlConfigRequestTypeDef(TypedDict):
    Id: str

class GetOriginAccessControlRequestTypeDef(TypedDict):
    Id: str

class GetOriginRequestPolicyConfigRequestTypeDef(TypedDict):
    Id: str

class GetOriginRequestPolicyRequestTypeDef(TypedDict):
    Id: str

class GetPublicKeyConfigRequestTypeDef(TypedDict):
    Id: str

class GetPublicKeyRequestTypeDef(TypedDict):
    Id: str

class GetRealtimeLogConfigRequestTypeDef(TypedDict):
    Name: NotRequired[str]
    ARN: NotRequired[str]

class GetResponseHeadersPolicyConfigRequestTypeDef(TypedDict):
    Id: str

class GetResponseHeadersPolicyRequestTypeDef(TypedDict):
    Id: str

class GetStreamingDistributionConfigRequestTypeDef(TypedDict):
    Id: str

class GetStreamingDistributionRequestTypeDef(TypedDict):
    Id: str

class GetVpcOriginRequestTypeDef(TypedDict):
    Id: str

class PathsOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class PathsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class InvalidationSummaryTypeDef(TypedDict):
    Id: str
    CreateTime: datetime
    Status: str

class KeyPairIdsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class KeyGroupConfigTypeDef(TypedDict):
    Name: str
    Items: Sequence[str]
    Comment: NotRequired[str]

class KeyValueStoreAssociationTypeDef(TypedDict):
    KeyValueStoreARN: str

class LambdaFunctionAssociationTypeDef(TypedDict):
    LambdaFunctionARN: str
    EventType: EventTypeType
    IncludeBody: NotRequired[bool]

class ListAnycastIpListsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

ListCachePoliciesRequestTypeDef = TypedDict(
    "ListCachePoliciesRequestTypeDef",
    {
        "Type": NotRequired[CachePolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCloudFrontOriginAccessIdentitiesRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListConflictingAliasesRequestTypeDef(TypedDict):
    DistributionId: str
    Alias: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListContinuousDeploymentPoliciesRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionTenantsByCustomizationRequestTypeDef(TypedDict):
    WebACLArn: NotRequired[str]
    CertificateArn: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListDistributionsByAnycastIpListIdRequestTypeDef(TypedDict):
    AnycastIpListId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionsByCachePolicyIdRequestTypeDef(TypedDict):
    CachePolicyId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionsByConnectionModeRequestTypeDef(TypedDict):
    ConnectionMode: ConnectionModeType
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListDistributionsByKeyGroupRequestTypeDef(TypedDict):
    KeyGroupId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionsByOriginRequestPolicyIdRequestTypeDef(TypedDict):
    OriginRequestPolicyId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionsByRealtimeLogConfigRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]
    RealtimeLogConfigName: NotRequired[str]
    RealtimeLogConfigArn: NotRequired[str]

class ListDistributionsByResponseHeadersPolicyIdRequestTypeDef(TypedDict):
    ResponseHeadersPolicyId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionsByVpcOriginIdRequestTypeDef(TypedDict):
    VpcOriginId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionsByWebACLIdRequestTypeDef(TypedDict):
    WebACLId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListDistributionsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListFieldLevelEncryptionConfigsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListFieldLevelEncryptionProfilesRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListFunctionsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]
    Stage: NotRequired[FunctionStageType]

class ListInvalidationsForDistributionTenantRequestTypeDef(TypedDict):
    Id: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListInvalidationsRequestTypeDef(TypedDict):
    DistributionId: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListKeyGroupsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListKeyValueStoresRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]
    Status: NotRequired[str]

class ListOriginAccessControlsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

ListOriginRequestPoliciesRequestTypeDef = TypedDict(
    "ListOriginRequestPoliciesRequestTypeDef",
    {
        "Type": NotRequired[OriginRequestPolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

class ListPublicKeysRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListRealtimeLogConfigsRequestTypeDef(TypedDict):
    MaxItems: NotRequired[str]
    Marker: NotRequired[str]

ListResponseHeadersPoliciesRequestTypeDef = TypedDict(
    "ListResponseHeadersPoliciesRequestTypeDef",
    {
        "Type": NotRequired[ResponseHeadersPolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

class ListStreamingDistributionsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    Resource: str

class ListVpcOriginsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ValidationTokenDetailTypeDef(TypedDict):
    Domain: str
    RedirectTo: NotRequired[str]
    RedirectFrom: NotRequired[str]

class RealtimeMetricsSubscriptionConfigTypeDef(TypedDict):
    RealtimeMetricsSubscriptionStatus: RealtimeMetricsSubscriptionStatusType

class OriginAccessControlSummaryTypeDef(TypedDict):
    Id: str
    Description: str
    Name: str
    SigningProtocol: Literal["sigv4"]
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType

class StatusCodesOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[int]

class OriginGroupMemberTypeDef(TypedDict):
    OriginId: str

class OriginShieldTypeDef(TypedDict):
    Enabled: bool
    OriginShieldRegion: NotRequired[str]

class S3OriginConfigTypeDef(TypedDict):
    OriginAccessIdentity: str

class VpcOriginConfigTypeDef(TypedDict):
    VpcOriginId: str
    OriginReadTimeout: NotRequired[int]
    OriginKeepaliveTimeout: NotRequired[int]

class OriginSslProtocolsTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[SslProtocolType]

StringSchemaConfigTypeDef = TypedDict(
    "StringSchemaConfigTypeDef",
    {
        "Required": bool,
        "Comment": NotRequired[str],
        "DefaultValue": NotRequired[str],
    },
)

class PublicKeySummaryTypeDef(TypedDict):
    Id: str
    Name: str
    CreatedTime: datetime
    EncodedKey: str
    Comment: NotRequired[str]

class PublishFunctionRequestTypeDef(TypedDict):
    Name: str
    IfMatch: str

class QueryArgProfileTypeDef(TypedDict):
    QueryArg: str
    ProfileId: str

class QueryStringCacheKeysTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[str]

class ResponseHeadersPolicyAccessControlAllowHeadersTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[str]

class ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]

class ResponseHeadersPolicyAccessControlAllowMethodsTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]

class ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[str]

class ResponseHeadersPolicyAccessControlAllowOriginsTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[str]

class ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[str]]

class ResponseHeadersPolicyAccessControlExposeHeadersTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[str]]

class ResponseHeadersPolicyServerTimingHeadersConfigTypeDef(TypedDict):
    Enabled: bool
    SamplingRate: NotRequired[float]

class ResponseHeadersPolicyContentSecurityPolicyTypeDef(TypedDict):
    Override: bool
    ContentSecurityPolicy: str

class ResponseHeadersPolicyContentTypeOptionsTypeDef(TypedDict):
    Override: bool

class ResponseHeadersPolicyCustomHeaderTypeDef(TypedDict):
    Header: str
    Value: str
    Override: bool

class ResponseHeadersPolicyFrameOptionsTypeDef(TypedDict):
    Override: bool
    FrameOption: FrameOptionsListType

class ResponseHeadersPolicyReferrerPolicyTypeDef(TypedDict):
    Override: bool
    ReferrerPolicy: ReferrerPolicyListType

class ResponseHeadersPolicyRemoveHeaderTypeDef(TypedDict):
    Header: str

class ResponseHeadersPolicyStrictTransportSecurityTypeDef(TypedDict):
    Override: bool
    AccessControlMaxAgeSec: int
    IncludeSubdomains: NotRequired[bool]
    Preload: NotRequired[bool]

class ResponseHeadersPolicyXSSProtectionTypeDef(TypedDict):
    Override: bool
    Protection: bool
    ModeBlock: NotRequired[bool]
    ReportUri: NotRequired[str]

class S3OriginTypeDef(TypedDict):
    DomainName: str
    OriginAccessIdentity: str

class StatusCodesTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[int]

class StreamingLoggingConfigTypeDef(TypedDict):
    Enabled: bool
    Bucket: str
    Prefix: str

class TagKeysTypeDef(TypedDict):
    Items: NotRequired[Sequence[str]]

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class TrustedKeyGroupsTypeDef(TypedDict):
    Enabled: bool
    Quantity: int
    Items: NotRequired[Sequence[str]]

class TrustedSignersTypeDef(TypedDict):
    Enabled: bool
    Quantity: int
    Items: NotRequired[Sequence[str]]

class UpdateConnectionGroupRequestTypeDef(TypedDict):
    Id: str
    IfMatch: str
    Ipv6Enabled: NotRequired[bool]
    AnycastIpListId: NotRequired[str]
    Enabled: NotRequired[bool]

class UpdateDistributionWithStagingConfigRequestTypeDef(TypedDict):
    Id: str
    StagingDistributionId: NotRequired[str]
    IfMatch: NotRequired[str]

class UpdateKeyValueStoreRequestTypeDef(TypedDict):
    Name: str
    Comment: str
    IfMatch: str

class VerifyDnsConfigurationRequestTypeDef(TypedDict):
    Identifier: str
    Domain: NotRequired[str]

class VpcOriginSummaryTypeDef(TypedDict):
    Id: str
    Name: str
    Status: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    Arn: str
    OriginEndpointArn: str

AliasesUnionTypeDef = Union[AliasesTypeDef, AliasesOutputTypeDef]

class AllowedMethodsOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[MethodType]
    CachedMethods: NotRequired[CachedMethodsOutputTypeDef]

class AnycastIpListCollectionTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    Items: NotRequired[List[AnycastIpListSummaryTypeDef]]
    NextMarker: NotRequired[str]

class AssociateDistributionTenantWebACLResultTypeDef(TypedDict):
    Id: str
    WebACLArn: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDistributionWebACLResultTypeDef(TypedDict):
    Id: str
    WebACLArn: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnycastIpListResultTypeDef(TypedDict):
    AnycastIpList: AnycastIpListTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateDistributionTenantWebACLResultTypeDef(TypedDict):
    Id: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateDistributionWebACLResultTypeDef(TypedDict):
    Id: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnycastIpListResultTypeDef(TypedDict):
    AnycastIpList: AnycastIpListTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionResultTypeDef(TypedDict):
    FunctionCode: StreamingBody
    ETag: str
    ContentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainAssociationResultTypeDef(TypedDict):
    Domain: str
    ResourceId: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestFunctionRequestTypeDef(TypedDict):
    Name: str
    IfMatch: str
    EventObject: BlobTypeDef
    Stage: NotRequired[FunctionStageType]

class CachePolicyCookiesConfigOutputTypeDef(TypedDict):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: NotRequired[CookieNamesOutputTypeDef]

class CookiePreferenceOutputTypeDef(TypedDict):
    Forward: ItemSelectionType
    WhitelistedNames: NotRequired[CookieNamesOutputTypeDef]

class OriginRequestPolicyCookiesConfigOutputTypeDef(TypedDict):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: NotRequired[CookieNamesOutputTypeDef]

class CachePolicyCookiesConfigTypeDef(TypedDict):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: NotRequired[CookieNamesTypeDef]

CookieNamesUnionTypeDef = Union[CookieNamesTypeDef, CookieNamesOutputTypeDef]

class OriginRequestPolicyCookiesConfigTypeDef(TypedDict):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: NotRequired[CookieNamesTypeDef]

class CachePolicyHeadersConfigOutputTypeDef(TypedDict):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: NotRequired[HeadersOutputTypeDef]

class OriginRequestPolicyHeadersConfigOutputTypeDef(TypedDict):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: NotRequired[HeadersOutputTypeDef]

class CachePolicyHeadersConfigTypeDef(TypedDict):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: NotRequired[HeadersTypeDef]

HeadersUnionTypeDef = Union[HeadersTypeDef, HeadersOutputTypeDef]

class OriginRequestPolicyHeadersConfigTypeDef(TypedDict):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: NotRequired[HeadersTypeDef]

class CachePolicyQueryStringsConfigOutputTypeDef(TypedDict):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: NotRequired[QueryStringNamesOutputTypeDef]

class OriginRequestPolicyQueryStringsConfigOutputTypeDef(TypedDict):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: NotRequired[QueryStringNamesOutputTypeDef]

class CachePolicyQueryStringsConfigTypeDef(TypedDict):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: NotRequired[QueryStringNamesTypeDef]

class OriginRequestPolicyQueryStringsConfigTypeDef(TypedDict):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: NotRequired[QueryStringNamesTypeDef]

CachedMethodsUnionTypeDef = Union[CachedMethodsTypeDef, CachedMethodsOutputTypeDef]

class CloudFrontOriginAccessIdentityTypeDef(TypedDict):
    Id: str
    S3CanonicalUserId: str
    CloudFrontOriginAccessIdentityConfig: NotRequired[CloudFrontOriginAccessIdentityConfigTypeDef]

class CreateCloudFrontOriginAccessIdentityRequestTypeDef(TypedDict):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef

class GetCloudFrontOriginAccessIdentityConfigResultTypeDef(TypedDict):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCloudFrontOriginAccessIdentityRequestTypeDef(TypedDict):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef
    Id: str
    IfMatch: NotRequired[str]

class CloudFrontOriginAccessIdentityListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[CloudFrontOriginAccessIdentitySummaryTypeDef]]

class ConflictingAliasesListTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    MaxItems: NotRequired[int]
    Quantity: NotRequired[int]
    Items: NotRequired[List[ConflictingAliasTypeDef]]

class ListConnectionGroupsRequestTypeDef(TypedDict):
    AssociationFilter: NotRequired[ConnectionGroupAssociationFilterTypeDef]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListConnectionGroupsResultTypeDef(TypedDict):
    NextMarker: str
    ConnectionGroups: List[ConnectionGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ContentTypeProfilesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[ContentTypeProfileTypeDef]]

class ContentTypeProfilesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[ContentTypeProfileTypeDef]]

class ContinuousDeploymentSingleWeightConfigTypeDef(TypedDict):
    Weight: float
    SessionStickinessConfig: NotRequired[SessionStickinessConfigTypeDef]

class CreateKeyValueStoreRequestTypeDef(TypedDict):
    Name: str
    Comment: NotRequired[str]
    ImportSource: NotRequired[ImportSourceTypeDef]

class CreateKeyValueStoreResultTypeDef(TypedDict):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyValueStoreResultTypeDef(TypedDict):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class KeyValueStoreListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[KeyValueStoreTypeDef]]

class UpdateKeyValueStoreResultTypeDef(TypedDict):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOriginAccessControlRequestTypeDef(TypedDict):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef

class GetOriginAccessControlConfigResultTypeDef(TypedDict):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginAccessControlTypeDef(TypedDict):
    Id: str
    OriginAccessControlConfig: NotRequired[OriginAccessControlConfigTypeDef]

class UpdateOriginAccessControlRequestTypeDef(TypedDict):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef
    Id: str
    IfMatch: NotRequired[str]

class CreatePublicKeyRequestTypeDef(TypedDict):
    PublicKeyConfig: PublicKeyConfigTypeDef

class GetPublicKeyConfigResultTypeDef(TypedDict):
    PublicKeyConfig: PublicKeyConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublicKeyTypeDef(TypedDict):
    Id: str
    CreatedTime: datetime
    PublicKeyConfig: PublicKeyConfigTypeDef

class UpdatePublicKeyRequestTypeDef(TypedDict):
    PublicKeyConfig: PublicKeyConfigTypeDef
    Id: str
    IfMatch: NotRequired[str]

class CustomErrorResponsesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[CustomErrorResponseTypeDef]]

class CustomErrorResponsesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[CustomErrorResponseTypeDef]]

class CustomHeadersOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[OriginCustomHeaderTypeDef]]

class CustomHeadersTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[OriginCustomHeaderTypeDef]]

class CustomOriginConfigOutputTypeDef(TypedDict):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: NotRequired[OriginSslProtocolsOutputTypeDef]
    OriginReadTimeout: NotRequired[int]
    OriginKeepaliveTimeout: NotRequired[int]

class VpcOriginEndpointConfigOutputTypeDef(TypedDict):
    Name: str
    Arn: str
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: NotRequired[OriginSslProtocolsOutputTypeDef]

class CustomizationsOutputTypeDef(TypedDict):
    WebAcl: NotRequired[WebAclCustomizationTypeDef]
    Certificate: NotRequired[CertificateTypeDef]
    GeoRestrictions: NotRequired[GeoRestrictionCustomizationOutputTypeDef]

class CustomizationsTypeDef(TypedDict):
    WebAcl: NotRequired[WebAclCustomizationTypeDef]
    Certificate: NotRequired[CertificateTypeDef]
    GeoRestrictions: NotRequired[GeoRestrictionCustomizationTypeDef]

class ListDistributionsByCachePolicyIdResultTypeDef(TypedDict):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByKeyGroupResultTypeDef(TypedDict):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByOriginRequestPolicyIdResultTypeDef(TypedDict):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByResponseHeadersPolicyIdResultTypeDef(TypedDict):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByVpcOriginIdResultTypeDef(TypedDict):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainConflictsRequestTypeDef(TypedDict):
    Domain: str
    DomainControlValidationResource: DistributionResourceIdTypeDef
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]

class UpdateDomainAssociationRequestTypeDef(TypedDict):
    Domain: str
    TargetResource: DistributionResourceIdTypeDef
    IfMatch: NotRequired[str]

class ListDistributionTenantsRequestTypeDef(TypedDict):
    AssociationFilter: NotRequired[DistributionTenantAssociationFilterTypeDef]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class VerifyDnsConfigurationResultTypeDef(TypedDict):
    DnsConfigurationList: List[DnsConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainConflictsResultTypeDef(TypedDict):
    DomainConflicts: List[DomainConflictTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptionEntityOutputTypeDef(TypedDict):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatternsOutputTypeDef

class EncryptionEntityTypeDef(TypedDict):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatternsTypeDef

class EndPointTypeDef(TypedDict):
    StreamType: str
    KinesisStreamConfig: NotRequired[KinesisStreamConfigTypeDef]

class FunctionAssociationsOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[FunctionAssociationTypeDef]]

class FunctionAssociationsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[FunctionAssociationTypeDef]]

class RestrictionsOutputTypeDef(TypedDict):
    GeoRestriction: GeoRestrictionOutputTypeDef

GeoRestrictionUnionTypeDef = Union[GeoRestrictionTypeDef, GeoRestrictionOutputTypeDef]

class GetDistributionRequestWaitTypeDef(TypedDict):
    Id: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetInvalidationForDistributionTenantRequestWaitTypeDef(TypedDict):
    DistributionTenantId: str
    Id: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetInvalidationRequestWaitTypeDef(TypedDict):
    DistributionId: str
    Id: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetStreamingDistributionRequestWaitTypeDef(TypedDict):
    Id: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetKeyGroupConfigResultTypeDef(TypedDict):
    KeyGroupConfig: KeyGroupConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class KeyGroupTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    KeyGroupConfig: KeyGroupConfigOutputTypeDef

class InvalidationBatchOutputTypeDef(TypedDict):
    Paths: PathsOutputTypeDef
    CallerReference: str

class InvalidationBatchTypeDef(TypedDict):
    Paths: PathsTypeDef
    CallerReference: str

class InvalidationListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[InvalidationSummaryTypeDef]]

class KGKeyPairIdsTypeDef(TypedDict):
    KeyGroupId: NotRequired[str]
    KeyPairIds: NotRequired[KeyPairIdsTypeDef]

class SignerTypeDef(TypedDict):
    AwsAccountNumber: NotRequired[str]
    KeyPairIds: NotRequired[KeyPairIdsTypeDef]

KeyGroupConfigUnionTypeDef = Union[KeyGroupConfigTypeDef, KeyGroupConfigOutputTypeDef]

class KeyValueStoreAssociationsOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[KeyValueStoreAssociationTypeDef]]

class KeyValueStoreAssociationsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[KeyValueStoreAssociationTypeDef]]

class LambdaFunctionAssociationsOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[LambdaFunctionAssociationTypeDef]]

class LambdaFunctionAssociationsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[LambdaFunctionAssociationTypeDef]]

class ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectionGroupsRequestPaginateTypeDef(TypedDict):
    AssociationFilter: NotRequired[ConnectionGroupAssociationFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDistributionTenantsByCustomizationRequestPaginateTypeDef(TypedDict):
    WebACLArn: NotRequired[str]
    CertificateArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDistributionTenantsRequestPaginateTypeDef(TypedDict):
    AssociationFilter: NotRequired[DistributionTenantAssociationFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDistributionsByConnectionModeRequestPaginateTypeDef(TypedDict):
    ConnectionMode: ConnectionModeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDistributionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainConflictsRequestPaginateTypeDef(TypedDict):
    Domain: str
    DomainControlValidationResource: DistributionResourceIdTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInvalidationsForDistributionTenantRequestPaginateTypeDef(TypedDict):
    Id: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInvalidationsRequestPaginateTypeDef(TypedDict):
    DistributionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKeyValueStoresRequestPaginateTypeDef(TypedDict):
    Status: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPublicKeysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamingDistributionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ManagedCertificateDetailsTypeDef(TypedDict):
    CertificateArn: NotRequired[str]
    CertificateStatus: NotRequired[ManagedCertificateStatusType]
    ValidationTokenHost: NotRequired[ValidationTokenHostType]
    ValidationTokenDetails: NotRequired[List[ValidationTokenDetailTypeDef]]

class MonitoringSubscriptionTypeDef(TypedDict):
    RealtimeMetricsSubscriptionConfig: NotRequired[RealtimeMetricsSubscriptionConfigTypeDef]

class OriginAccessControlListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[OriginAccessControlSummaryTypeDef]]

class OriginGroupFailoverCriteriaOutputTypeDef(TypedDict):
    StatusCodes: StatusCodesOutputTypeDef

class OriginGroupMembersOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[OriginGroupMemberTypeDef]

class OriginGroupMembersTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[OriginGroupMemberTypeDef]

OriginSslProtocolsUnionTypeDef = Union[OriginSslProtocolsTypeDef, OriginSslProtocolsOutputTypeDef]

class VpcOriginEndpointConfigTypeDef(TypedDict):
    Name: str
    Arn: str
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: NotRequired[OriginSslProtocolsTypeDef]

class ParameterDefinitionSchemaTypeDef(TypedDict):
    StringSchema: NotRequired[StringSchemaConfigTypeDef]

class PublicKeyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[PublicKeySummaryTypeDef]]

class QueryArgProfilesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[QueryArgProfileTypeDef]]

class QueryArgProfilesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[QueryArgProfileTypeDef]]

QueryStringCacheKeysUnionTypeDef = Union[
    QueryStringCacheKeysTypeDef, QueryStringCacheKeysOutputTypeDef
]

class ResponseHeadersPolicyCorsConfigOutputTypeDef(TypedDict):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: NotRequired[
        ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef
    ]
    AccessControlMaxAgeSec: NotRequired[int]

class ResponseHeadersPolicyCorsConfigTypeDef(TypedDict):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOriginsTypeDef
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeadersTypeDef
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethodsTypeDef
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: NotRequired[ResponseHeadersPolicyAccessControlExposeHeadersTypeDef]
    AccessControlMaxAgeSec: NotRequired[int]

class ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[ResponseHeadersPolicyCustomHeaderTypeDef]]

class ResponseHeadersPolicyCustomHeadersConfigTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[ResponseHeadersPolicyCustomHeaderTypeDef]]

class ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[ResponseHeadersPolicyRemoveHeaderTypeDef]]

class ResponseHeadersPolicyRemoveHeadersConfigTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[ResponseHeadersPolicyRemoveHeaderTypeDef]]

class ResponseHeadersPolicySecurityHeadersConfigTypeDef(TypedDict):
    XSSProtection: NotRequired[ResponseHeadersPolicyXSSProtectionTypeDef]
    FrameOptions: NotRequired[ResponseHeadersPolicyFrameOptionsTypeDef]
    ReferrerPolicy: NotRequired[ResponseHeadersPolicyReferrerPolicyTypeDef]
    ContentSecurityPolicy: NotRequired[ResponseHeadersPolicyContentSecurityPolicyTypeDef]
    ContentTypeOptions: NotRequired[ResponseHeadersPolicyContentTypeOptionsTypeDef]
    StrictTransportSecurity: NotRequired[ResponseHeadersPolicyStrictTransportSecurityTypeDef]

class StreamingDistributionSummaryTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    S3Origin: S3OriginTypeDef
    Aliases: AliasesOutputTypeDef
    TrustedSigners: TrustedSignersOutputTypeDef
    Comment: str
    PriceClass: PriceClassType
    Enabled: bool

StatusCodesUnionTypeDef = Union[StatusCodesTypeDef, StatusCodesOutputTypeDef]

class StreamingDistributionConfigOutputTypeDef(TypedDict):
    CallerReference: str
    S3Origin: S3OriginTypeDef
    Comment: str
    TrustedSigners: TrustedSignersOutputTypeDef
    Enabled: bool
    Aliases: NotRequired[AliasesOutputTypeDef]
    Logging: NotRequired[StreamingLoggingConfigTypeDef]
    PriceClass: NotRequired[PriceClassType]

class UntagResourceRequestTypeDef(TypedDict):
    Resource: str
    TagKeys: TagKeysTypeDef

class TagsOutputTypeDef(TypedDict):
    Items: NotRequired[List[TagTypeDef]]

class TagsTypeDef(TypedDict):
    Items: NotRequired[Sequence[TagTypeDef]]

TrustedKeyGroupsUnionTypeDef = Union[TrustedKeyGroupsTypeDef, TrustedKeyGroupsOutputTypeDef]
TrustedSignersUnionTypeDef = Union[TrustedSignersTypeDef, TrustedSignersOutputTypeDef]

class VpcOriginListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[VpcOriginSummaryTypeDef]]

class ListAnycastIpListsResultTypeDef(TypedDict):
    AnycastIpLists: AnycastIpListCollectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ForwardedValuesOutputTypeDef(TypedDict):
    QueryString: bool
    Cookies: CookiePreferenceOutputTypeDef
    Headers: NotRequired[HeadersOutputTypeDef]
    QueryStringCacheKeys: NotRequired[QueryStringCacheKeysOutputTypeDef]

class CookiePreferenceTypeDef(TypedDict):
    Forward: ItemSelectionType
    WhitelistedNames: NotRequired[CookieNamesUnionTypeDef]

class ParametersInCacheKeyAndForwardedToOriginOutputTypeDef(TypedDict):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfigOutputTypeDef
    CookiesConfig: CachePolicyCookiesConfigOutputTypeDef
    QueryStringsConfig: CachePolicyQueryStringsConfigOutputTypeDef
    EnableAcceptEncodingBrotli: NotRequired[bool]

class OriginRequestPolicyConfigOutputTypeDef(TypedDict):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfigOutputTypeDef
    CookiesConfig: OriginRequestPolicyCookiesConfigOutputTypeDef
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfigOutputTypeDef
    Comment: NotRequired[str]

class ParametersInCacheKeyAndForwardedToOriginTypeDef(TypedDict):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfigTypeDef
    CookiesConfig: CachePolicyCookiesConfigTypeDef
    QueryStringsConfig: CachePolicyQueryStringsConfigTypeDef
    EnableAcceptEncodingBrotli: NotRequired[bool]

class OriginRequestPolicyConfigTypeDef(TypedDict):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfigTypeDef
    CookiesConfig: OriginRequestPolicyCookiesConfigTypeDef
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfigTypeDef
    Comment: NotRequired[str]

class AllowedMethodsTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[MethodType]
    CachedMethods: NotRequired[CachedMethodsUnionTypeDef]

class CreateCloudFrontOriginAccessIdentityResultTypeDef(TypedDict):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCloudFrontOriginAccessIdentityResultTypeDef(TypedDict):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCloudFrontOriginAccessIdentityResultTypeDef(TypedDict):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCloudFrontOriginAccessIdentitiesResultTypeDef(TypedDict):
    CloudFrontOriginAccessIdentityList: CloudFrontOriginAccessIdentityListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConflictingAliasesResultTypeDef(TypedDict):
    ConflictingAliasesList: ConflictingAliasesListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContentTypeProfileConfigOutputTypeDef(TypedDict):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: NotRequired[ContentTypeProfilesOutputTypeDef]

class ContentTypeProfileConfigTypeDef(TypedDict):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: NotRequired[ContentTypeProfilesTypeDef]

TrafficConfigTypeDef = TypedDict(
    "TrafficConfigTypeDef",
    {
        "Type": ContinuousDeploymentPolicyTypeType,
        "SingleWeightConfig": NotRequired[ContinuousDeploymentSingleWeightConfigTypeDef],
        "SingleHeaderConfig": NotRequired[ContinuousDeploymentSingleHeaderConfigTypeDef],
    },
)

class ListKeyValueStoresResultTypeDef(TypedDict):
    KeyValueStoreList: KeyValueStoreListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOriginAccessControlResultTypeDef(TypedDict):
    OriginAccessControl: OriginAccessControlTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginAccessControlResultTypeDef(TypedDict):
    OriginAccessControl: OriginAccessControlTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOriginAccessControlResultTypeDef(TypedDict):
    OriginAccessControl: OriginAccessControlTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublicKeyResultTypeDef(TypedDict):
    PublicKey: PublicKeyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyResultTypeDef(TypedDict):
    PublicKey: PublicKeyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublicKeyResultTypeDef(TypedDict):
    PublicKey: PublicKeyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

CustomErrorResponsesUnionTypeDef = Union[
    CustomErrorResponsesTypeDef, CustomErrorResponsesOutputTypeDef
]
CustomHeadersUnionTypeDef = Union[CustomHeadersTypeDef, CustomHeadersOutputTypeDef]

class OriginOutputTypeDef(TypedDict):
    Id: str
    DomainName: str
    OriginPath: NotRequired[str]
    CustomHeaders: NotRequired[CustomHeadersOutputTypeDef]
    S3OriginConfig: NotRequired[S3OriginConfigTypeDef]
    CustomOriginConfig: NotRequired[CustomOriginConfigOutputTypeDef]
    VpcOriginConfig: NotRequired[VpcOriginConfigTypeDef]
    ConnectionAttempts: NotRequired[int]
    ConnectionTimeout: NotRequired[int]
    OriginShield: NotRequired[OriginShieldTypeDef]
    OriginAccessControlId: NotRequired[str]

class VpcOriginTypeDef(TypedDict):
    Id: str
    Arn: str
    Status: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    VpcOriginEndpointConfig: VpcOriginEndpointConfigOutputTypeDef

class DistributionTenantSummaryTypeDef(TypedDict):
    Id: str
    DistributionId: str
    Name: str
    Arn: str
    Domains: List[DomainResultTypeDef]
    CreatedTime: datetime
    LastModifiedTime: datetime
    ETag: str
    ConnectionGroupId: NotRequired[str]
    Customizations: NotRequired[CustomizationsOutputTypeDef]
    Enabled: NotRequired[bool]
    Status: NotRequired[str]

CustomizationsUnionTypeDef = Union[CustomizationsTypeDef, CustomizationsOutputTypeDef]

class EncryptionEntitiesOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[EncryptionEntityOutputTypeDef]]

class EncryptionEntitiesTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[EncryptionEntityTypeDef]]

class CreateRealtimeLogConfigRequestTypeDef(TypedDict):
    EndPoints: Sequence[EndPointTypeDef]
    Fields: Sequence[str]
    Name: str
    SamplingRate: int

class RealtimeLogConfigTypeDef(TypedDict):
    ARN: str
    Name: str
    SamplingRate: int
    EndPoints: List[EndPointTypeDef]
    Fields: List[str]

class UpdateRealtimeLogConfigRequestTypeDef(TypedDict):
    EndPoints: NotRequired[Sequence[EndPointTypeDef]]
    Fields: NotRequired[Sequence[str]]
    Name: NotRequired[str]
    ARN: NotRequired[str]
    SamplingRate: NotRequired[int]

FunctionAssociationsUnionTypeDef = Union[
    FunctionAssociationsTypeDef, FunctionAssociationsOutputTypeDef
]

class RestrictionsTypeDef(TypedDict):
    GeoRestriction: GeoRestrictionUnionTypeDef

class CreateKeyGroupResultTypeDef(TypedDict):
    KeyGroup: KeyGroupTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyGroupResultTypeDef(TypedDict):
    KeyGroup: KeyGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class KeyGroupSummaryTypeDef(TypedDict):
    KeyGroup: KeyGroupTypeDef

class UpdateKeyGroupResultTypeDef(TypedDict):
    KeyGroup: KeyGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvalidationTypeDef(TypedDict):
    Id: str
    Status: str
    CreateTime: datetime
    InvalidationBatch: InvalidationBatchOutputTypeDef

InvalidationBatchUnionTypeDef = Union[InvalidationBatchTypeDef, InvalidationBatchOutputTypeDef]

class ListInvalidationsForDistributionTenantResultTypeDef(TypedDict):
    InvalidationList: InvalidationListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvalidationsResultTypeDef(TypedDict):
    InvalidationList: InvalidationListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActiveTrustedKeyGroupsTypeDef(TypedDict):
    Enabled: bool
    Quantity: int
    Items: NotRequired[List[KGKeyPairIdsTypeDef]]

class ActiveTrustedSignersTypeDef(TypedDict):
    Enabled: bool
    Quantity: int
    Items: NotRequired[List[SignerTypeDef]]

class CreateKeyGroupRequestTypeDef(TypedDict):
    KeyGroupConfig: KeyGroupConfigUnionTypeDef

class UpdateKeyGroupRequestTypeDef(TypedDict):
    KeyGroupConfig: KeyGroupConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class FunctionConfigOutputTypeDef(TypedDict):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: NotRequired[KeyValueStoreAssociationsOutputTypeDef]

class FunctionConfigTypeDef(TypedDict):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: NotRequired[KeyValueStoreAssociationsTypeDef]

LambdaFunctionAssociationsUnionTypeDef = Union[
    LambdaFunctionAssociationsTypeDef, LambdaFunctionAssociationsOutputTypeDef
]

class GetManagedCertificateDetailsResultTypeDef(TypedDict):
    ManagedCertificateDetails: ManagedCertificateDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitoringSubscriptionRequestTypeDef(TypedDict):
    DistributionId: str
    MonitoringSubscription: MonitoringSubscriptionTypeDef

class CreateMonitoringSubscriptionResultTypeDef(TypedDict):
    MonitoringSubscription: MonitoringSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMonitoringSubscriptionResultTypeDef(TypedDict):
    MonitoringSubscription: MonitoringSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOriginAccessControlsResultTypeDef(TypedDict):
    OriginAccessControlList: OriginAccessControlListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OriginGroupOutputTypeDef(TypedDict):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaOutputTypeDef
    Members: OriginGroupMembersOutputTypeDef
    SelectionCriteria: NotRequired[OriginGroupSelectionCriteriaType]

OriginGroupMembersUnionTypeDef = Union[OriginGroupMembersTypeDef, OriginGroupMembersOutputTypeDef]

class CustomOriginConfigTypeDef(TypedDict):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: NotRequired[OriginSslProtocolsUnionTypeDef]
    OriginReadTimeout: NotRequired[int]
    OriginKeepaliveTimeout: NotRequired[int]

VpcOriginEndpointConfigUnionTypeDef = Union[
    VpcOriginEndpointConfigTypeDef, VpcOriginEndpointConfigOutputTypeDef
]

class ParameterDefinitionTypeDef(TypedDict):
    Name: str
    Definition: ParameterDefinitionSchemaTypeDef

class ListPublicKeysResultTypeDef(TypedDict):
    PublicKeyList: PublicKeyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryArgProfileConfigOutputTypeDef(TypedDict):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: NotRequired[QueryArgProfilesOutputTypeDef]

class QueryArgProfileConfigTypeDef(TypedDict):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: NotRequired[QueryArgProfilesTypeDef]

class ResponseHeadersPolicyConfigOutputTypeDef(TypedDict):
    Name: str
    Comment: NotRequired[str]
    CorsConfig: NotRequired[ResponseHeadersPolicyCorsConfigOutputTypeDef]
    SecurityHeadersConfig: NotRequired[ResponseHeadersPolicySecurityHeadersConfigTypeDef]
    ServerTimingHeadersConfig: NotRequired[ResponseHeadersPolicyServerTimingHeadersConfigTypeDef]
    CustomHeadersConfig: NotRequired[ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef]
    RemoveHeadersConfig: NotRequired[ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef]

class ResponseHeadersPolicyConfigTypeDef(TypedDict):
    Name: str
    Comment: NotRequired[str]
    CorsConfig: NotRequired[ResponseHeadersPolicyCorsConfigTypeDef]
    SecurityHeadersConfig: NotRequired[ResponseHeadersPolicySecurityHeadersConfigTypeDef]
    ServerTimingHeadersConfig: NotRequired[ResponseHeadersPolicyServerTimingHeadersConfigTypeDef]
    CustomHeadersConfig: NotRequired[ResponseHeadersPolicyCustomHeadersConfigTypeDef]
    RemoveHeadersConfig: NotRequired[ResponseHeadersPolicyRemoveHeadersConfigTypeDef]

class StreamingDistributionListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[StreamingDistributionSummaryTypeDef]]

class OriginGroupFailoverCriteriaTypeDef(TypedDict):
    StatusCodes: StatusCodesUnionTypeDef

class GetStreamingDistributionConfigResultTypeDef(TypedDict):
    StreamingDistributionConfig: StreamingDistributionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionGroupTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    Tags: NotRequired[TagsOutputTypeDef]
    Ipv6Enabled: NotRequired[bool]
    RoutingEndpoint: NotRequired[str]
    AnycastIpListId: NotRequired[str]
    Status: NotRequired[str]
    Enabled: NotRequired[bool]
    IsDefault: NotRequired[bool]

class DistributionTenantTypeDef(TypedDict):
    Id: NotRequired[str]
    DistributionId: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Domains: NotRequired[List[DomainResultTypeDef]]
    Tags: NotRequired[TagsOutputTypeDef]
    Customizations: NotRequired[CustomizationsOutputTypeDef]
    Parameters: NotRequired[List[ParameterTypeDef]]
    ConnectionGroupId: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    Enabled: NotRequired[bool]
    Status: NotRequired[str]

class ListTagsForResourceResultTypeDef(TypedDict):
    Tags: TagsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TagsUnionTypeDef = Union[TagsTypeDef, TagsOutputTypeDef]

class StreamingDistributionConfigTypeDef(TypedDict):
    CallerReference: str
    S3Origin: S3OriginTypeDef
    Comment: str
    TrustedSigners: TrustedSignersUnionTypeDef
    Enabled: bool
    Aliases: NotRequired[AliasesUnionTypeDef]
    Logging: NotRequired[StreamingLoggingConfigTypeDef]
    PriceClass: NotRequired[PriceClassType]

class ListVpcOriginsResultTypeDef(TypedDict):
    VpcOriginList: VpcOriginListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheBehaviorOutputTypeDef(TypedDict):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: NotRequired[TrustedSignersOutputTypeDef]
    TrustedKeyGroups: NotRequired[TrustedKeyGroupsOutputTypeDef]
    AllowedMethods: NotRequired[AllowedMethodsOutputTypeDef]
    SmoothStreaming: NotRequired[bool]
    Compress: NotRequired[bool]
    LambdaFunctionAssociations: NotRequired[LambdaFunctionAssociationsOutputTypeDef]
    FunctionAssociations: NotRequired[FunctionAssociationsOutputTypeDef]
    FieldLevelEncryptionId: NotRequired[str]
    RealtimeLogConfigArn: NotRequired[str]
    CachePolicyId: NotRequired[str]
    OriginRequestPolicyId: NotRequired[str]
    ResponseHeadersPolicyId: NotRequired[str]
    GrpcConfig: NotRequired[GrpcConfigTypeDef]
    ForwardedValues: NotRequired[ForwardedValuesOutputTypeDef]
    MinTTL: NotRequired[int]
    DefaultTTL: NotRequired[int]
    MaxTTL: NotRequired[int]

class DefaultCacheBehaviorOutputTypeDef(TypedDict):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: NotRequired[TrustedSignersOutputTypeDef]
    TrustedKeyGroups: NotRequired[TrustedKeyGroupsOutputTypeDef]
    AllowedMethods: NotRequired[AllowedMethodsOutputTypeDef]
    SmoothStreaming: NotRequired[bool]
    Compress: NotRequired[bool]
    LambdaFunctionAssociations: NotRequired[LambdaFunctionAssociationsOutputTypeDef]
    FunctionAssociations: NotRequired[FunctionAssociationsOutputTypeDef]
    FieldLevelEncryptionId: NotRequired[str]
    RealtimeLogConfigArn: NotRequired[str]
    CachePolicyId: NotRequired[str]
    OriginRequestPolicyId: NotRequired[str]
    ResponseHeadersPolicyId: NotRequired[str]
    GrpcConfig: NotRequired[GrpcConfigTypeDef]
    ForwardedValues: NotRequired[ForwardedValuesOutputTypeDef]
    MinTTL: NotRequired[int]
    DefaultTTL: NotRequired[int]
    MaxTTL: NotRequired[int]

CookiePreferenceUnionTypeDef = Union[CookiePreferenceTypeDef, CookiePreferenceOutputTypeDef]

class CachePolicyConfigOutputTypeDef(TypedDict):
    Name: str
    MinTTL: int
    Comment: NotRequired[str]
    DefaultTTL: NotRequired[int]
    MaxTTL: NotRequired[int]
    ParametersInCacheKeyAndForwardedToOrigin: NotRequired[
        ParametersInCacheKeyAndForwardedToOriginOutputTypeDef
    ]

class GetOriginRequestPolicyConfigResultTypeDef(TypedDict):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginRequestPolicyTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutputTypeDef

class CachePolicyConfigTypeDef(TypedDict):
    Name: str
    MinTTL: int
    Comment: NotRequired[str]
    DefaultTTL: NotRequired[int]
    MaxTTL: NotRequired[int]
    ParametersInCacheKeyAndForwardedToOrigin: NotRequired[
        ParametersInCacheKeyAndForwardedToOriginTypeDef
    ]

OriginRequestPolicyConfigUnionTypeDef = Union[
    OriginRequestPolicyConfigTypeDef, OriginRequestPolicyConfigOutputTypeDef
]
AllowedMethodsUnionTypeDef = Union[AllowedMethodsTypeDef, AllowedMethodsOutputTypeDef]

class ContinuousDeploymentPolicyConfigOutputTypeDef(TypedDict):
    StagingDistributionDnsNames: StagingDistributionDnsNamesOutputTypeDef
    Enabled: bool
    TrafficConfig: NotRequired[TrafficConfigTypeDef]

class ContinuousDeploymentPolicyConfigTypeDef(TypedDict):
    StagingDistributionDnsNames: StagingDistributionDnsNamesTypeDef
    Enabled: bool
    TrafficConfig: NotRequired[TrafficConfigTypeDef]

class OriginsOutputTypeDef(TypedDict):
    Quantity: int
    Items: List[OriginOutputTypeDef]

class CreateVpcOriginResultTypeDef(TypedDict):
    VpcOrigin: VpcOriginTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcOriginResultTypeDef(TypedDict):
    VpcOrigin: VpcOriginTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcOriginResultTypeDef(TypedDict):
    VpcOrigin: VpcOriginTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcOriginResultTypeDef(TypedDict):
    VpcOrigin: VpcOriginTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionTenantsByCustomizationResultTypeDef(TypedDict):
    NextMarker: str
    DistributionTenantList: List[DistributionTenantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionTenantsResultTypeDef(TypedDict):
    NextMarker: str
    DistributionTenantList: List[DistributionTenantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionTenantRequestTypeDef(TypedDict):
    Id: str
    IfMatch: str
    DistributionId: NotRequired[str]
    Domains: NotRequired[Sequence[DomainItemTypeDef]]
    Customizations: NotRequired[CustomizationsUnionTypeDef]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    ConnectionGroupId: NotRequired[str]
    ManagedCertificateRequest: NotRequired[ManagedCertificateRequestTypeDef]
    Enabled: NotRequired[bool]

class FieldLevelEncryptionProfileConfigOutputTypeDef(TypedDict):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntitiesOutputTypeDef
    Comment: NotRequired[str]

class FieldLevelEncryptionProfileSummaryTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    Name: str
    EncryptionEntities: EncryptionEntitiesOutputTypeDef
    Comment: NotRequired[str]

class FieldLevelEncryptionProfileConfigTypeDef(TypedDict):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntitiesTypeDef
    Comment: NotRequired[str]

class CreateRealtimeLogConfigResultTypeDef(TypedDict):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRealtimeLogConfigResultTypeDef(TypedDict):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RealtimeLogConfigsTypeDef(TypedDict):
    MaxItems: int
    IsTruncated: bool
    Marker: str
    Items: NotRequired[List[RealtimeLogConfigTypeDef]]
    NextMarker: NotRequired[str]

class UpdateRealtimeLogConfigResultTypeDef(TypedDict):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

RestrictionsUnionTypeDef = Union[RestrictionsTypeDef, RestrictionsOutputTypeDef]

class KeyGroupListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[KeyGroupSummaryTypeDef]]

class CreateInvalidationForDistributionTenantResultTypeDef(TypedDict):
    Location: str
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInvalidationResultTypeDef(TypedDict):
    Location: str
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvalidationForDistributionTenantResultTypeDef(TypedDict):
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvalidationResultTypeDef(TypedDict):
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInvalidationForDistributionTenantRequestTypeDef(TypedDict):
    Id: str
    InvalidationBatch: InvalidationBatchUnionTypeDef

class CreateInvalidationRequestTypeDef(TypedDict):
    DistributionId: str
    InvalidationBatch: InvalidationBatchUnionTypeDef

class StreamingDistributionTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    DomainName: str
    ActiveTrustedSigners: ActiveTrustedSignersTypeDef
    StreamingDistributionConfig: StreamingDistributionConfigOutputTypeDef
    LastModifiedTime: NotRequired[datetime]

class FunctionSummaryTypeDef(TypedDict):
    Name: str
    FunctionConfig: FunctionConfigOutputTypeDef
    FunctionMetadata: FunctionMetadataTypeDef
    Status: NotRequired[str]

FunctionConfigUnionTypeDef = Union[FunctionConfigTypeDef, FunctionConfigOutputTypeDef]

class OriginGroupsOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[OriginGroupOutputTypeDef]]

CustomOriginConfigUnionTypeDef = Union[CustomOriginConfigTypeDef, CustomOriginConfigOutputTypeDef]

class UpdateVpcOriginRequestTypeDef(TypedDict):
    VpcOriginEndpointConfig: VpcOriginEndpointConfigUnionTypeDef
    Id: str
    IfMatch: str

class TenantConfigOutputTypeDef(TypedDict):
    ParameterDefinitions: NotRequired[List[ParameterDefinitionTypeDef]]

class TenantConfigTypeDef(TypedDict):
    ParameterDefinitions: NotRequired[Sequence[ParameterDefinitionTypeDef]]

class FieldLevelEncryptionConfigOutputTypeDef(TypedDict):
    CallerReference: str
    Comment: NotRequired[str]
    QueryArgProfileConfig: NotRequired[QueryArgProfileConfigOutputTypeDef]
    ContentTypeProfileConfig: NotRequired[ContentTypeProfileConfigOutputTypeDef]

class FieldLevelEncryptionSummaryTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    Comment: NotRequired[str]
    QueryArgProfileConfig: NotRequired[QueryArgProfileConfigOutputTypeDef]
    ContentTypeProfileConfig: NotRequired[ContentTypeProfileConfigOutputTypeDef]

class FieldLevelEncryptionConfigTypeDef(TypedDict):
    CallerReference: str
    Comment: NotRequired[str]
    QueryArgProfileConfig: NotRequired[QueryArgProfileConfigTypeDef]
    ContentTypeProfileConfig: NotRequired[ContentTypeProfileConfigTypeDef]

class GetResponseHeadersPolicyConfigResultTypeDef(TypedDict):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseHeadersPolicyTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutputTypeDef

ResponseHeadersPolicyConfigUnionTypeDef = Union[
    ResponseHeadersPolicyConfigTypeDef, ResponseHeadersPolicyConfigOutputTypeDef
]

class ListStreamingDistributionsResultTypeDef(TypedDict):
    StreamingDistributionList: StreamingDistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

OriginGroupFailoverCriteriaUnionTypeDef = Union[
    OriginGroupFailoverCriteriaTypeDef, OriginGroupFailoverCriteriaOutputTypeDef
]

class CreateConnectionGroupResultTypeDef(TypedDict):
    ConnectionGroup: ConnectionGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionGroupByRoutingEndpointResultTypeDef(TypedDict):
    ConnectionGroup: ConnectionGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionGroupResultTypeDef(TypedDict):
    ConnectionGroup: ConnectionGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectionGroupResultTypeDef(TypedDict):
    ConnectionGroup: ConnectionGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionTenantResultTypeDef(TypedDict):
    DistributionTenant: DistributionTenantTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionTenantByDomainResultTypeDef(TypedDict):
    DistributionTenant: DistributionTenantTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionTenantResultTypeDef(TypedDict):
    DistributionTenant: DistributionTenantTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionTenantResultTypeDef(TypedDict):
    DistributionTenant: DistributionTenantTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnycastIpListRequestTypeDef(TypedDict):
    Name: str
    IpCount: int
    Tags: NotRequired[TagsUnionTypeDef]

class CreateConnectionGroupRequestTypeDef(TypedDict):
    Name: str
    Ipv6Enabled: NotRequired[bool]
    Tags: NotRequired[TagsUnionTypeDef]
    AnycastIpListId: NotRequired[str]
    Enabled: NotRequired[bool]

class CreateDistributionTenantRequestTypeDef(TypedDict):
    DistributionId: str
    Name: str
    Domains: Sequence[DomainItemTypeDef]
    Tags: NotRequired[TagsUnionTypeDef]
    Customizations: NotRequired[CustomizationsUnionTypeDef]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    ConnectionGroupId: NotRequired[str]
    ManagedCertificateRequest: NotRequired[ManagedCertificateRequestTypeDef]
    Enabled: NotRequired[bool]

class CreateVpcOriginRequestTypeDef(TypedDict):
    VpcOriginEndpointConfig: VpcOriginEndpointConfigUnionTypeDef
    Tags: NotRequired[TagsUnionTypeDef]

class TagResourceRequestTypeDef(TypedDict):
    Resource: str
    Tags: TagsUnionTypeDef

StreamingDistributionConfigUnionTypeDef = Union[
    StreamingDistributionConfigTypeDef, StreamingDistributionConfigOutputTypeDef
]

class CacheBehaviorsOutputTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[List[CacheBehaviorOutputTypeDef]]

class ForwardedValuesTypeDef(TypedDict):
    QueryString: bool
    Cookies: CookiePreferenceUnionTypeDef
    Headers: NotRequired[HeadersUnionTypeDef]
    QueryStringCacheKeys: NotRequired[QueryStringCacheKeysUnionTypeDef]

class CachePolicyTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    CachePolicyConfig: CachePolicyConfigOutputTypeDef

class GetCachePolicyConfigResultTypeDef(TypedDict):
    CachePolicyConfig: CachePolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOriginRequestPolicyResultTypeDef(TypedDict):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginRequestPolicyResultTypeDef(TypedDict):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

OriginRequestPolicySummaryTypeDef = TypedDict(
    "OriginRequestPolicySummaryTypeDef",
    {
        "Type": OriginRequestPolicyTypeType,
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
    },
)

class UpdateOriginRequestPolicyResultTypeDef(TypedDict):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

CachePolicyConfigUnionTypeDef = Union[CachePolicyConfigTypeDef, CachePolicyConfigOutputTypeDef]

class CreateOriginRequestPolicyRequestTypeDef(TypedDict):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigUnionTypeDef

class UpdateOriginRequestPolicyRequestTypeDef(TypedDict):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class ContinuousDeploymentPolicyTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutputTypeDef

class GetContinuousDeploymentPolicyConfigResultTypeDef(TypedDict):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

ContinuousDeploymentPolicyConfigUnionTypeDef = Union[
    ContinuousDeploymentPolicyConfigTypeDef, ContinuousDeploymentPolicyConfigOutputTypeDef
]

class FieldLevelEncryptionProfileTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutputTypeDef

class GetFieldLevelEncryptionProfileConfigResultTypeDef(TypedDict):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldLevelEncryptionProfileListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[FieldLevelEncryptionProfileSummaryTypeDef]]

FieldLevelEncryptionProfileConfigUnionTypeDef = Union[
    FieldLevelEncryptionProfileConfigTypeDef, FieldLevelEncryptionProfileConfigOutputTypeDef
]

class ListRealtimeLogConfigsResultTypeDef(TypedDict):
    RealtimeLogConfigs: RealtimeLogConfigsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyGroupsResultTypeDef(TypedDict):
    KeyGroupList: KeyGroupListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingDistributionResultTypeDef(TypedDict):
    StreamingDistribution: StreamingDistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingDistributionWithTagsResultTypeDef(TypedDict):
    StreamingDistribution: StreamingDistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingDistributionResultTypeDef(TypedDict):
    StreamingDistribution: StreamingDistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStreamingDistributionResultTypeDef(TypedDict):
    StreamingDistribution: StreamingDistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionResultTypeDef(TypedDict):
    FunctionSummary: FunctionSummaryTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFunctionResultTypeDef(TypedDict):
    FunctionSummary: FunctionSummaryTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[FunctionSummaryTypeDef]]

class PublishFunctionResultTypeDef(TypedDict):
    FunctionSummary: FunctionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestResultTypeDef(TypedDict):
    FunctionSummary: NotRequired[FunctionSummaryTypeDef]
    ComputeUtilization: NotRequired[str]
    FunctionExecutionLogs: NotRequired[List[str]]
    FunctionErrorMessage: NotRequired[str]
    FunctionOutput: NotRequired[str]

class UpdateFunctionResultTypeDef(TypedDict):
    FunctionSummary: FunctionSummaryTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionRequestTypeDef(TypedDict):
    Name: str
    FunctionConfig: FunctionConfigUnionTypeDef
    FunctionCode: BlobTypeDef

class UpdateFunctionRequestTypeDef(TypedDict):
    Name: str
    IfMatch: str
    FunctionConfig: FunctionConfigUnionTypeDef
    FunctionCode: BlobTypeDef

class OriginTypeDef(TypedDict):
    Id: str
    DomainName: str
    OriginPath: NotRequired[str]
    CustomHeaders: NotRequired[CustomHeadersUnionTypeDef]
    S3OriginConfig: NotRequired[S3OriginConfigTypeDef]
    CustomOriginConfig: NotRequired[CustomOriginConfigUnionTypeDef]
    VpcOriginConfig: NotRequired[VpcOriginConfigTypeDef]
    ConnectionAttempts: NotRequired[int]
    ConnectionTimeout: NotRequired[int]
    OriginShield: NotRequired[OriginShieldTypeDef]
    OriginAccessControlId: NotRequired[str]

TenantConfigUnionTypeDef = Union[TenantConfigTypeDef, TenantConfigOutputTypeDef]

class FieldLevelEncryptionTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutputTypeDef

class GetFieldLevelEncryptionConfigResultTypeDef(TypedDict):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldLevelEncryptionListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[FieldLevelEncryptionSummaryTypeDef]]

FieldLevelEncryptionConfigUnionTypeDef = Union[
    FieldLevelEncryptionConfigTypeDef, FieldLevelEncryptionConfigOutputTypeDef
]

class CreateResponseHeadersPolicyResultTypeDef(TypedDict):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResponseHeadersPolicyResultTypeDef(TypedDict):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

ResponseHeadersPolicySummaryTypeDef = TypedDict(
    "ResponseHeadersPolicySummaryTypeDef",
    {
        "Type": ResponseHeadersPolicyTypeType,
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
    },
)

class UpdateResponseHeadersPolicyResultTypeDef(TypedDict):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResponseHeadersPolicyRequestTypeDef(TypedDict):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigUnionTypeDef

class UpdateResponseHeadersPolicyRequestTypeDef(TypedDict):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class OriginGroupTypeDef(TypedDict):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaUnionTypeDef
    Members: OriginGroupMembersUnionTypeDef
    SelectionCriteria: NotRequired[OriginGroupSelectionCriteriaType]

class CreateStreamingDistributionRequestTypeDef(TypedDict):
    StreamingDistributionConfig: StreamingDistributionConfigUnionTypeDef

class StreamingDistributionConfigWithTagsTypeDef(TypedDict):
    StreamingDistributionConfig: StreamingDistributionConfigUnionTypeDef
    Tags: TagsUnionTypeDef

class UpdateStreamingDistributionRequestTypeDef(TypedDict):
    StreamingDistributionConfig: StreamingDistributionConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class DistributionConfigOutputTypeDef(TypedDict):
    CallerReference: str
    Origins: OriginsOutputTypeDef
    DefaultCacheBehavior: DefaultCacheBehaviorOutputTypeDef
    Comment: str
    Enabled: bool
    Aliases: NotRequired[AliasesOutputTypeDef]
    DefaultRootObject: NotRequired[str]
    OriginGroups: NotRequired[OriginGroupsOutputTypeDef]
    CacheBehaviors: NotRequired[CacheBehaviorsOutputTypeDef]
    CustomErrorResponses: NotRequired[CustomErrorResponsesOutputTypeDef]
    Logging: NotRequired[LoggingConfigTypeDef]
    PriceClass: NotRequired[PriceClassType]
    ViewerCertificate: NotRequired[ViewerCertificateTypeDef]
    Restrictions: NotRequired[RestrictionsOutputTypeDef]
    WebACLId: NotRequired[str]
    HttpVersion: NotRequired[HttpVersionType]
    IsIPV6Enabled: NotRequired[bool]
    ContinuousDeploymentPolicyId: NotRequired[str]
    Staging: NotRequired[bool]
    AnycastIpListId: NotRequired[str]
    TenantConfig: NotRequired[TenantConfigOutputTypeDef]
    ConnectionMode: NotRequired[ConnectionModeType]

class DistributionSummaryTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    Aliases: AliasesOutputTypeDef
    Origins: OriginsOutputTypeDef
    DefaultCacheBehavior: DefaultCacheBehaviorOutputTypeDef
    CacheBehaviors: CacheBehaviorsOutputTypeDef
    CustomErrorResponses: CustomErrorResponsesOutputTypeDef
    Comment: str
    PriceClass: PriceClassType
    Enabled: bool
    ViewerCertificate: ViewerCertificateTypeDef
    Restrictions: RestrictionsOutputTypeDef
    WebACLId: str
    HttpVersion: HttpVersionType
    IsIPV6Enabled: bool
    Staging: bool
    ETag: NotRequired[str]
    OriginGroups: NotRequired[OriginGroupsOutputTypeDef]
    AliasICPRecordals: NotRequired[List[AliasICPRecordalTypeDef]]
    ConnectionMode: NotRequired[ConnectionModeType]
    AnycastIpListId: NotRequired[str]

ForwardedValuesUnionTypeDef = Union[ForwardedValuesTypeDef, ForwardedValuesOutputTypeDef]
CachePolicySummaryTypeDef = TypedDict(
    "CachePolicySummaryTypeDef",
    {
        "Type": CachePolicyTypeType,
        "CachePolicy": CachePolicyTypeDef,
    },
)

class CreateCachePolicyResultTypeDef(TypedDict):
    CachePolicy: CachePolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCachePolicyResultTypeDef(TypedDict):
    CachePolicy: CachePolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCachePolicyResultTypeDef(TypedDict):
    CachePolicy: CachePolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginRequestPolicyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[OriginRequestPolicySummaryTypeDef]]

class CreateCachePolicyRequestTypeDef(TypedDict):
    CachePolicyConfig: CachePolicyConfigUnionTypeDef

class UpdateCachePolicyRequestTypeDef(TypedDict):
    CachePolicyConfig: CachePolicyConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class ContinuousDeploymentPolicySummaryTypeDef(TypedDict):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef

class CreateContinuousDeploymentPolicyResultTypeDef(TypedDict):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContinuousDeploymentPolicyResultTypeDef(TypedDict):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContinuousDeploymentPolicyResultTypeDef(TypedDict):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContinuousDeploymentPolicyRequestTypeDef(TypedDict):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigUnionTypeDef

class UpdateContinuousDeploymentPolicyRequestTypeDef(TypedDict):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class CreateFieldLevelEncryptionProfileResultTypeDef(TypedDict):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFieldLevelEncryptionProfileResultTypeDef(TypedDict):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFieldLevelEncryptionProfileResultTypeDef(TypedDict):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFieldLevelEncryptionProfilesResultTypeDef(TypedDict):
    FieldLevelEncryptionProfileList: FieldLevelEncryptionProfileListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldLevelEncryptionProfileRequestTypeDef(TypedDict):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigUnionTypeDef

class UpdateFieldLevelEncryptionProfileRequestTypeDef(TypedDict):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class ListFunctionsResultTypeDef(TypedDict):
    FunctionList: FunctionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestFunctionResultTypeDef(TypedDict):
    TestResult: TestResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

OriginUnionTypeDef = Union[OriginTypeDef, OriginOutputTypeDef]

class CreateFieldLevelEncryptionConfigResultTypeDef(TypedDict):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFieldLevelEncryptionResultTypeDef(TypedDict):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFieldLevelEncryptionConfigResultTypeDef(TypedDict):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFieldLevelEncryptionConfigsResultTypeDef(TypedDict):
    FieldLevelEncryptionList: FieldLevelEncryptionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldLevelEncryptionConfigRequestTypeDef(TypedDict):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigUnionTypeDef

class UpdateFieldLevelEncryptionConfigRequestTypeDef(TypedDict):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class ResponseHeadersPolicyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[ResponseHeadersPolicySummaryTypeDef]]

OriginGroupUnionTypeDef = Union[OriginGroupTypeDef, OriginGroupOutputTypeDef]

class CreateStreamingDistributionWithTagsRequestTypeDef(TypedDict):
    StreamingDistributionConfigWithTags: StreamingDistributionConfigWithTagsTypeDef

class DistributionTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    InProgressInvalidationBatches: int
    DomainName: str
    DistributionConfig: DistributionConfigOutputTypeDef
    ActiveTrustedSigners: NotRequired[ActiveTrustedSignersTypeDef]
    ActiveTrustedKeyGroups: NotRequired[ActiveTrustedKeyGroupsTypeDef]
    AliasICPRecordals: NotRequired[List[AliasICPRecordalTypeDef]]

class GetDistributionConfigResultTypeDef(TypedDict):
    DistributionConfig: DistributionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DistributionListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[DistributionSummaryTypeDef]]

class CacheBehaviorTypeDef(TypedDict):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: NotRequired[TrustedSignersUnionTypeDef]
    TrustedKeyGroups: NotRequired[TrustedKeyGroupsUnionTypeDef]
    AllowedMethods: NotRequired[AllowedMethodsUnionTypeDef]
    SmoothStreaming: NotRequired[bool]
    Compress: NotRequired[bool]
    LambdaFunctionAssociations: NotRequired[LambdaFunctionAssociationsUnionTypeDef]
    FunctionAssociations: NotRequired[FunctionAssociationsUnionTypeDef]
    FieldLevelEncryptionId: NotRequired[str]
    RealtimeLogConfigArn: NotRequired[str]
    CachePolicyId: NotRequired[str]
    OriginRequestPolicyId: NotRequired[str]
    ResponseHeadersPolicyId: NotRequired[str]
    GrpcConfig: NotRequired[GrpcConfigTypeDef]
    ForwardedValues: NotRequired[ForwardedValuesUnionTypeDef]
    MinTTL: NotRequired[int]
    DefaultTTL: NotRequired[int]
    MaxTTL: NotRequired[int]

class DefaultCacheBehaviorTypeDef(TypedDict):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: NotRequired[TrustedSignersUnionTypeDef]
    TrustedKeyGroups: NotRequired[TrustedKeyGroupsUnionTypeDef]
    AllowedMethods: NotRequired[AllowedMethodsUnionTypeDef]
    SmoothStreaming: NotRequired[bool]
    Compress: NotRequired[bool]
    LambdaFunctionAssociations: NotRequired[LambdaFunctionAssociationsUnionTypeDef]
    FunctionAssociations: NotRequired[FunctionAssociationsUnionTypeDef]
    FieldLevelEncryptionId: NotRequired[str]
    RealtimeLogConfigArn: NotRequired[str]
    CachePolicyId: NotRequired[str]
    OriginRequestPolicyId: NotRequired[str]
    ResponseHeadersPolicyId: NotRequired[str]
    GrpcConfig: NotRequired[GrpcConfigTypeDef]
    ForwardedValues: NotRequired[ForwardedValuesUnionTypeDef]
    MinTTL: NotRequired[int]
    DefaultTTL: NotRequired[int]
    MaxTTL: NotRequired[int]

class CachePolicyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[CachePolicySummaryTypeDef]]

class ListOriginRequestPoliciesResultTypeDef(TypedDict):
    OriginRequestPolicyList: OriginRequestPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContinuousDeploymentPolicyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int
    NextMarker: NotRequired[str]
    Items: NotRequired[List[ContinuousDeploymentPolicySummaryTypeDef]]

class OriginsTypeDef(TypedDict):
    Quantity: int
    Items: Sequence[OriginUnionTypeDef]

class ListResponseHeadersPoliciesResultTypeDef(TypedDict):
    ResponseHeadersPolicyList: ResponseHeadersPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OriginGroupsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[OriginGroupUnionTypeDef]]

class CopyDistributionResultTypeDef(TypedDict):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionResultTypeDef(TypedDict):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionWithTagsResultTypeDef(TypedDict):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionResultTypeDef(TypedDict):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionResultTypeDef(TypedDict):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionWithStagingConfigResultTypeDef(TypedDict):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByAnycastIpListIdResultTypeDef(TypedDict):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByConnectionModeResultTypeDef(TypedDict):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByRealtimeLogConfigResultTypeDef(TypedDict):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByWebACLIdResultTypeDef(TypedDict):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsResultTypeDef(TypedDict):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CacheBehaviorUnionTypeDef = Union[CacheBehaviorTypeDef, CacheBehaviorOutputTypeDef]
DefaultCacheBehaviorUnionTypeDef = Union[
    DefaultCacheBehaviorTypeDef, DefaultCacheBehaviorOutputTypeDef
]

class ListCachePoliciesResultTypeDef(TypedDict):
    CachePolicyList: CachePolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContinuousDeploymentPoliciesResultTypeDef(TypedDict):
    ContinuousDeploymentPolicyList: ContinuousDeploymentPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

OriginsUnionTypeDef = Union[OriginsTypeDef, OriginsOutputTypeDef]
OriginGroupsUnionTypeDef = Union[OriginGroupsTypeDef, OriginGroupsOutputTypeDef]

class CacheBehaviorsTypeDef(TypedDict):
    Quantity: int
    Items: NotRequired[Sequence[CacheBehaviorUnionTypeDef]]

CacheBehaviorsUnionTypeDef = Union[CacheBehaviorsTypeDef, CacheBehaviorsOutputTypeDef]

class DistributionConfigTypeDef(TypedDict):
    CallerReference: str
    Origins: OriginsUnionTypeDef
    DefaultCacheBehavior: DefaultCacheBehaviorUnionTypeDef
    Comment: str
    Enabled: bool
    Aliases: NotRequired[AliasesUnionTypeDef]
    DefaultRootObject: NotRequired[str]
    OriginGroups: NotRequired[OriginGroupsUnionTypeDef]
    CacheBehaviors: NotRequired[CacheBehaviorsUnionTypeDef]
    CustomErrorResponses: NotRequired[CustomErrorResponsesUnionTypeDef]
    Logging: NotRequired[LoggingConfigTypeDef]
    PriceClass: NotRequired[PriceClassType]
    ViewerCertificate: NotRequired[ViewerCertificateTypeDef]
    Restrictions: NotRequired[RestrictionsUnionTypeDef]
    WebACLId: NotRequired[str]
    HttpVersion: NotRequired[HttpVersionType]
    IsIPV6Enabled: NotRequired[bool]
    ContinuousDeploymentPolicyId: NotRequired[str]
    Staging: NotRequired[bool]
    AnycastIpListId: NotRequired[str]
    TenantConfig: NotRequired[TenantConfigUnionTypeDef]
    ConnectionMode: NotRequired[ConnectionModeType]

DistributionConfigUnionTypeDef = Union[DistributionConfigTypeDef, DistributionConfigOutputTypeDef]

class CreateDistributionRequestTypeDef(TypedDict):
    DistributionConfig: DistributionConfigUnionTypeDef

class DistributionConfigWithTagsTypeDef(TypedDict):
    DistributionConfig: DistributionConfigUnionTypeDef
    Tags: TagsUnionTypeDef

class UpdateDistributionRequestTypeDef(TypedDict):
    DistributionConfig: DistributionConfigUnionTypeDef
    Id: str
    IfMatch: NotRequired[str]

class CreateDistributionWithTagsRequestTypeDef(TypedDict):
    DistributionConfigWithTags: DistributionConfigWithTagsTypeDef
