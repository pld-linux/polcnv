Summary:	Small program to change text encoding (eg CP852 to ISO8859-2)
Summary(pl):	Programik do konwersji ogonków (np. CP852 do ISO-8859-2)
Name:		polcnv
Version:	2.2
Release:	2
License:	GPL
Vendor:		Jerzy Sobczyk <J.Sobczyk@ia.pw.edu.pl>
Group:		Applications/Text
Source0:	%{name}.%{version}.tar.gz
# Source0-md5:	de9658abecb1ec7c92af22f89ed97b83
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polcnv converts polish letters.

%description -l pl
Polcnv konwertuje ogonki w plikach tekstowych.

%prep
%setup -q -n %{name}.%{version}

%build
CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CZYTAJ.TO Copyright DISCLAIMER READ.ME
%attr(755,root,root) %{_bindir}/%{name}
