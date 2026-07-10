%global tl_name b1encoding
%global tl_revision 21271

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	LaTeX encoding tools for Bookhands fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/b1encoding
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package characterises and defines the author's B1 encoding for use
with LaTeX when typesetting things using his Bookhands fonts.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/b1encoding
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/source/latex/b1encoding
%dir %{_datadir}/texmf-dist/tex/latex/b1encoding
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/b1encoding
%doc %{_datadir}/texmf-dist/doc/latex/b1encoding/README
%doc %{_datadir}/texmf-dist/doc/latex/b1encoding/b1encoding.pdf
%{_datadir}/texmf-dist/fonts/enc/dvips/b1encoding/TeXB1.enc
%doc %{_datadir}/texmf-dist/source/latex/b1encoding/b1encoding.dtx
%doc %{_datadir}/texmf-dist/source/latex/b1encoding/b1encoding.ins
%{_datadir}/texmf-dist/tex/latex/b1encoding/b1cmr.fd
%{_datadir}/texmf-dist/tex/latex/b1encoding/b1enc.def
