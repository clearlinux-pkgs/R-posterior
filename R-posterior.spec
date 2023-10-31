#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-posterior
Version  : 1.5.0
Release  : 18
URL      : https://cran.r-project.org/src/contrib/posterior_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/posterior_1.5.0.tar.gz
Summary  : Tools for Working with Posterior Distributions
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-abind
Requires: R-checkmate
Requires: R-distributional
Requires: R-matrixStats
Requires: R-pillar
Requires: R-rlang
Requires: R-tensorA
Requires: R-tibble
Requires: R-vctrs
BuildRequires : R-abind
BuildRequires : R-checkmate
BuildRequires : R-distributional
BuildRequires : R-matrixStats
BuildRequires : R-pillar
BuildRequires : R-rlang
BuildRequires : R-tensorA
BuildRequires : R-tibble
BuildRequires : R-vctrs
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
for fitting Bayesian models or working with output from Bayesian models.

%prep
%setup -q -n posterior
pushd ..
cp -a posterior buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698768118

%install
export SOURCE_DATE_EPOCH=1698768118
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/posterior/CITATION
/usr/lib64/R/library/posterior/DESCRIPTION
/usr/lib64/R/library/posterior/INDEX
/usr/lib64/R/library/posterior/LICENSE
/usr/lib64/R/library/posterior/Meta/Rd.rds
/usr/lib64/R/library/posterior/Meta/features.rds
/usr/lib64/R/library/posterior/Meta/hsearch.rds
/usr/lib64/R/library/posterior/Meta/links.rds
/usr/lib64/R/library/posterior/Meta/nsInfo.rds
/usr/lib64/R/library/posterior/Meta/package.rds
/usr/lib64/R/library/posterior/Meta/vignette.rds
/usr/lib64/R/library/posterior/NAMESPACE
/usr/lib64/R/library/posterior/NEWS.md
/usr/lib64/R/library/posterior/R/posterior
/usr/lib64/R/library/posterior/R/posterior.rdb
/usr/lib64/R/library/posterior/R/posterior.rdx
/usr/lib64/R/library/posterior/R/sysdata.rdb
/usr/lib64/R/library/posterior/R/sysdata.rdx
/usr/lib64/R/library/posterior/doc/index.html
/usr/lib64/R/library/posterior/doc/posterior.R
/usr/lib64/R/library/posterior/doc/posterior.Rmd
/usr/lib64/R/library/posterior/doc/posterior.html
/usr/lib64/R/library/posterior/doc/rvar.R
/usr/lib64/R/library/posterior/doc/rvar.Rmd
/usr/lib64/R/library/posterior/doc/rvar.html
/usr/lib64/R/library/posterior/help/AnIndex
/usr/lib64/R/library/posterior/help/aliases.rds
/usr/lib64/R/library/posterior/help/figures/logo.svg
/usr/lib64/R/library/posterior/help/figures/stanlogo.png
/usr/lib64/R/library/posterior/help/paths.rds
/usr/lib64/R/library/posterior/help/posterior.rdb
/usr/lib64/R/library/posterior/help/posterior.rdx
/usr/lib64/R/library/posterior/html/00Index.html
/usr/lib64/R/library/posterior/html/R.css
/usr/lib64/R/library/posterior/tests/testthat.R
/usr/lib64/R/library/posterior/tests/testthat/test-as_draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-bind_draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-convergence.R
/usr/lib64/R/library/posterior/tests/testthat/test-discrete-summaries.R
/usr/lib64/R/library/posterior/tests/testthat/test-draws-index.R
/usr/lib64/R/library/posterior/tests/testthat/test-extract_variable.R
/usr/lib64/R/library/posterior/tests/testthat/test-extract_variable_matrix.R
/usr/lib64/R/library/posterior/tests/testthat/test-for_each_draw.R
/usr/lib64/R/library/posterior/tests/testthat/test-merge_chains.R
/usr/lib64/R/library/posterior/tests/testthat/test-mutate_variables.R
/usr/lib64/R/library/posterior/tests/testthat/test-pareto_smooth.R
/usr/lib64/R/library/posterior/tests/testthat/test-print.R
/usr/lib64/R/library/posterior/tests/testthat/test-remove_variables.R
/usr/lib64/R/library/posterior/tests/testthat/test-rename_variables.R
/usr/lib64/R/library/posterior/tests/testthat/test-repair_draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-resample_draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-rhat_nested.R
/usr/lib64/R/library/posterior/tests/testthat/test-rstar.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-apply.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-bind.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-cast.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-dim.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-dist.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-factor.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-math.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-print.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-rfun.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-slice.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-summaries-over-draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-rvar-summaries-within-draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-split_chains.R
/usr/lib64/R/library/posterior/tests/testthat/test-subset_draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-summarise_draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-thin_draws.R
/usr/lib64/R/library/posterior/tests/testthat/test-variables.R
/usr/lib64/R/library/posterior/tests/testthat/test-weight_draws.R
