"""
Type annotations for cloudfront service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudfront import CloudFrontClient

    client: CloudFrontClient = boto3.client("cloudfront")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    CachePolicyTypeType,
    FunctionStageType,
    OriginRequestPolicyTypeType,
    ResponseHeadersPolicyTypeType,
)
from .paginator import (
    ListCloudFrontOriginAccessIdentitiesPaginator,
    ListDistributionsPaginator,
    ListInvalidationsPaginator,
    ListStreamingDistributionsPaginator,
)
from .type_defs import (
    CachePolicyConfigTypeDef,
    CloudFrontOriginAccessIdentityConfigTypeDef,
    ContinuousDeploymentPolicyConfigTypeDef,
    CopyDistributionResultTypeDef,
    CreateCachePolicyResultTypeDef,
    CreateCloudFrontOriginAccessIdentityResultTypeDef,
    CreateContinuousDeploymentPolicyResultTypeDef,
    CreateDistributionResultTypeDef,
    CreateDistributionWithTagsResultTypeDef,
    CreateFieldLevelEncryptionConfigResultTypeDef,
    CreateFieldLevelEncryptionProfileResultTypeDef,
    CreateFunctionResultTypeDef,
    CreateInvalidationResultTypeDef,
    CreateKeyGroupResultTypeDef,
    CreateMonitoringSubscriptionResultTypeDef,
    CreateOriginAccessControlResultTypeDef,
    CreateOriginRequestPolicyResultTypeDef,
    CreatePublicKeyResultTypeDef,
    CreateRealtimeLogConfigResultTypeDef,
    CreateResponseHeadersPolicyResultTypeDef,
    CreateStreamingDistributionResultTypeDef,
    CreateStreamingDistributionWithTagsResultTypeDef,
    DescribeFunctionResultTypeDef,
    DistributionConfigTypeDef,
    DistributionConfigWithTagsTypeDef,
    EndPointTypeDef,
    FieldLevelEncryptionConfigTypeDef,
    FieldLevelEncryptionProfileConfigTypeDef,
    FunctionConfigTypeDef,
    GetCachePolicyConfigResultTypeDef,
    GetCachePolicyResultTypeDef,
    GetCloudFrontOriginAccessIdentityConfigResultTypeDef,
    GetCloudFrontOriginAccessIdentityResultTypeDef,
    GetContinuousDeploymentPolicyConfigResultTypeDef,
    GetContinuousDeploymentPolicyResultTypeDef,
    GetDistributionConfigResultTypeDef,
    GetDistributionResultTypeDef,
    GetFieldLevelEncryptionConfigResultTypeDef,
    GetFieldLevelEncryptionProfileConfigResultTypeDef,
    GetFieldLevelEncryptionProfileResultTypeDef,
    GetFieldLevelEncryptionResultTypeDef,
    GetFunctionResultTypeDef,
    GetInvalidationResultTypeDef,
    GetKeyGroupConfigResultTypeDef,
    GetKeyGroupResultTypeDef,
    GetMonitoringSubscriptionResultTypeDef,
    GetOriginAccessControlConfigResultTypeDef,
    GetOriginAccessControlResultTypeDef,
    GetOriginRequestPolicyConfigResultTypeDef,
    GetOriginRequestPolicyResultTypeDef,
    GetPublicKeyConfigResultTypeDef,
    GetPublicKeyResultTypeDef,
    GetRealtimeLogConfigResultTypeDef,
    GetResponseHeadersPolicyConfigResultTypeDef,
    GetResponseHeadersPolicyResultTypeDef,
    GetStreamingDistributionConfigResultTypeDef,
    GetStreamingDistributionResultTypeDef,
    InvalidationBatchTypeDef,
    KeyGroupConfigTypeDef,
    ListCachePoliciesResultTypeDef,
    ListCloudFrontOriginAccessIdentitiesResultTypeDef,
    ListConflictingAliasesResultTypeDef,
    ListContinuousDeploymentPoliciesResultTypeDef,
    ListDistributionsByCachePolicyIdResultTypeDef,
    ListDistributionsByKeyGroupResultTypeDef,
    ListDistributionsByOriginRequestPolicyIdResultTypeDef,
    ListDistributionsByRealtimeLogConfigResultTypeDef,
    ListDistributionsByResponseHeadersPolicyIdResultTypeDef,
    ListDistributionsByWebACLIdResultTypeDef,
    ListDistributionsResultTypeDef,
    ListFieldLevelEncryptionConfigsResultTypeDef,
    ListFieldLevelEncryptionProfilesResultTypeDef,
    ListFunctionsResultTypeDef,
    ListInvalidationsResultTypeDef,
    ListKeyGroupsResultTypeDef,
    ListOriginAccessControlsResultTypeDef,
    ListOriginRequestPoliciesResultTypeDef,
    ListPublicKeysResultTypeDef,
    ListRealtimeLogConfigsResultTypeDef,
    ListResponseHeadersPoliciesResultTypeDef,
    ListStreamingDistributionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    MonitoringSubscriptionTypeDef,
    OriginAccessControlConfigTypeDef,
    OriginRequestPolicyConfigTypeDef,
    PublicKeyConfigTypeDef,
    PublishFunctionResultTypeDef,
    ResponseHeadersPolicyConfigTypeDef,
    StreamingDistributionConfigTypeDef,
    StreamingDistributionConfigWithTagsTypeDef,
    TagKeysTypeDef,
    TagsTypeDef,
    TestFunctionResultTypeDef,
    UpdateCachePolicyResultTypeDef,
    UpdateCloudFrontOriginAccessIdentityResultTypeDef,
    UpdateContinuousDeploymentPolicyResultTypeDef,
    UpdateDistributionResultTypeDef,
    UpdateDistributionWithStagingConfigResultTypeDef,
    UpdateFieldLevelEncryptionConfigResultTypeDef,
    UpdateFieldLevelEncryptionProfileResultTypeDef,
    UpdateFunctionResultTypeDef,
    UpdateKeyGroupResultTypeDef,
    UpdateOriginAccessControlResultTypeDef,
    UpdateOriginRequestPolicyResultTypeDef,
    UpdatePublicKeyResultTypeDef,
    UpdateRealtimeLogConfigResultTypeDef,
    UpdateResponseHeadersPolicyResultTypeDef,
    UpdateStreamingDistributionResultTypeDef,
)
from .waiter import (
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
    ContinuousDeploymentPolicyAlreadyExists: Type[BotocoreClientError]
    ContinuousDeploymentPolicyInUse: Type[BotocoreClientError]
    DistributionAlreadyExists: Type[BotocoreClientError]
    DistributionNotDisabled: Type[BotocoreClientError]
    FieldLevelEncryptionConfigAlreadyExists: Type[BotocoreClientError]
    FieldLevelEncryptionConfigInUse: Type[BotocoreClientError]
    FieldLevelEncryptionProfileAlreadyExists: Type[BotocoreClientError]
    FieldLevelEncryptionProfileInUse: Type[BotocoreClientError]
    FieldLevelEncryptionProfileSizeExceeded: Type[BotocoreClientError]
    FunctionAlreadyExists: Type[BotocoreClientError]
    FunctionInUse: Type[BotocoreClientError]
    FunctionSizeLimitExceeded: Type[BotocoreClientError]
    IllegalDelete: Type[BotocoreClientError]
    IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: Type[BotocoreClientError]
    IllegalOriginAccessConfiguration: Type[BotocoreClientError]
    IllegalUpdate: Type[BotocoreClientError]
    InconsistentQuantities: Type[BotocoreClientError]
    InvalidArgument: Type[BotocoreClientError]
    InvalidDefaultRootObject: Type[BotocoreClientError]
    InvalidDomainNameForOriginAccessControl: Type[BotocoreClientError]
    InvalidErrorCode: Type[BotocoreClientError]
    InvalidForwardCookies: Type[BotocoreClientError]
    InvalidFunctionAssociation: Type[BotocoreClientError]
    InvalidGeoRestrictionParameter: Type[BotocoreClientError]
    InvalidHeadersForS3Origin: Type[BotocoreClientError]
    InvalidIfMatchVersion: Type[BotocoreClientError]
    InvalidLambdaFunctionAssociation: Type[BotocoreClientError]
    InvalidLocationCode: Type[BotocoreClientError]
    InvalidMinimumProtocolVersion: Type[BotocoreClientError]
    InvalidOrigin: Type[BotocoreClientError]
    InvalidOriginAccessControl: Type[BotocoreClientError]
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
    MonitoringSubscriptionAlreadyExists: Type[BotocoreClientError]
    NoSuchCachePolicy: Type[BotocoreClientError]
    NoSuchCloudFrontOriginAccessIdentity: Type[BotocoreClientError]
    NoSuchContinuousDeploymentPolicy: Type[BotocoreClientError]
    NoSuchDistribution: Type[BotocoreClientError]
    NoSuchFieldLevelEncryptionConfig: Type[BotocoreClientError]
    NoSuchFieldLevelEncryptionProfile: Type[BotocoreClientError]
    NoSuchFunctionExists: Type[BotocoreClientError]
    NoSuchInvalidation: Type[BotocoreClientError]
    NoSuchMonitoringSubscription: Type[BotocoreClientError]
    NoSuchOrigin: Type[BotocoreClientError]
    NoSuchOriginAccessControl: Type[BotocoreClientError]
    NoSuchOriginRequestPolicy: Type[BotocoreClientError]
    NoSuchPublicKey: Type[BotocoreClientError]
    NoSuchRealtimeLogConfig: Type[BotocoreClientError]
    NoSuchResource: Type[BotocoreClientError]
    NoSuchResponseHeadersPolicy: Type[BotocoreClientError]
    NoSuchStreamingDistribution: Type[BotocoreClientError]
    OriginAccessControlAlreadyExists: Type[BotocoreClientError]
    OriginAccessControlInUse: Type[BotocoreClientError]
    OriginRequestPolicyAlreadyExists: Type[BotocoreClientError]
    OriginRequestPolicyInUse: Type[BotocoreClientError]
    PreconditionFailed: Type[BotocoreClientError]
    PublicKeyAlreadyExists: Type[BotocoreClientError]
    PublicKeyInUse: Type[BotocoreClientError]
    QueryArgProfileEmpty: Type[BotocoreClientError]
    RealtimeLogConfigAlreadyExists: Type[BotocoreClientError]
    RealtimeLogConfigInUse: Type[BotocoreClientError]
    RealtimeLogConfigOwnerMismatch: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResponseHeadersPolicyAlreadyExists: Type[BotocoreClientError]
    ResponseHeadersPolicyInUse: Type[BotocoreClientError]
    StagingDistributionInUse: Type[BotocoreClientError]
    StreamingDistributionAlreadyExists: Type[BotocoreClientError]
    StreamingDistributionNotDisabled: Type[BotocoreClientError]
    TestFunctionFailed: Type[BotocoreClientError]
    TooLongCSPInResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyCacheBehaviors: Type[BotocoreClientError]
    TooManyCachePolicies: Type[BotocoreClientError]
    TooManyCertificates: Type[BotocoreClientError]
    TooManyCloudFrontOriginAccessIdentities: Type[BotocoreClientError]
    TooManyContinuousDeploymentPolicies: Type[BotocoreClientError]
    TooManyCookieNamesInWhiteList: Type[BotocoreClientError]
    TooManyCookiesInCachePolicy: Type[BotocoreClientError]
    TooManyCookiesInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyCustomHeadersInResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyDistributionCNAMEs: Type[BotocoreClientError]
    TooManyDistributions: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToCachePolicy: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToKeyGroup: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToOriginAccessControl: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToOriginRequestPolicy: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyDistributionsWithFunctionAssociations: Type[BotocoreClientError]
    TooManyDistributionsWithLambdaAssociations: Type[BotocoreClientError]
    TooManyDistributionsWithSingleFunctionARN: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionConfigs: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionContentTypeProfiles: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionEncryptionEntities: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionFieldPatterns: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionProfiles: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionQueryArgProfiles: Type[BotocoreClientError]
    TooManyFunctionAssociations: Type[BotocoreClientError]
    TooManyFunctions: Type[BotocoreClientError]
    TooManyHeadersInCachePolicy: Type[BotocoreClientError]
    TooManyHeadersInForwardedValues: Type[BotocoreClientError]
    TooManyHeadersInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyInvalidationsInProgress: Type[BotocoreClientError]
    TooManyKeyGroups: Type[BotocoreClientError]
    TooManyKeyGroupsAssociatedToDistribution: Type[BotocoreClientError]
    TooManyLambdaFunctionAssociations: Type[BotocoreClientError]
    TooManyOriginAccessControls: Type[BotocoreClientError]
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
    TooManyRemoveHeadersInResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyResponseHeadersPolicies: Type[BotocoreClientError]
    TooManyStreamingDistributionCNAMEs: Type[BotocoreClientError]
    TooManyStreamingDistributions: Type[BotocoreClientError]
    TooManyTrustedSigners: Type[BotocoreClientError]
    TrustedKeyGroupDoesNotExist: Type[BotocoreClientError]
    TrustedSignerDoesNotExist: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]

class CloudFrontClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudFrontClient exceptions.
        """
    def associate_alias(self, *, TargetDistributionId: str, Alias: str) -> None:
        """
        Associates an alias (also known as a CNAME or an alternate domain name) with a
        CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.associate_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#associate_alias)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#close)
        """
    def copy_distribution(
        self,
        *,
        PrimaryDistributionId: str,
        CallerReference: str,
        Staging: bool = None,
        IfMatch: str = None,
        Enabled: bool = None
    ) -> CopyDistributionResultTypeDef:
        """
        Creates a staging distribution using the configuration of the provided primary
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.copy_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#copy_distribution)
        """
    def create_cache_policy(
        self, *, CachePolicyConfig: "CachePolicyConfigTypeDef"
    ) -> CreateCachePolicyResultTypeDef:
        """
        Creates a cache policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_cache_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_cache_policy)
        """
    def create_cloud_front_origin_access_identity(
        self, *, CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef"
    ) -> CreateCloudFrontOriginAccessIdentityResultTypeDef:
        """
        Creates a new origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_cloud_front_origin_access_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_cloud_front_origin_access_identity)
        """
    def create_continuous_deployment_policy(
        self, *, ContinuousDeploymentPolicyConfig: "ContinuousDeploymentPolicyConfigTypeDef"
    ) -> CreateContinuousDeploymentPolicyResultTypeDef:
        """
        Creates a continuous deployment policy that distributes traffic for a custom
        domain name to two different CloudFront distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_continuous_deployment_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_continuous_deployment_policy)
        """
    def create_distribution(
        self, *, DistributionConfig: "DistributionConfigTypeDef"
    ) -> CreateDistributionResultTypeDef:
        """
        Creates a CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_distribution)
        """
    def create_distribution_with_tags(
        self, *, DistributionConfigWithTags: "DistributionConfigWithTagsTypeDef"
    ) -> CreateDistributionWithTagsResultTypeDef:
        """
        Create a new distribution with tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_distribution_with_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_distribution_with_tags)
        """
    def create_field_level_encryption_config(
        self, *, FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef"
    ) -> CreateFieldLevelEncryptionConfigResultTypeDef:
        """
        Create a new field-level encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_field_level_encryption_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_field_level_encryption_config)
        """
    def create_field_level_encryption_profile(
        self, *, FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef"
    ) -> CreateFieldLevelEncryptionProfileResultTypeDef:
        """
        Create a field-level encryption profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_field_level_encryption_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_field_level_encryption_profile)
        """
    def create_function(
        self,
        *,
        Name: str,
        FunctionConfig: "FunctionConfigTypeDef",
        FunctionCode: Union[bytes, IO[bytes], StreamingBody]
    ) -> CreateFunctionResultTypeDef:
        """
        Creates a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_function)
        """
    def create_invalidation(
        self, *, DistributionId: str, InvalidationBatch: "InvalidationBatchTypeDef"
    ) -> CreateInvalidationResultTypeDef:
        """
        Create a new invalidation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_invalidation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_invalidation)
        """
    def create_key_group(
        self, *, KeyGroupConfig: "KeyGroupConfigTypeDef"
    ) -> CreateKeyGroupResultTypeDef:
        """
        Creates a key group that you can use with `CloudFront signed URLs and signed
        cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Priv
        ateContent.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_key_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_key_group)
        """
    def create_monitoring_subscription(
        self, *, DistributionId: str, MonitoringSubscription: "MonitoringSubscriptionTypeDef"
    ) -> CreateMonitoringSubscriptionResultTypeDef:
        """
        Enables additional CloudWatch metrics for the specified CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_monitoring_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_monitoring_subscription)
        """
    def create_origin_access_control(
        self, *, OriginAccessControlConfig: "OriginAccessControlConfigTypeDef"
    ) -> CreateOriginAccessControlResultTypeDef:
        """
        Creates a new origin access control in CloudFront.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_origin_access_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_origin_access_control)
        """
    def create_origin_request_policy(
        self, *, OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef"
    ) -> CreateOriginRequestPolicyResultTypeDef:
        """
        Creates an origin request policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_origin_request_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_origin_request_policy)
        """
    def create_public_key(
        self, *, PublicKeyConfig: "PublicKeyConfigTypeDef"
    ) -> CreatePublicKeyResultTypeDef:
        """
        Uploads a public key to CloudFront that you can use with `signed URLs and signed
        cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Priv
        ateContent.html>`__, or with `field-level encryption
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-
        enc...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_public_key)
        """
    def create_realtime_log_config(
        self, *, EndPoints: List["EndPointTypeDef"], Fields: List[str], Name: str, SamplingRate: int
    ) -> CreateRealtimeLogConfigResultTypeDef:
        """
        Creates a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_realtime_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_realtime_log_config)
        """
    def create_response_headers_policy(
        self, *, ResponseHeadersPolicyConfig: "ResponseHeadersPolicyConfigTypeDef"
    ) -> CreateResponseHeadersPolicyResultTypeDef:
        """
        Creates a response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_response_headers_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_response_headers_policy)
        """
    def create_streaming_distribution(
        self, *, StreamingDistributionConfig: "StreamingDistributionConfigTypeDef"
    ) -> CreateStreamingDistributionResultTypeDef:
        """
        This API is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_streaming_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_streaming_distribution)
        """
    def create_streaming_distribution_with_tags(
        self, *, StreamingDistributionConfigWithTags: "StreamingDistributionConfigWithTagsTypeDef"
    ) -> CreateStreamingDistributionWithTagsResultTypeDef:
        """
        This API is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.create_streaming_distribution_with_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#create_streaming_distribution_with_tags)
        """
    def delete_cache_policy(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Deletes a cache policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_cache_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_cache_policy)
        """
    def delete_cloud_front_origin_access_identity(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Delete an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_cloud_front_origin_access_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_cloud_front_origin_access_identity)
        """
    def delete_continuous_deployment_policy(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Deletes a continuous deployment policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_continuous_deployment_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_continuous_deployment_policy)
        """
    def delete_distribution(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Delete a distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_distribution)
        """
    def delete_field_level_encryption_config(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Remove a field-level encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_field_level_encryption_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_field_level_encryption_config)
        """
    def delete_field_level_encryption_profile(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Remove a field-level encryption profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_field_level_encryption_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_field_level_encryption_profile)
        """
    def delete_function(self, *, Name: str, IfMatch: str) -> None:
        """
        Deletes a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_function)
        """
    def delete_key_group(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Deletes a key group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_key_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_key_group)
        """
    def delete_monitoring_subscription(self, *, DistributionId: str) -> Dict[str, Any]:
        """
        Disables additional CloudWatch metrics for the specified CloudFront
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_monitoring_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_monitoring_subscription)
        """
    def delete_origin_access_control(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Deletes a CloudFront origin access control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_origin_access_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_origin_access_control)
        """
    def delete_origin_request_policy(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Deletes an origin request policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_origin_request_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_origin_request_policy)
        """
    def delete_public_key(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Remove a public key you previously added to CloudFront.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_public_key)
        """
    def delete_realtime_log_config(self, *, Name: str = None, ARN: str = None) -> None:
        """
        Deletes a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_realtime_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_realtime_log_config)
        """
    def delete_response_headers_policy(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Deletes a response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_response_headers_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_response_headers_policy)
        """
    def delete_streaming_distribution(self, *, Id: str, IfMatch: str = None) -> None:
        """
        Delete a streaming distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.delete_streaming_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#delete_streaming_distribution)
        """
    def describe_function(
        self, *, Name: str, Stage: FunctionStageType = None
    ) -> DescribeFunctionResultTypeDef:
        """
        Gets configuration information and metadata about a CloudFront function, but not
        the function's code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.describe_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#describe_function)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#generate_presigned_url)
        """
    def get_cache_policy(self, *, Id: str) -> GetCachePolicyResultTypeDef:
        """
        Gets a cache policy, including the following metadata * The policy's identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_cache_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_cache_policy)
        """
    def get_cache_policy_config(self, *, Id: str) -> GetCachePolicyConfigResultTypeDef:
        """
        Gets a cache policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_cache_policy_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_cache_policy_config)
        """
    def get_cloud_front_origin_access_identity(
        self, *, Id: str
    ) -> GetCloudFrontOriginAccessIdentityResultTypeDef:
        """
        Get the information about an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_cloud_front_origin_access_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_cloud_front_origin_access_identity)
        """
    def get_cloud_front_origin_access_identity_config(
        self, *, Id: str
    ) -> GetCloudFrontOriginAccessIdentityConfigResultTypeDef:
        """
        Get the configuration information about an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_cloud_front_origin_access_identity_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_cloud_front_origin_access_identity_config)
        """
    def get_continuous_deployment_policy(
        self, *, Id: str
    ) -> GetContinuousDeploymentPolicyResultTypeDef:
        """
        Gets a continuous deployment policy, including metadata (the policy's identifier
        and the date and time when the policy was last modified).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_continuous_deployment_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_continuous_deployment_policy)
        """
    def get_continuous_deployment_policy_config(
        self, *, Id: str
    ) -> GetContinuousDeploymentPolicyConfigResultTypeDef:
        """
        Gets configuration information about a continuous deployment policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_continuous_deployment_policy_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_continuous_deployment_policy_config)
        """
    def get_distribution(self, *, Id: str) -> GetDistributionResultTypeDef:
        """
        Get the information about a distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_distribution)
        """
    def get_distribution_config(self, *, Id: str) -> GetDistributionConfigResultTypeDef:
        """
        Get the configuration information about a distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_distribution_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_distribution_config)
        """
    def get_field_level_encryption(self, *, Id: str) -> GetFieldLevelEncryptionResultTypeDef:
        """
        Get the field-level encryption configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_field_level_encryption)
        """
    def get_field_level_encryption_config(
        self, *, Id: str
    ) -> GetFieldLevelEncryptionConfigResultTypeDef:
        """
        Get the field-level encryption configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_field_level_encryption_config)
        """
    def get_field_level_encryption_profile(
        self, *, Id: str
    ) -> GetFieldLevelEncryptionProfileResultTypeDef:
        """
        Get the field-level encryption profile information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_field_level_encryption_profile)
        """
    def get_field_level_encryption_profile_config(
        self, *, Id: str
    ) -> GetFieldLevelEncryptionProfileConfigResultTypeDef:
        """
        Get the field-level encryption profile configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_profile_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_field_level_encryption_profile_config)
        """
    def get_function(
        self, *, Name: str, Stage: FunctionStageType = None
    ) -> GetFunctionResultTypeDef:
        """
        Gets the code of a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_function)
        """
    def get_invalidation(self, *, DistributionId: str, Id: str) -> GetInvalidationResultTypeDef:
        """
        Get the information about an invalidation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_invalidation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_invalidation)
        """
    def get_key_group(self, *, Id: str) -> GetKeyGroupResultTypeDef:
        """
        Gets a key group, including the date and time when the key group was last
        modified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_key_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_key_group)
        """
    def get_key_group_config(self, *, Id: str) -> GetKeyGroupConfigResultTypeDef:
        """
        Gets a key group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_key_group_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_key_group_config)
        """
    def get_monitoring_subscription(
        self, *, DistributionId: str
    ) -> GetMonitoringSubscriptionResultTypeDef:
        """
        Gets information about whether additional CloudWatch metrics are enabled for the
        specified CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_monitoring_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_monitoring_subscription)
        """
    def get_origin_access_control(self, *, Id: str) -> GetOriginAccessControlResultTypeDef:
        """
        Gets a CloudFront origin access control, including its unique identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_origin_access_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_origin_access_control)
        """
    def get_origin_access_control_config(
        self, *, Id: str
    ) -> GetOriginAccessControlConfigResultTypeDef:
        """
        Gets a CloudFront origin access control configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_origin_access_control_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_origin_access_control_config)
        """
    def get_origin_request_policy(self, *, Id: str) -> GetOriginRequestPolicyResultTypeDef:
        """
        Gets an origin request policy, including the following metadata * The policy's
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_origin_request_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_origin_request_policy)
        """
    def get_origin_request_policy_config(
        self, *, Id: str
    ) -> GetOriginRequestPolicyConfigResultTypeDef:
        """
        Gets an origin request policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_origin_request_policy_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_origin_request_policy_config)
        """
    def get_public_key(self, *, Id: str) -> GetPublicKeyResultTypeDef:
        """
        Gets a public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_public_key)
        """
    def get_public_key_config(self, *, Id: str) -> GetPublicKeyConfigResultTypeDef:
        """
        Gets a public key configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_public_key_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_public_key_config)
        """
    def get_realtime_log_config(
        self, *, Name: str = None, ARN: str = None
    ) -> GetRealtimeLogConfigResultTypeDef:
        """
        Gets a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_realtime_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_realtime_log_config)
        """
    def get_response_headers_policy(self, *, Id: str) -> GetResponseHeadersPolicyResultTypeDef:
        """
        Gets a response headers policy, including metadata (the policy's identifier and
        the date and time when the policy was last modified).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_response_headers_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_response_headers_policy)
        """
    def get_response_headers_policy_config(
        self, *, Id: str
    ) -> GetResponseHeadersPolicyConfigResultTypeDef:
        """
        Gets a response headers policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_response_headers_policy_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_response_headers_policy_config)
        """
    def get_streaming_distribution(self, *, Id: str) -> GetStreamingDistributionResultTypeDef:
        """
        Gets information about a specified RTMP distribution, including the distribution
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_streaming_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_streaming_distribution)
        """
    def get_streaming_distribution_config(
        self, *, Id: str
    ) -> GetStreamingDistributionConfigResultTypeDef:
        """
        Get the configuration information about a streaming distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.get_streaming_distribution_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#get_streaming_distribution_config)
        """
    def list_cache_policies(
        self, *, Type: CachePolicyTypeType = None, Marker: str = None, MaxItems: str = None
    ) -> ListCachePoliciesResultTypeDef:
        """
        Gets a list of cache policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_cache_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_cache_policies)
        """
    def list_cloud_front_origin_access_identities(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListCloudFrontOriginAccessIdentitiesResultTypeDef:
        """
        Lists origin access identities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_cloud_front_origin_access_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_cloud_front_origin_access_identities)
        """
    def list_conflicting_aliases(
        self, *, DistributionId: str, Alias: str, Marker: str = None, MaxItems: int = None
    ) -> ListConflictingAliasesResultTypeDef:
        """
        Gets a list of aliases (also called CNAMEs or alternate domain names) that
        conflict or overlap with the provided alias, and the associated CloudFront
        distributions and Amazon Web Services accounts for each conflicting alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_conflicting_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_conflicting_aliases)
        """
    def list_continuous_deployment_policies(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListContinuousDeploymentPoliciesResultTypeDef:
        """
        Gets a list of the continuous deployment policies in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_continuous_deployment_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_continuous_deployment_policies)
        """
    def list_distributions(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsResultTypeDef:
        """
        List CloudFront distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_distributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_distributions)
        """
    def list_distributions_by_cache_policy_id(
        self, *, CachePolicyId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByCachePolicyIdResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that's associated with the specified cache policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_cache_policy_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_distributions_by_cache_policy_id)
        """
    def list_distributions_by_key_group(
        self, *, KeyGroupId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByKeyGroupResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that references the specified key group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_key_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_distributions_by_key_group)
        """
    def list_distributions_by_origin_request_policy_id(
        self, *, OriginRequestPolicyId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByOriginRequestPolicyIdResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that's associated with the specified origin request policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_origin_request_policy_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_distributions_by_origin_request_policy_id)
        """
    def list_distributions_by_realtime_log_config(
        self,
        *,
        Marker: str = None,
        MaxItems: str = None,
        RealtimeLogConfigName: str = None,
        RealtimeLogConfigArn: str = None
    ) -> ListDistributionsByRealtimeLogConfigResultTypeDef:
        """
        Gets a list of distributions that have a cache behavior that's associated with
        the specified real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_realtime_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_distributions_by_realtime_log_config)
        """
    def list_distributions_by_response_headers_policy_id(
        self, *, ResponseHeadersPolicyId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByResponseHeadersPolicyIdResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that's associated with the specified response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_response_headers_policy_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_distributions_by_response_headers_policy_id)
        """
    def list_distributions_by_web_acl_id(
        self, *, WebACLId: str, Marker: str = None, MaxItems: str = None
    ) -> ListDistributionsByWebACLIdResultTypeDef:
        """
        List the distributions that are associated with a specified WAF web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_web_acl_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_distributions_by_web_acl_id)
        """
    def list_field_level_encryption_configs(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListFieldLevelEncryptionConfigsResultTypeDef:
        """
        List all field-level encryption configurations that have been created in
        CloudFront for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_field_level_encryption_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_field_level_encryption_configs)
        """
    def list_field_level_encryption_profiles(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListFieldLevelEncryptionProfilesResultTypeDef:
        """
        Request a list of field-level encryption profiles that have been created in
        CloudFront for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_field_level_encryption_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_field_level_encryption_profiles)
        """
    def list_functions(
        self, *, Marker: str = None, MaxItems: str = None, Stage: FunctionStageType = None
    ) -> ListFunctionsResultTypeDef:
        """
        Gets a list of all CloudFront functions in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_functions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_functions)
        """
    def list_invalidations(
        self, *, DistributionId: str, Marker: str = None, MaxItems: str = None
    ) -> ListInvalidationsResultTypeDef:
        """
        Lists invalidation batches.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_invalidations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_invalidations)
        """
    def list_key_groups(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListKeyGroupsResultTypeDef:
        """
        Gets a list of key groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_key_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_key_groups)
        """
    def list_origin_access_controls(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListOriginAccessControlsResultTypeDef:
        """
        Gets the list of CloudFront origin access controls in this Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_origin_access_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_origin_access_controls)
        """
    def list_origin_request_policies(
        self, *, Type: OriginRequestPolicyTypeType = None, Marker: str = None, MaxItems: str = None
    ) -> ListOriginRequestPoliciesResultTypeDef:
        """
        Gets a list of origin request policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_origin_request_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_origin_request_policies)
        """
    def list_public_keys(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListPublicKeysResultTypeDef:
        """
        List all public keys that have been added to CloudFront for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_public_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_public_keys)
        """
    def list_realtime_log_configs(
        self, *, MaxItems: str = None, Marker: str = None
    ) -> ListRealtimeLogConfigsResultTypeDef:
        """
        Gets a list of real-time log configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_realtime_log_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_realtime_log_configs)
        """
    def list_response_headers_policies(
        self,
        *,
        Type: ResponseHeadersPolicyTypeType = None,
        Marker: str = None,
        MaxItems: str = None
    ) -> ListResponseHeadersPoliciesResultTypeDef:
        """
        Gets a list of response headers policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_response_headers_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_response_headers_policies)
        """
    def list_streaming_distributions(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListStreamingDistributionsResultTypeDef:
        """
        List streaming distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_streaming_distributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_streaming_distributions)
        """
    def list_tags_for_resource(self, *, Resource: str) -> ListTagsForResourceResultTypeDef:
        """
        List tags for a CloudFront resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#list_tags_for_resource)
        """
    def publish_function(self, *, Name: str, IfMatch: str) -> PublishFunctionResultTypeDef:
        """
        Publishes a CloudFront function by copying the function code from the
        `DEVELOPMENT` stage to `LIVE`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.publish_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#publish_function)
        """
    def tag_resource(self, *, Resource: str, Tags: "TagsTypeDef") -> None:
        """
        Add tags to a CloudFront resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#tag_resource)
        """
    def test_function(
        self,
        *,
        Name: str,
        IfMatch: str,
        EventObject: Union[bytes, IO[bytes], StreamingBody],
        Stage: FunctionStageType = None
    ) -> TestFunctionResultTypeDef:
        """
        Tests a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.test_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#test_function)
        """
    def untag_resource(self, *, Resource: str, TagKeys: "TagKeysTypeDef") -> None:
        """
        Remove tags from a CloudFront resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#untag_resource)
        """
    def update_cache_policy(
        self, *, CachePolicyConfig: "CachePolicyConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdateCachePolicyResultTypeDef:
        """
        Updates a cache policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_cache_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_cache_policy)
        """
    def update_cloud_front_origin_access_identity(
        self,
        *,
        CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateCloudFrontOriginAccessIdentityResultTypeDef:
        """
        Update an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_cloud_front_origin_access_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_cloud_front_origin_access_identity)
        """
    def update_continuous_deployment_policy(
        self,
        *,
        ContinuousDeploymentPolicyConfig: "ContinuousDeploymentPolicyConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateContinuousDeploymentPolicyResultTypeDef:
        """
        Updates a continuous deployment policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_continuous_deployment_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_continuous_deployment_policy)
        """
    def update_distribution(
        self, *, DistributionConfig: "DistributionConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdateDistributionResultTypeDef:
        """
        Updates the configuration for a CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_distribution)
        """
    def update_distribution_with_staging_config(
        self, *, Id: str, StagingDistributionId: str = None, IfMatch: str = None
    ) -> UpdateDistributionWithStagingConfigResultTypeDef:
        """
        Copies the staging distribution's configuration to its corresponding primary
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_distribution_with_staging_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_distribution_with_staging_config)
        """
    def update_field_level_encryption_config(
        self,
        *,
        FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateFieldLevelEncryptionConfigResultTypeDef:
        """
        Update a field-level encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_field_level_encryption_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_field_level_encryption_config)
        """
    def update_field_level_encryption_profile(
        self,
        *,
        FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateFieldLevelEncryptionProfileResultTypeDef:
        """
        Update a field-level encryption profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_field_level_encryption_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_field_level_encryption_profile)
        """
    def update_function(
        self,
        *,
        Name: str,
        IfMatch: str,
        FunctionConfig: "FunctionConfigTypeDef",
        FunctionCode: Union[bytes, IO[bytes], StreamingBody]
    ) -> UpdateFunctionResultTypeDef:
        """
        Updates a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_function)
        """
    def update_key_group(
        self, *, KeyGroupConfig: "KeyGroupConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdateKeyGroupResultTypeDef:
        """
        Updates a key group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_key_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_key_group)
        """
    def update_origin_access_control(
        self,
        *,
        OriginAccessControlConfig: "OriginAccessControlConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateOriginAccessControlResultTypeDef:
        """
        Updates a CloudFront origin access control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_origin_access_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_origin_access_control)
        """
    def update_origin_request_policy(
        self,
        *,
        OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateOriginRequestPolicyResultTypeDef:
        """
        Updates an origin request policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_origin_request_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_origin_request_policy)
        """
    def update_public_key(
        self, *, PublicKeyConfig: "PublicKeyConfigTypeDef", Id: str, IfMatch: str = None
    ) -> UpdatePublicKeyResultTypeDef:
        """
        Update public key information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_public_key)
        """
    def update_realtime_log_config(
        self,
        *,
        EndPoints: List["EndPointTypeDef"] = None,
        Fields: List[str] = None,
        Name: str = None,
        ARN: str = None,
        SamplingRate: int = None
    ) -> UpdateRealtimeLogConfigResultTypeDef:
        """
        Updates a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_realtime_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_realtime_log_config)
        """
    def update_response_headers_policy(
        self,
        *,
        ResponseHeadersPolicyConfig: "ResponseHeadersPolicyConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateResponseHeadersPolicyResultTypeDef:
        """
        Updates a response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_response_headers_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_response_headers_policy)
        """
    def update_streaming_distribution(
        self,
        *,
        StreamingDistributionConfig: "StreamingDistributionConfigTypeDef",
        Id: str,
        IfMatch: str = None
    ) -> UpdateStreamingDistributionResultTypeDef:
        """
        Update a streaming distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Client.update_streaming_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/client.html#update_streaming_distribution)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_cloud_front_origin_access_identities"]
    ) -> ListCloudFrontOriginAccessIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators.html#listcloudfrontoriginaccessidentitiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_distributions"]
    ) -> ListDistributionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators.html#listdistributionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_invalidations"]
    ) -> ListInvalidationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators.html#listinvalidationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_distributions"]
    ) -> ListStreamingDistributionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators.html#liststreamingdistributionspaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["distribution_deployed"]
    ) -> DistributionDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#distributiondeployedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["invalidation_completed"]
    ) -> InvalidationCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#invalidationcompletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_distribution_deployed"]
    ) -> StreamingDistributionDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#streamingdistributiondeployedwaiter)
        """
