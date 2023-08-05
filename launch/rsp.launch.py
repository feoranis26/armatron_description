import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='armatron_description').find('armatron_description')
    mpath = os.path.join(pkg_share, 'description/armatron_description.urdf')
    #default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf_config.rviz')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        arguments=[mpath]
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
    )

    return launch.LaunchDescription([
        joint_state_publisher_node,
        robot_state_publisher_node,
    ])