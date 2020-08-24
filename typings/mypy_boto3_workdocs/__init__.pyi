"""
Main interface for workdocs service.

Usage::

    ```python
    import boto3
    from mypy_boto3_workdocs import (
        Client,
        DescribeActivitiesPaginator,
        DescribeCommentsPaginator,
        DescribeDocumentVersionsPaginator,
        DescribeFolderContentsPaginator,
        DescribeGroupsPaginator,
        DescribeNotificationSubscriptionsPaginator,
        DescribeResourcePermissionsPaginator,
        DescribeRootFoldersPaginator,
        DescribeUsersPaginator,
        WorkDocsClient,
    )

    session = boto3.Session()

    client: WorkDocsClient = boto3.client("workdocs")
    session_client: WorkDocsClient = session.client("workdocs")

    describe_activities_paginator: DescribeActivitiesPaginator = client.get_paginator("describe_activities")
    describe_comments_paginator: DescribeCommentsPaginator = client.get_paginator("describe_comments")
    describe_document_versions_paginator: DescribeDocumentVersionsPaginator = client.get_paginator("describe_document_versions")
    describe_folder_contents_paginator: DescribeFolderContentsPaginator = client.get_paginator("describe_folder_contents")
    describe_groups_paginator: DescribeGroupsPaginator = client.get_paginator("describe_groups")
    describe_notification_subscriptions_paginator: DescribeNotificationSubscriptionsPaginator = client.get_paginator("describe_notification_subscriptions")
    describe_resource_permissions_paginator: DescribeResourcePermissionsPaginator = client.get_paginator("describe_resource_permissions")
    describe_root_folders_paginator: DescribeRootFoldersPaginator = client.get_paginator("describe_root_folders")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""
from mypy_boto3_workdocs.client import WorkDocsClient
from mypy_boto3_workdocs.paginator import (
    DescribeActivitiesPaginator,
    DescribeCommentsPaginator,
    DescribeDocumentVersionsPaginator,
    DescribeFolderContentsPaginator,
    DescribeGroupsPaginator,
    DescribeNotificationSubscriptionsPaginator,
    DescribeResourcePermissionsPaginator,
    DescribeRootFoldersPaginator,
    DescribeUsersPaginator,
)

Client = WorkDocsClient


__all__ = (
    "Client",
    "DescribeActivitiesPaginator",
    "DescribeCommentsPaginator",
    "DescribeDocumentVersionsPaginator",
    "DescribeFolderContentsPaginator",
    "DescribeGroupsPaginator",
    "DescribeNotificationSubscriptionsPaginator",
    "DescribeResourcePermissionsPaginator",
    "DescribeRootFoldersPaginator",
    "DescribeUsersPaginator",
    "WorkDocsClient",
)
