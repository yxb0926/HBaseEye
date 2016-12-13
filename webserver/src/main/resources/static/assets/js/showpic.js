/**
 * Created by yuanxiaobin on 16/12/13.
 */

function showimg(obj){
    //var kpix       = obj.id;
    //var starttime = $("#nav-starttime").val();
    //var endtime   = $("#nav-endtime").val();
    //var hostname  = $("#nav-hostname").val()+'.niceprivate.com';
    //var portx     = $("#nav-port").val();

    alert("xxxxxxxxxxxxxxx");
    var isornotchecked = obj.checked;
    <!--如果checkbox是选中的， 那么就是要画图，否则要把图删掉（或者从页面隐藏掉）-->
    if (isornotchecked){
        // 画图
        var divhtml  = "<div class='col-xs-12' style='min-width:400px;height:300px;padding-left: 1px;padding-right: 1px;' "
        divhtml += ' id=div_' + kpix
        divhtml += '></div>'
        $("#imgsdiv").after(divhtml);

        //var URL  = "http://127.0.0.1/mysqlapi/mysqlpickpi?"
        var URL  = "http://monitor.niceprivate.com/mysqlapi/mysqlpickpi?"
        URL += "kpi=" + kpix
        URL += "&hostname=" + hostnamex
        URL += "&port=" + portx
        URL += "&starttime=" + starttimex
        URL += "&endtime=" + endtimex

        $.ajax({
            type: 'GET',
            contentType: "application/json",
            url: URL,
            dataType: 'json',
            success: function(result){
                drawpics(kpix, result[0]);
            }
        });

    }else{
        // 将图删掉（从页面隐藏掉）
        $("#div_"+obj.id).remove();
    }
}
