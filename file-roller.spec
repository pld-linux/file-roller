%define release 3
%define prefix  /usr
%define name	file-roller
%define version 1.0

Summary:	An archive manager for GNOME.
Name:		%{name}
Version:    	%{version}
Release:	%{release}
Copyright:	GPL
Vendor:		GNOME
URL:		http://fileroller.sourceforge.net
Group:		Applications/Archiving
Source0:	%{name}-%{version}.tar.gz
Packager:       Paolo Bacchilega <paolo.bacch@tin.it>
BuildRoot:	%{_builddir}/%{name}-%{version}-root
Requires:       glib >= 1.2.9
Requires:       gtk+ >= 1.2.9
Requires:	gnome-libs >= 1.2.0
Requires:	gdk-pixbuf >= 0.9.0
Requires:	libglade >= 0.14
Requires:	oaf >= 0.6.5
Requires:	bonobo >= 1.0.0
BuildRequires:	glib-devel >= 1.2.9
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	libglade-devel >= 0.14
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	bonobo-devel >= 1.0.0
Docdir:         %{prefix}/share/doc

%description
File Roller is an archive manager for the GNOME environment. With File Roller
you can : create and modify archives; view the content of an archive; view a 
file contained in the archive; extract files from the archive.
File Roller is only a front-end (a graphical interface) to various archiving 
programs. The supported file types are :
    * Tar archives uncompressed (.tar) or compressed with
          * gzip (.tar.gz , .tgz)
          * bzip (.tar.bz , .tbz)
          * bzip2 (.tar.bz2 , .tbz2)
          * compress (.tar.Z , .taz)
          * lzop (.tar.lzo , .tzo)
    * Zip archives (.zip)
    * Jar archives (.jar , .ear , .war)
    * Lha archives (.lzh)
    * Rar archives (.rar)
    * Single files compressed with gzip, bzip, bzip2, compress, lzop

%prep
%setup 

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/file-roller
%{_bindir}/fr-document-viewer
%{_datadir}/gnome/apps/Utilities/file-roller.desktop
%{_datadir}/file-roller/glade/*.glade
%{_datadir}/file-roller/icons/*.xpm
%{_datadir}/file-roller/scripts/Add_to_archive
%{_datadir}/file-roller/scripts/Extract_to
%{_datadir}/file-roller/scripts/Extract_here
%doc %{_datadir}/file-roller/scripts/README
%{_datadir}/locale/*/LC_MESSAGES/file-roller.mo
%{_datadir}/appliation-registry/file-roller.applications
%{_datadir}/mime-info/file-roller.*
%{_datadir}/pixmaps/file-roller.png
%doc AUTHORS NEWS README COPYING
