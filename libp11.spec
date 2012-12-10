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


%changelog
* Wed Jan 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.8-1
+ Revision: 756594
- version update 0.2.8

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-3mdv2011.0
+ Revision: 609769
- rebuild

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 0.2.7-2mdv2010.1
+ Revision: 536665
- rebuild

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.2.7-1mdv2010.1
+ Revision: 482737
- Update to new version 0.2.7 (new major)

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.2.4-3mdv2010.0
+ Revision: 438731
- rebuild

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 0.2.4-2mdv2009.0
+ Revision: 259231
- obsolete old libname
- correct libname

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2009.0
+ Revision: 259229
- New version 0.2.4
- fix libname and devel package name
- Rename to libp11

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-3mdv2009.0
+ Revision: 250390
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 05 2007 Andreas Hasenack <andreas@mandriva.com> 0.2.3-1mdv2008.1
+ Revision: 106181
- updated to version 0.2.3

