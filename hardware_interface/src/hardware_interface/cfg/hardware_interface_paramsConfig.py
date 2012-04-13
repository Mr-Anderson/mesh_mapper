## *********************************************************
## 
## File autogenerated for the hardware_interface package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

config_description = [{'srcline': 15, 'description': 'The time in seconds between watchdog timeouts', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'watchdog_timeout', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 16, 'description': 'Top motor speed in ticks/second', 'max': 800.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'max_speed', 'edit_method': '', 'default': 600.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 17, 'description': 'Stop motor threshold speed in ticks/second', 'max': 800.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'min_speed', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 18, 'description': 'Motor resolution in ticks/revolution', 'max': 500.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'motor_res', 'edit_method': '', 'default': 200.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 19, 'description': 'Radius of the robot base in meters', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'base_radius', 'edit_method': '', 'default': 0.177, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 20, 'description': 'Radius of the robot wheels in meters', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'wheel_radius', 'edit_method': '', 'default': 0.1016, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 21, 'description': 'I2C address of motor 1 controller', 'max': 127, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'motor1_i2c_addr', 'edit_method': '', 'default': 3, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 22, 'description': 'I2C address of motor 2 controller', 'max': 127, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'motor2_i2c_addr', 'edit_method': '', 'default': 1, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 23, 'description': 'I2C address of motor 3 controller', 'max': 127, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'motor3_i2c_addr', 'edit_method': '', 'default': 2, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 24, 'description': 'Enable control of Kinect tilt angle', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'tilt_enable', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 25, 'description': 'Serial port for motor controller', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/hardware_interface.cfg', 'name': 'serial_port', 'edit_method': '', 'default': '/dev/ttyUSB0', 'level': 0, 'min': '', 'type': 'str'}]

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

for param in config_description:
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

