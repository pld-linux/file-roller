Summary:	An archive manager for GNOME
Summary(pl):	Zarz�dca archiw�w dla GNOME
Summary(pt_BR):	Gerenciador de arquivos compactados para o GNOME
Name:		file-roller
Version:	2.10.3
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/file-roller/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	dd152e2cb1bfe5c46930ae74c73e4f8e
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.10.0-3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	gnome-vfs2 >= 2.10.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File Roller is an archive manager for the GNOME environment. With File
Roller you can: create and modify archives; view the content of an
archive; view a file contained in the archive; extract files from the
archive. File Roller is only a front-end (a graphical interface) to
various archiving programs. The supported file types are:
- Tar archives uncompressed (.tar) or compressed with
	- gzip (.tar.gz , .tgz)
	- bzip (.tar.bz , .tbz)
	- bzip2 (.tar.bz2 , .tbz2)
	- compress (.tar.Z , .taz)
	- lzop (.tar.lzo , .tzo)
- Zip archives (.zip)
- Jar archives (.jar , .ear , .war)
- Lha archives (.lzh)
- Rar archives (.rar)
- Single files compressed with gzip, bzip, bzip2, compress, lzop.

%description -l pl
File Roller to zarz�dca archiw�w dla �rodowiska GNOME. Przy jego
pomocy mo�na: tworzy� i modyfikowa� archiwa, ogl�da� ich zawarto��,
ogl�da� poszczeg�lne pliki zawarte w archiwum oraz rozpakowywa� pliki
z archiw�w. File Roller jest tylko interfejsem graficznym do
w�a�ciwych program�w archiwizuj�cych. Obs�ugiwane typy plik�w to:
- archiwa tar nieskompresowane (.tar) lub skompresowane programami:
	- gzip (.tar.gz, .tgz)
	- bzip (.tar.bz, .tbz)
	- bzip2 (.tar.bz2, .tbz2)
	- compress (.tar.Z, .taz)
	- lzop (.tar.lzo, .tzo)
- archiwa zip (.zip)
- archiwa jar (.jar, .ear, .war)
- archiwa lha (.lzh)
- archiwa rar (.rar)
- pojedyncze pliki skompresowane programami gzip, bzip, bzip2,
  compress, lzop.

%description -l pt_BR
File Roller � um gerenciador de pacotes de arquivos compactados para o
ambiente GNOME. Com ele � poss�vel criar arquivos, visualizar o
conte�do de arquivos existentes, visualizar um arquivo contido em um
pacote e extrair os arquivos de um pacote.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/{mime-info,application-registry}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install file-roller.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%banner %{name} -e << EOF
For fully operational File Roller you need to install archiving
programs described in README.
EOF

%preun
%gconf_schema_uninstall file-roller.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/file-roller
%attr(755,root,root) %{_libdir}/bonobo/*.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%{_libdir}/bonobo/servers/*.server
%{_datadir}/file-roller
%{_desktopdir}/*
%{_pixmapsdir}/file-roller.png
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/*
