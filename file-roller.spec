Summary:	An archive manager for GNOME
Summary(pl.UTF-8):	Zarządca archiwów dla GNOME
Summary(pt_BR.UTF-8):	Gerenciador de arquivos compactados para o GNOME
Name:		file-roller
Version:	2.30.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/file-roller/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	fe4fe7957431041dc079ab0f9d30805e
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	nautilus-devel >= 2.26.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
# libegg
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	nautilus-libs >= 2.26.0
Suggests:	bzip2
Suggests:	gzip
Suggests:	p7zip
%ifarch %{ix86}
Suggests:	rar
%else
Suggests:	unrar
%endif
Suggests:	tar
Suggests:	zip
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

%description -l pl.UTF-8
File Roller to zarządca archiwów dla środowiska GNOME. Przy jego
pomocy można: tworzyć i modyfikować archiwa, oglądać ich zawartość,
oglądać poszczególne pliki zawarte w archiwum oraz rozpakowywać pliki
z archiwów. File Roller jest tylko interfejsem graficznym do
właściwych programów archiwizujących. Obsługiwane typy plików to:
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

%description -l pt_BR.UTF-8
File Roller é um gerenciador de pacotes de arquivos compactados para o
ambiente GNOME. Com ele é possível criar arquivos, visualizar o
conteúdo de arquivos existentes, visualizar um arquivo contido em um
pacote e extrair os arquivos de um pacote.

%prep
%setup -q
sed -i 's/^en@shaw//' po/LINGUAS
rm po/en@shaw.po

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la

# the same locale as ur
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install file-roller.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall file-roller.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/file-roller
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-fileroller.so
%dir %{_libdir}/file-roller
%attr(755,root,root) %{_libdir}/file-roller/isoinfo.sh
%attr(755,root,root) %{_libdir}/file-roller/rpm2cpio
%{_datadir}/file-roller
%{_desktopdir}/file-roller.desktop
%{_iconsdir}/hicolor/*/apps/file-roller.*
%{_sysconfdir}/gconf/schemas/file-roller.schemas
