from django.shortcuts import render,HttpResponse
from .models import NBAData
from django.views import generic # 通用模块


def homepage(request):
    sql = "select * from dbo.index_nbadata"
    datas = NBAData.objects.raw(sql)
    win_list = []
    ballgame_list = []
    transport_list = []
    winrate_list = []
    for x in list(datas):
        win_list.append(x.win)
        ballgame_list.append(x.ballgame.encode('utf-8').decode('utf-8'))
        transport_list.append(x.transport)
        winrate_list.append(float(x.winrate.replace('%', '')))

    # map(lambda x:x.win,list(datas))
    ballgame_str = '_'.join(ballgame_list)
    NBAdata = {"win": win_list, "ballgame": ballgame_str, "transport": transport_list, "winrate": winrate_list, }
    return render(request, 'Homepage.html', locals())



# Create your views here.
def index(request):
    if request.method == "GET":
        sql = "select * from dbo.index_nbadata order by(winrate) desc;"
        datas = NBAData.objects.raw(sql)
        win_list = []
        ballgame_list = []
        transport_list = []
        winrate_list = []
        for x in list(datas):
            win_list.append(x.win)
            ballgame_list.append(x.ballgame.encode('utf-8').decode('utf-8')+' / '+x.area)
            transport_list.append(x.transport)
            winrate_list.append(float(x.winrate.replace('%','')))

        ballgame_str = '_'.join(ballgame_list)
        NBAdata = {
            "win":win_list,
            "ballgame":ballgame_str,
            "transport":transport_list,
            "winrate":winrate_list,
        }
        return render(request,'index.html',{'NBAdata':NBAdata,'datas':list(datas)})


class IndexViews(generic.ListView):
    model = NBAData # 设置后取数据库中的全部数据
    template_name = 'index.html' # 指定模块
    context_object_name = 'GGGG' # 获取数据名字 上下文中使用的变量的名称

    # queryset = NBAData.objects.filter().all()[0:5]  # 如果提供，则 queryset取代所提供的值model。
    #              ||(等价)
    def get_queryset(self):
        '''根据winrate列进行排序从大到小 -winrate 从小到大'''
        return NBAData.objects.order_by('-winrate')

class EastViews(generic.ListView):
    template_name = 'east.html'
    context_object_name = 'GGGG'
    def get_queryset(self):
        return NBAData.objects.filter(area='东部').all()

class WestViews(generic.ListView):
    template_name = 'west.html'
    context_object_name = 'GGGG'
    def get_queryset(self):
        return NBAData.objects.filter(area='西部').all()


class FirstViews(generic.DetailView):
    model = NBAData
    template_name = 'first.html'

    # def get_context_data(self, **kwargs):
        # 如果视图将model属性设置为 User，则默认上下文对象名称user将覆盖上下文处理器中的user变量 所以NBAData --> nbadata
        # context = super().get_context_data(**kwargs) # 重置函数
        # print(context)
        # {'object': <NBAData: 猛龙>, 'nbadata': <NBAData: 猛龙>, 'view': <index.views.FirstViews object at 0x0000016E47A314A8>}
        # return context







def east(request):
    if request.method == "GET":
        sql = "select * from dbo.index_nbadata where area='东部'  order by(winrate) desc"
        datas = NBAData.objects.raw(sql)
        win_list = []
        ballgame_list = []
        transport_list = []
        winrate_list = []
        for x in list(datas):
            win_list.append(x.win)
            ballgame_list.append(x.ballgame.encode('utf-8').decode('utf-8'))
            transport_list.append(x.transport)
            winrate_list.append(float(x.winrate.replace('%','')))

        ballgame_str = '_'.join(ballgame_list)
        datass = list(datas)
        NBAdata = {
            "win":win_list,
            "ballgame":ballgame_str,
            "transport":transport_list,
            "winrate":winrate_list,
        }
        return render(request,'east.html',{'NBAdata':NBAdata,'datas':list(datas)})



def west(request):
    if request.method == "GET":
        sql = "select * from dbo.index_nbadata where area='西部'  order by(winrate) desc"
        datas = NBAData.objects.raw(sql)
        win_list = []
        ballgame_list = []
        transport_list = []
        winrate_list = []
        for x in list(datas):
            win_list.append(x.win)
            ballgame_list.append(x.ballgame.encode('utf-8').decode('utf-8'))
            transport_list.append(x.transport)
            winrate_list.append(float(x.winrate.replace('%','')))


        ballgame_str = '_'.join(ballgame_list)
        datass = list(datas)
        NBAdata = {
            "win":win_list,
            "ballgame":ballgame_str,
            "transport":transport_list,
            "winrate":winrate_list,
        }
        return render(request,'west.html',{'NBAdata':NBAdata,'datas':list(datas)})


def first(request):
    sql = "select * from dbo.index_nbadata order by(winrate) desc;"
    datas = NBAData.objects.raw(sql)
    first = list(datas)[0]
    return render(request,'first.html',{"first":first})


