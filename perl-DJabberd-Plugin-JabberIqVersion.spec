%define realname   DJabberd-Plugin-JabberIqVersion

Name:		perl-%{realname}
Version:    0.40
Release:    %mkrel 2
License:	Artistic or GPL
Group:		Development/Perl
Summary:    Add support for "XEP 0092, Software version" to DJabberd
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/DJabberd/DJabberd-Plugin-JabberIqVersion-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(DJabberd)
BuildArch: noarch
%description
DJabberd::Plugin::JabberIqVersion add support for "XEP 0092, Software version" 
to DJabberd, a xmpp server framework.

%prep
%setup -q -n DJabberd-Plugin-JabberIqVersion-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# disabled, test seems to requires a update with new perl to work 
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DJabberd/*
%{_mandir}/man3/*

