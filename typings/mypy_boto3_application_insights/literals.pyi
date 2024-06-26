"""
Type annotations for application-insights service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/literals.html)

Usage::

    ```python
    from mypy_boto3_application_insights.literals import CloudWatchEventSourceType

    data: CloudWatchEventSourceType = "CODE_DEPLOY"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CloudWatchEventSourceType",
    "ConfigurationEventResourceTypeType",
    "ConfigurationEventStatusType",
    "DiscoveryTypeType",
    "FeedbackKeyType",
    "FeedbackValueType",
    "GroupingTypeType",
    "LogFilterType",
    "OsTypeType",
    "RecommendationTypeType",
    "ResolutionMethodType",
    "SeverityLevelType",
    "StatusType",
    "TierType",
    "UpdateStatusType",
    "VisibilityType",
)

CloudWatchEventSourceType = Literal["CODE_DEPLOY", "EC2", "HEALTH", "RDS"]
ConfigurationEventResourceTypeType = Literal[
    "CLOUDFORMATION", "CLOUDWATCH_ALARM", "CLOUDWATCH_LOG", "SSM_ASSOCIATION"
]
ConfigurationEventStatusType = Literal["ERROR", "INFO", "WARN"]
DiscoveryTypeType = Literal["ACCOUNT_BASED", "RESOURCE_GROUP_BASED"]
FeedbackKeyType = Literal["INSIGHTS_FEEDBACK"]
FeedbackValueType = Literal["NOT_SPECIFIED", "NOT_USEFUL", "USEFUL"]
GroupingTypeType = Literal["ACCOUNT_BASED"]
LogFilterType = Literal["ERROR", "INFO", "WARN"]
OsTypeType = Literal["LINUX", "WINDOWS"]
RecommendationTypeType = Literal["ALL", "INFRA_ONLY", "WORKLOAD_ONLY"]
ResolutionMethodType = Literal["AUTOMATIC", "MANUAL", "UNRESOLVED"]
SeverityLevelType = Literal["High", "Informative", "Low", "Medium"]
StatusType = Literal["IGNORE", "PENDING", "RECOVERING", "RECURRING", "RESOLVED"]
TierType = Literal[
    "ACTIVE_DIRECTORY",
    "CUSTOM",
    "DEFAULT",
    "DOT_NET_CORE",
    "DOT_NET_WEB",
    "DOT_NET_WEB_TIER",
    "DOT_NET_WORKER",
    "JAVA_JMX",
    "MYSQL",
    "ORACLE",
    "POSTGRESQL",
    "SAP_HANA_HIGH_AVAILABILITY",
    "SAP_HANA_MULTI_NODE",
    "SAP_HANA_SINGLE_NODE",
    "SAP_NETWEAVER_DISTRIBUTED",
    "SAP_NETWEAVER_HIGH_AVAILABILITY",
    "SAP_NETWEAVER_STANDARD",
    "SHAREPOINT",
    "SQL_SERVER",
    "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
    "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
]
UpdateStatusType = Literal["RESOLVED"]
VisibilityType = Literal["IGNORED", "VISIBLE"]
