Summary:	VistaLab Image Processing Framework
Summary(pl):	VistaLab - ¶rodowisko do przetwarzania obrazu
Name:		vistalab
Version:	3.1.5
Release:	1
License:	VistaLab Public License v1.5 (GPL v2+ with exception, see COPYING)
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/vistalab/%{name}-%{version}.tar.gz
# Source0-md5:	357f2620c1f88d01be7c655ee800e761
Patch0:		%{name}-DESTDIR.patch
URL:		http://vistalab.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.6.1
BuildRequires:	boost-bind-devel
BuildRequires:	boost-utility-devel
BuildRequires:	gettext-devel
BuildRequires:	gl2ps-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	vigra-devel >= 1.3.3
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VistaLab is a modular framework for developing image processing
algorithms with minimal overhead. New plugins can be easily
distributed in binary form - they are realized as shared libraries.
This way, reuse can be achived in an easy way. Furthermore, the code
for integrating own C++-classes into a plugin is kept at a minimum via
generative programming. Not only does it enable developers concentrate
on implementing new functionality in the image processing domain (and
not, e.g. in writing configuration dialogs), it also enables plugins
to be kept in a future-proof way as no data structures defined by the
framework have to be known - they are built automatically via
generative techniques. This feature makes developing new image
processing modules a child's play.

%description -l pl
VistaLab to modularny szkielet do rozwijania algorytmów przetwarzania
obrazu z minimalnym narzutem. Nowe wtyczki mo¿na ³atwo rozpowszechniaæ
w postaci binarnej - w postaci bibliotek wspó³dzielonych. W ten sposób
bardzo ³atwo mo¿na osi±gn±æ reu¿ywalno¶æ kodu. Co wiêcej, kod do
integrowania w³asnych klas C++ we wtyczkê jest minimalny dziêki
programowaniu generatywnemu. Nie tylko pozwala to programistom
skoncentrowaæ siê na implementowaniu nowej funkcjonalno¶ci w
dziedzinie przetwarzania obrazu (a nie np. pisaniu okien dialogowych
do konfiguracji), ale tak¿e pozwala na utrzymywanie wtyczek w
bezpieczny sposób, jako ¿e nie ma potrzeby znajomo¶ci struktur danych
definiowanych przez ¶rodowisko - s± one tworzone automatycznie poprzez
techniki generatywne. Ta cecha czyni tworzenie nowych modu³ów
przetwarzaj±cych obraz dziecinnie prostym.

%package devel
Summary:	Header files for VistaLab libraries
Summary(pl):	Pliki nag³ówkowe bibliotek VistaLab
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel
Requires:	gl2ps-devel
Requires:	vigra-devel >= 1.3.3
Requires:	wxGTK2-devel >= 2.6.0

%description devel
Header files for VistaLab libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek VistaLab.

%package static
Summary:	Static VistaLab libraries
Summary(pl):	Statyczne biblioteki VistaLab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VistaLab libraries.

%description static -l pl
Statyczne biblioteki VistaLab.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=wx-gtk2-ansi-config
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
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/vistalab
%attr(755,root,root) %{_libdir}/libvistalab*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vistalab-config
%attr(755,root,root) %{_libdir}/libvistalab*.so
%{_libdir}/libvistalab*.la
%{_includedir}/vistalab

%files static
%defattr(644,root,root,755)
%{_libdir}/libvistalab*.a
