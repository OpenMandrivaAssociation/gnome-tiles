Summary: Desktop Background Images for GNOME
Name: gnome-tiles
Version: 1
Release: 14
License: LGPL
Group: Graphical desktop/GNOME
Source: gnome-tiles-1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArchitectures: noarch
URL: http://www.gnome.org/

%description
If you use GNOME you can use these images to spruce up your background.
Of course, you can you use it for with another Window Manager.

%prep

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds/gnome-tiles
cd $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds 
bzcat %{SOURCE0}|tar xf -

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_datadir}/pixmaps/backgrounds/gnome-tiles



%changelog
* Sat Aug 06 2011 Götz Waschk <waschk@mandriva.org> 1-13mdv2012.0
+ Revision: 693427
- rebuild

* Thu Jul 30 2009 Frederic Crozat <fcrozat@mandriva.com> 1-12mdv2011.0
+ Revision: 404687
- Rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1-11mdv2009.0
+ Revision: 246469
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1-9mdv2008.1
+ Revision: 126028
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel


* Tue Jan 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1-9mdk
- Rebuild

* Fri Sep 10 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1-8mdk
- Rebuild

* Mon Aug 18 2003 Lenny Cartier <lenny@mandrakesoft.com> 1-7mdk
- remove provides & obsoletes

* Fri Feb 14 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 1-6mdk
- Rebuild

