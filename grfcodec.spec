%define release	1

Name:           grfcodec
Version:        1.0.0
Release:        %mkrel %{release}
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:          Development/Other
License:        GPLv2+
URL:            http://www.ttdpatch.net/grfcodec/
Source:		http://gb.binaries.openttd.org/binaries/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  boost-devel
BuildRequires:  upx

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep
%setup -q -n %{name}-%{version}-source

%build
%make CFLAGAPP="%{optflags}" LDOPT="%{ldflags}"

%install
rm -rf %{buildroot}
for file in grfcodec grfdiff grfmerge grfid; do
  install -D -m 755 $file %{buildroot}%{_bindir}/$file
  install -D -m 644 docs/$file.1 %{buildroot}%{_mandir}/man1/$file.1
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%{_bindir}/*
%{_mandir}/man1/gr*
