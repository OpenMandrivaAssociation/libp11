%define major 3
%define libname %mklibname p11_ %{major}
%define devname %mklibname p11 -d

Summary:	Small library on top of PKCS#11
Name:		libp11
Version:	0.4.9
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/OpenSC/libp11
Source0:	https://github.com/OpenSC/libp11/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libltdl-devel
BuildRequires:	pkgconfig(openssl)

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to make
using PKCS#11 implementations easier.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library files for libp11
Group:		System/Libraries

%description -n %{libname}
This package contains library files for libp11.

%files -n %{libname}
%{_libdir}/libp11.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for libp11
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains files needed for development with libp11.

%files -n %{devname}
%doc examples
%{_libdir}/*.so
%{_libdir}/engines-*/*.so
%{_libdir}/pkgconfig/libp11.pc
%{_includedir}/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

rm -fr %{buildroot}%{_datadir}/doc

