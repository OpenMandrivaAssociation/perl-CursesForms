%define upstream_name    CursesForms
%define upstream_version 1.997

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Form management for Curses::Widgets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Curses/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests require human input
#make test

%install
%makeinstall_std

%files
%doc CHANGELOG LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.997.0-2mdv2011.0
+ Revision: 658522
- rebuild for updated spec-helper

* Wed Jun 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.997.0-1mdv2011.0
+ Revision: 547327
- import perl-CursesForms


* Wed Jun 09 2010 cpan2dist 1.997-1mdv
- initial mdv release, generated with cpan2dist
