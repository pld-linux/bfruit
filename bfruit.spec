Summary:	Slot machine game
Summary(pl.UTF-8):	Jednoręki bandyta
Name:		bfruit
Version:	0.1.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net//bfruit/%{name}-%{version}.tar.bz2
# Source0-md5:	8022b31e716d5a5878c58435a8d531e7
URL:		http://bfruit.sourceforge.net/
BuildRequires:	sed >= 4.0
Requires:	python-pygame
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BFruit is an open source, GPL licensed fruit machine game written in
python and pygame.

%description -l pl.UTF-8
BFruit jest to gra w "Jednorękiego bandytę" oparta na licencji GPL,
napisana w pythonie z wykorzystaniem biblioteki pygame.

%prep
%setup -q
%{__sed} -i -e 's#data/#%{_datadir}/%{name}/#' bfruit.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install bfruit.py $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/bfruit
%{_datadir}/%{name}
