Name:		monsterz
Version: 0.7.0
Release:    %mkrel 2
# in reality, this is the DWYF license..
License:	Freeware
Group:		Games/Puzzles
Summary:    A little addictive puzzle game
Source:     http://sam.zoy.org/projects/monsterz/%{name}-%{version}.tar.bz2
Url:        http://sam.zoy.org/projects/monsterz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   pygame
BuildArch:  noarch 
BuildRequires: ImageMagick

%description
Monsterz is a little puzzle game, similar to the famous Bejeweled or Zookeeper.

The goal of the game is to create rows of similar monsters, either horizontally 
or vertically. The only allowed move is the swap of two adjacent monsters, on 
the condition that it creates a row of three or more. When alignments are 
cleared, pieces fall from the top of the screen to fill the board again. Chain 
reactions earn you even more points.

This game is mostly about luck, but it remains highly addictive. You have been 
warned. 

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_gamesdatadir}/%{name}
cp -R monsterz.py graphics/ sound/ $RPM_BUILD_ROOT/%{_gamesdatadir}/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_gamesbindir}/

cat > $RPM_BUILD_ROOT/%{_gamesbindir}/%{name} <<EOF
#!/bin/bash
exec python %{_gamesdatadir}/%{name}/monsterz.py
EOF

chmod 755 $RPM_BUILD_ROOT/%{_gamesbindir}/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_menudir}/

cat > %buildroot/%_menudir/%name << EOF
?package(%{name}): needs=x11 \
icon="%{name}.png" \
section="More Applications/Games/Puzzles" \
title=Monsterz longtitle="Addictive puzzle game" \
command="%{_gamesbindir}/%{name}" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Monsterz
Comment=Addictive puzzle game
Exec=%_gamesbindir/%{name}
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Puzzles;Game;BlocksGame;
EOF

mkdir -p $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}/
convert -geometry 16x16 graphics/icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert -geometry 32x32 graphics/icon.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -geometry 48x48 graphics/icon.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{update_menus}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README TODO 
%{_gamesdatadir}/%{name}/
%{_gamesbindir}/%{name}
%_datadir/applications/mandriva*
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
