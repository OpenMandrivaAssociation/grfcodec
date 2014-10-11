Name:		grfcodec
Version:	6.0.4
Release:	1
Summary:	A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:		Development/Other
License:	GPLv2+
URL:		http://www.ttdpatch.net/grfcodec/
Source0:	http://gb.binaries.openttd.org/binaries/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz
BuildRequires:	boost-devel
BuildRequires:	png-devel
Obsoletes:	nforenum < 5.0.0
Provides:	nforenum = %{version}-%{release}

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep
%setup -q

#build time options
%__cat << EOF >> Makefile.local
V=1
CXXFLAGS=%{optflags}
LDOPT=%{ldflags}
STRIP=true
DO_NOT_INSTALL_LICENSE=1
DO_NOT_INSTALL_DOCS=1
DO_NOT_INSTALL_CHANGELOG=1
prefix=%{_prefix}
EOF

%build
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%doc bundle/docs/*.txt
%{_bindir}/*
%{_mandir}/man1/gr*
%{_mandir}/man1/nforenum.*



%changelog
* Tue Apr 24 2012 Andrey Bondrov <abondrov@mandriva.org> 6.0.0-1mdv2012.0
+ Revision: 793108
- New version 6.0.0, update patch 0

* Sun Mar 20 2011 Jani Välimaa <wally@mandriva.org> 5.1.1-1
+ Revision: 647137
- new version 5.1.1

* Thu Dec 23 2010 Jani Välimaa <wally@mandriva.org> 5.1.0-2.r818.2mdv2011.0
+ Revision: 624052
- BR png-devel

* Thu Dec 23 2010 Jani Välimaa <wally@mandriva.org> 5.1.0-2.r818.1mdv2011.0
+ Revision: 624009
- use latest nightly build

* Sat Dec 11 2010 Jani Välimaa <wally@mandriva.org> 5.1.0-1mdv2011.0
+ Revision: 620574
- new version 5.1.0
- redo P0

* Tue Oct 19 2010 Jani Välimaa <wally@mandriva.org> 5.0.0-2mdv2011.0
+ Revision: 586844
- fix obsoletes

* Tue Oct 19 2010 Jani Välimaa <wally@mandriva.org> 5.0.0-1mdv2011.0
+ Revision: 586815
- new version 5.0.0
- rediff patch0
- nforenum is now part of grfcodec
- improve .spec (thanks goes to Fedora)

* Sat Aug 21 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 571781
- add patch to fix linking order
- fix build flags
- disable upx-ing the binaries
- fix install

* Sun Aug 15 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 569945
- new version 1.0.0

* Mon Aug 09 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-0.RC1.1mdv2011.0
+ Revision: 568204
- new version 1.0.0 RC1
- drop unneeded patches
- install man files

* Tue Apr 13 2010 Jani Välimaa <wally@mandriva.org> 0.9.10-r2306.1mdv2010.1
+ Revision: 534608
- import grfcodec


