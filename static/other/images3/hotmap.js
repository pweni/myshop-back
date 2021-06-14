    var map = new BMap.Map("chart_map");          // 创建地图实例
 
    var point = new BMap.Point(87.617733,43.792818);
    map.centerAndZoom(point, 10);             // 初始化地图，设置中心点坐标和地图级别
	map.setCurrentCity("乌鲁木齐");		//设置当前显示城市
    map.enableScrollWheelZoom(); // 允许滚轮缩放
 
	
	
    var points =[
{"lng":"87.627733","lat":"43.792818","count":"52"},
{"lng":"87.637733","lat":"43.792818","count":"7"},
{"lng":"87.647733","lat":"43.792818","count":"6"},
{"lng":"87.657733","lat":"43.792818","count":"19"},
{"lng":"87.667733","lat":"43.792818","count":"2"},
{"lng":"87.677733","lat":"43.792818","count":"4"},
{"lng":"87.687733","lat":"43.792818","count":"1"},
{"lng":"87.917733","lat":"43.792818","count":"5"},
{"lng":"87.874159","lat":"43.892032","count":"8"},
{"lng":"87.771111","lat":"43.891111","count":"11"},
{"lng":"87.571200","lat":"43.891200","count":"11"},
{"lng":"87.572200","lat":"43.892300","count":"3"},
{"lng":"87.472500","lat":"43.892500","count":"5"},
{"lng":"87.374159","lat":"43.892032","count":"38"},
{"lng":"87.274159","lat":"43.892032","count":"7"},
{"lng":"87.174159","lat":"43.892032","count":"55"},
{"lng":"87.574159","lat":"43.892032","count":"28"},
{"lng":"87.648979","lat":"43.043749","count":"1"},
{"lng":"87.104776","lat":"43.124067","count":"12"},
{"lng":"87.778275","lat":"43.095941","count":"3"},
{"lng":"87.778275","lat":"43.095941","count":"22"},
{"lng":"87.578275","lat":"43.095941","count":"4"},
{"lng":"87.913152","lat":"43.000907","count":"5"},
{"lng":"87.831853","lat":"43.843377","count":"4"},
{"lng":"87.825641","lat":"43.072186","count":"16"},
{"lng":"87.931695","lat":"43.262638","count":"9"},
{"lng":"87.965077","lat":"43.919748","count":"6"},
{"lng":"87.830067","lat":"43.932444","count":"1"},
{"lng":"87.830067","lat":"43.932444","count":"7"},
{"lng":"87.550022","lat":"43.976316","count":"10"},
{"lng":"87.534346","lat":"43.166723","count":"6"},
{"lng":"87.928979","lat":"43.059528","count":"14"},
{"lng":"87.598287","lat":"43.777943","count":"6"},
{"lng":"87.567283","lat":"43.134905","count":"29"},
{"lng":"87.51997","lat":"43.280506","count":"6"},
{"lng":"87.943795","lat":"43.768474","count":"3"},
{"lng":"87.818245","lat":"43.183143","count":"107"},
{"lng":"87.662547","lat":"43.916163","count":"12"},
{"lng":"87.762547","lat":"43.916163","count":"17"},
{"lng":"87.309528","lat":"43.098043","count":"12"},
{"lng":"87.684941","lat":"43.066066","count":"10"},
{"lng":"87.665651","lat":"43.016851","count":"10"},
{"lng":"87.694527","lat":"43.889239","count":"4"},
{"lng":"87.616588","lat":"43.953233","count":"33"},
{"lng":"87.662802","lat":"43.082315","count":"5"},
{"lng":"87.821994","lat":"43.940167","count":"7"},
{"lng":"87.732801","lat":"43.010095","count":"1"},
{"lng":"87.665014","lat":"43.827956","count":"5"},
{"lng":"87.687001","lat":"43.926633","count":"4"},
{"lng":"87.0886604","lat":"43.823869","count":"17"},
{"lng":"87.714493","lat":"43.824384","count":"9"},
{"lng":"87.838951","lat":"43.714762","count":"8"},
{"lng":"87.768614","lat":"43.820543","count":"3"},
{"lng":"87.045903","lat":"43.001222","count":"10"},
{"lng":"87.814282","lat":"43.05379","count":"1"},
{"lng":"87.89458","lat":"43.128534","count":"2"},
{"lng":"87.778884","lat":"43.09376","count":"3"},
{"lng":"87.891728","lat":"43.996425","count":"9"},
{"lng":"87.899498","lat":"43.684382","count":"2"},
{"lng":"87.453397","lat":"43.942211","count":"13"},
{"lng":"87.537118","lat":"43.959195","count":"5"},
{"lng":"87.374189","lat":"43.92115","count":"21"},
{"lng":"87.443543","lat":"43.884432","count":"1"},
{"lng":"87.434839","lat":"43.885617","count":"23"},
{"lng":"87.468909","lat":"43.952258","count":"17"},
{"lng":"87.438104","lat":"43.944822","count":"27"},
{"lng":"87.647021","lat":"43.968271","count":"6"},
{"lng":"87.483172","lat":"43.862866","count":"3"},
{"lng":"87.589631","lat":"43.856694","count":"4"},
{"lng":"87.37435","lat":"43.930392","count":"1"},
{"lng":"87.444444","lat":"43.82315","count":"26"},
{"lng":"87.322755","lat":"43.82315","count":"6"},
{"lng":"87.376392","lat":"43.013433","count":"3"},
{"lng":"87.447681","lat":"43.062479","count":"6"},
{"lng":"87.447981","lat":"43.052479","count":"13"},
{"lng":"87.31517","lat":"43.117569","count":"5"}
 
 
];//这里面添加经纬度
 
 
    if(!isSupportCanvas()){
        alert('热力图目前只支持有canvas支持的浏览器,您所使用的浏览器不能使用热力图功能~')
    }
    //详细的参数,可以查看heatmap.js的文档 https://github.com/pa7/heatmap.js/blob/master/README.md
    //参数说明如下:
    /* visible 热力图是否显示,默认为true
     * opacity 热力的透明度,1-100
     * radius 势力图的每个点的半径大小
     * gradient  {JSON} 热力图的渐变区间 . gradient如下所示
     *  {
            .2:'rgb(0, 255, 255)',
            .5:'rgb(0, 110, 255)',
            .8:'rgb(100, 0, 255)'
        }
        其中 key 表示插值的位置, 0~1.
            value 为颜色值.
     */
    heatmapOverlay = new BMapLib.HeatmapOverlay({"radius":100,"visible":true});
    map.addOverlay(heatmapOverlay);
    heatmapOverlay.setDataSet({data:points,max:100});
	
    //closeHeatmap();
	
	
 
    //判断浏览区是否支持canvas
    function isSupportCanvas(){
        var elem = document.createElement('canvas');
        return !!(elem.getContext && elem.getContext('2d'));
    }
 
    function setGradient(){
        /*格式如下所示:
        {
            0:'rgb(102, 255, 0)',
            .5:'rgb(255, 170, 0)',
            1:'rgb(255, 0, 0)'
        }*/
        var gradient = {};
        var colors = document.querySelectorAll("input[type='color']");
        colors = [].slice.call(colors,0);
        colors.forEach(function(ele){
            gradient[ele.getAttribute("data-key")] = ele.value;
        });
        heatmapOverlay.setOptions({"gradient":gradient});
    }
 
    function openHeatmap(){
        heatmapOverlay.show();
    }
 
    function closeHeatmap(){
        heatmapOverlay.hide();
    }