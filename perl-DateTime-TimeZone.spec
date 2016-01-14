%{?scl:%scl_package perl-DateTime-TimeZone}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-DateTime-TimeZone
Version:        1.63
Release:        5.sc1%{?dist}
Summary:        Time zone object base class and factory
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-TimeZone/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Class::Load)
BuildRequires:  %{?scl_prefix}perl(Class::Singleton) >= 1.03
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd) >= 3
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Compare)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Params::Validate) >= 0.72
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:  %{?scl_prefix}perl(Test::Output)
BuildRequires:  %{?scl_prefix}perl(Storable)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Sys::Hostname)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# not automatically detected
Requires:       %{?scl_prefix}perl(File::Compare)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

%global __requires_exclude %{__requires_exclude}|perl\\(Params::Validate\\)$|perl\\(Class::Singleton\\)$

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_requires /perl(Params::Validate)$/d
%filter_from_requires /perl(Class::Singleton)$/d
%filter_from_requires /perl(Win32/d
%endif

%if 0%{?perl_bootstrap}
# avoid circular dependencies - DateTime strictly requires DateTime::TimeZone
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(DateTime\\)
%global __requires_exclude %{__requires_exclude}|perl\\(DateTime::Duration\\)
%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_requires /perl(DateTime::Duration)/d
%filter_from_requires /perl(DateTime)/d
%endif
# perl-DateTime-TimeZone used to be bundled with perl-DateTime
# when bootstrapping, we can't require the unbundled version, so
# need to conflict with the old package
Conflicts:      %{?scl_prefix}perl-DateTime <= 1:0.7000-3.fc16
%else
# explicitly require the unbundled perl-DateTime to avoid implicit conflicts
Requires:       %{?scl_prefix}perl-DateTime >= 2:0.70-1
# and BR perl(DateTime) to enable testing
BuildRequires:  %{?scl_prefix}perl(DateTime)
BuildRequires:  %{?scl_prefix}perl(DateTime::Duration)
%endif

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_setup
%endif

%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

%prep
%setup -q -n DateTime-TimeZone-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-5
- Update filters

* Mon Nov 25 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-4
- Re-rebuild of bootstrapped packages

* Mon Nov 25 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-3
- Update filters

* Sun Nov 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-2
- Rebuilt for SCL

* Tue Oct 29 2013 Petr Pisar <ppisar@redhat.com> - 1.63-1
- update to latest upstream version - Olson 2013h

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 10 2013 Iain Arnell <iarnell@gmail.com> 1.60-1
- update to latest upstream version - Olson 2013d

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 1.59-3
- Perl 5.18 rebuild

* Wed Jun 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-2
- Specify all dependencies

* Mon Apr 22 2013 Iain Arnell <iarnell@gmail.com> 1.59-1
- update to latest upstream version - Olson 2013c

* Wed Mar 20 2013 Iain Arnell <iarnell@gmail.com> 1.58-1
- update to latest upstream version - Olson 2013b

* Sun Mar 03 2013 Iain Arnell <iarnell@gmail.com> 1.57-1
- update to latest upstream version - Olson 2013a

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Iain Arnell <iarnell@gmail.com> 1.56-1
- update to latest upstream version - still Olson 2012j

* Thu Nov 15 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.54-2
- add BR, filter duplicated requires

* Tue Nov 13 2012 Petr Pisar <ppisar@redhat.com> - 1.54-1
- update to latest upstream version - Olson 2012j

* Fri Nov 02 2012 Iain Arnell <iarnell@gmail.com> 1.52-1
- update to latest upstream version - Olson 2012h

* Thu Oct 18 2012 Petr Pisar <ppisar@redhat.com> - 1.51-1
- update to latest upstream version - Olson 2012g

* Sat Sep 15 2012 Iain Arnell <iarnell@gmail.com> 1.49-1
- update to latest upstream version - Olson 2012f

* Fri Aug 03 2012 Iain Arnell <iarnell@gmail.com> 1.48-1
- update to latest upstream version - Olson 2012e

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 1.47-1
- update to latest upstream version - Olson 2012d

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.46-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.46-2
- Perl 5.16 rebuild

* Tue Apr 03 2012 Iain Arnell <iarnell@gmail.com> 1.46-1
- update to latest upstream - Olson 2012c

* Sun Mar 04 2012 Iain Arnell <iarnell@gmail.com> 1.45-1
- update to latest upstream version

* Fri Mar 02 2012 Iain Arnell <iarnell@gmail.com> 1.44-1
- update to latest upstream version - Olson 2012b

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Iain Arnell <iarnell@gmail.com> 1.42-1
- update to latest upstream - Olson 2011n

* Tue Oct 25 2011 Iain Arnell <iarnell@gmail.com> 1.41-1
- update to latest upstream - Olson 2011m

* Tue Oct 11 2011 Iain Arnell <iarnell@gmail.com> 1.40-1
- update to latest upstream - Olson 2011l

* Tue Sep 27 2011 Iain Arnell <iarnell@gmail.com> 1.39-1
- update to latest upstream - Olson 2011k

* Wed Sep 14 2011 Iain Arnell <iarnell@gmail.com> 1.37-1
- update to latest upstream - Olson 2011j

* Tue Aug 30 2011 Iain Arnell <iarnell@gmail.com> 1.36-1
- update to latest upstream - Olson 2011i

* Thu Aug 18 2011 Iain Arnell <iarnell@gmail.com> 1.35-3
- rebuild against unbunled perl-DateTime

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 1.35-2
- additional explicit (build)requires for core modules

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 1.35-1
- Specfile autogenerated by cpanspec 1.78.
- Add bootstrapping logic
