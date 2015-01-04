#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tree
Version  : 1.0
Release  : 12
URL      : http://cran.r-project.org/src/contrib/tree_1.0-35.tar.gz
Source0  : http://cran.r-project.org/src/contrib/tree_1.0-35.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n tree

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library tree
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-codoc -l %{buildroot}/usr/lib64/R/library tree


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tree/DESCRIPTION
/usr/lib64/R/library/tree/INDEX
/usr/lib64/R/library/tree/Meta/Rd.rds
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
/usr/lib64/R/library/tree/libs/symbols.rds
/usr/lib64/R/library/tree/libs/tree.so
/usr/lib64/R/library/tree/po/en@quot/LC_MESSAGES/R-tree.mo
/usr/lib64/R/library/tree/po/en@quot/LC_MESSAGES/tree.mo
/usr/lib64/R/library/tree/po/pl/LC_MESSAGES/R-tree.mo
/usr/lib64/R/library/tree/po/pl/LC_MESSAGES/tree.mo
