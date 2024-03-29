Summary:	Glade - a user interface builder for GTK+2
Summary(es.UTF-8):	Herramienta visual para creación de interfaces GTK+2 o GNOME
Summary(fr.UTF-8):	Outil de programmation graphique visuel
Summary(pl.UTF-8):	Glade - narzędzie do budowania GUI w oparciu o bibliotekę GTK+2
Summary(pt_BR.UTF-8):	Ferramenta visual para criação de interfaces GTK+2 ou GNOME
Summary(ru.UTF-8):	Диалоговое построение интерфейсов на основе GTK+2
Summary(uk.UTF-8):	Діалогова побудова інтерфейсів на основі GTK+2
Name:		glade2
Version:	2.12.2
Release:	1
License:	GPL v2+
Group:		Development/Building
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glade/2.12/glade-%{version}.tar.bz2
# Source0-md5:	54082e44bba1c75770aa0bff2f38987e
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gda12.patch
Patch2:		%{name}-gtk_clist.patch
URL:		http://glade.gnome.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	intltool >= 0.36.0
BuildRequires:	libbonoboui-devel >= 2.15.0
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	libgnomedb-devel >= 1:1.2.2
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	sed >= 4.0
Requires(post,postun):	scrollkeeper
# loads libgail.so, libgail-gnome.so GTK+ modules on start
Requires:	gail
Requires:	libgail-gnome
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glade is a RAD tool to enable quick & easy development of user
interfaces for the GTK+2 toolkit. It also contains built-in support
for generating the C source code needed to recreate the interfaces.

The user interfaces designed in Glade are stored in the well-known XML
format, enabling easy integration with external tools. Several tools
are already available which can turn the XML files into source code in
other languages such as C, C++, ADA.

%description -l es.UTF-8
Herramienta visual para creación de interfaces GTK+2 o GNOME.

%description -l fr.UTF-8
Glade est un outil de développement rapide (RAD en anglais) permettant
de construire facilment des interfaces utilisateurs utilisant la boite
à outil GTK+2. Glade est capable d'utiliser les spécificités de GNOME.

Les interfaces conçues à l'aide de GLADE sont stockées au format XML,
permettant un interfacage aisé avec d'autres outils. Plusieurs outils
sont disponibles pour exporter le code source dans d'autres langages
tels que le C, le C++, l'ADA.

%description -l pl.UTF-8
Glade jest narzędziem typu RAD (Rapid Application Development) do
szybkiego i wygodnego tworzenia interfejsu użytkownika z użyciem
biblioteki GTK+2. Zawiera także w sobie generator kodu źródłowego
tworzonego interfejsu w C.

Definicja interfejsu użytkownika tworzona przez Glade jest
przechowywana w formacie dokumentu XML, który umożliwia łatwe używanie
tego opisu przez zewnętrzne narzędzia jak generatory kodu źródłowego w
innych językach programowania. W obecnej chwili są dostępne generatory
kodu źródłowego w C, C++, ADA.

%description -l pt_BR.UTF-8
Ferramenta visual para criação de interfaces GTK+2 ou GNOME.

%description -l ru.UTF-8
GLADE - это программа диалогового построения интерфейсов пользователя
под GTK+2 и GNOME. GLADE может создавать исходный код на языке C;
также доступна поддержка языков C++, Ada95, Python и Perl посредством
внешних инструментов, обрабатывающих XML файлы описания интерфейса,
созданные GLADE.

%description -l uk.UTF-8
GLADE - це програма діалогової побудови інтерфейсів користувача під
GTK+2 та GNOME. GLADE може створювати вихідний код на мові C; доступна
також підтримка мов C++, Ada95 через зовнішні інструменти, що
обробляють XML файли опису інтерфейсу, створені GLADE.

%prep
%setup -q -n glade-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv po/sr@{Latn,latin}.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gnome-db
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# glade-2.0.mo, but gnome/help/glade-2 - use --all-name
%find_lang glade-2.0 --all-name --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f glade-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glade-2
%{_desktopdir}/glade-2.desktop
%{_pixmapsdir}/*
