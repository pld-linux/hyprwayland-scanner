Summary:	A Hyprland implementation of wayland-scanner, in and for C++
Name:		hyprwayland-scanner
Version:	0.4.2
Release:	1
License:	BSD
Group:		Development/Tools
#Source0Download: https://github.com/hyprwm/hyprwayland-scanner/releases
Source0:	https://github.com/hyprwm/hyprwayland-scanner/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	700e4abd566bdd5ac346e88da123cfaf
Patch0:		flags.patch
URL:		https://hyprland.org/
BuildRequires:	cmake >= 3.19
BuildRequires:	libstdc++-devel >= 6:11
BuildRequires:	pkgconfig
BuildRequires:	pugixml-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Hyprland implementation of wayland-scanner, in and for C++.

%prep
%setup -q
%patch0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/hyprwayland-scanner
%{_libdir}/cmake/hyprwayland-scanner
%{_pkgconfigdir}/hyprwayland-scanner.pc
