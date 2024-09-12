from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import PushRosNamespace
from launch_ros.substitutions import FindPackageShare
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument("launch_driver", default_value="true"),
        DeclareLaunchArgument("host_ip", default_value="192.168.1.10"),
        DeclareLaunchArgument("use_concat_filter", default_value="true"),
        DeclareLaunchArgument("vehicle_id", default_value="$(env VEHICLE_ID default)"),
        DeclareLaunchArgument("vehicle_mirror_param_file"),
        DeclareLaunchArgument("pointcloud_container_name", default_value="pointcloud_container"),

        GroupAction([
            PushRosNamespace("lidar"),

            GroupAction([
                PushRosNamespace("top"),
                IncludeLaunchDescription(
                    XMLLaunchDescriptionSource(
                        [
                            FindPackageShare("common_sensor_launch"),
                            "/launch/velodyne_VLS128.launch.xml"
                        ]
                    ),
                    launch_arguments={
                        "max_range": "250.0",
                        "sensor_frame": "velodyne_top",
                        "sensor_ip": "192.168.1.201",
                        "host_ip": LaunchConfiguration("host_ip"),
                        "data_port": "2368",
                        "scan_phase": "300.0",
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        ),
                        "container_name": "pointcloud_container"
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("left"),
                IncludeLaunchDescription(
                    XMLLaunchDescriptionSource(
                        [
                            FindPackageShare("common_sensor_launch"),
                            "/launch/velodyne_VLP16.launch.xml"
                        ]
                    ),
                    launch_arguments={
                        "max_range": "5.0",
                        "sensor_frame": "velodyne_left",
                        "sensor_ip": "192.168.1.202",
                        "host_ip": LaunchConfiguration("host_ip"),
                        "data_port": "2369",
                        "scan_phase": "180.0",
                        "cloud_min_angle": "300",
                        "cloud_max_angle": "60",
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        ),
                        "container_name": "pointcloud_container"
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("right"),
                IncludeLaunchDescription(
                    XMLLaunchDescriptionSource(
                        [
                            FindPackageShare("common_sensor_launch"),
                            "/launch/velodyne_VLP16.launch.xml"
                        ]
                    ),
                    launch_arguments={
                        "max_range": "5.0",
                        "sensor_frame": "velodyne_right",
                        "sensor_ip": "192.168.1.203",
                        "host_ip": LaunchConfiguration("host_ip"),
                        "data_port": "2370",
                        "scan_phase": "180.0",
                        "cloud_min_angle": "300",
                        "cloud_max_angle": "60",
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        ),
                        "container_name": "pointcloud_container"
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("rear"),
                IncludeLaunchDescription(
                    XMLLaunchDescriptionSource(
                        [
                            FindPackageShare("common_sensor_launch"),
                            "/launch/velodyne_VLP16.launch.xml"
                        ]
                    ),
                    launch_arguments={
                        "max_range": "1.5",
                        "sensor_frame": "velodyne_rear",
                        "sensor_ip": "192.168.1.204",
                        "host_ip": LaunchConfiguration("host_ip"),
                        "data_port": "2371",
                        "scan_phase": "180.0",
                        "cloud_min_angle": "300",
                        "cloud_max_angle": "60",
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        ),
                        "container_name": "pointcloud_container"
                    }.items()
                ),
            ]),

            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [
                        FindPackageShare("sample_sensor_kit_launch"),
                        "/launch/pointcloud_preprocessor.launch.py"
                    ]
                ),
                launch_arguments={
                    "base_frame": "base_link",
                    "use_intra_process": "true",
                    "use_multithread": "true",
                    "pointcloud_container_name": LaunchConfiguration("pointcloud_container_name")
                }.items()
            ),
        ]),
    ])
