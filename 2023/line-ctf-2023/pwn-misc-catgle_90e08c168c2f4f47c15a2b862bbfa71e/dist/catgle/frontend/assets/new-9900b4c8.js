import{S as V,i as W,s as X,e as a,b as _,R as z,C as A,f as n,h as B,j as t,T as F,a4 as $,l as x,t as G,p as H,r as I,V as J,v as K,W as L,X as M,_ as O,$ as Q}from"./index-fc71ad6b.js";import{E as U}from"./Error-74362572.js";function Y(l){let o,i,b,u,m,e,r,d,C,c,w,p,v,E,f,S,j,y,h,T,D,k,q,N,P;return u=new U({props:{error:l[0]}}),{c(){o=a("div"),i=a("h5"),i.textContent="New question",b=_(),z(u.$$.fragment),m=_(),e=a("form"),r=a("div"),d=a("label"),d.textContent="Title",C=_(),c=a("input"),w=_(),p=a("div"),v=a("label"),v.textContent="Content",E=_(),f=a("textarea"),S=_(),j=a("span"),y=a("label"),h=a("input"),T=A(" markdown"),D=_(),k=a("button"),k.textContent="Post",n(i,"class","my-3 border-bottom pb-2"),n(d,"for","subject"),n(c,"type","text"),n(c,"class","form-control"),n(r,"class","mb-3"),n(v,"for","content"),n(f,"class","form-control"),n(f,"rows","10"),n(p,"class","mb-3"),n(h,"type","checkbox"),n(j,"class","d-flex justify-content-end"),n(k,"class","btn btn-primary"),n(e,"method","post"),n(e,"class","my-3"),n(o,"class","container my-3")},m(s,g){B(s,o,g),t(o,i),t(o,b),F(u,o,null),t(o,m),t(o,e),t(e,r),t(r,d),t(r,C),t(r,c),$(c,l[1]),t(e,w),t(e,p),t(p,v),t(p,E),t(p,f),$(f,l[2]),t(e,S),t(e,j),t(j,y),t(y,h),h.checked=l[3],t(y,T),t(e,D),t(e,k),q=!0,N||(P=[x(c,"input",l[5]),x(f,"input",l[6]),x(h,"change",l[7]),x(k,"click",l[4])],N=!0)},p(s,[g]){const R={};g&1&&(R.error=s[0]),u.$set(R),g&2&&c.value!==s[1]&&$(c,s[1]),g&4&&$(f,s[2]),g&8&&(h.checked=s[3])},i(s){q||(G(u.$$.fragment,s),q=!0)},o(s){H(u.$$.fragment,s),q=!1},d(s){s&&I(o),J(u),N=!1,K(P)}}}function Z(l,o,i){let b;L(l,M,p=>i(8,b=p));let u={detail:[]},m="",e="",r=!1;O()==!1&&b("/login");function d(p){p.preventDefault(),Q("post","/api/question/create",{subject:m,content:e,is_markdown:r},f=>{b("/forum")},f=>{i(0,u=f)})}function C(){m=this.value,i(1,m)}function c(){e=this.value,i(2,e)}function w(){r=this.checked,i(3,r)}return[u,m,e,r,d,C,c,w]}class nt extends V{constructor(o){super(),W(this,o,Z,Y,X,{})}}export{nt as default};