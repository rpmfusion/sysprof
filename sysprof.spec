Name:           sysprof      
Version:        1.0.12
Release:        2%{?dist}
Summary:        Sysprof is a sampling CPU profiler
Group:          Development/System
License:        GPLv2+
URL:            http://www.daimi.au.dk/~sandmann/sysprof/
Source0:        http://www.daimi.au.dk/~sandmann/sysprof/sysprof-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source1:        sysprof.desktop

# kmod related stuff
Provides:       sysprof-kmod-common = %{version}
Requires:       kmod-%{name} >= %{version}

BuildRequires:  gtk2-devel => 2.6
BuildRequires:  libglade2-devel
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils

ExclusiveArch:  i386 x86_64

%description
Sysprof is a sampling CPU profiler for Linux that uses a kernel module
to profile the entire system, not just a single application.
Sysprof handles shared libraries and applications do not need to be
recompiled. In fact they don't even have to be restarted.

%prep
%setup -q


%build
%configure --disable-kernel-module
make %{?_smp_mflags}


%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}

desktop-file-install --vendor fedora                            \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --add-category X-Fedora                                 \
        %{SOURCE1}


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog
%{_bindir}/sysprof
%{_datadir}/pixmaps/sysprof-icon.png
%dir %{_datadir}/sysprof
%{_datadir}/sysprof/sysprof-icon.png
%{_datadir}/sysprof/sysprof.glade
%{_datadir}/applications/*.desktop

%changelog
* Thu Feb 19 2009 Thorsten Leemhuis <fedora leemhuis info> - 1.0.12-2
- make it excludearch i386 instead of ix86, as the latter confuses plague

* Wed Feb 11 2009 Gianluca Sforna <giallu gmail com> - 1.0.12-1
- version update to 1.0.12

* Wed Apr  9 2008 Gianluca Sforna <giallu gmail com> - 1.0.9-1
- version update to 1.0.9

* Tue Aug 28 2007 Gianluca Sforna <giallu gmail com> 1.0.8-2
- update License field

* Thu Dec 21 2006 Gianluca Sforna <giallu gmail com> 1.0.8-1
- version update to 1.0.8

* Tue Nov 21 2006 Gianluca Sforna <giallu gmail com> 1.0.7-1
- version update to 1.0.7

* Wed Nov  1 2006 Gianluca Sforna <giallu gmail com> 1.0.5-1
- version update

* Sun Oct  8 2006 Gianluca Sforna <giallu gmail com> 1.0.3-6
- better to use ExclusiveArch %{ix86} (thanks Ville)

* Thu Oct  5 2006 Gianluca Sforna <giallu gmail com> 1.0.3-5
- add ExclusiveArch to match sysprof-kmod supported archs

* Tue Oct  2 2006 Gianluca Sforna <giallu gmail com> 1.0.3-4
- add .desktop file

* Fri Sep 30 2006 Gianluca Sforna <giallu gmail com> 1.0.3-3
- versioned Provides
- add BR: binutils-devel

* Fri Sep 29 2006 Gianluca Sforna <giallu gmail com> 1.0.3-2
- own sysprof directory

* Thu Jun 22 2006 Gianluca Sforna <giallu gmail com> 1.0.3-1
- version update
- use standard %%configure macro

* Sun May 14 2006 Gianluca Sforna <giallu gmail com> 1.0.2-1
- Initial Version
