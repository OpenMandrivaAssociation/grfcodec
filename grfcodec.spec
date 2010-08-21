Name:		grfcodec
Version:	1.0.0
Release:	%mkrel 2
Summary:	A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:		Development/Other
License:	GPLv2+
URL:		http://www.ttdpatch.net/grfcodec/
Source:		http://gb.binaries.openttd.org/binaries/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz
Patch0:		grfcodec-1.0.0-fix_linking_order.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	boost-devel

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p0

#fix build time flags
sed -i -e 's|-D_FORTIFY_SOURCE=2||' Makefile
sed -i -e 's|FLAGS += -Wall .*|FLAGS += %{optflags}\nLDOPT = %{ldflags}|' Makefile

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
