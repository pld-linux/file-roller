Summary:	An archive manager for GNOME
Summary(pl):	Zarz�dca archiw�w dla GNOME
Summary(pt_BR):	Gerenciador de arquivos compactados para o GNOME
Name:		file-roller
Version:	2.1.2
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/fileroller/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.0.4-3
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnome-devel >= 2.1.0-3
BuildRequires:	libgnomeui-devel >= 2.1.1-3
Requires:	gnome-vfs2 >= 2.0.4-3
Requires(post):	scrollkeeper
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2/gconf/schemas
%define		_omf_dest_dir   %(scrollkeeper-config --omfdir)

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

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
    --disable-schemas-install \
    --with-gconf-schema-file-dir=%{_sysconfdir}
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
GCONF_CONFIG_SOURCE="" \
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/*.schemas > /dev/null

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/file-roller
%{_datadir}/applications/*
%{_datadir}/file-roller
%{_datadir}/application-registry/file-roller.applications
%{_datadir}/mime-info/file-roller.*
%{_pixmapsdir}/file-roller.png
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/*
