%{?scl:%scl_package perl-DateTime-TimeZone}

Name:           %{?scl_prefix}perl-DateTime-TimeZone
Version:        2.01
Release:        3%{?dist}
Summary:        Time zone object base class and factory
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-TimeZone/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
# Parse local time zone definition from /etc/localtime as before giving up,
# bug #1135981, CPAN RT#55029
Patch0:         DateTime-TimeZone-2.01-Parse-etc-localtime-by-DateTime-TimeZone-Tzfile.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Runtime
BuildRequires:  %{?scl_prefix}perl(Class::Singleton) >= 1.03
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd) >= 3
# Unused BuildRequires:  %{?scl_prefix}perl(DateTime)
# Unused BuildRequires:  %{?scl_prefix}perl(DateTime::Duration)
# Unused BuildRequires:  %{?scl_prefix}perl(DateTime::TimeZone::Tzfile)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
# Unused BuildRequires:  %{?scl_prefix}perl(File::Compare)
# Unused BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
# Unused BuildRequires:  %{?scl_prefix}perl(List::Util) >= 1.33
BuildRequires:  %{?scl_prefix}perl(Module::Runtime)
BuildRequires:  %{?scl_prefix}perl(Params::Validate) >= 0.72
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(Try::Tiny)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests only
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Storable)
BuildRequires:  %{?scl_prefix}perl(Sys::Hostname)
BuildRequires:  %{?scl_prefix}perl(Test::Fatal)
# Test::Mojibake not used
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.96
BuildRequires:  %{?scl_prefix}perl(Test::Requires)
# Optional tests
%if !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::Output)
BuildRequires:  %{?scl_prefix}perl(Test::Taint)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(File::Basename)
Requires:       %{?scl_prefix}perl(File::Compare)
Requires:       %{?scl_prefix}perl(File::Find)
# Require optional DateTime::TimeZone::Tzfile to work in mock after tzdata
# upgrade, bug #1135981
Requires:       %{?scl_prefix}perl(DateTime::TimeZone::Tzfile)


%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Params::Validate)$/d
%filter_from_requires /^%{?scl_prefix}perl(Class::Singleton)$/d
# avoid circular dependencies - DateTime strictly requires DateTime::TimeZone
%if 0%{?perl_bootstrap}
%filter_from_requires /^%{?scl_prefix}perl(DateTime)/d
%filter_from_requires /^%{?scl_prefix}perl(DateTime::Duration)/d
%endif
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\((Params::Validate|Class::Singleton)\\)$
# avoid circular dependencies - DateTime strictly requires DateTime::TimeZone
%if 0%{?perl_bootstrap}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(DateTime(::Duration)?\\)
%endif
%endif

%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

%prep
%setup -q -n DateTime-TimeZone-%{version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jul 24 2016 Petr Pisar <ppisar@redhat.com> - 2.01-3
- Rebuild without bootstrap

* Mon Jul 18 2016 Petr Pisar <ppisar@redhat.com> - 2.01-2
- SCL

* Mon Jul 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-1
- 2.01 bump (2016f Olson database)

* Thu Jun 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1
- 2.00 bump

* Tue Jun 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-1
- 1.99 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-2
- Perl 5.24 rebuild

* Fri Apr 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-1
- 1.98 bump (2016d Olson database)

* Thu Mar 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.97-1
- 1.97 bump (2016c Olson database)

* Wed Mar 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-1
- 1.96 bump (2016b Olson database)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Petr Šabata <contyk@redhat.com> - 1.95-1
- 1.95 bump (2016a Olson database)

* Thu Oct 22 2015 Petr Pisar <ppisar@redhat.com> - 1.94-1
- 1.94 bump (2015g Olson database)

* Wed Aug 12 2015 Petr Šabata <contyk@redhat.com> - 1.93-1
- 1.93 bump, tzdata updated

* Tue Jun 23 2015 Petr Šabata <contyk@redhat.com> - 1.92-1
- 1.92 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Petr Šabata <contyk@redhat.com> - 1.91-1
- 1,91 bump, tzdata updated

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-2
- Perl 5.22 rebuild

* Fri May 15 2015 Petr Šabata <contyk@redhat.com> - 1.90-1
- 1.90 bump
- The `compile-all' test is now author-only, cutting the dep list somewhat
- Drop the old filters; I don't think we need them anymore

* Mon Apr 27 2015 Petr Šabata <contyk@redhat.com> - 1.88-1
- 1.88 bump, timezone data updated

* Tue Apr 21 2015 Petr Šabata <contyk@redhat.com> - 1.87-1
- 1.87 bump, timezone data updated

* Mon Mar 23 2015 Petr Šabata <contyk@redhat.com> - 1.86-1
- 1.86 bump, timezone data updated

* Tue Feb 03 2015 Petr Pisar <ppisar@redhat.com> - 1.85-1
- 1.85 bump

* Thu Jan 29 2015 Petr Pisar <ppisar@redhat.com> - 1.83-3
- Rebase patch to remove a spurious back-up file

* Fri Jan 16 2015 Petr Pisar <ppisar@redhat.com> - 1.83-2
- Fix dependency filtering

* Wed Jan 07 2015 Petr Šabata <contyk@redhat.com> - 1.83-1
- 1.83 bump, tests enhanced for 5.21
- Dropping F16-era conflicts

* Tue Nov 25 2014 Petr Šabata <contyk@redhat.com> - 1.81-1
- 1.81 bump, only removes Win32 tests

* Tue Nov 18 2014 Petr Šabata <contyk@redhat.com> - 1.80-1
- 1.80 bump, based on version 2014j of the Olson database

* Mon Nov 03 2014 Petr Pisar <ppisar@redhat.com> - 1.76-1
- 1.76 bump

* Wed Oct 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-1
- 1.75 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.74-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.74-3
- Perl 5.20 rebuild

* Tue Sep 02 2014 Petr Pisar <ppisar@redhat.com> - 1.74-2
- Parse local time zone definition from /etc/localtime (bug #1135981)

* Tue Sep 02 2014 Petr Pisar <ppisar@redhat.com> - 1.74-1
- 1.74 bump (updates to 2014g Olson database)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-2
- Perl 5.20 rebuild

* Thu Aug 07 2014 Petr Pisar <ppisar@redhat.com> - 1.73-1
- 1.73 bump

* Mon Jun 30 2014 Petr Pisar <ppisar@redhat.com> - 1.71-1
- update to latest upstream version - Olson 2014e

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Petr Pisar <ppisar@redhat.com> - 1.69-1
- update to latest upstream version - IANA 2014c database

* Mon Feb 10 2014 Paul Howarth <paul@city-fan.org> - 1.64-1
- Update to 1.64
  - Under taint mode, DateTime::TimeZone->new( name => 'local' ) could die
    depending on the method used to find the local time zone name, and the
    resulting variable would often be tainted; we now untaint all names before
    attempting to load them (CPAN RT#92631)

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
