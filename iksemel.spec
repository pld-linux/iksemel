Summary:	Library for the Jabber instant-messaging IM platform
Summary(pl.UTF-8):	Biblioteka dla platformy komunikacyjnej Jabbera
Name:		iksemel
Version:	1.4
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://iksemel.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	532e77181694f87ad5eb59435d11c1ca
Patch0:		%{name}-configure.patch
URL:		http://code.google.com/p/iksemel/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iksemel is a C library for the Jabber instant-messaging IM platform.
Iksemel handles Jabber connections, parses XML, and sends and receives
Jabber messages. It works pretty good for parsing other kinds of XML,
too, if the need arises.

%description -l pl.UTF-8
Iksemel jest biblioteką C dla platformy komunikacyjnej Jabbera.
Iksemel obsługuje połączenia Jabbera, analizuje XML oraz wysyła i
odbiera komunikaty Jabbera. Działa dobrze parsując także inne rodzaje
XML-a, jeśli jest taka potrzeba.

%package devel
Summary:	Iksemel library development files
Summary(pl.UTF-8):	Pliki dla programistów używających biblioteki Iksemel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Iksemel library development files.

%description devel -l pl.UTF-8
Pliki dla programistów używających biblioteki Iksemel.

%package static
Summary:	Static Iksemel library
Summary(pl.UTF-8):	Statyczna wersja biblioteki Iksemel
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Iksemel library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki Iksemel.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/ikslint
%attr(755,root,root) %{_bindir}/iksperf
%attr(755,root,root) %{_bindir}/iksroster
%attr(755,root,root) %{_libdir}/libiksemel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiksemel.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiksemel.so
%{_libdir}/libiksemel.la
%{_includedir}/iksemel.h
%{_pkgconfigdir}/iksemel.pc
%{_infodir}/iksemel

%files static
%defattr(644,root,root,755)
%{_libdir}/libiksemel.a
