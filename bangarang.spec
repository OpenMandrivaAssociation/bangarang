Summary:        Media player for KDE using nepomuk
Name:           bangarang
Version:        2.0.1
Release:        %mkrel 1
License:        GPLv2+
Group:          Graphical desktop/KDE
Source0:        http://bangarangissuetracking.googlecode.com/files/%{name}-%{version}.tar.gz
URL:            http://bangarangkde.wordpress.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  taglib-devel

%description
Bangarang is a media player for KDE using nepomuk to store informations

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/bangarang                        
%_kde_bindir/bangarangnepomukwriter
%_kde_datadir/applications/kde4/bangarang.desktop
%_kde_appsdir/solid/actions/*.desktop
%_kde_iconsdir/hicolor/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%name

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
