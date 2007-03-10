Summary:	GNOME Magnifier
Summary(pl.UTF-8):	Lupa GNOME
Name:		gnome-mag
Version:	0.14.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-mag/0.14/%{name}-%{version}.tar.bz2
# Source0-md5:	db9660614f7948a12b18464683a5704f
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	ORBit2-devel >= 1:2.14.7
BuildRequires:	at-spi-devel >= 1.17.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libbonobo-devel >= 2.17.92
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libbonobo >= 2.17.92
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
Requires:	ORBit2-devel >= 1:2.14.7
Requires:	gtk+2-devel >= 2:2.10.9
Requires:	libbonobo-devel >= 2.17.92

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
%{__aclocal}
%{__automake}
%{__autoconf}
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
