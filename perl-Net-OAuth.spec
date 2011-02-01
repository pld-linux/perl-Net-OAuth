#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Net
%define		pnam	OAuth
%include	/usr/lib/rpm/macros.perl
Summary:	Net::OAuth - OAuth protocol support
#Summary(pl.UTF-8):
Name:		perl-Net-OAuth
Version:	0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KG/KGRENNAN/Net-OAuth-%{version}.tar.gz
# Source0-md5:	6b7a854c8c848ba08e5e0703bdfd8c95
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Net-OAuth/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor >= 0.31
BuildRequires:	perl-Class-Data-Inheritable >= 0.06
BuildRequires:	perl-Digest-HMAC >= 1.01
BuildRequires:	perl-Digest-SHA1 >= 2.12
BuildRequires:	perl-Test-Warn >= 0.21
BuildRequires:	perl-URI >= 3.28
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An OAuth message is a set of key-value pairs. The following message
types are supported:
- Requests
- Responses

Each OAuth message type has one or more required parameters, zero or
more optional parameters, and most allow arbitrary parameters.

All OAuth requests must be signed by the Consumer. Responses from the
Service Provider, however, are not signed.

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
%doc Changes README
%{perl_vendorlib}/Net/*.pm
%{perl_vendorlib}/Net/OAuth
%{_mandir}/man3/*
