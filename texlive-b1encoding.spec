# revision 21271
# category Package
# catalog-ctan /macros/latex/contrib/b1encoding
# catalog-date 2011-02-01 08:52:21 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-b1encoding
Version:	1.0
Release:	11
Summary:	LaTeX encoding tools for Bookhands fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/b1encoding
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package characterises and defines the author's B1 encoding
for use with LaTeX when typesetting things using his Bookhands
fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/b1encoding/TeXB1.enc
%{_texmfdistdir}/tex/latex/b1encoding/b1cmr.fd
%{_texmfdistdir}/tex/latex/b1encoding/b1enc.def
%doc %{_texmfdistdir}/doc/latex/b1encoding/README
%doc %{_texmfdistdir}/doc/latex/b1encoding/b1encoding.pdf
#- source
%doc %{_texmfdistdir}/source/latex/b1encoding/b1encoding.dtx
%doc %{_texmfdistdir}/source/latex/b1encoding/b1encoding.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 749442
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 717876
- texlive-b1encoding
- texlive-b1encoding
- texlive-b1encoding
- texlive-b1encoding
- texlive-b1encoding

