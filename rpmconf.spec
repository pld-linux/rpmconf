Summary:	Tool to handle rpmnew and rpmsave files
Summary(pl.UTF-8):	Narzędzie do obsługi plików rpmnew oraz rpmsave
Name:		rpmconf
Version:	1.1.8
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://github.com/xsuchy/rpmconf/archive/%{name}-%{version}-1/rpmconf-%{version}.tar.gz
# Source0-md5:	e86ba5c336ee75fd9b34557de90407d6
URL:		https://github.com/xsuchy/rpmconf
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
BuildRequires:	python3-modules
BuildRequires:	python3-rpm
BuildRequires:	sphinx-pdg
%if %{with tests}
BuildRequires:	python3-pylint
BuildRequires:	python3-six
%endif
Requires:	python3-rpm
Requires:	python3-rpmconf = %{version}-%{release}
Requires:	which
Suggests:	diffuse
Suggests:	diffutils
Suggests:	kdiff3
Suggests:	meld
Suggests:	vim-X11
Suggests:	vim-enhanced
# sdiff
Suggests:	diffutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool search for .rpmnew, .rpmsave and .rpmorig files and ask you
what to do with them: Keep current version, place back old version,
watch the diff or merge.

%package -n python3-rpmconf
Summary:	Python interface for %{name}
Requires:	pydoc3

%description -n python3-rpmconf
Python interface for %{name}. Mostly useful for developers only.

%package -n python3-rpmconf-doc
Summary:	Documentation of python interface for %{name}

%description -n python3-rpmconf-doc
Documentation generated from code of python3-rpmconf.

%prep
%setup -q -n %{name}-%{name}-%{version}-1

%{__sed} -i -e 's/__version__ = .*/__version__ = "%{version}"/' rpmconf/rpmconf.py
%{__sed} -i -e 's/version = .*,/version = "%{version}",/' setup.py
%{__sed} -i -e 's@/usr/bin/ls@/bin/ls@' rpmconf/rpmconf.py

%build
%py3_build

docbook2man rpmconf.sgml
%{__make} -C docs html man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man{3,8},%{_datadir}/rpmconf}

%py3_install \
	--install-scripts %{_sbindir} \
	--root $RPM_BUILD_ROOT

cp -p rpmconf.8 $RPM_BUILD_ROOT%{_mandir}/man8/rpmconf.8
cp -p docs/build/man/rpmconf.3 $RPM_BUILD_ROOT%{_mandir}/man3/rpmconf.3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_sbindir}/rpmconf
%dir %{_datadir}/rpmconf
%{_mandir}/man8/rpmconf.8*

%files -n python3-rpmconf
%defattr(644,root,root,755)
%{py3_sitescriptdir}/rpmconf
%{py3_sitescriptdir}/rpmconf-*.egg-info
%{_mandir}/man3/rpmconf.3*

%files -n python3-rpmconf-doc
%defattr(644,root,root,755)
%doc docs/build/html
