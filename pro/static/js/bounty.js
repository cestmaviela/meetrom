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
            alert("no node....");
        }
        else
        {
            alert(msg);
            var json_msg = eval(msg)
            for (var i = 0; i < json_msg.length; i++) 
            {
                alert(json_msg[i]);
            }
        }
    });
}