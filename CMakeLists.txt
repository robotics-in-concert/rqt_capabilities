cmake_minimum_required(VERSION 2.8.3)
project(rqt_capabilities)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

## Install script
install(PROGRAMS scripts/rqt_capabilities
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

## Install resources
install(DIRECTORY resources
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

## Install plugin file
install(FILES plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
