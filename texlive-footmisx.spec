Name:		texlive-footmisx
Version:	42621
Release:	2
Summary:	A range of footnote options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footmisx
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This a fork of footmisc package allowing to use hyperref. Here
is a copy of the description of package footmisc: A collection
of ways to change the typesetting of footnotes. The package
provides means of changing the layout of the footnotes
themselves (including setting them in 'paragraphs' -- the para
option), a way to number footnotes per page (the perpage
option), to make footnotes disappear in a 'moving' argument
(stable option) and to deal with multiple references to
footnotes from the same place (multiple option). The package
also has a range of techniques for labelling footnotes with
symbols rather than numbers. Some of the functions of the
package are overlap with the functionality of other packages.
The para option is also provided by the manyfoot and bigfoot
packages, though those are both also portmanteau packages.
(Don't be seduced by fnpara, whose implementation is improved
by the present package.) The perpage option is also offered by
footnpag and by the rather more general-purpose perpage

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/footmisx
%{_texmfdistdir}/tex/latex/footmisx
%doc %{_texmfdistdir}/doc/latex/footmisx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
