Summary: Small program to change text encoding (eg CP852 to ISO8859-2)
Summary(pl): Programik do konwersji ogonków (np. CP852 do ISO-8859-2) 
Name: polcnv
Version: 2.2
Release: 1
Copyright: GPL
Group: Utilities/Text
Group(pl): Narzêdzia/Tekst
Source: %{name}.%{version}.tar.gz
#URL: 
#Requires: 
BuildRoot: /tmp/%{name}-%{version}-root

%description
Polcnv converts polish letters

%description -l pl
Polcnv konwertuje ogonki w plikach tekstowych

%changelog

%prep

%setup -q -n %{name}.%{version}

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS"
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}
install -d $RPM_BUILD_ROOT/usr/bin
install CZYTAJ.TO Copyright DISCLAIMER READ.ME $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}
install %{name} $RPM_BUILD_ROOT/usr/bin

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/%{name}
%doc CZYTAJ.TO Copyright DISCLAIMER READ.ME 
