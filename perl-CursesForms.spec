%define upstream_name    CursesForms
%define upstream_version 1.997
Name:		perl-%{upstream_name}
Version:	1.997
Release:	20

Summary:	Form management for Curses::Widgets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/C/CO/CORLISS/CursesForms-1.997.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Curses)
BuildRequires:	perl(Curses::Widgets)

BuildArch:	noarch

%description
Curses::Forms provide a simple framework for OO forms. The Forms module
itself provides a basic class from which extended forms can be derived, or,
it can be used as-is to control forms populated with widgets. More
specialised forms are also available under *Curses::Forms::Dialog*.

%prep
%setup -q -n CursesForms-1.997

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
# soft: do not fail package on test failures
set +e
# tests require human input
#make test || :

%install
%makeinstall_std

%files
%doc CHANGELOG LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

