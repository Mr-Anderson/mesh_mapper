## *********************************************************
## 
## File autogenerated for the mesh_bot_control package 
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

config_description = [{'srcline': 13, 'description': 'max robot speed in lineardirection', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'base_linear_speed', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 14, 'description': 'max robot speed in angular direction', 'max': 4.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'base_rot_speed', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 15, 'description': 'multiplyer of turbo button x', 'max': 5.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'turbo_angular', 'edit_method': '', 'default': 1.5, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 16, 'description': 'multiplyer of turbo button y', 'max': 5.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'turbo_linear', 'edit_method': '', 'default': 2.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 17, 'description': 'the percent that the dpad is scaled down', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'd_pad_percent', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 18, 'description': 'phrase to say when plus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'plus_mesage', 'edit_method': '', 'default': 'Pardon me. coming through.', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 19, 'description': 'sound to play when minus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'minus_sound', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/sounds/Ahooga_Car_Horn.wav', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 20, 'description': '.yaml file with autonomous waypoints', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'autonomous_waypoints', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/yaml/Autonomous_Waypoints.yaml', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 21, 'description': '.yaml file with autonomous waypoints', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'navigation_waypoints', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/yaml/Navigation_Waypoints.yaml', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 22, 'description': 'sound to play when minus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'waypoint_sound', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/sounds/Ahooga_Car_Horn.wav', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 23, 'description': 'sound to play when minus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/mesh_bot_control.cfg', 'name': 'done_sound', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/sounds/Ahooga_Car_Horn.wav', 'level': 0, 'min': '', 'type': 'str'}]

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

