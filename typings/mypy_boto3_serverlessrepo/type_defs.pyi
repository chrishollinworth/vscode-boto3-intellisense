"""
Main interface for serverlessrepo service type definitions.

Usage::

    ```python
    from mypy_boto3_serverlessrepo.type_defs import ApplicationDependencySummaryTypeDef

    data: ApplicationDependencySummaryTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationDependencySummaryTypeDef",
    "ApplicationPolicyStatementTypeDef",
    "ApplicationSummaryTypeDef",
    "ParameterDefinitionTypeDef",
    "RollbackTriggerTypeDef",
    "VersionSummaryTypeDef",
    "VersionTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateApplicationVersionResponseTypeDef",
    "CreateCloudFormationChangeSetResponseTypeDef",
    "CreateCloudFormationTemplateResponseTypeDef",
    "GetApplicationPolicyResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "GetCloudFormationTemplateResponseTypeDef",
    "ListApplicationDependenciesResponseTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterValueTypeDef",
    "PutApplicationPolicyResponseTypeDef",
    "RollbackConfigurationTypeDef",
    "TagTypeDef",
    "UpdateApplicationResponseTypeDef",
)

ApplicationDependencySummaryTypeDef = TypedDict(
    "ApplicationDependencySummaryTypeDef", {"ApplicationId": str, "SemanticVersion": str}
)

_RequiredApplicationPolicyStatementTypeDef = TypedDict(
    "_RequiredApplicationPolicyStatementTypeDef", {"Actions": List[str], "Principals": List[str]}
)
_OptionalApplicationPolicyStatementTypeDef = TypedDict(
    "_OptionalApplicationPolicyStatementTypeDef",
    {"PrincipalOrgIDs": List[str], "StatementId": str},
    total=False,
)


class ApplicationPolicyStatementTypeDef(
    _RequiredApplicationPolicyStatementTypeDef, _OptionalApplicationPolicyStatementTypeDef
):
    pass


_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {"ApplicationId": str, "Author": str, "Description": str, "Name": str},
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {"CreationTime": str, "HomePageUrl": str, "Labels": List[str], "SpdxLicenseId": str},
    total=False,
)


class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass


_RequiredParameterDefinitionTypeDef = TypedDict(
    "_RequiredParameterDefinitionTypeDef", {"Name": str, "ReferencedByResources": List[str]}
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


RollbackTriggerTypeDef = TypedDict("RollbackTriggerTypeDef", {"Arn": str, "Type": str})

_RequiredVersionSummaryTypeDef = TypedDict(
    "_RequiredVersionSummaryTypeDef",
    {"ApplicationId": str, "CreationTime": str, "SemanticVersion": str},
)
_OptionalVersionSummaryTypeDef = TypedDict(
    "_OptionalVersionSummaryTypeDef", {"SourceCodeUrl": str}, total=False
)


class VersionSummaryTypeDef(_RequiredVersionSummaryTypeDef, _OptionalVersionSummaryTypeDef):
    pass


_RequiredVersionTypeDef = TypedDict(
    "_RequiredVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List["ParameterDefinitionTypeDef"],
        "RequiredCapabilities": List[
            Literal[
                "CAPABILITY_IAM",
                "CAPABILITY_NAMED_IAM",
                "CAPABILITY_AUTO_EXPAND",
                "CAPABILITY_RESOURCE_POLICY",
            ]
        ],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "TemplateUrl": str,
    },
)
_OptionalVersionTypeDef = TypedDict(
    "_OptionalVersionTypeDef", {"SourceCodeArchiveUrl": str, "SourceCodeUrl": str}, total=False
)


class VersionTypeDef(_RequiredVersionTypeDef, _OptionalVersionTypeDef):
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
    },
    total=False,
)

CreateApplicationVersionResponseTypeDef = TypedDict(
    "CreateApplicationVersionResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List["ParameterDefinitionTypeDef"],
        "RequiredCapabilities": List[
            Literal[
                "CAPABILITY_IAM",
                "CAPABILITY_NAMED_IAM",
                "CAPABILITY_AUTO_EXPAND",
                "CAPABILITY_RESOURCE_POLICY",
            ]
        ],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)

CreateCloudFormationChangeSetResponseTypeDef = TypedDict(
    "CreateCloudFormationChangeSetResponseTypeDef",
    {"ApplicationId": str, "ChangeSetId": str, "SemanticVersion": str, "StackId": str},
    total=False,
)

CreateCloudFormationTemplateResponseTypeDef = TypedDict(
    "CreateCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": Literal["PREPARING", "ACTIVE", "EXPIRED"],
        "TemplateId": str,
        "TemplateUrl": str,
    },
    total=False,
)

GetApplicationPolicyResponseTypeDef = TypedDict(
    "GetApplicationPolicyResponseTypeDef",
    {"Statements": List["ApplicationPolicyStatementTypeDef"]},
    total=False,
)

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
    },
    total=False,
)

GetCloudFormationTemplateResponseTypeDef = TypedDict(
    "GetCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": Literal["PREPARING", "ACTIVE", "EXPIRED"],
        "TemplateId": str,
        "TemplateUrl": str,
    },
    total=False,
)

ListApplicationDependenciesResponseTypeDef = TypedDict(
    "ListApplicationDependenciesResponseTypeDef",
    {"Dependencies": List["ApplicationDependencySummaryTypeDef"], "NextToken": str},
    total=False,
)

ListApplicationVersionsResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionSummaryTypeDef"]},
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {"Applications": List["ApplicationSummaryTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ParameterValueTypeDef = TypedDict("ParameterValueTypeDef", {"Name": str, "Value": str})

PutApplicationPolicyResponseTypeDef = TypedDict(
    "PutApplicationPolicyResponseTypeDef",
    {"Statements": List["ApplicationPolicyStatementTypeDef"]},
    total=False,
)

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {"MonitoringTimeInMinutes": int, "RollbackTriggers": List["RollbackTriggerTypeDef"]},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

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
    },
    total=False,
)
