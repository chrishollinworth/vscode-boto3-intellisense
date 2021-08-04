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
    "FeedbackKeyType",
    "FeedbackValueType",
    "LogFilterType",
    "OsTypeType",
    "SeverityLevelType",
    "StatusType",
    "TierType",
)

CloudWatchEventSourceType = Literal["CODE_DEPLOY", "EC2", "HEALTH", "RDS"]
ConfigurationEventResourceTypeType = Literal[
    "CLOUDFORMATION", "CLOUDWATCH_ALARM", "CLOUDWATCH_LOG", "SSM_ASSOCIATION"
]
ConfigurationEventStatusType = Literal["ERROR", "INFO", "WARN"]
FeedbackKeyType = Literal["INSIGHTS_FEEDBACK"]
FeedbackValueType = Literal["NOT_SPECIFIED", "NOT_USEFUL", "USEFUL"]
LogFilterType = Literal["ERROR", "INFO", "WARN"]
OsTypeType = Literal["LINUX", "WINDOWS"]
SeverityLevelType = Literal["High", "Low", "Medium"]
StatusType = Literal["IGNORE", "PENDING", "RESOLVED"]
TierType = Literal[
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
    "SQL_SERVER",
    "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
]
