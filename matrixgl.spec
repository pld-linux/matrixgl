Summary:	3D screensaver
Summary(pl.UTF-8):	Trójwymiarowy wygaszacz ekranu
Name:		matrixgl
Version:	2.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/matrixgl/%{name}-%{version}-src.tar.gz
# Source0-md5:	f248848f4918a3b7c75d7b74d75830f4
Patch0:		%{name}-xscreensaver.patch
URL:		http://sourceforge.net/projects/matrixgl/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xscreensaver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matrixgl is a 3D screensaver for (partially for KDE) based on "The
Matrix Reloaded". It supports widescreen setups.

%description -l pl.UTF-8
Matrixgl to trójwymiarowy wygaszacz ekranu (częściowo dla KDE)
oparty na "Matrix: Reaktywacja". Posiada możliwość pracy na pełnym
ekranie.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__aclocal} -I m4
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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/matrixgl.1*
%{_datadir}/xscreensaver/matrixgl.xml
