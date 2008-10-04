Summary:	GNOME Magnifier
Summary(pl.UTF-8):	Lupa GNOME
Name:		gnome-mag
Version:	0.15.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-mag/0.15/%{name}-%{version}.tar.bz2
# Source0-md5:	77c099335ff2d913ac813e79f127acc0
# http://bugzilla.gnome.org/show_bug.cgi?id=554162
Patch0:		%{name}-use-pyexecdir.patch
URL:		http://live.gnome.org/GnomeMag
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	ORBit2-devel >= 1:2.14.9
BuildRequires:	at-spi-devel >= 1.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-desktop-devel >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libbonobo-devel >= 2.24.0
BuildRequires:	libcolorblind-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-desktop-applet
BuildRequires:	python-gnome-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXfixes-devel
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME magnifier.

%description -l pl.UTF-8
Lupa GNOME.

%package apidocs
Summary:	gnome-mag API documentation
Summary(pl.UTF-8):	Dokumentacja API gnome-mag
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gnome-mag API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gnome-mag.

%package devel
Summary:	gnome-mag headers
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-mag
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit2-devel >= 1:2.14.9
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	libbonobo-devel >= 2.24.0

%description devel
gnome-mag headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe gnome-mag.

%package static
Summary:	Static gnome-mag library
Summary(pl.UTF-8):	Statyczna biblioteka gnome-mag
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnome-mag library.

%description static -l pl.UTF-8
Statyczna biblioteka gnome-mag.

%package -n gnome-applet-colorblind
Summary:	Colorblind applet for GNOME panel
Summary(pl.UTF-8):	Aplet colorblind dla panelu GNOME
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2
Requires:	python-gnome-desktop-applet
Requires:	python-gnome-gconf
Requires:	python-gnome-ui
Requires:	python-gnome-vfs
Requires:	python-pygtk-glade

%description -n gnome-applet-colorblind
Controls image filters for colorblind people.

%description -n gnome-applet-colorblind -l pl.UTF-8
Obsługa filtrów obrazu dla osób ze ślepotą kolorów.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf} -I m4
%{__autoheader}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	referencedir=%{_gtkdocdir}/%{name}

# no *.la for orbit modules
rm -f $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/*.{la,a}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/colorblind/{keybinder,osutils}/*.{la,a}

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n gnome-applet-colorblind
%gconf_schema_install colorblind-applet.schemas
%update_icon_cache hicolor

%preun -n gnome-applet-colorblind
%gconf_schema_uninstall colorblind-applet.schemas

%postun -n gnome-applet-colorblind
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/magnifier
%attr(755,root,root) %{_libdir}/libgnome-mag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-mag.so.2
%attr(755,root,root) %{_libdir}/orbit-2.0/GNOME_Magnifier_module.so
%{_mandir}/man1/magnifier.1*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}
%{_datadir}/idl/%{name}-1.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-mag.so
%{_libdir}/libgnome-mag.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/gnome-mag-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-mag.a

%files -n gnome-applet-colorblind
%defattr(644,root,root,755)
%dir %{_libdir}/colorblind-applet
%attr(755,root,root) %{_libdir}/colorblind-applet/colorblind-applet
%dir %{py_sitedir}/colorblind
%{py_sitedir}/colorblind/*.py[co]
%dir %{py_sitedir}/colorblind/keybinder
%attr(755,root,root) %{py_sitedir}/colorblind/keybinder/_keybinder.so
%{py_sitedir}/colorblind/keybinder/*.py[co]
%dir %{py_sitedir}/colorblind/osutils
%attr(755,root,root) %{py_sitedir}/colorblind/osutils/_osutils.so
%{py_sitedir}/colorblind/osutils/*.py[co]
%dir %{py_sitedir}/colorblind/ui
%{py_sitedir}/colorblind/ui/*.py[co]
%{_datadir}/colorblind
%{_iconsdir}/hicolor/*/*/*
%{_sysconfdir}/gconf/schemas/colorblind-applet.schemas
