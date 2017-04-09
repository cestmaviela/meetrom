//测试用例
function test()
{
	alert("I am in testing ......");
}

//设置城市
function set_addr(addr_node_id)
{
     $.post("/set/addr",
    {
        str_node_id:addr_node_id
    },
    function(msg,status)
    {
        if (msg=="")
        {
            location.reload();
        }
        else
        {
            alert(msg);
        }
    });
}

//设置城市并把回到上一页
function set_addr_go_back(addr_node_id)
{
     $.post("/set/addr",
    {
        str_node_id:addr_node_id
    },
    function(msg,status)
    {
        if (msg=="")
        {
            location.href = document.referrer
        }
        else
        {
            alert(msg);
        }
    });
}

//设置房租出租选择数据获取
function set_fangwu_chaxun()
{
     $.post("/fangwuchaxun",
    {
        man:'male'
    },
    function(msg,status)
    {
        if (msg=="")
        {
            alert("此城市没有登入房产平台信息");
        }
        else
        {
            alert(msg);
            var json_msg = eval(msg);
            var list_city_name_id = json_msg[0];
            var str_city_labels = ("<label for='child_city'> <input type='radio' value='0' style='visibility: hidden;' name='child_city' id='0'/> 不限 </label>");
            for (var i = 0; i <list_city_name_id.length; i++) {
                var map_city_name_id = list_city_name_id[i];
                var city_val = map_city_name_id['id'];
                var city_id = ("city"+map_city_name_id['id']);
                var city_name = map_city_name_id['city_name'];
                var str_city_label = ("<label for='child_city'> <input type='radio' value=" + city_val +" style='visibility: hidden;' name='child_city' id='"+ city_id +"'/>"+ city_name +"</label>");
                str_city_labels += str_city_label;                
            }
            $("#child_city_names").html(str_city_labels);

            var list_fangzu = json_msg[1];
            var str_fangzu_labels = ("<p><label for='fang_zus'> 租金:</label>");
            for (var i = 0; i < list_fangzu.length; i++) {
                var fangzu_val = list_fangzu[i]
                var fangzu_name ='';
                if (i == 0)
                {
                    fangzu_name = (list_fangzu[i] + "元以下");
                }
                else if (i == (list_fangzu.length-1)) 
                {
                    fangzu_name = (list_fangzu[i] + "元以上");
                }
                else
                {
                    fangzu_name = (list_fangzu[i] + "-"+list_fangzu[i+1] + "元");
                }
                var fangzu_id = ("fangzu"+ str(i))
                var str_fangzu_label = ("<label for='fang_zus'> <input type='radio' value=" + fangzu_val +" style='visibility: hidden;' name='fang_zu' id='"+ fangzu_id +"'/>"+ fangzu_name +"</label>");
                str_fangzu_labels += str_fangzu_label;
            }
            var str_input_submit = ("<label for='pricestart'> <input type='text' style='width:70px;height:20px;'' name='pricestart' id='price_start'/> — </label><label for='priceend'> <input type='text' style='width:70px;height:20px;'' name='priceend' id='price_end'/></label><label for='subbtn'> <button type='btn btn-default'  style='height:20px;'' name='subbtn' id='sub_btn' onclick='set_fangwu_chaxun()'' />价格筛选</label>");
            str_fangzu_labels += str_input_submit;
            str_fangzu_labels += "</p>";
            $("#city_fangzu_levels").html(str_fangzu_labels);
        }
    });
}