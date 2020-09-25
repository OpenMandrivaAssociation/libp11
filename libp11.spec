%define major 3
%define libname %mklibname p11_ %{major}
%define devname %mklibname p11 -d

Summary:	Small library on top of PKCS#11
Name:		libp11
Version:	0.4.10
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/OpenSC/libp11
Source0:	https://github.com/OpenSC/libp11/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# (tpg) detect OpenSSL 3.0.x
Patch0:		libp11-0.4.10-openssl3.patch
BuildRequires:	libltdl-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(p11-kit-1)
%rename		engine_pkcs11

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to make
using PKCS#11 implementations easier.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library files for libp11
Group:		System/Libraries
Requires:	p11-kit-trust

%description -n %{libname}
This package contains library files for libp11.

%files -n %{libname}
%{_libdir}/libp11.so.%{major}*
# (tpg) these are engine plugins
%{_libdir}/engines-*/*.so

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
%{_libdir}/pkgconfig/libp11.pc
%{_includedir}/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
# (tpg) needed for OpenSSL 3.0.x patch
autoreconf -fiv

%build
%configure \
	--disable-static \
	--with-pkcs11-module

%make_build

%install
%make_install

rm -fr %{buildroot}%{_datadir}/doc
