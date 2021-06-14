//出行方式排行
$(function () {
    var myChart = echarts.init(document.getElementById('container12'));
    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: {
            x: 46,
            y: 30,
            x2: 32,
            y2: 40,
            borderWidth: 0
        },
        xAxis: {
            type: 'value',
            x: '180',
            splitLine: {
                show: false
            },
            axisLabel: {
                show: true,
                textStyle: {
                    color: '#a4a7ab'
                }
            }
        },
        yAxis: {
            type: 'category',
            data: ['其他', '飞机', '火车', '自驾游', '长途皮车'],
            splitLine: {
                show: false
            },
            axisLabel: {
                show: true,
                textStyle: {
                    color: '#a4a7ab'
                }
            }
        },
        series: [
            {
                name: '出行人数（人）',
                type: 'bar',
                stack: '总量',
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: [9900, 12350, 42563, 52364, 63524, 78224, 89254],
                itemStyle: {
                    normal: {
                        color: "#ff7d0a"
                    }
                }
            }
        ]
    };
    myChart.setOption(option);
});