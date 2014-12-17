Name:           ros-indigo-force-rotate-recovery
Version:        0.1.1
Release:        1%{?dist}
Summary:        ROS force_rotate_recovery package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-nav-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-base-local-planner
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-nav-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
The force_rotate_recovery package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-1
- Autogenerated by Bloom

* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-0
- Autogenerated by Bloom

* Tue Dec 09 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.5-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.3-1
- Autogenerated by Bloom

* Tue Dec 02 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.3-0
- Autogenerated by Bloom

