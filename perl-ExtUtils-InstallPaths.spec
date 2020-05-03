#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	InstallPaths
Summary:	ExtUtils::InstallPaths - Build.PL install path logic made easy
Summary(pl.UTF-8):	ExtUtils::InstallPaths - ułatwienie logiki ścieżek instalacyjnych Build.PL
Name:		perl-ExtUtils-InstallPaths
Version:	0.012
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a8d66aab1ffec98ea260faf03ac612b
URL:		https://metacpan.org/release/ExtUtils-InstallPaths
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(File::Spec::Functions) >= 0.83
BuildRequires:	perl-ExtUtils-Config >= 0.002
BuildRequires:	perl-File-Temp
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to make install path resolution as easy as possible.

When you want to install a module, it needs to figure out where to
install things. The nutshell version of how this works is that default
installation locations are determined from ExtUtils::Config, and they
may be individually overridden by using the install_path attribute.
An install_base attribute lets you specify an alternative installation
root like /home/foo and prefix does something similar in a rather
different (and more complicated) way. destdir lets you specify a
temporary installation directory like /tmp/install in case you want to
create bundled-up installable packages.

%description -l pl.UTF-8
Ten moduł próbuje ułatwić rozwiązywanie ścieżek instalacyjnych na
tyle, na ile to możliwe.

Aby zainstalować moduł, musi on określić, gdzie instalować
poszczególne elementy. W skrócie, domyślne ścieżki instalacyjne są
określane z ExtUtils::Config i mogą być indywidualnie nadpisywane przy
użyciu atrybutu install_path. Atrybut install_base pozwala na
określenie alternatywnego korzenia dzewa instalacji, np. /home/foo, a
prefix robi coś podobnego w nieco inny (i bardziej skomplikowany)
sposób. destdir pozwala określić tymczasowy katalog instalacyjny, na
przykład /tmp/install, aby utworzyć pakiety instalacyjne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/ExtUtils/InstallPaths.pm
%{_mandir}/man3/ExtUtils::InstallPaths.3pm*
