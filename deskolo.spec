Name:		deskolo
Version:	0.23
Release:	%mkrel 2
License:	GPLv2
Summary:	Deskolo energy consumption monitoring utilities
Url:        http://www.deskolo.com
Source:		deskolo-%{version}.tar.bz2
Group:		Monitoring
BuildRequires: libx11-devel
BuildRequires: libxext-devel
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

