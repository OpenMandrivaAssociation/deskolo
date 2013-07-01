Name:		deskolo
Version:	0.23
Release:	3
License:	GPLv2
Summary:	Energy consumption monitoring utilities
Url:        http://www.deskolo.com
Source:		deskolo-%{version}.tar.bz2
Group:		Monitoring
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: python-devel
Requires: wattsup
Requires: python-dbus
Requires: python-lxml
Requires: cpufrequtils
Requires: powertop
Suggests: collectd
Suggests: rrdtool
Suggests: xdg-utils
Suggests: xdpyinfo

%description
Deskolo aims at monitoring and controlling the energy consumption of 
computers in a corporate network.

%prep
%setup -q

%build

%install
%{__rm} -rf %buildroot
%{__mkdir_p} %buildroot/%{_bindir}
%{__make} DESTDIR=%buildroot%{_bindir} install
python setup.py install --root=%{buildroot}




%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/deskolo.cfg
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{py_ver}.egg-info
%{_bindir}/deskolo
%{_bindir}/xlib-dpms



%changelog
* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 0.23-2mdv2011.0
+ Revision: 594488
- rebuild for python 2.7
- fix file list

* Wed Sep 29 2010 Stéphane Laurière <slauriere@mandriva.com> 0.23-1mdv2011.0
+ Revision: 582045
- v0.23 release

* Wed Sep 29 2010 Stéphane Laurière <slauriere@mandriva.com> 0.22-1mdv2011.0
+ Revision: 582040
- v0.22 release
- v0.21 release
- added buildrequires libx11_6-devel
- v0.2 release

* Tue Sep 07 2010 Nicolas Vigier <nvigier@mandriva.com> 0.1-1mdv2011.0
+ Revision: 576539
- lol
- complete description (from website)
- import deskolo

