Name:           arm-frc-linux-gnueabi-frcmake
Version:        r102.c13ded0
Release:        1%{?dist}
Summary:        Wrapper scripts for using CMake with the FRC toolchain

License:        GPLv3
URL:            https://github.com/wpilibsuite/toolchain-builder
Source0:        https://github.com/wpilibsuite/toolchain-builder

%description
Wrapper scripts for using CMake with the FRC toolchain.

%prep
rm -rf %{builddir}
mkdir -p %{builddir}
cd %{builddir}

%install
cp -r %{_sourcedir}/toolchain-builder .
cd %{_sourcedir}/toolchain-builder/tools
make -f frcmake-nix-makefile "DESTDIR=%{buildroot}" install

%files

%{_prefix}/arm-frc-linux-gnueabi/share/cmake/toolchain.cmake
%{_bindir}/frc-cmake-toolchain
%{_bindir}/frcmake

%changelog
* Wed Jan 17 2018 David Chen <david.chen9909@gmail.com> 4.4-1 
- Initial version of the package

