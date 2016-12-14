/**
 * Created by yuanxiaobin on 16/12/13.
 */

function showimg(obj, type){

    var kpi = obj.id;
    var type = type;
    var starttime = $("#nav-starttime").val();
    var endtime   = $("#nav-endtime").val();
    var hostname  = $("#nav-hostname").val();

    var isornotchecked = obj.checked;
    <!--如果checkbox是选中的， 那么就是要画图，否则要把图删掉（或者从页面隐藏掉）-->
    if (isornotchecked){
        // 画图
        var divhtml  = "<div class='col-xs-12' style='min-width:400px;height:300px;padding-left: 1px;padding-right: 1px;' ";
        divhtml += ' id=div_' + kpi;
        divhtml += '></div>';
        $("#imgsdiv").after(divhtml);

        $.ajax({
            url:"api/kpi?",
            data:{
                "type": type,
                "tag": kpi,
                "serverName": hostname,
                "startTime": starttime,
                "endTime": endtime,
            },
            type: 'GET',
            dataType: 'json',
            success: function(result){
                drawpics(kpi, result);
                console.log(result);
            }
        });

    }else{
        // 将图删掉（从页面隐藏掉）
        $("#div_"+obj.id).remove();
    }
}

    function drawpics(kpi, data) {
        var div_name = "div_" + kpi;
        Highcharts.setOptions({
            global: { useUTC: false }

        });
        $('#'+div_name).highcharts({
            title: {
                text: kpi
            },
            chart: {
                zoomType:"x" //放大什么坐标上的数据 可以是x、y、xy
            },
            xAxis: {
                type: 'datetime',
                tickInterval: 3600 * 500,
                labels: {
                    formatter: function () {
                        return Highcharts.dateFormat('%y.%m.%d %H:%M', this.value);
                    }
                }
            },

            tooltip: {
                valueSuffix: '',
                xDateFormat: '%Y-%m-%d %H:%M:%S',
                crosshairs: true,
                shared: true
            },

            credits: {
                enabled: false
            },

            plotOptions: {
                series:{ lineWidth:1 }
            },
            series: [{
                name:"xx",
                data: data
            }]
        })

    }
