"""
Main interface for rekognition service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rekognition import (
        Client,
        DescribeProjectVersionsPaginator,
        DescribeProjectsPaginator,
        ListCollectionsPaginator,
        ListDatasetEntriesPaginator,
        ListDatasetLabelsPaginator,
        ListFacesPaginator,
        ListProjectPoliciesPaginator,
        ListStreamProcessorsPaginator,
        ListUsersPaginator,
        ProjectVersionRunningWaiter,
        ProjectVersionTrainingCompletedWaiter,
        RekognitionClient,
    )

    session = Session()
    client: RekognitionClient = session.client("rekognition")

    project_version_running_waiter: ProjectVersionRunningWaiter = client.get_waiter("project_version_running")
    project_version_training_completed_waiter: ProjectVersionTrainingCompletedWaiter = client.get_waiter("project_version_training_completed")

    describe_project_versions_paginator: DescribeProjectVersionsPaginator = client.get_paginator("describe_project_versions")
    describe_projects_paginator: DescribeProjectsPaginator = client.get_paginator("describe_projects")
    list_collections_paginator: ListCollectionsPaginator = client.get_paginator("list_collections")
    list_dataset_entries_paginator: ListDatasetEntriesPaginator = client.get_paginator("list_dataset_entries")
    list_dataset_labels_paginator: ListDatasetLabelsPaginator = client.get_paginator("list_dataset_labels")
    list_faces_paginator: ListFacesPaginator = client.get_paginator("list_faces")
    list_project_policies_paginator: ListProjectPoliciesPaginator = client.get_paginator("list_project_policies")
    list_stream_processors_paginator: ListStreamProcessorsPaginator = client.get_paginator("list_stream_processors")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from .client import RekognitionClient
from .paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListDatasetEntriesPaginator,
    ListDatasetLabelsPaginator,
    ListFacesPaginator,
    ListProjectPoliciesPaginator,
    ListStreamProcessorsPaginator,
    ListUsersPaginator,
)
from .waiter import ProjectVersionRunningWaiter, ProjectVersionTrainingCompletedWaiter

Client = RekognitionClient

__all__ = (
    "Client",
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListDatasetEntriesPaginator",
    "ListDatasetLabelsPaginator",
    "ListFacesPaginator",
    "ListProjectPoliciesPaginator",
    "ListStreamProcessorsPaginator",
    "ListUsersPaginator",
    "ProjectVersionRunningWaiter",
    "ProjectVersionTrainingCompletedWaiter",
    "RekognitionClient",
)
