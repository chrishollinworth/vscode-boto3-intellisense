"""
Main interface for opsworks service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_opsworks import (
        AppExistsWaiter,
        Client,
        DeploymentSuccessfulWaiter,
        DescribeEcsClustersPaginator,
        InstanceOnlineWaiter,
        InstanceRegisteredWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
        OpsWorksClient,
        OpsWorksServiceResource,
        ServiceResource,
    )

    session = Session()
    client: OpsWorksClient = session.client("opsworks")

    resource: OpsWorksServiceResource = session.resource("opsworks")

    app_exists_waiter: AppExistsWaiter = client.get_waiter("app_exists")
    deployment_successful_waiter: DeploymentSuccessfulWaiter = client.get_waiter("deployment_successful")
    instance_online_waiter: InstanceOnlineWaiter = client.get_waiter("instance_online")
    instance_registered_waiter: InstanceRegisteredWaiter = client.get_waiter("instance_registered")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")

    describe_ecs_clusters_paginator: DescribeEcsClustersPaginator = client.get_paginator("describe_ecs_clusters")
    ```
"""

from .client import OpsWorksClient
from .paginator import DescribeEcsClustersPaginator
from .waiter import (
    AppExistsWaiter,
    DeploymentSuccessfulWaiter,
    InstanceOnlineWaiter,
    InstanceRegisteredWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
)

try:
    from .service_resource import OpsWorksServiceResource
except ImportError:
    from builtins import object as OpsWorksServiceResource  # type: ignore[assignment]

Client = OpsWorksClient

ServiceResource = OpsWorksServiceResource

__all__ = (
    "AppExistsWaiter",
    "Client",
    "DeploymentSuccessfulWaiter",
    "DescribeEcsClustersPaginator",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "OpsWorksClient",
    "OpsWorksServiceResource",
    "ServiceResource",
)
