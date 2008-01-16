Summary:	Library for the Jabber instant-messaging IM platform
Summary(pl.UTF-8):	Biblioteka dla platformy komunikacyjnej Jabbera
Name:		iksemel
Version:	1.2
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://files.jabberstudio.org/iksemel/%{name}-%{version}.tar.gz
# Source0-md5:	82e7c8fdb6211839246b788c040a796b
URL:		http://iksemel.jabberstudio.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	libtool
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

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
