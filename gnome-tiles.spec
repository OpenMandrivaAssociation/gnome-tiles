Summary: Desktop Background Images for GNOME
Name: gnome-tiles
Version: 1
Release: 9mdk
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

