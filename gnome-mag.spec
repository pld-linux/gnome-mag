Summary:	GNOME Magnifier
Summary(pl.UTF-8):	Lupa GNOME
Name:		gnome-mag
Version:	0.15.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-mag/0.15/%{name}-%{version}.tar.bz2
# Source0-md5:	a297f2b2fae4cd0cde2a30bfacc4c380
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 1:2.14.9
BuildRequires:	at-spi-devel >= 1.20.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonobo-devel >= 2.20.0
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libbonobo >= 2.20.0
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
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libbonobo-devel >= 2.20.0

%description devel
gnome-mag headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe gnome-mag.

%package static
Summary:	Static gnome-mag library
Summary(pl.UTF-8):	Statyczna biblioteka gnome-mag
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnome-mag library.

%description static -l pl.UTF-8
Statyczna biblioteka gnome-mag.

%prep
%setup -q

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

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/magnifier
%attr(755,root,root) %{_libdir}/libgnome-mag.so.*.*.*
%attr(755,root,root) %{_libdir}/orbit-2.0/*.so*
%{_mandir}/man1/magnifier.1*
%{_libdir}/bonobo/servers/*
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
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
