(this.webpackJsonpindra=this.webpackJsonpindra||[]).push([[0],{143:function(e,t,a){},205:function(e,t,a){e.exports=a.p+"static/media/Sandpile.090bc1a0.jpg"},206:function(e,t,a){e.exports=a.p+"static/media/sandpile_2.d38b3fb1.png"},207:function(e,t,a){e.exports=a.p+"static/media/mendelobrot_sq.875dd8b8.jpg"},244:function(e,t,a){e.exports=a(595)},591:function(e,t,a){},592:function(e,t,a){},595:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),l=a(11),o=a.n(l),c=a(112),i=a(74),s=a(51),u=a(81),d=a(620),m=a(627),p=a(629);var h=function(){return r.a.createElement(m.a,{bg:"light",expand:"lg"},r.a.createElement(p.a,{className:"mr-auto"},r.a.createElement(p.a.Link,{as:i.b,to:"/"},"HOME")),r.a.createElement(m.a.Toggle,{"aria-controls":"basic-navbar-nav"}),r.a.createElement(m.a.Collapse,{id:"basic-navbar-nav"},r.a.createElement(p.a,{className:"mr-auto"},r.a.createElement(p.a.Link,{href:"https://gcallah.github.io/indras_net/index.html"},"ABOUT"),r.a.createElement(p.a.Link,{href:"https://github.com/gcallah/indras_net/"},"SOURCE CODE"))))};function g(e){var t=e.children;return r.a.createElement(d.a,null,r.a.createElement("link",{rel:"stylesheet",href:"//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css"}),r.a.createElement(h,null),t)}g.defaultProps={children:{}};var v=g,b=a(10),f=a.n(b),E=a(25),y=a(19),k=a(20),O=a(21),S=a(22),D=a(626),j=a(621),P=a(625),x=a(152),N=a(229),w=a(219),C=a(52),I=a.n(C),_=(a(342),a(343),a(204)),B=a.n(_),M=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;Object(y.a)(this,a),(n=t.call(this,e)).renderImage=function(){var e=n.props,t=e.dots,a=e.speed,l=e.autoplay,o=e.className,c=e.data,i={arrows:!1,dots:t,infinite:!0,speed:a,slidesToShow:1,slidesToScroll:1,autoplay:l,fade:!0,className:o},s=function(){for(var e=n.state.imagesLoadedStatus,t=0;t<e.length;t+=1)if(!e[t])return!1;return!0};return r.a.createElement("div",null,r.a.createElement(B.a,i,c.map((function(e,t){return r.a.createElement("div",{key:e.title},s()?null:r.a.createElement("div",null,"Loading..."),r.a.createElement("img",{src:e.image,style:s()?{}:{display:"none"},className:"rounded-circle carousel",alt:"Responsive Model","data-toggle":"tooltip","data-placement":"top",title:e.title,onLoad:function(){var e=n.state.imagesLoadedStatus.slice();e[t]=!0,n.setState({imagesLoadedStatus:e})}}))}))))};var l=new Array(e.data.length).fill(!1);return n.state={imagesLoadedStatus:l},n}return Object(k.a)(a,[{key:"render",value:function(){return r.a.createElement("div",null,this.renderImage())}}]),a}(n.Component);M.defaultProps={dots:!1,speed:1e3,autoplay:!1,className:"",data:[]};var R=M,F=a(205),L=a.n(F),T=a(206),A=a.n(T),U=a(207),W=a.n(U),V=(a(143),"https://indrasnet.pythonanywhere.com/");Object({NODE_ENV:"production",PUBLIC_URL:"/indras_net",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0}).REACT_APP_API_URL&&(V=Object({NODE_ENV:"production",PUBLIC_URL:"/indras_net",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0}).REACT_APP_API_URL);var H={API_URL:V},K=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).renderChooseModelProp=function(){return r.a.createElement("h1",{className:"small-header"},"Please choose a model: ")},n.state={allItems:[],loadingData:!1,apiFailed:!1,dataForCarousel:[{image:L.a,title:"by Seth Terashima"},{image:A.a,title:"by Colt Browninga"},{image:W.a,title:"by Adam Majewski"}]},n.api_server=H.API_URL,n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){var t,a;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.props.history,e.prev=1,this.setState({loadingData:!0}),document.title="Home",e.next=6,I.a.get("".concat(this.api_server,"models"));case 6:a=e.sent,this.setState({allItems:a.data,loadingData:!1}),localStorage.setItem("indra_model_details",JSON.stringify(a.data)),e.next=14;break;case 11:e.prev=11,e.t0=e.catch(1),t.push("/errorCatching");case 14:case"end":return e.stop()}}),e,this,[[1,11]])})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state,t=e.loadingData,a=e.dataForCarousel,n=e.allItems;return e.apiFailed?r.a.createElement("h1",null,"404 Error"):t?r.a.createElement(D.a,{active:!0,inverted:!0},r.a.createElement(j.a,{size:"massive"},"Loading...")):r.a.createElement("div",{className:"container"},r.a.createElement("div",{className:"margin-bottom-80"},r.a.createElement("h1",{className:"text-left"},"Indra Agent-Based Modeling System")),r.a.createElement("div",{className:"row"},r.a.createElement(x.a,{sm:12,lg:4,className:"mb-5"},this.renderChooseModelProp(),r.a.createElement(P.a,null,r.a.createElement(P.a.Toggle,{variant:"outline-dark",id:"dropdown-basic"},"Choose..."),r.a.createElement(P.a.Menu,null,Object.keys(n).map((function(e){return"active"in n[e]&&!0!==n[e].active?null:r.a.createElement(N.a,{key:"".concat(n[e].name,"-tooltip"),placement:"right",overlay:r.a.createElement(w.a,null,n[e].doc)},r.a.createElement(i.b,{to:{pathname:"/models/props/".concat(n[e]["model ID"]),state:{menuId:n[e]["model ID"],name:n[e].name,source:n[e].source,graph:n[e].graph}},className:"link text-dark dropdown-item",key:n[e].name},n[e].name))}))))),r.a.createElement(x.a,{sm:12,lg:{cols:6,span:6,offset:2}},r.a.createElement(R,{speed:5e3,autoplay:!0,className:"col",data:a}))))}}]),a}(n.Component);K.defaultProps={history:{}};var z=K,q=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).state={loadingData:!1},n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this.setState({loadingData:!0}),document.title="Indra | Work in Progress",this.setState({loadingData:!1});case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return this.state.loadingData?r.a.createElement(D.a,{active:!0,inverted:!0},r.a.createElement(j.a,{size:"massive"},"Loading...")):r.a.createElement("div",null,r.a.createElement("br",null),r.a.createElement("h1",{style:{textAlign:"center"}},"Welcome to the Indra ABM platform!"),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("p",null,"We will have this model running soon!"),r.a.createElement("br",null),r.a.createElement("br",null))}}]),a}(n.Component),X=a(67),J=a(63);function Y(e){var t=e.label,a=e.name,n=e.type,l=e.placeholder,o=e.propChange,c=e.error;return r.a.createElement("div",{key:t,className:"form-group"},r.a.createElement("div",null,r.a.createElement("label",{htmlFor:a,className:"col-sm-4 col-md-4 col-lg-4",key:t},t," "," "),r.a.createElement("input",{id:a,type:n,className:"col-sm-2 col-md-2 col-lg-2",style:{fontSize:"15pt"},placeholder:l,onChange:o,name:a}),r.a.createElement("span",{className:"col-sm-6 col-md-6 col-lg-6",style:{color:"red",fontSize:12}},c),r.a.createElement("br",null)))}Y.defaultProps={label:"",name:"",type:"",placeholder:0,propChange:function(){},error:""};var $=Y;var G=function(){return r.a.createElement(D.a,{active:!0,inverted:!0},r.a.createElement(j.a,{size:"massive"},"Loading..."))},Q="".concat(H.API_URL,"models/props/"),Z=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;Object(y.a)(this,a),(n=t.call(this,e)).states=function(e){var t=n.state.modelDetails;Object.keys(t).forEach((function(t){n.setState((function(a){return{modelDetails:Object(J.a)({},a.modelDetails,Object(X.a)({},t,Object(J.a)({},a.modelDetails[t],{defaultVal:e[t].val})))}}))}))},n.errors=function(){var e=n.state.modelDetails;Object.keys(e).forEach((function(e){return n.setState((function(t){return{modelDetails:Object(J.a)({},t.modelDetails,Object(X.a)({},e,Object(J.a)({},t.modelDetails[e],{errorMessage:"",disabledButton:!1})))}}))}))},n.errorSubmit=function(){var e=n.state.modelDetails,t=!1;return Object.keys(e).forEach((function(a){t=t||e[a].disabledButton})),t},n.propChanged=function(e){var t=n.state.modelDetails,a=e.target,r=a.name,l=a.value,o=n.checkValidity(r,l);t[r].disabledButton=!0,1===o?(t[r].val=parseInt(l,10),t[r].errorMessage="",t[r].disabledButton=!1,n.setState({modelDetails:t})):-1===o?(t[r].errorMessage="**Wrong Input Type",t[r].val=t[r].defaultVal,n.setState({modelDetails:t})):(t[r].errorMessage="**Please input a number between ".concat(t[r].lowval," and ").concat(t[r].hival,"."),t[r].val=t[r].defaultVal,n.setState({modelDetails:t})),n.setState({disabledButton:n.errorSubmit()})},n.checkValidity=function(e,t){var a=n.state.modelDetails;return t<=a[e].hival&&t>=a[e].lowval?"INT"===a[e].atype&&!1===!!(t%1)||"DBL"===a[e].atype?1:-1:0},n.handleSubmit=function(){var e=Object(E.a)(f.a.mark((function e(t){var a,r,l,o,c,i,s,u,d,m;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t.preventDefault(),a=n.state,r=a.modelDetails,l=a.menuId,o=a.name,c=a.source,i=a.graph,s=n.props.history,e.prev=3,e.next=6,I.a.put(Q+l,r);case 6:u=e.sent,d=l,m=u.data,s.push({pathname:"/models/menu/".concat(d.toString(10)),state:{envFile:m,name:o,source:c,graph:i}}),e.next=15;break;case 12:e.prev=12,e.t0=e.catch(3),s.push("/errorCatching");case 15:case"end":return e.stop()}}),e,null,[[3,12]])})));return function(t){return e.apply(this,arguments)}}(),n.renderHeader=function(){var e=n.state.name;return r.a.createElement("h1",{className:"header",style:{textAlign:"center",fontWeight:"200"}},"Please set the parameters for the ".concat(e," model"))},n.renderSubmitButton=function(){var e=n.state.disabledButton;return r.a.createElement("button",{type:"button",disabled:e,onClick:e?null:n.handleSubmit,className:"btn btn-primary m-2"},"Submit")},n.goback=function(){n.props.history.goBack()};var l=n.getInitialModelDetails();return n.state=Object(J.a)({modelDetails:{},loadingData:!1,disabledButton:!1},l),n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){var t,a,n;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.props.history,a=this.state.menuId,e.prev=2,document.title="Indra | Property",this.setState({loadingData:!0}),e.next=7,I.a.get("".concat(Q).concat(a));case 7:n=e.sent,this.setState({modelDetails:n.data}),this.states(n.data),this.errors(n.data),this.setState({loadingData:!1}),e.next=17;break;case 14:e.prev=14,e.t0=e.catch(2),t.push("/errorCatching");case 17:case"end":return e.stop()}}),e,this,[[2,14]])})));return function(){return e.apply(this,arguments)}}()},{key:"getInitialModelDetails",value:function(){var e,t=this.props,a=t.location,n=t.history,r=t.match;try{var l=a.state;if(void 0===l){var o=parseInt(r.params.id,10),c=JSON.parse(localStorage.getItem("indra_model_details")).filter((function(e){return e["model ID"]===o}))[0];e={menuId:o,name:c.name,source:c.source,graph:c.graph}}else e=l}catch(i){n.push("/errorCatching")}return e}},{key:"render",value:function(){var e=this,t=this.state,a=t.loadingData,n=t.modelDetails;return a?r.a.createElement(G,null):r.a.createElement("div",null,r.a.createElement("h1",{className:"margin-top-60"}," "),this.renderHeader(),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("form",null,r.a.createElement("div",{className:"container"},Object.keys(n).map((function(t){return"question"in n[t]?r.a.createElement($,{label:n[t].question,type:n[t].atype,placeholder:n[t].val,error:n[t].errorMessage,propChange:e.propChanged,name:t,key:t}):null})))),r.a.createElement("br",null),r.a.createElement("br",null),this.renderSubmitButton())}}]),a}(n.Component);Z.defaultProps={history:{},location:{state:{}},match:{params:{id:""}}};var ee=Z,te=a(61),ae=a(157),ne=a(77),re=a.n(ne),le=a(78),oe=(a(147),a(156)),ce=function(e){var t=e.title,a=e.children;return r.a.createElement(oe.a,null,r.a.createElement("h5",{style:{textAlign:"center",fontSize:16},className:"card-header bg-primary text-white"},t),r.a.createElement(oe.a.Body,null,a))};function ie(e){var t=["red","green","blue","black","purple","magenta","orange"],a=0,n=e.loadingData,l=e.envFile;if(n){var o=[],c=e.envFile.pop_hist.pops;return Object.keys(c).forEach((function(e,n){o.push({name:e,color:l.members[e]?l.members[e].attrs.color:t[a%7],data:{}}),Object.keys(c[e]).forEach((function(t,a){o[n].data[t]=c[e][a]})),a+=1})),r.a.createElement(ce,{title:"Population Graph"},r.a.createElement(le.b,{data:o,width:"600px",height:"600px"}))}return null}ie.defaultProps={loadingData:!0,envFile:{}};var se=ie;function ue(e){var t=["red","green","blue","black","purple","magenta","orange"],a=0,n=[],l=e.loadingData,o=e.envFile;if(l){var c=[],i=e.envFile.pop_hist.pops;return Object.keys(i).forEach((function(e,r){c.push({name:e,color:o.members[e]?o.members[e].attrs.color:t[a%7],data:{}}),Object.keys(i[e]).forEach((function(t,a){c[r].data[t]=i[e][a]})),a+=1,n=c.map((function(e){var t=Object.keys(e.data).map((function(t){return e.data[t]})).reduce((function(e,t){return e+t}),0);return[e.name,t]}))})),console.log(n),r.a.createElement(ce,{title:"Population Bar Graph"},r.a.createElement(le.a,{data:n,width:"600px",height:"600px"}))}return null}ue.defaultProps={loadingData:!0,envFile:{}};var de=ue;function me(e){var t=e.loadingData,a=e.envFile,n=(e.id,{tree:"triangle",square:"rect",person:"circle",deceased:"circle",circle:"circle",default:"circle"});if(t){var l=a.members,o=[],c={pointStyle:"circle"};return Object.keys(l).forEach((function(e,t){o.push({name:l[e].name,color:l[e].attrs.color,data:[]});var a=l[e].attrs.marker;c.pointStyle=a in n?n[l[e].attrs.marker]:"circle",Object.keys(l[e].members).forEach((function(a){null!==l[e].members[a].pos&&o[t].data.push(l[e].members[a].pos)}))})),r.a.createElement(ce,{title:"Scatter Plot"},r.a.createElement(le.c,{dataset:c,data:o,width:"600px",height:"600px"}))}return null}me.defaultProps={loadingData:!0,envFile:{},id:0};var pe=me,he=a(220),ge=a.n(he);function ve(e){var t=e.envFile;return e.loadingData?r.a.createElement(ce,{title:"Model Data"},r.a.createElement(ge.a,{src:t})):null}ve.defaultProps={envFile:{},loadingData:!0};var be=ve,fe=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;Object(y.a)(this,a),n=t.call(this,e),re()(Object(te.a)(n));var r=n.props,l=r.msg,o=r.title;return n.state={msg:l,title:o},n}return Object(k.a)(a,[{key:"render",value:function(){var e=this.state,t=e.msg,a=e.title;return r.a.createElement("div",null,r.a.createElement("div",{className:"card w-50 model-status"},r.a.createElement("h5",{style:{textAlign:"center",fontSize:16},className:"card-header bg-primary text-white"},a),r.a.createElement("div",{className:"card-body overflow-auto"},r.a.createElement("pre",{className:"card-text"},t))))}}],[{key:"getDerivedStateFromProps",value:function(e,t){return e.msg!==t.msg?{msg:e.msg}:null}}]),a}(r.a.Component);fe.defaultProps={msg:"",title:""};var Ee=a(628),ye=a(623),ke=function(e){var t=e.loadingData,a=e.code;return t?r.a.createElement(ce,{title:"Source Code"},r.a.createElement(Ee.a,{language:"python",style:ye.a},a)):null};ke.defaultProps={loadingData:!0,code:""};var Oe=ke,Se=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;return Object(y.a)(this,a),n=t.call(this,e),re()(Object(te.a)(n)),n.state={disabledButton:e.disabledButton,errorMessage:e.errorMessage,sendNumPeriods:e.sendNumPeriods,handleRunPeriod:e.handleRunPeriod},n}return Object(k.a)(a,[{key:"render",value:function(){var e=this.state,t=e.disabledButton,a=e.sendNumPeriods,n=e.handleRunPeriod,l=e.errorMessage;return r.a.createElement("div",null,r.a.createElement("button",{type:"button",disabled:t,onClick:t?null:a,className:"btn btn-success m-2"},"  ","Run","  ")," ",r.a.createElement("span",null,"model for")," ",r.a.createElement("input",{type:"INT",className:"from-control m-2 number-input",style:{width:"40px"},placeholder:"10",onChange:n})," ","periods.",r.a.createElement("span",{className:"error-message"},l))}}]),a}(r.a.Component);Se.defaultProps={disabledButton:!0,errorMessage:"",sendNumPeriods:function(){},handleRunPeriod:function(){}};var De=function(e){var t=e.loadingData,a=e.envFile;return t?r.a.createElement(ce,{title:"Logs"},r.a.createElement("div",{style:{whiteSpace:"pre-line"}},a.user.debug||"Run the model to see the logs")):null};De.defaultProps={loadingData:!0,envFile:{}};var je=De,Pe="".concat(H.API_URL,"models/menu/"),xe="".concat(H.API_URL,"registry/clear/"),Ne=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;Object(y.a)(this,a),(n=t.call(this,e)).viewSource=Object(E.a)(f.a.mark((function e(){var t,a,r,l;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,t=n.state.source,a=t.split("/"),r=a[a.length-1],e.next=6,I.a.get("https://raw.githubusercontent.com/gcallah/indras_net/master/models/".concat(r));case 6:return l=e.sent,e.abrupt("return",l.data);case 10:return e.prev=10,e.t0=e.catch(0),e.abrupt("return","Something has gone wrong.");case 13:case"end":return e.stop()}}),e,null,[[0,10]])}))),n.handleRunPeriod=function(e){n.setState({periodNum:e.target.value}),0===n.checkValidity(e.target.value)?n.setState({errorMessage:"**Please input an integer",disabledButton:!0}):n.setState({errorMessage:"",disabledButton:!1})},n.checkValidity=function(e){return e%1===0?1:0},n.handleClick=function(e){switch(n.setState({loadingData:!1,loadingSourceCode:!1,loadingDebugger:!1,loadingScatter:!1,loadingPopulation:!1,loadingLogs:!1,loadingBar:!1}),n.setState({activeDisplay:e}),e){case 2:n.setState({loadingPopulation:!0});break;case 3:n.setState({loadingScatter:!0});break;case 5:n.setState({loadingDebugger:!0});break;case 6:n.setState({loadingSourceCode:!0});break;case 7:n.setState({loadingLogs:!0});break;case 4:n.setState({loadingBar:!0})}},n.sendNumPeriods=Object(E.a)(f.a.mark((function e(){var t,a,r,l,o,c;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.state,a=t.periodNum,r=t.envFile,l=t.EXECUTION_KEY,console.log("Sending execution key",l),o=Object(J.a)({},r,{execution_key:l}),n.setState({loadingData:!0}),e.prev=4,e.next=7,I.a.put("".concat(H.API_URL,"models/run/").concat(String(a)),o,a);case 7:c=e.sent,n.setState({envFile:c.data,loadingData:!1,msg:c.data.user.user_msgs}),e.next=13;break;case 11:e.prev=11,e.t0=e.catch(4);case 13:case"end":return e.stop()}}),e,null,[[4,11]])}))),n.timeout=function(e){return new Promise((function(t){return setTimeout(t,e)}))},n.continuousRun=Object(E.a)(f.a.mark((function e(){return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n.setState({continuousRun:!0,continuousRunDisabled:!0,periodNum:1,initLoading:!1}),e.next=3,n.timeout(200);case 3:if(!n.state.continuousRun){e.next=14;break}n.sendNumPeriods();case 5:if(!n.state.loadingData){e.next=11;break}return e.next=8,n.timeout(200);case 8:console.log("still waiting for data..."),e.next=5;break;case 11:console.log("data arrived!!"),e.next=3;break;case 14:case"end":return e.stop()}}),e)}))),n.stopRun=function(){n.setState({continuousRun:!1,continuousRunDisabled:!1})},n.renderHeader=function(){var e=n.state.name;return r.a.createElement("h1",{className:"header"},e)},n.MenuItem=function(e,t,a,l){var o=n.state.graph,c=n.state.activeDisplay;return r.a.createElement(ae.a.Item,{className:"w-50 p-3 list-group-item list-group-item-action",as:"li",active:c===t,disabled:3===t&&"line"===o||2===t&&"scatter"===o,key:l,onClick:function(){return n.handleClick(t)}},a)},n.renderMenuItem=function(){var e=n.state,t=e.envFile,a=e.loadingDebugger,l=e.loadingSourceCode,o=e.sourceCode,c=e.loadingPopulation,i=e.loadingScatter,s=e.loadingLogs,u=e.loadingBar;return r.a.createElement("div",{className:"mt-5"},r.a.createElement(be,{loadingData:a,envFile:t}),r.a.createElement(Oe,{loadingData:l,code:o}),r.a.createElement(se,{loadingData:c,envFile:t}),r.a.createElement(de,{loadingData:u,envFile:t}),r.a.createElement(pe,{loadingData:i,envFile:t}),r.a.createElement(je,{loadingData:s,envFile:t}))},n.renderMapItem=function(){var e=n.state.menu;return r.a.createElement("div",{className:"row margin-bottom-80"},r.a.createElement("div",{className:"col w-25"},r.a.createElement(ae.a,null,Object.keys(e).map((function(t,a){return e[t].id>1?n.MenuItem(a,e[t].id,e[t].question,e[t].func):null})))))};var l=n.props.location.state.envFile;return n.state={menu:{},loadingData:!0,envFile:{},source:"",periodNum:10,errorMessage:"",disabledButton:!1,loadingSourceCode:!1,loadingDebugger:!1,loadingPopulation:!1,loadingScatter:!1,loadingBar:!1,loadingLogs:!1,activeDisplay:null,continuousRun:!0,continuousRunDisabled:!1,initLoading:!0,EXECUTION_KEY:l.execution_key},re()(Object(te.a)(n)),n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){var t,a,n,r,l,o,c,i,s;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.state.EXECUTION_KEY,a=this.props.location,n=a.state,r=n.envFile,l=n.name,o=n.source,c=n.graph,e.prev=4,document.title="Indra | Menu",e.next=8,I.a.get("".concat(Pe).concat(t));case 8:i=e.sent,this.setState({menu:i.data,name:l,source:o,envFile:r,graph:c,msg:r.user.user_msgs,loadingData:!1}),e.next=15;break;case 12:return e.prev=12,e.t0=e.catch(4),e.abrupt("return",!1);case 15:return"scatter"===c?this.setState({loadingScatter:!0,activeDisplay:3}):this.setState({loadingPopulation:!0,activeDisplay:2}),e.prev=17,e.next=20,this.viewSource();case 20:s=e.sent,this.setState({sourceCode:s}),e.next=27;break;case 24:return e.prev=24,e.t1=e.catch(17),e.abrupt("return",!1);case 27:return e.abrupt("return",!0);case 28:case"end":return e.stop()}}),e,this,[[4,12],[17,24]])})));return function(){return e.apply(this,arguments)}}()},{key:"componentWillUnmount",value:function(){var e=Object(E.a)(f.a.mark((function e(){var t;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.state.EXECUTION_KEY,e.next=3,I.a.get("".concat(xe).concat(t));case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state,t=e.loadingData,a=e.msg,n=e.disabledButton,l=e.errorMessage,o=e.initLoading,c=e.continuousRunDisabled;return t&&o?r.a.createElement(G,null):r.a.createElement("div",null,this.renderHeader(),r.a.createElement("div",null,r.a.createElement(fe,{title:"Model Status",msg:a,ref:this.modelStatusBoxElement})),r.a.createElement("ul",{className:"list-group"},r.a.createElement("div",{className:"row"},r.a.createElement("div",null,r.a.createElement(Se,{disabledButton:n,errorMessage:l,sendNumPeriods:this.sendNumPeriods,handleRunPeriod:this.handleRunPeriod}),r.a.createElement("button",{onClick:this.continuousRun,disabled:c,className:"btn btn-success m-2"},"Continuous Run"),r.a.createElement("button",{onClick:this.stopRun,className:"btn btn-danger m-2"},"Stop"),r.a.createElement("h3",{className:"margin-top-50 mb-4"},"Model Analysis:"))),this.renderMapItem()),this.renderMenuItem())}}]),a}(n.Component);Ne.defaultProps={location:{state:{envFile:{}}},history:{}};var we=Ne,Ce=(a(591),function(e){var t=e.code,a=e.children;return r.a.createElement(s.a,{render:function(e){var n=e.staticContext;return n&&(n.status=t),a}})});Ce.defaultProps={code:0,children:{}};var Ie=function(){return r.a.createElement(Ce,{code:404},r.a.createElement("div",{className:"NotFoundPage"},r.a.createElement("h1",null,"Oops!"),r.a.createElement("div",null,"Page not found."),r.a.createElement("div",{className:"action"},r.a.createElement("a",{className:"btn btn-primary",href:"/"},"Guide me to the right path!"))))},_e=function(e){Object(S.a)(a,e);var t=Object(O.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).state={loadingData:!1},n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this.setState({loadingData:!0}),document.title="Indra | Work in Progress",this.setState({loadingData:!1});case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return this.state.loadingData?r.a.createElement(D.a,{active:!0,inverted:!0},r.a.createElement(j.a,{size:"massive"},"Loading...")):r.a.createElement("div",null,r.a.createElement("br",null),r.a.createElement("h1",{style:{textAlign:"center"}},"Indra ABM platform"),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("p",null,"We are encountering some problems with the API server. We will have this model running soon!"),r.a.createElement("br",null),r.a.createElement("br",null))}}]),a}(n.Component);function Be(){var e=Object(c.a)(["\n  background: ",';\n  width: 100vw;\n  min-height: 100vh;\n  font-family: -apple-stem, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen";\n  h1 {\n    color: ',";\n  }\n"]);return Be=function(){return e},e}var Me=Object(u.b)("div")(Be(),(function(e){return e.theme.background}),(function(e){return e.theme.body}));function Re(){return r.a.createElement(s.c,null,r.a.createElement(s.a,{exact:!0,path:"/",component:z}),r.a.createElement(s.a,{exact:!0,path:"/wip",component:q}),r.a.createElement(s.a,{exact:!0,path:"/models/props/:id",component:ee}),r.a.createElement(s.a,{exact:!0,path:"/models/menu/:id",component:we}),r.a.createElement(s.a,{exact:!0,path:"/errorCatching",component:_e}),r.a.createElement(s.a,{component:Ie}))}var Fe=Object(u.c)((function(){return r.a.createElement(Me,null,r.a.createElement(i.a,null,r.a.createElement(v,null,r.a.createElement(Re,null))))})),Le=(a(592),a(593),a(594),a(230)),Te=a(231),Ae=a(624),Ue=a(48),We=a(96),Ve=a.n(We),He=Ve()("mode",{light:"#fafafa",dark:"#222"}),Ke=Ve()("mode",{light:"#000",dark:"#fff"});Ve()("mode",{light:"#222",dark:"#eee"}),Ve()("mode",{light:"#eee",dark:"#222"});function ze(){var e=Object(c.a)(["\n    background-color: ",";\n    color: ",";\n  "]);return ze=function(){return e},e}var qe=r.a.createContext(),Xe=Object(Ue.a)((function(e){return{root:{width:42,height:26,padding:0,margin:e.spacing(1)},switchBase:{padding:1,"&$checked":{transform:"translateX(16px)",color:e.palette.common.white,"& + $track":{backgroundColor:"#060606",opacity:1,border:"none"}},"&$focusVisible $thumb":{color:"#060606",border:"6px solid #fff"}},thumb:{width:24,height:24},track:{borderRadius:13,border:"1px solid ".concat(e.palette.grey[400]),backgroundColor:e.palette.grey[50],opacity:1,transition:e.transitions.create(["background-color","border"])},checked:{},focusVisible:{}}}))((function(e){var t=e.classes,a=Object(Te.a)(e,["classes"]);return r.a.createElement(Ae.a,Object.assign({focusVisibleClassName:t.focusVisible,disableRipple:!0,classes:{root:t.root,switchBase:t.switchBase,thumb:t.thumb,track:t.track,checked:t.checked}},a))})),Je=function(e){var t=e.children,a=r.a.useState({mode:"light",checkedB:!0}),n=Object(Le.a)(a,2),l=n[0],o=n[1],c=u.b.div(ze(),He,Ke),i=function(e){return function(t){var a="light"===l.mode?"dark":"light";o(Object(X.a)({mode:a},e,t.target.checked))}};return r.a.createElement(qe.Provider,{value:{toggle:i}},r.a.createElement(u.a,{theme:{mode:l.mode}},r.a.createElement(c,null,r.a.createElement(Xe,{checked:l.checkedB,onChange:i("checkedB"),value:"checkedB"}),t)))};o.a.render(r.a.createElement(Je,null,r.a.createElement(Fe,null)),document.getElementById("root"))}},[[244,1,2]]]);
//# sourceMappingURL=main.423d2d0a.chunk.js.map