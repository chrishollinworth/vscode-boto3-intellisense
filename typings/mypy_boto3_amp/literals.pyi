"""
Type annotations for amp service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/literals.html)

Usage::

    ```python
    from mypy_boto3_amp.literals import AlertManagerDefinitionStatusCodeType

    data: AlertManagerDefinitionStatusCodeType = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlertManagerDefinitionStatusCodeType",
    "ListRuleGroupsNamespacesPaginatorName",
    "ListWorkspacesPaginatorName",
    "LoggingConfigurationStatusCodeType",
    "RuleGroupsNamespaceStatusCodeType",
    "WorkspaceActiveWaiterName",
    "WorkspaceDeletedWaiterName",
    "WorkspaceStatusCodeType",
)

AlertManagerDefinitionStatusCodeType = Literal[
    "ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
]
ListRuleGroupsNamespacesPaginatorName = Literal["list_rule_groups_namespaces"]
ListWorkspacesPaginatorName = Literal["list_workspaces"]
LoggingConfigurationStatusCodeType = Literal[
    "ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
]
RuleGroupsNamespaceStatusCodeType = Literal[
    "ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
]
WorkspaceActiveWaiterName = Literal["workspace_active"]
WorkspaceDeletedWaiterName = Literal["workspace_deleted"]
WorkspaceStatusCodeType = Literal["ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATING"]
