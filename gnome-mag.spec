Summary:	GNOME Magnifier
Summary(pl):	Lupa GNOME
Name:		gnome-mag
Version:	0.10.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	bcfd31d2d56d399b4f2087eaf3a8fc04
Patch0:		%{name}-am.patch
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	ORBit2-devel >= 2.8.0
BuildRequires:	at-spi-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2.2.3
BuildRequires:	intltool >= 0.25
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME magnifier.

%description -l pl
Lupa GNOME.

%package devel
Summary:	gnome-mag headers
Summary(pl):	Pliki nag³ówkowe gnome-mag
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	ORBit2-devel >= 2.8.0
Requires:	glib2-devel >= 2.2.0
Requires:	libbonobo-devel >= 2.4.0

%description devel
gnome-mag headers.

%description devel -l pl
Pliki nag³ówkowe gnome-mag.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
