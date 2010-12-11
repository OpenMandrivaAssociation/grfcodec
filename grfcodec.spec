Name:		grfcodec
Version:	5.1.0
Release:	%mkrel 1
Summary:	A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:		Development/Other
License:	GPLv2+
URL:		http://www.ttdpatch.net/grfcodec/
Source:		http://gb.binaries.openttd.org/binaries/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz
Patch0:		grfcodec-5.1.0-fix_linking_order.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	boost-devel
Obsoletes:	nforenum < 5.0.0
Provides:	nforenum = %{version}-%{release}

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p0

#build time options
cat << EOF >> Makefile.local
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc bundle/docs/*.txt
%{_bindir}/*
%{_mandir}/man1/gr*
%{_mandir}/man1/nforenum.*
