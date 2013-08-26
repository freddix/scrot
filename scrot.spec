Summary:	Simple command-line screenshot utility for X
Name:		scrot
Version:	0.8
Release:	1
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	ccae904d225609571bdd3b03445c1e88
Patch0:		%{name}-ac.patch
URL:		http://scrot.sourcearchive.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giblib-devel
BuildRequires:	imlib2-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple command-line screenshot utility for X.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS TODO
%attr(755,root,root) %{_bindir}/scrot
%{_mandir}/man1/scrot.1*

