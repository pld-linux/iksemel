Summary:	Library for the Jabber instant-messaging IM platform
Name:		iksemel
Version:	0.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://files.jabberstudio.org/iksemel/%{name}-%{version}.tar.gz
URL:		http://iksemel.jabberstudio.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iksemel is a C library for the Jabber instant-messaging IM platform.
Iksemel handles Jabber connections, parses XML, and sends and receives
Jabber messages. It works pretty good for parsing other kinds of XML, too,
if the need arises.

%package devel
Summary:	Iksemel library development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Iksemel library development files.
%package static

Summary:	Static Iksemel library
Summary(pl):	Wersja statyczna biblioteki Jabberoo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Iksemel library.

%prep
%setup -q

%build
%{__libtoolize}
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
