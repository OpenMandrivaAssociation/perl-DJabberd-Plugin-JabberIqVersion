%define realname   DJabberd-Plugin-JabberIqVersion

Name:		perl-%{realname}
Version:	0.40
Release:	6
License:	Artistic or GPL
Group:		Development/Perl
Summary:	Add support for "XEP 0092, Software version" to DJabberd
Url:		http://search.cpan.org/dist/%{realname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DJabberd/DJabberd-Plugin-JabberIqVersion-%{version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(DJabberd)
BuildArch:	noarch

%description
DJabberd::Plugin::JabberIqVersion add support for "XEP 0092, Software version" 
to DJabberd, a xmpp server framework.

%prep
%setup -q -n DJabberd-Plugin-JabberIqVersion-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# disabled, test seems to requires a update with new perl to work 
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/DJabberd/*
%{_mandir}/man3/*



%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.40-3mdv2011.0
+ Revision: 681364
- mass rebuild

* Sun Nov 22 2009 Michael Scherer <misc@mandriva.org> 0.40-2mdv2011.0
+ Revision: 469101
- disable test, as they prevent the build. ( upstream has been notified and is ok )
- import perl-DJabberd-Plugin-JabberIqVersion

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Sep 20 2007 Michael Scherer <misc@mandriva.org> 0.40-1mdv2008.0
- First Mandriva package
