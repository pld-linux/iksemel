Summary:	Library for the Jabber instant-messaging IM platform
Summary(pl):	Biblioteka dla platformy komunikacyjnej Jabbera
Name:		iksemel
Version:	0.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://files.jabberstudio.org/iksemel/%{name}-%{version}.tar.gz
URL:		http://iksemel.jabberstudio.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iksemel is a C library for the Jabber instant-messaging IM platform.
Iksemel handles Jabber connections, parses XML, and sends and receives
Jabber messages. It works pretty good for parsing other kinds of XML,
too, if the need arises.

%description -l pl
Iksemel jest bibliotek± C dla platformy komunikacyjnej Jabbera.
Iksemel obs³uguje po³±czenia Jabbera, analizuje XML oraz wysy³a i
odbiera komunikaty Jabbera. Dzia³± dobrze parsuj±c tak¿e inne rodzaje
XML, je¶li jest taka potrzeba.

%package devel
Summary:	Iksemel library development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych biblioteki Iksemel
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Iksemel library development files.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych biblioteki Iksemel.

%package static
Summary:	Static Iksemel library
Summary(pl):	Statyczna wersja biblioteki Iksemel
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Iksemel library.

%description static -l pl
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
