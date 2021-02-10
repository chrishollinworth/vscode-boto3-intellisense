"""
Main interface for iotfleethub service type definitions.

Usage::

    ```python
    from mypy_boto3_iotfleethub.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
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
    "ApplicationSummaryTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {"applicationId": str, "applicationName": str, "applicationUrl": str},
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "applicationDescription": str,
        "applicationCreationDate": int,
        "applicationLastUpdateDate": int,
        "applicationState": Literal[
            "CREATING", "DELETING", "ACTIVE", "CREATE_FAILED", "DELETE_FAILED"
        ],
    },
    total=False,
)


class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass


CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef", {"applicationId": str, "applicationArn": str}
)

_RequiredDescribeApplicationResponseTypeDef = TypedDict(
    "_RequiredDescribeApplicationResponseTypeDef",
    {
        "applicationId": str,
        "applicationArn": str,
        "applicationName": str,
        "applicationUrl": str,
        "applicationState": Literal[
            "CREATING", "DELETING", "ACTIVE", "CREATE_FAILED", "DELETE_FAILED"
        ],
        "applicationCreationDate": int,
        "applicationLastUpdateDate": int,
        "roleArn": str,
    },
)
_OptionalDescribeApplicationResponseTypeDef = TypedDict(
    "_OptionalDescribeApplicationResponseTypeDef",
    {
        "applicationDescription": str,
        "ssoClientId": str,
        "errorMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class DescribeApplicationResponseTypeDef(
    _RequiredDescribeApplicationResponseTypeDef, _OptionalDescribeApplicationResponseTypeDef
):
    pass


ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {"applicationSummaries": List["ApplicationSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
