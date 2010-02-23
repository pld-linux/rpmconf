Summary:	Tool to handle rpmnew and rpmsave files
Summary(pl.UTF-8):	Narzędzie do obsługi plików rpmnew oraz rpmsave
Name:		rpmconf
Version:	0.2.2
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://github.com/downloads/xsuchy/rpmconf/%{name}-%{version}.tar.gz
# Source0-md5:	2a40cafc49b9bc008f3eb51b4d324d4e
URL:		http://wiki.github.com/xsuchy/rpmconf/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to handle rpmnew and rpmsave files.

What it does:
- run “rpmconf —help” and you will see :)
- it search all config file of all installed packages and check if
  file with .rpmsave or .rpmnew exists
- it allows you to see diff of this file against current file
- it allows you to keep current version or the other one (rpmsave or
  rpmnew one)
- it deletes .rpmsave and .rpmnew files which are identical to current
  file
- after your choice it deletes the unwanted file

%description -l pl.UTF-8
Narzędzie do obsługi plików rpmnew oraz rpmsave.

Co to robi:
- uruchom “rpmconf —help” i sam zobaczysz :)
- wyszukuje wszytskie pliki konfiguracyjne wszystkich zainstalowanych
  paczek i sprawdza czy istnieje plik z rozszerzeniem .rpmsave lub
  .rpmnew
- umożliwia wyświetlenie różnic między tym plikiem a plikiem aktualnie
  używanym
- umożliwia pozostawienie aktualnie używanego pliku lub zamianę go na
  inny (rpmsave lub rpmnew)
- usuwa te pliki .rpmsave i .rpmnew, które są identyczne z aktualnie
  używanym plikiem
- po dokonaniu przez użytkownika wyboru usuwa niechciane pliki

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install rpmconf $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/rpmconf
