Summary:	Media player for KDE using nepomuk
Name:		bangarang
Version:	2.1
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://bangarangkde.wordpress.com/
Source0:	http://bangarangissuetracking.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		bangarang-2.1-ru.patch
BuildRequires:	automoc4
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(soprano)
BuildRequires:	pkgconfig(taglib)

%description
Bangarang is a media player for KDE using nepomuk to store informations.

%files -f %{name}.lang
%{_kde_bindir}/bangarang
%{_kde_bindir}/bangarangnepomukwriter
%{_kde_datadir}/applications/kde4/bangarang.desktop
%{_kde_appsdir}/solid/actions/*.desktop
%{_kde_iconsdir}/hicolor/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{name}
%patch0 -p1 -b .ru

# GCC 4.7 fix
sed -i '22i#include <unistd.h>' src/platform/infofetchers/{lastfm,tmdb,tvdb}infofetcher.h

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

