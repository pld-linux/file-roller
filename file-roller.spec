Summary:	An archive manager for GNOME
Summary(pl):	Zarz±dca archiwów dla GNOME
Name:		file-roller
Version:	2.1.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/fileroller/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
Requires(post): scrollkeeper
Requires(post): GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix					/usr/X11R6
%define		_mandir					%{_prefix}/man
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

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Utilities \
	omf_dest_dir=%{_omf_dest_dir}/%{name}
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
scrollkeeper-update
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" \
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%config %{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/file-roller
%{_applnkdir}/Utilities/file-roller.desktop
%{_datadir}/file-roller
%{_datadir}/application-registry/file-roller.applications
%{_datadir}/mime-info/file-roller.*
%{_pixmapsdir}/file-roller.png
%{_omf_dest_dir}/%{name}
