$(document).ready(function(){
        var modify = $(".table-tb tbody tr");
         modify.each(function(i){
            $(this).attr("id","tr_" + i);
            $(this).children("td").children(".modify").on("click",function(){
                var houseid = $(this).parent().parent().children("td:eq(0)").text();
                $(this).html(houseid);
                var json_obj = {
                    houseId: $(this).parent().parent().children("td:eq(0)").text(),
                    houseTitle: $(this).parent().parent().children("td:eq(2)").text(),
                };
                var json_str = JSON.stringify(json_obj);
                $.post("/modify", json_str, "json");

            });
         })

        $(".small-img ul li").on({
            "mouseover":function(){
                $(this).children("img").css("border","1px solid #ffa100");
                $(this).siblings().children("img").css("border","0");
            },
            "click":function(){
                var imgurl = $(this).children("img").attr("src");
                $(".big-img img").attr("src",imgurl);
            }
        })
        $(".house-list a li").on({
            "mouseover":function(){
                $(this).css("background","#e7e7e7");
            },
            "mouseout":function(){
                $(this).css("background","#fff");
            },
        })
        $(".elems-l a").on({
            "mouseover":function(){
                $(this).css("color","#ffa011");
            },
            "mouseout":function(){
                $(this).css("color","#000");
            },
        })
        $("#id_headImg").parent().children("label").hide();
        $("#house-list a:first-child li").attr("class","fst-li");
        $("#id_username").attr("placeholder","用户名");
        $(".form-register li:eq(0) input").attr("placeholder","用户名");
        $(".form-register li:eq(1) input").attr("placeholder","密码");
        $("#id_password").attr("placeholder","密码");
        $(".form-register #id_email").attr("placeholder","Email");
        $(".errorlist").hide();
        $(".login-container").hide();
        $(".close span").on({
            "click": function(){
                $(".login-container").hide();
            },

        })
        $(".close span").on({
             "mouseover": function(){
                $(".close span").css("color","#ffa000");
            },
            "mouseout": function(){
                $(".close span").css("color","#999");
            },

        })
        $("header nav ul li a").on({
            "mouseover": function(){
                $(this).css("color","#10F1C2");
            },
            "mouseout": function(){
                $(this).css("color","#fff");
            },
        })
        $("header nav .login-nav #login").on({
            "click":function(){
                $("#login-container").show();
            },
        })
        $("header nav .login-nav #register").on({
            "click":function(){
                $("#register-container").show();
                $("#login-container").hide();
             },
        })
        $("#to-register").on({
            "click":function(){
                $("#register-container").show();
                $("#login-container").hide();

            },
        })
        $("#to-login").on({
            "click":function(){
                $("#login-container").show();
                $("#register-container").hide();
            },
        })

        var container=document.getElementById("history-content");
		var list=document.getElementById("list");
		var buttons=document.getElementById("buttons").getElementsByTagName("span");
		var prev=document.getElementById("prev");
		var next=document.getElementById("next");
		// 按钮标记
		var index=1;
		// 当切换时不应该再切换，切换结束再切换,运行时为true
		var animated=false;
		// 定时器
		var timer;

		var clientWidth = document.body.clientWidth * 0.42;
		var allCW = clientWidth * 5;
		var sevenCW = clientWidth * 7;
		console.log(sevenCW);
		$(".list").css("left",-clientWidth);
		$(".list").css("width",sevenCW);
		$(".list").css("height",clientWidth * 0.3);


		$(".history-content").css({"width":clientWidth * 1.8,"height":clientWidth * 0.5});
		$(".list img").css("width",clientWidth * 0.5);
		$(".list img").css("height",clientWidth * 0.3);
		$(".list img").css("padding-right","40px");
		$(".buttons").css({"left":clientWidth/2 + 180});
        function showButton(){
        	for(var i=0;i<buttons.length;i++){
        		if(buttons[i].className=="on"){
        			buttons[i].className="";
        			break;
        		}
        	}
        	buttons[index-1].className="on";
        }
		// 添加事件绑定
		// 当小于-3000变回-600，当大于-600变回-3000
		function animate (offset) {
			// body...
			if(offset==0){
				return;
			}
			animated=true;
			var newLeft=parseInt(list.style.left) + offset;
			// 位移总时间
			var time=400;
			// 位移间隔时间
			var interval=10;
			// 每一次的位移量
			var speed=offset/(time/interval);

			function go () {
				// body...
				// 向左移动
				if ( (speed > 0 && parseInt(list.style.left) < newLeft) || (speed < 0 && parseInt(list.style.left) > newLeft)) {
					list.style.left=parseInt(list.style.left)+speed+'px';
					// 递归
					setTimeout(go,interval);
				}else{
					list.style.left=newLeft+'px';
					if(newLeft>-clientWidth){
						list.style.left=-allCW+'px';
					}
					if(newLeft<-allCW){
						list.style.left=-clientWidth+'px';
					}
					animated=false;
				}
			}
			// debugger;
			go();
		}
		for (var i = 0; i < buttons.length; i++) {
			buttons[i].onclick=function(){
				if(this.className=='on'){
					// 当class当前为on时再点击时，就退出函数
					return;
				}
				var myIndex=parseInt(this.getAttribute('index'));
				// index是自定义的属性，getAttribute是DOM二级函数
				var offset=-clientWidth*(myIndex-index);
				// index当前的
				animate(offset);
				index=myIndex;
				showButton();
			}
		};
		next.onclick=function(){
			if(animated){
				return;
			}
			if(index==5){
				index=1;
			}else{
				index += 1;
			}
			showButton();
			animate(-clientWidth);
		};
		prev.onclick=function(){
			if(animated){
				return;
			}
			if(index==1){
				index=5
			}else{
				index -=1;
			}
			showButton();
			animate(clientWidth);
		};

		function play () {
			// body...
			timer=setTimeout(function(){
				next.onclick();
				play();
			},2500);

		}
		function stop () {
			// body...
			clearTimeout(timer);
		}
		container.onmouseout=play;
		container.onmouseover=stop;

		play();
		 $(".aPre").click(function(){
              htmlobj=$.ajax({url:"{{STATIC_URL}}/test.txt",async:false});
              $(".recommend").html(htmlobj.responseText);
         });

         // index.html
         //modify



    })