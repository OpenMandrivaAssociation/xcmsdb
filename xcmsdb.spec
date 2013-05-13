Name:		xcmsdb
Version:	1.0.4
Release:	2
Summary:	Device Color Characterization utility for X Color Management System
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
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
autoreconf -fi
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xcmsdb
%{_mandir}/man1/xcmsdb.1.*


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.4-1
+ Revision: 781033
- version update 1.0.4

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 671285
- mass rebuild

* Sun Sep 26 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 581090
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 464698
- New version: 1.0.2

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 351224
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 226021
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 155952
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 76408
- rebuild for 2008
- add description
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!

