"""
Type annotations for accessanalyzer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/literals.html)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.literals import AccessCheckPolicyTypeType

    data: AccessCheckPolicyTypeType = "IDENTITY_POLICY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessCheckPolicyTypeType",
    "AccessPreviewStatusReasonCodeType",
    "AccessPreviewStatusType",
    "AclPermissionType",
    "AnalyzerStatusType",
    "CheckAccessNotGrantedResultType",
    "CheckNoNewAccessResultType",
    "FindingChangeTypeType",
    "FindingSourceTypeType",
    "FindingStatusType",
    "FindingStatusUpdateType",
    "FindingTypeType",
    "GetFindingV2PaginatorName",
    "JobErrorCodeType",
    "JobStatusType",
    "KmsGrantOperationType",
    "ListAccessPreviewFindingsPaginatorName",
    "ListAccessPreviewsPaginatorName",
    "ListAnalyzedResourcesPaginatorName",
    "ListAnalyzersPaginatorName",
    "ListArchiveRulesPaginatorName",
    "ListFindingsPaginatorName",
    "ListFindingsV2PaginatorName",
    "ListPolicyGenerationsPaginatorName",
    "LocaleType",
    "OrderByType",
    "PolicyTypeType",
    "ReasonCodeType",
    "ResourceTypeType",
    "TypeType",
    "ValidatePolicyFindingTypeType",
    "ValidatePolicyPaginatorName",
    "ValidatePolicyResourceTypeType",
)

AccessCheckPolicyTypeType = Literal["IDENTITY_POLICY", "RESOURCE_POLICY"]
AccessPreviewStatusReasonCodeType = Literal["INTERNAL_ERROR", "INVALID_CONFIGURATION"]
AccessPreviewStatusType = Literal["COMPLETED", "CREATING", "FAILED"]
AclPermissionType = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
AnalyzerStatusType = Literal["ACTIVE", "CREATING", "DISABLED", "FAILED"]
CheckAccessNotGrantedResultType = Literal["FAIL", "PASS"]
CheckNoNewAccessResultType = Literal["FAIL", "PASS"]
FindingChangeTypeType = Literal["CHANGED", "NEW", "UNCHANGED"]
FindingSourceTypeType = Literal[
    "BUCKET_ACL", "POLICY", "S3_ACCESS_POINT", "S3_ACCESS_POINT_ACCOUNT"
]
FindingStatusType = Literal["ACTIVE", "ARCHIVED", "RESOLVED"]
FindingStatusUpdateType = Literal["ACTIVE", "ARCHIVED"]
FindingTypeType = Literal[
    "ExternalAccess",
    "UnusedIAMRole",
    "UnusedIAMUserAccessKey",
    "UnusedIAMUserPassword",
    "UnusedPermission",
]
GetFindingV2PaginatorName = Literal["get_finding_v2"]
JobErrorCodeType = Literal[
    "AUTHORIZATION_ERROR",
    "RESOURCE_NOT_FOUND_ERROR",
    "SERVICE_ERROR",
    "SERVICE_QUOTA_EXCEEDED_ERROR",
]
JobStatusType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
KmsGrantOperationType = Literal[
    "CreateGrant",
    "Decrypt",
    "DescribeKey",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GetPublicKey",
    "ReEncryptFrom",
    "ReEncryptTo",
    "RetireGrant",
    "Sign",
    "Verify",
]
ListAccessPreviewFindingsPaginatorName = Literal["list_access_preview_findings"]
ListAccessPreviewsPaginatorName = Literal["list_access_previews"]
ListAnalyzedResourcesPaginatorName = Literal["list_analyzed_resources"]
ListAnalyzersPaginatorName = Literal["list_analyzers"]
ListArchiveRulesPaginatorName = Literal["list_archive_rules"]
ListFindingsPaginatorName = Literal["list_findings"]
ListFindingsV2PaginatorName = Literal["list_findings_v2"]
ListPolicyGenerationsPaginatorName = Literal["list_policy_generations"]
LocaleType = Literal["DE", "EN", "ES", "FR", "IT", "JA", "KO", "PT_BR", "ZH_CN", "ZH_TW"]
OrderByType = Literal["ASC", "DESC"]
PolicyTypeType = Literal["IDENTITY_POLICY", "RESOURCE_POLICY", "SERVICE_CONTROL_POLICY"]
ReasonCodeType = Literal[
    "AWS_SERVICE_ACCESS_DISABLED",
    "DELEGATED_ADMINISTRATOR_DEREGISTERED",
    "ORGANIZATION_DELETED",
    "SERVICE_LINKED_ROLE_CREATION_FAILED",
]
ResourceTypeType = Literal[
    "AWS::EC2::Snapshot",
    "AWS::ECR::Repository",
    "AWS::EFS::FileSystem",
    "AWS::IAM::Role",
    "AWS::KMS::Key",
    "AWS::Lambda::Function",
    "AWS::Lambda::LayerVersion",
    "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::DBSnapshot",
    "AWS::S3::Bucket",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SecretsManager::Secret",
]
TypeType = Literal["ACCOUNT", "ACCOUNT_UNUSED_ACCESS", "ORGANIZATION", "ORGANIZATION_UNUSED_ACCESS"]
ValidatePolicyFindingTypeType = Literal["ERROR", "SECURITY_WARNING", "SUGGESTION", "WARNING"]
ValidatePolicyPaginatorName = Literal["validate_policy"]
ValidatePolicyResourceTypeType = Literal[
    "AWS::IAM::AssumeRolePolicyDocument",
    "AWS::S3::AccessPoint",
    "AWS::S3::Bucket",
    "AWS::S3::MultiRegionAccessPoint",
    "AWS::S3ObjectLambda::AccessPoint",
]
