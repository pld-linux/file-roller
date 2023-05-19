#
# Conditional build:
%bcond_with	apidocs		# API documentation (API not packaged, so disabled for now)
%bcond_without	libportal	# native app chooser via libportal
%bcond_without	nautilus	# Nautilus extension
#
Summary:	An archive manager for GNOME
Summary(pl.UTF-8):	Zarządca archiwów dla GNOME
Summary(pt_BR.UTF-8):	Gerenciador de arquivos compactados para o GNOME
Name:		file-roller
Version:	43.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/file-roller/43/%{name}-%{version}.tar.xz
# Source0-md5:	fd743c77f1af1934a9eac7e7b1688219
Patch0:		%{name}-packages.patch
URL:		https://wiki.gnome.org/Apps/FileRoller
BuildRequires:	cpio
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	json-glib-devel >= 0.14.0
BuildRequires:	libarchive-devel >= 3.2.0
BuildRequires:	libhandy1-devel >= 1.5.0
%{?with_libportal:BuildRequires:	libportal-devel >= 0.5}
%{?with_libportal:BuildRequires:	libportal-gtk3-devel >= 0.5}
BuildRequires:	meson >= 0.59
%{?with_nautilus:BuildRequires:	nautilus-devel >= 43}
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.38
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.38
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	json-glib >= 0.14.0
Requires:	libarchive >= 3.2.0
Requires:	libhandy1 >= 1.5.0
Suggests:	bzip2
Suggests:	cpio
Suggests:	gzip
Suggests:	p7zip
%ifarch %{ix86}
Suggests:	rar
%else
Suggests:	unrar
%endif
Suggests:	tar
Suggests:	zip
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
Requires:	nautilus >= 43

%description -n nautilus-extension-file-roller
File Roller (archive manager) extension for Nautilus (GNOME file
manager).

%description -n nautilus-extension-file-roller -l pl.UTF-8
Rozszerzenie File Roller (zarządca archiwów) Nautilusa (zarządcy
plików GNOME).

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{?with_apidocs:-Dapi_docs=enabled} \
	-Dintrospection=enabled \
	%{!?with_nautilus:-Dnautilus-actions=disabled} \
	%{!?with_libportal:-Duse_native_appchooser=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc AUTHORS MAINTAINERS NEWS README.md README_COMMANDLINE
%attr(755,root,root) %{_bindir}/file-roller
%dir %{_libexecdir}/file-roller
%attr(755,root,root) %{_libexecdir}/file-roller/isoinfo.sh
%attr(755,root,root) %{_libexecdir}/file-roller/rpm2cpio
%{_datadir}/dbus-1/services/org.gnome.ArchiveManager1.service
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/file-roller
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
%{_datadir}/metainfo/org.gnome.FileRoller.appdata.xml
%{_desktopdir}/org.gnome.FileRoller.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.FileRoller.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.FileRoller.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.FileRoller-symbolic.svg

%if %{with nautilus}
%files -n nautilus-extension-file-roller
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-4/libnautilus-fileroller.so
%endif
