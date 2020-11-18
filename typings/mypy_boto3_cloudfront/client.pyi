# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for cloudfront service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudfront import CloudFrontClient

    client: CloudFrontClient = boto3.client("cloudfront")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_cloudfront.paginator import (
    ListCloudFrontOriginAccessIdentitiesPaginator,
    ListDistributionsPaginator,
    ListInvalidationsPaginator,
    ListStreamingDistributionsPaginator,
)
from mypy_boto3_cloudfront.type_defs import (
    CachePolicyConfigTypeDef,
    CloudFrontOriginAccessIdentityConfigTypeDef,
    CreateCachePolicyResultTypeDef,
    CreateCloudFrontOriginAccessIdentityResultTypeDef,
    CreateDistributionResultTypeDef,
    CreateDistributionWithTagsResultTypeDef,
    CreateFieldLevelEncryptionConfigResultTypeDef,
    CreateFieldLevelEncryptionProfileResultTypeDef,
    CreateInvalidationResultTypeDef,
    CreateKeyGroupResultTypeDef,
    CreateMonitoringSubscriptionResultTypeDef,
    CreateOriginRequestPolicyResultTypeDef,
    CreatePublicKeyResultTypeDef,
    CreateRealtimeLogConfigResultTypeDef,
    CreateStreamingDistributionResultTypeDef,
    CreateStreamingDistributionWithTagsResultTypeDef,
    DistributionConfigTypeDef,
    DistributionConfigWithTagsTypeDef,
    EndPointTypeDef,
    FieldLevelEncryptionConfigTypeDef,
    FieldLevelEncryptionProfileConfigTypeDef,
    GetCachePolicyConfigResultTypeDef,
    GetCachePolicyResultTypeDef,
    GetCloudFrontOriginAccessIdentityConfigResultTypeDef,
    GetCloudFrontOriginAccessIdentityResultTypeDef,
    GetDistributionConfigResultTypeDef,
    GetDistributionResultTypeDef,
    GetFieldLevelEncryptionConfigResultTypeDef,
    GetFieldLevelEncryptionProfileConfigResultTypeDef,
    GetFieldLevelEncryptionProfileResultTypeDef,
    GetFieldLevelEncryptionResultTypeDef,
    GetInvalidationResultTypeDef,
    GetKeyGroupConfigResultTypeDef,
    GetKeyGroupResultTypeDef,
    GetMonitoringSubscriptionResultTypeDef,
    GetOriginRequestPolicyConfigResultTypeDef,
    GetOriginRequestPolicyResultTypeDef,
    GetPublicKeyConfigResultTypeDef,
    GetPublicKeyResultTypeDef,
    GetRealtimeLogConfigResultTypeDef,
    GetStreamingDistributionConfigResultTypeDef,
    GetStreamingDistributionResultTypeDef,
    InvalidationBatchTypeDef,
    KeyGroupConfigTypeDef,
    ListCachePoliciesResultTypeDef,
    ListCloudFrontOriginAccessIdentitiesResultTypeDef,
    ListDistributionsByCachePolicyIdResultTypeDef,
    ListDistributionsByKeyGroupResultTypeDef,
    ListDistributionsByOriginRequestPolicyIdResultTypeDef,
    ListDistributionsByRealtimeLogConfigResultTypeDef,
    ListDistributionsByWebACLIdResultTypeDef,
    ListDistributionsResultTypeDef,
    ListFieldLevelEncryptionConfigsResultTypeDef,
    ListFieldLevelEncryptionProfilesResultTypeDef,
    ListInvalidationsResultTypeDef,
    ListKeyGroupsResultTypeDef,
    ListOriginRequestPoliciesResultTypeDef,
    ListPublicKeysResultTypeDef,
    ListRealtimeLogConfigsResultTypeDef,
    ListStreamingDistributionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    MonitoringSubscriptionTypeDef,
    OriginRequestPolicyConfigTypeDef,
    PublicKeyConfigTypeDef,
    StreamingDistributionConfigTypeDef,
    StreamingDistributionConfigWithTagsTypeDef,
    TagKeysTypeDef,
    TagsTypeDef,
    UpdateCachePolicyResultTypeDef,
    UpdateCloudFrontOriginAccessIdentityResultTypeDef,
    UpdateDistributionResultTypeDef,
    UpdateFieldLevelEncryptionConfigResultTypeDef,
    UpdateFieldLevelEncryptionProfileResultTypeDef,
    UpdateKeyGroupResultTypeDef,
    UpdateOriginRequestPolicyResultTypeDef,
    UpdatePublicKeyResultTypeDef,
    UpdateRealtimeLogConfigResultTypeDef,
    UpdateStreamingDistributionResultTypeDef,
)
from mypy_boto3_cloudfront.waiter import (
    DistributionDeployedWaiter,
    InvalidationCompletedWaiter,
    StreamingDistributionDeployedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudFrontClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDenied: Type[BotocoreClientError]
    BatchTooLarge: Type[BotocoreClientError]
    CNAMEAlreadyExists: Type[BotocoreClientError]
    CachePolicyAlreadyExists: Type[BotocoreClientError]
    CachePolicyInUse: Type[BotocoreClientError]
    CannotChangeImmutablePublicKeyFields: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CloudFrontOriginAccessIdentityAlreadyExists: Type[BotocoreClientError]
    CloudFrontOriginAccessIdentityInUse: Type[BotocoreClientError]
    DistributionAlreadyExists: Type[BotocoreClientError]
    DistributionNotDisabled: Type[BotocoreClientError]
    FieldLevelEncryptionConfigAlreadyExists: Type[BotocoreClientError]
    FieldLevelEncryptionConfigInUse: Type[BotocoreClientError]
    FieldLevelEncryptionProfileAlreadyExists: Type[BotocoreClientError]
    FieldLevelEncryptionProfileInUse: Type[BotocoreClientError]
    FieldLevelEncryptionProfileSizeExceeded: Type[BotocoreClientError]
    IllegalDelete: Type[BotocoreClientError]
    IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: Type[BotocoreClientError]
    IllegalUpdate: Type[BotocoreClientError]
    InconsistentQuantities: Type[BotocoreClientError]
    InvalidArgument: Type[BotocoreClientError]
    InvalidDefaultRootObject: Type[BotocoreClientError]
    InvalidErrorCode: Type[BotocoreClientError]
    InvalidForwardCookies: Type[BotocoreClientError]
    InvalidGeoRestrictionParameter: Type[BotocoreClientError]
    InvalidHeadersForS3Origin: Type[BotocoreClientError]
    InvalidIfMatchVersion: Type[BotocoreClientError]
    InvalidLambdaFunctionAssociation: Type[BotocoreClientError]
    InvalidLocationCode: Type[BotocoreClientError]
    InvalidMinimumProtocolVersion: Type[BotocoreClientError]
    InvalidOrigin: Type[BotocoreClientError]
    InvalidOriginAccessIdentity: Type[BotocoreClientError]
    InvalidOriginKeepaliveTimeout: Type[BotocoreClientError]
    InvalidOriginReadTimeout: Type[BotocoreClientError]
    InvalidProtocolSettings: Type[BotocoreClientError]
    InvalidQueryStringParameters: Type[BotocoreClientError]
    InvalidRelativePath: Type[BotocoreClientError]
    InvalidRequiredProtocol: Type[BotocoreClientError]
    InvalidResponseCode: Type[BotocoreClientError]
    InvalidTTLOrder: Type[BotocoreClientError]
    InvalidTagging: Type[BotocoreClientError]
    InvalidViewerCertificate: Type[BotocoreClientError]
    InvalidWebACLId: Type[BotocoreClientError]
    KeyGroupAlreadyExists: Type[BotocoreClientError]
    MissingBody: Type[BotocoreClientError]
    NoSuchCachePolicy: Type[BotocoreClientError]
    NoSuchCloudFrontOriginAccessIdentity: Type[BotocoreClientError]
    NoSuchDistribution: Type[BotocoreClientError]
    NoSuchFieldLevelEncryptionConfig: Type[BotocoreClientError]
    NoSuchFieldLevelEncryptionProfile: Type[BotocoreClientError]
    NoSuchInvalidation: Type[BotocoreClientError]
    NoSuchOrigin: Type[BotocoreClientError]
    NoSuchOriginRequestPolicy: Type[BotocoreClientError]
    NoSuchPublicKey: Type[BotocoreClientError]
    NoSuchRealtimeLogConfig: Type[BotocoreClientError]
    NoSuchResource: Type[BotocoreClientError]
    NoSuchStreamingDistribution: Type[BotocoreClientError]
    OriginRequestPolicyAlreadyExists: Type[BotocoreClientError]
    OriginRequestPolicyInUse: Type[BotocoreClientError]
    PreconditionFailed: Type[BotocoreClientError]
    PublicKeyAlreadyExists: Type[BotocoreClientError]
    PublicKeyInUse: Type[BotocoreClientError]
    QueryArgProfileEmpty: Type[BotocoreClientError]
    RealtimeLogConfigAlreadyExists: Type[BotocoreClientError]
    RealtimeLogConfigInUse: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    StreamingDistributionAlreadyExists: Type[BotocoreClientError]
    StreamingDistributionNotDisabled: Type[BotocoreClientError]
    TooManyCacheBehaviors: Type[BotocoreClientError]
    TooManyCachePolicies: Type[BotocoreClientError]
    TooManyCertificates: Type[BotocoreClientError]
    TooManyCloudFrontOriginAccessIdentities: Type[BotocoreClientError]
    TooManyCookieNamesInWhiteList: Type[BotocoreClientError]
    TooManyCookiesInCachePolicy: Type[BotocoreClientError]
    TooManyCookiesInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyDistributionCNAMEs: Type[BotocoreClientError]
    TooManyDistributions: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToCachePolicy: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToKeyGroup: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToOriginRequestPolicy: Type[BotocoreClientError]
    TooManyDistributionsWithLambdaAssociations: Type[BotocoreClientError]
    TooManyDistributionsWithSingleFunctionARN: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionConfigs: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionContentTypeProfiles: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionEncryptionEntities: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionFieldPatterns: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionProfiles: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionQueryArgProfiles: Type[BotocoreClientError]
    TooManyHeadersInCachePolicy: Type[BotocoreClientError]
    TooManyHeadersInForwardedValues: Type[BotocoreClientError]
    TooManyHeadersInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyInvalidationsInProgress: Type[BotocoreClientError]
    TooManyKeyGroups: Type[BotocoreClientError]
    TooManyKeyGroupsAssociatedToDistribution: Type[BotocoreClientError]
    TooManyLambdaFunctionAssociations: Type[BotocoreClientError]
    TooManyOriginCustomHeaders: Type[BotocoreClientError]
    TooManyOriginGroupsPerDistribution: Type[BotocoreClientError]
    TooManyOriginRequestPolicies: Type[BotocoreClientError]
    TooManyOrigins: Type[BotocoreClientError]
    TooManyPublicKeys: Type[BotocoreClientError]
    TooManyPublicKeysInKeyGroup: Type[BotocoreClientError]
    TooManyQueryStringParameters: Type[BotocoreClientError]
    TooManyQueryStringsInCachePolicy: Type[BotocoreClientError]
    TooManyQueryStringsInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyRealtimeLogConfigs: Type[BotocoreClientError]
    TooManyStreamingDistributionCNAMEs: Type[BotocoreClientError]
    TooManyStreamingDistributions: Type[BotocoreClientError]
    TooManyTrustedSigners: Type[BotocoreClientError]
    TrustedKeyGroupDoesNotExist: Type[BotocoreClientError]
    TrustedSignerDoesNotExist: Type[BotocoreClientError]


class CloudFrontClient:
    """
    [CloudFront.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.can_paginate)
        """

    def create_cache_policy(
        self, CachePolicyConfig: "CachePolicyConfigTypeDef"
    ) -> CreateCachePolicyResultTypeDef:
        """
        [Client.create_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_cache_policy)
        """

    def create_cloud_front_origin_access_identity(
        self, CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef"
    ) -> CreateCloudFrontOriginAccessIdentityResultTypeDef:
        """
        [Client.create_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_cloud_front_origin_access_identity)
        """

    def create_distribution(
        self, DistributionConfig: "DistributionConfigTypeDef"
    ) -> CreateDistributionResultTypeDef:
        """
        [Client.create_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_distribution)
        """

    def create_distribution_with_tags(
        self, DistributionConfigWithTags: DistributionConfigWithTagsTypeDef
    ) -> CreateDistributionWithTagsResultTypeDef:
        """
        [Client.create_distribution_with_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_distribution_with_tags)
        """

    def create_field_level_encryption_config(
        self, FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef"
    ) -> CreateFieldLevelEncryptionConfigResultTypeDef:
        """
        [Client.create_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_field_level_encryption_config)
        """

    def create_field_level_encryption_profile(
        self, FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef"
    ) -> CreateFieldLevelEncryptionProfileResultTypeDef:
        """
        [Client.create_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_field_level_encryption_profile)
        """

    def create_invalidation(
        self, DistributionId: str, InvalidationBatch: "InvalidationBatchTypeDef"
    ) -> CreateInvalidationResultTypeDef:
        """
        [Client.create_invalidation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_invalidation)
        """

    def create_key_group(
        self, KeyGroupConfig: "KeyGroupConfigTypeDef"
    ) -> CreateKeyGroupResultTypeDef:
        """
        [Client.create_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_key_group)
        """

    def create_monitoring_subscription(
        self, DistributionId: str, MonitoringSubscription: "MonitoringSubscriptionTypeDef"
    ) -> CreateMonitoringSubscriptionResultTypeDef:
        """
        [Client.create_monitoring_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_monitoring_subscription)
        """

    def create_origin_request_policy(
        self, OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef"
    ) -> CreateOriginRequestPolicyResultTypeDef:
        """
        [Client.create_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_origin_request_policy)
        """

    def create_public_key(
        self, PublicKeyConfig: "PublicKeyConfigTypeDef"
    ) -> CreatePublicKeyResultTypeDef:
        """
        [Client.create_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_public_key)
        """

    def create_realtime_log_config(
        self, EndPoints: List["EndPointTypeDef"], Fields: List[str], Name: str, SamplingRate: int
    ) -> CreateRealtimeLogConfigResultTypeDef:
        """
        [Client.create_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_realtime_log_config)
        """

    def create_streaming_distribution(
        self, StreamingDistributionConfig: "StreamingDistributionConfigTypeDef"
    ) -> CreateStreamingDistributionResultTypeDef:
        """
        [Client.create_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_streaming_distribution)
        """

    def create_streaming_distribution_with_tags(
        self, StreamingDistributionConfigWithTags: StreamingDistributionConfigWithTagsTypeDef
    ) -> CreateStreamingDistributionWithTagsResultTypeDef:
        """
        [Client.create_streaming_distribution_with_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.create_streaming_distribution_with_tags)
        """

    def delete_cache_policy(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_cache_policy)
        """

    def delete_cloud_front_origin_access_identity(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_cloud_front_origin_access_identity)
        """

    def delete_distribution(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_distribution)
        """

    def delete_field_level_encryption_config(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_field_level_encryption_config)
        """

    def delete_field_level_encryption_profile(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_field_level_encryption_profile)
        """

    def delete_key_group(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_key_group)
        """

    def delete_monitoring_subscription(self, DistributionId: str) -> Dict[str, Any]:
        """
        [Client.delete_monitoring_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_monitoring_subscription)
        """

    def delete_origin_request_policy(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_origin_request_policy)
        """

    def delete_public_key(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_public_key)
        """

    def delete_realtime_log_config(self, Name: str = None, ARN: str = None) -> None:
        """
        [Client.delete_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_realtime_log_config)
        """

    def delete_streaming_distribution(self, Id: str, IfMatch: str = None) -> None:
        """
        [Client.delete_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.delete_streaming_distribution)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.generate_presigned_url)
        """

    def get_cache_policy(self, Id: str) -> GetCachePolicyResultTypeDef:
        """
        [Client.get_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_cache_policy)
        """

    def get_cache_policy_config(self, Id: str) -> GetCachePolicyConfigResultTypeDef:
        """
        [Client.get_cache_policy_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_cache_policy_config)
        """

    def get_cloud_front_origin_access_identity(
        self, Id: str
    ) -> GetCloudFrontOriginAccessIdentityResultTypeDef:
        """
        [Client.get_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_cloud_front_origin_access_identity)
        """

    def get_cloud_front_origin_access_identity_config(
        self, Id: str
    ) -> GetCloudFrontOriginAccessIdentityConfigResultTypeDef:
        """
        [Client.get_cloud_front_origin_access_identity_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_cloud_front_origin_access_identity_config)
        """

    def get_distribution(self, Id: str) -> GetDistributionResultTypeDef:
        """
        [Client.get_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_distribution)
        """

    def get_distribution_config(self, Id: str) -> GetDistributionConfigResultTypeDef:
        """
        [Client.get_distribution_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_distribution_config)
        """

    def get_field_level_encryption(self, Id: str) -> GetFieldLevelEncryptionResultTypeDef:
        """
        [Client.get_field_level_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption)
        """

    def get_field_level_encryption_config(
        self, Id: str
    ) -> GetFieldLevelEncryptionConfigResultTypeDef:
        """
        [Client.get_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_config)
        """

    def get_field_level_encryption_profile(
        self, Id: str
    ) -> GetFieldLevelEncryptionProfileResultTypeDef:
        """
        [Client.get_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_profile)
        """

    def get_field_level_encryption_profile_config(
        self, Id: str
    ) -> GetFieldLevelEncryptionProfileConfigResultTypeDef:
        """
        [Client.get_field_level_encryption_profile_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_profile_config)
        """

    def get_invalidation(self, DistributionId: str, Id: str) -> GetInvalidationResultTypeDef:
        """
        [Client.get_invalidation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_invalidation)
        """

    def get_key_group(self, Id: str) -> GetKeyGroupResultTypeDef:
        """
        [Client.get_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_key_group)
        """

    def get_key_group_config(self, Id: str) -> GetKeyGroupConfigResultTypeDef:
        """
        [Client.get_key_group_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_key_group_config)
        """

    def get_monitoring_subscription(
        self, DistributionId: str
    ) -> GetMonitoringSubscriptionResultTypeDef:
        """
        [Client.get_monitoring_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_monitoring_subscription)
        """

    def get_origin_request_policy(self, Id: str) -> GetOriginRequestPolicyResultTypeDef:
        """
        [Client.get_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_origin_request_policy)
        """

    def get_origin_request_policy_config(
        self, Id: str
    ) -> GetOriginRequestPolicyConfigResultTypeDef:
        """
        [Client.get_origin_request_policy_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_origin_request_policy_config)
        """

    def get_public_key(self, Id: str) -> GetPublicKeyResultTypeDef:
        """
        [Client.get_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_public_key)
        """

    def get_public_key_config(self, Id: str) -> GetPublicKeyConfigResultTypeDef:
        """
        [Client.get_public_key_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_public_key_config)
        """

    def get_realtime_log_config(
        self, Name: str = None, ARN: str = None
    ) -> GetRealtimeLogConfigResultTypeDef:
        """
        [Client.get_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_realtime_log_config)
        """

    def get_streaming_distribution(self, Id: str) -> GetStreamingDistributionResultTypeDef:
        """
        [Client.get_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_streaming_distribution)
        """

    def get_streaming_distribution_config(
        self, Id: str
    ) -> GetStreamingDistributionConfigResultTypeDef:
        """
        [Client.get_streaming_distribution_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.get_streaming_distribution_config)
        """

    def list_cache_policies(
        self, Type: Literal["managed", "custom"] = None, Marker: str = None, MaxItems: str = None
    ) -> ListCachePoliciesResultTypeDef:
        """
        [Client.list_cache_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_cache_policies)
        """

    def list_cloud_front_origin_access_identities(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListCloudFrontOriginAccessIdentitiesResultTypeDef:
        """
        [Client.list_cloud_front_origin_access_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_cloud_front_origin_access_identities)
        """

    def list_distributions(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsResultTypeDef:
        """
        [Client.list_distributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_distributions)
        """

    def list_distributions_by_cache_policy_id(
        self, CachePolicyId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByCachePolicyIdResultTypeDef:
        """
        [Client.list_distributions_by_cache_policy_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_cache_policy_id)
        """

    def list_distributions_by_key_group(
        self, KeyGroupId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByKeyGroupResultTypeDef:
        """
        [Client.list_distributions_by_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_key_group)
        """

    def list_distributions_by_origin_request_policy_id(
        self, OriginRequestPolicyId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByOriginRequestPolicyIdResultTypeDef:
        """
        [Client.list_distributions_by_origin_request_policy_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_origin_request_policy_id)
        """

    def list_distributions_by_realtime_log_config(
        self,
        Marker: str = None,
        MaxItems: str = None,
        RealtimeLogConfigName: str = None,
        RealtimeLogConfigArn: str = None,
    ) -> ListDistributionsByRealtimeLogConfigResultTypeDef:
        """
        [Client.list_distributions_by_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_realtime_log_config)
        """

    def list_distributions_by_web_acl_id(
        self, WebACLId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByWebACLIdResultTypeDef:
        """
        [Client.list_distributions_by_web_acl_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_web_acl_id)
        """

    def list_field_level_encryption_configs(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListFieldLevelEncryptionConfigsResultTypeDef:
        """
        [Client.list_field_level_encryption_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_field_level_encryption_configs)
        """

    def list_field_level_encryption_profiles(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListFieldLevelEncryptionProfilesResultTypeDef:
        """
        [Client.list_field_level_encryption_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_field_level_encryption_profiles)
        """

    def list_invalidations(
        self, DistributionId: str, Marker: str = None, MaxItems: str = None
    ) -> ListInvalidationsResultTypeDef:
        """
        [Client.list_invalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_invalidations)
        """

    def list_key_groups(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListKeyGroupsResultTypeDef:
        """
        [Client.list_key_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_key_groups)
        """

    def list_origin_request_policies(
        self, Type: Literal["managed", "custom"] = None, Marker: str = None, MaxItems: str = None
    ) -> ListOriginRequestPoliciesResultTypeDef:
        """
        [Client.list_origin_request_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_origin_request_policies)
        """

    def list_public_keys(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListPublicKeysResultTypeDef:
        """
        [Client.list_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_public_keys)
        """

    def list_realtime_log_configs(
        self, MaxItems: str = None, Marker: str = None
    ) -> ListRealtimeLogConfigsResultTypeDef:
        """
        [Client.list_realtime_log_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_realtime_log_configs)
        """

    def list_streaming_distributions(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListStreamingDistributionsResultTypeDef:
        """
        [Client.list_streaming_distributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_streaming_distributions)
        """

    def list_tags_for_resource(self, Resource: str) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.list_tags_for_resource)
        """

    def tag_resource(self, Resource: str, Tags: "TagsTypeDef") -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.tag_resource)
        """

    def untag_resource(self, Resource: str, TagKeys: TagKeysTypeDef) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.untag_resource)
        """

    def update_cache_policy(
        self, CachePolicyConfig: "CachePolicyConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdateCachePolicyResultTypeDef:
        """
        [Client.update_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_cache_policy)
        """

    def update_cloud_front_origin_access_identity(
        self,
        CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef",
        Id: str,
        IfMatch: str = None,
    ) -> UpdateCloudFrontOriginAccessIdentityResultTypeDef:
        """
        [Client.update_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_cloud_front_origin_access_identity)
        """

    def update_distribution(
        self, DistributionConfig: "DistributionConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdateDistributionResultTypeDef:
        """
        [Client.update_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_distribution)
        """

    def update_field_level_encryption_config(
        self,
        FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef",
        Id: str,
        IfMatch: str = None,
    ) -> UpdateFieldLevelEncryptionConfigResultTypeDef:
        """
        [Client.update_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_field_level_encryption_config)
        """

    def update_field_level_encryption_profile(
        self,
        FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef",
        Id: str,
        IfMatch: str = None,
    ) -> UpdateFieldLevelEncryptionProfileResultTypeDef:
        """
        [Client.update_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_field_level_encryption_profile)
        """

    def update_key_group(
        self, KeyGroupConfig: "KeyGroupConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdateKeyGroupResultTypeDef:
        """
        [Client.update_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_key_group)
        """

    def update_origin_request_policy(
        self,
        OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef",
        Id: str,
        IfMatch: str = None,
    ) -> UpdateOriginRequestPolicyResultTypeDef:
        """
        [Client.update_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_origin_request_policy)
        """

    def update_public_key(
        self, PublicKeyConfig: "PublicKeyConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdatePublicKeyResultTypeDef:
        """
        [Client.update_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_public_key)
        """

    def update_realtime_log_config(
        self,
        EndPoints: List["EndPointTypeDef"] = None,
        Fields: List[str] = None,
        Name: str = None,
        ARN: str = None,
        SamplingRate: int = None,
    ) -> UpdateRealtimeLogConfigResultTypeDef:
        """
        [Client.update_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_realtime_log_config)
        """

    def update_streaming_distribution(
        self,
        StreamingDistributionConfig: "StreamingDistributionConfigTypeDef",
        Id: str,
        IfMatch: str = None,
    ) -> UpdateStreamingDistributionResultTypeDef:
        """
        [Client.update_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Client.update_streaming_distribution)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cloud_front_origin_access_identities"]
    ) -> ListCloudFrontOriginAccessIdentitiesPaginator:
        """
        [Paginator.ListCloudFrontOriginAccessIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_distributions"]
    ) -> ListDistributionsPaginator:
        """
        [Paginator.ListDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invalidations"]
    ) -> ListInvalidationsPaginator:
        """
        [Paginator.ListInvalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_distributions"]
    ) -> ListStreamingDistributionsPaginator:
        """
        [Paginator.ListStreamingDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["distribution_deployed"]
    ) -> DistributionDeployedWaiter:
        """
        [Waiter.DistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["invalidation_completed"]
    ) -> InvalidationCompletedWaiter:
        """
        [Waiter.InvalidationCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_distribution_deployed"]
    ) -> StreamingDistributionDeployedWaiter:
        """
        [Waiter.StreamingDistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed)
        """
