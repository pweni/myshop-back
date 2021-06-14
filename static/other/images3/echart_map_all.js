$(function () {
    echart_1();
    echart_2();
    //chart2('');

    echart_3();
    echart_4();
    //echart_xj();
    //echart_map();
    //echart_gdMaps();

    //echart_1
    function echart_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_1'));

        var data = [
            { value: 335, name: '乌鲁木齐' },
            { value: 335, name: '喀什' },
            { value: 315, name: '昌吉' },
            { value: 200, name: '哈密' }
        ];

        option = {
            backgroundColor: 'transparent',
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            color: ['#0035f9', '#f36f8a', '#ffff43', '#25f3e6'],
            legend: { //图例组件，颜色和名字
                left: '65%',
                top: '95',
                orient: 'vertical',
                itemGap: 12, //图例每项之间的间隔
                itemWidth: 16,
                itemHeight: 12,

                icon: 'rect',
                data: ['乌鲁木齐', '喀什', '昌吉', '哈密'],
                textStyle: {
                    color: [],
                    fontStyle: 'normal',
                    fontFamily: '微软雅黑',
                    fontSize: 12,
                }
            },
            series: [{
                name: '类型',
                type: 'pie',
                clockwise: false, //饼图的扇区是否是顺时针排布
                minAngle: 20, //最小的扇区角度（0 ~ 360）
                center: ['35%', '50%'], //饼图的中心（圆心）坐标
                radius: [50, 80], //饼图的半径
                avoidLabelOverlap: true, ////是否启用防止标签重叠
                itemStyle: { //图形样式
                    normal: {
                        borderColor: '#1e2239',
                        borderWidth: 1.5,
                    },
                },

                label: { //标签的位置
                    normal: {
                        show: false,
                        position: 'inside', //标签的位置
                        formatter: "{d}%",
                        textStyle: {
                            color: '#fff',
                        }
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontWeight: 'bold'
                        }
                    }
                },
                data: data
            }, {
                name: '',
                type: 'pie',
                clockwise: false,
                silent: true,
                minAngle: 20, //最小的扇区角度（0 ~ 360）
                center: ['35%', '50%'], //饼图的中心（圆心）坐标
                radius: [0, 45], //饼图的半径
                itemStyle: { //图形样式
                    normal: {
                        borderColor: '#1e2239',
                        borderWidth: 1.5,
                        opacity: 0.21,
                    }
                },
                label: { //标签的位置
                    normal: {
                        show: false,
                    }
                },
                data: data
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    //echart_2
    function echart_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_2'));

        option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: { // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                }
            },

            legend: {
                // align: 'center',
                // left: '65%',
                top: '28',
                data: ['乌鲁木齐', '喀什', '昌吉', '哈密'],
                itemWidth: 16,
                itemHeight: 12,
                // borderRadius: 0, // 统一设置四个角的圆角大小
                icon: 'rect',
                textStyle: {
                    itemGap: 12, //图例每项之间的间隔
                    color: [],
                    fontStyle: 'normal',
                    fontFamily: '微软雅黑',
                    fontSize: 14,
                }
            },
            grid: {
                left: '5%',
                right: '5%',
                bottom: '5%',
                containLabel: true
            },

            xAxis: {
                axisLabel: { //调整x轴的lable
                    textStyle: {
                        color: '#fff',
                        fontSize: 13,
                    }
                },
                splitLine: {
                    show: false
                }
            },
            yAxis: {
                type: 'category',
                data: ['乌鲁木齐', '喀什', '昌吉', '哈密'],
                axisTick: { show: true },
                axisLabel: { //调整x轴的lable
                    textStyle: {
                        color: '#fff',
                        fontSize: 13,
                    }
                },
                splitLine: {
                    show: false
                }
            },
            series: [{
                name: '流出',
                type: 'bar',
                stack: '总量',
                color: '#0035f9',
                barWidth: 18,
                label: {
                    normal: {
                        show: false,
                        position: 'insideRight'
                    }
                },
                data: [4, 10, 8, 7]
            }, {
                name: '流入',
                type: 'bar',
                stack: '总量',
                color: '#f36f8a',
                barWidth: 20,
                label: {
                    normal: {
                        show: false,
                        position: 'insideRight'
                    }
                },
                data: [10, 4, 5, 6]
            }, {
                name: '人数',
                type: 'bar',
                stack: '总量',
                color: '#efe39b',
                barWidth: 20,
                label: {
                    normal: {
                        show: false,
                        position: 'insideRight'
                    }
                },
                data: [4, 10, 8, 7]
            }, {
                name: '其他',
                type: 'bar',
                stack: '总量',
                color: '#25f3e6',
                barWidth: 20,
                label: {
                    normal: {
                        show: false,
                        position: 'insideRight'
                    }
                },
                data: [4, 10, 8, 7]
            }

            ]

        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    // echart_map
    function echart_map() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_map'));

        var name_title = "投票统计"
        var subname = ''
        var nameColor = " rgb(55, 75, 113)"
        var name_fontFamily = '楷体'
        var name_fontSize = 52
        var mapName = 'china'
        var data = []
        var geoCoordMap = {};
        var toolTipData = [];

        /*获取地图数据*/
        myChart.showLoading();
        var mapFeatures = echarts.getMap(mapName).geoJson.features;
        myChart.hideLoading();
        mapFeatures.forEach(function (v) {
            // 地区名称
            var name = v.properties.name;
            // 地区经纬度
            geoCoordMap[name] = v.properties.cp;
            data.push({
                name: name,
                value: Math.round(Math.random() * 100 + 10)
            })
            toolTipData.push({
                name: name,
                value: [{
                    name: "客运车",
                    value: Math.round(Math.random() * 100 + 10)
                },
                {
                    name: "危险品运输车",
                    value: Math.round(Math.random() * 100 + 10)
                },
                {
                    name: "网约车",
                    value: Math.round(Math.random() * 100 + 10)
                },
                {
                    name: "学生班车",
                    value: Math.round(Math.random() * 100 + 10)
                }
                ]
            })
        });

        var max = 480,
            min = 9; // todo
        var maxSize4Pin = 100,
            minSize4Pin = 20;

        var convertData = function (data) {
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var geoCoord = geoCoordMap[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name,
                        value: geoCoord.concat(data[i].value),
                    });
                }
            }
            return res;
        };
        option = {
            title: {
                show: false,
                text: name_title,
                subtext: subname,
                x: 'center',
                textStyle: {
                    color: nameColor,
                    fontFamily: name_fontFamily,
                    fontSize: name_fontSize
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: function (params) {
                    if (typeof (params.value)[2] == "undefined") {
                        var toolTiphtml = ''
                        for (var i = 0; i < toolTipData.length; i++) {
                            if (params.name == toolTipData[i].name) {
                                toolTiphtml += toolTipData[i].name + ':<br>'
                                for (var j = 0; j < toolTipData[i].value.length; j++) {
                                    toolTiphtml += toolTipData[i].value[j].name + ':' + toolTipData[i].value[j].value + "<br>"
                                }
                            }
                        }
                        return toolTiphtml;
                    } else {
                        var toolTiphtml = ''
                        for (var i = 0; i < toolTipData.length; i++) {
                            if (params.name == toolTipData[i].name) {
                                toolTiphtml += toolTipData[i].name + ':<br>'
                                for (var j = 0; j < toolTipData[i].value.length; j++) {
                                    toolTiphtml += toolTipData[i].value[j].name + ':' + toolTipData[i].value[j].value + "<br>"
                                }
                            }
                        }
                        return toolTiphtml;
                    }
                }
            },
            legend: {
                orient: 'vertical',
                y: 'bottom',
                x: 'right',
                data: ['credit_pm2.5'],
                textStyle: {
                    color: '#fff'
                }
            },
            visualMap: {
                show: false,
                min: 0,
                max: 500,
                left: 'left',
                top: 'bottom',
                text: ['高', '低'], // 文本，默认为数值文本
                calculable: true,
                seriesIndex: [1],
                inRange: {
                    // color: ['#3B5077', '#031525'] // 蓝黑
                    // color: ['#ffc0cb', '#800080'] // 红紫
                    // color: ['#3C3B3F', '#605C3C'] // 黑绿
                    color: ['#0f0c29', '#302b63', '#24243e'] // 黑紫黑
                    // color: ['#23074d', '#cc5333'] // 紫红
                    // color: ['#00467F', '#A5CC82'] // 蓝绿
                    // color: ['#1488CC', '#2B32B2'] // 浅蓝
                    // color: ['#00467F', '#A5CC82'] // 蓝绿
                    // color: ['#00467F', '#A5CC82'] // 蓝绿
                    // color: ['#00467F', '#A5CC82'] // 蓝绿
                    // color: ['#00467F', '#A5CC82'] // 蓝绿

                }
            },
            /*工具按钮组*/
            toolbox: {
                show: false,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                    dataView: {
                        readOnly: false
                    },
                    restore: {},
                    saveAsImage: {}
                }
            },
            geo: {
                show: true,
                map: mapName,
                label: {
                    normal: {
                        show: false
                    },
                    emphasis: {
                        show: false,
                    }
                },
                roam: true,
                itemStyle: {
                    normal: {
                        areaColor: '#031525',
                        borderColor: '#3B5077',
                    },
                    emphasis: {
                        areaColor: '#2B91B7',
                    }
                }
            },
            series: [{
                name: '散点',
                type: 'scatter',
                coordinateSystem: 'geo',
                data: convertData(data),
                symbolSize: function (val) {
                    return val[2] / 10;
                },
                label: {
                    normal: {
                        formatter: '{b}',
                        position: 'right',
                        show: true
                    },
                    emphasis: {
                        show: true
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#05C3F9'
                    }
                }
            },
            {
                type: 'map',
                map: mapName,
                geoIndex: 0,
                aspectScale: 0.75, //长宽比
                showLegendSymbol: false, // 存在legend时显示
                label: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        show: false,
                        textStyle: {
                            color: '#fff'
                        }
                    }
                },
                roam: true,
                itemStyle: {
                    normal: {
                        areaColor: '#031525',
                        borderColor: '#0227ad',
                    },
                    emphasis: {
                        areaColor: '#2B91B7'
                    }
                },
                animation: false,
                data: data
            },
            {
                name: '点',
                type: 'scatter',
                coordinateSystem: 'geo',
                symbol: 'pin', //气泡
                symbolSize: function (val) {
                    var a = (maxSize4Pin - minSize4Pin) / (max - min);
                    var b = minSize4Pin - a * min;
                    b = maxSize4Pin - a * max;
                    return a * val[2] + b;
                },
                label: {
                    //气泡上的文字
                    normal: {
                        show: false,
                        textStyle: {
                            color: '#fff',
                            fontSize: 9,
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#F62157', //标志颜色
                    }
                },
                zlevel: 6,
                data: convertData(data),
            },
            {
                name: 'Top 5',
                type: 'effectScatter',
                coordinateSystem: 'geo',
                data: convertData(data.sort(function (a, b) {
                    return b.value - a.value;
                }).slice(0, 5)),
                symbolSize: function (val) {
                    return val[2] / 10;
                },
                showEffectOn: 'render',
                rippleEffect: {
                    brushType: 'stroke'
                },
                hoverAnimation: true,
                label: {
                    normal: {
                        formatter: '{b}',
                        position: 'right',
                        show: true
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#05C3F9',
                        shadowBlur: 10,
                        shadowColor: '#05C3F9'
                    }
                },
                zlevel: 1
            },

            ]
        };
        myChart.setOption(option);

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });

    }

    //echart_3
    function echart_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_3'));
        var xAxisData = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'];
        var legendData = ['', '', ''];
        var title = "";
        var serieData = [];
        var metaDate = [
            [120, 140, 100, 120, 300, 230, 130, 170, 140, 120, 300, 230, 120, 140, 100, 120, 300, 230, 130, 170, 140, 120, 300, 230]

        ]
        for (var v = 0; v < legendData.length; v++) {
            var serie = {
                name: legendData[v],
                type: 'line',
                symbol: "circle",
                symbolSize: 10,
                data: metaDate[v]
            };
            serieData.push(serie)
        }
        var colors = ["#ffff43"];
        var option = {
            backgroundColor: 'transparent',
            title: { text: title, textAlign: 'left', textStyle: { color: "#fff", fontSize: "16", fontWeight: "normal" } },

            color: colors,
            grid: { left: '4%', top: "30%", bottom: "5%", right: "4%", containLabel: true },
            tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
            xAxis: [
                {
                    type: 'category',
                    axisLine: { show: true, lineStyle: { color: '#2c3459' } },
                    axisLabel: { interval: 0, textStyle: { color: '#fff', fontSize: 12 } },
                    axisTick: { show: false },
                    data: xAxisData,
                },
            ],
            yAxis: [
                {
                    axisTick: { show: false },
                    splitLine: { show: false },
                    axisLabel: { textStyle: { color: '#fff', fontSize: 12 } },
                    axisLine: { show: true, lineStyle: { color: '#2c3459' } },
                },
            ],
            series: serieData
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echart_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_4'));

        /*中间显示的数据*/
        /*中间显示的数据*/
        var myData = ['流入', '流出', '全部', '其他']
        var databeast = {
            1: [38, 25, 26, 32]
        }
        var databeauty = {
            1: [11, 38, 23, 30]
        }
        var timeLineData = [1]

        var option = {
            baseOption: {
                backgroundColor: 'transparent',
                timeline: {
                    show: false,
                    top: 0,
                    data: []
                },
                legend: {
                    show: true,
                    // align: 'center',
                    left: '30%',
                    top: 30,
                    // data: ['行驶', '停车'],
                    // itemWidth:16,
                    // itemHeight:12,
                    // // borderRadius: 0, // 统一设置四个角的圆角大小
                    icon: 'rect',
                    textStyle: {
                        itemGap: 12, //图例每项之间的间隔
                        color: [],
                        fontStyle: 'normal',
                        fontFamily: '微软雅黑',
                        fontSize: 14,
                    }
                },
                tooltip: {
                    show: true,
                    trigger: 'axis',
                    formatter: '{b}<br/>{a}: {c}',
                    axisPointer: {
                        type: 'shadow'
                    }
                },

                grid: [{
                    show: false,
                    left: '8%',
                    top: 60,
                    bottom: 0,
                    containLabel: true,
                    width: '30%'
                }, {
                    show: false,
                    left: '57%',
                    top: 60,
                    bottom: 0,
                    width: '0%'
                }, {
                    show: false,
                    right: '8%',
                    top: 60,
                    bottom: 0,
                    containLabel: true,
                    width: '30%'
                }],

                xAxis: [{
                    type: 'value',
                    inverse: true,
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    position: 'top',
                    axisLabel: {
                        show: false
                    },
                    splitLine: {
                        show: false
                    }
                }, {
                    gridIndex: 1,
                    show: false
                }, {
                    gridIndex: 2,
                    nameTextStyle: {
                        color: '#50afff',
                        fontSize: 14
                    },
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    position: 'top',
                    axisLabel: {
                        show: false
                    },
                    splitLine: {
                        show: false
                    }
                }],
                yAxis: [{
                    type: 'category',
                    inverse: true,
                    position: 'right',
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        show: false
                    },
                    data: myData
                }, {
                    gridIndex: 1,
                    type: 'category',
                    inverse: true,
                    position: 'left',
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        show: true,
                        textStyle: {
                            color: '#fff',
                            fontSize: 14
                        }

                    },
                    data: myData.map(function (value) {
                        return {
                            value: value,
                            textStyle: {
                                align: 'center'
                            }
                        }
                    })
                }, {
                    gridIndex: 2,
                    type: 'category',
                    inverse: true,
                    position: 'left',
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        show: false

                    },
                    data: myData
                }],
                series: [

                ]

            },
            options: []
        }

        option.baseOption.timeline.data.push(timeLineData[0])
        option.options.push({
            tooltip: {
                trigger: 'axis',
                formatter: '{b}<br/>{c} {a}'
            },
            series: [{
                name: '昨天',
                type: 'bar',
                barWidth: 17,
                label: {
                    normal: {
                        show: true,
                        position: 'left',
                        offset: [0, 0],
                        textStyle: {
                            color: '#fff',
                            fontSize: 14
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#0035f9',
                        // barBorderRadius: 50
                    }
                },

                data: databeast[timeLineData[0]]
            }, {
                name: '今天',
                type: 'bar',
                barWidth: 18,
                xAxisIndex: 2,
                yAxisIndex: 2,
                label: {
                    normal: {
                        show: true,
                        position: 'right',
                        offset: [0, 0],
                        textStyle: {
                            color: '#fff',
                            fontSize: 14
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#25f3e6',
                        // barBorderRadius: 50
                    }
                },
                data: databeauty[timeLineData[0]]
            }]
        })

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });

    }

    function chart2(chartType) {
        var data = [{
            name: '乌鲁木齐市',
            value: 100
        }, {
            name: '克拉玛依市',
            value: 96
        }, {
            name: '吐鲁番市',
            value: 98
        }, {
            name: '哈密市',
            value: 80
        }, {
            name: '昌吉回族自治州',
            value: 88
        }, {
            name: '博尔塔拉蒙古自治州',
            value: 79
        }, {
            name: '巴音郭楞蒙古自治州',
            value: 77,
        }, {
            name: '阿克苏地区',
            value: 33
        }, {
            name: '克孜勒苏柯尔克孜自治州',
            value: 69,
        }, {
            name: '喀什地区',
            value: 66
        }, {
            name: '和田地区',
            value: 22
        }, {
            name: '伊犁哈萨克自治州',
            value: 51
        }, {
            name: '塔城地区',
            value: 44
        }, {
            name: '阿勒泰地区',
            value: 9
        }, {
            name: '石河子市',
            value: 44
        }, {
            name: '阿拉尔市',
            value: 9
        }, {
            name: '阿勒泰地区',
            value: 9
        }, {
            name: '石河子市',
            value: 44
        }, {
            name: '阿拉尔市',
            value: 9
        }, {
            name: '阿勒泰地区',
            value: 9
        }, {
            name: '石河子市',
            value: 44
        }, {
            name: '阿拉尔市',
            value: 9
        }, {
            name: '图木舒克市',
            value: 9
        }, {
            name: '五家渠市',
            value: 44
        }, {
            name: '北屯市',
            value: 9
        }]

        var myChart = echarts.init(document.getElementById('gdMap'));
        var myCharts = echarts.init(document.getElementById('gdMaps'));
        window.addEventListener('resize', function () {
            myChart.resize();
            myCharts.resize();
        });
        var yMax = 0;
        for (var j = 0; j < data.length; j++) {
            if (yMax < data[j].value) {
                yMax = data[j].value;
            }
        }
        myChart.hideLoading();
        myCharts.hideLoading();
        var option = {
            animation: true,
            tooltip: {
                show: true
            },
            visualMap: {
                min: 0,
                max: 100,
                text: ['高', '低'],
                //orient: 'horizontal',
                //itemWidth: 15,
                //itemHeight: 200,
                //right: 0,
                //bottom: 30,
                inRange: {
                    color: ['yellow', 'lightskyblue', 'orangered']
                }
                //textStyle: {
                //    color: 'white'
                //}
            },
            series: [
                {
                    name: '数据名称',
                    type: 'map',
                    mapType: 'xinjiang',
                    selectedMode: 'multiple',
                    roam: true,
                    tooltip: {
                        trigger: 'item',
                        formatter: '{b}<br/>{c} (件)'
                    },
                    itemStyle: {
                        normal: {
                            borderColor: '#389BB7',
                            areaColor: '#fff',
                        },
                        emphasis: {
                            areaColor: '#389BB7',
                            borderWidth: 0
                        }
                    },
                    animation: false,
                    data: data,
                }
            ]
        };

        alert(option)

        myChart.setOption(option);
        myCharts.setOption(option);
    }

    //新疆地图
    function echart_xj() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_xj'));
        function showProvince() {
            myChart.setOption(option = {
                // backgroundColor: '#ffffff',
                visualMap: {
                    show: false,
                    min: 0,
                    max: 100,
                    left: 'left',
                    top: 'bottom',
                    text: ['高', '低'], // 文本，默认为数值文本
                    calculable: true,
                    inRange: {
                        color: ['yellow', 'lightskyblue', 'orangered']
                    }
                },
                series: [{
                    type: 'map',
                    mapType: '新疆',
                    roam: true,
                    label: {
                        normal: {
                            show: true
                        },
                        emphasis: {
                            textStyle: {
                                color: '#fff'
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            borderColor: '#389BB7',
                            areaColor: '#fff',
                        },
                        emphasis: {
                            areaColor: '#389BB7',
                            borderWidth: 0
                        }
                    },
                    animation: false,
                    data: [{
                        name: '乌鲁木齐市',
                        value: 100
                    }, {
                        name: '克拉玛依市',
                        value: 96
                    }, {
                        name: '吐鲁番市',
                        value: 98
                    }, {
                        name: '哈密市',
                        value: 80
                    }, {
                        name: '昌吉回族自治州',
                        value: 88
                    }, {
                        name: '博尔塔拉蒙古自治州',
                        value: 79
                    }, {
                        name: '巴音郭楞蒙古自治州',
                        value: 77,
                    }, {
                        name: '阿克苏地区',
                        value: 33
                    }, {
                        name: '克孜勒苏柯尔克孜自治州',
                        value: 69,
                    }, {
                        name: '喀什地区',
                        value: 66
                    }, {
                        name: '和田地区',
                        value: 22
                    }, {
                        name: '伊犁哈萨克自治州',
                        value: 51
                    }, {
                        name: '塔城地区',
                        value: 44
                    }, {
                        name: '阿勒泰地区',
                        value: 9
                    }, {
                        name: '石河子市',
                        value: 44
                    }, {
                        name: '阿拉尔市',
                        value: 9
                    }, {
                        name: '阿勒泰地区',
                        value: 9
                    }, {
                        name: '石河子市',
                        value: 44
                    }, {
                        name: '阿拉尔市',
                        value: 9
                    }, {
                        name: '阿勒泰地区',
                        value: 9
                    }, {
                        name: '石河子市',
                        value: 44
                    }, {
                        name: '阿拉尔市',
                        value: 9
                    }, {
                        name: '图木舒克市',
                        value: 9
                    }, {
                        name: '五家渠市',
                        value: 44
                    }, {
                        name: '北屯市',
                        value: 9
                    }]
                }]
            });
        }

        var currentIdx = 0;
        showProvince();
        // 使用刚指定的配置项和数据显示图表。
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    //gdMaps 新疆地图
    function echart_gdMaps() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('gdMap'));
        var myCharts = echarts.init(document.getElementById('gdMaps'));

        var option = {
            // backgroundColor: '#ffffff',
            visualMap: {
                show: false,
                min: 0,
                max: 100,
                left: 'left',
                top: 'bottom',
                text: ['高', '低'], // 文本，默认为数值文本
                calculable: true,
                inRange: {
                    color: ['yellow', 'lightskyblue', 'orangered']
                }
            },
            series: [{
                type: 'map',
                mapType: 'xinjiang',
                roam: true,
                label: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        textStyle: {
                            color: '#fff'
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        borderColor: '#389BB7',
                        areaColor: '#fff',
                    },
                    emphasis: {
                        areaColor: '#389BB7',
                        borderWidth: 0
                    }
                },
                animation: false,
                data: [{
                    name: '乌鲁木齐市',
                    value: 100
                }, {
                    name: '克拉玛依市',
                    value: 96
                }, {
                    name: '吐鲁番市',
                    value: 98
                }, {
                    name: '哈密市',
                    value: 80
                }, {
                    name: '昌吉回族自治州',
                    value: 88
                }, {
                    name: '博尔塔拉蒙古自治州',
                    value: 79
                }, {
                    name: '巴音郭楞蒙古自治州',
                    value: 77,
                }, {
                    name: '阿克苏地区',
                    value: 33
                }, {
                    name: '克孜勒苏柯尔克孜自治州',
                    value: 69,
                }, {
                    name: '喀什地区',
                    value: 66
                }, {
                    name: '和田地区',
                    value: 22
                }, {
                    name: '伊犁哈萨克自治州',
                    value: 51
                }, {
                    name: '塔城地区',
                    value: 44
                }, {
                    name: '阿勒泰地区',
                    value: 9
                }, {
                    name: '石河子市',
                    value: 44
                }, {
                    name: '阿拉尔市',
                    value: 9
                }, {
                    name: '阿勒泰地区',
                    value: 9
                }, {
                    name: '石河子市',
                    value: 44
                }, {
                    name: '阿拉尔市',
                    value: 9
                }, {
                    name: '阿勒泰地区',
                    value: 9
                }, {
                    name: '石河子市',
                    value: 44
                }, {
                    name: '阿拉尔市',
                    value: 9
                }, {
                    name: '图木舒克市',
                    value: 9
                }, {
                    name: '五家渠市',
                    value: 44
                }, {
                    name: '北屯市',
                    value: 9
                }]
            }]
        };

        var currentIdx = 0;
        myChart.setOption(option);
        myCharts.setOption(option);
        // 使用刚指定的配置项和数据显示图表。
        window.addEventListener("resize", function () {
            myChart.resize();
            myCharts.resize();
        });
    }

    //页面地图数据
    var geoCoordMap = {
        '海门': [121.15, 31.89],
        '鄂尔多斯': [109.781327, 39.608266],
        '招远': [120.38, 37.35],
        '舟山': [122.207216, 29.985295],
        '齐齐哈尔': [123.97, 47.33],
        '盐城': [120.13, 33.38],
        '赤峰': [118.87, 42.28],
        '青岛': [120.33, 36.07],
        '乳山': [121.52, 36.89],
        '金昌': [102.188043, 38.520089],
        '泉州': [118.58, 24.93],
        '莱西': [120.53, 36.86],
        '日照': [119.46, 35.42],
        '胶南': [119.97, 35.88],
        '南通': [121.05, 32.08],
        '拉萨': [91.11, 29.97],
        '云浮': [112.02, 22.93],
        '梅州': [116.1, 24.55],
        '文登': [122.05, 37.2],
        '上海': [121.48, 31.22],
        '攀枝花': [101.718637, 26.582347],
        '威海': [122.1, 37.5],
        '承德': [117.93, 40.97],
        '厦门': [118.1, 24.46],
        '汕尾': [115.375279, 22.786211],
        '潮州': [116.63, 23.68],
        '丹东': [124.37, 40.13],
        '太仓': [121.1, 31.45],
        '曲靖': [103.79, 25.51],
        '烟台': [121.39, 37.52],
        '福州': [119.3, 26.08],
        '瓦房店': [121.979603, 39.627114],
        '即墨': [120.45, 36.38],
        '抚顺': [123.97, 41.97],
        '玉溪': [102.52, 24.35],
        '张家口': [114.87, 40.82],
        '阳泉': [113.57, 37.85],
        '莱州': [119.942327, 37.177017],
        '湖州': [120.1, 30.86],
        '汕头': [116.69, 23.39],
        '昆山': [120.95, 31.39],
        '宁波': [121.56, 29.86],
        '湛江': [110.359377, 21.270708],
        '揭阳': [116.35, 23.55],
        '荣成': [122.41, 37.16],
        '连云港': [119.16, 34.59],
        '葫芦岛': [120.836932, 40.711052],
        '常熟': [120.74, 31.64],
        '东莞': [113.75, 23.04],
        '河源': [114.68, 23.73],
        '淮安': [119.15, 33.5],
        '泰州': [119.9, 32.49],
        '南宁': [108.33, 22.84],
        '营口': [122.18, 40.65],
        '惠州': [114.4, 23.09],
        '江阴': [120.26, 31.91],
        '蓬莱': [120.75, 37.8],
        '韶关': [113.62, 24.84],
        '嘉峪关': [98.289152, 39.77313],
        '广州': [113.23, 23.16],
        '延安': [109.47, 36.6],
        '太原': [112.53, 37.87],
        '清远': [113.01, 23.7],
        '中山': [113.38, 22.52],
        '昆明': [102.73, 25.04],
        '寿光': [118.73, 36.86],
        '盘锦': [122.070714, 41.119997],
        '长治': [113.08, 36.18],
        '深圳': [114.07, 22.62],
        '珠海': [113.52, 22.3],
        '宿迁': [118.3, 33.96],
        '咸阳': [108.72, 34.36],
        '铜川': [109.11, 35.09],
        '平度': [119.97, 36.77],
        '佛山': [113.11, 23.05],
        '海口': [110.35, 20.02],
        '江门': [113.06, 22.61],
        '章丘': [117.53, 36.72],
        '肇庆': [112.44, 23.05],
        '大连': [121.62, 38.92],
        '临汾': [111.5, 36.08],
        '吴江': [120.63, 31.16],
        '石嘴山': [106.39, 39.04],
        '沈阳': [123.38, 41.8],
        '苏州': [120.62, 31.32],
        '茂名': [110.88, 21.68],
        '嘉兴': [120.76, 30.77],
        '长春': [125.35, 43.88],
        '胶州': [120.03336, 36.264622],
        '银川': [106.27, 38.47],
        '张家港': [120.555821, 31.875428],
        '三门峡': [111.19, 34.76],
        '锦州': [121.15, 41.13],
        '南昌': [115.89, 28.68],
        '柳州': [109.4, 24.33],
        '三亚': [109.511909, 18.252847],
        '自贡': [104.778442, 29.33903],
        '吉林': [126.57, 43.87],
        '阳江': [111.95, 21.85],
        '泸州': [105.39, 28.91],
        '西宁': [101.74, 36.56],
        '宜宾': [104.56, 29.77],
        '呼和浩特': [111.65, 40.82],
        '成都': [104.06, 30.67],
        '大同': [113.3, 40.12],
        '镇江': [119.44, 32.2],
        '桂林': [110.28, 25.29],
        '张家界': [110.479191, 29.117096],
        '宜兴': [119.82, 31.36],
        '北海': [109.12, 21.49],
        '西安': [108.95, 34.27],
        '金坛': [119.56, 31.74],
        '东营': [118.49, 37.46],
        '牡丹江': [129.58, 44.6],
        '遵义': [106.9, 27.7],
        '绍兴': [120.58, 30.01],
        '扬州': [119.42, 32.39],
        '常州': [119.95, 31.79],
        '潍坊': [119.1, 36.62],
        '重庆': [106.54, 29.59],
        '台州': [121.420757, 28.656386],
        '南京': [118.78, 32.04],
        '滨州': [118.03, 37.36],
        '贵阳': [106.71, 26.57],
        '无锡': [120.29, 31.59],
        '本溪': [123.73, 41.3],
        '克拉玛依': [84.77, 45.59],
        '渭南': [109.5, 34.52],
        '马鞍山': [118.48, 31.56],
        '宝鸡': [107.15, 34.38],
        '焦作': [113.21, 35.24],
        '句容': [119.16, 31.95],
        '北京': [116.46, 39.92],
        '徐州': [117.2, 34.26],
        '衡水': [115.72, 37.72],
        '包头': [110, 40.58],
        '绵阳': [104.73, 31.48],
        '乌鲁木齐': [87.68, 43.77],
        '枣庄': [117.57, 34.86],
        '杭州': [120.19, 30.26],
        '淄博': [118.05, 36.78],
        '鞍山': [122.85, 41.12],
        '溧阳': [119.48, 31.43],
        '库尔勒': [86.06, 41.68],
        '安阳': [114.35, 36.1],
        '开封': [114.35, 34.79],
        '济南': [117, 36.65],
        '德阳': [104.37, 31.13],
        '温州': [120.65, 28.01],
        '九江': [115.97, 29.71],
        '邯郸': [114.47, 36.6],
        '临安': [119.72, 30.23],
        '兰州': [103.73, 36.03],
        '沧州': [116.83, 38.33],
        '临沂': [118.35, 35.05],
        '南充': [106.110698, 30.837793],
        '天津': [117.2, 39.13],
        '富阳': [119.95, 30.07],
        '泰安': [117.13, 36.18],
        '诸暨': [120.23, 29.71],
        '郑州': [113.65, 34.76],
        '哈尔滨': [126.63, 45.75],
        '聊城': [115.97, 36.45],
        '芜湖': [118.38, 31.33],
        '唐山': [118.02, 39.63],
        '平顶山': [113.29, 33.75],
        '邢台': [114.48, 37.05],
        '德州': [116.29, 37.45],
        '济宁': [116.59, 35.38],
        '荆州': [112.239741, 30.335165],
        '宜昌': [111.3, 30.7],
        '义乌': [120.06, 29.32],
        '丽水': [119.92, 28.45],
        '洛阳': [112.44, 34.7],
        '秦皇岛': [119.57, 39.95],
        '株洲': [113.16, 27.83],
        '石家庄': [114.48, 38.03],
        '莱芜': [117.67, 36.19],
        '常德': [111.69, 29.05],
        '保定': [115.48, 38.85],
        '湘潭': [112.91, 27.87],
        '金华': [119.64, 29.12],
        '岳阳': [113.09, 29.37],
        '长沙': [113, 28.21],
        '衢州': [118.88, 28.97],
        '廊坊': [116.7, 39.53],
        '菏泽': [115.480656, 35.23375],
        '合肥': [117.27, 31.86],
        '武汉': [114.31, 30.52],
        '大庆': [125.03, 46.58],
        '安徽省': [117.17, 31.52],
        '北京市': [116.24, 39.55],
        '重庆市': [106.54, 29.59],
        '福建省': [119.18, 26.05],
        '甘肃省': [103.51, 36.04],
        '广东省': [113.14, 23.08],
        '广西壮族自治区': [108.19, 22.48],
        '贵州省': [106.42, 26.35],
        '海南省': [110.20, 20.02],
        '河北省': [114.30, 38.02],
        '河南省': [113.40, 34.46],
        '黑龙江省': [128.36, 45.44],
        '湖北省': [112.27, 30.15],
        '湖南省': [112.59, 28.12],
        '吉林省': [125.19, 43.54],
        '江苏省': [118.46, 32.03],
        '江西省': [115.55, 28.40],
        '辽宁省': [123.25, 41.48],
        '内蒙古': [108.41, 40.48],
        '内蒙古自治区': [108.41, 40.48],
        '宁夏回族自治区': [106.16, 38.27],
        '青海省': [101.48, 36.38],
        '山东省': [118.00, 36.40],
        '山西省': [112.33, 37.54],
        '陕西省': [108.57, 34.17],
        '上海市': [121.29, 31.14],
        '海南': [108.77, 19.10],
        '四川省': [104.04, 30.40],
        '天津市': [117.12, 39.02],
        '西藏自治区': [91.08, 29.39],
        '新疆维吾尔自治区': [87.36, 43.45],
        '云南省': [102.42, 25.04],
        '浙江省': [120.10, 30.16],
        '澳门特别行政区': [115.07, 21.33],
        '台湾省': [121.21, 23.53],
        '香港特别行政区': [114.1, 22.2]
    };
    //chart4Data模拟数据
    var chart4Data = [{
        'name': "天津",
        'value': 178546
    }, {
        'name': "湖南省",
        'value': 125687
    }, {
        'name': "福建省",
        'value': 78452
    }, {
        'name': "北京市",
        'value': 57841
    }, {
        'name': "江苏省",
        'value': 45879
    }, {
        'name': "海南",
        'value': 28584
    }, {
        'name': "四川省",
        'value': 14852
    }, {
        'name': "浙江省",
        'value': 12589
    }, {
        'name': "重庆市",
        'value': 5261
    }, {
        'name': "香港特别行政区",
        'value': 2563
    }, {
        'name': "内蒙古",
        'value': 856
    }]
    chart4(chart4Data, 1, '');

    function chart4(data, type, chartType) {
        var str = '<li><span></span><p>城市</p><p>派件</p></li>';
        for (var i = 0; i < 10; i++) {
            str += '<li><span>' + (i + 1) + '</span><p>' + data[i].name + '</p><p>' + data[i].value + '</p></li>';
        }

        var s_data = [];
        var myChart = echarts.init(document.getElementById('chart4'));
        //var myCharts = echarts.init(document.getElementById('chart4s'));
        window.addEventListener('resize', function () {
            myChart.resize();
            //myCharts.resize();
        });


        function formtGCData(geoData, data, srcNam, dest) {
            var tGeoDt = [];
            if (dest) {
                for (var i = 0, len = data.length; i < len; i++) {
                    if (srcNam != data[i].name) {
                        tGeoDt.push({
                            coords: [geoData[srcNam], geoData[data[i].name]],
                        });
                    }
                }
            } else {
                for (var i = 0, len = data.length; i < len; i++) {
                    if (srcNam != data[i].name) {
                        tGeoDt.push({
                            coords: [geoData[data[i].name], geoData[srcNam]],
                        });
                    }
                }
            }
            return tGeoDt;
        }

        function formtVData(geoData, data, srcNam) {
            var tGeoDt = [];
            for (var i = 0, len = data.length; i < len; i++) {
                var tNam = data[i].name
                if (srcNam != tNam) {
                    tGeoDt.push({
                        name: tNam,
                        symbolSize: 2,
                        itemStyle: {
                            normal: {
                                color: '#ffeb40',
                            }
                        },
                        value: geoData[tNam]
                    });
                }

            }
            tGeoDt.push({
                name: srcNam,
                value: geoData[srcNam],
                symbolSize: 5,
                itemStyle: {
                    normal: {
                        color: '#2ef358',
                    }
                }

            });
            return tGeoDt;
        }

        var planePath = 'pin';
        if (type == 2) {
            s_data.push({
                type: 'lines',
                zlevel: 2,
                mapType: 'china',
                symbol: 'none',
                effect: {
                    show: true,
                    period: 1.5,
                    trailLength: 0.1,
                    //                color: '#ffeb40',
                    color: '#2ef358',
                    symbol: planePath,
                    symbolSize: 6,
                    trailLength: 0.5

                },
                lineStyle: {
                    normal: {
                        color: '#2ef358',
                        width: 1,
                        opacity: 0.4,
                        curveness: 0.2
                    }
                },
                data: formtGCData(geoCoordMap, data, '新疆维吾尔自治区', true)
            })

        } else if (type == 1) {
            s_data.push({
                type: 'lines',
                zlevel: 2,
                effect: {
                    show: true,
                    period: 1.5,
                    trailLength: 0.1,
                    //                color: '#2ef358',
                    color: '#ffeb40',
                    symbol: planePath,
                    symbolSize: 6,
                    trailLength: 0.5
                },
                lineStyle: {
                    normal: {
                        color: '#ffeb40',
                        width: 1,
                        opacity: 0.4,
                        curveness: 0.2
                    }
                },
                data: formtGCData(geoCoordMap, data, '新疆维吾尔自治区', false)
            }, {

                type: 'effectScatter',
                coordinateSystem: 'geo',
                zlevel: 2,
                rippleEffect: {
                    period: 4,
                    scale: 2.5,
                    brushType: 'stroke'
                },
                symbol: 'none',
                symbolSize: 4,
                itemStyle: {
                    normal: {
                        color: '#fff'
                    }
                },

                data: formtVData(geoCoordMap, data, '新疆维吾尔自治区')
            })
        }

        var option = {
            tooltip: {
                trigger: 'item',
            },
            geo: {
                map: 'china',
                label: {
                    show: true,
                    position: 'insideLeft',
                    color: 'white',
                    fontSize: '10',
                    emphasis: {
                        show: true
                    }
                },
                roam: true,
                silent: true,
                itemStyle: {
                    normal: {
                        areaColor: 'transparent',
                        borderColor: '#0e94eb',
                        shadowBlur: 10,
                        shadowColor: '#0e94ea'
                    }
                },
                left: 10,
                right: 10
            },
            series: s_data
        };
        if (chartType === '') {
            $('.ranking-box').html(str);
            myChart.setOption(option);
            //myCharts.setOption(option);
        } else if (chartType === 0) {
            $('.center-bottom .ranking-box').html(str);
            myChart.setOption(option);
        } else if (chartType === 1) {
            $('.pop-data .ranking-box').html(str);
            //myCharts.setOption(option);
        }
    }

})
