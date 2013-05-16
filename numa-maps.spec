
Name:      numa-maps
Version:   See META
Release:   See META

Summary:   Print NUMA information for running processes.
Group:     Applications/System
License:   GPL
Source:    %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%define debug_package %{nil}

%description
numa-maps is a simple script which parses /proc/PID/numa_maps
and /proc/PID/maps to display NUMA information for running
processes.


%prep 
%setup

%build
#NOOP

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"
install -D -m 755 numa-maps   ${RPM_BUILD_ROOT}/%{_bindir}/numa-maps
install -D -m 644 numa-maps.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/numa-maps.1

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,0755)
%doc ChangeLog
%{_bindir}/numa-maps
%{_mandir}/*/*

