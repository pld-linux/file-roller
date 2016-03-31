#
# Conditional build:
%bcond_without	nautilus	# Nautilus extension
#
Summary:	An archive manager for GNOME
Summary(pl.UTF-8):	Zarządca archiwów dla GNOME
Summary(pt_BR.UTF-8):	Gerenciador de arquivos compactados para o GNOME
Name:		file-roller
Version:	3.20.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/file-roller/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	a8ff996145a069d5154f3600845d14b6
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.13.3
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel >= 0.14.0
BuildRequires:	libarchive-devel >= 3.0.0
BuildRequires:	libmagic-devel
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-progs
%{?with_nautilus:BuildRequires:	nautilus-devel >= 2.26.0}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.36.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.13.3
Requires:	hicolor-icon-theme
Requires:	json-glib >= 0.14.0
Requires:	libarchive >= 3.0.0
Requires:	libnotify >= 0.4.3
Suggests:	bzip2
Suggests:	gzip
Suggests:	nautilus-extension-file-roller = %{version}-%{release}
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

%package -n nautilus-extension-file-roller
Summary:	File Roller (archive manager) extension for Nautilus (GNOME file manager)
Summary(pl.UTF-8):	Rozszerzenie File Roller (zarządca archiwów) Nautilusa (zarządcy plików GNOME)
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.26.0

%description -n nautilus-extension-file-roller
File Roller (archive manager) extension for Nautilus (GNOME file
manager).

%description -n nautilus-extension-file-roller -l pl.UTF-8
Rozszerzenie File Roller (zarządca archiwów) Nautilusa (zarządcy
plików GNOME).

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_nautilus:--disable-nautilus-actions} \
	--disable-schemas-compile \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with nautilus}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
%endif

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README README_COMMANDLINE
%attr(755,root,root) %{_bindir}/file-roller
%dir %{_libdir}/file-roller
%attr(755,root,root) %{_libdir}/file-roller/isoinfo.sh
%attr(755,root,root) %{_libdir}/file-roller/rpm2cpio
%{_datadir}/GConf/gsettings/file-roller.convert
%{_datadir}/appdata/org.gnome.FileRoller.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/dbus-1/services/org.gnome.FileRoller.ArchiveManager1.service
%{_datadir}/file-roller
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
%{_desktopdir}/org.gnome.FileRoller.desktop
%{_iconsdir}/hicolor/*x*/apps/file-roller.png
%{_iconsdir}/hicolor/scalable/apps/file-roller-symbolic.svg

%if %{with nautilus}
%files -n nautilus-extension-file-roller
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-fileroller.so
%endif
