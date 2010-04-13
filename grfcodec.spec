%define rev	r2306
%define release	1

Name:           grfcodec
Version:        0.9.10
Release:        %mkrel %{rev}.%{release}
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:          Development/Other
License:        GPLv2+
URL:            http://www.ttdpatch.net/grfcodec/
Source0:        http://binaries.openttd.org/extra/%{name}/%{rev}/%{name}-%{rev}-source.tar.bz2
Patch0:		grfcodec-r2306-fix_str_fmt.patch
# don't pass -O3 to gcc
Patch1:		grfcodec-r2306-fix_cflags.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  boost-devel
BuildRequires:  upx

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep
%setup -q -n %{name}-%{rev}
%patch0 -p0
%patch1 -p1

for f in *.txt; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv 
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
%make CFLAGAPP="%{optflags}" LDOPT="%{ldflags}"

%install
rm -rf %{buildroot}
for file in grfcodec grfdiff grfmerge; do
  install -D -m 755 $file %{buildroot}%{_bindir}/$file
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changelog COPYING grfcodec.txt grftut.txt grf.txt todo.txt
%{_bindir}/*
