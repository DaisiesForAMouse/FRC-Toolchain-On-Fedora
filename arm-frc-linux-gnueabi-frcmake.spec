Name:           arm-frc-linux-gnueabi-frcmake
Version:        3
Release:        1%{?dist}
Summary:        Wrapper scripts for using CMake with the FRC toolchain

License:        GPLv3
URL:            https://github.com/wpilibsuite/toolchain-builder/
Source0:        toolchain.tar.gz

%description
Wrapper scripts for using CMake with the FRC toolchain.

%prep
rm -rf %{_builddir}
mkdir -p %{_builddir}
cd %{_builddir}
tar xf %{_sourcedir}/toolchain.tar.gz

%install
cd %{_builddir}/tools
make -f frcmake-nix-makefile "DESTDIR=%{buildroot}" install

%files
%{_prefix}/arm-frc-linux-gnueabi/share/cmake/toolchain.cmake
%{_bindir}/frc-cmake-toolchain
%{_bindir}/frcmake

%changelog
* Wed Jan 17 2018 David Chen <david.chen9909@gmail.com> 4.4-1
- Initial version of the package
-
