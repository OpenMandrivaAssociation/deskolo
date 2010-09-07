Name:		deskolo
Version:	0.1
Release:	%mkrel 1
License:	GPL
Summary:	deskolo project package
Source:		deskolo-%{version}.tar.bz2
Group:		Monitoring
%description
The DESKOLOL project is a product software for objective is the
visualisation and optimisation energical of computer in a enterprise
network.

Supervise the consommation energical of parks informatic heterogenous
by the intermediate of tools of supervision «WatchServer» of Wallerix
and park management «Pulse 2» of Mandriva.

%prep
%setup -q

%build

%install
python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/deskolo.cfg
%python_sitelib/deskolo/*
%python_sitelib/Distutils-0.1-py2.6.egg-info
%_bindir/deskolo
