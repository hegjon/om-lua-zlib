%global forgeurl https://github.com/brimworks/lua-zlib
%global tag v%{version}

%define lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)
%define lua_libdir %{_libdir}/lua/%{lua_version}

Name:      lua-zlib
Version:   1.2
Release:   1
Summary:   Simple streaming interface to zlib for Lua
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

Requires: lua

BuildRequires: lua-devel
BuildRequires: zlib-devel


%description
%{summary}.


%prep
%forgesetup


%build
%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o lua_zlib.o lua_zlib.c

%{__cc} %{?__global_ldflags} -lz -lm -llua -shared -o zlib.so lua_zlib.o


%install
install -dD %{buildroot}%{lua_libdir}
install -p -m 755 zlib.so %{buildroot}%{lua_libdir}/

%check
lua test.lua


%files
%license README
%doc README
%{lua_libdir}/zlib.so
