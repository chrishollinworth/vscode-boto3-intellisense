"""
Type annotations for ec2 service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ec2.client import EC2Client
    from mypy_boto3_ec2.waiter import (
        BundleTaskCompleteWaiter,
        ConversionTaskCancelledWaiter,
        ConversionTaskCompletedWaiter,
        ConversionTaskDeletedWaiter,
        CustomerGatewayAvailableWaiter,
        ExportTaskCancelledWaiter,
        ExportTaskCompletedWaiter,
        ImageAvailableWaiter,
        ImageExistsWaiter,
        InstanceExistsWaiter,
        InstanceRunningWaiter,
        InstanceStatusOkWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
        InternetGatewayExistsWaiter,
        KeyPairExistsWaiter,
        NatGatewayAvailableWaiter,
        NatGatewayDeletedWaiter,
        NetworkInterfaceAvailableWaiter,
        PasswordDataAvailableWaiter,
        SecurityGroupExistsWaiter,
        SnapshotCompletedWaiter,
        SnapshotImportedWaiter,
        SpotInstanceRequestFulfilledWaiter,
        StoreImageTaskCompleteWaiter,
        SubnetAvailableWaiter,
        SystemStatusOkWaiter,
        VolumeAvailableWaiter,
        VolumeDeletedWaiter,
        VolumeInUseWaiter,
        VpcAvailableWaiter,
        VpcExistsWaiter,
        VpcPeeringConnectionDeletedWaiter,
        VpcPeeringConnectionExistsWaiter,
        VpnConnectionAvailableWaiter,
        VpnConnectionDeletedWaiter,
    )

    session = Session()
    client: EC2Client = session.client("ec2")

    bundle_task_complete_waiter: BundleTaskCompleteWaiter = client.get_waiter("bundle_task_complete")
    conversion_task_cancelled_waiter: ConversionTaskCancelledWaiter = client.get_waiter("conversion_task_cancelled")
    conversion_task_completed_waiter: ConversionTaskCompletedWaiter = client.get_waiter("conversion_task_completed")
    conversion_task_deleted_waiter: ConversionTaskDeletedWaiter = client.get_waiter("conversion_task_deleted")
    customer_gateway_available_waiter: CustomerGatewayAvailableWaiter = client.get_waiter("customer_gateway_available")
    export_task_cancelled_waiter: ExportTaskCancelledWaiter = client.get_waiter("export_task_cancelled")
    export_task_completed_waiter: ExportTaskCompletedWaiter = client.get_waiter("export_task_completed")
    image_available_waiter: ImageAvailableWaiter = client.get_waiter("image_available")
    image_exists_waiter: ImageExistsWaiter = client.get_waiter("image_exists")
    instance_exists_waiter: InstanceExistsWaiter = client.get_waiter("instance_exists")
    instance_running_waiter: InstanceRunningWaiter = client.get_waiter("instance_running")
    instance_status_ok_waiter: InstanceStatusOkWaiter = client.get_waiter("instance_status_ok")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")
    internet_gateway_exists_waiter: InternetGatewayExistsWaiter = client.get_waiter("internet_gateway_exists")
    key_pair_exists_waiter: KeyPairExistsWaiter = client.get_waiter("key_pair_exists")
    nat_gateway_available_waiter: NatGatewayAvailableWaiter = client.get_waiter("nat_gateway_available")
    nat_gateway_deleted_waiter: NatGatewayDeletedWaiter = client.get_waiter("nat_gateway_deleted")
    network_interface_available_waiter: NetworkInterfaceAvailableWaiter = client.get_waiter("network_interface_available")
    password_data_available_waiter: PasswordDataAvailableWaiter = client.get_waiter("password_data_available")
    security_group_exists_waiter: SecurityGroupExistsWaiter = client.get_waiter("security_group_exists")
    snapshot_completed_waiter: SnapshotCompletedWaiter = client.get_waiter("snapshot_completed")
    snapshot_imported_waiter: SnapshotImportedWaiter = client.get_waiter("snapshot_imported")
    spot_instance_request_fulfilled_waiter: SpotInstanceRequestFulfilledWaiter = client.get_waiter("spot_instance_request_fulfilled")
    store_image_task_complete_waiter: StoreImageTaskCompleteWaiter = client.get_waiter("store_image_task_complete")
    subnet_available_waiter: SubnetAvailableWaiter = client.get_waiter("subnet_available")
    system_status_ok_waiter: SystemStatusOkWaiter = client.get_waiter("system_status_ok")
    volume_available_waiter: VolumeAvailableWaiter = client.get_waiter("volume_available")
    volume_deleted_waiter: VolumeDeletedWaiter = client.get_waiter("volume_deleted")
    volume_in_use_waiter: VolumeInUseWaiter = client.get_waiter("volume_in_use")
    vpc_available_waiter: VpcAvailableWaiter = client.get_waiter("vpc_available")
    vpc_exists_waiter: VpcExistsWaiter = client.get_waiter("vpc_exists")
    vpc_peering_connection_deleted_waiter: VpcPeeringConnectionDeletedWaiter = client.get_waiter("vpc_peering_connection_deleted")
    vpc_peering_connection_exists_waiter: VpcPeeringConnectionExistsWaiter = client.get_waiter("vpc_peering_connection_exists")
    vpn_connection_available_waiter: VpnConnectionAvailableWaiter = client.get_waiter("vpn_connection_available")
    vpn_connection_deleted_waiter: VpnConnectionDeletedWaiter = client.get_waiter("vpn_connection_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeBundleTasksRequestWaitTypeDef,
    DescribeConversionTasksRequestWaitExtraExtraTypeDef,
    DescribeConversionTasksRequestWaitExtraTypeDef,
    DescribeConversionTasksRequestWaitTypeDef,
    DescribeCustomerGatewaysRequestWaitTypeDef,
    DescribeExportTasksRequestWaitExtraTypeDef,
    DescribeExportTasksRequestWaitTypeDef,
    DescribeImagesRequestWaitExtraTypeDef,
    DescribeImagesRequestWaitTypeDef,
    DescribeImportSnapshotTasksRequestWaitTypeDef,
    DescribeInstancesRequestWaitExtraExtraExtraTypeDef,
    DescribeInstancesRequestWaitExtraExtraTypeDef,
    DescribeInstancesRequestWaitExtraTypeDef,
    DescribeInstancesRequestWaitTypeDef,
    DescribeInstanceStatusRequestWaitExtraTypeDef,
    DescribeInstanceStatusRequestWaitTypeDef,
    DescribeInternetGatewaysRequestWaitTypeDef,
    DescribeKeyPairsRequestWaitTypeDef,
    DescribeNatGatewaysRequestWaitExtraTypeDef,
    DescribeNatGatewaysRequestWaitTypeDef,
    DescribeNetworkInterfacesRequestWaitTypeDef,
    DescribeSecurityGroupsRequestWaitTypeDef,
    DescribeSnapshotsRequestWaitTypeDef,
    DescribeSpotInstanceRequestsRequestWaitTypeDef,
    DescribeStoreImageTasksRequestWaitTypeDef,
    DescribeSubnetsRequestWaitTypeDef,
    DescribeVolumesRequestWaitExtraExtraTypeDef,
    DescribeVolumesRequestWaitExtraTypeDef,
    DescribeVolumesRequestWaitTypeDef,
    DescribeVpcPeeringConnectionsRequestWaitExtraTypeDef,
    DescribeVpcPeeringConnectionsRequestWaitTypeDef,
    DescribeVpcsRequestWaitExtraTypeDef,
    DescribeVpcsRequestWaitTypeDef,
    DescribeVpnConnectionsRequestWaitExtraTypeDef,
    DescribeVpnConnectionsRequestWaitTypeDef,
    GetPasswordDataRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "BundleTaskCompleteWaiter",
    "ConversionTaskCancelledWaiter",
    "ConversionTaskCompletedWaiter",
    "ConversionTaskDeletedWaiter",
    "CustomerGatewayAvailableWaiter",
    "ExportTaskCancelledWaiter",
    "ExportTaskCompletedWaiter",
    "ImageAvailableWaiter",
    "ImageExistsWaiter",
    "InstanceExistsWaiter",
    "InstanceRunningWaiter",
    "InstanceStatusOkWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "InternetGatewayExistsWaiter",
    "KeyPairExistsWaiter",
    "NatGatewayAvailableWaiter",
    "NatGatewayDeletedWaiter",
    "NetworkInterfaceAvailableWaiter",
    "PasswordDataAvailableWaiter",
    "SecurityGroupExistsWaiter",
    "SnapshotCompletedWaiter",
    "SnapshotImportedWaiter",
    "SpotInstanceRequestFulfilledWaiter",
    "StoreImageTaskCompleteWaiter",
    "SubnetAvailableWaiter",
    "SystemStatusOkWaiter",
    "VolumeAvailableWaiter",
    "VolumeDeletedWaiter",
    "VolumeInUseWaiter",
    "VpcAvailableWaiter",
    "VpcExistsWaiter",
    "VpcPeeringConnectionDeletedWaiter",
    "VpcPeeringConnectionExistsWaiter",
    "VpnConnectionAvailableWaiter",
    "VpnConnectionDeletedWaiter",
)

class BundleTaskCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/BundleTaskComplete.html#EC2.Waiter.BundleTaskComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#bundletaskcompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBundleTasksRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/BundleTaskComplete.html#EC2.Waiter.BundleTaskComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#bundletaskcompletewaiter)
        """

class ConversionTaskCancelledWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ConversionTaskCancelled.html#EC2.Waiter.ConversionTaskCancelled)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#conversiontaskcancelledwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConversionTasksRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ConversionTaskCancelled.html#EC2.Waiter.ConversionTaskCancelled.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#conversiontaskcancelledwaiter)
        """

class ConversionTaskCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ConversionTaskCompleted.html#EC2.Waiter.ConversionTaskCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#conversiontaskcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConversionTasksRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ConversionTaskCompleted.html#EC2.Waiter.ConversionTaskCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#conversiontaskcompletedwaiter)
        """

class ConversionTaskDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ConversionTaskDeleted.html#EC2.Waiter.ConversionTaskDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#conversiontaskdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConversionTasksRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ConversionTaskDeleted.html#EC2.Waiter.ConversionTaskDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#conversiontaskdeletedwaiter)
        """

class CustomerGatewayAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/CustomerGatewayAvailable.html#EC2.Waiter.CustomerGatewayAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#customergatewayavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCustomerGatewaysRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/CustomerGatewayAvailable.html#EC2.Waiter.CustomerGatewayAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#customergatewayavailablewaiter)
        """

class ExportTaskCancelledWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ExportTaskCancelled.html#EC2.Waiter.ExportTaskCancelled)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#exporttaskcancelledwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportTasksRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ExportTaskCancelled.html#EC2.Waiter.ExportTaskCancelled.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#exporttaskcancelledwaiter)
        """

class ExportTaskCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ExportTaskCompleted.html#EC2.Waiter.ExportTaskCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#exporttaskcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportTasksRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ExportTaskCompleted.html#EC2.Waiter.ExportTaskCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#exporttaskcompletedwaiter)
        """

class ImageAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ImageAvailable.html#EC2.Waiter.ImageAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#imageavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImagesRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ImageAvailable.html#EC2.Waiter.ImageAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#imageavailablewaiter)
        """

class ImageExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ImageExists.html#EC2.Waiter.ImageExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#imageexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImagesRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/ImageExists.html#EC2.Waiter.ImageExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#imageexistswaiter)
        """

class InstanceExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceExists.html#EC2.Waiter.InstanceExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instanceexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceExists.html#EC2.Waiter.InstanceExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instanceexistswaiter)
        """

class InstanceRunningWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceRunning.html#EC2.Waiter.InstanceRunning)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instancerunningwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceRunning.html#EC2.Waiter.InstanceRunning.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instancerunningwaiter)
        """

class InstanceStatusOkWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceStatusOk.html#EC2.Waiter.InstanceStatusOk)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instancestatusokwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceStatusRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceStatusOk.html#EC2.Waiter.InstanceStatusOk.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instancestatusokwaiter)
        """

class InstanceStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceStopped.html#EC2.Waiter.InstanceStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instancestoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceStopped.html#EC2.Waiter.InstanceStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instancestoppedwaiter)
        """

class InstanceTerminatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceTerminated.html#EC2.Waiter.InstanceTerminated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instanceterminatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InstanceTerminated.html#EC2.Waiter.InstanceTerminated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#instanceterminatedwaiter)
        """

class InternetGatewayExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InternetGatewayExists.html#EC2.Waiter.InternetGatewayExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#internetgatewayexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInternetGatewaysRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/InternetGatewayExists.html#EC2.Waiter.InternetGatewayExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#internetgatewayexistswaiter)
        """

class KeyPairExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/KeyPairExists.html#EC2.Waiter.KeyPairExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#keypairexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeKeyPairsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/KeyPairExists.html#EC2.Waiter.KeyPairExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#keypairexistswaiter)
        """

class NatGatewayAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/NatGatewayAvailable.html#EC2.Waiter.NatGatewayAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#natgatewayavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNatGatewaysRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/NatGatewayAvailable.html#EC2.Waiter.NatGatewayAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#natgatewayavailablewaiter)
        """

class NatGatewayDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/NatGatewayDeleted.html#EC2.Waiter.NatGatewayDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#natgatewaydeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNatGatewaysRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/NatGatewayDeleted.html#EC2.Waiter.NatGatewayDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#natgatewaydeletedwaiter)
        """

class NetworkInterfaceAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/NetworkInterfaceAvailable.html#EC2.Waiter.NetworkInterfaceAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#networkinterfaceavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkInterfacesRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/NetworkInterfaceAvailable.html#EC2.Waiter.NetworkInterfaceAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#networkinterfaceavailablewaiter)
        """

class PasswordDataAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/PasswordDataAvailable.html#EC2.Waiter.PasswordDataAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#passworddataavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPasswordDataRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/PasswordDataAvailable.html#EC2.Waiter.PasswordDataAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#passworddataavailablewaiter)
        """

class SecurityGroupExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SecurityGroupExists.html#EC2.Waiter.SecurityGroupExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#securitygroupexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSecurityGroupsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SecurityGroupExists.html#EC2.Waiter.SecurityGroupExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#securitygroupexistswaiter)
        """

class SnapshotCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SnapshotCompleted.html#EC2.Waiter.SnapshotCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#snapshotcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SnapshotCompleted.html#EC2.Waiter.SnapshotCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#snapshotcompletedwaiter)
        """

class SnapshotImportedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SnapshotImported.html#EC2.Waiter.SnapshotImported)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#snapshotimportedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImportSnapshotTasksRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SnapshotImported.html#EC2.Waiter.SnapshotImported.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#snapshotimportedwaiter)
        """

class SpotInstanceRequestFulfilledWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SpotInstanceRequestFulfilled.html#EC2.Waiter.SpotInstanceRequestFulfilled)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#spotinstancerequestfulfilledwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSpotInstanceRequestsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SpotInstanceRequestFulfilled.html#EC2.Waiter.SpotInstanceRequestFulfilled.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#spotinstancerequestfulfilledwaiter)
        """

class StoreImageTaskCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/StoreImageTaskComplete.html#EC2.Waiter.StoreImageTaskComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#storeimagetaskcompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStoreImageTasksRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/StoreImageTaskComplete.html#EC2.Waiter.StoreImageTaskComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#storeimagetaskcompletewaiter)
        """

class SubnetAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SubnetAvailable.html#EC2.Waiter.SubnetAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#subnetavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSubnetsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SubnetAvailable.html#EC2.Waiter.SubnetAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#subnetavailablewaiter)
        """

class SystemStatusOkWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SystemStatusOk.html#EC2.Waiter.SystemStatusOk)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#systemstatusokwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceStatusRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/SystemStatusOk.html#EC2.Waiter.SystemStatusOk.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#systemstatusokwaiter)
        """

class VolumeAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VolumeAvailable.html#EC2.Waiter.VolumeAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#volumeavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVolumesRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VolumeAvailable.html#EC2.Waiter.VolumeAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#volumeavailablewaiter)
        """

class VolumeDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VolumeDeleted.html#EC2.Waiter.VolumeDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#volumedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVolumesRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VolumeDeleted.html#EC2.Waiter.VolumeDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#volumedeletedwaiter)
        """

class VolumeInUseWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VolumeInUse.html#EC2.Waiter.VolumeInUse)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#volumeinusewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVolumesRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VolumeInUse.html#EC2.Waiter.VolumeInUse.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#volumeinusewaiter)
        """

class VpcAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcAvailable.html#EC2.Waiter.VpcAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcAvailable.html#EC2.Waiter.VpcAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcavailablewaiter)
        """

class VpcExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcExists.html#EC2.Waiter.VpcExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcsRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcExists.html#EC2.Waiter.VpcExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcexistswaiter)
        """

class VpcPeeringConnectionDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcPeeringConnectionDeleted.html#EC2.Waiter.VpcPeeringConnectionDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcpeeringconnectiondeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcPeeringConnectionsRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcPeeringConnectionDeleted.html#EC2.Waiter.VpcPeeringConnectionDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcpeeringconnectiondeletedwaiter)
        """

class VpcPeeringConnectionExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcPeeringConnectionExists.html#EC2.Waiter.VpcPeeringConnectionExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcpeeringconnectionexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcPeeringConnectionsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpcPeeringConnectionExists.html#EC2.Waiter.VpcPeeringConnectionExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpcpeeringconnectionexistswaiter)
        """

class VpnConnectionAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpnConnectionAvailable.html#EC2.Waiter.VpnConnectionAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpnconnectionavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpnConnectionsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpnConnectionAvailable.html#EC2.Waiter.VpnConnectionAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpnconnectionavailablewaiter)
        """

class VpnConnectionDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpnConnectionDeleted.html#EC2.Waiter.VpnConnectionDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpnconnectiondeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpnConnectionsRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/waiter/VpnConnectionDeleted.html#EC2.Waiter.VpnConnectionDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters/#vpnconnectiondeletedwaiter)
        """
