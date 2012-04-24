Name:		grfcodec
Version:	6.0.0
Release:	%mkrel 1
Summary:	A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:		Development/Other
License:	GPLv2+
URL:		http://www.ttdpatch.net/grfcodec/
Source:		http://gb.binaries.openttd.org/binaries/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz
Patch0:		grfcodec-6.0.0-fix_linking_order.patch
BuildRequires:	boost-devel
BuildRequires:	png-devel
Obsoletes:	nforenum < 5.0.0
Provides:	nforenum = %{version}-%{release}

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep
%setup -q
%patch0 -p0

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

