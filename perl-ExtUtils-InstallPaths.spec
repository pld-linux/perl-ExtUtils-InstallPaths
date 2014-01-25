#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	InstallPaths
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils::InstallPaths - Build.PL install path logic made easy
#Summary(pl.UTF-8):	
Name:		perl-ExtUtils-InstallPaths
Version:	0.010
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f0b00cc6c04653588a6298fa1f16c07f
URL:		http://search.cpan.org/dist/ExtUtils-InstallPaths/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-Config >= 0.002
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

# %description -l pl.UTF-8
# TODO

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
%doc Changes INSTALL README
%{perl_vendorlib}/ExtUtils/InstallPaths.pm
%{_mandir}/man3/*
