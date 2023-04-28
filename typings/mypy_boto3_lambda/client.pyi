"""
Type annotations for lambda service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lambda import LambdaClient

    client: LambdaClient = boto3.client("lambda")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ArchitectureType,
    EventSourcePositionType,
    FunctionUrlAuthTypeType,
    InvocationTypeType,
    InvokeModeType,
    LogTypeType,
    PackageTypeType,
    ResponseStreamingInvocationTypeType,
    RuntimeType,
    UpdateRuntimeOnType,
)
from .paginator import (
    ListAliasesPaginator,
    ListCodeSigningConfigsPaginator,
    ListEventSourceMappingsPaginator,
    ListFunctionEventInvokeConfigsPaginator,
    ListFunctionsByCodeSigningConfigPaginator,
    ListFunctionsPaginator,
    ListFunctionUrlConfigsPaginator,
    ListLayersPaginator,
    ListLayerVersionsPaginator,
    ListProvisionedConcurrencyConfigsPaginator,
    ListVersionsByFunctionPaginator,
)
from .type_defs import (
    AddLayerVersionPermissionResponseTypeDef,
    AddPermissionResponseTypeDef,
    AliasConfigurationResponseMetadataTypeDef,
    AliasRoutingConfigurationTypeDef,
    AllowedPublishersTypeDef,
    AmazonManagedKafkaEventSourceConfigTypeDef,
    CodeSigningPoliciesTypeDef,
    ConcurrencyResponseMetadataTypeDef,
    CorsTypeDef,
    CreateCodeSigningConfigResponseTypeDef,
    CreateFunctionUrlConfigResponseTypeDef,
    DeadLetterConfigTypeDef,
    DestinationConfigTypeDef,
    DocumentDBEventSourceConfigTypeDef,
    EnvironmentTypeDef,
    EphemeralStorageTypeDef,
    EventSourceMappingConfigurationResponseMetadataTypeDef,
    FileSystemConfigTypeDef,
    FilterCriteriaTypeDef,
    FunctionCodeTypeDef,
    FunctionConfigurationResponseMetadataTypeDef,
    FunctionEventInvokeConfigResponseMetadataTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetCodeSigningConfigResponseTypeDef,
    GetFunctionCodeSigningConfigResponseTypeDef,
    GetFunctionConcurrencyResponseTypeDef,
    GetFunctionResponseTypeDef,
    GetFunctionUrlConfigResponseTypeDef,
    GetLayerVersionPolicyResponseTypeDef,
    GetLayerVersionResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProvisionedConcurrencyConfigResponseTypeDef,
    GetRuntimeManagementConfigResponseTypeDef,
    ImageConfigTypeDef,
    InvocationResponseTypeDef,
    InvokeAsyncResponseTypeDef,
    InvokeWithResponseStreamResponseTypeDef,
    LayerVersionContentInputTypeDef,
    ListAliasesResponseTypeDef,
    ListCodeSigningConfigsResponseTypeDef,
    ListEventSourceMappingsResponseTypeDef,
    ListFunctionEventInvokeConfigsResponseTypeDef,
    ListFunctionsByCodeSigningConfigResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListFunctionUrlConfigsResponseTypeDef,
    ListLayersResponseTypeDef,
    ListLayerVersionsResponseTypeDef,
    ListProvisionedConcurrencyConfigsResponseTypeDef,
    ListTagsResponseTypeDef,
    ListVersionsByFunctionResponseTypeDef,
    PublishLayerVersionResponseTypeDef,
    PutFunctionCodeSigningConfigResponseTypeDef,
    PutProvisionedConcurrencyConfigResponseTypeDef,
    PutRuntimeManagementConfigResponseTypeDef,
    ScalingConfigTypeDef,
    SelfManagedEventSourceTypeDef,
    SelfManagedKafkaEventSourceConfigTypeDef,
    SnapStartTypeDef,
    SourceAccessConfigurationTypeDef,
    TracingConfigTypeDef,
    UpdateCodeSigningConfigResponseTypeDef,
    UpdateFunctionUrlConfigResponseTypeDef,
    VpcConfigTypeDef,
)
from .waiter import (
    FunctionActiveV2Waiter,
    FunctionActiveWaiter,
    FunctionExistsWaiter,
    FunctionUpdatedV2Waiter,
    FunctionUpdatedWaiter,
    PublishedVersionActiveWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LambdaClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    CodeSigningConfigNotFoundException: Type[BotocoreClientError]
    CodeStorageExceededException: Type[BotocoreClientError]
    CodeVerificationFailedException: Type[BotocoreClientError]
    EC2AccessDeniedException: Type[BotocoreClientError]
    EC2ThrottledException: Type[BotocoreClientError]
    EC2UnexpectedException: Type[BotocoreClientError]
    EFSIOException: Type[BotocoreClientError]
    EFSMountConnectivityException: Type[BotocoreClientError]
    EFSMountFailureException: Type[BotocoreClientError]
    EFSMountTimeoutException: Type[BotocoreClientError]
    ENILimitReachedException: Type[BotocoreClientError]
    InvalidCodeSignatureException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestContentException: Type[BotocoreClientError]
    InvalidRuntimeException: Type[BotocoreClientError]
    InvalidSecurityGroupIDException: Type[BotocoreClientError]
    InvalidSubnetIDException: Type[BotocoreClientError]
    InvalidZipFileException: Type[BotocoreClientError]
    KMSAccessDeniedException: Type[BotocoreClientError]
    KMSDisabledException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KMSNotFoundException: Type[BotocoreClientError]
    PolicyLengthExceededException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ProvisionedConcurrencyConfigNotFoundException: Type[BotocoreClientError]
    RequestTooLargeException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    SnapStartException: Type[BotocoreClientError]
    SnapStartNotReadyException: Type[BotocoreClientError]
    SnapStartTimeoutException: Type[BotocoreClientError]
    SubnetIPAddressLimitReachedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedMediaTypeException: Type[BotocoreClientError]

class LambdaClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LambdaClient exceptions.
        """
    def add_layer_version_permission(
        self,
        *,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        Action: str,
        Principal: str,
        OrganizationId: str = None,
        RevisionId: str = None
    ) -> AddLayerVersionPermissionResponseTypeDef:
        """
        Adds permissions to the resource-based policy of a version of an `Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.add_layer_version_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#add_layer_version_permission)
        """
    def add_permission(
        self,
        *,
        FunctionName: str,
        StatementId: str,
        Action: str,
        Principal: str,
        SourceArn: str = None,
        SourceAccount: str = None,
        EventSourceToken: str = None,
        Qualifier: str = None,
        RevisionId: str = None,
        PrincipalOrgID: str = None,
        FunctionUrlAuthType: FunctionUrlAuthTypeType = None
    ) -> AddPermissionResponseTypeDef:
        """
        Grants an Amazon Web Service, Amazon Web Services account, or Amazon Web
        Services organization permission to use a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.add_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#add_permission)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#close)
        """
    def create_alias(
        self,
        *,
        FunctionName: str,
        Name: str,
        FunctionVersion: str,
        Description: str = None,
        RoutingConfig: "AliasRoutingConfigurationTypeDef" = None
    ) -> AliasConfigurationResponseMetadataTypeDef:
        """
        Creates an `alias <https://docs.aws.amazon.com/lambda/latest/dg/configuration-
        aliases.html>`__ for a Lambda function version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create_alias)
        """
    def create_code_signing_config(
        self,
        *,
        AllowedPublishers: "AllowedPublishersTypeDef",
        Description: str = None,
        CodeSigningPolicies: "CodeSigningPoliciesTypeDef" = None
    ) -> CreateCodeSigningConfigResponseTypeDef:
        """
        Creates a code signing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.create_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create_code_signing_config)
        """
    def create_event_source_mapping(
        self,
        *,
        FunctionName: str,
        EventSourceArn: str = None,
        Enabled: bool = None,
        BatchSize: int = None,
        FilterCriteria: "FilterCriteriaTypeDef" = None,
        MaximumBatchingWindowInSeconds: int = None,
        ParallelizationFactor: int = None,
        StartingPosition: EventSourcePositionType = None,
        StartingPositionTimestamp: Union[datetime, str] = None,
        DestinationConfig: "DestinationConfigTypeDef" = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
        TumblingWindowInSeconds: int = None,
        Topics: List[str] = None,
        Queues: List[str] = None,
        SourceAccessConfigurations: List["SourceAccessConfigurationTypeDef"] = None,
        SelfManagedEventSource: "SelfManagedEventSourceTypeDef" = None,
        FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]] = None,
        AmazonManagedKafkaEventSourceConfig: "AmazonManagedKafkaEventSourceConfigTypeDef" = None,
        SelfManagedKafkaEventSourceConfig: "SelfManagedKafkaEventSourceConfigTypeDef" = None,
        ScalingConfig: "ScalingConfigTypeDef" = None,
        DocumentDBEventSourceConfig: "DocumentDBEventSourceConfigTypeDef" = None
    ) -> EventSourceMappingConfigurationResponseMetadataTypeDef:
        """
        Creates a mapping between an event source and an Lambda function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.create_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create_event_source_mapping)
        """
    def create_function(
        self,
        *,
        FunctionName: str,
        Role: str,
        Code: "FunctionCodeTypeDef",
        Runtime: RuntimeType = None,
        Handler: str = None,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        Publish: bool = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        PackageType: PackageTypeType = None,
        DeadLetterConfig: "DeadLetterConfigTypeDef" = None,
        Environment: "EnvironmentTypeDef" = None,
        KMSKeyArn: str = None,
        TracingConfig: "TracingConfigTypeDef" = None,
        Tags: Dict[str, str] = None,
        Layers: List[str] = None,
        FileSystemConfigs: List["FileSystemConfigTypeDef"] = None,
        ImageConfig: "ImageConfigTypeDef" = None,
        CodeSigningConfigArn: str = None,
        Architectures: List[ArchitectureType] = None,
        EphemeralStorage: "EphemeralStorageTypeDef" = None,
        SnapStart: "SnapStartTypeDef" = None
    ) -> FunctionConfigurationResponseMetadataTypeDef:
        """
        Creates a Lambda function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.create_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create_function)
        """
    def create_function_url_config(
        self,
        *,
        FunctionName: str,
        AuthType: FunctionUrlAuthTypeType,
        Qualifier: str = None,
        Cors: "CorsTypeDef" = None,
        InvokeMode: InvokeModeType = None
    ) -> CreateFunctionUrlConfigResponseTypeDef:
        """
        Creates a Lambda function URL with the specified configuration parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.create_function_url_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create_function_url_config)
        """
    def delete_alias(self, *, FunctionName: str, Name: str) -> None:
        """
        Deletes a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_alias)
        """
    def delete_code_signing_config(self, *, CodeSigningConfigArn: str) -> Dict[str, Any]:
        """
        Deletes the code signing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_code_signing_config)
        """
    def delete_event_source_mapping(
        self, *, UUID: str
    ) -> EventSourceMappingConfigurationResponseMetadataTypeDef:
        """
        Deletes an `event source mapping
        <https://docs.aws.amazon.com/lambda/latest/dg/intro-invocation-modes.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_event_source_mapping)
        """
    def delete_function(self, *, FunctionName: str, Qualifier: str = None) -> None:
        """
        Deletes a Lambda function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_function)
        """
    def delete_function_code_signing_config(self, *, FunctionName: str) -> None:
        """
        Removes the code signing configuration from the function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_function_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_function_code_signing_config)
        """
    def delete_function_concurrency(self, *, FunctionName: str) -> None:
        """
        Removes a concurrent execution limit from a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_function_concurrency)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_function_concurrency)
        """
    def delete_function_event_invoke_config(
        self, *, FunctionName: str, Qualifier: str = None
    ) -> None:
        """
        Deletes the configuration for asynchronous invocation for a function, version,
        or alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_function_event_invoke_config)
        """
    def delete_function_url_config(self, *, FunctionName: str, Qualifier: str = None) -> None:
        """
        Deletes a Lambda function URL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_function_url_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_function_url_config)
        """
    def delete_layer_version(self, *, LayerName: str, VersionNumber: int) -> None:
        """
        Deletes a version of an `Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_layer_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_layer_version)
        """
    def delete_provisioned_concurrency_config(self, *, FunctionName: str, Qualifier: str) -> None:
        """
        Deletes the provisioned concurrency configuration for a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.delete_provisioned_concurrency_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete_provisioned_concurrency_config)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#generate_presigned_url)
        """
    def get_account_settings(self) -> GetAccountSettingsResponseTypeDef:
        """
        Retrieves details about your account's `limits
        <https://docs.aws.amazon.com/lambda/latest/dg/limits.html>`__ and usage in an
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_account_settings)
        """
    def get_alias(
        self, *, FunctionName: str, Name: str
    ) -> AliasConfigurationResponseMetadataTypeDef:
        """
        Returns details about a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_alias)
        """
    def get_code_signing_config(
        self, *, CodeSigningConfigArn: str
    ) -> GetCodeSigningConfigResponseTypeDef:
        """
        Returns information about the specified code signing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_code_signing_config)
        """
    def get_event_source_mapping(
        self, *, UUID: str
    ) -> EventSourceMappingConfigurationResponseMetadataTypeDef:
        """
        Returns details about an event source mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_event_source_mapping)
        """
    def get_function(
        self, *, FunctionName: str, Qualifier: str = None
    ) -> GetFunctionResponseTypeDef:
        """
        Returns information about the function or function version, with a link to
        download the deployment package that's valid for 10 minutes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_function)
        """
    def get_function_code_signing_config(
        self, *, FunctionName: str
    ) -> GetFunctionCodeSigningConfigResponseTypeDef:
        """
        Returns the code signing configuration for the specified function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_function_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_function_code_signing_config)
        """
    def get_function_concurrency(
        self, *, FunctionName: str
    ) -> GetFunctionConcurrencyResponseTypeDef:
        """
        Returns details about the reserved concurrency configuration for a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_function_concurrency)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_function_concurrency)
        """
    def get_function_configuration(
        self, *, FunctionName: str, Qualifier: str = None
    ) -> FunctionConfigurationResponseMetadataTypeDef:
        """
        Returns the version-specific settings of a Lambda function or version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_function_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_function_configuration)
        """
    def get_function_event_invoke_config(
        self, *, FunctionName: str, Qualifier: str = None
    ) -> FunctionEventInvokeConfigResponseMetadataTypeDef:
        """
        Retrieves the configuration for asynchronous invocation for a function, version,
        or alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_function_event_invoke_config)
        """
    def get_function_url_config(
        self, *, FunctionName: str, Qualifier: str = None
    ) -> GetFunctionUrlConfigResponseTypeDef:
        """
        Returns details about a Lambda function URL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_function_url_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_function_url_config)
        """
    def get_layer_version(
        self, *, LayerName: str, VersionNumber: int
    ) -> GetLayerVersionResponseTypeDef:
        """
        Returns information about a version of an `Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__,
        with a link to download the layer archive that's valid for 10 minutes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_layer_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_layer_version)
        """
    def get_layer_version_by_arn(self, *, Arn: str) -> GetLayerVersionResponseTypeDef:
        """
        Returns information about a version of an `Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__,
        with a link to download the layer archive that's valid for 10 minutes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_layer_version_by_arn)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_layer_version_by_arn)
        """
    def get_layer_version_policy(
        self, *, LayerName: str, VersionNumber: int
    ) -> GetLayerVersionPolicyResponseTypeDef:
        """
        Returns the permission policy for a version of an `Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_layer_version_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_layer_version_policy)
        """
    def get_policy(self, *, FunctionName: str, Qualifier: str = None) -> GetPolicyResponseTypeDef:
        """
        Returns the `resource-based IAM policy
        <https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-
        based.html>`__ for a function, version, or alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_policy)
        """
    def get_provisioned_concurrency_config(
        self, *, FunctionName: str, Qualifier: str
    ) -> GetProvisionedConcurrencyConfigResponseTypeDef:
        """
        Retrieves the provisioned concurrency configuration for a function's alias or
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_provisioned_concurrency_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_provisioned_concurrency_config)
        """
    def get_runtime_management_config(
        self, *, FunctionName: str, Qualifier: str = None
    ) -> GetRuntimeManagementConfigResponseTypeDef:
        """
        Retrieves the runtime management configuration for a function's version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.get_runtime_management_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get_runtime_management_config)
        """
    def invoke(
        self,
        *,
        FunctionName: str,
        InvocationType: InvocationTypeType = None,
        LogType: LogTypeType = None,
        ClientContext: str = None,
        Payload: Union[bytes, IO[bytes], StreamingBody] = None,
        Qualifier: str = None
    ) -> InvocationResponseTypeDef:
        """
        Invokes a Lambda function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.invoke)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#invoke)
        """
    def invoke_async(
        self, *, FunctionName: str, InvokeArgs: Union[bytes, IO[bytes], StreamingBody]
    ) -> InvokeAsyncResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.invoke_async)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#invoke_async)
        """
    def invoke_with_response_stream(
        self,
        *,
        FunctionName: str,
        InvocationType: ResponseStreamingInvocationTypeType = None,
        LogType: LogTypeType = None,
        ClientContext: str = None,
        Qualifier: str = None,
        Payload: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> InvokeWithResponseStreamResponseTypeDef:
        """
        Configure your Lambda functions to stream response payloads back to clients.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.invoke_with_response_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#invoke_with_response_stream)
        """
    def list_aliases(
        self,
        *,
        FunctionName: str,
        FunctionVersion: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ListAliasesResponseTypeDef:
        """
        Returns a list of `aliases
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html>`__ for
        a Lambda function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_aliases)
        """
    def list_code_signing_configs(
        self, *, Marker: str = None, MaxItems: int = None
    ) -> ListCodeSigningConfigsResponseTypeDef:
        """
        Returns a list of `code signing configurations
        <https://docs.aws.amazon.com/lambda/latest/dg/configuring-codesigning.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_code_signing_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_code_signing_configs)
        """
    def list_event_source_mappings(
        self,
        *,
        EventSourceArn: str = None,
        FunctionName: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ListEventSourceMappingsResponseTypeDef:
        """
        Lists event source mappings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_event_source_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_event_source_mappings)
        """
    def list_function_event_invoke_configs(
        self, *, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListFunctionEventInvokeConfigsResponseTypeDef:
        """
        Retrieves a list of configurations for asynchronous invocation for a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_function_event_invoke_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_function_event_invoke_configs)
        """
    def list_function_url_configs(
        self, *, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListFunctionUrlConfigsResponseTypeDef:
        """
        Returns a list of Lambda function URLs for the specified function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_function_url_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_function_url_configs)
        """
    def list_functions(
        self,
        *,
        MasterRegion: str = None,
        FunctionVersion: Literal["ALL"] = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ListFunctionsResponseTypeDef:
        """
        Returns a list of Lambda functions, with the version-specific configuration of
        each.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_functions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_functions)
        """
    def list_functions_by_code_signing_config(
        self, *, CodeSigningConfigArn: str, Marker: str = None, MaxItems: int = None
    ) -> ListFunctionsByCodeSigningConfigResponseTypeDef:
        """
        List the functions that use the specified code signing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_functions_by_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_functions_by_code_signing_config)
        """
    def list_layer_versions(
        self,
        *,
        LayerName: str,
        CompatibleRuntime: RuntimeType = None,
        Marker: str = None,
        MaxItems: int = None,
        CompatibleArchitecture: ArchitectureType = None
    ) -> ListLayerVersionsResponseTypeDef:
        """
        Lists the versions of an `Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_layer_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_layer_versions)
        """
    def list_layers(
        self,
        *,
        CompatibleRuntime: RuntimeType = None,
        Marker: str = None,
        MaxItems: int = None,
        CompatibleArchitecture: ArchitectureType = None
    ) -> ListLayersResponseTypeDef:
        """
        Lists `Lambda layers <https://docs.aws.amazon.com/lambda/latest/dg/invocation-
        layers.html>`__ and shows information about the latest version of each.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_layers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_layers)
        """
    def list_provisioned_concurrency_configs(
        self, *, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListProvisionedConcurrencyConfigsResponseTypeDef:
        """
        Retrieves a list of provisioned concurrency configurations for a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_provisioned_concurrency_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_provisioned_concurrency_configs)
        """
    def list_tags(self, *, Resource: str) -> ListTagsResponseTypeDef:
        """
        Returns a function's `tags
        <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_tags)
        """
    def list_versions_by_function(
        self, *, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListVersionsByFunctionResponseTypeDef:
        """
        Returns a list of `versions
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__, with
        the version-specific configuration of each.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.list_versions_by_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list_versions_by_function)
        """
    def publish_layer_version(
        self,
        *,
        LayerName: str,
        Content: "LayerVersionContentInputTypeDef",
        Description: str = None,
        CompatibleRuntimes: List[RuntimeType] = None,
        LicenseInfo: str = None,
        CompatibleArchitectures: List[ArchitectureType] = None
    ) -> PublishLayerVersionResponseTypeDef:
        """
        Creates an `Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ from
        a ZIP archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.publish_layer_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#publish_layer_version)
        """
    def publish_version(
        self,
        *,
        FunctionName: str,
        CodeSha256: str = None,
        Description: str = None,
        RevisionId: str = None
    ) -> FunctionConfigurationResponseMetadataTypeDef:
        """
        Creates a `version <https://docs.aws.amazon.com/lambda/latest/dg/versioning-
        aliases.html>`__ from the current code and configuration of a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.publish_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#publish_version)
        """
    def put_function_code_signing_config(
        self, *, CodeSigningConfigArn: str, FunctionName: str
    ) -> PutFunctionCodeSigningConfigResponseTypeDef:
        """
        Update the code signing configuration for the function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.put_function_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put_function_code_signing_config)
        """
    def put_function_concurrency(
        self, *, FunctionName: str, ReservedConcurrentExecutions: int
    ) -> ConcurrencyResponseMetadataTypeDef:
        """
        Sets the maximum number of simultaneous executions for a function, and reserves
        capacity for that concurrency level.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.put_function_concurrency)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put_function_concurrency)
        """
    def put_function_event_invoke_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: "DestinationConfigTypeDef" = None
    ) -> FunctionEventInvokeConfigResponseMetadataTypeDef:
        """
        Configures options for `asynchronous invocation
        <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html>`__ on a
        function, version, or alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.put_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put_function_event_invoke_config)
        """
    def put_provisioned_concurrency_config(
        self, *, FunctionName: str, Qualifier: str, ProvisionedConcurrentExecutions: int
    ) -> PutProvisionedConcurrencyConfigResponseTypeDef:
        """
        Adds a provisioned concurrency configuration to a function's alias or version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.put_provisioned_concurrency_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put_provisioned_concurrency_config)
        """
    def put_runtime_management_config(
        self,
        *,
        FunctionName: str,
        UpdateRuntimeOn: UpdateRuntimeOnType,
        Qualifier: str = None,
        RuntimeVersionArn: str = None
    ) -> PutRuntimeManagementConfigResponseTypeDef:
        """
        Sets the runtime management configuration for a function's version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.put_runtime_management_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put_runtime_management_config)
        """
    def remove_layer_version_permission(
        self, *, LayerName: str, VersionNumber: int, StatementId: str, RevisionId: str = None
    ) -> None:
        """
        Removes a statement from the permissions policy for a version of an `Lambda
        layer <https://docs.aws.amazon.com/lambda/latest/dg/configuration-
        layers.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.remove_layer_version_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#remove_layer_version_permission)
        """
    def remove_permission(
        self, *, FunctionName: str, StatementId: str, Qualifier: str = None, RevisionId: str = None
    ) -> None:
        """
        Revokes function-use permission from an Amazon Web Service or another Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#remove_permission)
        """
    def tag_resource(self, *, Resource: str, Tags: Dict[str, str]) -> None:
        """
        Adds `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ to a
        function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#tag_resource)
        """
    def untag_resource(self, *, Resource: str, TagKeys: List[str]) -> None:
        """
        Removes `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__
        from a function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#untag_resource)
        """
    def update_alias(
        self,
        *,
        FunctionName: str,
        Name: str,
        FunctionVersion: str = None,
        Description: str = None,
        RoutingConfig: "AliasRoutingConfigurationTypeDef" = None,
        RevisionId: str = None
    ) -> AliasConfigurationResponseMetadataTypeDef:
        """
        Updates the configuration of a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.update_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update_alias)
        """
    def update_code_signing_config(
        self,
        *,
        CodeSigningConfigArn: str,
        Description: str = None,
        AllowedPublishers: "AllowedPublishersTypeDef" = None,
        CodeSigningPolicies: "CodeSigningPoliciesTypeDef" = None
    ) -> UpdateCodeSigningConfigResponseTypeDef:
        """
        Update the code signing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.update_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update_code_signing_config)
        """
    def update_event_source_mapping(
        self,
        *,
        UUID: str,
        FunctionName: str = None,
        Enabled: bool = None,
        BatchSize: int = None,
        FilterCriteria: "FilterCriteriaTypeDef" = None,
        MaximumBatchingWindowInSeconds: int = None,
        DestinationConfig: "DestinationConfigTypeDef" = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
        ParallelizationFactor: int = None,
        SourceAccessConfigurations: List["SourceAccessConfigurationTypeDef"] = None,
        TumblingWindowInSeconds: int = None,
        FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]] = None,
        ScalingConfig: "ScalingConfigTypeDef" = None,
        DocumentDBEventSourceConfig: "DocumentDBEventSourceConfigTypeDef" = None
    ) -> EventSourceMappingConfigurationResponseMetadataTypeDef:
        """
        Updates an event source mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.update_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update_event_source_mapping)
        """
    def update_function_code(
        self,
        *,
        FunctionName: str,
        ZipFile: Union[bytes, IO[bytes], StreamingBody] = None,
        S3Bucket: str = None,
        S3Key: str = None,
        S3ObjectVersion: str = None,
        ImageUri: str = None,
        Publish: bool = None,
        DryRun: bool = None,
        RevisionId: str = None,
        Architectures: List[ArchitectureType] = None
    ) -> FunctionConfigurationResponseMetadataTypeDef:
        """
        Updates a Lambda function's code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.update_function_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update_function_code)
        """
    def update_function_configuration(
        self,
        *,
        FunctionName: str,
        Role: str = None,
        Handler: str = None,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Environment: "EnvironmentTypeDef" = None,
        Runtime: RuntimeType = None,
        DeadLetterConfig: "DeadLetterConfigTypeDef" = None,
        KMSKeyArn: str = None,
        TracingConfig: "TracingConfigTypeDef" = None,
        RevisionId: str = None,
        Layers: List[str] = None,
        FileSystemConfigs: List["FileSystemConfigTypeDef"] = None,
        ImageConfig: "ImageConfigTypeDef" = None,
        EphemeralStorage: "EphemeralStorageTypeDef" = None,
        SnapStart: "SnapStartTypeDef" = None
    ) -> FunctionConfigurationResponseMetadataTypeDef:
        """
        Modify the version-specific settings of a Lambda function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.update_function_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update_function_configuration)
        """
    def update_function_event_invoke_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: "DestinationConfigTypeDef" = None
    ) -> FunctionEventInvokeConfigResponseMetadataTypeDef:
        """
        Updates the configuration for asynchronous invocation for a function, version,
        or alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.update_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update_function_event_invoke_config)
        """
    def update_function_url_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str = None,
        AuthType: FunctionUrlAuthTypeType = None,
        Cors: "CorsTypeDef" = None,
        InvokeMode: InvokeModeType = None
    ) -> UpdateFunctionUrlConfigResponseTypeDef:
        """
        Updates the configuration for a Lambda function URL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Client.update_function_url_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update_function_url_config)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listaliasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_signing_configs"]
    ) -> ListCodeSigningConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListCodeSigningConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listcodesigningconfigspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_source_mappings"]
    ) -> ListEventSourceMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listeventsourcemappingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_function_event_invoke_configs"]
    ) -> ListFunctionEventInvokeConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctioneventinvokeconfigspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_function_url_configs"]
    ) -> ListFunctionUrlConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListFunctionUrlConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionurlconfigspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_functions"]) -> ListFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListFunctions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_functions_by_code_signing_config"]
    ) -> ListFunctionsByCodeSigningConfigPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListFunctionsByCodeSigningConfig)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionsbycodesigningconfigpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_layer_versions"]
    ) -> ListLayerVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_layers"]) -> ListLayersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListLayers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioned_concurrency_configs"]
    ) -> ListProvisionedConcurrencyConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listprovisionedconcurrencyconfigspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_versions_by_function"]
    ) -> ListVersionsByFunctionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listversionsbyfunctionpaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["function_active"]) -> FunctionActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Waiter.FunctionActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionactivewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["function_active_v2"]) -> FunctionActiveV2Waiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Waiter.FunctionActiveV2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionactivev2waiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["function_exists"]) -> FunctionExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Waiter.FunctionExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["function_updated"]) -> FunctionUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionupdatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["function_updated_v2"]) -> FunctionUpdatedV2Waiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Waiter.FunctionUpdatedV2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionupdatedv2waiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["published_version_active"]
    ) -> PublishedVersionActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lambda.html#Lambda.Waiter.PublishedVersionActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#publishedversionactivewaiter)
        """
