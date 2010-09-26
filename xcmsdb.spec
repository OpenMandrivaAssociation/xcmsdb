Name:		xcmsdb
Version:	1.0.3
Release:	%mkrel 1
Summary:	Device Color Characterization utility for X Color Management System
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
xcmsdb is used to load, query, or remove Device Color Characterization
data stored in properties on the root window of the screen as 
specified in section 7, Device Color Characterization, of the ICCCM.
Device Color Characterization data (also called the Device Profile) is
an integral part of Xlib's X Color Management System (Xcms), necessary
for proper conversion of color specification between device-
independent and device-dependent forms.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xcmsdb
%{_mandir}/man1/xcmsdb.1.*
