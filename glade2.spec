Summary:	Glade - a user interface builder for GTK+2
Summary(es):	Herramienta visual para creaci�n de interfaces GTK+2 o GNOME
Summary(fr):	Outil de programmation graphique visuel
Summary(pl):	Glade - narz�dzie do budowania GUI w oparciu o bibliotek� GTK+2
Summary(pt_BR):	Ferramenta visual para cria��o de interfaces GTK+2 ou GNOME
Summary(ru):	���������� ���������� ����������� �� ������ GTK+2
Summary(uk):	�������� �������� ��������Ӧ� �� ����צ GTK+2
Name:		glade2
Version:	2.6.4
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glade/2.6/glade-%{version}.tar.bz2
# Source0-md5:	00bd1efab0ef82d583c4cf6fe67ce17a
Patch0:		%{name}-locale-names.patch
URL:		http://glade.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libbonoboui-devel >= 2.6.0
BuildRequires:	libgnomedb-devel >= 1.0.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.1
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	xft-devel >= 2.0-6
# loads libgail.so, libgail-gnome.so GTK+ modules on start
Requires:	gail
Requires:	libgail-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glade is a RAD tool to enable quick & easy development of user
interfaces for the GTK+2 toolkit. It also contains built-in support for
generating the C source code needed to recreate the interfaces.

The user interfaces designed in Glade are stored in the well-known XML
format, enabling easy integration with external tools. Several tools
are already available which can turn the XML files into source code in
other languages such as C, C++, ADA, Perl and Python.

%description -l es
Herramienta visual para creaci�n de interfaces GTK+2 o GNOME

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
biblioteki GTK+2. Zawiera tak�e w sobie generator kodu �r�d�owego
tworzonego interfejsu w C.

Definicja interfejsu u�ytkownika tworzona przez Glade jest
przechowywana w formacie dokumentu XML, kt�ry umo�liwia �atwe u�ywanie
tego opisu przez zewn�trzne narz�dzia jak generatory kodu �r�d�owego
w innych j�zykach programowania. W obecnej chwili s� dost�pne
generatory kodu �r�d�owego w C, C++, ADA, Perlu i Pythonie.

%description -l pt_BR
Ferramenta visual para cria��o de interfaces GTK+2 ou GNOME.

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
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# glade-2.0.mo, but gnome/help/glade-2 - use --all-name
%find_lang glade-2.0 --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f glade-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glade-2
%{_omf_dest_dir}/glade-2
%{_desktopdir}/glade-2.desktop
%{_pixmapsdir}/*
