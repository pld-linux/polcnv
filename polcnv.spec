Summary:	Small program to change text encoding (eg CP852 to ISO8859-2)
Summary(pl):	Programik do konwersji ogonków (np. CP852 do ISO-8859-2) 
Name:		polcnv
Version:	2.2
Release:	1
License:	GPL
Vendor:		J.Sobczyk@ia.pw.edu.pl
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Source0:	%{name}.%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polcnv converts polish letters.

%description -l pl
Polcnv konwertuje ogonki w plikach tekstowych.

%prep
%setup -q -n %{name}.%{version}

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf CZYTAJ.TO Copyright DISCLAIMER READ.ME

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/%{name}
