Summary:	Glade - a user interface builder for Gtk+2
Summary(fr):	Outil de programmation graphique visuel
Summary(es):	Herramienta visual para creaci�n de interfaces gtk+2 o gnome
Summary(pl):	Glade - narz�dzie do budowania GUI w oparciu o bibliotek� Gtk+2
Summary(pt_BR):	Ferramenta visual para cria��o de interfaces gtk+2 ou gnome
Summary(ru):	���������� ���������� ����������� �� ������ GTK+2
Summary(uk):	�������� �������� ��������Ӧ� �� ����צ GTK+2
Name:		glade2
Version:	1.1.2
Release:	0
License:	GPL
Vendor:		Damon Chaplin <DAChaplin@msn.com>
Group:		Development/Building
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.2/sources/glade/glade-%{version}.tar.bz2
URL:		http://glade.pn.org/
#BuildRequires:	XFree86-libs
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	bonobo-devel >= 0.25
#BuildRequires:	gettext-devel
#BuildRequires:	gnome-libs-devel
#BuildRequires:	gnome-db-devel
#BuildRequires:	gtk+-devel
#BuildRequires:	intltool
#BuildRequires:	libtool
#BuildRequires:	scrollkeeper
#Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Glade is a RAD tool to enable quick & easy development of user
interfaces for the GTK+2 toolkit. It also contains built-in support for
generating the C source code needed to recreate the interfaces.

The user interfaces designed in Glade are stored in the well-known XML
format, enabling easy integration with external tools. Several tools
are already available which can turn the XML files into source code in
other languages such as C, C++, ADA, Perl and Python.

%description -l es
Herramienta visual para creaci�n de interfaces gtk+2 o gnome

%description -l fr
Glade est un outil de d�veloppement rapide (RAD en anglais) permettant
de construire facilment des interfaces utilisateurs utilisant la boite
� outil GTK+2. Glade est capable d'utiliser les sp�cificit�s de GNOME.

Les interfaces con�ues � l'aide de GLADE sont stock�es au format XML,
permettant un interfacage ais� avec d'autres outils. Plusieurs outils
sont disponibles pour exporter le code source dans d'autres langages
tels que le C, le C++, l'ADA, Perl et le Python.

%description -l pl
Glade jest narz�dziem typu RAD (Rapid Application Development) do
szybkiego i wygodnego tworzenia interfejsu u�ytkownika z u�yciem
biblioteki Gtk+2. Zawiera tak�e w sobie generator kodu �r�d�owego w C
tworzonego interfejsu.

Definicja interfejsu u�ytkownika tworzona przez Glade jest
przechowywana w formacie dokumentu XML, kt�ry umozliwia �atwe uzywanie
tego opisu przez zewn�trzne narz�dzia jak generatory kodu �r�d�owego
do innych j�zyk�w programowania. W obecnej chwili s� dost�pne
generatory kodu �r�d�owego do C, C++, ADA, Perla i Pythona.

%description -l pt_BR
Ferramenta visual para cria��o de interfaces gtk+ ou gnome.

%description -l ru
GLADE - ��� ��������� ����������� ���������� ����������� ������������
��� GTK+2 � GNOME. GLADE ����� ��������� �������� ��� �� ����� C; �����
�������� ��������� ������ C++, Ada95, Python � Perl �����������
������� ������������, �������������� XML ����� �������� ����������,
��������� GLADE.

%description -l uk
GLADE - �� �������� Ħ������ϧ �������� ��������Ӧ� ����������� Ц�
GTK+2 �� GNOME. GLADE ���� ���������� ��Ȧ���� ��� �� ��צ C; ��������
����� Ц������� ��� C++, Ada95, Python �� Perl ����� ���Φ�Φ
�����������, �� ���������� XML ����� ����� ����������, ������Φ GLADE.

%prep
%setup -q -n glade-%{version}

%build
#rm -f missing
#%{__libtoolize}
#%{__gettextize}
#xml-i18n-toolize --copy --force
#aclocal -I macros
#%{__autoconf}
#%{__automake}
%configure 
#	--without-bonobo \
#	--enable-gnome-db

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{_datadir}/applications \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

#rm -f doc/Makefile*

%find_lang glade-2.0

%post
scrollkeeper-update

%postun
scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f glade-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog doc/*.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/help/*
%{_datadir}/glade-2/*
%{_omf_dest_dir}/%{name}
%{_datadir}/applications/glade-2.desktop
%{_pixmapsdir}/*
