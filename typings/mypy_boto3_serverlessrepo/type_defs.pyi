"""
Type annotations for serverlessrepo service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/type_defs.html)

Usage::

    ```python
    from mypy_boto3_serverlessrepo.type_defs import ApplicationDependencySummaryTypeDef

    data: ApplicationDependencySummaryTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import CapabilityType, StatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApplicationDependencySummaryTypeDef",
    "ApplicationPolicyStatementTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateApplicationVersionRequestRequestTypeDef",
    "CreateApplicationVersionResponseTypeDef",
    "CreateCloudFormationChangeSetRequestRequestTypeDef",
    "CreateCloudFormationChangeSetResponseTypeDef",
    "CreateCloudFormationTemplateRequestRequestTypeDef",
    "CreateCloudFormationTemplateResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "GetApplicationPolicyRequestRequestTypeDef",
    "GetApplicationPolicyResponseTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetCloudFormationTemplateRequestRequestTypeDef",
    "GetCloudFormationTemplateResponseTypeDef",
    "ListApplicationDependenciesRequestRequestTypeDef",
    "ListApplicationDependenciesResponseTypeDef",
    "ListApplicationVersionsRequestRequestTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterDefinitionTypeDef",
    "ParameterValueTypeDef",
    "PutApplicationPolicyRequestRequestTypeDef",
    "PutApplicationPolicyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "TagTypeDef",
    "UnshareApplicationRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "VersionSummaryTypeDef",
    "VersionTypeDef",
)

ApplicationDependencySummaryTypeDef = TypedDict(
    "ApplicationDependencySummaryTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": str,
    },
)

_RequiredApplicationPolicyStatementTypeDef = TypedDict(
    "_RequiredApplicationPolicyStatementTypeDef",
    {
        "Actions": List[str],
        "Principals": List[str],
    },
)
_OptionalApplicationPolicyStatementTypeDef = TypedDict(
    "_OptionalApplicationPolicyStatementTypeDef",
    {
        "PrincipalOrgIDs": List[str],
        "StatementId": str,
    },
    total=False,
)

class ApplicationPolicyStatementTypeDef(
    _RequiredApplicationPolicyStatementTypeDef, _OptionalApplicationPolicyStatementTypeDef
):
    pass

_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "Description": str,
        "Name": str,
    },
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "CreationTime": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "SpdxLicenseId": str,
    },
    total=False,
)

class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "Author": str,
        "Description": str,
        "Name": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "HomePageUrl": str,
        "Labels": List[str],
        "LicenseBody": str,
        "LicenseUrl": str,
        "ReadmeBody": str,
        "ReadmeUrl": str,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "SpdxLicenseId": str,
        "TemplateBody": str,
        "TemplateUrl": str,
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": "VersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": str,
    },
)
_OptionalCreateApplicationVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationVersionRequestRequestTypeDef",
    {
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateBody": str,
        "TemplateUrl": str,
    },
    total=False,
)

class CreateApplicationVersionRequestRequestTypeDef(
    _RequiredCreateApplicationVersionRequestRequestTypeDef,
    _OptionalCreateApplicationVersionRequestRequestTypeDef,
):
    pass

CreateApplicationVersionResponseTypeDef = TypedDict(
    "CreateApplicationVersionResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List["ParameterDefinitionTypeDef"],
        "RequiredCapabilities": List[CapabilityType],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCloudFormationChangeSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCloudFormationChangeSetRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "StackName": str,
    },
)
_OptionalCreateCloudFormationChangeSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCloudFormationChangeSetRequestRequestTypeDef",
    {
        "Capabilities": List[str],
        "ChangeSetName": str,
        "ClientToken": str,
        "Description": str,
        "NotificationArns": List[str],
        "ParameterOverrides": List["ParameterValueTypeDef"],
        "ResourceTypes": List[str],
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "SemanticVersion": str,
        "Tags": List["TagTypeDef"],
        "TemplateId": str,
    },
    total=False,
)

class CreateCloudFormationChangeSetRequestRequestTypeDef(
    _RequiredCreateCloudFormationChangeSetRequestRequestTypeDef,
    _OptionalCreateCloudFormationChangeSetRequestRequestTypeDef,
):
    pass

CreateCloudFormationChangeSetResponseTypeDef = TypedDict(
    "CreateCloudFormationChangeSetResponseTypeDef",
    {
        "ApplicationId": str,
        "ChangeSetId": str,
        "SemanticVersion": str,
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCloudFormationTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCloudFormationTemplateRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalCreateCloudFormationTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCloudFormationTemplateRequestRequestTypeDef",
    {
        "SemanticVersion": str,
    },
    total=False,
)

class CreateCloudFormationTemplateRequestRequestTypeDef(
    _RequiredCreateCloudFormationTemplateRequestRequestTypeDef,
    _OptionalCreateCloudFormationTemplateRequestRequestTypeDef,
):
    pass

CreateCloudFormationTemplateResponseTypeDef = TypedDict(
    "CreateCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": StatusType,
        "TemplateId": str,
        "TemplateUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationPolicyRequestRequestTypeDef = TypedDict(
    "GetApplicationPolicyRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationPolicyResponseTypeDef = TypedDict(
    "GetApplicationPolicyResponseTypeDef",
    {
        "Statements": List["ApplicationPolicyStatementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredGetApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalGetApplicationRequestRequestTypeDef",
    {
        "SemanticVersion": str,
    },
    total=False,
)

class GetApplicationRequestRequestTypeDef(
    _RequiredGetApplicationRequestRequestTypeDef, _OptionalGetApplicationRequestRequestTypeDef
):
    pass

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": "VersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFormationTemplateRequestRequestTypeDef = TypedDict(
    "GetCloudFormationTemplateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "TemplateId": str,
    },
)

GetCloudFormationTemplateResponseTypeDef = TypedDict(
    "GetCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": StatusType,
        "TemplateId": str,
        "TemplateUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationDependenciesRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationDependenciesRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListApplicationDependenciesRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationDependenciesRequestRequestTypeDef",
    {
        "MaxItems": int,
        "NextToken": str,
        "SemanticVersion": str,
    },
    total=False,
)

class ListApplicationDependenciesRequestRequestTypeDef(
    _RequiredListApplicationDependenciesRequestRequestTypeDef,
    _OptionalListApplicationDependenciesRequestRequestTypeDef,
):
    pass

ListApplicationDependenciesResponseTypeDef = TypedDict(
    "ListApplicationDependenciesResponseTypeDef",
    {
        "Dependencies": List["ApplicationDependencySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListApplicationVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationVersionsRequestRequestTypeDef",
    {
        "MaxItems": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationVersionsRequestRequestTypeDef(
    _RequiredListApplicationVersionsRequestRequestTypeDef,
    _OptionalListApplicationVersionsRequestRequestTypeDef,
):
    pass

ListApplicationVersionsResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxItems": int,
        "NextToken": str,
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "Applications": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredParameterDefinitionTypeDef = TypedDict(
    "_RequiredParameterDefinitionTypeDef",
    {
        "Name": str,
        "ReferencedByResources": List[str],
    },
)
_OptionalParameterDefinitionTypeDef = TypedDict(
    "_OptionalParameterDefinitionTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "NoEcho": bool,
        "Type": str,
    },
    total=False,
)

class ParameterDefinitionTypeDef(
    _RequiredParameterDefinitionTypeDef, _OptionalParameterDefinitionTypeDef
):
    pass

ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

PutApplicationPolicyRequestRequestTypeDef = TypedDict(
    "PutApplicationPolicyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Statements": List["ApplicationPolicyStatementTypeDef"],
    },
)

PutApplicationPolicyResponseTypeDef = TypedDict(
    "PutApplicationPolicyResponseTypeDef",
    {
        "Statements": List["ApplicationPolicyStatementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {
        "MonitoringTimeInMinutes": int,
        "RollbackTriggers": List["RollbackTriggerTypeDef"],
    },
    total=False,
)

RollbackTriggerTypeDef = TypedDict(
    "RollbackTriggerTypeDef",
    {
        "Arn": str,
        "Type": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UnshareApplicationRequestRequestTypeDef = TypedDict(
    "UnshareApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "OrganizationId": str,
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "Author": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "ReadmeBody": str,
        "ReadmeUrl": str,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": "VersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVersionSummaryTypeDef = TypedDict(
    "_RequiredVersionSummaryTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "SemanticVersion": str,
    },
)
_OptionalVersionSummaryTypeDef = TypedDict(
    "_OptionalVersionSummaryTypeDef",
    {
        "SourceCodeUrl": str,
    },
    total=False,
)

class VersionSummaryTypeDef(_RequiredVersionSummaryTypeDef, _OptionalVersionSummaryTypeDef):
    pass

_RequiredVersionTypeDef = TypedDict(
    "_RequiredVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List["ParameterDefinitionTypeDef"],
        "RequiredCapabilities": List[CapabilityType],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "TemplateUrl": str,
    },
)
_OptionalVersionTypeDef = TypedDict(
    "_OptionalVersionTypeDef",
    {
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
    },
    total=False,
)

class VersionTypeDef(_RequiredVersionTypeDef, _OptionalVersionTypeDef):
    pass
