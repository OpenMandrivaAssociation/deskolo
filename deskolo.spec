Name:		deskolo
Version:	0.1
Release:	%mkrel 1
License:	GPL
Summary:	deskolo project package
Source:		deskolo-%{version}.tar.bz2
Group:		Monitoring
BuildRequires:	python
%description
The DESKOLOL software, whose purpose is to visualize and optimize the energy consumption of computers in a corporate network.

• Monitoring of energy consumption due to heterogeneous hardware monitoring "Watch Server with Wallix fleet and" Pulse 2 "Mandriva.

• awareness of the need to attract business for a rational use of energy in connection with their computer parks and savings they can achieve.

• Create a shortcut to the energy efficiency of IT networks and a website to provide anonymous or no information on their energy performance and compare.

• Control and reduction of energy consumption in heterogeneous IT parks in the standby mode, computers, peripherals and off the screen, and by setting up a Linux distribution "low consumption.

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
