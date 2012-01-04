%define major 2
%define libname %mklibname p11_ %major
%define develname %mklibname p11 -d

Summary: Small library on top of PKCS#11
Name: libp11
Version: 0.2.8
Release: 1
License: LGPLv2+
Group: System/Libraries
Source0: http://www.opensc-project.org/files/libp11/%{name}-%{version}.tar.gz
Buildrequires: libopenssl-devel
Buildrequires: libltdl-devel
URL: http://www.opensc-project.org/libp11/

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to make
using PKCS#11 implementations easier.

%package -n %libname
Summary: Library files for libp11
Group: System/Libraries
Obsoletes: libp11_1 < %version
Obsoletes: %mklibname p11 0

%description -n %libname
This package contains library files for libp11.

%package -n %develname
Summary: Development files for libp11
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%release
Obsoletes: libp11_1-devel < %{version}

%description -n %develname
This package contains files needed for development with libp11.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -rf %{buildroot}/%{_libdir}/libp11.a

# fix some permissions
chmod 0644 %{buildroot}%{_libdir}/*.so.*.*

rm -fr %buildroot%_datadir/doc

%files -n %libname
%doc NEWS
%{_libdir}/*.so.%{major}*

%files -n %develname
%doc examples 
%{_libdir}/*.so
%{_libdir}/pkgconfig/libp11.pc
%{_includedir}/*
