"""
Type annotations for lambda service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/literals.html)

Usage::

    ```python
    from mypy_boto3_lambda.literals import ArchitectureType

    data: ArchitectureType = "arm64"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ArchitectureType",
    "CodeSigningPolicyType",
    "EndPointTypeType",
    "EventSourcePositionType",
    "FunctionActiveV2WaiterName",
    "FunctionActiveWaiterName",
    "FunctionExistsWaiterName",
    "FunctionResponseTypeType",
    "FunctionUpdatedV2WaiterName",
    "FunctionUpdatedWaiterName",
    "FunctionUrlAuthTypeType",
    "FunctionVersionType",
    "InvocationTypeType",
    "LastUpdateStatusReasonCodeType",
    "LastUpdateStatusType",
    "ListAliasesPaginatorName",
    "ListCodeSigningConfigsPaginatorName",
    "ListEventSourceMappingsPaginatorName",
    "ListFunctionEventInvokeConfigsPaginatorName",
    "ListFunctionUrlConfigsPaginatorName",
    "ListFunctionsByCodeSigningConfigPaginatorName",
    "ListFunctionsPaginatorName",
    "ListLayerVersionsPaginatorName",
    "ListLayersPaginatorName",
    "ListProvisionedConcurrencyConfigsPaginatorName",
    "ListVersionsByFunctionPaginatorName",
    "LogTypeType",
    "PackageTypeType",
    "ProvisionedConcurrencyStatusEnumType",
    "PublishedVersionActiveWaiterName",
    "RuntimeType",
    "SnapStartApplyOnType",
    "SnapStartOptimizationStatusType",
    "SourceAccessTypeType",
    "StateReasonCodeType",
    "StateType",
    "TracingModeType",
)

ArchitectureType = Literal["arm64", "x86_64"]
CodeSigningPolicyType = Literal["Enforce", "Warn"]
EndPointTypeType = Literal["KAFKA_BOOTSTRAP_SERVERS"]
EventSourcePositionType = Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"]
FunctionActiveV2WaiterName = Literal["function_active_v2"]
FunctionActiveWaiterName = Literal["function_active"]
FunctionExistsWaiterName = Literal["function_exists"]
FunctionResponseTypeType = Literal["ReportBatchItemFailures"]
FunctionUpdatedV2WaiterName = Literal["function_updated_v2"]
FunctionUpdatedWaiterName = Literal["function_updated"]
FunctionUrlAuthTypeType = Literal["AWS_IAM", "NONE"]
FunctionVersionType = Literal["ALL"]
InvocationTypeType = Literal["DryRun", "Event", "RequestResponse"]
LastUpdateStatusReasonCodeType = Literal[
    "DisabledKMSKey",
    "EFSIOError",
    "EFSMountConnectivityError",
    "EFSMountFailure",
    "EFSMountTimeout",
    "EniLimitExceeded",
    "FunctionError",
    "ImageAccessDenied",
    "ImageDeleted",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidConfiguration",
    "InvalidImage",
    "InvalidRuntime",
    "InvalidSecurityGroup",
    "InvalidStateKMSKey",
    "InvalidSubnet",
    "InvalidZipFileException",
    "KMSKeyAccessDenied",
    "KMSKeyNotFound",
    "SubnetOutOfIPAddresses",
]
LastUpdateStatusType = Literal["Failed", "InProgress", "Successful"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListCodeSigningConfigsPaginatorName = Literal["list_code_signing_configs"]
ListEventSourceMappingsPaginatorName = Literal["list_event_source_mappings"]
ListFunctionEventInvokeConfigsPaginatorName = Literal["list_function_event_invoke_configs"]
ListFunctionUrlConfigsPaginatorName = Literal["list_function_url_configs"]
ListFunctionsByCodeSigningConfigPaginatorName = Literal["list_functions_by_code_signing_config"]
ListFunctionsPaginatorName = Literal["list_functions"]
ListLayerVersionsPaginatorName = Literal["list_layer_versions"]
ListLayersPaginatorName = Literal["list_layers"]
ListProvisionedConcurrencyConfigsPaginatorName = Literal["list_provisioned_concurrency_configs"]
ListVersionsByFunctionPaginatorName = Literal["list_versions_by_function"]
LogTypeType = Literal["None", "Tail"]
PackageTypeType = Literal["Image", "Zip"]
ProvisionedConcurrencyStatusEnumType = Literal["FAILED", "IN_PROGRESS", "READY"]
PublishedVersionActiveWaiterName = Literal["published_version_active"]
RuntimeType = Literal[
    "dotnet6",
    "dotnetcore1.0",
    "dotnetcore2.0",
    "dotnetcore2.1",
    "dotnetcore3.1",
    "go1.x",
    "java11",
    "java8",
    "java8.al2",
    "nodejs",
    "nodejs10.x",
    "nodejs12.x",
    "nodejs14.x",
    "nodejs16.x",
    "nodejs18.x",
    "nodejs4.3",
    "nodejs4.3-edge",
    "nodejs6.10",
    "nodejs8.10",
    "provided",
    "provided.al2",
    "python2.7",
    "python3.6",
    "python3.7",
    "python3.8",
    "python3.9",
    "ruby2.5",
    "ruby2.7",
]
SnapStartApplyOnType = Literal["None", "PublishedVersions"]
SnapStartOptimizationStatusType = Literal["Off", "On"]
SourceAccessTypeType = Literal[
    "BASIC_AUTH",
    "CLIENT_CERTIFICATE_TLS_AUTH",
    "SASL_SCRAM_256_AUTH",
    "SASL_SCRAM_512_AUTH",
    "SERVER_ROOT_CA_CERTIFICATE",
    "VIRTUAL_HOST",
    "VPC_SECURITY_GROUP",
    "VPC_SUBNET",
]
StateReasonCodeType = Literal[
    "Creating",
    "DisabledKMSKey",
    "EFSIOError",
    "EFSMountConnectivityError",
    "EFSMountFailure",
    "EFSMountTimeout",
    "EniLimitExceeded",
    "FunctionError",
    "Idle",
    "ImageAccessDenied",
    "ImageDeleted",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidConfiguration",
    "InvalidImage",
    "InvalidRuntime",
    "InvalidSecurityGroup",
    "InvalidStateKMSKey",
    "InvalidSubnet",
    "InvalidZipFileException",
    "KMSKeyAccessDenied",
    "KMSKeyNotFound",
    "Restoring",
    "SubnetOutOfIPAddresses",
]
StateType = Literal["Active", "Failed", "Inactive", "Pending"]
TracingModeType = Literal["Active", "PassThrough"]
