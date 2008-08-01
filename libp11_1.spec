%define major 1
%define tarball_name libp11

Summary: Small library on top of PKCS#11
Name: %{tarball_name}_%{major}
Version: 0.2.3
Release: %mkrel 3
License: GPL
Group: System/Libraries
Source0: http://www.opensc.org/files/%{tarball_name}-%{version}.tar.gz
Buildrequires: libopenssl-devel
Buildrequires: libltdl-devel
URL: http://www.opensc.org//libp11
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to make
using PKCS#11 implementations easier.

%package devel
Summary: Development files for libp11
Group: Development/C
Requires: %{name} = %{version}
Provides: %{tarball_name}-devel = %{version}

%description devel
This package contains files needed for development with libp11.

%prep
%setup -q -n %{tarball_name}-%{version}

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# fix some permissions
chmod 0644 %{buildroot}%{_libdir}/*.{la,a,so.*.*}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc doc/api doc/*.html doc/README doc/*.css
%doc examples 
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libp11.pc
%{_includedir}/*


