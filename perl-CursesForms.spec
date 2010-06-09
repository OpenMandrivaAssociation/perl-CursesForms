%define upstream_name    CursesForms
%define upstream_version 1.997

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Form management for Curses::Widgets
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Curses/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Curses)
BuildRequires: perl(Curses::Widgets)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Curses::Forms provide a simple framework for OO forms. The Forms module
itself provides a basic class from which extended forms can be derived, or,
it can be used as-is to control forms populated with widgets. More
specialised forms are also available under *Curses::Forms::Dialog*.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests require human input
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


