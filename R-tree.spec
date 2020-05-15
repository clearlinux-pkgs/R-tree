#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tree
Version  : 1.0.40
Release  : 64
URL      : https://cran.r-project.org/src/contrib/tree_1.0-40.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tree_1.0-40.tar.gz
Summary  : Classification and Regression Trees
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-tree-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-tree package.
Group: Libraries

%description lib
lib components for the R-tree package.


%prep
%setup -q -c -n tree
cd %{_builddir}/tree

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589565348

%install
export SOURCE_DATE_EPOCH=1589565348
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tree
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tree
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tree
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tree || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tree/DESCRIPTION
/usr/lib64/R/library/tree/INDEX
/usr/lib64/R/library/tree/Meta/Rd.rds
/usr/lib64/R/library/tree/Meta/features.rds
/usr/lib64/R/library/tree/Meta/hsearch.rds
/usr/lib64/R/library/tree/Meta/links.rds
/usr/lib64/R/library/tree/Meta/nsInfo.rds
/usr/lib64/R/library/tree/Meta/package.rds
/usr/lib64/R/library/tree/NAMESPACE
/usr/lib64/R/library/tree/R/tree
/usr/lib64/R/library/tree/R/tree.rdb
/usr/lib64/R/library/tree/R/tree.rdx
/usr/lib64/R/library/tree/help/AnIndex
/usr/lib64/R/library/tree/help/aliases.rds
/usr/lib64/R/library/tree/help/paths.rds
/usr/lib64/R/library/tree/help/tree.rdb
/usr/lib64/R/library/tree/help/tree.rdx
/usr/lib64/R/library/tree/html/00Index.html
/usr/lib64/R/library/tree/html/R.css
/usr/lib64/R/library/tree/po/en@quot/LC_MESSAGES/R-tree.mo
/usr/lib64/R/library/tree/po/en@quot/LC_MESSAGES/tree.mo
/usr/lib64/R/library/tree/po/pl/LC_MESSAGES/R-tree.mo
/usr/lib64/R/library/tree/po/pl/LC_MESSAGES/tree.mo
/usr/lib64/R/library/tree/tests/Examples/tree-Ex.Rout.save
/usr/lib64/R/library/tree/tests/cv.tree.R
/usr/lib64/R/library/tree/tests/deparse.R
/usr/lib64/R/library/tree/tests/no_obs.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tree/libs/tree.so
/usr/lib64/R/library/tree/libs/tree.so.avx2
/usr/lib64/R/library/tree/libs/tree.so.avx512
