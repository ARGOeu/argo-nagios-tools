Summary: ARGO tools for Nagios
Name: argo-nagios-tools
Version: 1.0.0
Release: 1%{?dist}
License: APL2
Group: Network/Monitoring
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
ARGO tools for Nagios:
- component argo-voms-htpasswd for fetching user DNs from GOCDB and VOMS
and generating htpasswd file for Apache
- component nagios-run-check for running Nagios check from CLI

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{_sbindir}
install --mode 755 argo-voms-htpasswd ${RPM_BUILD_ROOT}%{_sbindir}
install --directory ${RPM_BUILD_ROOT}%{_bindir}
install --mode 755 nagios-run-check ${RPM_BUILD_ROOT}%{_bindir}
install --directory ${RPM_BUILD_ROOT}/usr/libexec/
install --mode 755 argo-voms-htpasswd.libexec ${RPM_BUILD_ROOT}/usr/libexec/argo-voms-htpasswd
install --directory ${RPM_BUILD_ROOT}/etc/argo-voms-htpasswd
install --mode 644 argo-voms-htpasswd.conf ${RPM_BUILD_ROOT}/etc/argo-voms-htpasswd/
install --mode 644 argo-voms-htpasswd.conf.example ${RPM_BUILD_ROOT}/etc/argo-voms-htpasswd/
install --mode 644 argo-voms-htpasswd-bans.conf ${RPM_BUILD_ROOT}/etc/argo-voms-htpasswd/
install --directory ${RPM_BUILD_ROOT}/etc/argo-voms-htpasswd/argo-voms-htpasswd.d
install --directory ${RPM_BUILD_ROOT}/etc/init.d
install --mode 755 argo-voms-htpasswd.initd ${RPM_BUILD_ROOT}/etc/init.d/argo-voms-htpasswd
install --directory ${RPM_BUILD_ROOT}/etc/cron.d
install --mode 644 argo-voms-htpasswd.cron ${RPM_BUILD_ROOT}/etc/cron.d/argo-voms-htpasswd
install --directory ${RPM_BUILD_ROOT}/etc/logrotate.d
install --mode 644 argo-voms-htpasswd.logrotate ${RPM_BUILD_ROOT}/etc/logrotate.d/argo-voms-htpasswd
install --directory ${RPM_BUILD_ROOT}/etc/sysconfig
install --mode 644 argo-voms-htpasswd.sysconfig ${RPM_BUILD_ROOT}/etc/sysconfig/argo-voms-htpasswd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sbindir}/argo-voms-htpasswd
%{_bindir}/nagios-run-check
/usr/libexec/argo-voms-htpasswd
/etc/init.d/argo-voms-htpasswd
%attr(0644,root,root) %config(noreplace) /etc/sysconfig/argo-voms-htpasswd
%attr(0644,root,root) %config(noreplace) /etc/logrotate.d/argo-voms-htpasswd
%attr(0644,root,root) %config(noreplace) /etc/cron.d/argo-voms-htpasswd
%attr(0644,root,root) %config(noreplace) /etc/argo-voms-htpasswd/argo-voms-htpasswd.conf
%attr(0644,root,root) %config(noreplace) /etc/argo-voms-htpasswd/argo-voms-htpasswd-bans.conf
/etc/argo-voms-htpasswd/argo-voms-htpasswd.conf.example
%dir /etc/argo-voms-htpasswd/argo-voms-htpasswd.d

%post
/sbin/chkconfig --add argo-voms-htpasswd
:

%preun
if [ "$1" = 0 ]; then
   /sbin/service argo-voms-htpasswd stop
   /sbin/chkconfig --del argo-voms-htpasswd
fi
:

%changelog
* Tue Mar 8 2016 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version based on voms-htpasswd, voms2htpasswd and 
  grid-monitoring-fm-nagios-local
