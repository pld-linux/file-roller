Summary:	An archive manager for GNOME
Summary(pl):	Zarz±dca archiwów dla GNOME
Summary(pt_BR):	Gerenciador de arquivos compactados para o GNOME
Name:		file-roller
Version:	2.2.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.2/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnome-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	rpm-build >= 4.1-10
Requires:	gnome-vfs2 >= 2.2.0
Requires(post):	scrollkeeper
Requires(post):	GConf2
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
File Roller to zarz±dca archiwów dla ¶rodowiska GNOME. Przy jego
pomocy mo¿na: tworzyæ i modyfikowaæ archiwa, ogl±daæ ich zawarto¶æ,
ogl±daæ poszczególne pliki zawarte w archiwum oraz rozpakowywaæ pliki
z archiwów. File Roller jest tylko interfejsem graficznym do
w³a¶ciwych programów archiwizuj±cych. Obs³ugiwane typy plików to:
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
File Roller é um gerenciador de pacotes de arquivos compactados para o
ambiente GNOME. Com ele é possível criar arquivos, visualizar o
conteúdo de arquivos existentes, visualizar um arquivo contido em um
pacote e extrair os arquivos de um pacote.

%prep
%setup -q

%build
rm -f missing
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
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/file-roller
%attr(755,root,root) %{_libdir}/bonobo/*.so
%{_libdir}/bonobo/*.la
%{_libdir}/bonobo/servers/*.server
%{_datadir}/applications/*
%{_datadir}/file-roller
%{_datadir}/application-registry/file-roller.applications
%{_datadir}/mime-info/file-roller.*
%{_pixmapsdir}/file-roller.png
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/**
