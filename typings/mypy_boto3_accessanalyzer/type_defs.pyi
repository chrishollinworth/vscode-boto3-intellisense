"""
Main interface for accessanalyzer service type definitions.

Usage::

    ```python
    from mypy_boto3_accessanalyzer.type_defs import AnalyzedResourceSummaryTypeDef

    data: AnalyzedResourceSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "AnalyzerSummaryTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CriterionTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "StatusReasonTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "GetAnalyzerResponseTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "GetFindingResponseTypeDef",
    "InlineArchiveRuleTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListAnalyzersResponseTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SortCriteriaTypeDef",
)

AnalyzedResourceSummaryTypeDef = TypedDict(
    "AnalyzedResourceSummaryTypeDef",
    {
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": Literal[
            "AWS::S3::Bucket",
            "AWS::IAM::Role",
            "AWS::SQS::Queue",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::KMS::Key",
        ],
    },
)

_RequiredAnalyzedResourceTypeDef = TypedDict(
    "_RequiredAnalyzedResourceTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "isPublic": bool,
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": Literal[
            "AWS::S3::Bucket",
            "AWS::IAM::Role",
            "AWS::SQS::Queue",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::KMS::Key",
        ],
        "updatedAt": datetime,
    },
)
_OptionalAnalyzedResourceTypeDef = TypedDict(
    "_OptionalAnalyzedResourceTypeDef",
    {
        "actions": List[str],
        "error": str,
        "sharedVia": List[str],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
    },
    total=False,
)


class AnalyzedResourceTypeDef(_RequiredAnalyzedResourceTypeDef, _OptionalAnalyzedResourceTypeDef):
    pass


_RequiredAnalyzerSummaryTypeDef = TypedDict(
    "_RequiredAnalyzerSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "status": Literal["ACTIVE", "CREATING", "DISABLED", "FAILED"],
        "type": Literal["ACCOUNT", "ORGANIZATION"],
    },
)
_OptionalAnalyzerSummaryTypeDef = TypedDict(
    "_OptionalAnalyzerSummaryTypeDef",
    {
        "lastResourceAnalyzed": str,
        "lastResourceAnalyzedAt": datetime,
        "statusReason": "StatusReasonTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class AnalyzerSummaryTypeDef(_RequiredAnalyzerSummaryTypeDef, _OptionalAnalyzerSummaryTypeDef):
    pass


ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
        "updatedAt": datetime,
    },
)

CriterionTypeDef = TypedDict(
    "CriterionTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)

FindingSourceDetailTypeDef = TypedDict(
    "FindingSourceDetailTypeDef", {"accessPointArn": str}, total=False
)

_RequiredFindingSourceTypeDef = TypedDict(
    "_RequiredFindingSourceTypeDef", {"type": Literal["POLICY", "BUCKET_ACL", "S3_ACCESS_POINT"]}
)
_OptionalFindingSourceTypeDef = TypedDict(
    "_OptionalFindingSourceTypeDef", {"detail": "FindingSourceDetailTypeDef"}, total=False
)


class FindingSourceTypeDef(_RequiredFindingSourceTypeDef, _OptionalFindingSourceTypeDef):
    pass


_RequiredFindingSummaryTypeDef = TypedDict(
    "_RequiredFindingSummaryTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": Literal[
            "AWS::S3::Bucket",
            "AWS::IAM::Role",
            "AWS::SQS::Queue",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::KMS::Key",
        ],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
        "updatedAt": datetime,
    },
)
_OptionalFindingSummaryTypeDef = TypedDict(
    "_OptionalFindingSummaryTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class FindingSummaryTypeDef(_RequiredFindingSummaryTypeDef, _OptionalFindingSummaryTypeDef):
    pass


_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": Literal[
            "AWS::S3::Bucket",
            "AWS::IAM::Role",
            "AWS::SQS::Queue",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::KMS::Key",
        ],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "code": Literal[
            "AWS_SERVICE_ACCESS_DISABLED",
            "DELEGATED_ADMINISTRATOR_DEREGISTERED",
            "ORGANIZATION_DELETED",
            "SERVICE_LINKED_ROLE_CREATION_FAILED",
        ]
    },
)

CreateAnalyzerResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseTypeDef", {"arn": str}, total=False
)

GetAnalyzedResourceResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseTypeDef", {"resource": "AnalyzedResourceTypeDef"}, total=False
)

GetAnalyzerResponseTypeDef = TypedDict(
    "GetAnalyzerResponseTypeDef", {"analyzer": "AnalyzerSummaryTypeDef"}
)

GetArchiveRuleResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseTypeDef", {"archiveRule": "ArchiveRuleSummaryTypeDef"}
)

GetFindingResponseTypeDef = TypedDict(
    "GetFindingResponseTypeDef", {"finding": "FindingTypeDef"}, total=False
)

InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef", {"filter": Dict[str, "CriterionTypeDef"], "ruleName": str}
)

_RequiredListAnalyzedResourcesResponseTypeDef = TypedDict(
    "_RequiredListAnalyzedResourcesResponseTypeDef",
    {"analyzedResources": List["AnalyzedResourceSummaryTypeDef"]},
)
_OptionalListAnalyzedResourcesResponseTypeDef = TypedDict(
    "_OptionalListAnalyzedResourcesResponseTypeDef", {"nextToken": str}, total=False
)


class ListAnalyzedResourcesResponseTypeDef(
    _RequiredListAnalyzedResourcesResponseTypeDef, _OptionalListAnalyzedResourcesResponseTypeDef
):
    pass


_RequiredListAnalyzersResponseTypeDef = TypedDict(
    "_RequiredListAnalyzersResponseTypeDef", {"analyzers": List["AnalyzerSummaryTypeDef"]}
)
_OptionalListAnalyzersResponseTypeDef = TypedDict(
    "_OptionalListAnalyzersResponseTypeDef", {"nextToken": str}, total=False
)


class ListAnalyzersResponseTypeDef(
    _RequiredListAnalyzersResponseTypeDef, _OptionalListAnalyzersResponseTypeDef
):
    pass


_RequiredListArchiveRulesResponseTypeDef = TypedDict(
    "_RequiredListArchiveRulesResponseTypeDef", {"archiveRules": List["ArchiveRuleSummaryTypeDef"]}
)
_OptionalListArchiveRulesResponseTypeDef = TypedDict(
    "_OptionalListArchiveRulesResponseTypeDef", {"nextToken": str}, total=False
)


class ListArchiveRulesResponseTypeDef(
    _RequiredListArchiveRulesResponseTypeDef, _OptionalListArchiveRulesResponseTypeDef
):
    pass


_RequiredListFindingsResponseTypeDef = TypedDict(
    "_RequiredListFindingsResponseTypeDef", {"findings": List["FindingSummaryTypeDef"]}
)
_OptionalListFindingsResponseTypeDef = TypedDict(
    "_OptionalListFindingsResponseTypeDef", {"nextToken": str}, total=False
)


class ListFindingsResponseTypeDef(
    _RequiredListFindingsResponseTypeDef, _OptionalListFindingsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef", {"attributeName": str, "orderBy": Literal["ASC", "DESC"]}, total=False
)
