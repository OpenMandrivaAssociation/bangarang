Summary:	Media player for KDE using nepomuk
Name:		bangarang
Version:	2.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://bangarangissuetracking.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		bangarang-2.1-ru.patch
URL:		http://bangarangkde.wordpress.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automoc4
BuildRequires:	kdelibs4-devel >= 2:4.6
BuildRequires:	taglib-devel

%description
Bangarang is a media player for KDE using nepomuk to store informations

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/bangarang
%{_kde_bindir}/bangarangnepomukwriter
%{_kde_datadir}/applications/kde4/bangarang.desktop
%{_kde_appsdir}/solid/actions/*.desktop
%{_kde_iconsdir}/hicolor/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{name}
%patch0 -p1 -b .ru

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{name}

%clean
rm -rf %{buildroot}

