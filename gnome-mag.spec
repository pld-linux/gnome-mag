Summary:	GNOME Magnifier
Summary(pl):	Lupa GNOME
Name:		gnome-mag
Version:	0.11.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.11/%{name}-%{version}.tar.bz2
# Source0-md5:	43b811541e7e1871457a019f1452aa7d
Patch0:		%{name}-am.patch
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	ORBit2-devel >= 2.12.0
BuildRequires:	at-spi-devel >= 1.6.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libbonobo-devel >= 2.8.0
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME magnifier.

%description -l pl
Lupa GNOME.

%package devel
Summary:	gnome-mag headers
Summary(pl):	Pliki nagłówkowe gnome-mag
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit2-devel >= 2.12.0
Requires:	glib2-devel >= 1:2.4.0
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	libbonobo-devel >= 2.8.0

%description devel
gnome-mag headers.

%description devel -l pl
Pliki nagłówkowe gnome-mag.

%package static
Summary:	Static gnome-mag library
Summary(pl):	Statyczna biblioteka gnome-mag
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnome-mag library.

%description static -l pl
Statyczna biblioteka gnome-mag.

%prep
%setup -q
%patch0 -p1

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
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/magnifier
%attr(755,root,root) %{_libdir}/libgnome-mag.so.*.*.*
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}
%{_datadir}/idl/%{name}-1.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-mag.so
%{_libdir}/libgnome-mag.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
