"""
Main interface for rekognition service.

Usage::

    ```python
    import boto3
    from mypy_boto3_rekognition import (
        Client,
        DescribeProjectVersionsPaginator,
        DescribeProjectsPaginator,
        ListCollectionsPaginator,
        ListFacesPaginator,
        ListStreamProcessorsPaginator,
        ProjectVersionRunningWaiter,
        ProjectVersionTrainingCompletedWaiter,
        RekognitionClient,
    )

    session = boto3.Session()

    client: RekognitionClient = boto3.client("rekognition")
    session_client: RekognitionClient = session.client("rekognition")

    project_version_running_waiter: ProjectVersionRunningWaiter = client.get_waiter("project_version_running")
    project_version_training_completed_waiter: ProjectVersionTrainingCompletedWaiter = client.get_waiter("project_version_training_completed")

    describe_project_versions_paginator: DescribeProjectVersionsPaginator = client.get_paginator("describe_project_versions")
    describe_projects_paginator: DescribeProjectsPaginator = client.get_paginator("describe_projects")
    list_collections_paginator: ListCollectionsPaginator = client.get_paginator("list_collections")
    list_faces_paginator: ListFacesPaginator = client.get_paginator("list_faces")
    list_stream_processors_paginator: ListStreamProcessorsPaginator = client.get_paginator("list_stream_processors")
    ```
"""
from .client import RekognitionClient
from .paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListFacesPaginator,
    ListStreamProcessorsPaginator,
)
from .waiter import ProjectVersionRunningWaiter, ProjectVersionTrainingCompletedWaiter

Client = RekognitionClient

__all__ = (
    "Client",
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
    "ProjectVersionRunningWaiter",
    "ProjectVersionTrainingCompletedWaiter",
    "RekognitionClient",
)
